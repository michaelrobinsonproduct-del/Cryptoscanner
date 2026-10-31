"""Read-only verifier workflow safety: never become a second scanner writer."""
import unittest
from pathlib import Path

WORKFLOW = Path(".github/workflows/paper-forward-audit.yml")


class VerifierWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.code = WORKFLOW.read_text()

    def test_unattended_independent_hourly_readback(self):
        self.assertIn("  schedule:", self.code)
        self.assertIn("cron: '21 * * * *'", self.code)
        self.assertIn("--before-commit", self.code)
        self.assertIn("--after-commit", self.code)
        self.assertIn("git show", self.code)

    def test_pull_request_checks_use_exact_immutable_head(self):
        self.assertIn("github.event.pull_request.head.sha || github.sha", self.code)
        self.assertIn("persist-credentials: false", self.code)

    def test_verifier_cannot_write_ledger_or_production(self):
        self.assertIn("permissions:\n  contents: read", self.code)
        self.assertIn("persist-credentials: false", self.code)
        for forbidden in ("contents: write", "git push", "gh api -X POST",
                          "secrets.", "paper-ledger-next.json"):
            self.assertNotIn(forbidden, self.code)

    def test_checked_audit_artifacts_are_durable_and_bounded(self):
        self.assertIn("sha256sum independent-audit.json transition-audit.json", self.code)
        self.assertIn("retention-days: 90", self.code)
        self.assertIn("if-no-files-found: error", self.code)
        self.assertIn("transition-audit.json", self.code)
        self.assertIn("cancel-in-progress: false", self.code)


if __name__ == "__main__":
    unittest.main()
