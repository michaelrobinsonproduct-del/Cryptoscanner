"""Synthetic contract tests; no predictive claims from fixtures."""
import datetime as dt
import hashlib
import unittest
from unittest.mock import patch

from research.marketwide_episode_diagnostics import analyze, lagged_return, lagged_return_diagnostic, wilson, chronological_readiness, cluster_episodes

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

    def test_many_overlapping_positive_labels_are_not_independent_training_examples(self):
        runs={str(m):BASE+dt.timedelta(hours=m) for m in range(100)}
        rows=[]
        # Old readiness used >=10 positive/negative observations per split.
        # Repeated hourly entries from one market satisfy that but are not
        # independent positive episodes or a diverse negative cohort.
        for m in list(range(20))+list(range(70,90)):
            rows.append({"run_id":str(m),"pair":"ONEUSD","hit_30":True,
                         "lagged_returns":{"60m":0.1}})
        for m in list(range(30,50))+list(range(80,100)):
            rows.append({"run_id":str(m),"pair":"NEGUSD","hit_30":False,
                         "lagged_returns":{"60m":0.0}})
        split=chronological_readiness(rows,runs,6)
        for part in ("train","test"):
            self.assertGreaterEqual(split[part]["positive_lag_60m_covered"],10)
            self.assertLess(split[part]["positive_lag_60m_episodes"],10)
            self.assertEqual(split[part]["positive_pairs"],1)
            self.assertEqual(split[part]["negative_lag_60m_pairs"],1)
        self.assertFalse(split["model_evaluation_ready"])
        self.assertEqual(
            {(b["partition"],b["requirement"],b["required"],b["observed"])
             for b in split["minimum_sample_requirements"]},
            {(p,requirement,10,observed)
             for p in ("train","test")
             for requirement,observed in (
                 ("episode_first_positive_lag_60m",split[p]["positive_lag_60m_episodes"]),
                 ("distinct_negative_lag_60m_pairs",1))})

    def test_readiness_requires_both_independent_positive_and_negative_cohorts(self):
        runs={str(m):BASE+dt.timedelta(hours=m) for m in range(100)}
        rows=[]
        for part_start in (0,70):
            for k in range(12):
                rid=str(part_start+k)
                rows.append({"run_id":rid,"pair":f"POS{k}USD","hit_30":True,
                             "lagged_returns":{"60m":0.12}})
                rows.append({"run_id":rid,"pair":f"NEG{k}USD","hit_30":False,
                             "lagged_returns":{"60m":-0.01}})
        split=chronological_readiness(rows,runs,1)
        for part in ("train","test"):
            self.assertEqual(split[part]["positive_lag_60m_episodes"],12)
            self.assertEqual(split[part]["negative_lag_60m_pairs"],12)
        self.assertTrue(split["sample_thresholds_met"])
        self.assertFalse(split["model_evaluation_ready"])
        self.assertEqual(split["minimum_sample_requirements"],[])
        self.assertIn("exchange_authenticated_market_history",split["unmet_evidence_gates"])
        self.assertIn("independent_held_out_challenger",split["unmet_evidence_gates"])
        # This is sample-readiness only; no challenger was trained.
        self.assertEqual(split["status"],"DESCRIPTIVE_SPLIT_ONLY_NO_TRAINED_CHALLENGER")

    def test_later_surge_feature_cannot_backfill_missing_first_entry_feature(self):
        runs={str(m):BASE+dt.timedelta(hours=m) for m in range(100)}
        rows=[]
        for start in (0,70):
            for k in range(12):
                # One positive episode per pair; first positive has no
                # historical lag. The later overlapping label has a feature.
                for offset,lag in ((0,None),(1,0.30)):
                    rows.append({"run_id":str(start+offset),
                                 "pair":f"POS{k}USD","hit_30":True,
                                 "lagged_returns":{"60m":lag}})
                rows.append({"run_id":str(start),"pair":f"NEG{k}USD",
                             "hit_30":False,"lagged_returns":{"60m":0.0}})
        split=chronological_readiness(rows,runs,6)
        for part in ("train","test"):
            self.assertEqual(split[part]["positive_episodes"],12)
            self.assertEqual(split[part]["positive_lag_60m_covered"],12)
            self.assertEqual(split[part]["positive_lag_60m_episodes"],0)
            self.assertEqual(split[part]["negative_lag_60m_pairs"],12)
        self.assertFalse(split["model_evaluation_ready"])

    def test_no_chronological_split_from_single_scan(self):
        r=chronological_readiness([],{"0":BASE},6)
        self.assertEqual(r["status"],"INSUFFICIENT_SCAN_TIMES")
        self.assertFalse(r["model_evaluation_ready"])
        self.assertFalse(r["sample_thresholds_met"])

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
            for label in ("positive_20","negative_20","positive_30","negative_30"):
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



    def test_episode_first_feature_coverage_has_explicit_denominators(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            report=analyze(fixture())
        for horizon in report["horizons"].values():
            for threshold in (20,30):
                total=horizon["unique_mover_episodes"+("_20" if threshold==20 else "")]
                stats=horizon["episode_first_entry_feature_coverage_"+str(threshold)]
                for lag in ("30m","60m","180m"):
                    row=stats[lag]
                    self.assertEqual(row["episodes"],total)
                    self.assertEqual(row["with_asof_feature"]+row["without_asof_feature"],total)
                    self.assertLessEqual(row["distinct_covered_pairs"],row["with_asof_feature"])
                    self.assertEqual(row["covered_fraction"],
                                     row["with_asof_feature"]/total if total else None)
                    self.assertEqual(row["with_asof_feature"],
                        horizon["episode_first_entry_feature_distributions"+
                                ("_20" if threshold==20 else "")][lag]["n"])
        # A positive case with no historical anchor must remain uncovered,
        # not become an apparent zero-return historical feature.
        one=report["horizons"]["1"]
        self.assertGreater(one["episode_first_entry_feature_coverage_30"]["60m"]
                           ["without_asof_feature"],0)

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

    def test_ambiguous_historical_quote_abstains_feature(self):
        series=[(BASE,100,"0"),(BASE+dt.timedelta(minutes=30),100,"30"),
                (BASE+dt.timedelta(minutes=30),200,"other"),
                (BASE+dt.timedelta(minutes=60),150,"60")]
        self.assertIsNone(lagged_return(series,[r[0] for r in series],3,60))
        series[2]=(series[2][0],100,"other")
        self.assertEqual(lagged_return(series,[r[0] for r in series],3,60),0.5)

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

    def test_multiple_duplicate_anchor_quotes_cannot_hide_earlier_conflict(self):
        # The final two anchor prices agree, but the first contradicts them.
        # Checking only the immediately preceding quote would miss it.
        series=[(BASE,100,"a"),(BASE,200,"b"),(BASE,200,"c"),
                (BASE+dt.timedelta(minutes=30),225,"middle"),
                (BASE+dt.timedelta(minutes=60),250,"entry")]
        times=[r[0] for r in series]
        self.assertIsNone(lagged_return(series,times,4,60))
        series[0]=(BASE,200,"a")
        self.assertAlmostEqual(lagged_return(series,times,4,60),0.25)

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


    def test_watch_outcome_denominators_distinguish_unknown_from_nonhits(self):
        state=fixture()
        state["predictions"].append({"run_id":"480","pair":"BBBUSD"})
        # A WATCH at run 0 is label-incomplete when later BBB observations
        # are missing; it must not be counted as a false positive.
        state["predictions"].append({"run_id":"0","pair":"BBBUSD"})
        state["observations"]=[o for o in state["observations"]
            if not (o["pair"]=="BBBUSD" and o["run_id"] in ("60","90"))]
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        c=one["coverage"]
        self.assertGreater(c["watch_immature"],0)
        self.assertGreater(c["watch_abstain_gap"],0)
        self.assertEqual(c["watch_eligible"],
            c["watch_matured"]+c["watch_immature"]+c["watch_abstain_gap"])
        self.assertEqual(c["missed_20"],c["movers_20"]-c["watch_positive_20"])
        self.assertEqual(c["missed_30"],c["movers"]-c["watch_positive"])
        self.assertEqual(one["missed_mover_episodes_20"],
            one["unique_mover_episodes_20"]-one["watch_captured_episodes_20"])
        self.assertEqual(one["missed_mover_episodes_30"],
            one["unique_mover_episodes"]-one["watch_captured_episodes"])

    def test_20pct_feature_cohorts_do_not_reuse_30pct_negative_labels(self):
        state=fixture()
        for o in state["observations"]:
            if o["pair"]=="AAAUSD" and o["price"]==135:
                o["price"]=125
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        for lag in ("30m","60m","180m"):
            d=one["pre_entry_price_feature_distributions"][lag]
            self.assertEqual(d["positive_30"]["n"],0)
            self.assertGreaterEqual(d["positive_20"]["n"],0)
            self.assertEqual(d["positive_20"]["n"]+d["negative_20"]["n"],
                d["positive_30"]["n"]+d["negative_30"]["n"])
            self.assertLessEqual(d["negative_20"]["n"],d["negative_30"]["n"])


    def test_episode_clusters_use_decision_time_not_stale_quote_time(self):
        cases=[
            {"pair":"AAAUSD","entry_at":iso(0),"decision_at":iso(0),
             "watch":False,"lagged_returns":{"60m":None},
             "peak_observed_return":0.35},
            {"pair":"AAAUSD","entry_at":iso(40),"decision_at":iso(80),
             "watch":False,"lagged_returns":{"60m":None},
             "peak_observed_return":0.40},
        ]
        episodes=cluster_episodes(cases,1)
        self.assertEqual(len(episodes),2)
        self.assertEqual([e["first_decision_at"] for e in episodes],
                         [iso(0),iso(80)])
        self.assertEqual([e["entry_cases"] for e in episodes],[1,1])



    def test_first_qualifying_entry_capture_is_not_later_watch(self):
        cases=[{"pair":"AAAUSD","entry_at":iso(m),"decision_at":iso(m),
                "watch":watch,"lagged_returns":{"60m":None},
                "peak_observed_return":0.35} for m,watch in ((0,False),(30,True))]
        episodes=cluster_episodes(cases,1)
        self.assertEqual(len(episodes),1)
        self.assertTrue(episodes[0]["watch_captured"])
        self.assertFalse(episodes[0]["first_entry_watch"])
        self.assertEqual(episodes[0]["first_watch_decision_at"],iso(30))
        cases[0]["watch"]=True
        episodes=cluster_episodes(cases,1)
        self.assertTrue(episodes[0]["first_entry_watch"])
        self.assertEqual(episodes[0]["first_watch_decision_at"],iso(0))

    def test_same_first_decision_watch_is_not_misclassified_as_late(self):
        # Two same-decision entries must not depend on sort stability.
        base={"pair":"AAAUSD","entry_at":iso(0),"decision_at":iso(0),
              "lagged_returns":{"60m":None},"peak_observed_return":0.35}
        for order in ((False, True), (True, False)):
            cases=[dict(base,watch=watch) for watch in order]
            cases.append(dict(base,entry_at=iso(30),decision_at=iso(30),watch=False))
            episodes=cluster_episodes(cases,1)
            self.assertEqual(len(episodes),1)
            self.assertTrue(episodes[0]["first_entry_watch"])
            self.assertTrue(episodes[0]["watch_captured"])
            self.assertEqual(episodes[0]["first_watch_decision_at"],iso(0))

    def test_episode_first_watch_accounting_preserves_any_watch_recall(self):
        state=fixture()
        state["predictions"].append({"run_id":"30","pair":"AAAUSD"})
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        self.assertGreater(one["watch_captured_episodes"],0)
        self.assertEqual(one["watch_first_entry_episodes_30"],1)
        self.assertEqual(one["watch_late_only_episodes_30"],0)
        self.assertEqual(one["watch_captured_episodes"],
                         one["watch_first_entry_episodes_30"]+one["watch_late_only_episodes_30"])
        self.assertLessEqual(one["watch_first_entry_episodes_20"],
                             one["watch_captured_episodes_20"])


    def test_first_entry_recall_is_separate_from_later_capture(self):
        state=fixture()
        # The first +30% qualifying entry is at decision 0. A later WATCH
        # can capture the episode but cannot claim first-entry detection.
        state["predictions"].append({"run_id":"30","pair":"AAAUSD"})
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        self.assertGreater(one["watch_captured_episodes"],0)
        self.assertLessEqual(one["watch_first_entry_recall_30"],one["watch_episode_recall_30"])
        self.assertEqual(one["watch_first_entry_recall_30"],
                         one["watch_first_entry_episodes_30"]/one["unique_mover_episodes"])
        with patch("paper_pov.ledger.verify",return_value=None):
            immature=analyze(fixture())["horizons"]["24"]
        for h in (one,immature):
            for threshold in (20,30):
                total=h["unique_mover_episodes"+("_20" if threshold==20 else "")]
                ratio=h["watch_first_entry_recall_"+str(threshold)]
                count=h["watch_first_entry_episodes_"+str(threshold)]
                self.assertEqual(ratio,count/total if total else None)

    def test_gap_reasons_partition_all_abstentions(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            report=analyze(fixture())
        keys=("abstain_conflicting_quotes","abstain_future_entry_quotes",
              "abstain_no_future_observation","abstain_missing_horizon_anchor",
              "abstain_stale_entry","abstain_discontinuous_path")
        for horizon in report["horizons"].values():
            c=horizon["coverage"]
            self.assertEqual(c["abstain_gap"],sum(c[k] for k in keys))
            self.assertEqual(c["eligible"],c["matured"]+c["immature"]+c["abstain_gap"])

    def test_missing_anchor_and_stale_entry_are_not_false_positives(self):
        state=fixture()
        # Remove the exact 60m maturity anchor and the 90m fallback for AAA.
        state["observations"]=[o for o in state["observations"] if not
            (o["pair"]=="AAAUSD" and o["run_id"] in ("60","90"))]
        # BBB's run-0 quote predates the decision by more than 45 minutes.
        for o in state["observations"]:
            if o["pair"]=="BBBUSD" and o["run_id"]=="0":
                o["at"]=iso(-50)
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        c=one["coverage"]
        self.assertGreater(c["abstain_missing_horizon_anchor"],0)
        self.assertGreater(c["abstain_stale_entry"],0)
        self.assertEqual(c["abstain_gap"],sum(c[k] for k in (
            "abstain_conflicting_quotes","abstain_future_entry_quotes",
            "abstain_no_future_observation","abstain_missing_horizon_anchor",
            "abstain_stale_entry","abstain_discontinuous_path")))


    def test_watch_gap_reasons_are_subset_of_market_gap_reasons(self):
        state=fixture()
        state["predictions"].extend([
            {"run_id":"0","pair":"AAAUSD"},
            {"run_id":"0","pair":"BBBUSD"}])
        state["observations"]=[o for o in state["observations"] if not
            (o["pair"]=="AAAUSD" and o["run_id"] in ("60","90"))]
        for o in state["observations"]:
            if o["pair"]=="BBBUSD" and o["run_id"]=="0":
                o["at"]=iso(-50)
        with patch("paper_pov.ledger.verify",return_value=None):
            c=analyze(state)["horizons"]["1"]["coverage"]
        keys=("abstain_conflicting_quotes","abstain_future_entry_quotes",
              "abstain_no_future_observation","abstain_missing_horizon_anchor",
              "abstain_stale_entry","abstain_discontinuous_path")
        self.assertEqual(c["watch_abstain_gap"],sum(c["watch_"+k] for k in keys))
        self.assertGreater(c["watch_abstain_missing_horizon_anchor"],0)
        self.assertGreater(c["watch_abstain_stale_entry"],0)
        for key in keys:
            self.assertLessEqual(c["watch_"+key],c[key])


    def test_feature_missing_reasons_are_point_in_time_and_mutually_exclusive(self):
        series=[(BASE,100,"0"),(BASE+dt.timedelta(minutes=30),110,"30"),
                (BASE+dt.timedelta(minutes=60),120,"60")]
        times=[r[0] for r in series]
        self.assertEqual(lagged_return_diagnostic(series,times,0,30),
                         (None,"no_prior_anchor"))
        self.assertEqual(lagged_return_diagnostic(series,times,2,180),
                         (None,"no_prior_anchor"))
        self.assertAlmostEqual(lagged_return_diagnostic(series,times,2,60)[0],0.2)
        self.assertEqual(lagged_return_diagnostic(series,times,2,60)[1],"covered")
        old=[(BASE-dt.timedelta(minutes=60),100,"old"),series[2]]
        self.assertEqual(lagged_return_diagnostic(old,[r[0] for r in old],1,30),
                         (None,"stale_prior_anchor"))
        gap=[(BASE,100,"0"),(BASE+dt.timedelta(minutes=60),120,"60")]
        self.assertEqual(lagged_return_diagnostic(gap,[r[0] for r in gap],1,60),
                         (None,"discontinuous_history"))

    def test_feature_missing_reasons_do_not_backfill_later_episode_entries(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(fixture())["horizons"]["1"]
        for threshold in (20,30):
            cohort=one["episode_first_entry_feature_coverage_"+str(threshold)]
            for lag in ("30m","60m","180m"):
                stats=cohort[lag]
                self.assertEqual(sum(stats["missing_reasons"].values()),
                                 stats["without_asof_feature"])
                self.assertEqual(stats["with_asof_feature"]+
                                 stats["without_asof_feature"],stats["episodes"])
        self.assertGreater(one["episode_first_entry_feature_coverage_30"]
                           ["60m"]["missing_reasons"].get("no_prior_anchor",0),0)

    def test_conflicting_anchor_reason_survives_duplicate_quote_order(self):
        series=[(BASE,100,"a"),(BASE,200,"b"),(BASE,200,"c"),
                (BASE+dt.timedelta(minutes=30),220,"m"),
                (BASE+dt.timedelta(minutes=60),250,"entry")]
        self.assertEqual(lagged_return_diagnostic(series,[r[0] for r in series],4,60),
                         (None,"conflicting_anchor"))
        series[0]=(BASE,200,"a")
        value,reason=lagged_return_diagnostic(series,[r[0] for r in series],4,60)
        self.assertEqual(reason,"covered")
        self.assertAlmostEqual(value,0.25)


    def test_overlapping_watch_nonhits_are_not_counted_as_independent_windows(self):
        state=fixture()
        state["predictions"].extend([
            {"run_id":"60","pair":"BBBUSD"},
            {"run_id":"90","pair":"BBBUSD"}])
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        self.assertEqual(one["coverage"]["watch_false_positive_30"],3)
        self.assertEqual(one["coverage"]["watch_false_positive_20"],3)
        self.assertEqual(one["watch_nonhit_windows_30"],1)
        self.assertEqual(one["watch_nonhit_windows_20"],1)
        self.assertEqual(one["watch_nonhit_distinct_pairs_30"],1)
        self.assertEqual(one["watch_nonhit_distinct_pairs_20"],1)

    def test_watch_nonhit_windows_keep_separate_pairs_and_distant_decisions(self):
        state=fixture()
        state["predictions"].extend([
            {"run_id":"180","pair":"AAAUSD"},
            {"run_id":"180","pair":"BBBUSD"},
            {"run_id":"360","pair":"BBBUSD"}])
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        self.assertEqual(one["watch_nonhit_distinct_pairs_30"],2)
        self.assertGreaterEqual(one["watch_nonhit_windows_30"],3)
        self.assertLessEqual(one["watch_nonhit_windows_30"],
                             one["coverage"]["watch_false_positive_30"])
        self.assertEqual(one["watch_nonhit_windows_20"],
                         one["watch_nonhit_windows_30"])


    def test_sample_thresholds_cannot_authorize_paper_model_evaluation(self):
        runs={str(m):BASE+dt.timedelta(hours=m) for m in range(100)}
        rows=[]
        for offset in (0,70):
            for k in range(12):
                rid=str(offset+k)
                rows.extend((
                    {"run_id":rid,"pair":f"POS{k}USD","hit_30":True,
                     "lagged_returns":{"60m":0.1}},
                    {"run_id":rid,"pair":f"NEG{k}USD","hit_30":False,
                     "lagged_returns":{"60m":-0.01}}))
        readiness=chronological_readiness(rows,runs,1)
        self.assertTrue(readiness["sample_thresholds_met"])
        self.assertFalse(readiness["model_evaluation_ready"])
        self.assertEqual(readiness["minimum_sample_requirements"],[])
        self.assertEqual(len(readiness["unmet_evidence_gates"]),3)

    def test_twenty_percent_wilson_intervals_have_matured_denominators(self):
        with patch("paper_pov.ledger.verify",return_value=None):
            horizons=analyze(fixture())["horizons"]
        for report in horizons.values():
            c=report["coverage"]
            self.assertEqual(report["watch_recall_wilson_95_naive_20"],
                             wilson(c["watch_positive_20"],c["movers_20"]))
            self.assertEqual(report["watch_precision_wilson_95_naive_20"],
                             wilson(c["watch_positive_20"],c["watch_matured"]))
            if c["movers_20"]==0:
                self.assertIsNone(report["watch_recall_wilson_95_naive_20"])
            if c["watch_matured"]==0:
                self.assertIsNone(report["watch_precision_wilson_95_naive_20"])


    def test_chronological_first_entry_missing_reasons_never_backfill_late_surge(self):
        runs={str(m):BASE+dt.timedelta(hours=m) for m in range(100)}
        rows=[]
        for offset in (0,70):
            for k in range(3):
                pair=f"POS{k}USD"
                rows.append({"run_id":str(offset),"pair":pair,"hit_30":True,
                             "lagged_returns":{"30m":None,"60m":None,"180m":0.03},
                             "lagged_return_reasons":{"30m":"no_prior_anchor",
                                                       "60m":"discontinuous_history",
                                                       "180m":"covered"}})
                rows.append({"run_id":str(offset+1),"pair":pair,"hit_30":True,
                             "lagged_returns":{"30m":0.1,"60m":0.2,"180m":0.3},
                             "lagged_return_reasons":{"30m":"covered","60m":"covered",
                                                       "180m":"covered"}})
        split=chronological_readiness(rows,runs,6)
        for part in ("train","test"):
            s=split[part]
            self.assertEqual(s["positive_episodes"],3)
            self.assertEqual(s["positive_lag_60m_covered"],3)
            self.assertEqual(s["positive_lag_60m_episodes"],0)
            f=s["positive_first_entry_feature_coverage"]
            self.assertEqual(f["30m"]["missing_reasons"],{"no_prior_anchor":3})
            self.assertEqual(f["60m"]["missing_reasons"],{"discontinuous_history":3})
            self.assertEqual(f["180m"]["with_asof_feature"],3)
            for lag in ("30m","60m","180m"):
                self.assertEqual(f[lag]["episodes"],3)
                self.assertEqual(f[lag]["without_asof_feature"],
                                 sum(f[lag]["missing_reasons"].values()))

    def test_chronological_missing_reason_unavailable_is_explicit(self):
        runs={str(m):BASE+dt.timedelta(hours=m) for m in range(100)}
        rows=[{"run_id":str(m),"pair":"POSUSD","hit_30":True,
               "lagged_returns":{"30m":None,"60m":None,"180m":None}}
              for m in (0,70)]
        split=chronological_readiness(rows,runs,1)
        for part in ("train","test"):
            reasons=split[part]["positive_first_entry_feature_coverage"]
            self.assertEqual(reasons["60m"]["missing_reasons"],{"reason_unavailable":1})
            self.assertEqual(reasons["60m"]["with_asof_feature"],0)


    def test_per_pair_coverage_conserves_all_mature_gap_immature_and_watch_counts(self):
        state=fixture()
        state["predictions"].append({"run_id":"0","pair":"AAAUSD"})
        state["observations"]=[o for o in state["observations"] if not
            (o["run_id"] in ("60","90") and o["pair"]=="AAAUSD")]
        with patch("paper_pov.ledger.verify",return_value=None):
            horizons=analyze(state)["horizons"]
        keys=("eligible","matured","immature","abstain_gap","watch_eligible",
              "watch_matured","watch_immature","watch_abstain_gap","movers_20",
              "movers","watch_positive_20","watch_positive")
        observed={o["pair"] for o in state["observations"]}
        for report in horizons.values():
            c=report["coverage"]
            p=report["pair_coverage"]
            self.assertEqual(p["observed_pairs"],len(observed))
            self.assertEqual(set(p["totals"]),set(keys))
            for key in keys:
                self.assertEqual(p["totals"][key],c[key])
            self.assertLessEqual(len(p["top_gap_pairs"]),10)
            self.assertTrue(all(row["pair"] in observed and row["abstain_gap"]>0
                                for row in p["top_gap_pairs"]))
            self.assertEqual(p["top_gap_pairs"],
                             sorted(p["top_gap_pairs"],
                                    key=lambda row:(-row["abstain_gap"],row["pair"])))
        self.assertGreater(horizons["1"]["pair_coverage"]["pairs_with_gap"],0)

    def test_pair_gap_rank_ties_use_stable_names_and_never_invent_pairs(self):
        state=fixture()
        # Two observed pairs with the same sparse pattern must tie by name.
        state["observations"]=[
            {"run_id":rid,"at":iso(int(rid)),"pair":pair,"price":100}
            for pair in ("ZZZUSD","CCCUSD")
            for rid in ("0","480")]
        state["predictions"]=[]
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]["pair_coverage"]
        self.assertEqual(one["observed_pairs"],2)
        self.assertEqual(one["pairs_with_gap"],2)
        self.assertEqual([r["pair"] for r in one["top_gap_pairs"]],
                         ["CCCUSD","ZZZUSD"])
        self.assertEqual(one["totals"]["eligible"],4)
        self.assertEqual(one["totals"]["abstain_gap"],2)
        self.assertEqual(one["totals"]["immature"],2)

    def test_first_entry_recall_uncertainty_uses_episode_not_case_denominator(self):
        state=fixture()
        with patch("paper_pov.ledger.verify",return_value=None):
            horizons=analyze(state)["horizons"]
        for report in horizons.values():
            for threshold in (20,30):
                suffix="_20" if threshold==20 else ""
                total=report["unique_mover_episodes"+suffix]
                first=report["watch_first_entry_episodes_"+str(threshold)]
                self.assertEqual(report["watch_first_entry_recall_wilson_95_naive_"+str(threshold)],
                                 wilson(first,total))
                if total==0:
                    self.assertIsNone(report["watch_first_entry_recall_wilson_95_naive_"+str(threshold)])
        # Late WATCH may capture an episode but cannot count as first entry.
        state["predictions"].append({"run_id":"30","pair":"AAAUSD"})
        with patch("paper_pov.ledger.verify",return_value=None):
            one=analyze(state)["horizons"]["1"]
        self.assertLessEqual(one["watch_first_entry_episodes_30"],
                             one["watch_captured_episodes"])
        self.assertEqual(one["watch_first_entry_recall_wilson_95_naive_30"],
                         wilson(one["watch_first_entry_episodes_30"],
                                one["unique_mover_episodes"]))


    def test_per_pair_gap_reasons_exhaust_unknown_labels_without_inventing_coverage(self):
        state=fixture()
        # Independently create a stale entry and a missing maturity anchor.
        for row in state["observations"]:
            if row["pair"]=="BBBUSD" and row["run_id"]=="0":
                row["at"]=iso(-50)
        state["observations"]=[o for o in state["observations"] if not
            (o["pair"]=="AAAUSD" and o["run_id"] in ("60","90"))]
        with patch("paper_pov.ledger.verify",return_value=None):
            horizons=analyze(state)["horizons"]
        for report in horizons.values():
            c=report["coverage"]
            pair=report["pair_coverage"]
            self.assertEqual(sum(pair["gap_reason_totals"].values()),c["abstain_gap"])
            for reason,count in pair["gap_reason_totals"].items():
                self.assertEqual(count,c["abstain_"+reason])
            for row in pair["top_gap_pairs"]:
                self.assertEqual(sum(row["gap_reasons"].values()),row["abstain_gap"])
                self.assertLessEqual(row["abstain_gap"],row["eligible"])
        one=horizons["1"]["pair_coverage"]
        self.assertGreater(one["gap_reason_totals"]["stale_entry"],0)
        self.assertGreater(one["gap_reason_totals"]["missing_horizon_anchor"],0)

    def test_unknown_watch_outcomes_bound_all_entry_precision(self):
        state = fixture()
        with patch("paper_pov.ledger.verify", return_value=None):
            reports = analyze(state)["horizons"]
        for horizon in ("1", "6", "24", "48"):
            c = reports[horizon]["coverage"]
            bounds = c["watch_precision_all_entries_bounds"]
            self.assertEqual(bounds["unknown"], c["watch_immature"] + c["watch_abstain_gap"])
            self.assertEqual(c["watch_eligible"], c["watch_matured"] + bounds["unknown"])
            for threshold, positive in (("20", "watch_positive_20"), ("30", "watch_positive")):
                self.assertEqual(bounds[threshold]["lower"], c[positive] / c["watch_eligible"])
                self.assertEqual(bounds[threshold]["upper"],
                                 (c[positive] + bounds["unknown"]) / c["watch_eligible"])
                self.assertLessEqual(bounds[threshold]["lower"], bounds[threshold]["upper"])
            s = c["selection_maturity"]
            self.assertEqual(s["watch"]["eligible"] + s["nonwatch"]["eligible"], c["eligible"])
            self.assertEqual(s["watch"]["matured"] + s["nonwatch"]["matured"], c["matured"])
        # With no 48-hour matured outcomes, uncertainty is [0, 1], not a zero precision.
        self.assertEqual(reports["48"]["coverage"]["watch_precision_all_entries_bounds"]["30"],
                         {"lower": 0.0, "upper": 1.0})

    def test_no_watch_has_undefined_precision_bounds(self):
        state = fixture()
        state["predictions"] = []
        with patch("paper_pov.ledger.verify", return_value=None):
            c = analyze(state)["horizons"]["1"]["coverage"]
        self.assertEqual(c["watch_precision_all_entries_bounds"]["unknown"], 0)
        self.assertIsNone(c["watch_precision_all_entries_bounds"]["20"]["lower"])
        self.assertIsNone(c["watch_precision_all_entries_bounds"]["30"]["upper"])
        self.assertEqual(c["selection_maturity"]["watch"]["eligible"], 0)
        self.assertIsNone(c["selection_maturity"]["watch"]["mature_fraction"])

    def test_subthreshold_high_precision_prices_are_not_rounded_into_hits(self):
        runs = [{"id":str(m), "as_of":iso(m)} for m in range(0,481,30)]
        observations = [
            {"run_id":str(m), "at":iso(m), "pair":pair,
             "price": (near if m==30 else "100")}
            for pair,near in (("AAAUSD","119.999999999999999999999999999"),
                              ("BBBUSD","129.999999999999999999999999999"))
            for m in range(0,481,30)]
        state = {"schema":1,"generation":len(runs),"sha256":"0"*64,
                 "runs":runs,"observations":observations,"predictions":[]}
        with patch("paper_pov.ledger.verify", return_value=None):
            c = analyze(state)["horizons"]["1"]["coverage"]
        self.assertGreater(c["matured"], 0)
        self.assertEqual(c["movers_20"], 1)  # BBB near +30% is still >= +20%.
        self.assertEqual(c["movers"], 0)

    def test_exact_decimal_thresholds_remain_inclusive_after_precision_fix(self):
        runs = [{"id":str(m), "as_of":iso(m)} for m in range(0,481,30)]
        observations = [
            {"run_id":str(m), "at":iso(m), "pair":pair,
             "price": (peak if m==30 else "100")}
            for pair,peak in (("AAAUSD","120.000000000000000000000000000"),
                              ("BBBUSD","130.000000000000000000000000000"))
            for m in range(0,481,30)]
        state = {"schema":1,"generation":len(runs),"sha256":"0"*64,
                 "runs":runs,"observations":observations,"predictions":[]}
        with patch("paper_pov.ledger.verify", return_value=None):
            c = analyze(state)["horizons"]["1"]["coverage"]
        self.assertEqual(c["movers_20"], 2)
        self.assertEqual(c["movers"], 1)

    def test_false_positive_rate_excludes_unknown_and_positive_labels(self):
        with patch("paper_pov.ledger.verify", return_value=None):
            horizons = analyze(fixture())["horizons"]
        for report in horizons.values():
            c = report["coverage"]
            for suffix,mover,fp in (("20", "movers_20", "watch_false_positive_20"),
                                     ("30", "movers", "watch_false_positive_30")):
                n = c["matured"] - c[mover]
                self.assertEqual(c["matured_negative_" + suffix], n)
                self.assertEqual(c["false_positive_rate_" + suffix],
                                 c[fp] / n if n else None)
                self.assertEqual(c["false_positive_rate_wilson_95_naive_" + suffix],
                                 wilson(c[fp], n))
        # 24h and 48h have no mature negatives; FPR is undefined, not zero.
        self.assertIsNone(horizons["48"]["coverage"]["false_positive_rate_30"])

    def test_zero_observations_do_not_fabricate_fpr_denominators(self):
        state = fixture()
        state["observations"] = []
        state["predictions"] = []
        with patch("paper_pov.ledger.verify", return_value=None):
            c = analyze(state)["horizons"]["1"]["coverage"]
        self.assertEqual(c["matured_negative_20"], 0)
        self.assertEqual(c["matured_negative_30"], 0)
        self.assertIsNone(c["false_positive_rate_20"])
        self.assertIsNone(c["false_positive_rate_wilson_95_naive_30"])

if __name__=="__main__":
    unittest.main()
