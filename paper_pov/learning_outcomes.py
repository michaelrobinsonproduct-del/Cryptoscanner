"""Read-only point-in-time research on a sealed PAPER ledger.

Client-observed sampled quotes are NOT exchange-complete highs, tradeable
fills, independent samples, calibrated probabilities or held-out lift.
No scanner writer, production promotion, trading, or external IO.
"""
from bisect import bisect_right
from collections import defaultdict
import datetime as dt
import math

from paper_pov import ledger
from paper_pov.scanner import utc
from paper_pov.segmented_storage import MAX_RAW_BYTES

HORIZONS = (1, 6, 24, 48)
MAX_GAP = dt.timedelta(minutes=45)
UTC = dt.timezone.utc


def _aware(value):
    if isinstance(value, str):
        return utc(value)
    if not isinstance(value, dt.datetime) or value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("Evaluation time must be timezone-aware")
    return value.astimezone(UTC)


def _index(state, evaluation_at):
    ledger.verify(state, MAX_RAW_BYTES)
    if not state["runs"]:
        raise ValueError("Cannot evaluate empty ledger")
    if evaluation_at < utc(state["runs"][0]["as_of"]):
        raise ValueError("Evaluation precedes ledger")
    runs = {r["id"]: r for r in state["runs"]}
    watch = {(p["run_id"], p["pair"]): p for p in state["predictions"]}
    by_pair = defaultdict(list)
    same_run = {}
    for obs in state["observations"]:
        at = utc(obs["at"])
        if at <= evaluation_at:
            by_pair[obs["pair"]].append((at, float(obs["price"])))
        same_run[(obs["run_id"], obs["pair"])] = obs
    for pair in by_pair:
        by_pair[pair].sort()
    return runs, watch, by_pair, same_run


def sampled_outcomes(state, evaluation_at, horizons=HORIZONS):
    """All observed markets, not only WATCH. Require target+45m maturity.

    Peak excludes post-target prices. Missing continuous <=45m observations
    or target anchor abstains. No future observation may enter evaluation.
    """
    now = _aware(evaluation_at)
    if not isinstance(horizons, (tuple, list)) or not horizons or any(
            type(h) is not int or h not in HORIZONS for h in horizons) or len(set(horizons)) != len(horizons):
        raise ValueError("Unsupported or duplicate horizons")
    runs, watch, by_pair, same_run = _index(state, now)
    rows = []
    for (run_id, pair), entry in sorted(same_run.items(),
                                        key=lambda kv: (utc(runs[kv[0][0]]["as_of"]), kv[0][1])):
        run = runs[run_id]
        start = utc(run["as_of"])
        if start > now:
            continue
        observed_at = utc(entry["at"])
        if observed_at > start or start - observed_at > dt.timedelta(seconds=180):
            raise ValueError("Untrusted same-run quote time")
        price = float(entry["price"])
        if not math.isfinite(price) or price <= 0:
            raise ValueError("Untrusted entry price")
        pred = watch.get((run_id, pair))
        timeline = by_pair.get(pair, [])
        for h in horizons:
            target = start + dt.timedelta(hours=h)
            base = {"run_id": run_id, "pair": pair, "as_of": run["as_of"],
                    "horizon_hours": h, "target_at": target.isoformat(),
                    "watch": pred is not None,
                    "baseline_score": pred["baseline_score"] if pred else None,
                    "challenger_score": pred["challenger_score"] if pred else None,
                    "entry_price": price}
            if now < target + MAX_GAP:
                rows.append({**base, "status": "IMMATURE"})
                continue
            lo = bisect_right(timeline, (start, float("inf")))
            hi = bisect_right(timeline, (target + MAX_GAP, float("inf")))
            candidates = timeline[lo:hi]
            within = [(t, p) for t, p in candidates if t <= target]
            anchors = [(t, p) for t, p in candidates if t >= target]
            stamps = [start] + [t for t, _ in within]
            contiguous = bool(within and anchors) and all(
                b - a <= MAX_GAP for a, b in zip(stamps, stamps[1:]))
            if contiguous:
                contiguous = anchors[0][0] - stamps[-1] <= MAX_GAP
            if not contiguous:
                rows.append({**base, "status": "ABSTAIN_GAP"})
                continue
            peak = 100 * (max(p for _, p in within) / price - 1)
            final = 100 * (anchors[0][1] / price - 1)
            rows.append({**base, "status": "MATURED_OBSERVED",
                         "anchor_at": anchors[0][0].isoformat(),
                         "observed_peak_pct": round(peak, 6),
                         "observed_terminal_pct": round(final, 6),
                         "observed_20pct_hit": peak >= 20,
                         "observed_30pct_hit": peak >= 30})
    return rows


def coverage_summary(rows):
    """Overlapping market/run windows are correlated, not independent labels."""
    if not isinstance(rows, list):
        raise ValueError("Rows must be a list")
    output = {}
    for h in HORIZONS:
        sample = [r for r in rows if r["horizon_hours"] == h]
        mature = [r for r in sample if r["status"] == "MATURED_OBSERVED"]
        output[str(h)] = {
            "market_run_windows": len(sample),
            "matured_observed": len(mature),
            "gap_abstentions": sum(r["status"] == "ABSTAIN_GAP" for r in sample),
            "immature": sum(r["status"] == "IMMATURE" for r in sample),
            "sampled_20pct_windows": sum(r["observed_20pct_hit"] for r in mature),
            "sampled_30pct_windows": sum(r["observed_30pct_hit"] for r in mature),
            "watch_20pct_hits": sum(r["watch"] and r["observed_20pct_hit"] for r in mature),
            "watch_30pct_hits": sum(r["watch"] and r["observed_30pct_hit"] for r in mature),
            "nonwatch_missed_20pct": sum(not r["watch"] and r["observed_20pct_hit"] for r in mature),
            "nonwatch_missed_30pct": sum(not r["watch"] and r["observed_30pct_hit"] for r in mature)}
    return {"scope": "SAMPLED_CLIENT_OBSERVED_QUOTES_NOT_EXCHANGE_COMPLETE",
            "correlated_overlapping_windows": True,
            "held_out_lift": None, "production_applied": False,
            "by_horizon": output}


def shadow_rank_diagnostic(rows, cutoff, horizon_hours=1, top_k=3,
                           embargo_hours=48, min_test_runs=8):
    """Frozen cutoff, identical WATCH cohorts, 48h embargo and test spacing.

    No training, parameter tuning, scoring promotion or claimed held-out lift.
    """
    boundary = _aware(cutoff)
    if (type(horizon_hours) is not int or horizon_hours not in HORIZONS
            or type(top_k) is not int or top_k < 1
            or type(embargo_hours) is not int or embargo_hours < 48
            or type(min_test_runs) is not int or min_test_runs < 2):
        raise ValueError("Invalid chronological shadow evaluation parameters")
    by_run = defaultdict(list)
    for row in rows:
        if row["horizon_hours"] == horizon_hours and row["watch"]:
            by_run[(row["as_of"], row["run_id"])].append(row)
    eligible = []
    for (at, run_id), candidates in sorted(by_run.items(), key=lambda x: (_aware(x[0][0]), x[0][1])):
        moment = _aware(at)
        if moment < boundary + dt.timedelta(hours=embargo_hours):
            continue
        if not candidates or any(r["status"] != "MATURED_OBSERVED" for r in candidates):
            continue
        if any(not isinstance(r[k], (int, float)) or not math.isfinite(r[k])
               for r in candidates for k in ("baseline_score", "challenger_score")):
            raise ValueError("Invalid as-of scores")
        eligible.append((moment, run_id, candidates))
    independent = []
    for moment, run_id, candidates in eligible:
        if not independent or moment - independent[-1][0] >= dt.timedelta(hours=48):
            independent.append((moment, run_id, candidates))
    result = {"mode": "OFFLINE_SHADOW_ONLY", "held_out_lift": None,
              "production_applied": False, "cutoff_utc": boundary.isoformat(),
              "embargo_hours": embargo_hours, "horizon_hours": horizon_hours,
              "top_k": top_k, "eligible_test_runs": len(eligible),
              "nonoverlapping_test_runs": len(independent),
              "sampled_quote_only": True, "threshold_pct": 30,
              "status": "INSUFFICIENT_INDEPENDENT_TEST_RUNS"}
    if len(independent) < min_test_runs:
        return result
    counts = {"baseline": 0, "challenger": 0}
    total = 0
    for _, _, candidates in independent:
        n = min(top_k, len(candidates))
        total += n
        for key in counts:
            selected = sorted(candidates, key=lambda r: (-r[key + "_score"], r["pair"]))[:n]
            counts[key] += sum(r["observed_30pct_hit"] for r in selected)
    result.update({"status": "EXPLORATORY_SHADOW_DIAGNOSTIC_NOT_VALIDATED_LIFT",
                   "evaluated_positions": total,
                   "baseline_sampled_hits": counts["baseline"],
                   "challenger_sampled_hits": counts["challenger"],
                   "baseline_sampled_precision": counts["baseline"] / total,
                   "challenger_sampled_precision": counts["challenger"] / total})
    return result
