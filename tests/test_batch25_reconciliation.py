"""Batch 25 fixture-only receipt reconciliation acceptance."""
import tempfile
import unittest
from simple_scanner import fixture_delivery_outbox as outbox
from simple_scanner import fixture_receipt_reconciliation as recon

R={"status":"VERIFIED","buy_approved":False,"watch":[]}

class ReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=self.temp.name
        self.entry=outbox.stage(self.root,7,"scan-1",R)
        self.marker=recon.marker(7,"scan-1",self.entry["sha256"])

    def test_timeout_then_matching_existing_comment_confirms_without_post(self):
        self.assertEqual(recon.reconcile(self.root,7,[]),"UNRESOLVED_NO_REPOST")
        self.assertEqual(len(outbox.pending(self.root)),1)
        self.assertEqual(recon.reconcile(self.root,7,[{"id":91,"body":"receipt "+self.marker}]),"DELIVERED")
        self.assertEqual(outbox.pending(self.root),[])

    def test_duplicate_comments_stop_for_operator(self):
        result=recon.reconcile(self.root,7,[{"id":91,"body":self.marker},{"id":92,"body":self.marker}])
        self.assertEqual(result,"DUPLICATE_REQUIRES_OPERATOR")
        self.assertEqual(len(outbox.pending(self.root)),1)

    def test_wrong_issue_or_run_cannot_confirm(self):
        self.assertEqual(recon.reconcile(self.root,7,[{"id":91,"body":recon.marker(8,"scan-1",self.entry["sha256"])}]),"UNRESOLVED_NO_REPOST")
        self.assertEqual(recon.reconcile(self.root,7,[{"id":91,"body":recon.marker(7,"scan-2",self.entry["sha256"])}]),"UNRESOLVED_NO_REPOST")

    def test_incomplete_comment_listing_fails_closed(self):
        for evidence in (None,[{"id":91}],[{"id":"91","body":self.marker}]):
            with self.assertRaises(ValueError):
                recon.reconcile(self.root,7,evidence)
        self.assertEqual(len(outbox.pending(self.root)),1)

    def test_idempotent_reconciliation(self):
        comments=[{"id":91,"body":self.marker}]
        self.assertEqual(recon.reconcile(self.root,7,comments),"DELIVERED")
        self.assertEqual(recon.reconcile(self.root,7,comments),"NOT_PENDING")

    def test_invalid_digest_rejected(self):
        with self.assertRaises(ValueError):
            recon.marker(7,"scan-1","not-a-digest")

if __name__=="__main__":
    unittest.main()
