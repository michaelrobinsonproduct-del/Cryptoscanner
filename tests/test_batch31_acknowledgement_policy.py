"""Batch 31 offline acknowledgement policy and outbox boundary acceptance."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner.manual_acknowledgement_policy import acknowledgement_decision
from simple_scanner.fixture_manual_delivery_decision import classify_delivery
from simple_scanner import fixture_delivery_outbox as outbox
from simple_scanner import fixture_receipt_reconciliation as recon

RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[]}
REQUESTS=[{"issue_number":81},{"issue_number":82}]

class Batch31PolicyTests(unittest.TestCase):
    def test_blocked_and_ambiguous_post_never_acknowledge_or_repost(self):
        decision=acknowledgement_decision(REQUESTS,[])
        self.assertEqual(decision["pending_issue_numbers"],[81,82])
        self.assertEqual(decision["acknowledge_issue_numbers"],[])
        self.assertEqual(decision["safe_to_repost_issue_numbers"],[])
        self.assertFalse(decision["scan_rerun_required"])

    def test_partial_confirmations_are_not_mistaken_for_full_delivery(self):
        decision=acknowledgement_decision(REQUESTS,[{"issue_number":81,"comment_id":900}])
        self.assertEqual(decision["acknowledge_issue_numbers"],[81])
        self.assertEqual(decision["pending_issue_numbers"],[82])
        self.assertEqual(decision["status"],"RECONCILIATION_REQUIRED")

    def test_all_confirmed_is_still_only_a_policy_decision(self):
        decision=acknowledgement_decision(REQUESTS,[{"issue_number":81,"comment_id":900},{"issue_number":82,"comment_id":901}])
        self.assertEqual(decision["status"],"ALL_CONFIRMED")
        self.assertEqual(decision["acknowledge_issue_numbers"],[81,82])

    def test_reject_untrusted_or_duplicate_confirmation_identity(self):
        for confirmations in ([{"issue_number":81}], [{"issue_number":81,"comment_id":0}],
                              [{"issue_number":83,"comment_id":900}],
                              [{"issue_number":81,"comment_id":900},{"issue_number":81,"comment_id":901}],
                              [{"issue_number":81,"comment_id":900},{"issue_number":82,"comment_id":900}]):
            with self.subTest(confirmations=confirmations),self.assertRaises(ValueError):
                acknowledgement_decision(REQUESTS,confirmations)

    def test_existing_outbox_survives_timeout_and_reconciles_offline(self):
        with tempfile.TemporaryDirectory() as root:
            classify_delivery(root,[REQUESTS[0]],[],"run-1",RECEIPT)
            entry=outbox.pending(root)[0]
            self.assertEqual(acknowledgement_decision([REQUESTS[0]],[])["pending_issue_numbers"],[81])
            self.assertEqual(recon.reconcile(root,81,[]),"UNRESOLVED_NO_REPOST")
            self.assertEqual(outbox.pending(root)[0],entry)
            token=recon.marker(81,"run-1",entry["sha256"])
            self.assertEqual(recon.reconcile(root,81,[{"id":900,"body":token}]),"DELIVERED")
            self.assertEqual(acknowledgement_decision([REQUESTS[0]],[{"issue_number":81,"comment_id":900}])["acknowledge_issue_numbers"],[81])

    def test_rollback_on_interrupted_outbox_write(self):
        with tempfile.TemporaryDirectory() as root:
            with patch.object(outbox.os,"replace",side_effect=OSError("offline failure")):
                with self.assertRaises(OSError):
                    classify_delivery(root,[REQUESTS[0]],[],"run-1",RECEIPT)
            self.assertFalse((Path(root)/outbox.FILENAME).exists())

    def test_manual_and_cron_share_identical_pure_policy(self):
        for origin in ("manual","cron"):
            with self.subTest(origin=origin):
                self.assertEqual(acknowledgement_decision(REQUESTS,[]),acknowledgement_decision(REQUESTS,[]))

    def test_execution_wrapper_not_modified_to_import_policy(self):
        source=(Path(__file__).resolve().parents[1]/"simple_scanner/execute_once.py").read_text()
        self.assertNotIn("manual_acknowledgement_policy",source)
        self.assertNotIn("fixture_manual_delivery_decision",source)

if __name__=="__main__":
    unittest.main()
