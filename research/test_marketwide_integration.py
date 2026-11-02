"""Cross-evaluator contracts on genuine SHA-sealed PAPER fixtures.

No mocked ledger verification, synthetic outcomes are not predictive evidence.
"""
import unittest

from research.marketwide_paper_outcomes import evaluate
from research.marketwide_episode_diagnostics import analyze
from research.test_marketwide_paper_outcomes import sealed_fixture, fixture, iso


def assert_same_cohorts(test, state):
    windows = evaluate(state)
    episodes = analyze(state)
    for h, w in windows["horizons"].items():
        e = episodes["horizons"][h]
        test.assertEqual(e["coverage"]["eligible"], w["eligible"], h)
        test.assertEqual(e["coverage"]["matured"], w["matured"], h)
        test.assertEqual(e["coverage"]["abstain_gap"], w["abstain_gap"], h)
        test.assertEqual(e["coverage"]["immature"], w["immature"], h)
        test.assertEqual(e["coverage"]["movers_20"], w["movers_20"], h)
        test.assertEqual(e["coverage"]["movers"], w["movers_30"], h)
        test.assertLessEqual(e["unique_mover_episodes"], w["movers_30"], h)
        # WATCH outcomes are partitioned into resolved, immature and abstained;
        # missing labels cannot be treated as false positives.
        test.assertEqual(e["coverage"]["watch_eligible"], w["watch_eligible"], h)
        test.assertEqual(e["coverage"]["watch_immature"], w["watch_immature"], h)
        test.assertEqual(e["coverage"]["watch_abstain_gap"], w["watch_abstain_gap"], h)
        test.assertEqual(e["coverage"]["watch_matured"], w["watch_matured"], h)
        test.assertEqual(e["coverage"]["watch_eligible"],
            e["coverage"]["watch_matured"] + e["coverage"]["watch_immature"] +
            e["coverage"]["watch_abstain_gap"], h)
        test.assertEqual(e["coverage"]["missed_20"], w["missed_20"], h)
        test.assertEqual(e["coverage"]["missed_30"], w["missed_30"], h)
        test.assertEqual(e["coverage"]["watch_false_positive_20"],
                         w["watch_false_positive_20"], h)
        test.assertEqual(e["coverage"]["watch_false_positive_30"],
                         w["watch_false_positive_30"], h)
        for lag in ("30m","60m","180m"):
            cohorts=e["pre_entry_price_feature_distributions"][lag]
            test.assertEqual(cohorts["positive_20"]["n"]+cohorts["negative_20"]["n"],
                             cohorts["positive_30"]["n"]+cohorts["negative_30"]["n"], (h,lag))
        test.assertEqual(e["missed_mover_episodes_20"],
            e["unique_mover_episodes_20"]-e["watch_captured_episodes_20"], h)
        test.assertEqual(e["missed_mover_episodes_30"],
            e["unique_mover_episodes"]-e["watch_captured_episodes"], h)
    test.assertFalse(windows["eligible_for_model_promotion"])
    test.assertFalse(episodes["source"]["eligible_for_model_promotion"])


class CrossEvaluatorTests(unittest.TestCase):
    def test_sealed_cohort_parity(self):
        assert_same_cohorts(self, sealed_fixture(fixture()))

    def test_conflicting_quote_is_not_an_episode(self):
        runs=[]; observations=[]
        for minute, quote_at, price in ((0,0,100),(30,30,140),
                                         (31,30,100),(60,60,100),(120,120,100)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(quote_at),
                                 "pair":"AAAUSD","price":price})
        state=sealed_fixture({"runs":runs,"observations":observations,
                              "predictions":[]})
        assert_same_cohorts(self,state)
        self.assertEqual(analyze(state)["horizons"]["1"]["unique_mover_episodes"],0)

    def test_horizon_boundary_and_missing_gap_agree(self):
        runs=[]; observations=[]
        for minute,price in ((0,100),(30,100),(60,100),(90,135),(120,135)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(minute),
                                 "pair":"AAAUSD","price":price})
        assert_same_cohorts(self,sealed_fixture({"runs":runs,"observations":observations,
                                                 "predictions":[]}))


if __name__ == "__main__":
    unittest.main()
