"""Offline behavioral tests; synthetic fixtures are NOT predictive evidence."""
import datetime as dt
import hashlib
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
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
    def test_watch_resolution_denominator_excludes_immature(self):
        row=evaluate(sealed_fixture(fixture()))["horizons"]["1"]
        self.assertEqual(row["watch_eligible"],7)
        self.assertEqual(row["watch_matured"],3)
        self.assertEqual(row["watch_immature"],4)
        self.assertEqual(row["watch_abstain_gap"],0)
        self.assertEqual(row["watch_resolved_fraction"],3/7)
        self.assertEqual(row["watch_eligible"],row["watch_matured"]+
                         row["watch_immature"]+row["watch_abstain_gap"])
        self.assertEqual(row["watch_30"]+row["watch_false_positive_30"],
                         row["watch_matured"])

    def test_watch_gap_is_unresolved_not_false_positive(self):
        f=fixture()
        f["observations"]=[o for o in f["observations"] if o["run_id"] in ("0","180")]
        row=evaluate(sealed_fixture(f))["horizons"]["1"]
        self.assertEqual(row["watch_eligible"],2)
        self.assertEqual(row["watch_abstain_gap"],1)
        self.assertEqual(row["watch_immature"],1)
        self.assertEqual(row["watch_matured"],0)
        self.assertEqual(row["watch_false_positive_30"],0)
        self.assertIsNone(row["watch_precision_30"])

    def test_descriptive_evidence_cannot_claim_authenticated_history_or_promotion(self):
        report=evaluate(sealed_fixture(fixture()))
        self.assertEqual(report["status"],"DESCRIPTIVE_ONLY_NOT_HELD_OUT_LIFT")
        self.assertIs(report["source_authenticated"],False)
        self.assertIs(report["complete_market_history"],False)
        self.assertIs(report["eligible_for_model_promotion"],False)
        self.assertIn("overlapping",report["metric_unit"])
        self.assertIn("not independently authenticated",report["source_provenance"])

    def test_invalid_checksum_rejected_before_any_outcome(self):
        state=sealed_fixture(fixture())
        state["observations"][0]["price"]=999
        with self.assertRaisesRegex(ValueError,"Ledger checksum mismatch"):
            evaluate(state)

    def test_observed_cohort_counts_are_explicit_not_full_market_claims(self):
        report=evaluate(sealed_fixture(fixture()))
        self.assertEqual(report["observed_run_count"],7)
        self.assertEqual(report["observed_pair_count"],2)
        self.assertEqual(report["observed_entry_count"],14)
        self.assertEqual(report["watched_prediction_count"],7)
        for row in report["horizons"].values():
            self.assertEqual(row["eligible"],report["observed_entry_count"])
            self.assertLessEqual(row["watch_eligible"],report["watched_prediction_count"])
        self.assertIs(report["complete_market_history"],False)

    def test_exact_gap_boundary_is_mature_but_one_minute_late_abstains(self):
        def state(first_followup):
            runs=[]; observations=[]
            for minute in (0,first_followup,60,120):
                rid=str(minute)
                runs.append({"id":rid,"as_of":iso(minute)})
                observations.append({"run_id":rid,"at":iso(minute),
                                     "pair":"AAAUSD","price":100})
            return sealed_fixture({"runs":runs,"observations":observations,
                                   "predictions":[]})
        at_boundary=evaluate(state(45))["horizons"]["1"]
        beyond_boundary=evaluate(state(46))["horizons"]["1"]
        self.assertEqual(at_boundary["matured"],1)
        self.assertEqual(at_boundary["abstain_gap"],0)
        self.assertEqual(beyond_boundary["matured"],0)
        self.assertEqual(beyond_boundary["abstain_gap"],1)

    def test_missing_target_anchor_abstains_instead_of_false_positive(self):
        runs=[]; observations=[]
        for minute in (0,30,50,120):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(minute),
                                 "pair":"AAAUSD","price":100})
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
        self.assertGreater(row["abstain_gap"],0)
        self.assertEqual(row["watch_false_positive_30"],0)
        self.assertEqual(row["watch_matured"],0)

    def test_post_horizon_spike_cannot_become_one_hour_hit(self):
        runs=[]; observations=[]
        for minute,price in ((0,100),(30,100),(60,100),(90,135),(110,135)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(minute),
                                 "pair":"AAAUSD","price":price})
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
        self.assertEqual(row["matured"],1)
        self.assertEqual(row["movers_30"],0)
        self.assertEqual(row["watch_30"],0)
        self.assertEqual(row["watch_false_positive_30"],1)

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
        first=state["predictions"][0]
        quote=next(o for o in state["observations"]
                   if o["run_id"]==first["run_id"] and o["pair"]==first["pair"])
        quote["price"]=999
        seal(state)
        with self.assertRaisesRegex(ValueError,"Prediction price differs"):
            evaluate(state)

    def test_sampled_windows_are_not_distinct_episodes(self):
        runs=[]; observations=[]
        # One +35% surge can make two earlier entry windows positive.
        for minute,price in ((0,100),(30,100),(60,135),(90,135),
                             (120,135),(150,135),(180,135)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(minute),
                                 "pair":"AAAUSD","price":price})
        result=evaluate(sealed_fixture({"runs":runs,
                                       "observations":observations,
                                       "predictions":[]}))
        self.assertEqual(result["horizons"]["1"]["movers_30"],2)
        self.assertIn("NOT distinct surge episodes",result["metric_unit"])
        self.assertIn("not independently authenticated",result["source_provenance"])


    def test_conflicting_same_timestamp_quote_must_abstain(self):
        # Two distinct valid runs can carry the same quote timestamp with
        # conflicting prices. A max() would invent a reliable +30% mover.
        runs=[]; observations=[]
        for minute, quote_at, price in ((0,0,100),(30,30,140),
                                        (31,30,100),(60,60,100),(120,120,100)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(quote_at),
                                 "pair":"AAAUSD","price":price})
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
        self.assertEqual(row["movers_30"],0)
        self.assertGreaterEqual(row["abstain_gap"],1)
        self.assertEqual(row["abstain_conflicting_quote"],1)
        self.assertLessEqual(row["watch_abstain_conflicting_quote"],row["watch_abstain_gap"])

    def test_identical_same_timestamp_quote_remains_usable(self):
        runs=[]; observations=[]
        for minute, quote_at, price in ((0,0,100),(30,30,135),
                                        (31,30,135),(60,60,135),(120,120,135)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(quote_at),
                                 "pair":"AAAUSD","price":price})
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
        self.assertEqual(row["movers_30"],1)
        self.assertEqual(row["matured"],1)
        self.assertEqual(row["abstain_conflicting_quote"],0)

    def test_other_pair_spike_never_leaks_into_watched_pair(self):
        runs=[]; observations=[]
        for minute in (0,30,60,120):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            for pair, price in (("AAAUSD",135 if minute else 100),
                                ("BBBUSD",100)):
                observations.append({"run_id":rid,"at":iso(minute),
                                     "pair":pair,"price":price})
        raw={"runs":runs,"observations":observations,
             "predictions":[{"run_id":"0","pair":"BBBUSD"}]}
        row=evaluate(sealed_fixture(raw))["horizons"]["1"]
        self.assertEqual(row["movers_30"],1)
        self.assertEqual(row["watch_30"],0)
        self.assertEqual(row["missed_30"],1)
        self.assertEqual(row["watch_false_positive_30"],1)

    def test_cli_unresolved_watch_null_precision_and_no_promotion(self):
        from research.marketwide_paper_outcomes import main
        raw=fixture()
        raw["observations"]=[o for o in raw["observations"]
                             if o["run_id"] in ("0","180")]
        state=sealed_fixture(raw)
        with tempfile.TemporaryDirectory() as folder:
            source=Path(folder)/"ledger.json"
            output=Path(folder)/"report.json"
            source.write_text(json.dumps(state))
            with patch.object(sys,"argv",["marketwide","--verified-ledger",str(source),
                                         "--output",str(output)]):
                with contextlib.redirect_stdout(io.StringIO()):
                    main()
            report=json.loads(output.read_text())
        row=report["horizons"]["1"]
        self.assertEqual(row["watch_matured"],0)
        self.assertIsNone(row["watch_precision_30"])
        self.assertIsNone(row["watch_precision_20"])
        self.assertIs(report["source_authenticated"],False)
        self.assertIs(report["complete_market_history"],False)
        self.assertIs(report["eligible_for_model_promotion"],False)


    def test_resealed_future_quote_fails_source_timestamp_contract(self):
        state=sealed_fixture(fixture())
        state["observations"][0]["at"]=iso(1)
        seal(state)
        with self.assertRaisesRegex(ValueError,"Observation timestamp outside run"):
            evaluate(state)

    def test_resealed_nonmonotonic_runs_fail_before_labels(self):
        state=sealed_fixture(fixture())
        state["runs"][0],state["runs"][1]=state["runs"][1],state["runs"][0]
        seal(state)
        with self.assertRaisesRegex(ValueError,"Nonmonotonic run timestamps"):
            evaluate(state)


    def test_conflicting_entry_quote_abstains_even_when_future_clean(self):
        # Two sealed run snapshots claim different entry prices for one
        # quote timestamp. Neither is a trustworthy base for +30% labels.
        runs=[]; observations=[]
        for minute, quote_at, price in ((0,0,100),(1,0,140),
                                        (30,30,130),(60,60,130),(120,120,130)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(quote_at),
                                 "pair":"AAAUSD","price":price})
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
        self.assertEqual(row["movers_30"],0)
        self.assertGreaterEqual(row["abstain_conflicting_quote"],1)

    def test_resealed_late_scan_quote_is_unknown_not_matured_nonhit(self):
        # The 104m quote was first observed by a valid 106m PAPER scan.
        # The entry-0 1h+45m horizon cannot use it, even if +35%.
        runs=[]; observations=[]
        for minute,quote_at,price in ((0,0,100),(30,30,100),(60,60,100),
                                      (106,104,135),(150,150,135),(180,180,135)):
            rid=str(minute)
            runs.append({"id":rid,"as_of":iso(minute)})
            observations.append({"run_id":rid,"at":iso(quote_at),
                                 "pair":"AAAUSD","price":price})
        row=evaluate(sealed_fixture({"runs":runs,"observations":observations,
                                     "predictions":[]}))["horizons"]["1"]
        self.assertEqual(row["abstain_outcome_provenance"],1)
        self.assertEqual(row["watch_abstain_outcome_provenance"],1)
        self.assertEqual(row["watch_false_positive_30"],0)
        self.assertEqual(row["watch_eligible"],
                         row["watch_matured"]+row["watch_immature"]+row["watch_abstain_gap"])

if __name__=="__main__":unittest.main()
