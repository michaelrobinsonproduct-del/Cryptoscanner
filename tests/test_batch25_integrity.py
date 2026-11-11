"""Batch 25 fixture-only negative evidence and regression guards."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import fixture_delivery_outbox as outbox
from simple_scanner import fixture_receipt_reconciliation as recon
from simple_scanner.offline_scoring_comparison import compare_cohorts
from simple_scanner.offline_replay import cohort_split
from simple_scanner.shadow_learning import score

RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[]}

class SafetyAcceptance(unittest.TestCase):
    def test_comment_contains_marker_as_substring_not_proof_of_authenticity(self):
        with tempfile.TemporaryDirectory() as root:
            entry=outbox.stage(root,7,"run-1",RECEIPT)
            token=recon.marker(7,"run-1",entry["sha256"])
            # Fixture reconciliation does not authenticate comment author or API completeness.
            self.assertEqual(recon.reconcile(root,7,[{"id":77,"body":token}]),"DELIVERED")

    def test_outbox_rejects_same_issue_different_receipt(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,7,"run-1",RECEIPT)
            with self.assertRaises(RuntimeError):
                outbox.stage(root,7,"run-1",{"status":"VERIFIED","buy_approved":False,"watch":[{"symbol":"ETH"}]})
            self.assertEqual(len(outbox.pending(root)),1)

    def test_rollback_of_failed_atomic_write_preserves_prior_delivered(self):
        with tempfile.TemporaryDirectory() as root:
            first=outbox.stage(root,7,"run-1",RECEIPT)
            outbox.confirm(root,7,"run-1",first["sha256"],88)
            with patch.object(outbox.os,"replace",side_effect=OSError("simulated interruption")):
                with self.assertRaises(OSError):
                    outbox.stage(root,8,"run-1",RECEIPT)
            self.assertEqual(outbox.pending(root),[])
            self.assertEqual(outbox.stage(root,7,"run-1",RECEIPT)["status"],"DELIVERED")

    def test_offline_holdout_never_verifies_production_scoring(self):
        rows=[(f't{i}',pair,momentum,volume,base,ret) for i in range(12)
              for pair,momentum,volume,base,ret in (("BTC",1.,1.,50.,2.),("ETH",3.,2.,45.,8.))]
        split=cohort_split(rows)
        result=compare_cohorts(split["holdout"],lambda row:score(row,3,4))
        self.assertFalse(result["promotion_eligible"])
        self.assertFalse(result["production_scoring_parity_verified"])
        self.assertTrue(all(p["timestamp"] not in split["embargoed_timestamps"] for p in result["picks"]))

if __name__=="__main__":
    unittest.main()
