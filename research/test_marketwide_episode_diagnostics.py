"""Synthetic contract tests; no predictive claims from fixtures."""
import datetime as dt
import unittest
from unittest.mock import patch

from research.marketwide_episode_diagnostics import analyze, lagged_return, wilson, chronological_readiness, cluster_episodes

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
                    "hit_30":m==0,
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

    def test_rounded_return_does_not_create_false_positive_label(self):
        state=fixture()
        for o in state["observations"]:
            if o["pair"]=="AAAUSD" and o["price"]==135:
                o["price"]=129.99999999
        with patch("paper_pov.ledger.verify",return_value=None):
            report=analyze(state)
        one=report["horizons"]["1"]
        self.assertEqual(one["coverage"]["movers"],0)
        self.assertEqual(one["unique_mover_episodes"],0)
        self.assertGreater(one["coverage"]["movers_20"],0)
        self.assertEqual(one["chronological_readiness"]["train"]["positive_cases"],0)

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

    def test_exact_20pct_threshold_from_decimal_quotes(self):
        state=fixture()
        for o in state["observations"]:
            if o["pair"]=="AAAUSD" and o["price"]==135:
                o["price"]=120.0
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        self.assertGreater(one["coverage"]["movers_20"],0)
        self.assertEqual(one["coverage"]["movers"],0)
        self.assertEqual(one["unique_mover_episodes_20"],1)

    def test_exact_30pct_threshold_from_decimal_quotes(self):
        state=fixture()
        for o in state["observations"]:
            if o["pair"]=="AAAUSD" and o["price"]==135:
                o["price"]=130.0
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        self.assertGreater(one["coverage"]["movers"],0)
        self.assertEqual(one["unique_mover_episodes"],1)

    def test_episode_clustering_does_not_chain_indefinitely(self):
        cases=[{"pair":"AAAUSD","entry_at":iso(m),"watch":False,
                "lagged_returns":{"60m":None},"peak_observed_return":0.35}
               for m in (0,50,100,150)]
        episodes=cluster_episodes(cases,1)
        self.assertEqual(len(episodes),2)
        self.assertEqual([e["entry_cases"] for e in episodes],[2,2])

    def test_multihorizon_pre_entry_distributions_have_explicit_coverage(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(fixture())["horizons"]["1"]
        dist=one["pre_entry_price_feature_distributions"]
        self.assertEqual(set(dist),{"30m","60m","180m"})
        for lag in dist:
            for label in ("positive_30","negative_30"):
                d=dist[lag][label]
                self.assertEqual(set(d),{"n","mean","positive_fraction","median","min","max"})
                self.assertLessEqual(d["n"],one["coverage"]["matured"])
        self.assertEqual(dist["60m"]["positive_30"]["n"],one["coverage"]["mover_feature_60m"])


    def test_episode_first_entry_feature_diversity_and_even_median(self):
        state=fixture()
        for pair, at60, spike in (("XXXUSD",110,150),("YYYUSD",120,170)):
            for o in list(state["observations"]):
                if o["pair"]=="BBBUSD":
                    minute=int(o["run_id"])
                    price=100 if minute==0 else at60 if minute<120 else spike
                    state["observations"].append(dict(o,pair=pair,price=price))
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        stats=one["episode_first_entry_feature_distributions"]["60m"]
        self.assertEqual(stats["n"],2)
        self.assertEqual(stats["distinct_pairs"],2)
        self.assertAlmostEqual(stats["median"],0.15)
        self.assertAlmostEqual(stats["mean"],0.15)
        self.assertEqual(one["episode_first_lag_60m"]["n"],stats["n"])
        self.assertLessEqual(stats["n"],one["unique_mover_episodes"])
        for lag in ("30m","60m","180m"):
            cohort=one["episode_first_entry_feature_distributions"][lag]
            self.assertLessEqual(cohort["distinct_pairs"],cohort["n"])



    def test_provenance_and_coverage_are_not_model_evidence(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            report=analyze(fixture())
        source=report["source"]
        self.assertFalse(source["source_authenticated"])
        self.assertFalse(source["complete_market_history"])
        self.assertFalse(source["eligible_for_model_promotion"])
        self.assertEqual(source["generation"],len(fixture()["runs"]))
        for horizon in report["horizons"].values():
            cov=horizon["coverage"]
            self.assertEqual(cov["eligible"],cov["matured"]+cov["abstain_gap"]+cov["immature"])
            self.assertAlmostEqual(cov["matured_fraction"],cov["matured"]/cov["eligible"])
            self.assertLessEqual(cov["distinct_positive_pairs"],cov["distinct_matured_pairs"])
            self.assertLessEqual(cov["distinct_matured_pairs"],cov["matured"])


if __name__=="__main__":
    unittest.main()
