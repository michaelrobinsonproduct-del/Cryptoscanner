"""Batch 27 isolated release blockers and outbox failure guards.

No network, live database, production execution, or deploy operations.
"""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import fixture_delivery_outbox as outbox
from simple_scanner import fixture_receipt_reconciliation as recon

RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[{"symbol":"BTC/USD"}]}

class Batch27Acceptance(unittest.TestCase):
    def test_corrupted_receipt_body_is_detectable_but_not_yet_rejected(self):
        # Documents an important limitation: persisted SHA is not revalidated on read.
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,10,"run-10",RECEIPT)
            path=Path(root,outbox.FILENAME)
            state=json.loads(path.read_text())
            state["entries"]["10"]["receipt"]["watch"][0]["symbol"]="FORGED"
            path.write_text(json.dumps(state))
            entry=outbox.pending(root)[0]
            self.assertNotEqual(recon.receipt_digest(entry["receipt"]),entry["sha256"])

    def test_rollback_atomic_write_preserves_preexisting_pending(self):
        with tempfile.TemporaryDirectory() as root:
            first=outbox.stage(root,10,"run-10",RECEIPT)
            with patch.object(outbox.os,"replace",side_effect=OSError("fixture disk unavailable")):
                with self.assertRaises(OSError):
                    outbox.stage(root,11,"run-10",RECEIPT)
            self.assertEqual(outbox.pending(root),[first])

    def test_receipt_identity_cannot_be_changed_by_restage(self):
        with tempfile.TemporaryDirectory() as root:
            first=outbox.stage(root,10,"run-10",RECEIPT)
            with self.assertRaises(RuntimeError):
                outbox.stage(root,10,"run-11",RECEIPT)
            self.assertEqual(outbox.pending(root),[first])

    def test_no_matching_comment_means_no_automatic_retry(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,10,"run-10",RECEIPT)
            self.assertEqual(recon.reconcile(root,10,[]),"UNRESOLVED_NO_REPOST")
            self.assertEqual(len(outbox.pending(root)),1)

if __name__=="__main__":
    unittest.main()
