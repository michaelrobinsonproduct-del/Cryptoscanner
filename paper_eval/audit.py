"""Independent paper-only evaluation of sampled forward outcomes.

This deliberately DOES NOT claim independent price completeness, a backtest,
a validated +30% strategy, or held-out uplift.  It evaluates only observations
that were already recorded as-of in the immutable paper ledger.
"""
import datetime as dt
import hashlib
import math
from collections import defaultdict

from paper_pov import ledger
from paper_pov.scanner import utc

HORIZONS = frozenset(ledger.HORIZONS)
MAX_DELAY = ledger.MAX_DELAY
TOLERANCE_PCT = 0.001


def _finite(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Invalid " + label)
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("Nonfinite " + label)
    return number


def _timeline(pair, start, target, by_pair):
    """Independent reconstruction using ONLY previously recorded quote samples."""
    series = sorted(
        (o for o in by_pair.get(pair, ()) if start < utc(o["at"]) <= target + MAX_DELAY),
        key=lambda o: utc(o["at"]))
    in_window = [o for o in series if utc(o["at"]) <= target]
    anchors = [o for o in series if target <= utc(o["at"]) <= target + MAX_DELAY]
    timeline = [start] + [utc(o["at"]) for o in in_window]
    contiguous = bool(anchors) and bool(in_window) and all(
        dt.timedelta(0) < b - a <= MAX_DELAY for a, b in zip(timeline, timeline[1:]))
    if not contiguous or not dt.timedelta(0) <= utc(anchors[0]["at"]) - timeline[-1] <= MAX_DELAY:
        return None
    return in_window, anchors[0]


def _validate(state):
    ledger.verify(state)
    runs = state["runs"]
    run_map = {}
    for run in runs:
        rid = run["id"]
        if not isinstance(rid, str) or len(rid) != 64 or rid in run_map:
            raise ValueError("Invalid or duplicate run identity")
        if not isinstance(run.get("source_sha"), str) or len(run["source_sha"]) != 40:
            raise ValueError("Missing immutable source revision")
        utc(run["as_of"])
        run_map[rid] = run
    latest = utc(runs[-1]["as_of"]) if runs else None

    predictions = defaultdict(list)
    pred_map = {}
    for p in state["predictions"]:
        run = run_map.get(p["run_id"])
        if run is None or p["as_of"] != run["as_of"]:
            raise ValueError("Orphan or altered prediction run/as-of")
        pair = p["pair"]
        if not isinstance(pair, str) or not pair or len(pair) > 64:
            raise ValueError("Invalid prediction pair")
        expected = hashlib.sha256(("paper-v1|" + p["as_of"] + "|" + pair).encode()).hexdigest()
        if p["prediction_id"] != expected:
            raise ValueError("Prediction identity does not match as-of/pair")
        if any(x["pair"] == pair for x in predictions[p["run_id"]]):
            raise ValueError("Duplicate prediction market in run")
        if _finite(p["price"], "prediction price") <= 0:
            raise ValueError("Nonpositive prediction price")
        _finite(p["baseline_score"], "baseline score")
        _finite(p["challenger_score"], "challenger score")
        if not isinstance(p.get("rank"), int) or isinstance(p["rank"], bool) or p["rank"] < 1:
            raise ValueError("Invalid prediction rank")
        predictions[p["run_id"]].append(p)
        pred_map[p["prediction_id"]] = p

    observations = defaultdict(list)
    obs_per_run = defaultdict(list)
    for o in state["observations"]:
        run = run_map.get(o["run_id"])
        if run is None:
            raise ValueError("Orphan observation")
        at = utc(o["at"])
        if not utc(run["as_of"]) - dt.timedelta(seconds=180) <= at <= utc(run["as_of"]):
            raise ValueError("Observation is not contemporaneous with run")
        if _finite(o["price"], "observation price") <= 0:
            raise ValueError("Nonpositive observation price")
        if not isinstance(o["pair"], str) or not o["pair"]:
            raise ValueError("Invalid observation market")
        if any(x["pair"] == o["pair"] for x in obs_per_run[o["run_id"]]):
            raise ValueError("Duplicate observation market in run")
        observations[o["pair"]].append(o)
        obs_per_run[o["run_id"]].append(o)
    for rid, run in run_map.items():
        if run.get("watch_count") != len(predictions[rid]):
            raise ValueError("Prediction count mismatch")
        if run.get("observation_count") != len(obs_per_run[rid]):
            raise ValueError("Observation count mismatch")
        ranks = [p["rank"] for p in predictions[rid]]
        if sorted(ranks) != list(range(1, len(ranks) + 1)):
            raise ValueError("Noncontiguous prediction ranks")

    outcomes = {}
    for o in state["outcomes"]:
        p = pred_map.get(o["prediction_id"])
        hours = o["horizon_hours"]
        if p is None or type(hours) is not int or hours not in HORIZONS:
            raise ValueError("Orphan or invalid outcome horizon")
        key = (o["prediction_id"], hours)
        if key in outcomes:
            raise ValueError("Duplicate outcome")
        target = utc(p["as_of"]) + dt.timedelta(hours=hours)
        if utc(o["target_at"]) != target or latest is None or latest < target + MAX_DELAY:
            raise ValueError("Outcome target or maturity mismatch")
        reconstructed = _timeline(p["pair"], utc(p["as_of"]), target, observations)
        if o["status"] == "ABSTAIN_GAP":
            if reconstructed is not None:
                raise ValueError("Gap abstention contradicts contiguous recorded quotes")
            if any(k in o for k in ("observed_30pct_hit", "return_pct", "observed_peak_pct")):
                raise ValueError("Gap abstention carries fabricated outcome")
        elif o["status"] == "MATURED_OBSERVED":
            if reconstructed is None:
                raise ValueError("Matured outcome lacks contiguous recorded quotes")
            window, anchor = reconstructed
            if utc(o["observed_at"]) != utc(anchor["at"]):
                raise ValueError("Matured anchor timestamp mismatch")
            actual_return = 100 * (anchor["price"] / p["price"] - 1)
            actual_peak = 100 * (max(x["price"] for x in window) / p["price"] - 1)
            if abs(_finite(o["return_pct"], "return") - actual_return) > TOLERANCE_PCT:
                raise ValueError("Matured return disagrees with recorded prices")
            if abs(_finite(o["observed_peak_pct"], "peak") - actual_peak) > TOLERANCE_PCT:
                raise ValueError("Matured peak disagrees with recorded prices")
            if type(o.get("observed_30pct_hit")) is not bool or o["observed_30pct_hit"] != (actual_peak >= 30):
                raise ValueError("Matured hit label disagrees with recorded prices")
        else:
            raise ValueError("Unknown outcome status")
        outcomes[key] = o
    return runs, predictions, obs_per_run, observations, outcomes, latest


def evaluate(state, horizon_hours=24, top_k=5):
    """Return audited sampled-only scoreboard; never report validated held-out lift.

    Baseline and challenger rank exactly the SAME already-watched universe.
    Exclude runs with any missing/abstained watch labels, not just losing picks.
    Observed misses cover only continuously sampled non-watch markets.
    """
    if type(horizon_hours) is not int or horizon_hours not in HORIZONS:
        raise ValueError("Unsupported horizon")
    if type(top_k) is not int or not 1 <= top_k <= 12:
        raise ValueError("Invalid top_k")
    runs, preds, starts, by_pair, outcomes, latest = _validate(state)
    mature_runs = 0
    eligible_runs = 0
    excluded_gap = 0
    excluded_immature = 0
    baseline_hits = challenger_hits = 0
    baseline_return = challenger_return = 0.0
    observed_missed = 0
    covered_nonwatch = 0
    gap_nonwatch = 0
    for run in runs:
        ps = preds[run["id"]]
        if len(ps) < top_k:
            continue
        start = utc(run["as_of"])
        target = start + dt.timedelta(hours=horizon_hours)
        if latest is None or latest < target + MAX_DELAY:
            excluded_immature += 1
            continue
        mature_runs += 1
        labels = [outcomes.get((p["prediction_id"], horizon_hours)) for p in ps]
        if any(o is None or o["status"] != "MATURED_OBSERVED" for o in labels):
            excluded_gap += 1
            continue
        eligible_runs += 1
        by_id = {o["prediction_id"]: o for o in labels}
        baseline = sorted(ps, key=lambda p: (-p["baseline_score"], p["pair"]))[:top_k]
        challenger = sorted(ps, key=lambda p: (-p["challenger_score"], p["pair"]))[:top_k]
        for p in baseline:
            o = by_id[p["prediction_id"]]
            baseline_hits += int(o["observed_30pct_hit"])
            baseline_return += o["return_pct"]
        for p in challenger:
            o = by_id[p["prediction_id"]]
            challenger_hits += int(o["observed_30pct_hit"])
            challenger_return += o["return_pct"]
        watched = {p["pair"] for p in ps}
        for obs in starts[run["id"]]:
            if obs["pair"] in watched:
                continue
            timeline = _timeline(obs["pair"], start, target, by_pair)
            if timeline is None:
                gap_nonwatch += 1
                continue
            covered_nonwatch += 1
            in_window, _ = timeline
            if max(x["price"] for x in in_window) >= 1.3 * obs["price"]:
                observed_missed += 1
    count = eligible_runs * top_k
    return {
        "schema": 1, "horizon_hours": horizon_hours, "top_k": top_k,
        "ledger_generation": state["generation"], "ledger_sha256": state["sha256"],
        "actual_scans": len(runs), "mature_enough_runs": mature_runs,
        "comparable_runs": eligible_runs, "excluded_incomplete_or_gap": excluded_gap,
        "excluded_immature": excluded_immature, "comparison_samples_per_arm": count,
        "baseline_observed_hits": baseline_hits,
        "challenger_observed_hits": challenger_hits,
        "baseline_observed_hit_rate": round(baseline_hits / count, 6) if count else None,
        "challenger_observed_hit_rate": round(challenger_hits / count, 6) if count else None,
        "baseline_mean_sampled_return_pct": round(baseline_return / count, 4) if count else None,
        "challenger_mean_sampled_return_pct": round(challenger_return / count, 4) if count else None,
        "observed_nonwatch_30pct_movers": observed_missed,
        "continuously_sampled_nonwatch_pairs": covered_nonwatch,
        "nonwatch_gap_abstentions": gap_nonwatch,
        "independent_held_out_lift": None, "production_applied": False,
        "limitations": "Same selected watch pool; client-observed snapshots, not complete price highs. Observed hits/misses are sampled lower bounds, not all-market recall or independent held-out uplift."
    }
