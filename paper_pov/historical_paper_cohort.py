"""Rebuild a read-only historical cohort from retained GitHub paper ledger snapshots.

Each artifact is a ledger snapshot; overlapping prediction IDs are deduplicated.
Archived counters are never expanded into invented per-prediction outcomes.
"""
import argparse
import json
from pathlib import Path
from .public_ledger_learning import HORIZONS
from .shadow_learning_evidence import canonical_digest

def reconstruct_history(ledgers):
    predictions, outcomes, conflicts = {}, {}, []
    generations = []
    for source_name, ledger in sorted(ledgers, key=lambda item: (item[1].get("generation", 0), item[0])):
        if ledger.get("schema") is None:
            raise ValueError("Missing ledger schema: " + source_name)
        generations.append({"source": source_name, "generation": ledger.get("generation")})
        for prediction in ledger.get("predictions", []):
            key = prediction["prediction_id"]
            if key in predictions and predictions[key] != prediction:
                conflicts.append({"source": source_name, "prediction_id": key, "kind": "PREDICTION"})
            else:
                predictions[key] = prediction
        for outcome in ledger.get("outcomes", []):
            key = (outcome["prediction_id"], outcome["horizon_hours"])
            if key in outcomes and outcomes[key] != outcome:
                prior = outcomes[key]
                if prior.get("status") in ("MATURE_HIT", "MATURE_MISS") and prior != outcome:
                    conflicts.append({"source": source_name, "prediction_id": key[0],
                                      "horizon_hours": key[1], "kind": "MATURE_OUTCOME_CHANGED"})
                elif outcome.get("status") in ("MATURE_HIT", "MATURE_MISS"):
                    outcomes[key] = outcome
                elif prior.get("status") not in ("MATURE_HIT", "MATURE_MISS"):
                    outcomes[key] = outcome
            else:
                outcomes[key] = outcome
    if conflicts:
        raise ValueError("Conflicting historical ledger snapshots: " + json.dumps(conflicts[:5]))
    counts = {str(h): {"hits": 0, "misses": 0, "abstentions": 0} for h in HORIZONS}
    qualified = []
    for (prediction_id, horizon), outcome in sorted(outcomes.items()):
        if prediction_id not in predictions:
            raise ValueError("Historical outcome without prediction: " + prediction_id)
        if horizon not in HORIZONS:
            continue
        status = outcome["status"]
        bucket = counts[str(horizon)]
        if status == "MATURE_HIT":
            bucket["hits"] += 1
        elif status == "MATURE_MISS":
            bucket["misses"] += 1
        elif status.startswith("ABSTAIN") or status in ("IMMATURE", "MISSING_CANDLES"):
            bucket["abstentions"] += 1
        else:
            raise ValueError("Unknown historical status: " + status)
        if status in ("MATURE_HIT", "MATURE_MISS"):
            qualified.append({"prediction_id": prediction_id, "horizon_hours": horizon,
                              "hit": status == "MATURE_HIT",
                              "entry_utc": predictions[prediction_id].get("as_of"),
                              "baseline_score": predictions[prediction_id].get("baseline_score"),
                              "challenger_score": predictions[prediction_id].get("challenger_score"),
                              "source_authenticated": False})
    result = {"schema": "historical_paper_cohort_v1",
              "snapshots": generations,
              "unique_predictions": len(predictions),
              "unique_outcomes": len(outcomes),
              "horizon_counts": counts,
              "recovered_mature_outcomes": len(qualified),
              "mature_outcome_rows": qualified,
              "prediction_rows": [predictions[k] for k in sorted(predictions)],
              "outcome_rows": [outcomes[k] for k in sorted(outcomes)],
              "source_authenticated": False,
              "measured_lift_verified": False,
              "promotion_authorized": False,
              "production_applied": False}
    result["evidence_digest"] = canonical_digest(result)
    return result

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("snapshot_directory", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    paths = sorted(args.snapshot_directory.glob("*/ledger.json"))
    paths += sorted(args.snapshot_directory.glob("*/historical-cohort.json"))
    if not paths:
        raise ValueError("No historical ledger snapshots found")
    snapshots = []
    for p in paths:
        data = json.loads(p.read_text())
        if p.name == "historical-cohort.json":
            if data.get("schema") != "historical_paper_cohort_v1":
                raise ValueError("Unexpected retained cohort schema")
            if data.get("evidence_digest") != canonical_digest({k: v for k, v in data.items() if k != "evidence_digest"}):
                raise ValueError("Retained cohort digest mismatch")
            data = {"schema": "recovered_cohort", "generation": -1,
                    "predictions": data["prediction_rows"], "outcomes": data["outcome_rows"]}
        snapshots.append((str(p.parent.name), data))
    result = reconstruct_history(snapshots)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("unique_predictions", "unique_outcomes",
                                             "recovered_mature_outcomes", "evidence_digest")}))
    return result

if __name__ == "__main__":
    main()
