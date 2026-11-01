"""Recovery controller failure-injection contracts: never dispatch on ambiguity."""
import datetime as dt
import unittest
from pathlib import Path

from paper_pov.monitor import UTC
from paper_pov.recovery import decide, RECOVERY_MARKER
from paper_pov.test_monitor import fixture, run, SHA

NOW = dt.datetime(2026, 10, 31, 23, 27, tzinfo=UTC)
COMMIT = "d" * 40
MESSAGE = "paper: immutable scan 123 source " + SHA
BOT = {"login": "github-actions[bot]", "id": 41898282}


def scan(run_id=123, when="2026-10-31T20:10:00Z", **kwargs):
    return dict(run(run_id, when, **kwargs), head_branch="main")


def decision(runs=None, comments=None, ledger=None, now=NOW, commit=COMMIT, message=MESSAGE):
    if runs is None:
        runs = [scan()]
    if comments is None:
        comments = []
    if ledger is None:
        ledger = fixture()
    return decide({"workflow_runs": runs}, comments, ledger, commit, message, now)


class RecoveryTests(unittest.TestCase):
    def test_two_matured_slots_and_verified_ledger_permit_same_workflow_request(self):
        d = decision()
        self.assertEqual(d["action"], "DISPATCH_EXISTING_WORKFLOW")
        self.assertEqual(d["reason"], "TWO_MATURED_SLOTS_MISSED")
        self.assertEqual(d["latest_run_id"], 123)
        self.assertEqual(d["ledger_generation"], 1)
        self.assertEqual(len(d["missed_matured_slots"]), 2)
        self.assertEqual(d["attempt_marker"], RECOVERY_MARKER + COMMIT)

    def test_no_dispatch_with_only_one_matured_missed_slot(self):
        d = decision(now=dt.datetime(2026, 10, 31, 21, 27, tzinfo=UTC))
        self.assertEqual(d["action"], "NO_DISPATCH")

    def test_recent_success_does_not_dispatch(self):
        d = decision(now=dt.datetime(2026, 10, 31, 21, 0, tzinfo=UTC))
        self.assertEqual((d["action"], d["reason"]), ("NO_DISPATCH", "RECENT_SUCCESS"))

    def test_queued_or_running_existing_writer_prevents_dispatch(self):
        for status in ("queued", "in_progress", "waiting", "requested", "pending"):
            with self.subTest(status=status):
                d = decision(runs=[scan(), scan(124, "2026-10-31T23:20:00Z",
                                              status=status, conclusion=None)])
                self.assertEqual((d["action"], d["reason"]), ("NO_DISPATCH", "SCANNER_ACTIVE_OR_QUEUED"))

    def test_newest_failed_scan_blocks_unattended_recovery(self):
        d = decision(runs=[scan(), scan(124, "2026-10-31T22:10:00Z", conclusion="failure")])
        self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "LATEST_SCANNER_RUN_FAILED"))

    def test_newer_success_without_ledger_readback_blocks(self):
        d = decision(runs=[scan(), scan(124, "2026-10-31T22:10:00Z")])
        self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "LEDGER_NOT_LINKED_TO_NEWEST_SUCCESS"))

    def test_same_ledger_recent_recovery_attempt_prevents_duplicate(self):
        d = decision(comments=[{"body": "<!-- " + RECOVERY_MARKER + COMMIT + " -->",
                                "created_at": "2026-10-31T23:15:00Z", "user": BOT}])
        self.assertEqual((d["action"], d["reason"]), ("NO_DISPATCH", "RECOVERY_ALREADY_ATTEMPTED"))

    def test_old_attempt_permits_bounded_retry(self):
        d = decision(comments=[{"body": RECOVERY_MARKER + COMMIT,
                                "created_at": "2026-10-31T21:00:00Z", "user": BOT}])
        self.assertEqual(d["action"], "DISPATCH_EXISTING_WORKFLOW")

    def test_malformed_recovery_marker_fails_closed(self):
        d = decision(comments=[{"body": RECOVERY_MARKER + COMMIT,
                                "created_at": "not-a-date", "user": BOT}])
        self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "RECOVERY_MARKER_TIMESTAMP_INVALID"))

    def test_public_comment_cannot_spoof_recovery_attempt(self):
        for actor in (None, {"login": "github-actions[bot]", "id": 999},
                      {"login": "attacker", "id": 41898282}):
            with self.subTest(actor=actor):
                d = decision(comments=[{"body": RECOVERY_MARKER + COMMIT,
                                        "created_at": "not-a-date", "user": actor}])
                self.assertEqual(d["action"], "DISPATCH_EXISTING_WORKFLOW")

    def test_missing_issue_comments_fails_closed(self):
        self.assertEqual(decision(comments="missing")["action"], "BLOCKED")

    def test_corrupt_ledger_fails_closed(self):
        state = fixture()
        state["predictions"][0]["price"] = 999.0
        d = decision(ledger=state)
        self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "LEDGER_INVALID"))

    def test_source_mismatch_fails_closed(self):
        d = decision(message="paper: immutable scan 123 source " + "f"*40)
        self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "LEDGER_COMMIT_PROVENANCE_MISMATCH"))

    def test_source_run_mismatch_fails_closed(self):
        d = decision(runs=[dict(scan(), head_sha="f"*40)])
        self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "LEDGER_NOT_LINKED_TO_NEWEST_SUCCESS"))

    def test_historical_completed_main_push_is_not_a_scanner_run(self):
        # GitHub's real workflow history contains five old push-triggered CI
        # runs and later successful schedule runs. Legacy CI must not block
        # recovery when a newer immutable scheduled scan anchors the ledger.
        legacy = dict(scan(122, "2026-10-31T18:00:00Z"), event="push")
        d = decision(runs=[legacy, scan()])
        self.assertEqual(d["action"], "DISPATCH_EXISTING_WORKFLOW")
        self.assertEqual(d["latest_run_id"], 123)
        self.assertEqual(d["ignored_historical_push_run_ids"], [122])
        self.assertEqual(len(d["missed_matured_slots"]), 2)

    def test_untrusted_push_events_never_enable_recovery(self):
        variants = [
            dict(scan(124, "2026-10-31T22:00:00Z"), event="push"),
            dict(scan(122, "2026-10-31T18:00:00Z"), event="push", status="in_progress", conclusion=None),
            dict(scan(122, "2026-10-31T18:00:00Z"), event="push", head_branch="dev"),
            dict(scan(122, "2026-10-31T18:00:00Z"), event="pull_request"),
            dict(scan(122, "2026-10-31T18:00:00Z"), event="push", conclusion=None),
            dict(scan(122, "2026-10-31T18:00:00Z"), event="push", id=None),
            dict(scan(122, "2026-10-31T18:00:00Z"), event="push", head_sha="bad"),
        ]
        for item in variants:
            with self.subTest(item=item):
                d = decision(runs=[scan(), item])
                self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "RUN_EVENT_INVALID"))

    def test_historical_push_malformed_or_future_timestamp_fails_closed(self):
        for when in ("not-a-date", "2026-11-02T23:00:00Z"):
            with self.subTest(when=when):
                d = decision(runs=[scan(), dict(scan(122, when), event="push")])
                self.assertEqual(d["action"], "BLOCKED")

    def test_non_main_branch_or_invalid_event_fails_closed(self):
        for item in (dict(scan(), head_branch="dev"), dict(scan(), event="pull_request")):
            self.assertEqual(decision(runs=[item])["action"], "BLOCKED")

    def test_missing_main_branch_fails_closed(self):
        for branch in (None, ""):
            with self.subTest(branch=branch):
                d = decision(runs=[dict(scan(), head_branch=branch)])
                self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "RUN_BRANCH_NOT_MAIN"))

    def test_unknown_or_missing_run_status_fails_closed(self):
        for status in (None, "unknown", "startup_failure"):
            with self.subTest(status=status):
                newer = scan(124, "2026-10-31T23:20:00Z", status=status, conclusion=None)
                d = decision(runs=[scan(), newer])
                self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "RUN_STATUS_INVALID"))

    def test_missing_run_api_fails_closed(self):
        self.assertEqual(decide({"error": "rate limited"}, [], fixture(), COMMIT, MESSAGE, NOW)["action"], "BLOCKED")

    def test_missing_run_history_fails_closed(self):
        self.assertEqual(decision(runs=[])["action"], "BLOCKED")

    def test_future_timestamp_fails_closed(self):
        self.assertEqual(decision(runs=[scan(123, "2026-11-01T23:00:00Z")])["action"], "BLOCKED")

    def test_no_false_exchange_freshness_or_predictive_claims(self):
        code = Path("paper_pov/recovery.py").read_text()
        self.assertNotIn("git push", code)
        self.assertNotIn("production_applied = True", code)
        self.assertNotIn("railway", code.lower())

    def test_workflow_only_dispatches_existing_single_writer_and_has_cas(self):
        workflow = Path(".github/workflows/paper-recovery.yml").read_text()
        self.assertIn("actions/workflows/paper-pipeline.yml/dispatches", workflow)
        self.assertEqual(workflow.count("actions/workflows/paper-pipeline.yml/dispatches"), 1)
        self.assertIn("public-paper-recovery-controller", workflow)
        self.assertIn("cancel-in-progress: false", workflow)
        self.assertIn("PAPER_RECOVERY_LEDGER_MOVED_ABORT", workflow)
        self.assertIn("PAPER_RECOVERY_RECHECK_ABORT", workflow)
        self.assertIn("PAPER_RECOVERY_MAIN_CHANGED_ABORT", workflow)
        self.assertIn("PAPER_RECOVERY_ATTEMPT_READBACK_VERIFIED", workflow)
        self.assertEqual(workflow.count("--jq '.[] | {body,created_at,user:{login:.user.login,id:.user.id}} | @json'"), 2)
        self.assertIn("PAPER_RECOVERY_RUNS_CHANGED_ABORT", workflow)
        self.assertIn("github.event.workflow_run.event == 'schedule'", workflow)
        self.assertIn("github.event.workflow_run.head_branch == 'main'", workflow)
        self.assertIn("github.event.workflow_run.conclusion == 'success'", workflow)
        self.assertNotIn("git push", workflow)
        self.assertNotIn("railway", workflow.lower())


if __name__ == "__main__":
    unittest.main()
