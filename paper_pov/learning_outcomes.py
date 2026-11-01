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
GAP_REASONS = (
    "NO_POST_ENTRY_QUOTE_BEFORE_TARGET",
    "NO_TARGET_ANCHOR_WITHIN_45M",
    "INTERIOR_GAP_OVER_45M",
    "TARGET_BRIDGE_OVER_45M",
)
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
                # Attribute abstention without imputing a price or a missing candle.
                if not within:
                    reason = GAP_REASONS[0]
                elif not anchors:
                    reason = GAP_REASONS[1]
                elif any(b - a > MAX_GAP for a, b in zip(stamps, stamps[1:])):
                    reason = GAP_REASONS[2]
                else:
                    reason = GAP_REASONS[3]
                rows.append({**base, "status": "ABSTAIN_GAP",
                             "gap_reason": reason})
                continue
            # The immutable same-run entry quote is part of the observed window.
            # Excluding it misreports a falling market's peak as negative.
            peak = 100 * (max([price] + [p for _, p in within]) / price - 1)
            final = 100 * (anchors[0][1] / price - 1)
            rows.append({**base, "status": "MATURED_OBSERVED",
                         "anchor_at": anchors[0][0].isoformat(),
                         "observed_peak_pct": round(peak, 6),
                         "observed_terminal_pct": round(final, 6),
                         "observed_20pct_hit": peak >= 20,
                         "observed_30pct_hit": peak >= 30})
    return rows



def sampled_mover_episode_clusters(rows, horizon_hours, threshold_pct):
    """Group overlapping non-WATCH sampled windows; clusters are NOT independent events.

    This is a descriptive deduplication of correlated entry windows, not a
    reconstruction of exchange highs, executable opportunities or validated lift.
    No future observations are introduced: input rows must already be matured.
    """
    if (not isinstance(rows, list) or type(horizon_hours) is not int
            or horizon_hours not in HORIZONS or type(threshold_pct) is not int
            or threshold_pct not in (20, 30)):
        raise ValueError("Invalid sampled episode parameters")
    key = f"observed_{threshold_pct}pct_hit"
    by_pair = defaultdict(list)
    seen = set()
    for row in rows:
        if row.get("horizon_hours") != horizon_hours:
            continue
        if (row.get("status") != "MATURED_OBSERVED"
                or row.get("watch") is not False or row.get(key) is not True):
            continue
        pair = row.get("pair")
        run_id = row.get("run_id")
        peak = row.get("observed_peak_pct")
        if (not isinstance(pair, str) or not pair
                or not isinstance(run_id, str) or not run_id
                or not isinstance(peak, (int, float)) or isinstance(peak, bool)
                or not math.isfinite(peak) or peak < threshold_pct):
            raise ValueError("Invalid sampled episode observation")
        start = _aware(row["as_of"])
        end = _aware(row["target_at"])
        if end - start != dt.timedelta(hours=horizon_hours):
            raise ValueError("Invalid sampled episode target")
        identity = (pair, run_id)
        if identity in seen:
            raise ValueError("Duplicate sampled episode entry")
        seen.add(identity)
        by_pair[pair].append((start, end, peak))
    clusters = []
    for pair in sorted(by_pair):
        current = None
        for start, end, peak in sorted(by_pair[pair]):
            if current is None or start > current["end"]:
                if current is not None:
                    clusters.append(current)
                current = {"pair": pair, "start": start, "last_entry": start,
                           "end": end, "windows": 1, "max_peak": peak}
            else:
                current["last_entry"] = start
                current["end"] = max(current["end"], end)
                current["windows"] += 1
                current["max_peak"] = max(current["max_peak"], peak)
        if current is not None:
            clusters.append(current)
    clusters.sort(key=lambda c: (-c["max_peak"], c["pair"], c["start"]))
    examples = [{
        "pair": c["pair"], "first_entry_as_of": c["start"].isoformat(),
        "last_entry_as_of": c["last_entry"].isoformat(),
        "last_target_at": c["end"].isoformat(),
        "correlated_windows": c["windows"],
        "max_sampled_peak_pct": c["max_peak"]
    } for c in clusters[:20]]
    return {"horizon_hours": horizon_hours, "threshold_pct": threshold_pct,
            "raw_correlated_windows": sum(c["windows"] for c in clusters),
            "overlap_cluster_count": len(clusters),
            "clusters_not_independent": True,
            "scope": "SAMPLED_QUOTES_OVERLAPPING_ENTRY_WINDOWS_ONLY",
            "examples": examples}


def coverage_summary(rows):
    """Overlapping market/run windows are correlated, not independent labels."""
    if not isinstance(rows, list):
        raise ValueError("Rows must be a list")
    output = {}
    for h in HORIZONS:
        sample = [r for r in rows if r["horizon_hours"] == h]
        mature = [r for r in sample if r["status"] == "MATURED_OBSERVED"]
        gaps = [r for r in sample if r["status"] == "ABSTAIN_GAP"]
        reasons = {reason: sum(r.get("gap_reason") == reason for r in gaps)
                   for reason in GAP_REASONS}
        if sum(reasons.values()) != len(gaps):
            raise ValueError("Unattributed or unrecognized sampled gap abstention")
        output[str(h)] = {
            "market_run_windows": len(sample),
            "matured_observed": len(mature),
            "gap_abstentions": len(gaps),
            "gap_reason_counts": reasons,
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



def gap_concentration_summary(rows, top_n=20):
    """Rank sampled gap abstentions by market and horizon, not by independent events.

    A concentration report helps diagnose missing 24h/48h coverage without
    filling gaps, inventing observations, or implying independent opportunities.
    The input must be point-in-time outcome rows from a sealed ledger.
    """
    if not isinstance(rows, list) or type(top_n) is not int or not 1 <= top_n <= 20:
        raise ValueError("Invalid gap concentration parameters")
    by_horizon = {h: defaultdict(lambda: {reason: 0 for reason in GAP_REASONS})
                  for h in HORIZONS}
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Invalid gap concentration row")
        h, pair, run_id = row.get("horizon_hours"), row.get("pair"), row.get("run_id")
        if (type(h) is not int or h not in HORIZONS
                or not isinstance(pair, str) or not pair
                or not isinstance(run_id, str) or not run_id):
            raise ValueError("Invalid gap concentration identity")
        key = (h, pair, run_id)
        if key in seen:
            raise ValueError("Duplicate gap concentration row")
        seen.add(key)
        status = row.get("status")
        if status == "ABSTAIN_GAP":
            reason = row.get("gap_reason")
            if reason not in GAP_REASONS:
                raise ValueError("Unattributed gap concentration row")
            by_horizon[h][pair][reason] += 1
        elif status not in ("IMMATURE", "MATURED_OBSERVED"):
            raise ValueError("Unknown gap concentration status")
        elif "gap_reason" in row:
            raise ValueError("Unexpected gap reason on non-gap row")
    result = {}
    for h in HORIZONS:
        ranked = sorted(by_horizon[h].items(),
                        key=lambda item: (-sum(item[1].values()), item[0]))
        result[str(h)] = {
            "gap_abstentions": sum(sum(counts.values()) for _, counts in ranked),
            "affected_markets": len(ranked),
            "top_markets": [
                {"pair": pair, "gap_abstentions": sum(counts.values()),
                 "gap_reason_counts": dict(counts)}
                for pair, counts in ranked[:top_n]
            ],
        }
    return {"scope": "SAMPLED_CLIENT_OBSERVED_GAP_COUNTS_ONLY",
            "correlated_overlapping_windows": True,
            "not_independent_events": True,
            "by_horizon": result}


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


def main(argv=None):
    """Reproducible local/CI artifact from an already verified sealed ledger.

    No network calls, implicit wall-clock maturity, ledger mutation, or tuning.
    Evaluation is frozen at the newest durable run's own as-of timestamp.
    """
    import argparse
    import json
    from pathlib import Path
    parser = argparse.ArgumentParser(description="Offline sampled-quote PAPER learning audit")
    parser.add_argument("--ledger", required=True, help="Already verified exported sealed ledger JSON")
    args = parser.parse_args(argv)
    state = json.loads(Path(args.ledger).read_bytes())
    if not state.get("runs"):
        raise ValueError("No durable runs")
    as_of = state["runs"][-1]["as_of"]
    rows = sampled_outcomes(state, as_of)
    misses = sorted((r for r in rows if r["horizon_hours"] == 1
                     and r["status"] == "MATURED_OBSERVED"
                     and not r["watch"] and r["observed_20pct_hit"]),
                    key=lambda r: (-r["observed_peak_pct"], r["as_of"], r["pair"]))
    result = {"schema": 1, "mode": "READ_ONLY_OFFLINE_LEARNING",
              "source_ledger_sha256": state["sha256"],
              "source_generation": state["generation"],
              "evaluation_as_of": as_of,
              "coverage": coverage_summary(rows),
              "gap_concentration": gap_concentration_summary(rows),
              "sampled_nonwatch_1h_20pct_examples": misses[:20],
              "sampled_nonwatch_overlap_clusters": {
                  str(h): {str(t): sampled_mover_episode_clusters(rows, h, t)
                           for t in (20, 30)} for h in HORIZONS},
              "shadow": shadow_rank_diagnostic(rows, state["runs"][0]["as_of"]),
              "held_out_lift": None, "production_applied": False}
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False))
    return result


if __name__ == "__main__":
    main()
