"""Offline behavioral tests; synthetic fixtures are NOT predictive evidence."""
import datetime as dt
import hashlib
import unittest
from paper_pov.ledger import seal, verify
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
def sealed_fixture(raw):
    """Construct a valid SHA-sealed PAPER ledger, not a mocked verifier."""
    by_run = {}
    for o in raw["observations"]:
        by_run.setdefault(o["run_id"], []).append(o)
    watches = {(p["run_id"], p["pair"]) for p in raw["predictions"]}
    state = {"schema":1, "generation":0, "runs":[], "predictions":[],
             "observations":[], "outcomes":[]}
    for run in raw["runs"]:
        observations = by_run.get(run["id"], [])
        if not observations:
            continue
        run_id = hashlib.sha256(("test-run|" + run["id"]).encode()).hexdigest()
        selected = [o for o in observations
                    if (run["id"], o["pair"]) in watches]
        selected = selected or observations[:1]
        state["runs"].append({"id":run_id, "as_of":run["as_of"],
                              "source_sha":"a"*40, "report_sha256":"b"*64,
                              "watch_count":len(selected),
                              "observation_count":len(observations)})
        for rank, obs in enumerate(selected, 1):
            pair = obs["pair"]
            pid = hashlib.sha256(("paper-v1|" + run["as_of"] + "|" + pair).encode()).hexdigest()
            state["predictions"].append({"prediction_id":pid, "run_id":run_id,
                                          "as_of":run["as_of"], "pair":pair,
                                          "price":obs["price"], "rank":rank,
                                          "baseline_score":0.0,
                                          "challenger_score":0.0})
        for obs in observations:
            state["observations"].append({"run_id":run_id, "at":obs["at"],
                                           "pair":obs["pair"], "price":obs["price"]})
    state["generation"] = len(state["runs"])
    seal(state)
    verify(state)
    return state

class Tests(unittest.TestCase):
    def test_marketwide_missed_mover(self):
        result=evaluate(sealed_fixture(fixture()))["horizons"]["1"]
        self.assertGreater(result["missed_30"],0)
        self.assertEqual(result["watch_30"],0)
        self.assertGreater(result["watch_false_positive_30"],0)
        self.assertEqual(result["eligible"],result["matured"]+result["abstain_gap"]+result["immature"])
    def test_gap_is_not_negative(self):
        f=fixture()
        f["observations"]=[o for o in f["observations"] if o["run_id"] in ("0","180")]
        r=evaluate(sealed_fixture(f))["horizons"]["1"]
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
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
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
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
        self.assertEqual(row["matured"],1)
        self.assertEqual(row["abstain_gap"],0)
    def test_exact_twenty_percent_boundary(self):
        runs=[]; observations=[]
        for minute,price in ((0,100),(30,120),(60,120),(120,120)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(minute),
                                 "pair":"AAAUSD","price":price})
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
        self.assertEqual(row["movers_20"],1)
        self.assertEqual(row["movers_30"],0)
        self.assertEqual(row["watch_20"],1)

    def test_exact_thirty_percent_boundary(self):
        runs=[]; observations=[]
        for minute,price in ((0,100),(30,130),(60,130),(120,130)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(minute),
                                 "pair":"AAAUSD","price":price})
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
        self.assertEqual(row["movers_20"],1)
        self.assertEqual(row["movers_30"],1)
        self.assertEqual(row["watch_30"],1)

    def test_authentic_ledger_verification_is_not_mocked(self):
        state=sealed_fixture(fixture())
        state["observations"][0]["price"]=999
        seal(state)
        with self.assertRaisesRegex(ValueError,"Prediction price differs"):
            evaluate(state)

if __name__=="__main__":unittest.main()
