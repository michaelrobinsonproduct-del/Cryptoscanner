"""Offline-only adversarial recovery reconciliation; synthetic IDs, no live API."""
import datetime as dt
import unittest
from paper_pov.slot_claim_protocol import prepare, OWNER_ID
from paper_pov.slot_recovery_reconciliation import reconcile

S = dt.datetime(2026, 11, 2, 21, 0, tzinfo=dt.timezone.utc)
SOURCE = "e3fb5ec272d74a72f19e306c1825aae1b7960576"


def fixture():
    claim = prepare(slot=S, now=S + dt.timedelta(minutes=12),
                    source_sha=SOURCE, main_sha=SOURCE, ledger_commit="a"*40,
                    decision_sha256="b"*64, controller_run_id=99991,
                    owner_comment_id=99992, owner_id=OWNER_ID)
    tag_sha = "c"*40
    return dict(
        claim=claim, tag_ref_sha=tag_sha,
        tag=dict(authenticated=True, sha=tag_sha, name=claim["tag_name"],
                 target_sha=SOURCE, message=claim["message"]),
        runs=[dict(authenticated=True, id=99993, workflow="paper-pipeline.yml",
                   event="workflow_dispatch", head_sha=SOURCE, run_attempt=1,
                   slot_utc=claim["slot_utc"], status="completed", conclusion="success")],
        receipts=[dict(authenticated=True, claim_digest=claim["digest"],
                       slot_utc=claim["slot_utc"], source_sha=SOURCE,
                       controller_run_id=99991, origin="external_owner_recovery",
                       run_id=99993)],
        ledger=dict(authenticated=True, remote_readback=True, source_sha=SOURCE,
                    run_id=99993, claim_digest=claim["digest"], generation=58,
                    sha256="d"*64, scan_id="synthetic-scan-58"),
        delivery=dict(authenticated=True, run_id=99993, published=True,
                      user_receipt=False))


class RecoveryReconciliationTests(unittest.TestCase):
    def test_bounded_success_never_claims_native_or_global_proof(self):
        r = reconcile(**fixture())
        self.assertEqual(r["status"], "RECONCILED")
        self.assertTrue(r["github_publication_verified"])
        for key in ("native_schedule_proven", "global_writer_exclusivity_proven",
                    "retry_authorized", "user_receipt_verified", "dispatch_executed"):
            self.assertFalse(r[key])

    def test_claim_without_receipt_is_stranded_and_not_retried(self):
        a = fixture(); a["receipts"] = []
        r = reconcile(**a)
        self.assertEqual(r["reason"], "CLAIMED_WITHOUT_DISPATCH_RECEIPT")
        self.assertFalse(r["retry_authorized"])

    def test_missing_ref_abstains(self):
        a = fixture(); a["tag_ref_sha"] = None
        self.assertEqual(reconcile(**a)["status"], "UNVERIFIED")

    def test_tampered_tag_fails(self):
        a = fixture(); a["tag"]["message"] += "tampered"
        self.assertEqual(reconcile(**a)["reason"], "CLAIM_REF_OR_TAG_MISMATCH")

    def test_duplicate_receipts_fail(self):
        a = fixture(); a["receipts"].append(dict(a["receipts"][0]))
        self.assertEqual(reconcile(**a)["reason"], "MULTIPLE_DISPATCH_RECEIPTS")

    def test_owner_controller_drift_fails(self):
        a = fixture(); a["receipts"][0]["controller_run_id"] = 4
        self.assertEqual(reconcile(**a)["reason"], "CONFLICTING_OR_UNAUTHENTICATED_RECEIPT")

    def test_untrusted_receipt_fails(self):
        a = fixture(); a["receipts"][0]["authenticated"] = False
        self.assertEqual(reconcile(**a)["status"], "FAILED")

    def test_native_schedule_cannot_masquerade_as_recovery(self):
        a = fixture(); a["runs"][0]["event"] = "schedule"
        self.assertEqual(reconcile(**a)["reason"], "WRITER_RUN_ORIGIN_MISMATCH")

    def test_rerun_attempt_rejected(self):
        a = fixture(); a["runs"][0]["run_attempt"] = 2
        self.assertEqual(reconcile(**a)["status"], "FAILED")

    def test_native_and_recovery_same_slot_are_duplicate(self):
        a = fixture(); a["runs"].append(dict(a["runs"][0], id=99994, event="schedule"))
        self.assertEqual(reconcile(**a)["reason"], "MULTIPLE_WRITER_RUNS_FOR_SLOT")

    def test_failed_writer_does_not_prove_delivery(self):
        a = fixture(); a["runs"][0]["conclusion"] = "failure"
        self.assertEqual(reconcile(**a)["status"], "UNVERIFIED")

    def test_ledger_readback_missing_abstains(self):
        a = fixture(); a["ledger"]["remote_readback"] = False
        self.assertEqual(reconcile(**a)["reason"], "CANONICAL_LEDGER_LINK_NOT_PROVEN")

    def test_ledger_identity_mismatch_abstains(self):
        for change in ({"run_id": 4}, {"generation": 0}, {"claim_digest": "f"*64}):
            with self.subTest(change=change):
                a = fixture(); a["ledger"].update(change)
                self.assertEqual(reconcile(**a)["status"], "UNVERIFIED")

    def test_missing_publication_abstains(self):
        a = fixture(); a["delivery"]["published"] = False
        self.assertEqual(reconcile(**a)["reason"], "RESULTS_PUBLICATION_NOT_PROVEN")

    def test_user_receipt_requires_authenticated_delivery(self):
        a = fixture(); a["delivery"]["user_receipt"] = True
        self.assertTrue(reconcile(**a)["user_receipt_verified"])
        a["delivery"]["authenticated"] = False
        self.assertFalse(reconcile(**a)["user_receipt_verified"])

    def test_invalid_claim_blocks_before_evidence(self):
        a = fixture(); a["claim"]["digest"] = "0"*64
        self.assertEqual(reconcile(**a)["reason"], "INVALID_CLAIM")


if __name__ == "__main__":
    unittest.main()
