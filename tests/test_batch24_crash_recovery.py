"""Batch 24 isolated crash/reconciliation acceptance. No HTTP or live scans."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import fixture_delivery_outbox as outbox

RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[{"symbol":"BTC/USD","score":50}]}

class RecoveryAcceptance(unittest.TestCase):
    def test_crash_before_atomic_replace_retains_prior_pending(self):
        with tempfile.TemporaryDirectory() as root:
            original=outbox.stage(root,11,"run-1",RECEIPT)
            with patch.object(outbox.os,"replace",side_effect=OSError("fixture crash")):
                with self.assertRaises(OSError):
                    outbox.confirm(root,11,"run-1",original["sha256"],101)
            self.assertEqual(outbox.pending(root),[original])
            self.assertEqual(list(Path(root).glob(".fixture_outbox_*")),[])

    def test_restarted_process_reads_pending_without_new_scan(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,11,"run-1",RECEIPT)
            pending=outbox.pending(root)
            self.assertEqual(len(pending),1)
            # An ambiguous POST timeout does not establish delivery.
            self.assertEqual(pending[0]["status"],"PENDING")
            outbox.confirm(root,11,"run-1",pending[0]["sha256"],999)
            self.assertEqual(outbox.pending(root),[])

    def test_wrong_receipt_hash_does_not_reconcile(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,11,"run-1",RECEIPT)
            with self.assertRaises(RuntimeError):
                outbox.confirm(root,11,"run-1","0"*64,999)
            self.assertEqual(len(outbox.pending(root)),1)

    def test_two_manual_requests_are_independently_confirmed(self):
        with tempfile.TemporaryDirectory() as root:
            a=outbox.stage(root,11,"run-1",RECEIPT)
            outbox.stage(root,12,"run-1",RECEIPT)
            outbox.confirm(root,11,"run-1",a["sha256"],999)
            self.assertEqual([r["issue_number"] for r in outbox.pending(root)],[12])

    def test_corrupt_delivery_state_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root,outbox.FILENAME).write_text(json.dumps({"entries":{"11":{"status":"UNKNOWN"}}}))
            with self.assertRaises(RuntimeError):
                outbox.pending(root)

if __name__=="__main__":
    unittest.main()
