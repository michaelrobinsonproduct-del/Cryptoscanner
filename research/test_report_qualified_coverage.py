import unittest
from research.report_qualified_coverage import coverage


class CoverageTests(unittest.TestCase):
    def test_actual_thirteen_round_four_market_pattern(self):
        rows=[]
        for pair in ("XBTUSD","ETHUSD","SOLUSD","XRPUSD"):
            rows.append({"pair":pair,"entry_first_observed_at":1000,
                         "status":"QUALIFIED_OBSERVED_PATH","ge30pct":False})
            rows.extend({"pair":pair,"entry_first_observed_at":1000+i*300,
                         "status":"ABSTAIN_INCOMPLETE",
                         "observed_forward_slots":12-i,"expected_forward_slots":12}
                        for i in range(1,13))
        result=coverage({"rounds_verified":13,"snapshots_verified":52,
                         "abstentions":[],"outcomes":rows})
        self.assertEqual(result["qualified_entries"],4)
        self.assertEqual(result["qualified_negative_30pct"],4)
        self.assertEqual(result["right_censored_entries"],48)
        self.assertEqual(result["incomplete_with_later_qualified_path"],0)
        self.assertEqual(result["status_counts"]["ABSTAIN_INCOMPLETE"],48)
        self.assertEqual(result["rule"],"NO QUALIFIED RULE")

    def test_incomplete_before_later_qualified_is_not_right_censor(self):
        rows=[{"pair":"XBTUSD","entry_first_observed_at":1,
               "status":"ABSTAIN_INCOMPLETE","observed_forward_slots":5,
               "expected_forward_slots":12},
              {"pair":"XBTUSD","entry_first_observed_at":10000,
               "status":"QUALIFIED_OBSERVED_PATH","ge30pct":True}]
        result=coverage({"rounds_verified":14,"snapshots_verified":14,
                         "abstentions":[{"reason":"missing"}],"outcomes":rows})
        self.assertEqual(result["incomplete_with_later_qualified_path"],1)
        self.assertEqual(result["right_censored_entries"],0)
        self.assertEqual(result["qualified_positive_30pct"],1)
        self.assertEqual(result["source_abstentions"],1)


if __name__=="__main__":
    unittest.main()
