"""Fail-closed dual-format Git ledger reader integration for independent consumers.

These tests are static workflow acceptance contracts. The storage repository's
dynamic legacy/packed replay and corruption tests run in the same exact CI.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = {
    "paper-monitor.yml": ("paper-monitor-ledger.json", "paper-monitor-previous.json"),
    "paper-forward-audit.yml": ("public-paper-ledger.json", "public-paper-ledger-before.json"),
    "paper-combined-acceptance.yml": ("public-paper-ledger.json",),
    "paper-restore-audit.yml": ("paper-git-ledger.json",),
}


class DualFormatReaderContracts(unittest.TestCase):
    def test_every_independent_reader_uses_authenticated_export(self):
        for name, outputs in WORKFLOWS.items():
            with self.subTest(name=name):
                workflow = (ROOT / ".github/workflows" / name).read_text()
                self.assertIn("paper_pov.segmented_repository export-git", workflow)
                self.assertIn("git fetch --no-tags --unshallow", workflow)
                self.assertIn("contents: read", workflow)
                self.assertNotIn("git push ", workflow)
                self.assertNotIn("python -m paper_pov.scanner", workflow)
                for output in outputs:
                    self.assertIn(output, workflow)

    def test_all_read_only_evaluators_allow_bounded_packed_logical_state(self):
        for module in ("paper_pov/monitor.py", "paper_eval/report.py",
                       "paper_eval/continuity.py", "paper_eval/chain.py",
                       "paper_eval/audit.py", "paper_eval/recovery.py"):
            with self.subTest(module=module):
                source = (ROOT / module).read_text()
                self.assertIn("MAX_RAW_BYTES", source)
                self.assertNotIn("api.kraken.com/0/private/", source)
                self.assertNotIn("AddOrder", source)

    def test_no_read_only_workflow_writes_the_ledger(self):
        for name in WORKFLOWS:
            workflow = (ROOT / ".github/workflows" / name).read_text()
            self.assertNotIn("paper-proof-ledger-single-writer", workflow)
            self.assertNotIn("contents: write", workflow)
            self.assertNotIn("git commit ", workflow)
            self.assertNotIn("git push ", workflow)


if __name__ == "__main__":
    unittest.main()
