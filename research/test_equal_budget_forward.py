import datetime as dt
import unittest
from research.equal_budget_forward import compare

T="2026-10-01T00:00:00+00:00"

def row(pair,base,challenger,return_pct=None):
    outcomes={}
    if return_pct is not None:
        for h in (1,3,6,24):
            due=(dt.datetime.fromisoformat(T)+dt.timedelta(hours=h,minutes=5)).isoformat()
            outcomes[str(h)]={"return_pct":return_pct,"evaluated_at":due}
    return {"run_at":T,"features_observed_at":T,"pair":pair,"price":1.0,
            "baseline_score":base,"challenger_score":challenger,
            "notional_usd":200000,"spread_bps":10,"outcomes":outcomes}

class ForwardComparisonTests(unittest.TestCase):
    def test_equal_budget_and_no_promotion(self):
        result=compare([row("A",10,1,25),row("B",1,10,-3)],budget=1)
        one=result["horizons"][1]
        self.assertEqual(one["baseline"]["hits20"],1)
        self.assertEqual(one["challenger"]["hits20"],0)
        self.assertEqual(one["challenger"]["false_positives"],1)
        self.assertEqual(one["baseline"]["selected"],one["challenger"]["selected"])
        self.assertFalse(result["promotion_eligible"])

    def test_missing_outcomes_not_counted_as_failures(self):
        result=compare([row("A",1,1)],budget=1)
        self.assertEqual(result["horizons"][24]["baseline"]["matured"],0)
        self.assertIsNone(result["horizons"][24]["baseline"]["mean_matured_return_pct"])

    def test_future_features_rejected(self):
        r=row("A",1,1)
        r["features_observed_at"]="2026-10-01T00:01:00+00:00"
        with self.assertRaises(ValueError):
            compare([r])

    def test_immature_outcome_rejected(self):
        r=row("A",1,1,25)
        r["outcomes"]["1"]["evaluated_at"]=T
        with self.assertRaises(ValueError):
            compare([r])

    def test_liquidity_filter(self):
        r=row("A",1,1,25)
        r["spread_bps"]=100
        result=compare([r])
        self.assertEqual(result["horizons"][1]["baseline"]["selected"],0)

if __name__=="__main__":
    unittest.main()
