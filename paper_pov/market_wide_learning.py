"""Build prediction-independent learning anchors from completed five-minute candles.

Input candles use close timestamps, not Kraken interval-open timestamps.
Caller must authenticate source and supply the point-in-time eligible universe.
No production decisions or ledger writes.
"""
from bisect import bisect_left, bisect_right
from datetime import datetime, timedelta, timezone
import argparse
import json
from pathlib import Path
from math import isfinite
from .shadow_learning_evidence import utc_time, canonical_digest
from .heldout_outcome_adapter import reconstruct_forward_outcomes
from .frozen_historical_shadow import features_at_entry


def describe_observed_crossings(anchors, outcomes, candles, asof):
    """Capture actual candle-high crossings, even when the window has gaps.

    A partial observed positive is evidence of a price excursion, not a
    qualified label or a guarantee of execution. The candle close is an
    upper bound on crossing time, not the exact trade timestamp.
    """
    by_pair = {}
    for row in candles:
        t = utc_time(row["timestamp_utc"])
        if t <= asof:
            by_pair.setdefault(row["pair"], []).append((t, float(row["high"])))
    for rows in by_pair.values():
        rows.sort()
    times = {pair: [t for t, _ in rows] for pair, rows in by_pair.items()}
    by_id = {a["prediction_id"]: a for a in anchors}
    for o in outcomes:
        if o["hit"] is False:
            continue
        a = by_id[o["prediction_id"]]
        entry = utc_time(a["entry_utc"])
        end = min(asof, entry + timedelta(hours=o["horizon_hours"]))
        stamps = times.get(a["pair"], [])
        rows = by_pair.get(a["pair"], [])
        lo, hi = bisect_right(stamps, entry), bisect_right(stamps, end)
        first = next((t for t, high in rows[lo:hi] if high / a["entry_price"] - 1 >= .30), None)
        if first is not None:
            o["observed_crossing_candle_close_utc"] = first.isoformat()
            o["observed_lead_hours_upper_bound"] = (first - entry).total_seconds()/3600
            o["crossing_evidence"] = "COMPLETE_WINDOW" if o["coverage_complete"] else "PARTIAL_WINDOW"


def crossing_summary(outcomes):
    """Separate anchor-label counts from descriptive time-cluster counts.

    Cluster completed 48h hit crossings by pair and consecutive crossings
    within six hours. This is a reproducible event proxy, not exact exchange
    trade-level surge identity.
    """
    partial = {str(h): 0 for h in (1, 6, 24, 48)}
    by_pair = {}
    for o in outcomes:
        crossing = o.get("observed_crossing_candle_close_utc")
        if crossing is None:
            continue
        if not o["coverage_complete"]:
            partial[str(o["horizon_hours"])] += 1
        if o["horizon_hours"] == 48 and o["hit"] is True and o["coverage_complete"]:
            by_pair.setdefault(o["pair"], set()).add(utc_time(crossing))
    clusters = 0
    for stamps in by_pair.values():
        previous = None
        for stamp in sorted(stamps):
            if previous is None or stamp-previous > timedelta(hours=6):
                clusters += 1
            previous = stamp
    return {"partial_observed_crossings_by_horizon": partial,
            "completed_48h_crossing_clusters": clusters,
            "cluster_definition": "PAIR_CONSECUTIVE_CROSSINGS_WITHIN_6H_PROXY"}


def build_market_cohort(candles, *, eligible_pairs, evaluation_asof_utc,
                        eligibility_observations=None, anchor_start_utc=None):
    asof = utc_time(evaluation_asof_utc)
    anchor_start = utc_time(anchor_start_utc) if anchor_start_utc else None
    eligible = set(eligible_pairs)
    grouped = {}
    seen_at = {}
    if eligibility_observations is not None:
        for observation in eligibility_observations:
            if observation['pair'] in eligible:
                seen_at.setdefault(observation['pair'], []).append(utc_time(observation['at']))
        for pair in seen_at:
            seen_at[pair] = sorted(set(seen_at[pair]))
    eligibility_abstentions = 0
    for c in candles:
        if c["pair"] not in eligible:
            continue
        t = utc_time(c["timestamp_utc"])
        if t > asof:
            continue
        close, high = float(c["close"]), float(c["high"])
        if not (isfinite(close) and isfinite(high) and 0 < close <= high):
            raise ValueError("Invalid candle")
        grouped.setdefault(c["pair"], []).append((t, c))
    anchors, observed = [], []
    for pair, rows in sorted(grouped.items()):
        rows.sort(key=lambda r: r[0])
        if len({t for t, _ in rows}) != len(rows):
            raise ValueError("Duplicate candle")
        observed.extend(c for _, c in rows)
        for i in range(3, len(rows)):
            t, c = rows[i]
            if t + timedelta(hours=1) > asof:
                break
            if anchor_start is not None and t < anchor_start:
                continue
            if t.minute or t.second or t.microsecond:
                continue
            if eligibility_observations is not None:
                stamps = seen_at.get(pair, [])
                index = bisect_right(stamps, t) - 1
                if index < 0 or t - stamps[index] > timedelta(minutes=10):
                    eligibility_abstentions += 1
                    continue
            window = rows[i-3:i+1]
            if any(window[j][0]-window[j-1][0] != timedelta(minutes=5) for j in range(1,4)):
                continue
            p = float(c["close"])
            # Reuse the existing six-feature contract; label discovery remains
            # independent of whether the full feature window is available.
            features = features_at_entry(rows[max(0, i-12):i+1], t)
            anchors.append({"prediction_id": canonical_digest([pair,t.isoformat()]),
                            "pair": pair, "entry_utc": t.isoformat(),
                            "feature_asof_utc": t.isoformat(), "entry_price": p,
                            "features": features or {},
                            "feature_complete": features is not None,
                            "liquidity_qualified": False})
    outcomes = reconstruct_forward_outcomes(anchors, observed, evaluation_asof_utc=evaluation_asof_utc)
    describe_observed_crossings(anchors, outcomes, observed, asof)
    per_horizon = {}
    for h in (1, 6, 24, 48):
        rows = [o for o in outcomes if o["horizon_hours"] == h]
        per_horizon[str(h)] = {
            "hits": sum(o["hit"] is True for o in rows),
            "misses": sum(o["hit"] is False for o in rows),
            "immature": sum(o["outcome_status"] == "IMMATURE" for o in rows),
            "missing_candles": sum(o["outcome_status"] == "MISSING_CANDLES" for o in rows),
        }
    return {"anchors": anchors, "outcomes": outcomes,
            "per_horizon": per_horizon,
            "crossing_summary": crossing_summary(outcomes),
            "feature_complete_anchors": sum(a["feature_complete"] for a in anchors),
            "eligibility_abstentions": eligibility_abstentions,
            "eligibility_scope": "RECORDED_ASOF_OBSERVATIONS" if eligibility_observations is not None else "CALLER_SUPPLIED_UNIVERSE",
            "missing_eligible_pairs": sorted(eligible - set(grouped)),
            "eligible_pairs": sorted(eligible), "observed_pairs": sorted(grouped),
            "source_authenticated": False, "production_applied": False,
            "promotion_authorized": False}



STATE_SCHEMA = "market_wide_continuity_v1"
MAX_RETAINED_ANCHORS = 250000


def validate_prior_market_state(prior, ledger):
    if prior is None:
        return
    if prior.get("schema") != STATE_SCHEMA or prior.get("digest") != canonical_digest(
            {k: v for k, v in prior.items() if k != "digest"}):
        raise ValueError("Invalid market learning continuity checksum")
    if prior.get("production_applied") is not False:
        raise ValueError("Refusing promoted market learning state")
    if prior["ledger_generation"] > ledger["generation"]:
        raise ValueError("Market learning generation rollback")
    if utc_time(prior["evaluation_asof_utc"]) > utc_time(ledger["runs"][-1]["as_of"]):
        raise ValueError("Market learning time rollback")


def retain_hourly_eligibility(ledger, prior):
    """Preserve an actual observation in the ten minutes before each hour.

    Only the last 72h of evidence is needed for the recent REST OHLC window.
    No observation is manufactured for times we did not see.
    """
    now = utc_time(ledger["runs"][-1]["as_of"])
    cutoff = now - timedelta(hours=72)
    latest = {}
    for observation in (prior or {}).get("eligibility", []) + ledger["observations"]:
        t = utc_time(observation["at"])
        if not cutoff <= t <= now:
            continue
        hour = t.replace(minute=0, second=0, microsecond=0)
        if t != hour:
            hour += timedelta(hours=1)
        if hour-t > timedelta(minutes=10):
            continue
        key = (observation["pair"], hour)
        if key not in latest or t > utc_time(latest[key]["at"]):
            latest[key] = {"pair": observation["pair"], "at": t.isoformat()}
    return [latest[key] for key in sorted(latest)]


def merge_market_state(cohort, eligibility, prior):
    """Checksummed cumulative research state, never a second trade ledger.

    Preserve mature complete outcomes; replace immature/gap records when a
    genuinely complete re-observation becomes available. Each anchor/horizon
    counts only once across shards and reruns.
    """
    prior = prior or {}
    anchors = {a["prediction_id"]: a for a in prior.get("anchors", [])}
    outcomes = {(o["prediction_id"], o["horizon_hours"]): o
                for o in prior.get("outcomes", [])}
    for a in cohort["anchors"]:
        k = a["prediction_id"]
        old = anchors.get(k)
        if old is not None:
            identity = ("pair", "entry_utc", "feature_asof_utc", "entry_price")
            if any(old[f] != a[f] for f in identity):
                raise ValueError("Market learning anchor identity changed")
            if old["feature_complete"] and a["feature_complete"] and old["features"] != a["features"]:
                raise ValueError("Complete historical feature window changed")
            if old["feature_complete"] or not a["feature_complete"]:
                continue
        anchors[k] = a
    for o in cohort["outcomes"]:
        k = (o["prediction_id"], o["horizon_hours"])
        if k[0] not in anchors:
            raise ValueError("Outcome without retained market anchor")
        old = outcomes.get(k)
        if old is not None and old["coverage_complete"]:
            if o["coverage_complete"] and any(old[f] != o[f] for f in
                    ("hit", "max_favorable_return", "close_return")):
                raise ValueError("Complete market outcome changed")
            continue
        if old is None or o["coverage_complete"] or old["outcome_status"] == "IMMATURE":
            outcomes[k] = o
    if len(anchors) > MAX_RETAINED_ANCHORS:
        raise ValueError("Market learning state requires durable archive compaction; refusing silent loss")
    attempts = dict(prior.get("last_attempt_generation", {}))
    successes = dict(prior.get("last_success_generation", {}))
    generation = cohort["ledger_generation"]
    sequence = max(prior.get("attempt_sequence",0),max(attempts.values(),default=0))+1
    attempt_sequence = dict(prior.get("last_attempt_sequence",attempts))
    for pair in cohort["selected_pairs"]:
        attempts[pair] = generation
        attempt_sequence[pair] = sequence
    for pair in cohort["observed_pairs"]:
        successes[pair] = generation
    result = {"schema": STATE_SCHEMA, "ledger_generation": generation,
              "evaluation_asof_utc": cohort["evaluation_asof_utc"],
              "previous_digest": prior.get("digest"),
              "eligibility": eligibility,
              "anchors": [anchors[k] for k in sorted(anchors)],
              "outcomes": [outcomes[k] for k in sorted(outcomes)],
              "last_attempt_generation": attempts, "last_success_generation": successes,
              "attempt_sequence": sequence,"last_attempt_sequence":attempt_sequence,
              "production_applied": False, "source_authenticated": False}
    if prior.get("continuity_recovery_44220533486") is True:
        result["continuity_recovery_44220533486"]=True
    result["cold_segments"]=list(prior.get("cold_segments",[]))
    result["digest"] = canonical_digest(result)
    return result




def recover_market_state(primary, earlier):
    """Union two successful isolated research artifacts after a stale ancestor read.

    Do not discard immutable evidence or manufacture completed outcomes. The
    newer state remains the temporal authority; the earlier state contributes
    only compatible observations, anchors, labels and original shadow records.
    """
    if primary.get("schema")!=STATE_SCHEMA or earlier.get("schema")!=STATE_SCHEMA:
        raise ValueError("Invalid recovery state schema")
    for state in (primary,earlier):
        if state.get("digest")!=canonical_digest({k:v for k,v in state.items() if k!="digest"}) or state.get("production_applied") is not False:
            raise ValueError("Invalid recovery state checksum")
    if (earlier["ledger_generation"]>primary["ledger_generation"] or
            utc_time(earlier["evaluation_asof_utc"])>utc_time(primary["evaluation_asof_utc"])):
        raise ValueError("Recovery would advance beyond selected primary")
    # Keep the earliest original signal for repeated IDs; a stale replay
    # cannot replace a timely signal. Differences in signal economics fail.
    shadow={}
    for source in (earlier,primary):
        for p in source.get("shadow_predictions",[]):
            key=p["prediction_id"]
            old=shadow.get(key)
            if old is not None:
                immutable=("pair","batch_id","model_version","run_id","entry_price",
                           "feature_asof_utc","features","shadow_score","baseline_watch",
                           "shadow_equal_budget_watch")
                if any(old.get(k)!=p.get(k) for k in immutable):
                    raise ValueError("Recovered prospective prediction conflict")
                def order(row):
                    return (row.get("recording_scope")!="TIMELY_RECORDED_QUOTE_REFERENCE",
                            utc_time(row.get("recorded_at_utc",row["entry_utc"])))
                if order(old)<=order(p):
                    continue
            shadow[key]=p
    def union_outcomes(sources, field, allowed):
        merged={}
        for source in sources:
            for o in source.get(field,[]):
                key=(o["prediction_id"],o["horizon_hours"])
                if key[0] not in allowed or o["entry_utc"]!=allowed[key[0]]["entry_utc"]:
                    continue
                old=merged.get(key)
                if old is not None and old["coverage_complete"]:
                    if o["coverage_complete"] and any(old[k]!=o[k] for k in ("hit","max_favorable_return","close_return")):
                        raise ValueError("Recovered completed outcome conflict")
                    continue
                if old is None or o["coverage_complete"] or old["outcome_status"]=="IMMATURE":
                    merged[key]=o
        return [merged[k] for k in sorted(merged)]
    anchors={}
    for source in (earlier,primary):
        for a in source["anchors"]:
            key=a["prediction_id"]
            old=anchors.get(key)
            if old is not None:
                if any(old[k]!=a[k] for k in ("pair","entry_utc","feature_asof_utc","entry_price")):
                    raise ValueError("Recovered anchor identity conflict")
                if old["feature_complete"]:
                    if a["feature_complete"] and old["features"]!=a["features"]:
                        raise ValueError("Recovered feature conflict")
                    continue
            anchors[key]=a
    if max(len(anchors),len(shadow))>MAX_RETAINED_ANCHORS:
        raise ValueError("Recovered state requires archive compaction")
    result=dict(primary)
    result["anchors"]=[anchors[k] for k in sorted(anchors)]
    result["outcomes"]=union_outcomes((earlier,primary),"outcomes",anchors)
    result["shadow_predictions"]=[shadow[k] for k in sorted(shadow)]
    result["shadow_outcomes"]=union_outcomes((earlier,primary),"shadow_outcomes",shadow)
    result["eligibility"]=retain_hourly_eligibility(
        {"runs":[{"as_of":primary["evaluation_asof_utc"]}],"observations":primary["eligibility"]},earlier)
    for field in ("last_attempt_generation","last_success_generation","last_attempt_sequence"):
        values={}
        for source in (earlier,primary):
            for k,v in source.get(field,source.get("last_attempt_generation",{}) if field=="last_attempt_sequence" else {}).items():
                values[k]=max(values.get(k,0),v)
        result[field]=values
    result["attempt_sequence"]=max(primary.get("attempt_sequence",0),earlier.get("attempt_sequence",0),
                                  max(result["last_attempt_sequence"].values(),default=0))
    result["recovered_state_digests"]=sorted({primary["digest"],earlier["digest"]})
    result["digest"]=canonical_digest({k:v for k,v in result.items() if k!="digest"})
    return result


def select_completed_learning_publication(publication, fetch_writer, fetch_parent):
    """Choose one completed canonical writer, or its immediate immutable parent.

    This is research input selection, not scanner delivery. Stale research
    inputs may be replayed but may never be counted as timely predictions.
    """
    import re
    def validate(p):
        if (p.get("schema")!=2 or p.get("status")!="SUCCESS_PAPER_ONLY"
                or p.get("publication_mode")!="ATOMIC_LEDGER_RESULTS"
                or p.get("remote_readback_verified") is not True
                or p.get("buy_approved") is not False or p.get("production_applied") is not False
                or type(p.get("ledger_generation")) is not int or p["ledger_generation"]<=0
                or not re.fullmatch(r"[0-9a-f]{40}",str(p.get("source_sha","")))
                or not re.fullmatch(r"[0-9a-f]{64}",str(p.get("ledger_sha256","")))
                or not str(p.get("run_id","")).isdigit()):
            raise ValueError("Invalid canonical learning publication")
    def writer(p):
        w=fetch_writer(str(p["run_id"]))
        if str(w.get("id"))!=str(p["run_id"]) or w.get("head_branch")!="main" or w.get("head_sha")!=p["source_sha"]:
            raise ValueError("Learning writer identity mismatch")
        return w
    validate(publication)
    w=writer(publication)
    if w.get("status")=="completed" and w.get("conclusion")=="success":
        return publication, "CANONICAL_COMPLETED"
    if w.get("status") not in ("queued","in_progress"):
        raise ValueError("Canonical learning writer not successful")
    parent=publication.get("ledger_parent_commit","")
    if not re.fullmatch(r"[0-9a-f]{40}",parent):
        raise ValueError("Invalid immutable learning parent")
    prior=fetch_parent(parent)
    validate(prior)
    if prior["ledger_generation"]!=publication["ledger_generation"]-1 or str(prior["run_id"])==str(publication["run_id"]):
        raise ValueError("Learning parent continuity mismatch")
    w=writer(prior)
    if w.get("status")!="completed" or w.get("conclusion")!="success":
        raise ValueError("Immediate learning parent not successful")
    return prior, "IMMEDIATE_PARENT_COMPLETED_NEWER_IN_PROGRESS"


def select_market_batch(ledger, *, batch_size=12, prior=None):
    """Rotate independently of WATCH rankings across the latest observed universe.

    The latest writer's observations establish the current universe only.
    Historical eligibility is separately checked at each anchor.
    """
    if not 1 <= batch_size <= 30:
        raise ValueError("Expected between 1 and 30 markets")
    latest = ledger["runs"][-1]
    pairs = sorted({o["pair"] for o in ledger["observations"] if o["run_id"] == latest["id"]})
    if not pairs or len(pairs) != latest["observation_count"]:
        raise ValueError("Latest observed universe incomplete")
    generation = ledger["generation"]
    if type(generation) is not int or generation <= 0:
        raise ValueError("Invalid ledger generation")
    shard_count = (len(pairs) + batch_size - 1) // batch_size
    shard = (generation - 1) % shard_count
    if prior is not None:
        attempts = prior.get('last_attempt_sequence', prior['last_attempt_generation'])
        selected = sorted(pairs, key=lambda pair: (attempts.get(pair, 0), pair))[:batch_size]
        return pairs, selected, shard, shard_count
    return pairs, pairs[shard*batch_size:(shard+1)*batch_size], shard, shard_count



def score_prospective_market_shard(ledger, results, model_source, *, model_available_utc, top_k=5, recorded_at_utc=None):
    """Score independently selected current markets before forward outcomes.

    Compare only against actual WATCH decisions within this same scored shard,
    never represent it as a full production universe ranking. The shadow
    equal-budget selection uses the number of actual WATCHs in the shard.
    """
    from .frozen_historical_shadow import NAMES, frozen_model
    if not 1 <= top_k <= 12:
        raise ValueError("Invalid shadow selection budget")
    if model_source.get("schema") == "kraken_q3_frozen_shadow_v1":
        fitted = frozen_model(model_source)
        centers, scales, weights = fitted["means"], fitted["scales"], fitted["weights"]
        version = model_source["version"]
        train_end = utc_time(model_source["training_window_end"])
    else:
        if (model_source.get("schema") not in ("market_wide_archive_shadow_v1","market_wide_cumulative_shadow_v1")
                or model_source.get("digest") != canonical_digest({k:v for k,v in model_source.items() if k!="digest"})
                or model_source.get("production_applied") is not False):
            raise ValueError("Invalid shadow model report")
        fitted = model_source["model"]
        if fitted.get("status") != "SHADOW_ONLY" or fitted.get("version") != canonical_digest(
                {k:v for k,v in fitted.items() if k!="version"}):
            raise ValueError("Invalid fitted shadow model")
        if tuple(fitted["feature_names"]) != NAMES:
            raise ValueError("Incompatible shadow feature contract")
        centers, scales, weights = fitted["feature_centers"], fitted["feature_scales"], fitted["feature_weights"]
        version = fitted["version"]
        train_end = utc_time(fitted["training_end_utc"])
    latest = ledger["runs"][-1]
    scan_at = utc_time(latest["as_of"])
    available = utc_time(model_available_utc)
    recorded = utc_time(recorded_at_utc) if recorded_at_utc else datetime.now(timezone.utc)
    if recorded < scan_at:
        raise ValueError("Recording precedes the writer snapshot")
    if available < train_end or scan_at <= available:
        raise ValueError("Model was not available before this prospective scan")
    if scan_at < train_end + timedelta(hours=48):
        raise ValueError("Model training/scan purge insufficient")
    quotes = {o["pair"]: o for o in ledger["observations"] if o["run_id"] == latest["id"]}
    watch = {p["pair"] for p in ledger["predictions"] if p["run_id"] == latest["id"]}
    batch_id = canonical_digest([latest["id"], version, sorted(r["pair"] for r in results)])
    predictions, excluded = [], {}
    for result in results:
        pair = result["pair"]
        q = quotes[pair]
        at = utc_time(q["at"])
        if at < available or at > scan_at or scan_at-at > timedelta(minutes=3):
            excluded[pair] = "QUOTE_OUTSIDE_PROSPECTIVE_WINDOW"
            continue
        rows = sorted((utc_time(c["timestamp_utc"]), c) for c in result["candles"])
        features = features_at_entry(rows, at)
        if features is None:
            excluded[pair] = "NO_COMPLETE_ASOF_FEATURES"
            continue
        score = sum((features[f]-centers[f])/scales[f]*weights[f] for f in NAMES)
        price = float(q["price"])
        if price <= 0 or not isfinite(price) or not isfinite(score):
            raise ValueError("Invalid prospective score or price")
        timely = timedelta(0) <= recorded-at <= timedelta(minutes=10)
        # Evaluate only the forward window after the actual signal recording.
        # The earlier writer quote remains an explicitly non-executable reference.
        entry = recorded if timely else at
        predictions.append({"prediction_id": canonical_digest([batch_id,pair]), "pair":pair,
                            "run_id":latest["id"], "batch_id":batch_id, "model_version":version,
                            "model_available_utc":available.isoformat(), "entry_utc":entry.isoformat(),
                            "quote_observed_at":at.isoformat(),"recorded_at_utc":recorded.isoformat(),
                            "recording_scope":"TIMELY_RECORDED_QUOTE_REFERENCE" if timely else "ASOF_REPLAY_ONLY",
                            "feature_asof_utc":max(t for t,_ in rows if t<=at).isoformat(),
                            "entry_price":price, "features":features, "shadow_score":score,
                            "baseline_watch":pair in watch, "source_sha256":result["response_sha256"],
                            "liquidity_qualified":False})
    predictions.sort(key=lambda p:(-p["shadow_score"],p["pair"]))
    budget = sum(p["baseline_watch"] for p in predictions)
    for i,p in enumerate(predictions):
        p["shadow_rank"] = i+1
        p["shadow_top_k"] = i<top_k
        p["shadow_equal_budget_watch"] = i<budget
    return {"predictions": predictions, "excluded": excluded, "baseline_budget":budget,
            "model_version":version, "batch_id":batch_id,
            "scope":"CURRENT_ROTATING_SHARD_NOT_FULL_UNIVERSE",
            "production_applied":False, "promotion_authorized":False}



def prospective_metrics_by_version(predictions, outcomes):
    """Equal-budget paired metrics for each model and each horizon.

    Never combine different fitted model versions into one performance claim.
    Report incomplete or unselected batches rather than counting them as losses.
    """
    groups={}
    for p in predictions:
        if p.get("recording_scope")=="TIMELY_RECORDED_QUOTE_REFERENCE":
            groups.setdefault((p["model_version"],p["batch_id"]),[]).append(p)
    labels={(o["prediction_id"],o["horizon_hours"]):o for o in outcomes}
    result={}
    for (version,_),group in groups.items():
        base=[p for p in group if p["baseline_watch"]]
        shadow=[p for p in group if p["shadow_equal_budget_watch"]]
        by_h=result.setdefault(version,{str(h):{"paired_complete_batches":0,"unavailable_batches":0,
            "zero_budget_batches":0,"selected_per_scanner":0,"baseline_hits":0,"shadow_hits":0,
            "timely_scored_anchors":0,"known_positive_anchors":0,"unknown_outcome_anchors":0,
            "baseline_known_missed_positives":0,"shadow_known_missed_positives":0,
            "baseline_known_detected_positives":0,"shadow_known_detected_positives":0,
            "baseline_crossing_lead_hours_upper_bounds":[],"shadow_crossing_lead_hours_upper_bounds":[]}
            for h in (1,6,24,48)})
        for h in (1,6,24,48):
            m=by_h[str(h)]
            # Coverage and missed-positive accounting is restricted to timely
            # scored shard anchors; it is not full-universe event recall.
            for p in group:
                o=labels.get((p["prediction_id"],h))
                m["timely_scored_anchors"]+=1
                if not o or o["coverage_complete"] is not True or type(o["hit"]) is not bool:
                    m["unknown_outcome_anchors"]+=1
                    continue
                if not o["hit"]:
                    continue
                m["known_positive_anchors"]+=1
                for scanner, selected in (("baseline",p["baseline_watch"]),
                                          ("shadow",p["shadow_equal_budget_watch"])):
                    m[f"{scanner}_known_{'detected' if selected else 'missed'}_positives"]+=1
                    lead=o.get("observed_lead_hours_upper_bound")
                    if selected and type(lead) in (int,float) and isfinite(lead) and 0<=lead<=h:
                        m[f"{scanner}_crossing_lead_hours_upper_bounds"].append(lead)
            if not base and not shadow:
                m["zero_budget_batches"]+=1
                continue
            keys=[(p["prediction_id"],h) for p in base+shadow]
            if (len(base)!=len(shadow) or any(k not in labels or
                   labels[k]["coverage_complete"] is not True or type(labels[k]["hit"]) is not bool
                   for k in keys)):
                m["unavailable_batches"]+=1
                continue
            m["paired_complete_batches"]+=1
            m["selected_per_scanner"]+=len(base)
            m["baseline_hits"]+=sum(labels[(p["prediction_id"],h)]["hit"] for p in base)
            m["shadow_hits"]+=sum(labels[(p["prediction_id"],h)]["hit"] for p in shadow)
    for by_h in result.values():
        for m in by_h.values():
            n=m["selected_per_scanner"]
            m["baseline_false_positives"]=n-m["baseline_hits"]
            m["shadow_false_positives"]=n-m["shadow_hits"]
            m["baseline_precision"]=m["baseline_hits"]/n if n else None
            m["shadow_precision"]=m["shadow_hits"]/n if n else None
            # Report known misses and observed lead bounds separately from
            # equal-budget paired precision. Never treat unknowns as negatives.
            for scanner in ("baseline","shadow"):
                leads=m.pop(f"{scanner}_crossing_lead_hours_upper_bounds")
                m[f"{scanner}_crossing_lead_samples"]=len(leads)
                m[f"{scanner}_mean_lead_hours_upper_bound"]=sum(leads)/len(leads) if leads else None
            m["missed_positive_scope"]="TIMELY_SCORED_SHARD_ANCHORS_ONLY"
            m["measured_lift_verified"]=False
    return result


def eligible_scoring_model(model, available, scan_at):
    """Availability is an actual prior artifact completion timestamp."""
    if model.get("schema")=="kraken_q3_frozen_shadow_v1":
        training_end=utc_time(model["training_window_end"])
    else:
        if model.get("schema") not in ("market_wide_archive_shadow_v1","market_wide_cumulative_shadow_v1"):
            raise ValueError("Unrecognized model schema")
        if model.get("digest")!=canonical_digest({k:v for k,v in model.items() if k!="digest"}):
            raise ValueError("Model report checksum mismatch")
        if model["model"]["status"]!="SHADOW_ONLY":
            return False
        training_end=utc_time(model["model"]["training_end_utc"])
    at,ready=utc_time(scan_at),utc_time(available)
    return training_end<=ready<at and at>=training_end+timedelta(hours=48)



def due_outcome_followups(prior, eligible_pairs, scored_pairs, *, asof, budget):
    """Use spare requests for matured paired windows first, then missed-gainer controls.

    Revisit older markets before their five-minute REST history expires.
    A genuinely incomplete window remains an abstention. Unselected timely
    anchors need outcomes too: otherwise known-miss counts are selection-biased.
    The independent rotation and WATCH controls keep their existing budget.
    """
    if not prior or budget<=0:
        return []
    now=utc_time(asof)
    eligible=set(eligible_pairs)-set(scored_pairs)
    outcomes={(o["prediction_id"],o["horizon_hours"]):o for o in prior.get("shadow_outcomes",[])}
    groups={}
    for p in prior.get("shadow_predictions",[]):
        if p.get("recording_scope")=="TIMELY_RECORDED_QUOTE_REFERENCE":
            groups.setdefault((p["model_version"],p["batch_id"]),[]).append(p)
    due={}
    for group in groups.values():
        base=[p for p in group if p["baseline_watch"]]
        shadow=[p for p in group if p["shadow_equal_budget_watch"]]
        if not base or len(base)!=len(shadow):
            continue
        selected={p["prediction_id"]:p for p in base+shadow}
        for hours in (1,6,24,48):
            # Do not spend extra requests on a cohort already known incomplete.
            rows=[outcomes.get((p["prediction_id"],hours)) for p in selected.values()]
            if any(o and o["outcome_status"]=="MISSING_CANDLES" for o in rows):
                continue
            for p in selected.values():
                entry=utc_time(p["entry_utc"])
                if not entry+timedelta(hours=hours)<=now<=entry+timedelta(hours=59):
                    continue
                o=outcomes.get((p["prediction_id"],hours))
                if p["pair"] not in eligible or (o and o["outcome_status"]!="IMMATURE"):
                    continue
                priority=(entry,-hours,p["pair"])
                if p["pair"] not in due or priority<due[p["pair"]]:
                    due[p["pair"]]=priority
    # Complete the paired evaluation budget first. Only remaining requests
    # go to timely anchors not selected by either scanner (including zero
    # selection-budget batches). This measures known missed positives without
    # treating uncovered controls as negatives or altering the scoring set.
    paired=sorted(due,key=due.get)[:budget]
    if len(paired)==budget:
        return paired
    controls={}
    for group in groups.values():
        for p in group:
            if p["baseline_watch"] or p["shadow_equal_budget_watch"]:
                continue
            pair=p["pair"]
            if pair not in eligible or pair in due:
                continue
            entry=utc_time(p["entry_utc"])
            for hours in (1,6,24,48):
                if not entry+timedelta(hours=hours)<=now<=entry+timedelta(hours=59):
                    continue
                o=outcomes.get((p["prediction_id"],hours))
                if o and o["outcome_status"]!="IMMATURE":
                    continue
                priority=(entry,-hours,pair)
                if pair not in controls or priority<controls[pair]:
                    controls[pair]=priority
    return paired+sorted(controls,key=controls.get)[:budget-len(paired)]


def retain_prospective_shadow(state, prior, cohort, results, ledger, model_source=None, model_available_utc=None, scored_pairs=None):
    """Retain immutable prospective predictions and re-evaluate revisited markets."""
    prior = prior or {}
    predictions = {p["prediction_id"]:p for p in prior.get("shadow_predictions",[])}
    outcomes = {(o["prediction_id"],o["horizon_hours"]):o for o in prior.get("shadow_outcomes",[])}
    snapshot = None
    if model_source is not None:
        score_results=results if scored_pairs is None else [r for r in results if r['pair'] in scored_pairs]
        snapshot = score_prospective_market_shard(ledger,score_results,model_source,
                                                model_available_utc=model_available_utc)
        for p in snapshot["predictions"]:
            old = predictions.get(p["prediction_id"])
            # A repeated source fetch may have a different response digest, but
            # the originally recorded feature/decision/price must not change.
            if old is not None:
                if any(old.get(k)!=p[k] for k in p if k not in ("source_sha256","entry_utc","recorded_at_utc","recording_scope","quote_observed_at")):
                    raise ValueError("Prospective prediction identity changed")
                continue
            predictions[p["prediction_id"]] = p
    observed = {r["pair"] for r in results}
    asof = utc_time(cohort["evaluation_asof_utc"])
    active = [p for p in predictions.values() if p["pair"] in observed
              and asof-timedelta(hours=60)<=utc_time(p["entry_utc"])<=asof]
    candles=[c for r in results for c in r["candles"]]
    fresh = reconstruct_forward_outcomes(active,candles,evaluation_asof_utc=asof.isoformat())
    describe_observed_crossings(active,fresh,candles,asof)
    for o in fresh:
        key=(o["prediction_id"],o["horizon_hours"])
        old=outcomes.get(key)
        if old is not None and old["coverage_complete"]:
            if o["coverage_complete"] and any(old[k]!=o[k] for k in ("hit","close_return","max_favorable_return")):
                raise ValueError("Verified prospective outcome changed")
            continue
        if old is None or o["coverage_complete"] or old["outcome_status"]=="IMMATURE":
            outcomes[key]=o
    if len(predictions)>MAX_RETAINED_ANCHORS:
        raise ValueError("Prospective evidence needs archive compaction")
    state["shadow_predictions"]=[predictions[k] for k in sorted(predictions)]
    state["shadow_outcomes"]=[outcomes[k] for k in sorted(outcomes)]
    state["digest"]=canonical_digest({k:v for k,v in state.items() if k!="digest"})
    groups={}
    for p in predictions.values():
        groups.setdefault(p["batch_id"],[]).append(p)
    count=hits_base=hits_shadow=selected=0
    for group in groups.values():
        if not all(p.get("recording_scope")=="TIMELY_RECORDED_QUOTE_REFERENCE" for p in group):
            continue
        base=[p for p in group if p["baseline_watch"]]
        shadow=[p for p in group if p["shadow_equal_budget_watch"]]
        keys=[(p["prediction_id"],48) for p in base+shadow]
        if not base or len(base)!=len(shadow) or any(k not in outcomes or not outcomes[k]["coverage_complete"] for k in keys):
            continue
        count+=1
        selected+=len(base)
        hits_base+=sum(outcomes[(p["prediction_id"],48)]["hit"] for p in base)
        hits_shadow+=sum(outcomes[(p["prediction_id"],48)]["hit"] for p in shadow)
    return {"scope":"ACTUAL_WATCHS_EQUAL_BUDGET_WITHIN_SCORED_SHARDS",
            "prospective_snapshot":snapshot, "retained_predictions":len(predictions),
            "timely_recorded_predictions":sum(p.get("recording_scope")=="TIMELY_RECORDED_QUOTE_REFERENCE" for p in predictions.values()),
            "replay_only_predictions":sum(p.get("recording_scope")!="TIMELY_RECORDED_QUOTE_REFERENCE" for p in predictions.values()),
            "paired_complete_batches":count,"selected_per_scanner":selected,
            "baseline_hits":hits_base,"shadow_hits":hits_shadow,
            "by_model_and_horizon":prospective_metrics_by_version(predictions.values(),outcomes.values()),
            "measured_lift_verified":False,"production_applied":False}


def run_observed_market_batch(ledger, *, fetch=None, batch_size=12, prior=None,
                              model_source=None, model_available_utc=None, include_watch_controls=False):
    """Read-only real Kraken smoke; never describes a shard as full coverage."""
    from .kraken_observed_candles import fetch_kraken_ohlc
    fetch = fetch or fetch_kraken_ohlc
    validate_prior_market_state(prior, ledger)
    pairs, selected, shard, shard_count = select_market_batch(ledger, batch_size=batch_size, prior=prior)
    independent = list(selected)
    controls = []
    if include_watch_controls:
        latest_id = ledger['runs'][-1]['id']
        controls = sorted({p['pair'] for p in ledger['predictions'] if p['run_id']==latest_id} & set(pairs))
        selected = sorted(set(independent) | set(controls))
        if len(selected)>30:
            raise ValueError('Independent market and WATCH controls exceed bounded request budget')
    scored_pairs=list(selected)
    followups=due_outcome_followups(prior,pairs,scored_pairs,asof=ledger['runs'][-1]['as_of'],budget=30-len(scored_pairs))
    selected=scored_pairs+followups
    results, errors = [], {}
    for pair in selected:
        try:
            result = fetch(pair)
            digest = result["response_sha256"]
            if (result["pair"] != pair or result["source"] != "kraken_public_ohlc_rest"
                    or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest)
                    or any(row["pair"] != pair for row in result["candles"])
                    or not result["candles"]):
                raise ValueError("Invalid Kraken response evidence")
            results.append(result)
        except (ValueError, KeyError, OSError) as exc:
            errors[pair] = str(exc)[:200]
    if not results:
        raise ValueError("No successful Kraken OHLC responses: " + repr(errors))
    latest = ledger["runs"][-1]
    eligibility = retain_hourly_eligibility(ledger, prior)
    cohort = build_market_cohort(
        [c for item in results for c in item["candles"]],
        eligible_pairs=pairs, evaluation_asof_utc=latest["as_of"],
        eligibility_observations=eligibility)
    digests = {item["pair"]: item["response_sha256"] for item in results}
    for row in cohort["anchors"] + cohort["outcomes"]:
        row["source_sha256"] = digests[row["pair"]]
    cohort.update(schema="market_wide_observed_learning_v1",
                  ledger_generation=ledger["generation"], ledger_run_id=latest["id"],
                  evaluation_asof_utc=latest["as_of"], selected_pairs=selected,
                  independent_selected_pairs=independent, watch_control_pairs=controls,
                  outcome_followup_pairs=followups,
                  shard_index=shard, shard_count=shard_count, fetch_errors=errors,
                  source_digests=digests, coverage_scope="PARTIAL_ROTATING_SHARD_PLUS_WATCH_CONTROLS" if include_watch_controls else "PARTIAL_ROTATING_SHARD",
                  measured_lift_verified=False)
    cohort["continuity_state"] = merge_market_state(cohort, eligibility, prior)
    cohort["prospective_shadow"] = retain_prospective_shadow(cohort["continuity_state"], prior, cohort,
        results, ledger, model_source, model_available_utc,scored_pairs=set(scored_pairs))
    cohort["evidence_digest"] = canonical_digest(cohort)
    return cohort



def run_archive_market_cohorts(zip_path, *, expected_sha256, start_utc, end_utc, cohort_output):
    """Stream independent market cohorts from pinned Kraken OHLCVT archive bytes.

    Archive-listed USD pairs are an observed historical universe, not certified
    past live eligibility or executable liquidity. Keep those distinctions.
    Only one pair is in memory at a time; emitted cohorts can be reused.
    """
    import csv
    import gzip
    import hashlib
    import io
    import zipfile
    from historical.kraken_q3_48h_shadow import parse_market, parse_bar

    start, end = utc_time(start_utc), utc_time(end_utc)
    if end <= start or end - start > timedelta(days=366):
        raise ValueError("Expected bounded historical window")
    digest = hashlib.sha256()
    with Path(zip_path).open("rb") as src:
        for block in iter(lambda: src.read(4*1024*1024), b""):
            digest.update(block)
    archive_sha = digest.hexdigest()
    if archive_sha != expected_sha256:
        raise ValueError("Historical archive SHA256 mismatch")
    counts = {str(h): {k: 0 for k in ("hits", "misses", "immature", "missing_candles")}
              for h in (1, 6, 24, 48)}
    observed_markets = anchors = features = valid_bars = 0
    crossing_clusters = 0
    partial_crossings = {str(h): 0 for h in (1, 6, 24, 48)}
    markets_with_hits = set()
    Path(cohort_output).parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as archive, gzip.open(cohort_output, "wt", encoding="utf-8") as output:
        members = sorted((parse_market(n), n) for n in archive.namelist() if parse_market(n))
        if not members or len({pair for pair, _ in members}) != len(members):
            raise ValueError("Missing or ambiguous historical USD archive members")
        for pair, name in members:
            candles = []
            with archive.open(name) as source:
                for row in csv.reader(io.TextIOWrapper(source, encoding="utf-8")):
                    bar = parse_bar(row)
                    if bar is None:
                        continue
                    stamp, close, volume, trades = bar
                    # Archive timestamps are interval-open; features know the
                    # close only five minutes later.
                    t = datetime.fromtimestamp(stamp, tz=timezone.utc) + timedelta(minutes=5)
                    if start-timedelta(hours=1) <= t <= end:
                        candles.append({"pair": pair, "timestamp_utc": t.isoformat(),
                                        "close": close, "high": float(row[2]),
                                        "volume": volume, "trades": trades})
            if not candles:
                continue
            valid_bars += len(candles)
            observed_markets += 1
            cohort = build_market_cohort(candles, eligible_pairs=[pair],
                                         evaluation_asof_utc=end.isoformat(),
                                         anchor_start_utc=start.isoformat())
            for record in cohort["anchors"] + cohort["outcomes"]:
                record["source_sha256"] = archive_sha
            cohort.update(source_archive_sha256=archive_sha, source_member=name,
                          eligibility_scope="OBSERVED_ARCHIVE_USD_NOT_LIVE_POLICY")
            output.write(json.dumps(cohort, sort_keys=True, separators=(",", ":")) + "\n")
            crossing_clusters += cohort["crossing_summary"]["completed_48h_crossing_clusters"]
            for h, count in cohort["crossing_summary"]["partial_observed_crossings_by_horizon"].items():
                partial_crossings[h] += count
            anchors += len(cohort["anchors"])
            features += cohort["feature_complete_anchors"]
            for h, row_counts in cohort["per_horizon"].items():
                for key, count in row_counts.items():
                    counts[h][key] += count
                if row_counts["hits"]:
                    markets_with_hits.add(pair)
    if anchors == 0:
        raise ValueError("No historical learning anchors in requested window")
    return {"schema": "market_wide_archive_summary_v1", "archive_sha256": archive_sha,
            "pinned_archive_verified": True, "source_authenticated": False,
            "start_utc": start.isoformat(), "end_utc": end.isoformat(),
            "archive_usd_members": len(members), "observed_markets": observed_markets,
            "valid_bars": valid_bars, "anchors": anchors, "feature_complete_anchors": features,
            "per_horizon": counts, "markets_with_hits": sorted(markets_with_hits),
            "crossing_summary": {"partial_observed_crossings_by_horizon": partial_crossings,
                                 "completed_48h_crossing_clusters": crossing_clusters,
                                 "cluster_definition": "PAIR_CONSECUTIVE_CROSSINGS_WITHIN_6H_PROXY"},
            "eligibility_scope": "OBSERVED_ARCHIVE_USD_NOT_LIVE_POLICY",
            "label_scope": "COMPLETE_CANDLE_HIGH_NOT_EXECUTABLE_FILL",
            "production_applied": False, "promotion_authorized": False,
            "measured_lift_verified": False}



def train_archive_shadow(cohort_path, *, training_end_utc, holdout_start_utc,
                         evaluation_asof_utc, top_k=5, allow_observed_positive=False):
    """Fit the existing shadow trainer on saved archive cohorts, then rank.

    Historical baseline is the existing absolute 60m momentum proxy, NOT
    the production ranker. All feature-complete candidates enter each
    ranking before outcome coverage is inspected. Compare only timestamps
    at which both selected sets have complete 48h labels.
    """
    import gzip
    from .frozen_historical_shadow import NAMES
    from .heldout_outcome_adapter import train_shadow_challenger
    if not 1 <= top_k <= 12:
        raise ValueError("Invalid evaluation selection budget")
    training_end = utc_time(training_end_utc)
    holdout_start = utc_time(holdout_start_utc)
    asof = utc_time(evaluation_asof_utc)
    if asof <= holdout_start + timedelta(hours=48):
        raise ValueError("No mature blind holdout interval")
    predictions, outcomes, seen = [], [], set()
    archive_digests = set()
    with gzip.open(cohort_path, "rt", encoding="utf-8") as source:
        for line in source:
            cohort = json.loads(line)
            digest = cohort["source_archive_sha256"]
            if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
                raise ValueError("Invalid cohort archive digest")
            if cohort.get("production_applied") is not False or cohort.get("source_authenticated") is not False:
                raise ValueError("Unexpected archive cohort qualification")
            archive_digests.add(digest)
            qualified = set()
            for a in cohort["anchors"]:
                key = a["prediction_id"]
                if key in seen:
                    raise ValueError("Duplicate archive anchor")
                seen.add(key)
                if a["source_sha256"] != digest:
                    raise ValueError("Anchor archive provenance mismatch")
                entry = utc_time(a["entry_utc"])
                if (not a["feature_complete"] or entry+timedelta(hours=48)>asof or
                        training_end <= entry < holdout_start):
                    continue
                predictions.append(a)
                qualified.add(key)
            for o in cohort["outcomes"]:
                if o["horizon_hours"] == 48 and o["prediction_id"] in qualified:
                    if o["source_sha256"] != digest:
                        raise ValueError("Outcome archive provenance mismatch")
                    outcomes.append(o)
    if len(archive_digests) != 1:
        raise ValueError("Expected one pinned archive for initial shadow replay")
    model = train_shadow_challenger(predictions, outcomes, training_end_utc=training_end_utc,
                                    holdout_start_utc=holdout_start_utc, feature_names=NAMES,
                                    allow_observed_positive=allow_observed_positive)
    by_id = {a["prediction_id"]: a for a in predictions}
    labels = {o["prediction_id"]: o for o in outcomes
              if o["coverage_complete"] and type(o["hit"]) is bool}
    outcome_by_id = {o["prediction_id"]:o for o in outcomes}
    scores = model.get("shadow_scores", {})
    groups = {}
    for key in scores:
        groups.setdefault(by_id[key]["entry_utc"], []).append(key)
    metrics = {n: {"selected": 0, "hits": 0, "false_positives": 0, "early_hits": 0,
                   "lead_hours_sum": 0., "lead_count": 0} for n in ("baseline_proxy", "challenger")}
    bounds = {n:{"selected":0,"complete_hits":0,"complete_misses":0,
                 "partial_observed_hits":0,"unknown":0} for n in metrics}
    comparable, unavailable, covered_positive_anchors = 0, 0, 0
    for stamp, keys in sorted(groups.items()):
        base = sorted(keys, key=lambda k: (-abs(by_id[k]["features"]["momentum_60m"]), k))[:top_k]
        challenger = sorted(keys, key=lambda k: (-scores[k], k))[:top_k]
        if len(base) == top_k:
            for name, selected in (("baseline_proxy",base),("challenger",challenger)):
                b = bounds[name]
                b["selected"] += len(selected)
                for key in selected:
                    o = outcome_by_id.get(key, {})
                    if key in labels:
                        b["complete_hits" if labels[key]["hit"] else "complete_misses"] += 1
                    elif o.get("crossing_evidence") == "PARTIAL_WINDOW":
                        b["partial_observed_hits"] += 1
                    else:
                        b["unknown"] += 1
        if len(base) != top_k or any(k not in labels for k in base+challenger):
            unavailable += 1
            continue
        comparable += 1
        covered_positive_anchors += sum(labels[k]["hit"] for k in keys if k in labels)
        for name, selected in (("baseline_proxy", base), ("challenger", challenger)):
            m = metrics[name]
            m["selected"] += len(selected)
            for key in selected:
                o = labels[key]
                if not o["hit"]:
                    m["false_positives"] += 1
                    continue
                m["hits"] += 1
                m["early_hits"] += int(abs(by_id[key]["features"]["momentum_60m"]) <= .03)
                lead = o.get("observed_lead_hours_upper_bound")
                if lead is not None:
                    m["lead_hours_sum"] += lead
                    m["lead_count"] += 1
    for m in metrics.values():
        m["precision"] = m["hits"]/m["selected"] if m["selected"] else None
        m["covered_anchor_recall"] = m["hits"]/covered_positive_anchors if covered_positive_anchors else None
        m["mean_lead_hours_upper_bound"] = m.pop("lead_hours_sum")/m["lead_count"] if m["lead_count"] else None
        m.pop("lead_hours_sum", None)
    for b in bounds.values():
        b["observed_hit_lower_bound"] = b["complete_hits"] + b["partial_observed_hits"]
        b["possible_hit_upper_bound"] = b["observed_hit_lower_bound"] + b["unknown"]
        b["precision_lower_bound"] = b["observed_hit_lower_bound"]/b["selected"] if b["selected"] else None
        b["precision_upper_bound"] = b["possible_hit_upper_bound"]/b["selected"] if b["selected"] else None
    # Retain the actual fitted model, not the potentially large temporary
    # vector of holdout predictions. The model version is recomputed here.
    model.pop("shadow_scores", None)
    model["source_archive_sha256"] = next(iter(archive_digests))
    model["version"] = canonical_digest({k:v for k,v in model.items() if k!="version"})
    result = {"schema": "market_wide_archive_shadow_v1", "model": model,
              "evaluation_asof_utc": evaluation_asof_utc, "top_k": top_k,
              "training_label_policy":"OBSERVED_POSITIVE_SENSITIVITY" if allow_observed_positive else "COMPLETE_ONLY",
              "baseline": "HISTORICAL_ABS_MOMENTUM_60M_PROXY_NOT_PRODUCTION",
              "comparison_status": "SHADOW_EVALUATED" if comparable else "NO_PAIRED_COMPLETE_TIMESTAMPS",
              "comparable_timestamps": comparable, "unavailable_timestamps": unavailable,
              "covered_positive_anchors": covered_positive_anchors, "metrics": metrics,
              "all_ranked_selection_observation_bounds":bounds,
              "bounds_scope":"DESCRIPTIVE_CANDLE_HIGH_NOT_QUALIFIED_LIFT",
              "source_authenticated": False, "measured_lift_verified": False,
              "production_applied": False, "promotion_authorized": False}
    result["digest"] = canonical_digest(result)
    return result



def train_cumulative_market_model(cohort_path, state, *, expected_archive_sha256, additional_archives=(), retained_observed=(), historical_trade_directory=None, compact_seed=None, original_cohort_hashes=None, cold_state_directory=None):
    """Refit on archived and newly matured independent labels, then freeze.

    This is a new prospective model, not a repeat of the historical holdout.
    The training cutoff precedes the observed state by the required 48h
    purge, so the next genuinely later scan can use the frozen model.
    Never claim source authentication, verified lift or production approval.
    """
    import gzip
    import hashlib
    from .frozen_historical_shadow import NAMES
    from .heldout_outcome_adapter import train_shadow_challenger
    if (state.get("schema") != STATE_SCHEMA or state.get("digest") != canonical_digest(
            {k:v for k,v in state.items() if k!="digest"}) or state.get("production_applied") is not False):
        raise ValueError("Invalid cumulative learning state")
    observed_asof = utc_time(state["evaluation_asof_utc"])
    cutoff = observed_asof - timedelta(hours=48)
    eligible, labels = {}, {}
    origin = {}
    def ingest(anchors, outcomes, namespace):
        by_id = {}
        for a in anchors:
            if not a.get("feature_complete"):
                continue
            entry = utc_time(a["entry_utc"])
            if entry+timedelta(hours=48)>cutoff:
                continue
            key = a["prediction_id"]
            if key in by_id:
                raise ValueError("Duplicate source anchor")
            by_id[key] = a
        for o in outcomes:
            if o["horizon_hours"]!=48 or o["prediction_id"] not in by_id:
                continue
            if not o["coverage_complete"] or type(o["hit"]) is not bool:
                continue
            if utc_time(o["label_mature_utc"])>cutoff:
                continue
            a = by_id[o["prediction_id"]]
            identity = (a["pair"],utc_time(a["entry_utc"]).isoformat())
            if utc_time(o["label_mature_utc"])!=utc_time(a["entry_utc"])+timedelta(hours=48):
                raise ValueError("Unexpected label maturity")
            if identity in eligible:
                previous=eligible[identity]
                previous_label=labels[identity]
                if (previous["features"]!=a["features"] or previous["entry_price"]!=a["entry_price"]
                        or previous_label["hit"]!=o["hit"]):
                    raise ValueError("Conflicting historical/live training overlap")
                continue
            eligible[identity]=a
            labels[identity]=o
            origin[identity]=namespace
    sources=[(Path(cohort_path),expected_archive_sha256)]+[(Path(p),d) for p,d in additional_archives]
    if any(len(d)!=64 or any(c not in "0123456789abcdef" for c in d) for _,d in sources):
        raise ValueError("Invalid pinned archive digest")
    from .learning_retention import file_sha,load_seed,read_rows,validate_source
    specs=[("archive",path,d) for path,d in sources]+[("retained_observed",Path(p),d) for p,d in retained_observed]
    source_receipts=[]
    observed_receipts=[]
    if compact_seed is not None:
        if original_cohort_hashes is None or len(original_cohort_hashes)!=len(specs):
            raise ValueError("Compact seed requires pinned original cohort hashes")
        manifest=load_seed(compact_seed,[(kind,d,h) for (kind,_,d),h in zip(specs,original_cohort_hashes)])
    else:
        manifest=None
    for i,(kind,path,expected) in enumerate(specs):
        if len(expected)!=64 or any(c not in "0123456789abcdef" for c in expected):
            raise ValueError("Invalid source digest")
        if manifest is not None:
            rec=manifest["sources"][i]
            original=rec["cohort_sha256"]
            path=Path(compact_seed)/rec["seed_file"]
        else:
            original=file_sha(path)
            if original_cohort_hashes is not None and original!=original_cohort_hashes[i]:
                raise ValueError("Pinned original cohort checksum mismatch")
        for c in read_rows(path):
            validate_source(c,kind,expected)
            ingest(c["anchors"],c["outcomes"],kind)
        if kind=="archive":
            source_receipts.append({"archive_sha256":expected,"cohort_sha256":original})
        else:
            observed_receipts.append({"snapshot_set_sha256":expected,"cohort_sha256":original})
    trade_receipts=[]
    # Event-prioritized samples are potentially outcome-enriched. Retain
    # their counts in a distinct sensitivity dataset, not the strict fit.
    # Admit only randomly/outcome-independently sampled windows to the main
    # fit once that sampling provenance is recorded and verified.
    trade_examples=trade_positives=0
    if historical_trade_directory is not None:
        from .historical_trade_batch import verified_trade_cohorts
        for c, receipt in verified_trade_cohorts(historical_trade_directory):
            anchors={a["prediction_id"]:a for a in c["anchors"] if a.get("feature_complete")}
            for o in c["outcomes"]:
                if (o["horizon_hours"]==48 and o["prediction_id"] in anchors and
                    o["coverage_complete"] and type(o["hit"]) is bool and
                    utc_time(o["label_mature_utc"])<=cutoff):
                    trade_examples+=1
                    trade_positives+=int(o["hit"])
            trade_receipts.append(receipt)
    if state.get("cold_segments"):
        if cold_state_directory is None:
            raise ValueError("Cumulative training requires retained cold history")
        from .learning_retention import assemble_history
        history=assemble_history(state,cold_state_directory)
        ingest(history["anchors"],history["outcomes"],"recent_observed")
    else:
        ingest(state["anchors"],state["outcomes"],"recent_observed")
    keys=sorted(eligible)
    model=train_shadow_challenger([eligible[k] for k in keys],[labels[k] for k in keys],
                                  training_end_utc=cutoff.isoformat(),
                                  holdout_start_utc=(cutoff+timedelta(hours=48)).isoformat(),feature_names=NAMES)
    model.pop("shadow_scores",None)
    model["source_archive_sha256"]=expected_archive_sha256
    model["archive_cohort_receipts"]=source_receipts
    model["retained_observed_cohort_receipts"]=observed_receipts
    model["training_dataset_digest"]=canonical_digest([[eligible[k],labels[k]] for k in keys])
    model["version"]=canonical_digest({k:v for k,v in model.items() if k!="version"})
    counts={n:{"examples":0,"positives":0} for n in ("archive","retained_observed","recent_observed")}
    for k in keys:
        counts[origin[k]]["examples"]+=1
        counts[origin[k]]["positives"]+=int(labels[k]["hit"])
    report={"schema":"market_wide_cumulative_shadow_v1","model":model,
            "archive_cohort_sha256":source_receipts[0]["cohort_sha256"],
            "archive_cohort_receipts":source_receipts,"retained_observed_cohort_receipts":observed_receipts,"state_digest":state["digest"],
            "source_counts":counts,"training_data_cutoff_utc":cutoff.isoformat(),
            "historical_trade_research":{"complete_window_receipts":trade_receipts,
                "feature_complete_mature_48h_examples":trade_examples,"positive_examples":trade_positives,
                "included_in_strict_fit":False,"reason":("OUTCOME_ENRICHED_SAMPLING_NOT_YET_QUALIFIED" if historical_trade_directory is not None else "HISTORICAL_TRADE_EVIDENCE_NOT_AVAILABLE")},
            "state_asof_utc":observed_asof.isoformat(),"purge_hours":48,
            "comparison_status":"FUTURE_HOLDOUT_NOT_YET_MATURE",
            "source_authenticated":False,"production_applied":False,
            "promotion_authorized":False,"measured_lift_verified":False}
    report["digest"]=canonical_digest(report)
    return report



def choose_fitted_candidate(current, previous=None):
    """Identical strict training examples must not fragment prospective metrics.

    Only reuse a validated, shadow-only model with the same data fingerprint,
    features and fitted values. A real data or algorithm change freezes a new
    candidate. The original report is retained unchanged as model provenance.
    """
    def validate(report):
        if (report.get("schema")!="market_wide_cumulative_shadow_v1"
            or report.get("digest")!=canonical_digest({k:v for k,v in report.items() if k!="digest"})
            or report.get("production_applied") is not False
            or report.get("promotion_authorized") is not False):
            raise ValueError("Invalid cumulative candidate report")
        model=report["model"]
        if (model.get("status")!="SHADOW_ONLY" or
            model.get("version")!=canonical_digest({k:v for k,v in model.items() if k!="version"})):
            raise ValueError("Invalid frozen candidate model")
        return model
    new=validate(current)
    if previous is None:
        return current,False
    old=validate(previous)
    fields=("training_dataset_digest","feature_names","feature_weights",
            "feature_centers","feature_scales","training_count","positive_count","negative_count")
    if (old.get("training_dataset_digest") and all(old.get(k)==new.get(k) for k in fields)
        and utc_time(old["training_end_utc"])<=utc_time(new["training_end_utc"])):
        return previous,True
    return current,False



def build_learning_receipt(observed, training, candidate, *, writer, learning_scope):
    """Compact read-only delivery evidence; never modify the production result."""
    if learning_scope not in ("pr","main"):
        raise ValueError("Invalid learning scope")
    if observed.get("evidence_digest")!=canonical_digest({k:v for k,v in observed.items() if k!="evidence_digest"}):
        raise ValueError("Observed report checksum mismatch")
    state=observed["continuity_state"]
    if state.get("digest")!=canonical_digest({k:v for k,v in state.items() if k!="digest"}):
        raise ValueError("Continuity state checksum mismatch")
    chosen,_=choose_fitted_candidate(training,candidate)
    if chosen!=candidate:
        raise ValueError("Candidate fit does not match current training data")
    if training["state_digest"]!=state["digest"] or observed["ledger_generation"]!=writer["ledger_generation"]:
        raise ValueError("Learning state/writer provenance mismatch")
    if state["ledger_generation"]!=writer["ledger_generation"] or observed["evaluation_asof_utc"]!=state["evaluation_asof_utc"]:
        raise ValueError("Learning state generation/asof mismatch")
    shadow=observed["prospective_shadow"]
    snapshot=shadow.get("prospective_snapshot") or {}
    model=training["model"]
    eligible=set(observed["eligible_pairs"])
    receipt={"schema":"market_wide_learning_receipt_v1","learning_scope":learning_scope,
        "writer_run_id":str(writer["run_id"]),"source_sha":writer["source_sha"],
        "ledger_generation":writer["ledger_generation"],"ledger_sha256":writer["ledger_sha256"],
        "evaluation_asof_utc":observed["evaluation_asof_utc"],"state_digest":state["digest"],
        "active_model_version":snapshot.get("model_version"),"candidate_model_version":candidate["model"]["version"],
        "training_count":model["training_count"],"positive_count":model["positive_count"],
        "negative_count":model["negative_count"],"source_counts":training["source_counts"],
        "training_dataset_digest":model["training_dataset_digest"],
        "eligible_markets":len(eligible),"cumulative_observed_current_markets":len(eligible&set(state["last_success_generation"])),
        "retained_anchors":len(state["anchors"])+sum(r["counts"]["anchors"] for r in state.get("cold_segments",[])),
        "active_anchors":len(state["anchors"]),"cold_segment_count":len(state.get("cold_segments",[])),
        "timely_shadow_predictions":shadow["timely_recorded_predictions"],
        "per_horizon_current_shard":observed["per_horizon"],
        "crossing_summary_current_shard":observed.get("crossing_summary"),
        "prospective_by_version_and_horizon":shadow["by_model_and_horizon"],
        "historical_trade_research":training.get("historical_trade_research",{}),
        "coverage_scope":observed["coverage_scope"],"fetch_errors":observed["fetch_errors"],
        "source_authenticated":False,"production_applied":False,"promotion_authorized":False,
        "measured_lift_verified":False}
    receipt["digest"]=canonical_digest(receipt)
    return receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description="Prediction-independent read-only Kraken outcome smoke")
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=12)
    parser.add_argument("--include-watch-controls",action="store_true")
    parser.add_argument("--prior-state", type=Path)
    parser.add_argument("--state-output", type=Path)
    parser.add_argument("--shadow-model", type=Path)
    parser.add_argument("--shadow-model-available")
    parser.add_argument("--train-cohorts", action="store_true")
    parser.add_argument("--observed-positive-sensitivity", action="store_true")
    parser.add_argument("--cumulative-state", type=Path)
    parser.add_argument("--cumulative-archive-sha256")
    parser.add_argument("--additional-archive",action="append",nargs=2,metavar=("COHORT_PATH","SHA256"),default=[])
    parser.add_argument("--retained-observed",action="append",nargs=2,metavar=("COHORT_PATH","SNAPSHOT_SET_SHA256"),default=[])
    parser.add_argument("--historical-trade-directory",type=Path)
    parser.add_argument("--compact-seed",type=Path)
    parser.add_argument("--cold-state-directory",type=Path)
    parser.add_argument("--prior-cold-directory",type=Path)
    parser.add_argument("--original-cohort-hash",action="append")
    parser.add_argument("--training-end")
    parser.add_argument("--holdout-start")
    parser.add_argument("--evaluation-asof")
    parser.add_argument("--archive-sha256")
    parser.add_argument("--archive-start")
    parser.add_argument("--archive-end")
    parser.add_argument("--archive-cohort-output", type=Path)
    args = parser.parse_args(argv)
    if args.cumulative_state:
        if not args.cumulative_archive_sha256:
            parser.error("Cumulative training requires pinned archive digest")
        report=train_cumulative_market_model(args.ledger,json.loads(args.cumulative_state.read_text()),
                                             expected_archive_sha256=args.cumulative_archive_sha256,
                                             additional_archives=args.additional_archive,retained_observed=args.retained_observed,historical_trade_directory=args.historical_trade_directory,compact_seed=args.compact_seed,
                                             original_cohort_hashes=args.original_cohort_hash,cold_state_directory=args.cold_state_directory)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,sort_keys=True)+"\n")
        print(json.dumps(report,sort_keys=True))
        return report
    if args.train_cohorts:
        if not (args.training_end and args.holdout_start and args.evaluation_asof):
            parser.error("Training requires chronological split and evaluation date")
        report = train_archive_shadow(args.ledger, training_end_utc=args.training_end,
                                      holdout_start_utc=args.holdout_start, evaluation_asof_utc=args.evaluation_asof,
                                      allow_observed_positive=args.observed_positive_sensitivity)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, sort_keys=True) + "\n")
        print(json.dumps(report, sort_keys=True))
        return report
    if args.archive_sha256:
        if not (args.archive_start and args.archive_end and args.archive_cohort_output):
            parser.error("Archive mode requires start, end and cohort output")
        report = run_archive_market_cohorts(args.ledger, expected_sha256=args.archive_sha256,
                                           start_utc=args.archive_start, end_utc=args.archive_end,
                                           cohort_output=args.archive_cohort_output)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, sort_keys=True) + "\n")
        print(json.dumps(report, sort_keys=True))
        return report
    prior = json.loads(args.prior_state.read_text()) if args.prior_state else None
    if args.shadow_model and not args.shadow_model_available:
        parser.error("Shadow model availability timestamp required")
    model_source = json.loads(args.shadow_model.read_text()) if args.shadow_model else None
    report = run_observed_market_batch(json.loads(args.ledger.read_text()), batch_size=args.batch_size, prior=prior,
                                       model_source=model_source, model_available_utc=args.shadow_model_available,
                                       include_watch_controls=args.include_watch_controls)
    if args.cold_state_directory is not None:
        from .learning_retention import compact_live_state,assemble_history
        active=compact_live_state(report["continuity_state"],args.cold_state_directory,
                                  previous_directory=args.prior_cold_directory)
        report["continuity_state"]=active
        history=assemble_history(active,args.cold_state_directory)
        shadow=report["prospective_shadow"]
        shadow["retained_predictions"]=len(history["shadow_predictions"])
        shadow["timely_recorded_predictions"]=sum(p.get("recording_scope")=="TIMELY_RECORDED_QUOTE_REFERENCE" for p in history["shadow_predictions"])
        shadow["replay_only_predictions"]=shadow["retained_predictions"]-shadow["timely_recorded_predictions"]
        shadow["by_model_and_horizon"]=prospective_metrics_by_version(history["shadow_predictions"],history["shadow_outcomes"])
        # Sum actual matched 48h batches by model without presenting pooled lift.
        for target,source in (("paired_complete_batches","paired_complete_batches"),("selected_per_scanner","selected_per_scanner"),("baseline_hits","baseline_hits"),("shadow_hits","shadow_hits")):
            shadow[target]=sum(m["48"][source] for m in shadow["by_model_and_horizon"].values())
        report["evidence_digest"]=canonical_digest({k:v for k,v in report.items() if k!="evidence_digest"})
    elif report["continuity_state"].get("cold_segments"):
        raise ValueError("Missing cold history output; refusing loss")
    if args.state_output:
        args.state_output.parent.mkdir(parents=True, exist_ok=True)
        args.state_output.write_text(json.dumps(report["continuity_state"], sort_keys=True, separators=(",", ":")) + "\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n")
    summary = {k: report[k] for k in ("ledger_generation", "shard_index", "shard_count",
               "per_horizon", "feature_complete_anchors", "eligibility_abstentions",
               "fetch_errors", "coverage_scope", "source_authenticated", "crossing_summary")}
    summary.update(eligible_count=len(report["eligible_pairs"]), selected_count=len(report["selected_pairs"]),
                   observed_count=len(report["observed_pairs"]),
                   cumulative_anchors=len(report["continuity_state"]["anchors"])+sum(r["counts"]["anchors"] for r in report["continuity_state"].get("cold_segments",[])),
                   cumulative_observed_markets=len(report["continuity_state"]["last_success_generation"]),
                   independent_selected_count=len(report["independent_selected_pairs"]),
                   watch_control_count=len(report["watch_control_pairs"]),
                   outcome_followup_count=len(report["outcome_followup_pairs"]))
    shadow = report["prospective_shadow"]
    snapshot = shadow["prospective_snapshot"]
    summary["prospective_shadow"] = {k:v for k,v in shadow.items() if k!="prospective_snapshot"}
    if snapshot is not None:
        summary["prospective_shadow"].update(scored=len(snapshot["predictions"]),
            baseline_budget=snapshot["baseline_budget"],model_version=snapshot["model_version"],
            excluded_count=len(snapshot["excluded"]))
    print(json.dumps(summary, sort_keys=True))
    return report


if __name__ == "__main__":
    main()
