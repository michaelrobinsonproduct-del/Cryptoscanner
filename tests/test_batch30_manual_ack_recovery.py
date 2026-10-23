"""Batch 30 offline reproduction and safe manual delivery decision tests."""
import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner.fixture_manual_delivery_decision import classify_delivery
from simple_scanner import fixture_delivery_outbox as outbox
from simple_scanner import fixture_receipt_reconciliation as recon
from simple_scanner.manual_requests import acknowledge_requests,plan_requests,read_ledger

RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[]}

class Batch30Acceptance(unittest.TestCase):
    def setUp(self):
        self.now=dt.datetime.now(dt.timezone.utc)
        self.requests=[{"issue_number":81,"created_at":self.now.isoformat()}]

    def test_reproduce_legacy_acknowledgement_without_delivery(self):
        # Demonstrates the existing flaw in isolation; does NOT invoke execute_once.
        with tempfile.TemporaryDirectory() as root:
            acknowledged=acknowledge_requests(root,self.requests,"run-1")
            self.assertEqual(acknowledged["completed_issue_numbers"],[81])
            self.assertEqual(plan_requests(self.requests,read_ledger(root),self.now),[])
            self.assertFalse((Path(root)/outbox.FILENAME).exists())

    def test_blocked_delivery_keeps_durable_pending_without_ledger_ack(self):
        with tempfile.TemporaryDirectory() as root:
            result=classify_delivery(root,self.requests,[],"run-1",RECEIPT)
            self.assertEqual(result["status"],"RECONCILIATION_REQUIRED")
            self.assertEqual(result["safe_to_repost_issue_numbers"],[])
            self.assertEqual(result["safe_to_acknowledge_as_delivered_issue_numbers"],[])
            self.assertEqual(len(outbox.pending(root)),1)
            self.assertFalse((Path(root)/"manual_request_ledger.json").exists())

    def test_reported_success_without_comment_id_is_not_confirmed(self):
        with tempfile.TemporaryDirectory() as root:
            result=classify_delivery(root,self.requests,self.requests,"run-1",RECEIPT)
            self.assertEqual(result["delivery_reported_issue_numbers"],[81])
            self.assertEqual(result["confirmed_delivery_issue_numbers"],[])
            self.assertEqual(len(outbox.pending(root)),1)

    def test_ambiguous_timeout_no_rescan_and_verified_fixture_reconciliation(self):
        with tempfile.TemporaryDirectory() as root:
            first=classify_delivery(root,self.requests,[],"run-1",RECEIPT)
            second=classify_delivery(root,self.requests,[],"run-1",RECEIPT)
            self.assertEqual(first,second)
            self.assertEqual(recon.reconcile(root,81,[]),"UNRESOLVED_NO_REPOST")
            pending=outbox.pending(root)[0]
            token=recon.marker(81,"run-1",pending["sha256"])
            self.assertEqual(recon.reconcile(root,81,[{"id":900,"body":token}]),"DELIVERED")
            self.assertEqual(outbox.pending(root),[])

    def test_crash_during_stage_does_not_acknowledge(self):
        with tempfile.TemporaryDirectory() as root:
            with patch.object(outbox.os,"replace",side_effect=OSError("fixture write interrupted")):
                with self.assertRaises(OSError):
                    classify_delivery(root,self.requests,[],"run-1",RECEIPT)
            self.assertFalse((Path(root)/"manual_request_ledger.json").exists())
            self.assertEqual(outbox.pending(root),[])

    def test_manual_cron_same_offline_decision(self):
        with tempfile.TemporaryDirectory() as manual, tempfile.TemporaryDirectory() as cron:
            a=classify_delivery(manual,self.requests,[],"run-1",RECEIPT)
            b=classify_delivery(cron,self.requests,[],"run-1",RECEIPT)
            self.assertEqual(a,b)

    def test_reject_duplicate_or_foreign_delivery_evidence(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(ValueError):
                classify_delivery(root,self.requests,[{"issue_number":82}],"run-1",RECEIPT)
            with self.assertRaises(ValueError):
                classify_delivery(root,self.requests,self.requests*2,"run-1",RECEIPT)
            self.assertEqual(outbox.pending(root),[])

if __name__=="__main__":
    unittest.main()
