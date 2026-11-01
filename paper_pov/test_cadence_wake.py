"""Adversarial offline acceptance for the independent single-writer cadence wake."""
import copy
import datetime as dt
import unittest

from paper_pov.cadence_wake import (
    authorize, decide, slot_at, COMMAND, MARKER, REPOSITORY, OWNER, BOT,
)
from paper_pov.test_external_heartbeat_guard import event as owner_event
from paper_pov.test_recovery import scan, COMMIT, MESSAGE
from paper_pov.test_monitor import fixture, SHA

UTC = dt.timezone.utc
NOW = dt.datetime(2026, 10, 31, 23, 10, tzinfo=UTC)
MAIN = "a" * 40
INTENT = {"schema": 1, "paper_only": True, "action": "REQUEST_EXISTING_PAPER_WRITER_ONLY",
          "workflow": "paper-pipeline.yml", "ref": "main", "issue": 34,
          "comment_id": 6557038235}


def decision(runs=None, comments=None, ledger=None, now=NOW, intent=None,
             commit=COMMIT, message=MESSAGE, main=MAIN):
    return decide({"workflow_runs": [scan()] if runs is None else runs},
                  [] if comments is None else comments,
                  fixture() if ledger is None else ledger,
                  commit, message, main, INTENT if intent is None else intent, now)


def event():
    e = owner_event()
    e["comment"]["body"] = COMMAND
    return e


def authorized(e=None, now=dt.datetime(2026, 11, 1, 11, 0, tzinfo=UTC)):
    return authorize(event() if e is None else e, repository=REPOSITORY,
                     actor=OWNER, ref="refs/heads/main", event_name="issue_comment", now=now)


class CadenceWakeTests(unittest.TestCase):
    def test_valid_owner_command_fixed_writer_only(self):
        a = authorized()
        self.assertEqual(a["workflow"], "paper-pipeline.yml")
        self.assertEqual(a["action"], "REQUEST_EXISTING_PAPER_WRITER_ONLY")
        self.assertEqual(a["issue"], 34)

    def test_owner_command_rejects_all_recovery_and_arbitrary_commands(self):
        for value in ("/paper-recovery-heartbeat", "/paper-cadence-heartbeat\n",
                      " /paper-cadence-heartbeat", "/paper-cadence-heartbeat --force",
                      "/paper-cadence-heartbeat;rm -rf /", "", None):
            with self.subTest(value=value):
                e = event()
                e["comment"]["body"] = value
                with self.assertRaises(ValueError):
                    authorized(e)

    def test_owner_and_sender_cannot_be_spoofed(self):
        for target in ("sender", "comment", "repository"):
            for key, value in (("id", 1), ("id", "336805669"), ("login", "attacker")):
                with self.subTest(target=target, key=key, value=value):
                    e = event()
                    obj = e[target]["user"] if target == "comment" else (
                        e[target]["owner"] if target == "repository" else e[target])
                    obj[key] = value
                    with self.assertRaises(ValueError):
                        authorized(e)

    def test_stale_future_issue_and_execution_context_rejected(self):
        for key, value in (("created_at", "2026-11-01T10:29:59Z"),
                           ("created_at", "2026-11-01T11:02:01Z"),
                           ("created_at", "2026-11-01T11:00:00")):
            e = event()
            e["comment"][key] = value
            with self.assertRaises(ValueError):
                authorized(e)
        e = event()
        e["issue"]["number"] = 35
        with self.assertRaises(ValueError):
            authorized(e)
        with self.assertRaises(ValueError):
            authorize(event(), repository=REPOSITORY, actor=OWNER,
                      ref="refs/heads/evil", event_name="issue_comment",
                      now=dt.datetime(2026, 11, 1, 11, 0, tzinfo=UTC))

    def test_durable_anchor_and_25_minute_spacing_allow_due_dispatch(self):
        d = decision()
        self.assertEqual((d["action"], d["reason"]),
                         ("DISPATCH_EXISTING_WORKFLOW", "INDEPENDENT_CADENCE_DUE"))
        self.assertEqual(d["attempt_marker"], MARKER + COMMIT)
        self.assertEqual(d["ledger_generation"], 1)
        self.assertEqual(d["target_slot"], "2026-10-31T23:00:00+00:00")

    def test_30_minute_slot_mapping(self):
        self.assertEqual(slot_at(dt.datetime(2026, 11, 1, 11, 35, tzinfo=UTC)).minute, 30)
        self.assertEqual(slot_at(dt.datetime(2026, 11, 1, 11, 29, tzinfo=UTC)).minute, 0)

    def test_stale_external_command_window_abstains(self):
        d = decision(now=dt.datetime(2026, 10, 31, 23, 21, tzinfo=UTC))
        self.assertEqual((d["action"], d["reason"]), ("NO_DISPATCH", "CADENCE_SLOT_TOO_LATE"))

    def test_new_durable_scan_covers_slot(self):
        # The sealed run was recorded after 23:00 and must not be duplicated.
        state = fixture()
        from paper_pov.ledger import seal
        import hashlib
        asof = "2026-10-31T23:02:00+00:00"
        state["runs"][0]["as_of"] = asof
        state["predictions"][0]["as_of"] = asof
        state["predictions"][0]["prediction_id"] = hashlib.sha256(
            ("paper-v1|" + asof + "|" + state["predictions"][0]["pair"]).encode()).hexdigest()
        state["observations"][0]["at"] = "2026-10-31T23:01:50+00:00"
        d = decision(ledger=seal(state))
        self.assertEqual((d["action"], d["reason"]), ("NO_DISPATCH", "CADENCE_SLOT_ALREADY_DURABLE"))

    def test_recent_scan_and_recent_failed_attempt_block(self):
        self.assertEqual(decision(now=dt.datetime(2026, 10, 31, 20, 30, tzinfo=UTC))["action"],
                         "NO_DISPATCH")
        d = decision(runs=[scan(), scan(124, "2026-10-31T23:00:00Z", conclusion="failure")])
        self.assertEqual((d["action"], d["reason"]), ("NO_DISPATCH", "RECENT_SCAN_OR_ATTEMPT"))

    def test_active_or_queued_writer_blocks(self):
        for status in ("queued", "in_progress", "waiting", "requested", "pending"):
            with self.subTest(status=status):
                d = decision(runs=[scan(), scan(124, "2026-10-31T23:09:00Z",
                                              status=status, conclusion=None)])
                self.assertEqual((d["action"], d["reason"]), ("NO_DISPATCH", "SCANNER_ACTIVE_OR_QUEUED"))

    def test_newer_unsealed_success_and_cancelled_block(self):
        for conclusion in ("success", "cancelled", None):
            with self.subTest(conclusion=conclusion):
                d = decision(runs=[scan(), scan(124, "2026-10-31T22:00:00Z",
                                              conclusion=conclusion)])
                self.assertEqual(d["action"], "BLOCKED")

    def test_post_ledger_failure_recovery_after_spacing(self):
        d = decision(runs=[scan(conclusion="failure")])
        self.assertEqual(d["action"], "DISPATCH_EXISTING_WORKFLOW")
        d = decision(runs=[scan(), scan(124, "2026-10-31T22:00:00Z", conclusion="failure")])
        self.assertEqual(d["action"], "DISPATCH_EXISTING_WORKFLOW")

    def test_equal_second_ambiguous_run_blocks(self):
        d = decision(runs=[scan(), scan(124, "2026-10-31T20:10:00Z", conclusion="failure")])
        self.assertEqual((d["action"], d["reason"]), ("BLOCKED", "RUN_CREATED_AT_TIE_AMBIGUOUS"))

    def test_corrupt_ledger_or_provenance_blocks(self):
        state = fixture()
        state["predictions"][0]["price"] = 999
        self.assertEqual(decision(ledger=state)["action"], "BLOCKED")
        self.assertEqual(decision(message="paper: immutable scan 123 source " + "f"*40)["action"], "BLOCKED")
        self.assertEqual(decision(runs=[dict(scan(), head_sha="f"*40)])["action"], "BLOCKED")
        self.assertEqual(decision(commit="broken")["action"], "BLOCKED")
        self.assertEqual(decision(main="broken")["action"], "BLOCKED")

    def test_missing_api_and_intent_block(self):
        self.assertEqual(decide(None, [], fixture(), COMMIT, MESSAGE, MAIN, INTENT, NOW)["action"], "BLOCKED")
        self.assertEqual(decision(intent={})["action"], "BLOCKED")
        self.assertEqual(decision(runs=[])["action"], "BLOCKED")

    def test_bot_attempt_markers_dedup_both_controllers(self):
        for marker, reason in ((MARKER, "CADENCE_ALREADY_ATTEMPTED"),
                               ("PAPER_RECOVERY_ATTEMPT:", "RECOVERY_ALREADY_ATTEMPTED")):
            with self.subTest(marker=marker):
                comment = {"body": "<!-- " + marker + COMMIT + " -->",
                           "created_at": "2026-10-31T23:05:00Z", "user": BOT}
                self.assertEqual((decision(comments=[comment])["action"],
                                  decision(comments=[comment])["reason"]), ("NO_DISPATCH", reason))
                fake = copy.deepcopy(comment)
                fake["user"] = {"login": "attacker", "id": 99}
                self.assertEqual(decision(comments=[fake])["action"], "DISPATCH_EXISTING_WORKFLOW")
                malformed = copy.deepcopy(comment)
                malformed["created_at"] = "invalid"
                self.assertEqual(decision(comments=[malformed])["action"], "BLOCKED")

    def test_old_legacy_push_is_ignored_only_when_unambiguous(self):
        legacy = dict(scan(122, "2026-10-31T18:00:00Z"), event="push")
        self.assertEqual(decision(runs=[legacy, scan()])["action"], "DISPATCH_EXISTING_WORKFLOW")
        recent = dict(scan(124, "2026-10-31T22:00:00Z"), event="push")
        self.assertEqual(decision(runs=[recent, scan()])["action"], "BLOCKED")


if __name__ == "__main__":
    unittest.main()
