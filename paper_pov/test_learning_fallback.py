"""Synthetic fail-closed owner learning fallback contracts; no GitHub writes."""
import copy
import datetime as dt
import unittest
from pathlib import Path

from paper_pov.learning_fallback import COMMAND, REPO, decide
from paper_pov.test_learning_outcomes import fixture, START

UTC = dt.timezone.utc


def iso(minutes):
    return (START + dt.timedelta(minutes=minutes)).isoformat().replace("+00:00", "Z")


def case():
    state = fixture(range(0, 600, 30))
    writer = {
        "id": 12345, "name": "Public Kraken Paper POV (scheduled, isolated ledger)",
        "path": ".github/workflows/paper-pipeline.yml",
        "repository": {"full_name": REPO}, "head_repository": {"full_name": REPO},
        "head_branch": "main", "head_sha": "a" * 40,
        "event": "workflow_dispatch", "status": "completed", "conclusion": "success",
        "run_attempt": 1, "created_at": iso(568), "updated_at": iso(572)
    }
    event = {
        "action": "created", "repository": {"full_name": REPO, "default_branch": "main"},
        "issue": {"number": 34}, "sender": {"login": "michaelrobinsonproduct-del", "id": 336805669},
        "comment": {"id": 111, "body": COMMAND, "author_association": "OWNER",
                    "user": {"login": "michaelrobinsonproduct-del", "id": 336805669}}
    }
    comments = [{"id": 111, "body": COMMAND, "created_at": iso(574),
                 "user": {"login": "michaelrobinsonproduct-del", "id": 336805669}}]
    manifest = {"head": {"generation": 20, "ledger_sha256": state["sha256"]}}
    return dict(event=event, paper_runs=[writer], learning_runs=[], comments=comments,
                state=state, manifest=manifest,
                ledger_message="paper: atomic packed scan 12345 source " + "a" * 40,
                ledger_commit="b" * 40, repository=REPO, current_run_id=999,
                checkout_sha="a" * 40, now=START + dt.timedelta(minutes=575))


class OwnerLearningFallbackTests(unittest.TestCase):
    def test_exact_successful_durable_writer_and_no_learning_permit_read_only(self):
        args = case()
        original = copy.deepcopy(args["state"])
        result = decide(**args)
        self.assertEqual(result["action"], "RUN_READ_ONLY_LEARNING")
        self.assertEqual(result["writer_run_id"], 12345)
        self.assertEqual(result["ledger_sha256"], args["state"]["sha256"])
        self.assertTrue(result["paper_only"])
        self.assertEqual(args["state"], original)

    def test_wrong_owner_sender_issue_command_or_default_branch_rejected(self):
        for key, value in (("sender", {"login": "attacker", "id": 123}),
                           ("issue", {"number": 35}),
                           ("repository", {"full_name": REPO, "default_branch": "develop"}),
                           ("comment", {"id": 111, "body": "/paper-scan",
                                        "author_association": "OWNER",
                                        "user": {"login": "michaelrobinsonproduct-del",
                                                 "id": 336805669}})):
            args = case()
            args["event"][key] = value
            with self.assertRaisesRegex(ValueError, "Untrusted"):
                decide(**args)

    def test_existing_native_learning_or_duplicate_command_abstains(self):
        args = case()
        args["learning_runs"] = [{"id": 88, "event": "workflow_run", "created_at": iso(573)}]
        self.assertEqual(decide(**args)["reason"], "AUTOMATIC_LEARNING_EXISTS_OR_AMBIGUOUS")
        args = case()
        args["comments"].append(dict(args["comments"][0], id=222))
        self.assertEqual(decide(**args)["reason"], "DUPLICATE_OR_MISSING_OWNER_COMMAND")

    def test_active_failed_mismatched_or_old_writer_abstains(self):
        for mutate in (
            lambda a: a["paper_runs"][0].update(status="in_progress", conclusion=None),
            lambda a: a["paper_runs"][0].update(head_sha="f" * 40),
            lambda a: a.update(ledger_message="paper: wrong"),
            lambda a: a.update(now=START + dt.timedelta(minutes=650)),
        ):
            args = case()
            mutate(args)
            self.assertEqual(decide(**args)["action"], "ABSTAIN")

    def test_truncated_learning_history_abstains_instead_of_claiming_no_native_run(self):
        args = case()
        args["learning_runs"] = [
            {"id": i + 1, "event": "pull_request", "created_at": iso(569)}
            for i in range(100)
        ]
        self.assertEqual(decide(**args)["reason"], "LEARNING_HISTORY_TRUNCATED")
        args["learning_runs"][0]["created_at"] = iso(560)
        self.assertEqual(decide(**args)["action"], "RUN_READ_ONLY_LEARNING")

    def test_owner_comment_concurrency_not_starved_by_unrelated_comments(self):
        # GitHub Actions keeps at most one pending workflow per concurrency
        # group. An unrelated issue_comment must not evict the owner command.
        workflow = (Path(__file__).resolve().parent.parent /
                    ".github/workflows/paper-learning-outcomes-shadow.yml").read_text()
        self.assertIn(
            "group: paper-learning-shadow-${{ github.event.workflow_run.id || github.event.comment.id || github.run_id }}",
            workflow,
        )
        self.assertIn("cancel-in-progress: false", workflow)

    def test_corrupt_manifest_or_ledger_fails_closed(self):
        args = case()
        args["manifest"]["head"]["ledger_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "Unsealed"):
            decide(**args)
        args = case()
        args["state"]["observations"][0]["price"] = 999
        with self.assertRaisesRegex(ValueError, "checksum"):
            decide(**args)


if __name__ == "__main__":
    unittest.main()
