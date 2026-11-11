"""Focused collector-to-durable-index wiring test; no network."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.kraken_prospective_batch import main
from research.test_prospective_outcome_adapter import fixture
from research.prospective_round_store import evaluate_index


class CollectorIndexWiringTests(unittest.TestCase):
    def test_cli_indexes_verified_batch_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            batch = root / "capture"
            index = root / "index.jsonl"

            def fake_collect(pairs, directory):
                self.assertEqual(pairs, ["XBTUSD"])
                Path(directory).mkdir()
                fixture(Path(directory))
                return {"pairs_requested": 1, "pairs_eligible": 1,
                        "pairs_stale": 0, "pairs_invalid": 0,
                        "pairs_budget_skipped": 0}

            argv = ["collector", "--pairs", "XBTUSD",
                    "--output-dir", str(batch), "--round-index", str(index)]
            with patch.object(sys, "argv", argv), patch(
                    "research.kraken_prospective_batch.collect", side_effect=fake_collect):
                main()
            self.assertEqual(len(index.read_text().splitlines()), 1)
            self.assertEqual(evaluate_index(index)["snapshots_verified"], 1)
            self.assertEqual(evaluate_index(index)["qualified_first_entry_episodes"], 0)


if __name__ == "__main__":
    unittest.main()
