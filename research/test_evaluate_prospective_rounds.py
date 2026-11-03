"""CLI acceptance: independent source batches retained across separate jobs."""
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from research.evaluate_prospective_rounds import main
from research.test_prospective_outcome_adapter import fixture


class MultiJobEvaluationTests(unittest.TestCase):
    def test_append_independent_batches_then_read_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            index = root / "rounds.jsonl"
            batches = []
            for number in range(2):
                batch = root / ("capture-%d" % number)
                batch.mkdir()
                fixture(batch)
                batches.append(batch)
            with redirect_stdout(io.StringIO()) as output:
                with patch.object(sys, "argv", ["eval", "--index", str(index),
                                                "--append-batch", str(batches[0]),
                                                "--append-batch", str(batches[1])]):
                    main()
            result = json.loads(output.getvalue().split("KRAKEN_PROSPECTIVE_ROUND_COVERAGE ")[1])
            self.assertEqual(result["rounds_verified"], 2)
            self.assertEqual(result["snapshots_verified"], 2)
            self.assertEqual(result["qualified_first_entry_episodes"], 0)
            self.assertFalse(result["production_applied"])
            with redirect_stdout(io.StringIO()) as output:
                with patch.object(sys, "argv", ["eval", "--index", str(index)]):
                    main()
            self.assertIn('"rounds_verified": 2', output.getvalue())


if __name__ == "__main__":
    unittest.main()
