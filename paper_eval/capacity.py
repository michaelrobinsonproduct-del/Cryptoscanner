"""Read-only conservative storage forecast for GitHub-hosted paper history.

No scanner writer, market requests, release promotion, or schedule modification.
This is a modeled capacity gate, not a reliability or predictive-success proof.
"""
import argparse
import datetime as dt
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

from paper_pov import ledger
from paper_pov.scanner import atomic_json

RESERVE_FRACTION = 0.20
MIN_RUNS = 3
MIN_OBSERVATIONS_PER_RUN = 100


def _size(item):
    return len(ledger.canonical(item)) + 1  # JSON collection comma/newline allowance


def _upper(items, fallback=0):
    return max([fallback] + [_size(x) for x in items])


def _forecast(state, cadence, counts, sizes, limit):
    if cadence not in (1, 2):
        raise ValueError("Only one or two scans per hour are modeled")
    active = math.ceil(ledger.RETENTION.total_seconds() / 3600 * cadence) + 4
    indexed = math.ceil(ledger.ARCHIVE_INDEX_RETENTION.total_seconds() / 3600 * cadence) + 4
    # Two conservative margins: +10% on record widths and quote population,
    # plus a separate 20% hard-capacity reserve before declaring storage safe.
    quote_count = math.ceil(counts["observations"] * 1.10)
    predictions = counts["predictions"]
    projected = (8192
                 + active * (math.ceil(sizes["run"] * 1.10)
                             + predictions * math.ceil(sizes["prediction"] * 1.10)
                             + quote_count * math.ceil(sizes["observation"] * 1.10)
                             + predictions * len(ledger.HORIZONS) *
                               math.ceil(sizes["outcome"] * 1.10))
                 + indexed * math.ceil(sizes["run"] * 1.10))
    threshold = math.floor(limit * (1 - RESERVE_FRACTION))
    return {
        "scans_per_hour": cadence,
        "modeled_active_runs": active,
        "modeled_30d_index_runs": indexed,
        "modeled_quotes_per_scan": quote_count,
        "modeled_predictions_per_scan": predictions,
        "forecast_ledger_bytes": projected,
        "max_ledger_bytes": limit,
        "reserved_headroom_bytes": limit - projected,
        "safety_threshold_bytes": threshold,
        "storage_capacity_pass": projected <= threshold,
    }


def capacity_report(state, *, max_bytes=ledger.MAX_BYTES):
    ledger.verify(state)
    if type(max_bytes) is not int or max_bytes <= 0:
        raise ValueError("Invalid ledger capacity")
    runs = state["runs"]
    observations = state["observations"]
    predictions = state["predictions"]
    if not runs:
        raise ValueError("No real persisted ledger runs to size")
    per_run_obs = Counter(o["run_id"] for o in observations)
    # A 48h matured outcome has more fields than a gap abstention. Never
    # forecast only from early zero-maturity or gap-only outcomes.
    sample_outcome = {
        "prediction_id": "f" * 64, "horizon_hours": 48,
        "status": "MATURED_OBSERVED",
        "target_at": "2026-10-31T20:30:00.000000+00:00",
        "observed_at": "2026-10-31T21:15:00.000000+00:00",
        "return_pct": -999999.9999, "observed_peak_pct": 999999.9999,
        "observed_30pct_hit": True,
    }
    sizes = {
        "run": _upper(runs + state.get("archive_index", [])),
        "prediction": _upper(predictions),
        "observation": _upper(observations),
        "outcome": _upper(state["outcomes"], _size(sample_outcome)),
    }
    counts = {
        "observations": max(per_run_obs.values()),
        "predictions": max(r["watch_count"] for r in runs),
    }
    sufficient = (len(runs) >= MIN_RUNS and
                  min(per_run_obs.get(r["id"], 0) for r in runs) >=
                  MIN_OBSERVATIONS_PER_RUN)
    scenarios = {
        str(c): _forecast(state, c, counts, sizes, max_bytes)
        for c in (1, 2)
    }
    return {
        "schema": 1,
        "mode": "READ_ONLY_PAPER_STORAGE_FORECAST",
        "ledger_generation": state["generation"],
        "ledger_sha256": state["sha256"],
        "current_ledger_bytes": len(ledger.canonical(state)),
        "sampled_retained_runs": len(runs),
        "min_observations_in_sampled_run": min(per_run_obs.get(r["id"], 0)
                                               for r in runs),
        "max_observations_in_sampled_run": counts["observations"],
        "max_predictions_in_sampled_run": counts["predictions"],
        "sample_sufficient": sufficient,
        "serialized_max_record_bytes": sizes,
        "cadences": scenarios,
        "stage2_storage_gate_pass": sufficient and scenarios["2"]["storage_capacity_pass"],
        "stage2_authorized": False,
        "independent_held_out_lift": None,
        "production_applied": False,
        "limitations": (
            "Conservative model from checksum-sealed client-observed paper records; "
            "not a future Kraken market-count guarantee, 30-day recovery proof, "
            "unattended reliability proof, or permission to increase scan cadence."
        ),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--ledger-commit", required=True)
    args = p.parse_args()
    if (len(args.ledger_commit) != 40 or
            any(c not in "0123456789abcdef" for c in args.ledger_commit)):
        raise ValueError("Exact immutable ledger Git commit required")
    state = json.loads(Path(args.ledger).read_text())
    result = capacity_report(state)
    result["ledger_commit"] = args.ledger_commit
    result["report_sha256"] = hashlib.sha256(ledger.canonical(result)).hexdigest()
    atomic_json(args.output, result)
    if json.loads(Path(args.output).read_text()) != result:
        raise ValueError("Storage report readback mismatch")
    print("PAPER_STORAGE_CAPACITY", json.dumps({
        "ledger_commit": args.ledger_commit,
        "generation": result["ledger_generation"],
        "current_bytes": result["current_ledger_bytes"],
        "hourly_forecast_bytes": result["cadences"]["1"]["forecast_ledger_bytes"],
        "twice_hourly_forecast_bytes": result["cadences"]["2"]["forecast_ledger_bytes"],
        "twice_hourly_storage_pass": result["stage2_storage_gate_pass"],
        "stage2_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
