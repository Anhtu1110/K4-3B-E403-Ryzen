import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from case_store import CaseStore  # noqa: E402


class CaseStoreTest(unittest.TestCase):
    def test_transitions_and_reclassification_are_persisted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "case-state.json"
            store = CaseStore(path)
            claimed = store.transition("CASE-001", "deadline", "IN_REVIEW", assigned_to="42")
            self.assertEqual(claimed.assigned_to, "42")
            store.reclassify("CASE-001", "deadline", "policy")

            reloaded = CaseStore(path).get("CASE-001", "deadline")
            self.assertEqual(reloaded.status, "IN_REVIEW")
            self.assertEqual(reloaded.topic, "policy")
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["cases"][0]["case_id"], "CASE-001")

    def test_find_does_not_create_a_case(self):
        store = CaseStore()

        self.assertIsNone(store.find("CASE-unknown"))


if __name__ == "__main__":
    unittest.main()
