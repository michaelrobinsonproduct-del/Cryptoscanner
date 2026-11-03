import unittest
from unittest.mock import patch
from paper_pov.ledger import empty
from research.reconcile_paper_scores import reconcile

SHA="a"*64
EVIDENCE={"rounds_verified":13,"snapshots_verified":52,"qualified_first_entry_episodes":4,
          "abstentions":[],"production_applied":False,
          "outcomes":[{"pair":"XBTUSD","entry_first_observed_at":1000,
                       "entry_source_sha256":SHA,"entry_liquidity_usd":100,
                       "status":"QUALIFIED_OBSERVED_PATH","ge30pct":False}]}


def run(ledger,evidence=EVIDENCE):
    return reconcile(ledger,evidence,split_at=200000,baseline_version="base-v1",
                     challenger_version="candidate-v1",evidence_sha256="b"*64)


class PaperScoreReconciliationTests(unittest.TestCase):
    def test_actual_empty_sealed_ledger_yields_no_promotion(self):
        result=run(empty())
        self.assertEqual(result["comparison"]["paper_predictions_examined"],0)
        self.assertEqual(result["comparison"]["source_qualified_episodes"],4)
        self.assertIsNone(result["comparison"]["held_out_lift"])
        self.assertEqual(result["shadow_decision"]["decision"],"KEEP_BASELINE")

    def test_unbound_real_paper_score_abstains_even_with_same_pair(self):
        ledger={"predictions":[{"pair":"XBTUSD","baseline_score":2,"challenger_score":3,
                                "as_of":"2026-11-03T11:20:00+00:00"}]}
        with patch("research.reconcile_paper_scores.verify"):
            result=run(ledger)
        self.assertEqual(result["comparison"]["excluded"]["PAPER_TICKER_LACKS_DEPTH_SOURCE_RECEIPT"],1)
        self.assertEqual(result["shadow_decision"]["decision"],"KEEP_BASELINE")

    def test_wrong_source_or_late_receipt_cannot_join(self):
        ledger={"predictions":[{"pair":"XBTUSD","entry_first_observed_at":1000,
                                "source_sha256":"c"*64,"score_observed_at":999,
                                "baseline_score":2,"challenger_score":3},
                               {"pair":"XBTUSD","entry_first_observed_at":1000,
                                "source_sha256":SHA,"score_observed_at":1001,
                                "baseline_score":2,"challenger_score":3}]}
        with patch("research.reconcile_paper_scores.verify"):
            result=run(ledger)
        self.assertEqual(result["comparison"]["excluded"]["DEPTH_SOURCE_SHA_MISMATCH"],1)
        self.assertEqual(result["comparison"]["excluded"]["NO_PRE_ENTRY_SCORE_RECEIPT"],1)
        self.assertEqual(result["comparison"]["held_out_n"],0)

    def test_source_bound_score_enters_train_not_held_out(self):
        ledger={"predictions":[{"pair":"XBTUSD","entry_first_observed_at":1000,
                                "source_sha256":SHA,"score_observed_at":999,
                                "baseline_score":2,"challenger_score":3}]}
        with patch("research.reconcile_paper_scores.verify"):
            result=run(ledger)
        self.assertEqual(result["comparison"]["train_n"],1)
        self.assertEqual(result["comparison"]["held_out_n"],0)
        self.assertEqual(result["shadow_decision"]["decision"],"KEEP_BASELINE")

    def test_nonresearch_source_rejected(self):
        with self.assertRaisesRegex(ValueError,"nonresearch"):
            run(empty(),{**EVIDENCE,"production_applied":True})


if __name__=="__main__":
    unittest.main()
