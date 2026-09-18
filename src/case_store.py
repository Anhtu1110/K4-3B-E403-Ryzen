"""Small persistent state store for TA case workflow.

The store is intentionally independent from Discord so transitions can be tested
without a network connection. Writes are atomic to avoid a partial JSON file.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class CaseRecord:
    case_id: str
    topic: str
    status: str = "NEEDS_TA_REVIEW"
    assigned_to: str | None = None
    updated_at: str = ""


class CaseStore:
    def __init__(self, path: Path | None = None) -> None:
        self.path = path
        self._records: dict[str, CaseRecord] = {}
        self._load()

    def _load(self) -> None:
        if not self.path or not self.path.exists():
            return
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        records = payload.get("cases", [])
        # Drafting is no longer part of the workflow.  Preserve old state files
        # but return their pending cases to the queue rather than leaving them
        # in an obsolete DRAFTED status.
        for item in records:
            if item.get("status") == "DRAFTED":
                item["status"] = "NEEDS_TA_REVIEW"
            item.pop("draft_reply", None)
        self._records = {item["case_id"]: CaseRecord(**item) for item in records}

    def _save(self) -> None:
        if not self.path:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        payload = {"cases": [asdict(item) for item in self._records.values()]}
        temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        temporary.replace(self.path)

    def get(self, case_id: str, topic: str) -> CaseRecord:
        record = self._records.get(case_id)
        if record is None:
            record = CaseRecord(case_id=case_id, topic=topic, updated_at=self._timestamp())
            self._records[case_id] = record
            self._save()
        return record

    def find(self, case_id: str) -> CaseRecord | None:
        """Return an existing case without creating or persisting a new record."""
        return self._records.get(case_id)

    def transition(
        self,
        case_id: str,
        topic: str,
        status: str,
        *,
        assigned_to: str | None = None,
    ) -> CaseRecord:
        record = self.get(case_id, topic)
        record.status = status
        if assigned_to is not None:
            record.assigned_to = assigned_to
        record.updated_at = self._timestamp()
        self._save()
        return record

    def reclassify(self, case_id: str, current_topic: str, new_topic: str) -> CaseRecord:
        record = self.get(case_id, current_topic)
        record.topic = new_topic
        record.updated_at = self._timestamp()
        self._save()
        return record

    @staticmethod
    def _timestamp() -> str:
        return datetime.now(timezone.utc).isoformat(timespec="seconds")
