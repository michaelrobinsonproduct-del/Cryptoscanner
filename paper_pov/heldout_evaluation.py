"""Read-only, no-promotion chronological comparison of existing paper ledger scores.

Only matured, source-observed 48h labels qualify. No invented counterfactual
market movers or uplift; archived counts are insufficient for cohort evaluation.
"""
import argparse
import datetime as dt
import json
import math
from collections import defaultdict
from pathlib import Path

from .ledger import verify
from .scanner import utc

PURGE = dt.timedelta(hours=48)
MIN_TRAIN = 30
MIN_TEST = 30


def _finite_score(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Missing numeric ranking score")
    n = float(value)
    if not math.isfinite(n):
        raise ValueError("Nonfinite ranking score")
    return n


def evaluate(state, *, horizon=48, top_k=3, min_train=MIN_TRAIN,
             min_test=MIN_TEST):
    """Evaluate equal, fully observed cohorts; never promote a model."""
    verify(state)
    if horizon != 48:
        raise ValueError("Only fully matured 48h cohort supported")
    if type(top_k) is not int or top_k < 1:
        raise ValueError("Invalid top-k")
    if any(type(n) is not int or n < 1 for n in (min_train, min_test)):
        raise ValueError("Invalid minimum sample sizes")
    outcomes = {(o["prediction_id"], o["horizon_hours"]): o
                for o in state["outcomes"]}
    runs = {r["id"]: r for r in state["runs"]}
    grouped = defaultdict(list)
    abstained = 0
    for p in state["predictions"]:
        o = outcomes.get((p["prediction_id"], horizon))
        if o is None or o["status"] != "MATURED_OBSERVED":
            abstained += 1
            continue
        if (type(o.get("observed_30pct_hit")) is not bool
                or not isinstance(o.get("observed_peak_pct"), (int, float))
                or not math.isfinite(float(o["observed_peak_pct"]))):
            raise ValueError("Matured label lacks valid source outcome")
        if p["run_id"] not in runs:
            raise ValueError("Orphan evaluation run")
        grouped[p["run_id"]].append((p, o))
    cohorts = []
    for run_id, rows in grouped.items():
        # Require every WATCH in the scan to have a valid outcome.
        # Otherwise selecting only successful labels biases ranking results.
        if len(rows) != runs[run_id]["watch_count"]:
            abstained += len(rows)
            continue
        for p, _ in rows:
            _finite_score(p["baseline_score"])
            _finite_score(p["challenger_score"])
        if len(rows) < top_k:
            abstained += len(rows)
            continue
        base = sorted(rows, key=lambda x: (-float(x[0]["baseline_score"]),
                                          x[0]["prediction_id"]))[:top_k]
        challenge = sorted(rows, key=lambda x: (-float(x[0]["challenger_score"]),
                                               x[0]["prediction_id"]))[:top_k]
        cohorts.append({
            "as_of": utc(runs[run_id]["as_of"]),
            "run_id": run_id,
            "baseline_hits": sum(o["observed_30pct_hit"] for _, o in base),
            "challenger_hits": sum(o["observed_30pct_hit"] for _, o in challenge),
        })
    cohorts.sort(key=lambda x: (x["as_of"], x["run_id"]))
    result = {
        "schema": "paper_heldout_v1", "status": "NO_QUALIFIED_RULE",
        "horizon_hours": horizon, "top_k": top_k, "purge_hours": 48,
        "eligible_complete_runs": len(cohorts),
        "abstained_or_incomplete_predictions": abstained,
        "minimum_train_runs": min_train, "minimum_test_runs": min_test,
        "train_runs": 0, "test_runs": 0, "held_out_lift": None,
        "production_applied": False, "promotion_authorized": False,
        "reason": "Insufficient complete chronological cohorts",
    }
    if len(cohorts) < min_train + min_test:
        return result
    # Fixed last-N holdout; earlier training ends at least 48h before test.
    test = cohorts[-min_test:]
    cutoff = test[0]["as_of"] - PURGE
    train = [x for x in cohorts[:-min_test] if x["as_of"] <= cutoff]
    result["train_runs"] = len(train)
    result["test_runs"] = len(test)
    if len(train) < min_train:
        result["reason"] = "Insufficient pre-holdout cohorts after 48h purge"
        return result
    base_hits = sum(x["baseline_hits"] for x in test)
    challenge_hits = sum(x["challenger_hits"] for x in test)
    denominator = len(test) * top_k
    result.update({
        "baseline_hits": base_hits, "challenger_hits": challenge_hits,
        "holdout_predictions_per_arm": denominator,
        "baseline_hit_rate": base_hits / denominator,
        "challenger_hit_rate": challenge_hits / denominator,
        "held_out_lift": (challenge_hits - base_hits) / denominator,
        "holdout_start": test[0]["as_of"].isoformat(),
        "holdout_end": test[-1]["as_of"].isoformat(),
    })
    # A measured difference is not automatically a qualified rule.
    result["reason"] = "Exploratory held-out comparison only; no statistical or liquidity qualification"
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--top-k", type=int, default=3)
    args = p.parse_args()
    state = json.loads(Path(args.ledger).read_text())
    report = evaluate(state, top_k=args.top_k)
    from .scanner import atomic_json
    atomic_json(args.output, report)
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
