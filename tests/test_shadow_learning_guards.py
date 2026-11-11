"""Read-only shadow-learning invariants; no production model promotion."""
import unittest
from simple_scanner.shadow_learning import (
    score, compare, early_accumulation_rank, assess_challenger_promotion,
)

class ShadowLearningGuardTests(unittest.TestCase):
    def test_legacy_zero_weight_score_parity(self):
        rows = [('t1','BTC',1.0,1.2,50.0,3.0),
                ('t1','ETH',2.0,2.0,60.0,-1.0),
                ('t2','SOL',0.5,1.5,40.0,2.0)]
        self.assertEqual([score(r,0,0) for r in rows], [r[4] for r in rows])
        self.assertEqual(compare(rows,0,0)['delta_pct'], 0)

    def test_ranking_has_no_future_label_input(self):
        observed = [('BTC',1.0,20.0,150000.0,100.0,101.0),
                    ('ETH',2.0,25.0,200000.0,100.0,102.0)]
        first = early_accumulation_rank(observed)
        self.assertEqual(first, early_accumulation_rank(list(reversed(observed))))
        self.assertEqual(set(first[0]), {'pair','score','recent_change_pct','spread_bps','notional_24h_usd'})

    def test_shadow_promotion_always_blocked(self):
        for validation in ({'status':'AWAITING_HISTORY'},
                           {'status':'HISTORICAL_HOLDOUT_EVALUATED',
                            'metrics': {k: {'events':100,'challenger_recall':1,'baseline_recall':0}
                                        for k in ('20pct_1h','50pct_1h','100pct_1h')}}):
            gate=assess_challenger_promotion(validation)
            self.assertFalse(gate['promotion_eligible'])
            self.assertFalse(gate['live_weights_modified'])

if __name__=='__main__':
    unittest.main()
