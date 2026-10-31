"""Stage-1 paper execution safety: one GitHub writer, one hourly slot, no relaxed labels.

These tests are deterministic and make no network calls. They guard the
requested stage gate, not the predictive value of the paper scanner.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / ".github/workflows/paper-pipeline.yml"
LEDGER = ROOT / "paper_pov/ledger.py"


class StageOneScheduleTests(unittest.TestCase):
    def test_only_one_hourly_scheduled_execution_before_acceptance(self):
        text = PIPELINE.read_text()
        crons = re.findall(r"(?m)^\s*-\s*cron:\s*['\"]([^'\"]+)['\"]\s*$", text)
        self.assertEqual(crons, ["9 * * * *"])

    def test_global_non_cancelling_single_writer_mutex(self):
        text = PIPELINE.read_text()
        self.assertIn("group: public-paper-proof-ledger-single-writer", text)
        self.assertIn("cancel-in-progress: false", text)
        self.assertEqual(text.count("git push origin HEAD:refs/heads/paper-proof-ledger"), 1)

    def test_only_paper_pipeline_pushes_ledger(self):
        writers = []
        for workflow in (ROOT / ".github/workflows").glob("*.yml"):
            if "git push origin HEAD:refs/heads/paper-proof-ledger" in workflow.read_text():
                writers.append(workflow.name)
        self.assertEqual(writers, ["paper-pipeline.yml"])

    def test_no_silent_bootstrap_and_tests_before_market_scan(self):
        text = PIPELINE.read_text()
        self.assertLess(text.index("Exact commit tests before any ledger mutation"),
                        text.index("Restore checksum-sealed existing ledger"))
        self.assertLess(text.index("Restore checksum-sealed existing ledger"),
                        text.index("Real bounded public Kraken scan"))
        self.assertIn("paper_pov.segmented_repository export-git", text)
        self.assertIn("--full-replay", text)
        self.assertIn("git fetch --no-tags --depth=512 origin refs/heads/paper-proof-ledger", text)
        self.assertIn("paper_pov.segmented_live_writer stage", text)
        self.assertIn("PAPER_RESTORED", text)

    def test_nonforce_cas_remote_readback_and_artifact(self):
        text = PIPELINE.read_text()
        self.assertLess(text.index("Preserve independently downloadable checked artifact"),
                        text.index("Non-force, single-writer ledger push"))
        self.assertIn('test "$(git rev-parse refs/remotes/origin/paper-proof-ledger)" = "$(cat /tmp/paper-base.sha)"', text)
        self.assertIn("git push origin HEAD:refs/heads/paper-proof-ledger", text)
        self.assertNotIn("git push --force", text)
        self.assertIn("paper_pov.segmented_live_writer verify-remote", text)
        self.assertIn("PAPER_LEDGER_REMOTE_READBACK_VERIFIED", text)
        self.assertIn("paper_pov.segmented_live_writer apply", text)
        self.assertIn("retention-days: 90", text)

    def test_only_main_schedule_or_manual_dispatch_can_write(self):
        text = PIPELINE.read_text()
        self.assertNotIn("  push:", text)
        self.assertIn("github.ref == 'refs/heads/main'", text)
        self.assertIn("github.event_name == 'schedule'", text)
        self.assertIn("github.event_name == 'workflow_dispatch'", text)

    def test_do_not_weaken_forty_five_minute_gap_abstention(self):
        text = LEDGER.read_text()
        self.assertIn("MAX_DELAY = dt.timedelta(minutes=45)", text)
        self.assertIn("ABSTAIN_GAP", text)

    def test_paper_only_workflow_never_uses_private_or_production_services(self):
        text = PIPELINE.read_text().lower()
        for forbidden in ("api.kraken.com/0/private/", "addorder", "railway", "supabase", "secrets."):
            self.assertNotIn(forbidden, text)
        self.assertIn("public kraken", text)
        self.assertIn("production applied: no", text)


if __name__ == "__main__":
    unittest.main()
