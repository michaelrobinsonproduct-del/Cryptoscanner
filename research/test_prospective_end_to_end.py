"""E1 end-to-end fixture tests: actual receipt cadence, quote-update drift, gaps."""
import json
import tempfile
import unittest
from pathlib import Path

from research.test_prospective_outcome_adapter import fixture
from research.prospective_round_store import append_round, evaluate_index


class EndToEndObservedRounds(unittest.TestCase):
    def _round(self, root, number, *, skip=False, price="99"):
        batch = root / ("round-%02d" % number)
        batch.mkdir()
        _, evidence = fixture(batch)
        # Factual capture times are five minutes apart. Kraken best-level
        # updates occur at different event times and MUST NOT be rounded.
        evidence["depth_receipt"]["first_observed_at"] = 1700000002 + 300 * number
        evidence["bid_level_event_at"] = str(1699999998 + 300 * number + (number % 4))
        evidence["ask_level_event_at"] = str(1699999999 + 300 * number + (number % 3))
        evidence["best_bid"] = price
        (batch / "00-XBTUSD-evidence.json").write_text(json.dumps(evidence))
        if not skip:
            append_round(root / "rounds.jsonl", batch)
        return batch

    def test_thirteen_real_receipt_slots_can_qualify_positive(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for i in range(13):
                self._round(root, i, price="131" if i == 7 else "99")
            result = evaluate_index(root / "rounds.jsonl")
            self.assertEqual(result["snapshots_verified"], 13)
            self.assertEqual(result["qualified_first_entry_episodes"], 1)
            qualified = [o for o in result["outcomes"]
                         if o["status"] == "QUALIFIED_OBSERVED_PATH"]
            self.assertTrue(qualified[0]["ge30pct"])

    def test_missing_capture_round_abstains(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for i in range(13):
                if i != 5:
                    self._round(root, i)
            result = evaluate_index(root / "rounds.jsonl")
            self.assertEqual(result["qualified_first_entry_episodes"], 0)


if __name__ == "__main__":
    unittest.main()
