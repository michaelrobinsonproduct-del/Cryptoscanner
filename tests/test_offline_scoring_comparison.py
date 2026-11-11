import unittest
from simple_scanner.offline_scoring_comparison import compare_cohorts
from simple_scanner.shadow_learning import score
from simple_scanner.offline_replay import cohort_split

class OfflineScoringComparisonTests(unittest.TestCase):
    def setUp(self):
        self.rows = [(f't{i}', pair, momentum, volume, base, ret)
                     for i in range(10)
                     for pair, momentum, volume, base, ret in (
                         ('BTC',1.,1.,50.,2.), ('ETH',3.,2.,45.,8.))]

    def test_zero_weight_parity_and_equal_budget(self):
        result=compare_cohorts(self.rows, lambda r: score(r,0,0))
        self.assertEqual(result['cohorts'],10)
        self.assertEqual(result['delta_pct'],0)
        self.assertEqual(result['selection_budget_per_cohort'],1)
        self.assertFalse(result['promotion_eligible'])
        self.assertFalse(result['production_scoring_parity_verified'])

    def test_challenger_comparison_order_independent(self):
        first=compare_cohorts(self.rows,lambda r:score(r,3,4))
        second=compare_cohorts(list(reversed(self.rows)),lambda r:score(r,3,4))
        self.assertEqual(first,second)
        self.assertEqual(first['legacy_avg_return_pct'],2)
        self.assertEqual(first['challenger_avg_return_pct'],8)

    def test_chronological_holdout_excludes_embargo(self):
        split=cohort_split(self.rows)
        result=compare_cohorts(split['holdout'],lambda r:score(r,3,4))
        self.assertEqual(result['cohorts'],split['holdout_timestamps'])
        self.assertTrue(all(p['timestamp'] not in split['embargoed_timestamps'] for p in result['picks']))

    def test_missing_history_fails_closed(self):
        self.assertEqual(compare_cohorts([],lambda r:0)['status'],'INSUFFICIENT_HISTORY')

if __name__=='__main__':
    unittest.main()
