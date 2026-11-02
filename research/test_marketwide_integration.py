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
        # Validate episode-first WATCH capture independently on the sealed
        # fixture, without equating later WATCH with early identification.
        for suffix, total in (("20", "watch_captured_episodes_20"),
                              ("30", "watch_captured_episodes")):
            first=e["watch_first_entry_episodes_"+suffix]
            late=e["watch_late_only_episodes_"+suffix]
            test.assertGreaterEqual(first,0,h)
            test.assertGreaterEqual(late,0,h)
            test.assertEqual(first+late,e[total],(h,suffix))
        reasons=("abstain_conflicting_quotes","abstain_future_entry_quotes",
                 "abstain_outcome_provenance","abstain_no_future_observation","abstain_missing_horizon_anchor",
                 "abstain_stale_entry","abstain_discontinuous_path")
        c=e["coverage"]
        test.assertEqual(sum(c[k] for k in reasons),c["abstain_gap"],h)
        test.assertEqual(sum(c["watch_"+k] for k in reasons),c["watch_abstain_gap"],h)
        for k in reasons:
            test.assertLessEqual(c["watch_"+k],c[k],(h,k))
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


    def test_late_first_observation_abstains_in_both_evaluators(self):
        # Valid sealed quote at minute 104 was FIRST observed at scan 106.
        # For the minute-0 entry the 1h+45m acceptance limit is minute 105.
        runs=[]; observations=[]
        for minute,quote_at,price in ((0,0,100),(30,30,100),(60,60,100),
                                      (106,104,135),(150,150,135),(180,180,135)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(quote_at),
                                 "pair":"AAAUSD","price":price})
        state=sealed_fixture({"runs":runs,"observations":observations,"predictions":[]})
        assert_same_cohorts(self,state)
        one=evaluate(state)["horizons"]["1"]
        c=analyze(state)["horizons"]["1"]["coverage"]
        self.assertEqual(one["abstain_outcome_provenance"],1)
        self.assertEqual(one["watch_abstain_outcome_provenance"],1)
        self.assertEqual(c["abstain_outcome_provenance"],1)
        self.assertEqual(one["watch_false_positive_30"],0)

if __name__ == "__main__":
    unittest.main()
