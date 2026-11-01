"""Adversarial tests for the GitHub issue-comment heartbeat authorization.

These are offline only: no GitHub API write, workflow dispatch, or ledger write.
"""
import copy
import datetime as dt
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from paper_pov.external_heartbeat_guard import (
    COMMAND, ISSUE_NUMBER, OWNER, OWNER_ID, REPOSITORY, WORKFLOW, authorize,
)

ROOT = Path(__file__).resolve().parents[1]
NOW = dt.datetime(2026, 11, 1, 11, 0, tzinfo=dt.timezone.utc)


def event():
    identity = {"login": OWNER, "id": OWNER_ID, "type": "User"}
    return {
        "action": "created",
        "repository": {
            "full_name": REPOSITORY, "default_branch": "main",
            "owner": copy.deepcopy(identity),
        },
        "issue": {"number": ISSUE_NUMBER, "state": "open"},
        "comment": {
            "id": 6557038235, "body": COMMAND,
            "created_at": "2026-11-01T11:00:00Z",
            "author_association": "OWNER", "user": copy.deepcopy(identity),
        },
        "sender": copy.deepcopy(identity),
    }


def check(e=None, **kwargs):
    return authorize(event() if e is None else e, repository=REPOSITORY,
                     actor=OWNER, ref="refs/heads/main",
                     event_name="issue_comment", now=NOW, **kwargs)


class ExternalHeartbeatGuardTests(unittest.TestCase):
    def assert_rejected(self, mutation):
        e = event()
        mutation(e)
        with self.assertRaises((ValueError, TypeError)):
            check(e)

    def test_only_fixed_existing_recovery_controller_is_authorized(self):
        intent = check()
        self.assertEqual(intent["workflow"], "paper-recovery.yml")
        self.assertEqual(intent["ref"], "main")
        self.assertEqual(intent["action"], "REQUEST_EXISTING_RECOVERY_CONTROLLER_ONLY")
        self.assertTrue(intent["paper_only"])
        self.assertEqual(intent["comment_id"], 6557038235)
        self.assertNotIn("paper-pipeline.yml", json.dumps(intent))

    def test_exact_command_only_no_shell_or_scan_override(self):
        for command in ("/paper-scan", "/paper-recovery", "/paper-recovery-heartbeat\n",
                        " /paper-recovery-heartbeat", "/paper-recovery-heartbeat --ref evil",
                        "/paper-recovery-heartbeat; echo unsafe", "x" + COMMAND, "",
                        None, "/PAPER-RECOVERY-HEARTBEAT"):
            with self.subTest(command=command):
                self.assert_rejected(lambda e: e["comment"].update(body=command))

    def test_sender_and_author_identity_are_both_immutable(self):
        for key in ("sender", "comment", "repository"):
            for field, value in (("login", "attacker"), ("id", 1),
                                 ("id", "336805669"), ("id", True),
                                 ("login", None)):
                with self.subTest(key=key, field=field, value=value):
                    def mutate(e):
                        target = e[key]["user"] if key == "comment" else (
                            e[key]["owner"] if key == "repository" else e[key])
                        target[field] = value
                    self.assert_rejected(mutate)
        self.assert_rejected(lambda e: e["comment"].update(author_association="COLLABORATOR"))
        self.assert_rejected(lambda e: e["comment"].update(author_association=None))

    def test_issue_and_repository_are_exact(self):
        for value in (33, 35, "34", True, None):
            with self.subTest(number=value):
                self.assert_rejected(lambda e: e["issue"].update(number=value))
        self.assert_rejected(lambda e: e["issue"].update(pull_request={"url": "x"}))
        self.assert_rejected(lambda e: e["issue"].update(state="closed"))
        self.assert_rejected(lambda e: e["repository"].update(default_branch="dev"))
        self.assert_rejected(lambda e: e["repository"].update(full_name="attacker/repo"))

    def test_event_action_and_comment_identity(self):
        for action in ("edited", "deleted", "opened", None):
            with self.subTest(action=action):
                self.assert_rejected(lambda e: e.update(action=action))
        for cid in (0, -1, "6557038235", True, None):
            with self.subTest(comment_id=cid):
                self.assert_rejected(lambda e: e["comment"].update(id=cid))
        for key in ("sender", "comment", "issue", "repository"):
            self.assert_rejected(lambda e: e.pop(key))

    def test_execution_context_must_be_default_branch_issue_comment(self):
        variants = [
            {"repository": "attacker/repo"}, {"actor": "attacker"},
            {"ref": "refs/heads/dev"}, {"ref": "refs/pull/10/merge"},
            {"event_name": "workflow_dispatch"}, {"event_name": "schedule"},
        ]
        for overrides in variants:
            with self.subTest(overrides=overrides), self.assertRaises(ValueError):
                args = dict(repository=REPOSITORY, actor=OWNER,
                            ref="refs/heads/main", event_name="issue_comment", now=NOW)
                args.update(overrides)
                authorize(event(), **args)

    def test_stale_future_and_naive_timestamps_fail_closed(self):
        for timestamp in ("2026-11-01T10:29:59Z", "2026-11-01T11:02:01Z",
                          "2026-11-01T11:00:00", "invalid", None):
            with self.subTest(timestamp=timestamp):
                self.assert_rejected(lambda e: e["comment"].update(created_at=timestamp))
        self.assert_rejected(lambda e: e["comment"].update(created_at=123))
        with self.assertRaises(ValueError):
            authorize(event(), repository=REPOSITORY, actor=OWNER,
                      ref="refs/heads/main", event_name="issue_comment",
                      now=dt.datetime(2026, 11, 1, 11, 0))

    def test_boundary_clock_window(self):
        e = event()
        e["comment"]["created_at"] = "2026-11-01T10:30:00Z"
        self.assertEqual(check(e)["workflow"], WORKFLOW)
        e["comment"]["created_at"] = "2026-11-01T11:02:00Z"
        self.assertEqual(check(e)["workflow"], WORKFLOW)

    def test_cli_never_leaves_old_authorization_on_bad_event(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, output = Path(tmp) / "event.json", Path(tmp) / "intent.json"
            command = [sys.executable, "-m", "paper_pov.external_heartbeat_guard",
                       "--event", str(source), "--repository", REPOSITORY,
                       "--actor", OWNER, "--ref", "refs/heads/main",
                       "--event-name", "issue_comment", "--output", str(output)]
            e = event()
            e["comment"]["created_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
            source.write_text(json.dumps(e))
            success = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(success.returncode, 0, success.stderr)
            self.assertEqual(json.loads(output.read_text())["workflow"], WORKFLOW)
            e["comment"]["body"] = "/paper-scan"
            source.write_text(json.dumps(e))
            failure = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(failure.returncode, 0)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
