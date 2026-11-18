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
    for pair in cohort["selected_pairs"]:
        attempts[pair] = generation
    for pair in cohort["observed_pairs"]:
        successes[pair] = generation
    result = {"schema": STATE_SCHEMA, "ledger_generation": generation,
              "evaluation_asof_utc": cohort["evaluation_asof_utc"],
              "previous_digest": prior.get("digest"),
              "eligibility": eligibility,
              "anchors": [anchors[k] for k in sorted(anchors)],
              "outcomes": [outcomes[k] for k in sorted(outcomes)],
              "last_attempt_generation": attempts, "last_success_generation": successes,
              "production_applied": False, "source_authenticated": False}
    result["digest"] = canonical_digest(result)
    return result


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
        attempts = prior['last_attempt_generation']
        selected = sorted(pairs, key=lambda pair: (attempts.get(pair, 0), pair))[:batch_size]
        return pairs, selected, shard, shard_count
    return pairs, pairs[shard*batch_size:(shard+1)*batch_size], shard, shard_count


def run_observed_market_batch(ledger, *, fetch=None, batch_size=12, prior=None):
    """Read-only real Kraken smoke; never describes a shard as full coverage."""
    from .kraken_observed_candles import fetch_kraken_ohlc
    fetch = fetch or fetch_kraken_ohlc
    validate_prior_market_state(prior, ledger)
    pairs, selected, shard, shard_count = select_market_batch(ledger, batch_size=batch_size, prior=prior)
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
                  shard_index=shard, shard_count=shard_count, fetch_errors=errors,
                  source_digests=digests, coverage_scope="PARTIAL_ROTATING_SHARD",
                  measured_lift_verified=False)
    cohort["continuity_state"] = merge_market_state(cohort, eligibility, prior)
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
                         evaluation_asof_utc, top_k=5):
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
                                    holdout_start_utc=holdout_start_utc, feature_names=NAMES)
    by_id = {a["prediction_id"]: a for a in predictions}
    labels = {o["prediction_id"]: o for o in outcomes
              if o["coverage_complete"] and type(o["hit"]) is bool}
    scores = model.get("shadow_scores", {})
    groups = {}
    for key in scores:
        groups.setdefault(by_id[key]["entry_utc"], []).append(key)
    metrics = {n: {"selected": 0, "hits": 0, "false_positives": 0, "early_hits": 0,
                   "lead_hours_sum": 0., "lead_count": 0} for n in ("baseline_proxy", "challenger")}
    comparable, unavailable, covered_positive_anchors = 0, 0, 0
    for stamp, keys in sorted(groups.items()):
        base = sorted(keys, key=lambda k: (-abs(by_id[k]["features"]["momentum_60m"]), k))[:top_k]
        challenger = sorted(keys, key=lambda k: (-scores[k], k))[:top_k]
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
    # Retain the actual fitted model, not the potentially large temporary
    # vector of holdout predictions. The model version is recomputed here.
    model.pop("shadow_scores", None)
    model["source_archive_sha256"] = next(iter(archive_digests))
    model["version"] = canonical_digest({k:v for k,v in model.items() if k!="version"})
    result = {"schema": "market_wide_archive_shadow_v1", "model": model,
              "evaluation_asof_utc": evaluation_asof_utc, "top_k": top_k,
              "baseline": "HISTORICAL_ABS_MOMENTUM_60M_PROXY_NOT_PRODUCTION",
              "comparison_status": "SHADOW_EVALUATED" if comparable else "NO_PAIRED_COMPLETE_TIMESTAMPS",
              "comparable_timestamps": comparable, "unavailable_timestamps": unavailable,
              "covered_positive_anchors": covered_positive_anchors, "metrics": metrics,
              "source_authenticated": False, "measured_lift_verified": False,
              "production_applied": False, "promotion_authorized": False}
    result["digest"] = canonical_digest(result)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Prediction-independent read-only Kraken outcome smoke")
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=12)
    parser.add_argument("--prior-state", type=Path)
    parser.add_argument("--state-output", type=Path)
    parser.add_argument("--train-cohorts", action="store_true")
    parser.add_argument("--training-end")
    parser.add_argument("--holdout-start")
    parser.add_argument("--evaluation-asof")
    parser.add_argument("--archive-sha256")
    parser.add_argument("--archive-start")
    parser.add_argument("--archive-end")
    parser.add_argument("--archive-cohort-output", type=Path)
    args = parser.parse_args(argv)
    if args.train_cohorts:
        if not (args.training_end and args.holdout_start and args.evaluation_asof):
            parser.error("Training requires chronological split and evaluation date")
        report = train_archive_shadow(args.ledger, training_end_utc=args.training_end,
                                      holdout_start_utc=args.holdout_start, evaluation_asof_utc=args.evaluation_asof)
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
    report = run_observed_market_batch(json.loads(args.ledger.read_text()), batch_size=args.batch_size, prior=prior)
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
                   cumulative_anchors=len(report["continuity_state"]["anchors"]),
                   cumulative_observed_markets=len(report["continuity_state"]["last_success_generation"]))
    print(json.dumps(summary, sort_keys=True))
    return report


if __name__ == "__main__":
    main()
