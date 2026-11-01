"""Frozen, read-only early-mover hypothesis: prior sampled momentum vs WATCH baseline.

No training, price interpolation, exchange-complete high, live writer, orders,
score promotion, or production changes. A quote 30-90 minutes old is an
as-of-only sampled feature, NOT proof of continuous price coverage.
"""
from bisect import bisect_right
from collections import defaultdict
import datetime as dt
import math

from paper_pov.learning_outcomes import sampled_outcomes, _aware

UTC = dt.timezone.utc
THRESHOLDS = (5, 20, 30)
HORIZONS = (1, 6)
MIN_MOMENTUM_UNIVERSE = 100


def trailing_sampled_return(timeline, as_of, entry_price):
    """Last quote 30-90m before as_of; never peek at current/future outcomes."""
    as_of = _aware(as_of)
    if not math.isfinite(entry_price) or entry_price <= 0:
        raise ValueError("Invalid entry price")
    upper = as_of - dt.timedelta(minutes=30)
    lower = as_of - dt.timedelta(minutes=90)
    index = bisect_right(timeline, (upper, float("inf"))) - 1
    if index < 0 or timeline[index][0] < lower:
        return None
    timestamp, prior = timeline[index]
    if timestamp > upper or not math.isfinite(prior) or prior <= 0:
        raise ValueError("Invalid prior sampled quote")
    return entry_price / prior - 1


def _top(candidates, key, k=3):
    if any(not isinstance(c["pair"], str) or not c["pair"]
           or not math.isfinite(c[key]) for c in candidates):
        raise ValueError("Invalid as-of ranking candidate")
    return sorted(candidates, key=lambda c: (-c[key], c["pair"]))[:k]


def _metrics(selected, outcomes, threshold):
    result = {"selected": len(selected), "known": 0, "unknown_gap": 0,
              "hits": 0, "false_positives": 0}
    for candidate in selected:
        row = outcomes.get(candidate["pair"])
        if row is None or row["status"] != "MATURED_OBSERVED":
            result["unknown_gap"] += 1
            continue
        result["known"] += 1
        if row["observed_peak_pct"] >= threshold:
            result["hits"] += 1
        else:
            result["false_positives"] += 1
    result["precision_known_only"] = (result["hits"] / result["known"]
                                      if result["known"] else None)
    return result


def evaluate(state, evaluation_at, horizons=HORIZONS, thresholds=THRESHOLDS):
    """Frozen 40% time cutoff + 6h embargo; spaced test windows.

    Candidate selection is exclusively as-of. Missing outcomes are UNKNOWN,
    never silently dropped or counted as losses. Recall denominator is only
    observed mature market/run windows, not all actual exchange movers.
    """
    if tuple(horizons) != HORIZONS or tuple(thresholds) != THRESHOLDS:
        raise ValueError("Frozen experiment parameters cannot be tuned")
    now = _aware(evaluation_at)
    rows = sampled_outcomes(state, now, horizons=HORIZONS)  # verifies ledger
    runs = sorted(state["runs"], key=lambda r: _aware(r["as_of"]))
    if not runs or now != _aware(runs[-1]["as_of"]):
        raise ValueError("Evaluation must be frozen at newest durable run")
    start = _aware(runs[0]["as_of"])
    cutoff = start + (now - start) * 0.4
    test_start = cutoff + dt.timedelta(hours=6)
    obs_by_pair = defaultdict(list)
    entry_by_run = defaultdict(dict)
    for obs in state["observations"]:
        stamp = _aware(obs["at"])
        if stamp > now:
            raise ValueError("Future quote in sealed evaluation")
        price = float(obs["price"])
        if not math.isfinite(price) or price <= 0:
            raise ValueError("Invalid sampled quote")
        obs_by_pair[obs["pair"]].append((stamp, price))
        if obs["pair"] in entry_by_run[obs["run_id"]]:
            raise ValueError("Duplicate same-run market observation")
        entry_by_run[obs["run_id"]][obs["pair"]] = obs
    for pair, quotes in obs_by_pair.items():
        quotes.sort()
        if len({t for t, _ in quotes}) != len(quotes):
            raise ValueError("Duplicate sampled quote timestamp")
    watch_by_run = defaultdict(list)
    for p in state["predictions"]:
        watch_by_run[p["run_id"]].append(p)
    outcomes = defaultdict(dict)
    for row in rows:
        outcomes[(row["run_id"], row["horizon_hours"])][row["pair"]] = row
    result = {
        "mode": "OFFLINE_FROZEN_SHADOW_ONLY",
        "hypothesis": "rank all as-of observed markets by 30-90m trailing sampled return",
        "control": "top-3 existing WATCH by frozen baseline score",
        "feature_is_sparse_sampled_return": True,
        "training_fraction": 0.4,
        "embargo_hours": 6,
        "cutoff_utc": cutoff.isoformat(),
        "test_start_utc": test_start.isoformat(),
        "source_generation": state["generation"],
        "source_ledger_sha256": state["sha256"],
        "held_out_lift": None,
        "production_applied": False,
        "by_horizon": {}
    }
    for h in HORIZONS:
        selected_runs = []
        for run in runs:
            at = _aware(run["as_of"])
            if at < test_start or now < at + dt.timedelta(hours=h, minutes=45):
                continue
            if selected_runs and at - selected_runs[-1][0] < dt.timedelta(hours=h):
                continue
            run_entries = entry_by_run[run["id"]]
            momentum = []
            for pair, obs in run_entries.items():
                entry = float(obs["price"])
                if _aware(obs["at"]) > at:
                    raise ValueError("Future same-run quote")
                score = trailing_sampled_return(obs_by_pair[pair], at, entry)
                if score is not None:
                    momentum.append({"pair": pair, "momentum": score})
            control = []
            for p in watch_by_run[run["id"]]:
                if p["pair"] not in run_entries:
                    raise ValueError("WATCH missing contemporaneous observation")
                score = float(p["baseline_score"])
                if not math.isfinite(score):
                    raise ValueError("Nonfinite baseline")
                control.append({"pair": p["pair"], "baseline": score})
            if len(momentum) < MIN_MOMENTUM_UNIVERSE or len(control) < 3:
                continue
            selected_runs.append((at, run, _top(control, "baseline"),
                                  _top(momentum, "momentum")))
        by_threshold = {}
        for threshold in THRESHOLDS:
            control_totals = {"selected": 0, "known": 0, "unknown_gap": 0,
                              "hits": 0, "false_positives": 0}
            challenger_totals = dict(control_totals)
            universe_hits = 0
            universe_known = 0
            for _, run, baseline, challenger in selected_runs:
                run_outcomes = outcomes[(run["id"], h)]
                universe_hits += sum(
                    r["observed_peak_pct"] >= threshold
                    for r in run_outcomes.values() if r["status"] == "MATURED_OBSERVED")
                universe_known += sum(r["status"] == "MATURED_OBSERVED"
                                      for r in run_outcomes.values())
                for totals, picks in ((control_totals, baseline),
                                      (challenger_totals, challenger)):
                    m = _metrics(picks, run_outcomes, threshold)
                    for key in totals:
                        totals[key] += m[key]
            for totals in (control_totals, challenger_totals):
                totals["precision_known_only"] = (
                    totals["hits"] / totals["known"] if totals["known"] else None)
                totals["recall_observed_only"] = (
                    totals["hits"] / universe_hits if universe_hits else None)
            by_threshold[str(threshold)] = {
                "observed_matured_market_windows": universe_known,
                "observed_positive_market_windows": universe_hits,
                "baseline": control_totals, "momentum_challenger": challenger_totals}
        result["by_horizon"][str(h)] = {
            "test_run_count": len(selected_runs),
            "nonoverlapping_spacing_hours": h,
            "test_run_as_of": [at.isoformat() for at, *_ in selected_runs],
            "thresholds": by_threshold}
    return result


def main(argv=None):
    import argparse
    import json
    from pathlib import Path
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", required=True)
    a = p.parse_args(argv)
    state = json.loads(Path(a.ledger).read_bytes())
    result = evaluate(state, state["runs"][-1]["as_of"])
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False))
    return result


if __name__ == "__main__":
    main()
