"""Safety contracts for the one-shot read-only public artifact restore proof."""
import unittest
from pathlib import Path

PATH = Path(".github/workflows/paper-restore-audit.yml")


class RecoveryWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = PATH.read_text()

    def test_one_shot_only_no_scanner_schedule(self):
        self.assertIn("  pull_request:", self.workflow)
        self.assertIn("  workflow_dispatch:", self.workflow)
        self.assertNotIn("  schedule:", self.workflow)
        self.assertNotIn("cron:", self.workflow)

    def test_exact_pr_head_and_read_only_token(self):
        self.assertIn("github.event.pull_request.head.sha || github.sha", self.workflow)
        self.assertIn("persist-credentials: false", self.workflow)
        self.assertIn("permissions:\n  contents: read\n  actions: read", self.workflow)
        self.assertNotIn("contents: write", self.workflow)
        self.assertNotIn("secrets.", self.workflow)

    def test_genuine_scheduled_run_and_immutable_git_comparison(self):
        for phrase in ("event=schedule", "status=success",
                       "git rev-list --first-parent --max-count=40",
                       "paper_pov.segmented_repository export-git", "cmp -s",
                       "verify_bundle(load_bundle", "source_sha",
                       "head_sha", "remote_git_bytes_match"):
            self.assertIn(phrase, self.workflow)

    def test_no_ledger_writes_or_order_paths(self):
        for forbidden in ("git push", "git commit", "AddOrder",
                          "/0/private/", "railway", "gh api -X POST",
                          "cancel-in-progress: true"):
            self.assertNotIn(forbidden, self.workflow)

    def test_bounded_artifact_download_and_proof_retention(self):
        for phrase in ("--max-filesize 20000000", "--max-time 120",
                       "--connect-timeout 15", "MAX_TOTAL_BYTES", "MAX_FILE_BYTES",
                       "stat.S_ISLNK", "Unsafe ZIP member",
                       "retention-days: 90", "if-no-files-found: error"):
            self.assertIn(phrase, self.workflow)


if __name__ == "__main__":
    unittest.main()
