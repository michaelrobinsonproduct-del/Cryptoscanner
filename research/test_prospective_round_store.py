import json
import tempfile
import unittest
from pathlib import Path

from research.prospective_round_store import append_round, evaluate_index
from research.test_prospective_outcome_adapter import fixture


class RoundStoreTests(unittest.TestCase):
    def test_durable_append_and_incomplete_outcomes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            index = root / "rounds.jsonl"
            for i in range(2):
                batch = root / ("batch" + str(i))
                batch.mkdir()
                fixture(batch)
                record = append_round(index, batch)
                self.assertEqual(record["snapshots_verified"], 1)
            self.assertEqual(len(index.read_text().splitlines()), 2)
            result = evaluate_index(index)
            self.assertEqual(result["rounds_verified"], 2)
            self.assertEqual(result["snapshots_verified"], 2)
            self.assertEqual(result["qualified_first_entry_episodes"], 0)

    def test_duplicate_append_rejected_without_extra_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch = root / "batch"
            batch.mkdir()
            fixture(batch)
            index = root / "rounds.jsonl"
            append_round(index, batch)
            with self.assertRaisesRegex(ValueError, "duplicate batch"):
                append_round(index, batch)
            self.assertEqual(len(index.read_text().splitlines()), 1)

    def test_mutated_manifest_rejected_on_readback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch = root / "batch"
            batch.mkdir()
            fixture(batch)
            index = root / "rounds.jsonl"
            append_round(index, batch)
            manifest = batch / "manifest.json"
            manifest.write_text(manifest.read_text() + " ")
            with self.assertRaisesRegex(ValueError, "manifest changed"):
                evaluate_index(index)


if __name__ == "__main__":
    unittest.main()
