"""Guard the one-writer stage-1 paper scan event and main-only execution contract."""
import re
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1] / ".github/workflows/paper-pipeline.yml"


class MainOnlyPaperTriggerTests(unittest.TestCase):
    def test_only_schedule_and_explicit_dispatch_can_trigger_writer(self):
        text = PIPELINE.read_text()
        events = text.split("\npermissions:", 1)[0]
        self.assertIn("\n  workflow_dispatch:", events)
        self.assertIn("\n  schedule:", events)
        for forbidden in ("push:", "pull_request:", "issue_comment:", "repository_dispatch:"):
            self.assertNotIn(forbidden, events)

    def test_job_runs_only_from_default_main_ref(self):
        text = PIPELINE.read_text()
        self.assertIn(
            "if: github.ref == 'refs/heads/main' && "
            "(github.event_name == 'schedule' || github.event_name == 'workflow_dispatch')",
            text,
        )
        self.assertEqual(text.count("if: github.ref == 'refs/heads/main'"), 1)

    def test_stage_one_single_hourly_schedule_and_single_writer_unchanged(self):
        text = PIPELINE.read_text()
        self.assertEqual(re.findall(r"(?m)^\s*-\s*cron:\s*['\"]([^'\"]+)['\"]", text), ["9 * * * *"])
        self.assertIn("group: public-paper-proof-ledger-single-writer", text)
        self.assertIn("cancel-in-progress: false", text)
        self.assertEqual(text.count("git push origin HEAD:refs/heads/paper-proof-ledger"), 1)
        self.assertIn("PAPER_LEDGER_REMOTE_READBACK_VERIFIED", text)
        self.assertIn("Render verified UTC results after ledger remote readback", text)

    def test_dispatch_is_paper_only_and_has_no_second_writer(self):
        text = PIPELINE.read_text()
        self.assertIn("python -m paper_pov.scanner", text)
        self.assertIn("PAPER_RESULTS_VERIFIED", (PIPELINE.parents[1] / "paper_pov/results_report.py").read_text())
        self.assertNotIn("git push --force", text)
        self.assertNotIn("railway", text.lower())


if __name__ == "__main__":
    unittest.main()
