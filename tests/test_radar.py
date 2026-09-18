import sys
import unittest
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from radar import Message, anon_id, is_announcement, response_candidates  # noqa: E402


def message(msg_id, author, created_at, *, content="Câu hỏi?", reply_to="", channel="channel_01", is_bot=False):
    return Message(msg_id, "K4", channel, author, is_bot, "reply" if reply_to else "message", datetime.strptime(created_at, "%Y-%m-%d %H:%M"), reply_to, content)


class RadarRulesTest(unittest.TestCase):
    def test_announcement_is_filtered(self):
        self.assertTrue(is_announcement(message("M1", "D1", "2026-09-12 09:00", content="@everyone thông báo")))

    def test_anonymisation_is_stable_and_hides_author(self):
        self.assertEqual(anon_id("D4964"), anon_id("D4964"))
        self.assertNotIn("D4964", anon_id("D4964"))

    def test_reply_graph_and_nearby_response_respect_four_hour_window(self):
        question = message("Q", "D1", "2026-09-12 09:00")
        direct = message("R1", "D2", "2026-09-12 09:05", reply_to="Q")
        nearby = message("R2", "D3", "2026-09-12 10:00")
        late = message("R3", "D4", "2026-09-12 13:01")
        results = response_candidates(question, [question, direct, nearby, late], {"Q": [direct]})
        self.assertEqual([item.msg_id for item in results], ["R1", "R2"])


if __name__ == "__main__":
    unittest.main()
