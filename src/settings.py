"""Validated runtime configuration for the Discord radar application."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


def _required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value or value.startswith("your_"):
        raise RuntimeError(f"Thiếu biến môi trường {name} trong file .env")
    return value


def _ids(name: str, *, required: bool = True) -> frozenset[int]:
    raw = _required(name) if required else os.getenv(name, "").strip()
    try:
        values = frozenset(int(value.strip()) for value in raw.split(",") if value.strip())
    except ValueError as error:
        raise RuntimeError(f"Biến {name} phải chứa Discord ID dạng số, ngăn cách bằng dấu phẩy") from error
    if required and not values:
        raise RuntimeError(f"Biến {name} chưa có Discord ID")
    return values


@dataclass(frozen=True)
class AppSettings:
    discord_bot_token: str
    discord_guild_id: int
    source_channel_ids: frozenset[int]
    summary_channel_id: int
    audit_channel_id: int
    openai_model: str
    answer_sla_minutes: int
    case_state_path: Path

    @classmethod
    def from_env(cls) -> "AppSettings":
        load_dotenv()
        answer_sla_minutes = int(os.getenv("RADAR_ANSWER_SLA_MINUTES", "240"))
        if not 1 <= answer_sla_minutes <= 10_080:
            raise RuntimeError("RADAR_ANSWER_SLA_MINUTES phải nằm trong khoảng 1..10080")
        return cls(
            discord_bot_token=_required("DISCORD_BOT_TOKEN"),
            discord_guild_id=int(_required("DISCORD_GUILD_ID")),
            source_channel_ids=_ids("DISCORD_SOURCE_CHANNEL_IDS"),
            summary_channel_id=int(_required("DISCORD_SUMMARY_CHANNEL_ID")),
            audit_channel_id=int(_required("DISCORD_AUDIT_CHANNEL_ID")),
            openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini",
            answer_sla_minutes=answer_sla_minutes,
            case_state_path=Path(os.getenv("DISCORD_CASE_STATE_PATH", "artifacts/case-state.json")),
        )
