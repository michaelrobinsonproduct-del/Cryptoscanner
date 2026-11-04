"""Focused E1 tests for actual source-verified multi-round coverage."""
import json
import tempfile
import unittest
from pathlib import Path
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
