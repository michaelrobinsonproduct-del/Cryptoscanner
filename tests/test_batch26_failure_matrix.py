"""Batch 26 fixture-only failure matrix. Never calls live GitHub or scanner."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from simple_scanner import fixture_delivery_outbox as outbox
from simple_scanner import fixture_receipt_reconciliation as reconcile

RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[]}

class Batch26FailureMatrix(unittest.TestCase):
    def test_atomic_stage_failure_leaves_no_false_delivery_or_partial_file(self):
        with tempfile.TemporaryDirectory() as root:
            with patch.object(outbox.os,"replace",side_effect=OSError("disk failure")):
                with self.assertRaises(OSError):
                    outbox.stage(root,19,"run-a",RECEIPT)
            self.assertEqual(outbox.pending(root),[])
            self.assertEqual(list(Path(root).glob(".fixture_outbox_*")),[])

    def test_two_requests_one_reconciled_one_still_pending(self):
        with tempfile.TemporaryDirectory() as root:
            a=outbox.stage(root,19,"run-a",RECEIPT)
            outbox.stage(root,20,"run-a",RECEIPT)
            marker=reconcile.marker(19,"run-a",a["sha256"])
            self.assertEqual(reconcile.reconcile(root,19,[{"id":500,"body":marker}]),"DELIVERED")
            self.assertEqual([e["issue_number"] for e in outbox.pending(root)],[20])

    def test_duplicate_comment_evidence_never_marks_delivered(self):
        with tempfile.TemporaryDirectory() as root:
            a=outbox.stage(root,19,"run-a",RECEIPT)
            marker=reconcile.marker(19,"run-a",a["sha256"])
            comments=[{"id":500,"body":marker},{"id":501,"body":marker}]
            self.assertEqual(reconcile.reconcile(root,19,comments),"DUPLICATE_REQUIRES_OPERATOR")
            self.assertEqual(len(outbox.pending(root)),1)

    def test_corrupt_state_does_not_get_replaced_by_new_receipt(self):
        with tempfile.TemporaryDirectory() as root:
            file=Path(root,outbox.FILENAME)
            original='{"entries":{"19":{"status":"INVALID"}}}'
            file.write_text(original)
            with self.assertRaises(RuntimeError):
                outbox.stage(root,20,"run-a",RECEIPT)
            self.assertEqual(file.read_text(),original)

    def test_delivered_receipt_is_not_reopened_on_repeated_stage(self):
        with tempfile.TemporaryDirectory() as root:
            first=outbox.stage(root,19,"run-a",RECEIPT)
            outbox.confirm(root,19,"run-a",first["sha256"],500)
            again=outbox.stage(root,19,"run-a",RECEIPT)
            self.assertEqual(again["status"],"DELIVERED")
            self.assertEqual(outbox.pending(root),[])

if __name__=="__main__":
    unittest.main()
