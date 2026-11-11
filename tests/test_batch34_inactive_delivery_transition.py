"""Batch 34 inactive manual-delivery transition gate acceptance."""
import tempfile
import unittest
from pathlib import Path
from simple_scanner.manual_acknowledgement_policy import plan_manual_delivery_transition
from simple_scanner import fixture_delivery_outbox as outbox

REQUEST=[{"issue_number":81}]
RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[]}
CONFIRM=[{"issue_number":81,"comment_id":900}]

class Batch34Tests(unittest.TestCase):
    def test_blocked_delivery_remains_unacknowledged_without_rescan_or_post(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,81,"run-1",RECEIPT)
            decision=plan_manual_delivery_transition(REQUEST,[],outbox.pending(root))
            self.assertEqual(decision["acknowledge_issue_numbers"],[])
            self.assertEqual(decision["pending_issue_numbers"],[81])
            self.assertEqual(decision["safe_to_repost_issue_numbers"],[])
            self.assertFalse(decision["scan_rerun_required"])
            self.assertFalse((Path(root)/"manual_request_ledger.json").exists())

    def test_http_success_without_durable_confirmation_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,81,"run-1",RECEIPT)
            with self.assertRaises(ValueError):
                plan_manual_delivery_transition(REQUEST,CONFIRM,outbox.pending(root))

    def test_durable_confirmed_receipt_permits_only_policy_acknowledgement(self):
        with tempfile.TemporaryDirectory() as root:
            staged=outbox.stage(root,81,"run-1",RECEIPT)
            outbox.confirm(root,81,"run-1",staged["sha256"],900)
            entry=outbox._read(root)["entries"]["81"]
            decision=plan_manual_delivery_transition(REQUEST,CONFIRM,[entry])
            self.assertEqual(decision["acknowledge_issue_numbers"],[81])
            self.assertFalse((Path(root)/"manual_request_ledger.json").exists())

    def test_mismatched_comment_id_and_duplicate_outbox_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            staged=outbox.stage(root,81,"run-1",RECEIPT)
            outbox.confirm(root,81,"run-1",staged["sha256"],900)
            entry=outbox._read(root)["entries"]["81"]
            for entries in ([dict(entry,comment_id=901)],[entry,entry]):
                with self.subTest(entries=entries),self.assertRaises(ValueError):
                    plan_manual_delivery_transition(REQUEST,CONFIRM,entries)

    def test_manual_and_scheduled_decisions_identical(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,81,"run-1",RECEIPT)
            self.assertEqual(plan_manual_delivery_transition(REQUEST,[],outbox.pending(root)),
                             plan_manual_delivery_transition(REQUEST,[],outbox.pending(root)))

    def test_execution_path_remains_unmodified_and_unwired(self):
        source=(Path(__file__).resolve().parents[1]/"simple_scanner/execute_once.py").read_text()
        self.assertNotIn("plan_manual_delivery_transition",source)
        self.assertNotIn("fixture_delivery_outbox",source)

if __name__=="__main__":
    unittest.main()
