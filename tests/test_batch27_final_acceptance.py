"""Batch 27 negative-case acceptance. No production or GitHub network."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import fixture_delivery_outbox as outbox
from simple_scanner import fixture_receipt_reconciliation as recon
from simple_scanner.offline_replay import cohort_split
from simple_scanner.offline_scoring_comparison import compare_cohorts
from simple_scanner.shadow_learning import score

RECEIPT={"status":"VERIFIED","buy_approved":False,"watch":[]}

class Batch27FinalAcceptance(unittest.TestCase):
    def test_tampered_delivered_comment_id_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            first=outbox.stage(root,31,"run-31",RECEIPT)
            outbox.confirm(root,31,"run-31",first["sha256"],900)
            path=Path(root,outbox.FILENAME)
            state=json.loads(path.read_text())
            state["entries"]["31"]["comment_id"]=0
            path.write_text(json.dumps(state))
            with self.assertRaises(RuntimeError):
                outbox.pending(root)

    def test_tampered_issue_identity_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            outbox.stage(root,31,"run-31",RECEIPT)
            path=Path(root,outbox.FILENAME)
            state=json.loads(path.read_text())
            state["entries"]["31"]["issue_number"]=32
            path.write_text(json.dumps(state))
            with self.assertRaises(RuntimeError):
                outbox.pending(root)

    def test_interrupted_confirmation_preserves_pending_recovery(self):
        with tempfile.TemporaryDirectory() as root:
            first=outbox.stage(root,31,"run-31",RECEIPT)
            with patch.object(outbox.os,"replace",side_effect=OSError("fixture disk interruption")):
                with self.assertRaises(OSError):
                    outbox.confirm(root,31,"run-31",first["sha256"],900)
            self.assertEqual(len(outbox.pending(root)),1)
            marker=recon.marker(31,"run-31",first["sha256"])
            self.assertEqual(recon.reconcile(root,31,[{"id":900,"body":marker}]),"DELIVERED")
            self.assertEqual(outbox.pending(root),[])

    def test_synthetic_holdout_not_promotion_evidence(self):
        rows=[(f"t{i}",pair,m,v,b,r) for i in range(12) for pair,m,v,b,r in
              (("BTC",1.,1.,50.,2.),("ETH",3.,2.,45.,8.))]
        split=cohort_split(rows)
        result=compare_cohorts(split["holdout"],lambda row:score(row,3,4))
        self.assertFalse(result["promotion_eligible"])
        self.assertFalse(result["production_scoring_parity_verified"])
        self.assertTrue(all(x["timestamp"] not in split["embargoed_timestamps"] for x in result["picks"]))

if __name__=="__main__":
    unittest.main()
