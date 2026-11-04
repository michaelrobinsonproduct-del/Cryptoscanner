"""Read-only verified-partition to multi-horizon outcomes orchestration.

Source provenance and eligibility remain explicit; labels cannot be fed to
learning as authenticated without independent publisher evidence and liquidity.
"""
import argparse
import json
from pathlib import Path
from .historical_outcome_bridge import prepare_outcome_input
from .qualified_ohlc_outcomes import reconstruct_batch
from .scanner import atomic_json


def run_historical_outcomes(manifest, root, schema, partitions, predictions, observed_until):
    prepared = prepare_outcome_input(manifest, root, schema, partitions,
                                     predictions, observed_until)
    payload = prepared["outcome_input"]
    outcomes = reconstruct_batch(payload["predictions"], payload["bars_by_pair"],
                                 observed_until=payload["observed_until"],
                                 source_sha256=prepared["outcome_input_sha256"])
    statuses = outcomes["status_counts"]
    return {"schema": "historical_outcome_execution_v1",
            "outcomes": outcomes,
            "partition_provenance": prepared["partition_provenance"],
            "outcome_input_sha256": prepared["outcome_input_sha256"],
            "prediction_count": outcomes["prediction_count"],
            "status_counts": statuses,
            "source_authenticated": False,
            "qualified_for_learning": False,
            "qualified_cohorts": [],
            "learning_qualified_count": 0,
            "held_out_lift": None,
            "promotion_authorized": False,
            "production_applied": False,
            "reason": "Archive publisher attestation, executable entry liquidity, and unbiased baseline candidate universe missing"}


def main():
    parser = argparse.ArgumentParser()
    for key in ("manifest", "schema", "root", "partitions", "predictions", "observed-until", "output"):
        parser.add_argument("--" + key, required=True)
    args = parser.parse_args()
    result = run_historical_outcomes(
        json.loads(Path(args.manifest).read_text()), args.root,
        json.loads(Path(args.schema).read_text()),
        json.loads(Path(args.partitions).read_text()),
        json.loads(Path(args.predictions).read_text()), args.observed_until)
    atomic_json(args.output, result)
    print(json.dumps({"prediction_count": result["prediction_count"],
                      "status_counts": result["status_counts"],
                      "learning_qualified_count": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
