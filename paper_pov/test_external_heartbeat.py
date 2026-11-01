"""Static fail-closed contract for owner-authenticated external wake workflow.

This event is deliberately NOT a second scanner or ledger writer.  The
separately reviewed recovery controller owns all durable CAS and dispatch gates.
"""
import unittest
from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/paper-external-heartbeat.yml"


class ExternalHeartbeatContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_only_created_issue_comment_can_wake(self):
        s = self.workflow
        self.assertRegex(s, r"(?m)^on:\n  issue_comment:\n    types: \[created\]")
        self.assertIn("github.event.action == 'created'", s)
        self.assertIn("github.event.issue.pull_request == null", s)

    def test_exact_repository_branch_issue_owner_and_body(self):
        s = self.workflow
        for guard in (
            "github.repository == 'michaelrobinsonproduct-del/Cryptoscanner'",
            "github.ref == 'refs/heads/main'",
            "github.event.issue.number == 34",
            "github.event.comment.user.login == 'michaelrobinsonproduct-del'",
            "github.event.comment.body == 'PAPER_RECOVERY_WAKE_V1'",
        ):
            with self.subTest(guard=guard):
                self.assertIn(guard, s)

    def test_dispatch_only_existing_recovery_not_scanner_or_ledger(self):
        s = self.workflow
        self.assertIn("actions: write", s)
        self.assertIn("target.state !== 'active'", s)
        self.assertIn("github.rest.actions.createWorkflowDispatch", s)
        self.assertIn("workflow_id = 'paper-recovery.yml'", s)
        self.assertIn("ref: 'main'", s)
        self.assertNotIn("paper-pipeline.yml", s)
        self.assertNotIn("paper-proof-ledger", s)
        self.assertNotIn("git push", s)
        self.assertNotIn("curl ", s)
        self.assertNotRegex(s, r"(?m)^\s+run:")

    def test_no_schedule_dependency_or_self_dispatch(self):
        s = self.workflow
        self.assertNotRegex(s, r"(?m)^  (schedule|workflow_run|workflow_dispatch):")
        self.assertNotIn("workflow_id = 'paper-external-heartbeat.yml'", s)
        self.assertIn("cancel-in-progress: false", s)


if __name__ == "__main__":
    unittest.main()
