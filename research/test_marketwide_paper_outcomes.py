"""Offline behavioral tests; synthetic fixtures are NOT predictive evidence."""
import datetime as dt
import unittest
from unittest.mock import patch
from research.marketwide_paper_outcomes import evaluate

BASE=dt.datetime(2026,1,1,tzinfo=dt.timezone.utc)
def iso(minutes):
    return (BASE+dt.timedelta(minutes=minutes)).isoformat()
def fixture():
    runs=[]
    observations=[]
    for i in range(0, 181, 30):
        rid=str(i)
        runs.append({"id":rid,"as_of":iso(i)})
        for pair, price in (("AAAUSD",100 if i==0 else 135),("BBBUSD",100)):
            observations.append({"run_id":rid,"at":iso(i),"pair":pair,"price":price})
    return {"runs":runs,"observations":observations,"predictions":[{"run_id":"0","pair":"BBBUSD"}]}
class Tests(unittest.TestCase):
    def test_marketwide_missed_mover(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            result=evaluate(fixture())["horizons"]["1"]
        self.assertGreater(result["missed_30"],0)
        self.assertEqual(result["watch_30"],0)
        self.assertGreater(result["watch_false_positive_30"],0)
        self.assertEqual(result["eligible"],result["matured"]+result["abstain_gap"]+result["immature"])
    def test_gap_is_not_negative(self):
        f=fixture()
        f["observations"]=[o for o in f["observations"] if o["run_id"] in ("0","180")]
        with patch("paper_pov.ledger.verify",return_value=None):
            r=evaluate(f)["horizons"]["1"]
        self.assertGreater(r["abstain_gap"],0)
        self.assertEqual(r["matured"],0)
    def test_pre_decision_spike_is_not_future_mover(self):
        # A later scan can carry a slightly older quote than an earlier scan.
        # A price seen BEFORE the as-of decision must not count as a hit.
        runs=[{"id":"before","as_of":iso(-1)},
              {"id":"decision","as_of":iso(0)}]
        observations=[{"run_id":"before","at":iso(-1),"pair":"AAAUSD","price":150},
                      {"run_id":"decision","at":iso(-2),"pair":"AAAUSD","price":100}]
        for minute in (30,60,90,120):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(minute),"pair":"AAAUSD","price":100})
        with patch("paper_pov.ledger.verify",return_value=None):
            row=evaluate({"runs":runs,"observations":observations,
                          "predictions":[]})["horizons"]["1"]
        self.assertEqual(row["movers_30"],0)
        self.assertEqual(row["missed_30"],0)
        self.assertEqual(row["matured"],2)

    def test_continuity_starts_at_decision_not_stale_quote(self):
        # Entry quote is 2 minutes old; 44 minutes after decision is within
        # MAX_GAP even though 46 minutes have elapsed since that quote.
        runs=[]
        observations=[]
        for minute,quote_at in ((0,-2),(44,44),(60,60),(120,120)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(quote_at),
                                 "pair":"AAAUSD","price":100})
        with patch("paper_pov.ledger.verify",return_value=None):
            row=evaluate({"runs":runs,"observations":observations,
                          "predictions":[]})["horizons"]["1"]
        self.assertEqual(row["matured"],1)
        self.assertEqual(row["abstain_gap"],0)
if __name__=="__main__":unittest.main()
