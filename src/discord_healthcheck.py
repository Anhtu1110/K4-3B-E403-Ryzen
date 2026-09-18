"""Read-only Discord connectivity and permission check.

This script logs the bot in, validates configured guild/channels/permissions,
prints a compact result, and disconnects without posting any message.
"""

from __future__ import annotations

import discord

from settings import AppSettings


class HealthcheckClient(discord.Client):
    def __init__(self, settings: AppSettings) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        super().__init__(intents=intents)
        self.settings = settings
        self.failures: list[str] = []

    async def on_ready(self) -> None:
        guild = self.get_guild(self.settings.discord_guild_id)
        if guild is None:
            self.failures.append("Bot không nhìn thấy guild đã cấu hình")
            await self.close()
            return
        member = guild.me
        if member is None:
            self.failures.append("Không lấy được bot member trong guild")
            await self.close()
            return

        print(f"CONNECTED bot={self.user} guild={guild.name}")
        for channel_id in sorted(self.settings.source_channel_ids):
            channel = self.get_channel(channel_id)
            if not isinstance(channel, (discord.TextChannel, discord.Thread)):
                self.failures.append(f"source channel {channel_id}: không tìm thấy hoặc sai loại")
                continue
            permissions = channel.permissions_for(member)
            ok = permissions.view_channel and permissions.read_message_history
            print(f"SOURCE #{channel.name}: view/read_history={'OK' if ok else 'MISSING'}")
            if not ok:
                self.failures.append(f"source #{channel.name}: thiếu View Channel/Read Message History")

        for label, channel_id in (
            ("SUMMARY", self.settings.summary_channel_id),
            ("AUDIT", self.settings.audit_channel_id),
        ):
            channel = self.get_channel(channel_id)
            if not isinstance(channel, discord.TextChannel):
                self.failures.append(f"{label.lower()} channel {channel_id}: không tìm thấy hoặc sai loại")
                continue
            permissions = channel.permissions_for(member)
            ok = permissions.view_channel and permissions.send_messages and permissions.embed_links
            print(f"{label} #{channel.name}: view/send/embed={'OK' if ok else 'MISSING'}")
            if not ok:
                self.failures.append(f"{label.lower()} #{channel.name}: thiếu View/Send/Embed Links")

        print(f"MESSAGE_CONTENT_INTENT configured={'YES' if self.intents.message_content else 'NO'}")
        await self.close()


def main() -> int:
    settings = AppSettings.from_env()
    client = HealthcheckClient(settings)
    client.run(settings.discord_bot_token, log_handler=None)
    if client.failures:
        print("HEALTHCHECK FAILED")
        for failure in client.failures:
            print(f"- {failure}")
        return 1
    print("HEALTHCHECK PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
