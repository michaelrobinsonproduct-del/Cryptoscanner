"""Build prediction-independent learning anchors from completed five-minute candles.

Input candles use close timestamps, not Kraken interval-open timestamps.
Caller must authenticate source and supply the point-in-time eligible universe.
No production decisions or ledger writes.
"""
from bisect import bisect_right
from datetime import timedelta
import argparse
import json
from pathlib import Path
from math import isfinite
from .shadow_learning_evidence import utc_time, canonical_digest
from .heldout_outcome_adapter import reconstruct_forward_outcomes
from .frozen_historical_shadow import features_at_entry

def build_market_cohort(candles, *, eligible_pairs, evaluation_asof_utc,
                        eligibility_observations=None):
    asof = utc_time(evaluation_asof_utc)
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
            "feature_complete_anchors": sum(a["feature_complete"] for a in anchors),
            "eligibility_abstentions": eligibility_abstentions,
            "eligibility_scope": "RECORDED_ASOF_OBSERVATIONS" if eligibility_observations is not None else "CALLER_SUPPLIED_UNIVERSE",
            "missing_eligible_pairs": sorted(eligible - set(grouped)),
            "eligible_pairs": sorted(eligible), "observed_pairs": sorted(grouped),
            "source_authenticated": False, "production_applied": False,
            "promotion_authorized": False}


def select_market_batch(ledger, *, batch_size=12):
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
    return pairs, pairs[shard*batch_size:(shard+1)*batch_size], shard, shard_count


def run_observed_market_batch(ledger, *, fetch=None, batch_size=12):
    """Read-only real Kraken smoke; never describes a shard as full coverage."""
    from .kraken_observed_candles import fetch_kraken_ohlc
    fetch = fetch or fetch_kraken_ohlc
    pairs, selected, shard, shard_count = select_market_batch(ledger, batch_size=batch_size)
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
    cohort = build_market_cohort(
        [c for item in results for c in item["candles"]],
        eligible_pairs=pairs, evaluation_asof_utc=latest["as_of"],
        eligibility_observations=ledger["observations"])
    digests = {item["pair"]: item["response_sha256"] for item in results}
    for row in cohort["anchors"] + cohort["outcomes"]:
        row["source_sha256"] = digests[row["pair"]]
    cohort.update(schema="market_wide_observed_learning_v1",
                  ledger_generation=ledger["generation"], ledger_run_id=latest["id"],
                  evaluation_asof_utc=latest["as_of"], selected_pairs=selected,
                  shard_index=shard, shard_count=shard_count, fetch_errors=errors,
                  source_digests=digests, coverage_scope="PARTIAL_ROTATING_SHARD",
                  measured_lift_verified=False)
    cohort["evidence_digest"] = canonical_digest(cohort)
    return cohort


def main(argv=None):
    parser = argparse.ArgumentParser(description="Prediction-independent read-only Kraken outcome smoke")
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=12)
    args = parser.parse_args(argv)
    report = run_observed_market_batch(json.loads(args.ledger.read_text()), batch_size=args.batch_size)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n")
    summary = {k: report[k] for k in ("ledger_generation", "shard_index", "shard_count",
               "per_horizon", "feature_complete_anchors", "eligibility_abstentions",
               "fetch_errors", "coverage_scope", "source_authenticated")}
    summary.update(eligible_count=len(report["eligible_pairs"]), selected_count=len(report["selected_pairs"]),
                   observed_count=len(report["observed_pairs"]))
    print(json.dumps(summary, sort_keys=True))
    return report


if __name__ == "__main__":
    main()
