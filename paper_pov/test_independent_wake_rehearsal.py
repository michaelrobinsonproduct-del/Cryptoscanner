"""Offline adversarial acceptance for independently clocked existing-writer path."""
import datetime as dt
import hashlib
import unittest
from pathlib import Path
from unittest.mock import patch

from paper_pov.independent_wake_rehearsal import (
    REPO, checkout_contracts, rehearse, validate_workflows,
)

NOW = dt.datetime(2026, 11, 2, 19, 20, tzinfo=dt.timezone.utc)
SHA = "e3fb5ec272d74a72f19e306c1825aae1b7960576"
OWNER = {"login": "michaelrobinsonproduct-del", "id": 336805669}


def sources():
    root = Path(__file__).resolve().parent.parent / ".github" / "workflows"
    return {n: (root / n).read_text() for n in
            ("paper-pipeline.yml", "paper-cadence-wake.yml",
             "paper-recovery.yml", "paper-external-heartbeat.yml")}


def event():
    return {
        "action": "created",
        "repository": {"full_name": REPO, "default_branch": "main", "owner": OWNER},
        "issue": {"number": 34, "state": "open", "pull_request": None},
        "comment": {"id": 1901, "body": "/paper-cadence-heartbeat",
                    "created_at": NOW.isoformat(), "author_association": "OWNER",
                    "user": OWNER},
        "sender": OWNER,
    }


def args():
    return dict(event=event(), repository=REPO, actor=OWNER["login"],
                ref="refs/heads/main", event_name="issue_comment", now=NOW,
                checkout_sha=SHA, main_sha=SHA, sources=sources(),
                runs_payload={"workflow_runs": []}, comments=[], ledger={},
                ledger_commit="a" * 40, ledger_message="")


CANDIDATE = {"action": "DISPATCH_EXISTING_WORKFLOW",
             "reason": "INDEPENDENT_CADENCE_DUE",
             "source_sha": SHA, "target_slot": "2026-11-02T19:00:00+00:00",
             "attempt_marker": "PAPER_CADENCE_ATTEMPT:" + "a" * 40,
             "ledger_generation": 55, "anchor_run_id": 41473947157}
CANDIDATE["decision_sha256"] = hashlib.sha256(
    ("a" * 40 + "|41473947157|2026-11-02T19:00:00+00:00|" + SHA).encode()
).hexdigest()


class IndependentWakeTests(unittest.TestCase):
    def test_exact_checkout_has_one_writer_and_shared_controller_mutex(self):
        c = checkout_contracts(Path(__file__).resolve().parent.parent)
        self.assertEqual(c["single_writer"], "paper-pipeline.yml")
        self.assertFalse(c["durable_slot_cas_proven"])
        self.assertEqual(c["pending_queue_mode"], "single")
        self.assertTrue(c["pending_replacement_risk"])

    def test_eligible_candidate_never_dispatches_or_claims_live_recovery(self):
        with patch("paper_pov.independent_wake_rehearsal.decide", return_value=CANDIDATE):
            result = rehearse(**args())
        self.assertEqual(result["action"], "DRY_RUN_CANDIDATE_ONLY")
        self.assertEqual(result["proposed_target"], "paper-pipeline.yml")
        for key in ("dispatch_executed", "ledger_written", "scanner_executed",
                    "native_schedule_claimed", "production_authorized",
                    "durable_slot_cas_proven"):
            self.assertFalse(result[key], key)

    def test_controller_duplicate_suppression_is_preserved(self):
        with patch("paper_pov.independent_wake_rehearsal.decide",
                   return_value={"action": "NO_DISPATCH",
                                 "reason": "CADENCE_ALREADY_ATTEMPTED"}):
            result = rehearse(**args())
        self.assertEqual(result["action"], "NO_DISPATCH")
        self.assertEqual(result["reason"], "CADENCE_ALREADY_ATTEMPTED")

    def test_unavailable_live_ledger_abstains_without_mock(self):
        result = rehearse(**args())
        self.assertNotEqual(result["action"], "DRY_RUN_CANDIDATE_ONLY")

    def test_wrong_source_abstains(self):
        a = args()
        a["checkout_sha"] = "b" * 40
        self.assertEqual(rehearse(**a)["reason"], "EXACT_MAIN_SOURCE_MISMATCH")

    def test_foreign_actor_abstains(self):
        a = args()
        a["actor"] = "untrusted"
        self.assertEqual(rehearse(**a)["action"], "BLOCKED")

    def test_foreign_comment_author_abstains(self):
        a = args()
        a["event"]["comment"]["user"] = {"login": "untrusted", "id": 7}
        self.assertEqual(rehearse(**a)["action"], "BLOCKED")

    def test_untrusted_command_abstains(self):
        a = args()
        a["event"]["comment"]["body"] = "/paper-recovery-heartbeat"
        self.assertEqual(rehearse(**a)["action"], "BLOCKED")

    def test_stale_event_abstains(self):
        a = args()
        a["event"]["comment"]["created_at"] = "2026-11-01T00:00:00Z"
        self.assertEqual(rehearse(**a)["action"], "BLOCKED")

    def test_bad_writer_mutex_abstains(self):
        a = args()
        a["sources"]["paper-pipeline.yml"] = a["sources"]["paper-pipeline.yml"].replace(
            "cancel-in-progress: false", "cancel-in-progress: true")
        self.assertEqual(rehearse(**a)["reason"], "WRITER_MUTEX_DRIFT")

    def test_second_writer_entrypoint_abstains(self):
        a = args()
        a["sources"]["paper-pipeline.yml"] += "\npython -m paper_pov.scanner\n"
        self.assertEqual(rehearse(**a)["reason"], "WRITER_ENTRYPOINT_DRIFT")

    def test_controller_mutex_drift_abstains(self):
        a = args()
        a["sources"]["paper-cadence-wake.yml"] = a["sources"]["paper-cadence-wake.yml"].replace(
            "group: public-paper-recovery-controller", "group: wrong-mutex")
        self.assertEqual(rehearse(**a)["reason"], "CADENCE_CONTROLLER_DRIFT")

    def test_recovery_controller_direct_scan_abstains(self):
        a = args()
        a["sources"]["paper-recovery.yml"] += "\npython -m paper_pov.scanner\n"
        self.assertEqual(rehearse(**a)["reason"], "RECOVERY_CONTROLLER_DRIFT")

    def test_external_owner_gate_removed_abstains(self):
        a = args()
        a["sources"]["paper-external-heartbeat.yml"] = a["sources"]["paper-external-heartbeat.yml"].replace(
            "github.event.comment.user.id == 336805669", "true")
        self.assertEqual(rehearse(**a)["reason"], "EXTERNAL_OWNER_EVENT_DRIFT")

    def test_external_recovery_target_changed_abstains(self):
        a = args()
        a["sources"]["paper-external-heartbeat.yml"] = a["sources"]["paper-external-heartbeat.yml"].replace(
            "workflow_id = 'paper-recovery.yml'", "workflow_id = 'other.yml'")
        self.assertEqual(rehearse(**a)["reason"], "EXTERNAL_RECOVERY_TARGET_DRIFT")

    def test_malformed_positive_decision_abstains(self):
        with patch("paper_pov.independent_wake_rehearsal.decide",
                   return_value={"action": "DISPATCH_EXISTING_WORKFLOW",
                                 "source_sha": "f" * 40, "attempt_marker": "x"}):
            result = rehearse(**args())
        self.assertEqual(result["action"], "BLOCKED")
        self.assertEqual(result["reason"], "UNBOUND_CANDIDATE_SOURCE_OR_MARKER")

    def test_unsupported_decision_abstains(self):
        with patch("paper_pov.independent_wake_rehearsal.decide",
                   return_value={"action": "EXECUTE_SCANNER"}):
            self.assertEqual(rehearse(**args())["reason"],
                             "UNTRUSTED_CONTROLLER_DECISION")

    def test_naive_clock_abstains(self):
        a = args()
        a["now"] = NOW.replace(tzinfo=None)
        self.assertEqual(rehearse(**a)["reason"], "INVALID_CLOCK")

    def test_missing_target_slot_abstains(self):
        bad = dict(CANDIDATE)
        bad.pop("target_slot")
        with patch("paper_pov.independent_wake_rehearsal.decide", return_value=bad):
            self.assertEqual(rehearse(**args())["reason"], "UNBOUND_CANDIDATE_SLOT_OR_DECISION")

    def test_wrong_target_slot_abstains(self):
        bad = dict(CANDIDATE, target_slot="2026-11-02T18:30:00+00:00")
        with patch("paper_pov.independent_wake_rehearsal.decide", return_value=bad):
            self.assertEqual(rehearse(**args())["reason"], "UNBOUND_CANDIDATE_SLOT_OR_DECISION")

    def test_wrong_decision_digest_abstains(self):
        bad = dict(CANDIDATE, decision_sha256="0" * 64)
        with patch("paper_pov.independent_wake_rehearsal.decide", return_value=bad):
            self.assertEqual(rehearse(**args())["reason"], "UNBOUND_CANDIDATE_SLOT_OR_DECISION")

    def test_wrong_anchor_abstains(self):
        bad = dict(CANDIDATE, anchor_run_id=41473947158)
        with patch("paper_pov.independent_wake_rehearsal.decide", return_value=bad):
            self.assertEqual(rehearse(**args())["reason"], "UNBOUND_CANDIDATE_SLOT_OR_DECISION")

    def test_missing_generation_abstains(self):
        bad = dict(CANDIDATE, ledger_generation=None)
        with patch("paper_pov.independent_wake_rehearsal.decide", return_value=bad):
            self.assertEqual(rehearse(**args())["reason"], "UNBOUND_CANDIDATE_SLOT_OR_DECISION")

    def test_wrong_attempt_marker_suffix_abstains(self):
        bad = dict(CANDIDATE, attempt_marker="PAPER_CADENCE_ATTEMPT:" + "b" * 40)
        with patch("paper_pov.independent_wake_rehearsal.decide", return_value=bad):
            self.assertEqual(rehearse(**args())["reason"], "UNBOUND_CANDIDATE_SLOT_OR_DECISION")

    def test_mismatched_ledger_commit_abstains(self):
        a = args()
        a["ledger_commit"] = "b" * 40
        with patch("paper_pov.independent_wake_rehearsal.decide", return_value=CANDIDATE):
            self.assertEqual(rehearse(**a)["reason"], "UNBOUND_CANDIDATE_SLOT_OR_DECISION")

    def test_candidate_outside_slot_grace_abstains(self):
        a = args()
        a["now"] = NOW.replace(minute=29, second=1)
        a["event"]["comment"]["created_at"] = a["now"].isoformat()
        with patch("paper_pov.independent_wake_rehearsal.decide", return_value=CANDIDATE):
            self.assertEqual(rehearse(**a)["reason"], "UNBOUND_CANDIDATE_SLOT_OR_DECISION")

    def test_writer_mutex_false_elsewhere_cannot_bypass_drift(self):
        a = args()
        w = a["sources"]["paper-pipeline.yml"]
        a["sources"]["paper-pipeline.yml"] = w.replace(
            "cancel-in-progress: false", "cancel-in-progress: true", 1) + (
            "\n# cancel-in-progress: false\n")
        self.assertEqual(rehearse(**a)["reason"], "WRITER_MUTEX_DRIFT")

    def test_controller_mutex_false_elsewhere_cannot_bypass_drift(self):
        a = args()
        w = a["sources"]["paper-cadence-wake.yml"]
        a["sources"]["paper-cadence-wake.yml"] = w.replace(
            "cancel-in-progress: false", "cancel-in-progress: true", 1) + (
            "\n# cancel-in-progress: false\n")
        self.assertEqual(rehearse(**a)["reason"], "CADENCE_CONTROLLER_DRIFT")

    def test_unsupported_queue_mode_abstains(self):
        a = args()
        w = a["sources"]["paper-pipeline.yml"]
        a["sources"]["paper-pipeline.yml"] = w.replace(
            "cancel-in-progress: false", "cancel-in-progress: false\n  queue: invalid", 1)
        self.assertEqual(rehearse(**a)["reason"], "WRITER_QUEUE_DRIFT")

    def test_queue_max_proposal_still_does_not_prove_slot_cas(self):
        a = args()
        w = a["sources"]["paper-pipeline.yml"]
        a["sources"]["paper-pipeline.yml"] = w.replace(
            "cancel-in-progress: false", "cancel-in-progress: false\n  queue: max", 1)
        c = validate_workflows(a["sources"])
        self.assertEqual(c["pending_queue_mode"], "max")
        self.assertFalse(c["pending_replacement_risk"])
        self.assertFalse(c["durable_slot_cas_proven"])


if __name__ == "__main__":
    unittest.main()
