"""Read-only bridge from verified trade bars to PR #173 outcome batch input.

Creates a provenance-bearing candidate payload, not a qualified outcome or
learning cohort. Consumer must recheck archive publisher authentication.
"""
import argparse
import hashlib
import json
from pathlib import Path
from .kraken_trade_csv_adapter import convert_pinned_csv
from .scanner import atomic_json, utc


def prepare_outcome_input(manifest, root, schema, partitions, predictions, observed_until):
    if not isinstance(partitions, dict) or not partitions:
        raise ValueError("Missing market-to-partition mapping")
    if not isinstance(predictions, list) or not predictions:
        raise ValueError("Missing paper predictions")
    pairs = {p["pair"] for p in predictions}
    if any(p.get("status") != "PAPER_WATCH" for p in predictions):
        raise ValueError("Only PAPER_WATCH predictions allowed")
    if any(not isinstance(p.get("prediction_id"), str) for p in predictions):
        raise ValueError("Missing immutable prediction identity")
    until = utc(observed_until)
    for p in predictions:
        if utc(p["as_of"]) > until:
            raise ValueError("Prediction after observation cutoff")
    bars_by_pair = {}
    provenance = {}
    for pair in sorted(pairs):
        name = partitions.get(pair)
        if name is None:
            bars_by_pair[pair] = []
            provenance[pair] = {"status": "ABSTAIN_NO_PINNED_PARTITION"}
            continue
        result = convert_pinned_csv(manifest, root, partition_file=name,
                                    pair=pair, schema=schema)
        bars_by_pair[pair] = result["bars"]
        provenance[pair] = {"status": "PINNED_BYTES_VERIFIED",
                            "partition": name,
                            "partition_sha256": result["partition_sha256"],
                            "trade_count": result["parsed_trade_count"],
                            "bar_count": result["bar_count"]}
    payload = {"predictions": predictions, "bars_by_pair": bars_by_pair,
               "observed_until": until.isoformat()}
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return {"schema": "historical_outcome_input_bridge_v1",
            "outcome_input": payload, "outcome_input_sha256": hashlib.sha256(canonical).hexdigest(),
            "partition_provenance": provenance,
            "source_authenticated": False, "qualified_for_learning": False,
            "production_applied": False,
            "reason": "Pinned partition bytes are not independently publisher-authenticated"}


def main():
    parser = argparse.ArgumentParser()
    for arg in ("manifest", "schema", "root", "partitions", "predictions", "observed-until", "output"):
        parser.add_argument("--" + arg, required=True)
    args = parser.parse_args()
    report = prepare_outcome_input(
        json.loads(Path(args.manifest).read_text()), args.root,
        json.loads(Path(args.schema).read_text()),
        json.loads(Path(args.partitions).read_text()),
        json.loads(Path(args.predictions).read_text()), args.observed_until)
    atomic_json(args.output, report)
    print(json.dumps({"schema": report["schema"], "markets": len(report["partition_provenance"]),
                      "qualified_for_learning": False}, sort_keys=True))


if __name__ == "__main__":
    main()
