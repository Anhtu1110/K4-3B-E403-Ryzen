"""Native Discord embeds and interactive components for the TA workflow."""

from __future__ import annotations

from typing import Any

import discord

from case_store import CaseRecord, CaseStore


TOPIC_LABELS = {
    "lab": "Lab & cài đặt",
    "deadline": "Deadline & nộp bài",
    "policy": "Quy chế",
    "attendance": "Điểm danh & workshop",
    "ticket": "Ticket hỗ trợ",
    "team": "Team & ghép nhóm",
    "xp": "Standup & XP",
    "other": "Khác / mơ hồ",
}
STATUS_LABELS = {
    "NEEDS_TA_REVIEW": "CẦN TA REVIEW",
    "UNANSWERED": "CHƯA TRẢ LỜI",
    "IN_REVIEW": "ĐANG XỬ LÝ",
    "RESOLVED": "ĐÃ GIẢI QUYẾT",
    "ESCALATED": "ESCALATED",
    "SNOOZED": "THEO DÕI LẠI",
}


def topic_label(topic: str) -> str:
    return TOPIC_LABELS.get(topic, topic.replace("_", " ").title())


def build_jump_url(case: dict[str, Any]) -> str | None:
    guild, channel, message = str(case.get("guild", "")), str(case.get("channel", "")), str(case.get("msg_id", ""))
    if not all(value.isdigit() for value in (guild, channel, message)):
        return None
    return f"https://discord.com/channels/{guild}/{channel}/{message}"


def build_case_embed(case: dict[str, Any], record: CaseRecord) -> discord.Embed:
    colours = {
        "RESOLVED": discord.Colour.green(),
        "IN_REVIEW": discord.Colour.gold(),
        "SNOOZED": discord.Colour.light_grey(),
        "ESCALATED": discord.Colour.red(),
    }
    colour = colours.get(record.status, discord.Colour.red() if case["status"] == "NEEDS_TA_REVIEW" else discord.Colour.orange())
    hours, minutes = divmod(int(case.get("age_minutes", 0)), 60)
    embed = discord.Embed(
        title=f"{case['case_id']} · {topic_label(record.topic)} · quá {hours}h{minutes:02d}",
        description=f"> {case.get('safe_excerpt') or 'Mở tin gốc để xem nội dung.'}",
        colour=colour,
    )
    embed.add_field(name="Trạng thái", value=STATUS_LABELS.get(record.status, record.status), inline=True)
    embed.add_field(name="AI confidence", value=f"{float(case.get('confidence', 0)):.0%}", inline=True)
    embed.add_field(name="Kênh nguồn", value=f"<#{case['channel']}>", inline=True)
    embed.add_field(name="Vì sao được đưa vào hàng đợi", value=case.get("reason", "Chưa có giải thích")[:1024], inline=False)
    if record.assigned_to:
        embed.add_field(name="TA đang xử lý", value=f"<@{record.assigned_to}>", inline=True)
    embed.set_footer(text="Mở tin gốc để kiểm chứng trước khi kết luận")
    return embed


class QuickReplyModal(discord.ui.Modal, title="Trả lời nhanh vào tin gốc"):
    reply = discord.ui.TextInput(
        label="Nội dung phản hồi",
        style=discord.TextStyle.paragraph,
        placeholder="Nội dung này sẽ được bot gửi dưới dạng reply vào tin nhắn gốc.",
        max_length=1800,
    )

    def __init__(self, parent_view: "CaseActionView") -> None:
        super().__init__()
        self.parent_view = parent_view

    async def on_submit(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=True, thinking=True)
        try:
            channel_id = int(self.parent_view.case["channel"])
            message_id = int(self.parent_view.case["msg_id"])
            channel = interaction.client.get_channel(channel_id)
            if not isinstance(channel, (discord.TextChannel, discord.Thread)):
                raise LookupError("source channel unavailable")
            original = await channel.fetch_message(message_id)
            sent = await original.reply(
                str(self.reply.value).strip(),
                mention_author=False,
                allowed_mentions=discord.AllowedMentions.none(),
            )
        except (LookupError, ValueError, discord.Forbidden, discord.HTTPException, discord.NotFound):
            await interaction.followup.send(
                "Không thể gửi phản hồi vào tin gốc. Kiểm tra tin vẫn tồn tại và bot có quyền View Channel, "
                "Read Message History và Send Messages.",
                ephemeral=True,
            )
            return

        record = self.parent_view.store.transition(
            self.parent_view.case["case_id"],
            self.parent_view.case["topic"],
            "RESOLVED",
            assigned_to=str(interaction.user.id),
        )
        self.parent_view.sync_controls(record)
        if self.parent_view.message:
            await self.parent_view.message.edit(
                embed=build_case_embed(self.parent_view.case, record),
                view=self.parent_view,
            )
        await self.parent_view.audit(interaction, f"quick_replied:{sent.id}")
        await interaction.followup.send(
            "Đã gửi phản hồi dưới dạng reply vào tin gốc và đánh dấu case đã giải quyết.",
            ephemeral=True,
        )


class TopicSelect(discord.ui.Select):
    def __init__(self, parent_view: "CaseActionView") -> None:
        self.parent_view = parent_view
        options = [discord.SelectOption(label=label, value=value) for value, label in TOPIC_LABELS.items()]
        super().__init__(placeholder="Đổi chủ đề nếu AI phân loại sai", options=options, row=1)

    async def callback(self, interaction: discord.Interaction) -> None:
        old_topic = self.parent_view.case["topic"]
        new_topic = self.values[0]
        record = self.parent_view.store.reclassify(self.parent_view.case["case_id"], old_topic, new_topic)
        self.parent_view.case["topic"] = new_topic
        await interaction.response.edit_message(
            embed=build_case_embed(self.parent_view.case, record),
            view=self.parent_view,
        )
        await self.parent_view.audit(interaction, f"reclassified:{old_topic}->{new_topic}")


class CaseActionView(discord.ui.View):
    def __init__(
        self,
        case: dict[str, Any],
        store: CaseStore,
        audit_channel_id: int,
    ) -> None:
        super().__init__(timeout=24 * 60 * 60)
        self.case = case
        self.store = store
        self.audit_channel_id = audit_channel_id
        self.message: discord.Message | None = None
        jump_url = build_jump_url(case)
        if jump_url:
            self.add_item(discord.ui.Button(label="Mở tin gốc", style=discord.ButtonStyle.link, url=jump_url, row=0))
        self.add_item(TopicSelect(self))
        self.sync_controls(store.get(case["case_id"], case["topic"]))

    async def audit(self, interaction: discord.Interaction, action: str) -> None:
        channel = interaction.client.get_channel(self.audit_channel_id)
        if isinstance(channel, discord.TextChannel):
            await channel.send(
                f"case `{self.case['case_id']}` · action `{action}` · actor `{interaction.user.id}` · "
                f"source `{self.case['msg_id']}`"
            )

    def sync_controls(self, record: CaseRecord) -> None:
        self.claim.disabled = record.status in {"IN_REVIEW", "RESOLVED"}
        self.resolve.disabled = record.status == "RESOLVED"
        self.quick_reply.disabled = record.status == "RESOLVED"

    async def update(self, interaction: discord.Interaction, status: str, action: str) -> None:
        record = self.store.transition(
            self.case["case_id"], self.case["topic"], status, assigned_to=str(interaction.user.id)
        )
        self.sync_controls(record)
        await interaction.response.edit_message(
            embed=build_case_embed(self.case, record), view=self
        )
        await self.audit(interaction, action)

    @discord.ui.button(label="Nhận xử lý", style=discord.ButtonStyle.primary, row=0, custom_id="radar:claim")
    async def claim(self, interaction: discord.Interaction, _: discord.ui.Button) -> None:
        await self.update(interaction, "IN_REVIEW", "claimed")

    @discord.ui.button(label="Answer", style=discord.ButtonStyle.success, row=0, custom_id="radar:quick-reply")
    async def quick_reply(self, interaction: discord.Interaction, _: discord.ui.Button) -> None:
        await interaction.response.send_modal(QuickReplyModal(self))

    @discord.ui.button(label=None, emoji="✅", style=discord.ButtonStyle.success, row=0, custom_id="radar:resolve")
    async def resolve(self, interaction: discord.Interaction, _: discord.ui.Button) -> None:
        await self.update(interaction, "RESOLVED", "resolved")

    @discord.ui.button(label="Escalate", style=discord.ButtonStyle.danger, row=0, custom_id="radar:escalate")
    async def escalate(self, interaction: discord.Interaction, _: discord.ui.Button) -> None:
        await self.update(interaction, "ESCALATED", "escalated")
