"""Discord adapter for Daily Question Radar.

The bot only runs analysis after a TA invokes /daily-radar. It reads configured
public demo channels, posts the anonymised result to the configured TA channel,
and never sends automatic answers to students.
"""

from __future__ import annotations

import asyncio
import os
from datetime import datetime, timedelta

import discord
from discord import app_commands
from dotenv import load_dotenv

from radar import Message, SemanticClassifier, build_report

load_dotenv()


def required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value or value.startswith("your_"):
        raise RuntimeError(f"Thiếu biến môi trường {name} trong file .env")
    return value


TOKEN = required("DISCORD_BOT_TOKEN")
GUILD_ID = int(required("DISCORD_GUILD_ID"))
SOURCE_CHANNEL_IDS = {int(value) for value in required("DISCORD_SOURCE_CHANNEL_IDS").split(",") if value.strip()}
SUMMARY_CHANNEL_ID = int(required("DISCORD_SUMMARY_CHANNEL_ID"))
AUDIT_CHANNEL_ID = int(required("DISCORD_AUDIT_CHANNEL_ID"))
TA_ROLE_IDS = {int(value) for value in os.getenv("DISCORD_TA_ROLE_IDS", "").split(",") if value.strip()}
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


def to_radar_message(message: discord.Message) -> Message:
    return Message(
        msg_id=str(message.id), guild=str(message.guild.id), channel=str(message.channel.id),
        author=str(message.author.id), is_bot=message.author.bot,
        msg_type="reply" if message.reference and message.reference.message_id else "message",
        created_at=message.created_at.replace(tzinfo=None),
        reply_to=str(message.reference.message_id) if message.reference and message.reference.message_id else "",
        content=message.content,
    )


async def fetch_source_messages(hours: int) -> list[Message]:
    after = discord.utils.utcnow() - timedelta(hours=hours)
    records: list[Message] = []
    for channel_id in SOURCE_CHANNEL_IDS:
        channel = client.get_channel(channel_id)
        if not isinstance(channel, discord.TextChannel):
            raise RuntimeError(f"Không thấy text channel nguồn {channel_id}; kiểm tra ID và quyền View Channel.")
        async for message in channel.history(after=after, oldest_first=True, limit=None):
            records.append(to_radar_message(message))
    return sorted(records, key=lambda item: item.created_at)


def can_run(interaction: discord.Interaction) -> bool:
    member = interaction.user
    if not isinstance(member, discord.Member):
        return False
    if member.guild_permissions.administrator or member.guild_permissions.manage_guild:
        return True
    return bool(TA_ROLE_IDS and any(role.id in TA_ROLE_IDS for role in member.roles))


def summary_embed(report: dict) -> discord.Embed:
    summary = report["summary"]
    embed = discord.Embed(
        title="Daily Question Radar",
        description=(
            f"**Chưa trả lời:** {summary['UNANSWERED']}  ·  "
            f"**Cần TA xem lại:** {summary['NEEDS_TA_REVIEW']}  ·  "
            f"**Đã trả lời:** {summary['ANSWERED']}\n"
            f"Không tính `{summary['WAITING']}` tin chưa đủ 4 giờ. Tất cả ID học viên đã ẩn danh."
        ),
        colour=discord.Colour.orange(),
        timestamp=discord.utils.utcnow(),
    )
    urgent = [item for item in report["clusters"] if item["status"] == "NEEDS_TA_REVIEW"]
    backlog = [item for item in report["clusters"] if item["status"] == "UNANSWERED"]
    for label, clusters in [("CẦN TA KIỂM TRA", urgent), ("BACKLOG THEO CHỦ ĐỀ", backlog)]:
        if not clusters:
            embed.add_field(name=label, value="Không có", inline=False)
            continue
        lines = [f"• **{item['topic']}** — {item['count']} tin: {item['intent_key']}" for item in clusters[:8]]
        embed.add_field(name=label, value="\n".join(lines)[:1024], inline=False)
    embed.set_footer(text="AI chỉ hỗ trợ phân loại; TA kiểm chứng deadline/quy chế trước khi trả lời.")
    return embed


@tree.command(name="daily-radar", description="Quét câu hỏi tồn trong các kênh demo và gửi summary cho TA.")
@app_commands.describe(hours="Số giờ cần quét, từ 4 đến 72; mặc định 24")
async def daily_radar(interaction: discord.Interaction, hours: app_commands.Range[int, 4, 72] = 24) -> None:
    if interaction.guild_id != GUILD_ID:
        await interaction.response.send_message("Lệnh chỉ được chạy trong server demo đã cấu hình.", ephemeral=True)
        return
    if not can_run(interaction):
        await interaction.response.send_message("Chỉ TA/Mod hoặc người quản lý server được chạy lệnh này.", ephemeral=True)
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        messages = await fetch_source_messages(hours)
        if not messages:
            await interaction.followup.send("Không có tin nhắn trong cửa sổ đã chọn.", ephemeral=True)
            return
        report = await asyncio.to_thread(
            build_report, messages, SemanticClassifier(MODEL), datetime.utcnow(), 0.85
        )
        summary_channel = client.get_channel(SUMMARY_CHANNEL_ID)
        audit_channel = client.get_channel(AUDIT_CHANNEL_ID)
        if not isinstance(summary_channel, discord.TextChannel) or not isinstance(audit_channel, discord.TextChannel):
            raise RuntimeError("Không tìm thấy summary/audit channel; kiểm tra ID và quyền bot.")
        await summary_channel.send(embed=summary_embed(report))
        await audit_channel.send(
            f"Radar run by `{interaction.user.id}` · scanned `{len(messages)}` messages · "
            f"result: `{report['summary']}`"
        )
        await interaction.followup.send("Đã đăng summary vào #ta-daily-summary và log vào #radar-audit.", ephemeral=True)
    except Exception as error:
        await interaction.followup.send(f"Radar chưa chạy: `{type(error).__name__}: {error}`", ephemeral=True)


@client.event
async def on_ready() -> None:
    guild = discord.Object(id=GUILD_ID)
    tree.copy_global_to(guild=guild)
    await tree.sync(guild=guild)
    print(f"Logged in as {client.user} · /daily-radar synced to guild {GUILD_ID}")


client.run(TOKEN)
