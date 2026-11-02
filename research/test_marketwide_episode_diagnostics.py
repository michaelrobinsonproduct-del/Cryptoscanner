"""Synthetic contract tests; no predictive claims from fixtures."""
import datetime as dt
import unittest
from unittest.mock import patch

from research.marketwide_episode_diagnostics import analyze, lagged_return, wilson, chronological_readiness

BASE=dt.datetime(2026,1,1,tzinfo=dt.timezone.utc)


def iso(minutes):
    return (BASE+dt.timedelta(minutes=minutes)).isoformat()


def fixture():
    runs=[]
    observations=[]
    for minute in range(0,481,30):
        rid=str(minute)
        runs.append({"id":rid,"as_of":iso(minute)})
        observations.extend([
            {"run_id":rid,"at":iso(minute),"pair":"AAAUSD",
             "price":100 if minute<=60 else 135},
            {"run_id":rid,"at":iso(minute),"pair":"BBBUSD","price":100}])
    return {"schema":1,"generation":len(runs),"sha256":"0"*64,
            "runs":runs,"observations":observations,
            "predictions":[{"run_id":"30","pair":"BBBUSD"}]}


class EpisodeTests(unittest.TestCase):
    def test_mover_cases_are_not_distinct_episodes(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            report=analyze(fixture())
        one=report["horizons"]["1"]
        self.assertGreaterEqual(one["coverage"]["movers"],2)
        self.assertEqual(one["unique_mover_episodes"],1)
        self.assertEqual(one["unique_mover_pairs"],1)
        self.assertEqual(one["watch_captured_episodes"],0)
        self.assertEqual(one["watch_episode_recall_30"],0.0)
        self.assertEqual(one["episode_first_lag_60m"]["n"],0)
        self.assertEqual(one["episodes"][0]["entry_cases"],one["coverage"]["movers"])
        self.assertEqual(one["coverage"]["watch_positive"],0)
        self.assertEqual(one["coverage"]["eligible"],
            one["coverage"]["matured"]+one["coverage"]["abstain_gap"]+one["coverage"]["immature"])
        self.assertGreaterEqual(one["coverage"]["mover_feature_60m"],1)
        self.assertEqual(report["source"]["observations"],len(fixture()["observations"]))

    def test_predecision_spike_is_not_a_future_mover(self):
        # First quote is 2 minutes before the decision. Another run's
        # quote rises 50% one minute BEFORE that decision, then falls.
        # It cannot be counted as a post-decision +30% opportunity.
        minutes = [0, 1, 30, 60, 90, 120, 150, 180]
        runs = [{"id":str(m), "as_of":iso(m)} for m in minutes]
        observations = [
            {"run_id":str(m), "at":iso(-2 if m==0 else -1 if m==1 else m),
             "pair":"AAAUSD", "price":150 if m==1 else 100}
            for m in minutes
        ]
        state = {"schema":1,"generation":len(runs),"sha256":"0"*64,
                 "runs":runs,"observations":observations,"predictions":[]}
        with patch("paper_pov.ledger.verify",return_value=None):
            report = analyze(state)
        one = report["horizons"]["1"]
        self.assertGreater(one["coverage"]["matured"],0)
        self.assertEqual(one["coverage"]["movers"],0)
        self.assertEqual(one["unique_mover_episodes"],0)

    def test_continuity_starts_at_decision_not_stale_quote(self):
        # A two-minute-old entry quote plus a 44-minute forward gap is
        # valid as-of coverage; starting at quote time would falsely
        # turn the gap into 46 minutes and abstain.
        minutes = [0, 44, 60, 90, 120, 150, 180]
        runs = [{"id":str(m), "as_of":iso(m)} for m in minutes]
        observations = [
            {"run_id":str(m), "at":iso(-2 if m==0 else m),
             "pair":"AAAUSD", "price":100 if m==0 else 135}
            for m in minutes
        ]
        state = {"schema":1,"generation":len(runs),"sha256":"0"*64,
                 "runs":runs,"observations":observations,"predictions":[]}
        with patch("paper_pov.ledger.verify",return_value=None):
            report = analyze(state)
        one = report["horizons"]["1"]
        self.assertGreaterEqual(one["coverage"]["movers"],1)
        self.assertEqual(one["unique_mover_episodes"],1)

    def test_chronological_split_embargoes_future_labels(self):
        times = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540]
        runs = {str(m):BASE+dt.timedelta(minutes=m) for m in times}
        records = [{"run_id":str(m),"pair":"AAAUSD",
                    "peak_observed_return":0.35 if m==0 else 0.0,
                    "lagged_returns":{"60m":0.01}} for m in times]
        split = chronological_readiness(records,runs,1)
        cutoff = BASE+dt.timedelta(minutes=420)
        self.assertEqual(split["cutoff"],cutoff.isoformat())
        self.assertEqual(split["train"]["matured_cases"],6)
        self.assertEqual(split["test"]["matured_cases"],3)
        self.assertEqual(split["excluded_crossing_cutoff"],1)
        self.assertEqual(split["train"]["positive_cases"],1)
        self.assertFalse(split["model_evaluation_ready"])
        self.assertEqual(split["status"],"DESCRIPTIVE_SPLIT_ONLY_NO_TRAINED_CHALLENGER")

    def test_no_chronological_split_from_single_scan(self):
        r=chronological_readiness([],{"0":BASE},6)
        self.assertEqual(r["status"],"INSUFFICIENT_SCAN_TIMES")

    def test_20pct_episode_is_not_misreported_as_30pct(self):
        state=fixture()
        for o in state["observations"]:
            if o["pair"]=="AAAUSD" and o["price"]==135:
                o["price"]=125
        with patch("paper_pov.ledger.verify",return_value=None):
            report=analyze(state)
        one=report["horizons"]["1"]
        self.assertGreater(one["coverage"]["movers_20"],0)
        self.assertEqual(one["coverage"]["movers"],0)
        self.assertEqual(one["unique_mover_episodes_20"],1)
        self.assertEqual(one["unique_mover_episodes"],0)
        self.assertEqual(one["watch_captured_episodes_20"],0)

    def test_gap_abstains_not_false_negative(self):
        state=fixture()
        state["observations"]=[o for o in state["observations"]
                               if o["run_id"] in ("0","480")]
        with patch("paper_pov.ledger.verify",return_value=None):
            report=analyze(state)
        self.assertEqual(report["horizons"]["1"]["coverage"]["matured"],0)
        self.assertGreater(report["horizons"]["1"]["coverage"]["abstain_gap"],0)

    def test_asof_features_do_not_look_ahead(self):
        at=BASE+dt.timedelta(minutes=60)
        series=[(BASE,100,"0"),(BASE+dt.timedelta(minutes=30),100,"30"),
                (at,100,"60"),(BASE+dt.timedelta(minutes=90),200,"90")]
        times=[x[0] for x in series]
        self.assertEqual(lagged_return(series,times,2,60),0.0)
        self.assertIsNone(lagged_return(series,times,0,60))
        self.assertIsNone(lagged_return(series,times,2,180))

    def test_lag_gap_and_intervals(self):
        series=[(BASE,100,"0"),(BASE+dt.timedelta(minutes=90),135,"90")]
        self.assertIsNone(lagged_return(series,[x[0] for x in series],1,60))
        self.assertIsNone(wilson(0,0))
        lo,hi=wilson(0,24)
        self.assertEqual(lo,0)
        self.assertGreater(hi,0)
        self.assertLess(hi,0.2)


if __name__=="__main__":
    unittest.main()
