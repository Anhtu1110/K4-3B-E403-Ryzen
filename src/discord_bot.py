"""Discord adapter for AI Daily Question Radar.

TA invokes /daily-radar to scan configured Discord channels. The bot posts an
anonymised queue to the TA channel and only replies after a TA submits a Quick
Reply action.
"""

from __future__ import annotations

import asyncio
from datetime import datetime, timedelta

import discord
from discord import app_commands

from case_store import CaseStore
from discord_ui import CaseActionView, build_case_embed, build_summary_embed
from radar import Message, SemanticClassifier, build_report
from settings import AppSettings

def to_radar_message(message: discord.Message) -> Message:
    return Message(
        msg_id=str(message.id),
        guild=str(message.guild.id),
        channel=str(message.channel.id),
        author=str(message.author.id),
        is_bot=message.author.bot,
        msg_type="reply" if message.reference and message.reference.message_id else "message",
        created_at=message.created_at.replace(tzinfo=None),
        reply_to=str(message.reference.message_id) if message.reference and message.reference.message_id else "",
        content=message.content,
    )


class RadarBot(discord.Client):
    def __init__(self, settings: AppSettings) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        super().__init__(intents=intents)
        self.settings = settings
        self.tree = app_commands.CommandTree(self)
        self.case_store = CaseStore(settings.case_state_path)
        self._register_commands()

    def _register_commands(self) -> None:
        @self.tree.command(
            name="daily-radar",
            description="Quét câu hỏi tồn và đăng hàng đợi tương tác cho TA.",
        )
        @app_commands.describe(
            before_hours="Quét các tin trong N giờ trước thời điểm hiện tại, từ 1 đến 72; mặc định 24",
        )
        async def daily_radar(
            interaction: discord.Interaction,
            before_hours: app_commands.Range[int, 1, 72] = 24,
        ) -> None:
            await self.run_daily_radar(interaction, before_hours=before_hours)

    async def setup_hook(self) -> None:
        guild = discord.Object(id=self.settings.discord_guild_id)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

    async def on_ready(self) -> None:
        print(
            f"Logged in as {self.user} · /daily-radar synced to guild "
            f"{self.settings.discord_guild_id}",
            flush=True,
        )

    async def fetch_source_messages(self, before_hours: int) -> list[Message]:
        after = discord.utils.utcnow() - timedelta(hours=before_hours)
        records: list[Message] = []
        for channel_id in self.settings.source_channel_ids:
            channel = self.get_channel(channel_id)
            if not isinstance(channel, (discord.TextChannel, discord.Thread)):
                raise RuntimeError(
                    f"Không thấy text channel/thread nguồn {channel_id}; kiểm tra ID và quyền View Channel."
                )
            async for message in channel.history(after=after, oldest_first=True, limit=None):
                records.append(to_radar_message(message))
        return sorted(records, key=lambda item: item.created_at)

    async def run_daily_radar(
        self,
        interaction: discord.Interaction,
        *,
        before_hours: int,
    ) -> None:
        # Discord invalidates an unacknowledged interaction after a few seconds.
        # Acknowledge first so permission checks and downstream I/O cannot race
        # that deadline on a busy gateway connection.
        await interaction.response.defer(ephemeral=True, thinking=True)
        if interaction.guild_id != self.settings.discord_guild_id:
            await interaction.followup.send(
                "Lệnh chỉ được chạy trong server đã cấu hình.", ephemeral=True
            )
            return
        try:
            as_of = datetime.utcnow()
            messages = await self.fetch_source_messages(before_hours)
            if not messages:
                await interaction.followup.send(
                    "Không có tin nhắn trong cửa sổ đã chọn.",
                    ephemeral=True,
                )
                return

            classifier = SemanticClassifier(self.settings.openai_model)
            report = await asyncio.to_thread(
                build_report,
                messages,
                classifier,
                as_of,
                0.85,
                answer_sla_minutes=self.settings.answer_sla_minutes,
            )
            summary_channel = self.get_channel(self.settings.summary_channel_id)
            audit_channel = self.get_channel(self.settings.audit_channel_id)
            if not isinstance(summary_channel, discord.TextChannel):
                raise RuntimeError("Không tìm thấy summary channel; kiểm tra ID và quyền bot.")
            if not isinstance(audit_channel, discord.TextChannel):
                raise RuntimeError("Không tìm thấy audit channel; kiểm tra ID và quyền bot.")

            await summary_channel.send(
                embed=build_summary_embed(report, len(messages))
            )
            actionable = [
                item
                for item in report["decisions"]
                if item["status"] in {"NEEDS_TA_REVIEW", "UNANSWERED"}
            ]
            actionable.sort(
                key=lambda item: (
                    item["status"] != "NEEDS_TA_REVIEW",
                    -int(item.get("age_minutes", 0)),
                )
            )
            for case in actionable[: self.settings.max_case_cards]:
                record = self.case_store.get(case["case_id"], case["topic"])
                view = CaseActionView(
                    case,
                    self.case_store,
                    self.settings.audit_channel_id,
                )
                message = await summary_channel.send(
                    embed=build_case_embed(case, record), view=view
                )
                view.message = message

            await audit_channel.send(
                f"radar_run · actor `{interaction.user.id}` · scanned `{len(messages)}` · "
                f"posted `{min(len(actionable), self.settings.max_case_cards)}` · "
                f"result `{report['summary']}`"
            )
            await interaction.followup.send(
                f"Đã kết nối và đăng bản tin vào <#{self.settings.summary_channel_id}>. "
                f"Có `{len(actionable)}` case cần chú ý; đã hiển thị tối đa "
                f"`{self.settings.max_case_cards}` case.",
                ephemeral=True,
            )
        except Exception as error:
            await interaction.followup.send(
                f"Radar chưa chạy: `{type(error).__name__}: {error}`", ephemeral=True
            )


def main() -> None:
    settings = AppSettings.from_env()
    RadarBot(settings).run(settings.discord_bot_token)


if __name__ == "__main__":
    main()
