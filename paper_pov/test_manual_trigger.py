"""Security and integration-contract tests for owner-only paper scan dispatch."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from paper_pov.manual_trigger import authorize, REPOSITORY

ROOT = Path(__file__).resolve().parents[1]


def event():
    return {
        "action": "created",
        "repository": {"full_name": REPOSITORY},
        "issue": {"number": 34},
        "comment": {
            "id": 987654321,
            "body": "/paper-scan",
            "author_association": "OWNER",
            "user": {"login": "michaelrobinsonproduct-del"},
        },
        "sender": {"login": "michaelrobinsonproduct-del"},
    }


class ManualPaperTriggerTests(unittest.TestCase):
    def test_valid_owner_command_only_dispatches_existing_main_workflow(self):
        result = authorize(event(), REPOSITORY)
        self.assertEqual(result, {
            "repository": REPOSITORY,
            "issue": 34,
            "comment_id": 987654321,
            "workflow": "paper-pipeline.yml",
            "ref": "main",
            "paper_only": True,
        })

    def test_command_is_exact_and_never_accepts_arbitrary_shell_input(self):
        for command in (" /paper-scan", "/paper-scan\n", "/paper-scan now",
                        "/paper-scan; echo injected", "/paper-scan --ref evil",
                        "/PAPER-SCAN", "", None, "please /paper-scan"):
            with self.subTest(command=command):
                e = event()
                e["comment"]["body"] = command
                with self.assertRaises(ValueError):
                    authorize(e, REPOSITORY)

    def test_owner_identity_must_match_comment_sender_and_association(self):
        changes = [
            ("comment", "author_association", "NONE"),
            ("comment", "author_association", "COLLABORATOR"),
            ("comment", "author_association", None),
            ("sender", "login", "attacker"),
        ]
        for parent, field, value in changes:
            with self.subTest(parent=parent, field=field, value=value):
                e = event()
                e[parent][field] = value
                with self.assertRaises(ValueError):
                    authorize(e, REPOSITORY)
        e = event()
        e["comment"]["user"]["login"] = "attacker"
        with self.assertRaises(ValueError):
            authorize(e, REPOSITORY)

    def test_rejects_wrong_issue_pr_comment_and_wrong_repo(self):
        for number in (0, 33, 35, "34", True, None):
            e = event()
            e["issue"]["number"] = number
            with self.subTest(number=number), self.assertRaises(ValueError):
                authorize(e, REPOSITORY)
        e = event()
        e["issue"]["pull_request"] = {"url": "https://github.com/other/pr"}
        with self.assertRaises(ValueError):
            authorize(e, REPOSITORY)
        e = event()
        e["repository"]["full_name"] = "attacker/Cryptoscanner"
        with self.assertRaises(ValueError):
            authorize(e, REPOSITORY)
        with self.assertRaises(ValueError):
            authorize(event(), "attacker/Cryptoscanner")

    def test_rejects_replay_edit_delete_and_missing_identity(self):
        for action in ("edited", "deleted", None):
            e = event()
            e["action"] = action
            with self.subTest(action=action), self.assertRaises(ValueError):
                authorize(e, REPOSITORY)
        for comment_id in (0, -1, "987654321", True, None):
            e = event()
            e["comment"]["id"] = comment_id
            with self.subTest(comment_id=comment_id), self.assertRaises(ValueError):
                authorize(e, REPOSITORY)
        for key in ("sender", "comment", "issue", "repository"):
            e = event()
            e.pop(key)
            with self.subTest(key=key), self.assertRaises((ValueError, TypeError)):
                authorize(e, REPOSITORY)

    def test_cli_writes_fixed_intent_and_fails_closed_on_bad_event(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp) / "event.json", Path(tmp) / "intent.json"
            src.write_text(json.dumps(event()))
            cmd = [sys.executable, "-m", "paper_pov.manual_trigger",
                   "--event", str(src), "--repository", REPOSITORY,
                   "--output", str(dst)]
            ok = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(ok.returncode, 0, ok.stderr)
            self.assertEqual(json.loads(dst.read_text())["workflow"], "paper-pipeline.yml")
            dst.unlink()
            e = event()
            e["comment"]["body"] = "/paper-scan --ref malicious"
            src.write_text(json.dumps(e))
            bad = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(bad.returncode, 0)
            self.assertFalse(dst.exists())

    def test_workflow_requires_owner_and_only_dispatches_existing_writer(self):
        path = ROOT / ".github" / "workflows" / "paper-issue-trigger.yml"
        workflow = path.read_text()
        for required in (
            "issue_comment:", "types: [created]",
            "github.repository == 'michaelrobinsonproduct-del/Cryptoscanner'",
            "github.event.issue.number == 34",
            "github.event.issue.pull_request == null",
            "github.event.comment.user.login == 'michaelrobinsonproduct-del'",
            "github.event.comment.author_association == 'OWNER'",
            "github.event.comment.body == '/paper-scan'",
            "github.event.sender.login == 'michaelrobinsonproduct-del'",
            "python -m paper_pov.manual_trigger",
            "gh workflow run paper-pipeline.yml --ref main",
            "cancel-in-progress: false",
            "actions: write",
            "persist-credentials: false",
        ):
            with self.subTest(required=required):
                self.assertIn(required, workflow)
        for forbidden in ("git push", "paper-proof-ledger", "python -m paper_pov.scanner",
                          "secrets.KRAKEN", "workflow_dispatch:"):
            self.assertNotIn(forbidden, workflow)


if __name__ == "__main__":
    unittest.main()
