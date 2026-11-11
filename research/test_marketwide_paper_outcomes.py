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
if __name__=="__main__":unittest.main()
