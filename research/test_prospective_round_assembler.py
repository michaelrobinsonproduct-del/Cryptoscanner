"""Focused E1 tests for actual source-verified multi-round coverage."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from research.test_prospective_outcome_adapter import fixture
from research.prospective_round_assembler import evaluate_rounds


class RoundAssemblerTests(unittest.TestCase):
    def test_two_independent_rounds_do_not_fabricate_twelve_slots(self):
        with tempfile.TemporaryDirectory() as tmp:
            roots = [Path(tmp) / str(i) for i in range(2)]
            for i, root in enumerate(roots):
                root.mkdir()
                _, evidence = fixture(root)
                evidence["depth_receipt"]["first_observed_at"] += i * 300
                evidence["bid_level_event_at"] = str(1700000000 + i * 300)
                evidence["ask_level_event_at"] = str(1700000000 + i * 300)
                (root / "00-XBTUSD-evidence.json").write_text(json.dumps(evidence))
            result = evaluate_rounds(roots)
            self.assertEqual(result["rounds_verified"], 2)
            self.assertEqual(result["snapshots_verified"], 2)
            self.assertEqual(result["qualified_first_entry_episodes"], 0)
            self.assertTrue(all(o["status"] == "ABSTAIN_INCOMPLETE" for o in result["outcomes"]))

    def test_thirteen_source_verified_receipts_produce_one_mature_one_hour_label(self):
        with tempfile.TemporaryDirectory() as tmp:
            roots = []
            for i in range(13):
                root = Path(tmp) / str(i)
                root.mkdir()
                _, evidence = fixture(root)
                evidence["depth_receipt"]["first_observed_at"] = 1700000002 + i * 300
                evidence["bid_level_event_at"] = str(1700000000 + i * 300)
                evidence["ask_level_event_at"] = str(1700000000 + i * 300)
                (root / "00-XBTUSD-evidence.json").write_text(json.dumps(evidence))
                roots.append(root)
            result = evaluate_rounds(roots, 1)
            qualified = [o for o in result["outcomes"]
                         if o["status"] == "QUALIFIED_OBSERVED_PATH"]
            self.assertEqual(result["snapshots_verified"], 13)
            self.assertEqual(result["qualified_first_entry_episodes"], 1)
            self.assertEqual(len(qualified), 1)
            self.assertFalse(qualified[0]["ge30pct"])
            self.assertEqual(len(result["outcomes"]) - len(qualified), 12)

    def test_complete_577_receipt_path_is_evaluable_at_48_hours(self):
        rows = []
        for i in range(577):
            observed = 1700000002 + i * 300
            rows.append({"pair": "XBTUSD", "first_observed_at": observed,
                         "event_at": observed - 2,
                         "source_sha256": format(i+1, "064x"),
                         "ask": "100", "bid": "99", "entry_liquidity_usd": 100.0})
        with patch("research.prospective_round_assembler.verified_rows",
                   side_effect=lambda batch: ([rows[int(batch)]], [])):
            report = evaluate_rounds([str(i) for i in range(577)], 48)
        self.assertEqual(report["snapshots_verified"], 577)
        self.assertEqual(report["qualified_first_entry_episodes"], 1)
        self.assertEqual(report["outcomes"][0]["status"], "QUALIFIED_OBSERVED_PATH")
        self.assertEqual(report["outcomes"][0]["forward_slots"], 576)

    def test_mutated_second_round_fails_entire_evidence_set(self):
        with tempfile.TemporaryDirectory() as tmp:
            roots = [Path(tmp) / str(i) for i in range(2)]
            for root in roots:
                root.mkdir()
                fixture(root)
            (roots[1] / "00-XBTUSD-depth.json").write_bytes(b"tampered")
            with self.assertRaisesRegex(ValueError, "raw receipt mismatch"):
                evaluate_rounds(roots)

    def test_duplicate_round_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            with self.assertRaisesRegex(ValueError, "duplicate batch"):
                evaluate_rounds([root, root])


if __name__ == "__main__":
    unittest.main()
