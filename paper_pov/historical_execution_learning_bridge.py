"""Read-only bridge from E1's real Kraken trade-bar reconstruction to B learning.

The upstream pinned-byte SHA is not independent Kraken publisher attestation.
Every next-bar proxy entry remains excluded from qualified learning.
"""
import argparse
import hashlib
import json
from pathlib import Path

HORIZONS = (1, 6, 24, 48)
STATUSES = ("MATURED_OBSERVED", "ABSTAIN_ENTRY", "ABSTAIN_IMMATURE", "ABSTAIN_GAP")


def project_historical_execution(execution, *, frozen_predictions):
    if not isinstance(execution, dict) or execution.get("schema") != "historical_outcome_execution_v1":
        raise ValueError("Unsupported historical execution")
    batch = execution.get("outcomes")
    if not isinstance(batch, dict) or batch.get("schema") != "qualified_ohlc_outcome_batch_v1":
        raise ValueError("Unsupported reconstructed outcomes")
    if execution.get("source_authenticated") is not False or batch.get("source_authenticated") is not False:
        raise ValueError("Unexpected authentication claim")
    if execution.get("qualified_for_learning") is not False or execution.get("promotion_authorized") is not False:
        raise ValueError("Unexpected qualification claim")
    if not isinstance(frozen_predictions, list) or not frozen_predictions:
        raise ValueError("Missing frozen pre-outcome universe")
    universe = {}
    for prediction in frozen_predictions:
        if not isinstance(prediction, dict):
            raise ValueError("Malformed frozen prediction")
        pid, pair = prediction.get("prediction_id"), prediction.get("pair")
        if not isinstance(pid, str) or not pid or not isinstance(pair, str) or not pair or pid in universe:
            raise ValueError("Duplicate or malformed frozen identity")
        universe[pid] = pair
    records = batch.get("records")
    if not isinstance(records, list) or len(records) != batch.get("prediction_count"):
        raise ValueError("Invalid reconstructed record count")
    if not isinstance(execution.get("outcome_input_sha256"), str) or len(execution["outcome_input_sha256"]) != 64:
        raise ValueError("Missing input digest")
    if batch.get("source_sha256") != execution["outcome_input_sha256"]:
        raise ValueError("Inconsistent reconstruction digest")
    counts = {str(h): {status: 0 for status in STATUSES} for h in HORIZONS}
    seen = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Malformed reconstructed record")
        pid = record.get("prediction_id")
        if pid in seen or pid not in universe or record.get("pair") != universe[pid]:
            raise ValueError("Reconstruction does not match frozen prediction universe")
        seen.add(pid)
        if record.get("source_authenticated") is not False or record.get("entry_method") != "next_5m_bar_open_proxy":
            raise ValueError("Unexpected entry qualification or authentication")
        if record.get("source_sha256") != batch["source_sha256"]:
            raise ValueError("Inconsistent record source digest")
        labels = record.get("labels")
        if not isinstance(labels, list) or len(labels) != len(HORIZONS):
            raise ValueError("Incomplete horizon record")
        observed = set()
        for label in labels:
            if not isinstance(label, dict):
                raise ValueError("Malformed horizon label")
            horizon, status = label.get("horizon_hours"), label.get("status")
            if type(horizon) is not int or horizon not in HORIZONS or horizon in observed or status not in STATUSES:
                raise ValueError("Invalid or duplicate reconstructed horizon")
            observed.add(horizon)
            if status == "MATURED_OBSERVED":
                if type(label.get("observed_30pct_hit")) is not bool or label.get("qualified_for_learning") is not False:
                    raise ValueError("Unqualified observed label malformed")
            elif label.get("observed_30pct_hit") is not None:
                raise ValueError("Abstaining horizon cannot carry a hit")
            counts[str(horizon)][status] += 1
        if observed != set(HORIZONS):
            raise ValueError("Missing reconstructed horizon")
    canonical = json.dumps(sorted(universe.items()), separators=(",", ":")).encode()
    return {
        "schema": "paper_learning_handoff_v1",
        "status": "NO_QUALIFIED_RULE",
        "source": "historical_outcome_execution_v1",
        "outcome_input_sha256": batch["source_sha256"],
        "frozen_universe_digest": hashlib.sha256(canonical).hexdigest(),
        "frozen_prediction_count": len(universe),
        "reconstructed_prediction_count": len(seen),
        "missing_prediction_count": len(universe) - len(seen),
        "diagnostic_horizon_status_counts": counts,
        "qualified_cohort_count": 0,
        "source_authenticated": False,
        "measured_lift_verified": False,
        "live_watch_authorized": False,
        "promotion_authorized": False,
        "production_applied": False,
        "read_only": True,
        "reason": "Pinned trade bytes and proxy entry do not establish publisher authentication or executable liquidity",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Read-only historical outcomes to B abstention handoff")
    parser.add_argument("--execution", type=Path, required=True)
    parser.add_argument("--frozen-predictions", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.output.exists():
        raise FileExistsError("Refusing to overwrite learning evidence")
    execution = json.loads(args.execution.read_text(encoding="utf-8"))
    frozen = json.loads(args.frozen_predictions.read_text(encoding="utf-8"))
    result = project_historical_execution(execution, frozen_predictions=frozen)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    main()
