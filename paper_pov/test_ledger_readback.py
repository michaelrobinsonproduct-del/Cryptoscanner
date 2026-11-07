"""D1: persisted ledger readback must be exact before reporting success."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from paper_pov import ledger


class PersistedReadbackTests(unittest.TestCase):
    def run_case(self, writer):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src, report, out = (root / x for x in ("old.json", "report.json", "new.json"))
            src.write_text(json.dumps(ledger.empty()))
            report.write_text("{}")
            proposed = ledger.empty()
            with patch.object(ledger, "advance", return_value=proposed), \
                 patch.object(ledger, "atomic_json", side_effect=writer):
                return ledger.update_file(src, report, "a" * 40, out)

    def test_missing_write_is_not_success(self):
        with self.assertRaises(FileNotFoundError):
            self.run_case(lambda path, state: None)

    def test_truncated_write_is_not_success(self):
        def truncated(path, state):
            Path(path).write_text('{"schema":')
        with self.assertRaises(json.JSONDecodeError):
            self.run_case(truncated)

    def test_resealed_but_different_generation_is_not_success(self):
        def changed(path, state):
            altered = ledger.empty()
            altered["generation"] = 1
            ledger.seal(altered)
            Path(path).write_text(json.dumps(altered))
        with self.assertRaises(ValueError):
            self.run_case(changed)

    def test_valid_write_returns_readback_scoreboard(self):
        def correct(path, state):
            Path(path).write_text(json.dumps(state))
        result = self.run_case(correct)
        self.assertEqual(result["generation"], 0)
        self.assertEqual(result["ledger_sha256"], ledger.empty()["sha256"])


if __name__ == "__main__":
    unittest.main()
