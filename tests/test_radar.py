import sys
import unittest
import json
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from radar import (  # noqa: E402
    Message,
    SemanticClassifier,
    anon_id,
    case_id,
    build_report,
    is_announcement,
    mask_sensitive_text,
    response_candidates,
)


def message(msg_id, author, created_at, *, content="Câu hỏi?", reply_to="", channel="channel_01", is_bot=False):
    return Message(msg_id, "K4", channel, author, is_bot, "reply" if reply_to else "message", datetime.strptime(created_at, "%Y-%m-%d %H:%M"), reply_to, content)


class RadarRulesTest(unittest.TestCase):
    def test_announcement_is_filtered(self):
        self.assertTrue(is_announcement(message("M1", "D1", "2026-09-12 09:00", content="@everyone thông báo")))

    def test_anonymisation_is_stable_and_hides_author(self):
        self.assertEqual(anon_id("D4964"), anon_id("D4964"))
        self.assertNotIn("D4964", anon_id("D4964"))
        self.assertEqual(case_id("123"), case_id("123"))
        self.assertNotIn("123", case_id("123"))

    def test_sensitive_text_is_masked_before_ai_or_ui(self):
        masked = mask_sensitive_text(
            "Nhờ <@123456789012345678> xem https://example.com và email a@b.com, sđt 0912345678"
        )
        self.assertNotIn("123456789012345678", masked)
        self.assertNotIn("https://example.com", masked)
        self.assertNotIn("a@b.com", masked)
        self.assertNotIn("0912345678", masked)

    def test_reply_graph_and_nearby_response_respect_sla_window(self):
        question = message("Q", "D1", "2026-09-12 09:00")
        direct = message("R1", "D2", "2026-09-12 09:05", reply_to="Q")
        nearby = message("R2", "D3", "2026-09-12 10:00")
        late = message("R3", "D4", "2026-09-12 13:01")
        results = response_candidates(question, [question, direct, nearby, late], {"Q": [direct]})
        self.assertEqual([item.msg_id for item in results], ["R1", "R2"])

        two_minute_results = response_candidates(
            question, [question, direct, nearby, late], {"Q": [direct]}, answer_sla_minutes=2
        )
        self.assertEqual([item.msg_id for item in two_minute_results], ["R1"])

    def test_classifier_retries_only_message_ids_missing_from_a_response(self):
        class PartialResponseClassifier(SemanticClassifier):
            model = "test"

            def __init__(self):
                self.calls = []

            def _json(self, instructions, input_text, schema_name, schema):
                message_ids = [item["msg_id"] for item in json.loads(input_text)]
                self.calls.append((message_ids, schema))
                returned_ids = message_ids[:1]
                return {"items": [
                    {
                        "msg_id": msg_id,
                        "is_question": False,
                        "topic": "other",
                        "intent_key": "không phải câu hỏi",
                        "confidence": 1.0,
                        "needs_official_source": False,
                        "reason": "test",
                    }
                    for msg_id in returned_ids
                ]}

        classifier = PartialResponseClassifier()
        candidates = [
            message("Q1", "D1", "2026-09-12 09:00"),
            message("Q2", "D2", "2026-09-12 09:01"),
        ]

        result = classifier.classify_questions(candidates)

        self.assertEqual(set(result), {"Q1", "Q2"})
        self.assertEqual([call[0] for call in classifier.calls], [["Q1", "Q2"], ["Q2"]])
        first_schema = classifier.calls[0][1]
        self.assertEqual(first_schema["properties"]["items"]["minItems"], 2)
        self.assertEqual(first_schema["properties"]["items"]["maxItems"], 2)
        self.assertEqual(
            first_schema["properties"]["items"]["items"]["properties"]["msg_id"]["enum"],
            ["Q1", "Q2"],
        )

    def test_direct_reply_excludes_question_before_classification(self):
        class FailIfClassified:
            model = "test"

            def classify_questions(self, candidates):
                if candidates:
                    raise AssertionError("A directly replied question must not be classified")
                return {}

            def answer_adequacy(self, question, replies):
                raise AssertionError("A directly replied question must not be assessed")

        question = message("Q1", "D1", "2026-09-12 09:00")
        reply = message("R1", "D2", "2026-09-12 09:01", reply_to="Q1")
        report = build_report(
            [question, reply],
            FailIfClassified(),
            datetime.strptime("2026-09-12 10:00", "%Y-%m-%d %H:%M"),
            0.85,
        )

        self.assertEqual(report["decisions"], [])
        self.assertIn(
            {"msg_id": "Q1", "result": "DIRECT_REPLY_EXISTS", "reply_msg_ids": ["R1"]},
            report["audit"],
        )

    def test_duplicate_source_message_is_classified_once(self):
        class OneQuestionClassifier:
            model = "test"

            def classify_questions(self, candidates):
                self.seen_ids = [item.msg_id for item in candidates]
                return {
                    item.msg_id: {
                        "is_question": True,
                        "topic": "lab",
                        "intent_key": "lỗi cài đặt",
                        "confidence": 1.0,
                        "needs_official_source": False,
                        "reason": "cần hỗ trợ",
                    }
                    for item in candidates
                }

            def answer_adequacy(self, question, replies):
                return {"answered": False, "adequate_reply_ids": [], "reason": "no reply"}

        classifier = OneQuestionClassifier()
        question = message("Q1", "D1", "2026-09-12 09:00")
        report = build_report(
            [question, question],
            classifier,
            datetime.strptime("2026-09-12 10:00", "%Y-%m-%d %H:%M"),
            0.85,
        )

        self.assertEqual(classifier.seen_ids, ["Q1"])
        self.assertEqual(len(report["decisions"]), 1)
        self.assertIn({"msg_id": "Q1", "result": "DUPLICATE_SOURCE_MESSAGE"}, report["audit"])


if __name__ == "__main__":
    unittest.main()
