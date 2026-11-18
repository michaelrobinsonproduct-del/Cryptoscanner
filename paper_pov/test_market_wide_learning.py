import unittest
from datetime import datetime, timedelta, timezone
from paper_pov.market_wide_learning import build_market_cohort

class MarketWideLearningTest(unittest.TestCase):
    def test_unselected_market_and_negative_control(self):
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        candles = []
        for pair in ("GAINUSD", "FLATUSD", "EXCLUDED"):
            for i in range(601):
                close = 100 if pair != "GAINUSD" or i < 24 else 135
                candles.append(dict(pair=pair, timestamp_utc=(start+timedelta(minutes=5*i)).isoformat(), close=close, high=close))
        result = build_market_cohort(candles, eligible_pairs=["GAINUSD","FLATUSD"], evaluation_asof_utc=(start+timedelta(hours=50)).isoformat())
        self.assertEqual(result["observed_pairs"], ["FLATUSD","GAINUSD"])
        outcomes = result["outcomes"]
        self.assertTrue(any(x["pair"]=="GAINUSD" and x["hit"] is True for x in outcomes))
        self.assertTrue(any(x["pair"]=="FLATUSD" and x["hit"] is False for x in outcomes))
        self.assertFalse(result["production_applied"])
        self.assertFalse(result["source_authenticated"])

    def test_recent_short_horizon_and_unobserved_pair(self):
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        candles = []
        for i in range(25):
            close = 100 if i < 24 else 135
            candles.append(dict(pair="GAINUSD", timestamp_utc=(start+timedelta(minutes=5*i)).isoformat(), close=close, high=close))
        result = build_market_cohort(candles, eligible_pairs=["GAINUSD", "MISSINGUSD"], evaluation_asof_utc=(start+timedelta(hours=2)).isoformat())
        self.assertEqual(result["missing_eligible_pairs"], ["MISSINGUSD"])
        self.assertEqual(result["per_horizon"]["1"]["hits"], 1)
        for h in ("6", "24", "48"):
            self.assertEqual(result["per_horizon"][h]["immature"], 1)
            self.assertEqual(result["per_horizon"][h]["hits"], 0)

    def test_features_reuse_existing_contract_without_future_leakage(self):
        from paper_pov.frozen_historical_shadow import NAMES
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        rows = [dict(pair="GAINUSD", timestamp_utc=(start+timedelta(minutes=5*i)).isoformat(),
                     close=100 if i < 24 else 135, high=100 if i < 24 else 135,
                     volume=10+i, trades=5+i) for i in range(25)]
        kwargs = dict(eligible_pairs=["GAINUSD"], evaluation_asof_utc=(start+timedelta(hours=2)).isoformat())
        result = build_market_cohort(rows, **kwargs)
        self.assertEqual(result["feature_complete_anchors"], 1)
        self.assertEqual(set(result["anchors"][0]["features"]), set(NAMES))
        rows[-1]["close"] = rows[-1]["high"] = 150
        later = build_market_cohort(rows, **kwargs)
        self.assertEqual(result["anchors"][0]["features"], later["anchors"][0]["features"])

    def test_real_source_adapter_rotates_without_watchs_and_checks_asof_eligibility(self):
        from paper_pov.market_wide_learning import run_observed_market_batch, select_market_batch
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        at = lambda minutes: (start+timedelta(minutes=minutes)).isoformat()
        ledger = {"generation": 2, "runs": [{"id": "latest", "as_of": at(120), "observation_count": 2}],
                  "observations": [{"run_id": "older", "pair": "GAINUSD", "at": at(59)},
                                   {"run_id": "latest", "pair": "GAINUSD", "at": at(120)},
                                   {"run_id": "latest", "pair": "FLATUSD", "at": at(120)}],
                  "predictions": []}
        self.assertEqual(select_market_batch(ledger, batch_size=1)[1], ["GAINUSD"])
        def fetch(pair):
            return {"pair": pair, "source": "kraken_public_ohlc_rest", "response_sha256": "a"*64,
                    "candles": [dict(pair=pair, timestamp_utc=at(i*5), close=100 if i<24 else 135,
                                    high=100 if i<24 else 135, volume=10+i, trades=5+i)
                                for i in range(25)]}
        report = run_observed_market_batch(ledger, fetch=fetch, batch_size=1)
        self.assertEqual(report["per_horizon"]["1"]["hits"], 1)
        self.assertEqual(report["missing_eligible_pairs"], ["FLATUSD"])
        self.assertEqual(report["outcomes"][0]["source_sha256"], "a"*64)
        self.assertFalse(report["source_authenticated"])
        self.assertFalse(report["production_applied"])
        ledger["observations"].pop(0)
        report = run_observed_market_batch(ledger, fetch=fetch, batch_size=1)
        self.assertEqual(report["eligibility_abstentions"], 1)
        self.assertEqual(report["per_horizon"]["1"]["hits"], 0)

    def test_archive_stream_pinned_digest_completed_high_and_exclusions(self):
        import gzip
        import hashlib
        import json
        import tempfile
        import zipfile
        from pathlib import Path
        from paper_pov.market_wide_learning import run_archive_market_cohorts
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as temp:
            archive, output = Path(temp)/"source.zip", Path(temp)/"rows.jsonl.gz"
            with zipfile.ZipFile(archive, "w") as z:
                for pair in ("GAINUSD", "FLATUSD", "GAIN EUR".replace(" ", "")):
                    lines = []
                    for i in range(24):
                        stamp = int((start+timedelta(minutes=5*i)).timestamp())
                        high = 135 if pair == "GAINUSD" and i == 23 else 100
                        lines.append(f"{stamp},100,{high},100,100,10,5")
                    z.writestr(pair+"_5.csv", "\n".join(lines))
            digest = hashlib.sha256(archive.read_bytes()).hexdigest()
            args = dict(start_utc=start.isoformat(), end_utc=(start+timedelta(hours=2)).isoformat(), cohort_output=output)
            result = run_archive_market_cohorts(archive, expected_sha256=digest, **args)
            self.assertEqual(result["archive_usd_members"], 2)
            self.assertEqual(result["per_horizon"]["1"]["hits"], 1)
            self.assertEqual(result["per_horizon"]["1"]["misses"], 1)
            self.assertEqual(result["markets_with_hits"], ["GAINUSD"])
            self.assertTrue(result["pinned_archive_verified"])
            self.assertFalse(result["source_authenticated"])
            with gzip.open(output, "rt") as source:
                rows = [json.loads(line) for line in source]
            self.assertEqual(len(rows), 2)
            self.assertTrue(all(r["anchors"][0]["entry_utc"] == (start+timedelta(hours=1)).isoformat() for r in rows))
            with self.assertRaisesRegex(ValueError, "SHA256 mismatch"):
                run_archive_market_cohorts(archive, expected_sha256="0"*64, **args)

    def test_cumulative_state_preserves_eligibility_and_matures_without_duplicate_labels(self):
        from paper_pov.market_wide_learning import run_observed_market_batch
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        at = lambda minutes: (start+timedelta(minutes=minutes)).isoformat()
        def ledger(generation, minutes, include_old=False):
            rows = [{"run_id": "latest", "pair": p, "at": at(minutes)}
                    for p in ("GAINUSD", "FLATUSD")]
            if include_old:
                rows.append({"run_id": "older", "pair": "GAINUSD", "at": at(59)})
            return {"generation": generation, "runs": [{"id": "latest", "as_of": at(minutes), "observation_count": 2}],
                    "observations": rows, "predictions": []}
        def fetch(pair):
            return {"pair": pair, "source": "kraken_public_ohlc_rest", "response_sha256": "a"*64,
                    "candles": [dict(pair=pair, timestamp_utc=at(i*5),
                                     close=100 if i<24 else 135, high=100 if i<24 else 135,
                                     volume=10+i, trades=5+i) for i in range(601)]}
        a = run_observed_market_batch(ledger(2, 120, True), fetch=fetch, batch_size=1)
        state = a["continuity_state"]
        key = a["anchors"][0]["prediction_id"]
        self.assertTrue(any(r["at"] == at(59) for r in state["eligibility"]))
        b = run_observed_market_batch(ledger(3, 180), fetch=fetch, batch_size=1, prior=state)
        self.assertEqual(b["selected_pairs"], ["FLATUSD"])
        c = run_observed_market_batch(ledger(4, 2940), fetch=fetch, batch_size=1, prior=b["continuity_state"])
        self.assertEqual(c["selected_pairs"], ["GAINUSD"])
        final = c["continuity_state"]
        row = [o for o in final["outcomes"] if o["prediction_id"] == key and o["horizon_hours"] == 48]
        self.assertEqual(len(row), 1)
        self.assertTrue(row[0]["hit"])
        self.assertEqual(len(final["last_success_generation"]), 2)
        self.assertEqual(final["previous_digest"], b["continuity_state"]["digest"])
        from copy import deepcopy
        tampered = deepcopy(final)
        tampered["ledger_generation"] = 0
        with self.assertRaisesRegex(ValueError, "checksum"):
            run_observed_market_batch(ledger(5, 3000), fetch=fetch, batch_size=1, prior=tampered)
        with self.assertRaisesRegex(ValueError, "rollback"):
            run_observed_market_batch(ledger(3, 180), fetch=fetch, batch_size=1, prior=final)

    def test_partial_crossings_remain_unqualified_and_events_not_anchor_counts(self):
        from paper_pov.market_wide_learning import crossing_summary
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        rows = []
        for i in range(25):
            if i == 18:
                continue
            rows.append(dict(pair="GAINUSD", timestamp_utc=(start+timedelta(minutes=5*i)).isoformat(),
                             close=100, high=135 if i == 20 else 100))
        report = build_market_cohort(rows, eligible_pairs=["GAINUSD"],
                        evaluation_asof_utc=(start+timedelta(hours=2)).isoformat())
        one = [o for o in report["outcomes"] if o["horizon_hours"] == 1][0]
        self.assertIsNone(one["hit"])
        self.assertFalse(one["coverage_complete"])
        self.assertEqual(one["crossing_evidence"], "PARTIAL_WINDOW")
        self.assertEqual(report["crossing_summary"]["partial_observed_crossings_by_horizon"]["1"], 1)
        self.assertEqual(report["per_horizon"]["1"]["hits"], 0)
        def event(hour):
            return {"pair":"GAINUSD", "horizon_hours":48, "hit":True, "coverage_complete":True,
                    "observed_crossing_candle_close_utc":(start+timedelta(hours=hour)).isoformat()}
        self.assertEqual(crossing_summary([event(1), event(1), event(2), event(10)])
                         ["completed_48h_crossing_clusters"], 2)

    def test_archive_shadow_trains_and_compares_same_blind_top_one_cohort(self):
        import gzip
        import json
        import tempfile
        from pathlib import Path
        from paper_pov.frozen_historical_shadow import NAMES
        from paper_pov.market_wide_learning import train_archive_shadow
        start = datetime(2026, 1, 1, tzinfo=timezone.utc)
        at = lambda day: (start+timedelta(days=day)).isoformat()
        digest = "a"*64
        anchors, outcomes = [], []
        for day in (0, 5):
            for positive in (True, False):
                key = str((day, positive))
                features = {f: (2.0 if positive else 1.0) for f in NAMES}
                features["momentum_60m"] = .02 if positive else .3
                anchors.append(dict(prediction_id=key, pair="GAINUSD" if positive else "FLATUSD",
                                  entry_utc=at(day), feature_asof_utc=at(day),
                                  feature_complete=True, features=features, source_sha256=digest))
                outcomes.append(dict(prediction_id=key, horizon_hours=48, hit=positive,
                                     coverage_complete=True, label_mature_utc=at(day+2),
                                     source_sha256=digest, observed_lead_hours_upper_bound=12))
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)/"cohort.jsonl.gz"
            with gzip.open(path, "wt") as f:
                f.write(json.dumps(dict(anchors=anchors, outcomes=outcomes,
                    source_archive_sha256=digest, production_applied=False, source_authenticated=False))+"\n")
            result = train_archive_shadow(path, training_end_utc=at(3), holdout_start_utc=at(5),
                                          evaluation_asof_utc=at(8), top_k=1)
            self.assertEqual(result["model"]["positive_count"], 1)
            self.assertEqual(result["model"]["negative_count"], 1)
            self.assertEqual(result["comparable_timestamps"], 1)
            self.assertEqual(result["metrics"]["baseline_proxy"]["hits"], 0)
            self.assertEqual(result["metrics"]["challenger"]["hits"], 1)
            self.assertEqual(result["metrics"]["challenger"]["early_hits"], 1)
            self.assertEqual(result["all_ranked_selection_observation_bounds"]["challenger"]["observed_hit_lower_bound"],1)
            self.assertEqual(result["all_ranked_selection_observation_bounds"]["baseline_proxy"]["possible_hit_upper_bound"],0)
            self.assertFalse(result["measured_lift_verified"])
            self.assertFalse(result["production_applied"])


    def test_prospective_scoring_requires_preexisting_model_and_excludes_future_features(self):
        import json
        from pathlib import Path
        from paper_pov.market_wide_learning import score_prospective_market_shard
        model=json.loads(Path("historical/evidence/q3_2026_frozen_shadow_v1.json").read_text())
        start=datetime(2026,11,15,tzinfo=timezone.utc)
        at=lambda m:(start+timedelta(minutes=m)).isoformat()
        ledger={"runs":[{"id":"scan","as_of":at(61)}],
                "observations":[{"run_id":"scan","pair":"GAINUSD","at":at(60),"price":100},
                                {"run_id":"scan","pair":"FLATUSD","at":at(60),"price":100}],
                "predictions":[{"run_id":"scan","pair":"FLATUSD"}]}
        results=[{"pair":pair,"response_sha256":"a"*64,
                  "candles":[dict(pair=pair,timestamp_utc=at(i*5),close=100+i*.01,
                                  high=100+i*.01,volume=10+i,trades=5+i) for i in range(14)]}
                  for pair in ("GAINUSD","FLATUSD")]
        first=score_prospective_market_shard(ledger,results,model,model_available_utc="2026-11-11T03:27:00Z",recorded_at_utc=at(62))
        self.assertEqual(first["baseline_budget"],1)
        self.assertEqual(len(first["predictions"]),2)
        self.assertEqual(sum(p["shadow_equal_budget_watch"] for p in first["predictions"]),1)
        self.assertTrue(all(p["feature_asof_utc"]==at(60) for p in first["predictions"]))
        self.assertTrue(all(p["entry_utc"]==at(62) and p["recording_scope"]=="TIMELY_RECORDED_QUOTE_REFERENCE" for p in first["predictions"]))
        replay=score_prospective_market_shard(ledger,results,model,model_available_utc="2026-11-11T03:27:00Z",recorded_at_utc=at(90))
        self.assertTrue(all(p["recording_scope"]=="ASOF_REPLAY_ONLY" for p in replay["predictions"]))
        results[0]["candles"][-1]["close"]=999
        second=score_prospective_market_shard(ledger,results,model,model_available_utc="2026-11-11T03:27:00Z",recorded_at_utc=at(62))
        self.assertEqual(first,second)
        with self.assertRaisesRegex(ValueError,"not available"):
            score_prospective_market_shard(ledger,results,model,model_available_utc=at(62))


    def test_cumulative_training_uses_archived_and_later_matured_examples(self):
        import gzip
        import json
        import tempfile
        from pathlib import Path
        from paper_pov.frozen_historical_shadow import NAMES
        from paper_pov.market_wide_learning import train_cumulative_market_model, STATE_SCHEMA
        from paper_pov.shadow_learning_evidence import canonical_digest
        start=datetime(2026,1,1,tzinfo=timezone.utc)
        at=lambda d:(start+timedelta(days=d)).isoformat()
        digest="a"*64
        def sample(key,day,hit):
            a=dict(prediction_id=key,pair=key+"USD",entry_utc=at(day),feature_asof_utc=at(day),
                   entry_price=100,feature_complete=True,source_sha256=digest,
                   features={n:float(hit) for n in NAMES})
            o=dict(prediction_id=key,horizon_hours=48,hit=hit,coverage_complete=True,
                   label_mature_utc=at(day+2),source_sha256=digest)
            return a,o
        a,b=sample("A",0,True)
        c,d=sample("B",0,False)
        e,f=sample("C",6,True)
        g,h=sample("D",9,True)
        state=dict(schema=STATE_SCHEMA,evaluation_asof_utc=at(10),production_applied=False,
                   anchors=[e,g],outcomes=[f,h])
        state["digest"]=canonical_digest(state)
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"cohorts.jsonl.gz"
            with gzip.open(path,"wt") as out:
                out.write(json.dumps(dict(source_archive_sha256=digest,production_applied=False,
                    source_authenticated=False,anchors=[a,c],outcomes=[b,d]))+"\n")
            report=train_cumulative_market_model(path,state,expected_archive_sha256=digest)
            self.assertEqual(report["source_counts"]["archive"],{"examples":2,"positives":1})
            self.assertEqual(report["source_counts"]["recent_observed"],{"examples":1,"positives":1})
            self.assertEqual(report["model"]["training_end_utc"],at(8))
            self.assertEqual(report["model"]["holdout_start_utc"],at(10))
            self.assertEqual(report["model"]["training_count"],3)
            self.assertEqual(report["model"]["positive_count"],2)
            self.assertEqual(report["comparison_status"],"FUTURE_HOLDOUT_NOT_YET_MATURE")
            self.assertFalse(report["production_applied"])


    def test_optional_partial_positive_training_does_not_invent_negative_labels(self):
        from paper_pov.heldout_outcome_adapter import train_shadow_challenger
        start=datetime(2026,1,1,tzinfo=timezone.utc)
        at=lambda d:(start+timedelta(days=d)).isoformat()
        preds=[dict(prediction_id=k,entry_utc=at(0),feature_asof_utc=at(0),features={"f":v})
               for k,v in (("a",2.),("b",0.),("c",3.),("d",4.))]
        def record(key,hit,complete):
            return dict(prediction_id=key,horizon_hours=48,entry_utc=at(0),
                        label_mature_utc=at(2),hit=hit,coverage_complete=complete,
                        outcome_status="MATURE" if complete else "MISSING_CANDLES",
                        source_sha256="a"*64)
        outcomes=[record("a",True,True),record("b",False,True),
                  record("c",None,False),record("d",None,False)]
        outcomes[2].update(crossing_evidence="PARTIAL_WINDOW",observed_crossing_candle_close_utc=at(1))
        kwargs=dict(training_end_utc=at(3),holdout_start_utc=at(5),feature_names=["f"])
        base=train_shadow_challenger(preds,outcomes,**kwargs)
        sensitivity=train_shadow_challenger(preds,outcomes,allow_observed_positive=True,**kwargs)
        self.assertEqual(base["training_count"],2)
        self.assertEqual(sensitivity["training_count"],3)
        self.assertEqual(sensitivity["partial_observed_positive_count"],1)
        self.assertEqual(sensitivity["negative_count"],1)
        self.assertIsNone(outcomes[2]["hit"])
        self.assertFalse(outcomes[2]["coverage_complete"])
        self.assertFalse(sensitivity["production_applied"])

if __name__ == "__main__":
    unittest.main()
