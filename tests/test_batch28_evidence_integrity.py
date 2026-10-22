"""Batch 28: immutable fixture receipt evidence and isolated rollback guards."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import fixture_delivery_outbox as outbox
from simple_scanner import fixture_receipt_reconciliation as recon

RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[{"symbol":"BTC"}]}

class Batch28Evidence(unittest.TestCase):
    def test_conflicting_comment_confirmation_cannot_change_delivered_result(self):
        with tempfile.TemporaryDirectory() as root:
            entry=outbox.stage(root,41,"run-41",RECEIPT)
            delivered=outbox.confirm(root,41,"run-41",entry["sha256"],701)
            with self.assertRaises(RuntimeError):
                outbox.confirm(root,41,"run-41",entry["sha256"],702)
            self.assertEqual(outbox.stage(root,41,"run-41",RECEIPT),delivered)

    def test_tampered_digest_fails_closed_and_preserves_file(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,41,"run-41",RECEIPT)
            path=Path(root,outbox.FILENAME)
            state=json.loads(path.read_text())
            state["entries"]["41"]["sha256"]="0"*64
            path.write_text(json.dumps(state))
            before=path.read_bytes()
            with self.assertRaises(RuntimeError):
                outbox.stage(root,42,"run-42",RECEIPT)
            self.assertEqual(path.read_bytes(),before)

    def test_ambiguous_duplicate_evidence_cannot_auto_confirm(self):
        with tempfile.TemporaryDirectory() as root:
            entry=outbox.stage(root,41,"run-41",RECEIPT)
            token=recon.marker(41,"run-41",entry["sha256"])
            self.assertEqual(recon.reconcile(root,41,[{"id":701,"body":token},{"id":702,"body":token}]),"DUPLICATE_REQUIRES_OPERATOR")
            self.assertEqual(outbox.pending(root)[0]["status"],"PENDING")

    def test_interrupted_confirm_preserves_previous_pending_receipt(self):
        with tempfile.TemporaryDirectory() as root:
            entry=outbox.stage(root,41,"run-41",RECEIPT)
            with patch.object(outbox.os,"replace",side_effect=OSError("fixture disk fault")):
                with self.assertRaises(OSError):
                    outbox.confirm(root,41,"run-41",entry["sha256"],701)
            self.assertEqual(outbox.pending(root)[0],entry)

if __name__=="__main__":
    unittest.main()
