"""Resolve human-readable Discord placeholders in .env to snowflake IDs.

Supported placeholders:
  DISCORD_GUILD_ID=ID_server_Mini_Hackathon
  DISCORD_SOURCE_CHANNEL_IDS=ID_general,ID_homework_help

The command only writes these two keys after unique guild/channel matches are
found. It never prints the bot token or resolved IDs.
"""

from __future__ import annotations

import os
from pathlib import Path

import discord
from dotenv import load_dotenv


ENV_PATH = Path(".env")


def replace_env_values(path: Path, replacements: dict[str, str]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    seen: set[str] = set()
    updated: list[str] = []
    for line in lines:
        key = line.split("=", 1)[0].strip() if "=" in line else ""
        if key in replacements:
            updated.append(f"{key}={replacements[key]}")
            seen.add(key)
        else:
            updated.append(line)
    for key, value in replacements.items():
        if key not in seen:
            updated.append(f"{key}={value}")
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text("\n".join(updated) + "\n", encoding="utf-8")
    temporary.replace(path)


class ConfigureClient(discord.Client):
    def __init__(self, guild_name: str, source_names: list[str]) -> None:
        intents = discord.Intents.default()
        intents.guilds = True
        super().__init__(intents=intents)
        self.guild_name = guild_name
        self.source_names = source_names
        self.failure: str | None = None

    async def on_ready(self) -> None:
        guild_matches = [guild for guild in self.guilds if guild.name == self.guild_name]
        if len(guild_matches) != 1:
            self.failure = (
                f"Cần đúng 1 guild tên {self.guild_name!r}, nhưng bot nhìn thấy {len(guild_matches)}."
            )
            await self.close()
            return
        guild = guild_matches[0]
        resolved_channels: list[discord.TextChannel] = []
        for name in self.source_names:
            matches = [channel for channel in guild.text_channels if channel.name == name]
            if len(matches) != 1:
                self.failure = f"Cần đúng 1 text channel #{name}, nhưng tìm thấy {len(matches)}."
                await self.close()
                return
            resolved_channels.append(matches[0])

        replace_env_values(
            ENV_PATH,
            {
                "DISCORD_GUILD_ID": str(guild.id),
                "DISCORD_SOURCE_CHANNEL_IDS": ",".join(str(channel.id) for channel in resolved_channels),
            },
        )
        print(f"CONFIGURED guild={guild.name} sources={','.join('#' + item.name for item in resolved_channels)}")
        await self.close()


def main() -> int:
    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN", "").strip()
    guild_value = os.getenv("DISCORD_GUILD_ID", "").strip()
    source_value = os.getenv("DISCORD_SOURCE_CHANNEL_IDS", "").strip()
    if not token:
        raise RuntimeError("Thiếu DISCORD_BOT_TOKEN")
    if guild_value.isdigit() and all(value.strip().isdigit() for value in source_value.split(",")):
        print("CONFIGURATION ALREADY NUMERIC")
        return 0
    if not guild_value.startswith("ID_server_"):
        raise RuntimeError("Guild placeholder phải có dạng ID_server_<tên-server>")
    raw_sources = [item.strip() for item in source_value.split(",") if item.strip()]
    if not raw_sources or not all(item.startswith("ID_") for item in raw_sources):
        raise RuntimeError("Source placeholders phải có dạng ID_<tên-channel>, ngăn cách bằng dấu phẩy")

    guild_name = guild_value.removeprefix("ID_server_")
    source_names = [item.removeprefix("ID_").replace("_", "-") for item in raw_sources]
    client = ConfigureClient(guild_name, source_names)
    client.run(token, log_handler=None)
    if client.failure:
        print(f"CONFIGURATION FAILED: {client.failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
