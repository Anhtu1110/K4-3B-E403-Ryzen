import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from case_store import CaseRecord, CaseStore  # noqa: E402
from discord_ui import CaseActionView, build_case_embed, build_jump_url  # noqa: E402


class DiscordUiTest(unittest.TestCase):
    def setUp(self):
        self.case = {
            "case_id": "CASE-ABC123",
            "msg_id": "123",
            "guild": "456",
            "channel": "789",
            "status": "NEEDS_TA_REVIEW",
            "topic": "deadline",
            "age_minutes": 372,
            "confidence": 0.61,
            "safe_excerpt": "Cái link bài 2 bị lỗi",
            "reason": "Liên quan deadline và chưa có phản hồi",
        }

    def test_case_embed_contains_actionable_context_without_author(self):
        record = CaseRecord(case_id="CASE-ABC123", topic="deadline")
        embed = build_case_embed(self.case, record)
        payload = embed.to_dict()
        rendered = str(payload)
        self.assertIn("CASE-ABC123", rendered)
        self.assertIn("61%", rendered)
        self.assertNotIn("anon_hv_id", rendered)

    def test_jump_url_targets_source_message(self):
        self.assertEqual(build_jump_url(self.case), "https://discord.com/channels/456/789/123")

    def test_view_has_answer_and_no_draft(self):
        view = CaseActionView(self.case, CaseStore(), audit_channel_id=1)
        labels = {item.label for item in view.children if hasattr(item, "label")}

        self.assertIn("Answer", labels)
        self.assertNotIn("Soạn nháp", labels)
        self.assertEqual(str(view.resolve.emoji), "✅")
        view.stop()

if __name__ == "__main__":
    unittest.main()
