import unittest
from copy import deepcopy
from paper_pov.learning_delivery import verify_learning_delivery
from paper_pov.shadow_learning_evidence import canonical_digest


class LearningDeliveryTests(unittest.TestCase):
    def setUp(self):
        sha="a"*40
        self.run=dict(id=8,head_branch="main",event="workflow_dispatch",head_sha="b"*40)
        self.job=dict(name="market-wide-shadow-learning",run_id=8,head_sha="b"*40,
                      status="completed",conclusion="success")
        self.art=dict(name="market-wide-learning-continuity-main-8",expired=False,
                      workflow_run=dict(id=8,head_branch="main",head_sha="b"*40))
        self.source=dict(schema=2,status="SUCCESS_PAPER_ONLY",publication_mode="ATOMIC_LEDGER_RESULTS",
                         remote_readback_verified=True,production_applied=False,buy_approved=False,
                         run_id="9",source_sha=sha,ledger_generation=10,ledger_sha256="c"*64,
                         as_of="2026-11-19T06:00:00Z")
        self.writer=dict(id=9,head_branch="main",head_sha=sha,status="completed",conclusion="success")
        self.receipt=dict(schema="market_wide_learning_receipt_v1",learning_scope="main",
                          production_applied=False,promotion_authorized=False,writer_run_id="9",
                          source_sha=sha,ledger_generation=10,ledger_sha256="c"*64,
                          evaluation_asof_utc="2026-11-19T06:00:00Z",
                          source_authenticated=False,measured_lift_verified=False)
        self.seal()
        self.delivered=deepcopy(self.source)

    def seal(self):
        self.receipt["digest"]=canonical_digest({k:v for k,v in self.receipt.items() if k!="digest"})

    def verify(self):
        return verify_learning_delivery(self.receipt,self.run,self.job,self.art,
                                        self.source,self.writer,self.delivered)

    def test_current_and_lag_preserve_evidence(self):
        self.assertEqual(self.verify()["status"],"CURRENT")
        self.delivered.update(ledger_generation=12,run_id="11",ledger_sha256="d"*64,
                              as_of="2026-11-19T06:10:00Z")
        result=self.verify()
        self.assertEqual(result["status"],"LAGGING")
        self.assertEqual(result["generation_lag"],2)
        self.assertFalse(result["receipt"]["source_authenticated"])
        self.assertFalse(result["receipt"]["measured_lift_verified"])

    def test_pr_or_failed_job_rejected(self):
        self.run["head_branch"]="learning-market-wide-20261117"
        with self.assertRaisesRegex(ValueError,"owner"):
            self.verify()
        self.run["head_branch"]="main"
        self.job["conclusion"]="failure"
        with self.assertRaisesRegex(ValueError,"owner"):
            self.verify()

    def test_artifact_and_receipt_tampering_rejected(self):
        self.art["workflow_run"]["id"]=7
        with self.assertRaisesRegex(ValueError,"artifact"):
            self.verify()
        self.art["workflow_run"]["id"]=8
        self.receipt["ledger_sha256"]="e"*64
        with self.assertRaisesRegex(ValueError,"receipt"):
            self.verify()
        self.seal()
        with self.assertRaisesRegex(ValueError,"provenance"):
            self.verify()

    def test_source_writer_and_future_generation_rejected(self):
        self.writer["conclusion"]="failure"
        with self.assertRaisesRegex(ValueError,"writer"):
            self.verify()
        self.writer["conclusion"]="success"
        self.delivered["ledger_generation"]=9
        with self.assertRaisesRegex(ValueError,"generation"):
            self.verify()

    def test_equal_generation_must_match_source(self):
        self.delivered["ledger_sha256"]="d"*64
        with self.assertRaisesRegex(ValueError,"Equal-generation"):
            self.verify()
