"""Synthetic contract tests; no predictive claims from fixtures."""
import datetime as dt
import json
import hashlib
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
                self.assertEqual(set(d),{"n","distinct_pairs","mean","positive_fraction","median","min","max"})
                self.assertLessEqual(d["distinct_pairs"],d["n"])
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



    def test_extreme_price_ratio_never_emits_nonfinite_json(self):
        state=fixture()
        for o in state["observations"]:
            if o["pair"]=="AAAUSD":
                o["price"]=1e-300 if o["run_id"]=="0" else 1e300
        with patch("paper_pov.ledger.verify",return_value=None):
            report=analyze(state)
        self.assertGreater(report["horizons"]["1"]["coverage"]["movers"],0)
        self.assertIsNone(report["horizons"]["1"]["mover_cases"][0]["peak_observed_return"])
        json.dumps(report,allow_nan=False)

    def test_episode_clusters_by_decision_not_stale_quote_time(self):
        # Decisions are exactly 60m apart, but the first quote is 3m old.
        # Grouping by quote timestamps would split one episode into two.
        cases=[{"pair":"AAAUSD","entry_at":iso(-3),"decision_at":iso(0),
                "watch":False,"lagged_returns":{"60m":None},
                "peak_observed_return":0.35},
               {"pair":"AAAUSD","entry_at":iso(60),"decision_at":iso(60),
                "watch":False,"lagged_returns":{"60m":None},
                "peak_observed_return":0.35}]
        episodes=cluster_episodes(cases,1)
        self.assertEqual(len(episodes),1)
        self.assertEqual(episodes[0]["entry_cases"],2)
        self.assertEqual(episodes[0]["first_decision_at"],iso(0))

    def test_conflicting_future_quote_abstains_in_episode_metrics(self):
        # A second retained quote for the same pair/time disagrees. A
        # sealed ledger cannot authenticate which is correct.
        baseline=fixture()
        altered=fixture()
        altered["observations"].append({
            "run_id":"120", "at":iso(90), "pair":"AAAUSD", "price":999})
        with patch("paper_pov.ledger.verify",return_value=None):
            clean=analyze(baseline)["horizons"]["1"]["coverage"]
            ambiguous=analyze(altered)["horizons"]["1"]["coverage"]
        self.assertLess(ambiguous["movers"],clean["movers"])
        self.assertGreater(ambiguous["abstain_gap"],clean["abstain_gap"])

    def test_conflicting_past_quote_abstains_from_lagged_feature(self):
        series=[(BASE,100,"0"),
                (BASE+dt.timedelta(minutes=30),105,"30"),
                (BASE+dt.timedelta(minutes=60),110,"60")]
        times=[v[0] for v in series]
        self.assertIsNotNone(lagged_return(series,times,2,60))
        self.assertIsNone(lagged_return(
            series,times,2,60,[BASE+dt.timedelta(minutes=30)]))

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


    def test_conflicting_same_timestamp_future_and_entry_quotes_abstain(self):
        baseline=fixture()
        with patch("paper_pov.ledger.verify",return_value=None):
            normal=analyze(baseline)["horizons"]["1"]
        state=fixture()
        # A second run reports a different price at the exact future
        # timestamp; neither the high nor low can be trusted as a label.
        state["observations"].append({"run_id":"90","at":iso(90),
            "pair":"AAAUSD","price":200})
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        self.assertGreater(one["coverage"]["abstain_conflicting_quotes"],0)
        self.assertLess(one["coverage"]["movers"],normal["coverage"]["movers"])
        self.assertLessEqual(one["coverage"]["abstain_conflicting_quotes"],
                             one["coverage"]["abstain_gap"])
        self.assertEqual(one["coverage"]["eligible"],
                         one["coverage"]["matured"]+
                         one["coverage"]["abstain_gap"]+
                         one["coverage"]["immature"])
        entry=fixture()
        entry["observations"].append({"run_id":"30","at":iso(30),
            "pair":"AAAUSD","price":200})
        with patch("paper_pov.ledger.verify",return_value=None):
            entry_result=analyze(entry)["horizons"]["1"]
        self.assertGreater(entry_result["coverage"]["abstain_conflicting_quotes"],0)


    def test_postdecision_entry_quote_is_not_an_asof_entry(self):
        state=fixture()
        for obs in state["observations"]:
            if obs["run_id"]=="30" and obs["pair"]=="AAAUSD":
                obs["at"]=iso(31)  # Quote from the future of the decision.
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        cov=one["coverage"]
        self.assertGreaterEqual(cov["abstain_future_entry_quotes"],1)
        self.assertLessEqual(cov["abstain_future_entry_quotes"],cov["abstain_gap"])
        self.assertEqual(cov["eligible"],cov["matured"]+cov["abstain_gap"]+cov["immature"])
        self.assertTrue(all(case["entry_quote_age_minutes"]>=0
                            for case in one["mover_cases"]))


    def test_real_sha_sealed_ledger_contract_and_tamper_rejection(self):
        # Unlike the fast synthetic unit fixtures, this exercises the
        # production ledger's real checksum and relationship verification.
        from paper_pov.ledger import seal, verify
        state=fixture()
        mapping={}
        for run in state["runs"]:
            old_id=run["id"]
            rid=hashlib.sha256(("episode-fixture|"+run["as_of"]).encode()).hexdigest()
            mapping[old_id]=rid
            run.update(id=rid,source_sha="a"*40,report_sha256="b"*64,
                       watch_count=1,observation_count=2)
        for obs in state["observations"]:
            obs["run_id"]=mapping[obs["run_id"]]
        state["predictions"]=[]
        for run in state["runs"]:
            asof=run["as_of"]
            state["predictions"].append({
                "run_id":run["id"],"pair":"BBBUSD","as_of":asof,
                "prediction_id":hashlib.sha256(("paper-v1|"+asof+"|BBBUSD").encode()).hexdigest(),
                "price":100,"baseline_score":0.0,"challenger_score":0.0,"rank":1})
        state.update(schema=1,generation=len(state["runs"]),outcomes=[])
        seal(state)
        verify(state)
        one=analyze(state)["horizons"]["1"]
        self.assertGreater(one["coverage"]["movers"],0)
        self.assertEqual(one["watch_captured_episodes"],0)
        self.assertFalse(analyze(state)["source"]["eligible_for_model_promotion"])
        state["observations"][0]["price"]=999
        with self.assertRaisesRegex(ValueError,"checksum"):
            analyze(state)


    def test_episode_cohort_and_matured_watch_diagnostics(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            report=analyze(fixture())
        one=report["horizons"]["1"]
        cov=one["coverage"]
        self.assertEqual(cov["watch_false_positive_30"],cov["watch_matured"]-cov["watch_positive"])
        self.assertEqual(cov["watch_false_positive_20"],cov["watch_matured"]-cov["watch_positive_20"])
        self.assertLessEqual(cov["abstain_conflicting_quotes"]+cov["abstain_future_entry_quotes"],cov["abstain_gap"])
        self.assertIn("episode_first_entry_feature_distributions_20",one)
        self.assertIn("watch_episode_recall_wilson_95_naive_20",one)
        json.dumps(report,allow_nan=False)


    def test_duplicate_exact_lag_anchor_conflict_abstains(self):
        # bisect_right selects the last of the two zero-minute quotes.
        # The earlier contradictory quote must still invalidate the feature.
        series=[(BASE,100,"first"),(BASE,200,"second"),
                (BASE+dt.timedelta(minutes=30),125,"middle"),
                (BASE+dt.timedelta(minutes=60),150,"entry")]
        times=[x[0] for x in series]
        self.assertIsNone(lagged_return(series,times,3,60))
        # Identical repeated quotes do not create artificial abstentions;
        # the intermediate quote ensures the 45-minute coverage gate passes.
        series[1]=(BASE,100,"second")
        self.assertAlmostEqual(lagged_return(series,times,3,60),0.5)


    def test_watch_false_positives_require_matured_labels(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(fixture())["horizons"]["1"]
        cov=one["coverage"]
        self.assertGreater(cov["watch_matured"],0)
        self.assertEqual(cov["watch_false_positive_30"],
                         cov["watch_matured"]-cov["watch_positive"])
        self.assertEqual(cov["watch_false_positive_20"],
                         cov["watch_matured"]-cov["watch_positive_20"])
        self.assertGreaterEqual(cov["watch_false_positive_30"],0)
        self.assertLessEqual(cov["watch_false_positive_30"],cov["watch_matured"])
        self.assertEqual(cov["eligible"],
                         cov["matured"]+cov["immature"]+cov["abstain_gap"])


    def test_episode_first_20pct_features_are_not_30pct_evidence(self):
        state=fixture()
        for o in state["observations"]:
            if o["pair"]=="AAAUSD" and o["price"]==135:
                o["price"]=125
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        self.assertEqual(one["unique_mover_episodes"],0)
        self.assertGreater(one["unique_mover_episodes_20"],0)
        self.assertIsNone(one["watch_episode_recall_wilson_95_naive"])
        self.assertIsNotNone(one["watch_episode_recall_wilson_95_naive_20"])
        for lag in ("30m","60m","180m"):
            stats=one["episode_first_entry_feature_distributions_20"][lag]
            self.assertLessEqual(stats["distinct_pairs"],stats["n"])
            self.assertLessEqual(stats["n"],one["unique_mover_episodes_20"])
            self.assertEqual(set(stats),
                             {"n","distinct_pairs","mean","positive_fraction",
                              "median","min","max"})



    def test_chronological_20pct_readiness_uses_20pct_labels(self):
        state=fixture()
        for obs in state["observations"]:
            if obs["pair"]=="AAAUSD" and obs["price"]==135:
                obs["price"]=125
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        twenty=one["chronological_readiness_20"]
        thirty=one["chronological_readiness"]
        self.assertEqual(twenty["cutoff"],thirty["cutoff"])
        self.assertEqual(twenty["embargo_hours"],thirty["embargo_hours"])
        self.assertEqual(twenty["train"]["matured_cases"],
                         thirty["train"]["matured_cases"])
        self.assertGreater(twenty["train"]["positive_cases"],
                           thirty["train"]["positive_cases"])
        self.assertFalse(twenty["model_evaluation_ready"])
        self.assertEqual(twenty["status"],
                         "DESCRIPTIVE_SPLIT_ONLY_NO_TRAINED_CHALLENGER")


if __name__=="__main__":
    unittest.main()
