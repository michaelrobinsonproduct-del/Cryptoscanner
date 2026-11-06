"""Read-only adapter for the real public paper ledger artifact."""
import argparse
import hashlib
import json
from pathlib import Path

from .shadow_learning_evidence import canonical_digest

HORIZONS = (1, 6, 24, 48)

def learn_from_public_ledger(ledger):
    """Account for persisted predictions and observed outcomes without inventing candles."""
    if not isinstance(ledger, dict) or ledger.get("schema") is None:
        raise ValueError("Missing public ledger schema")
    predictions = {}
    for prediction in ledger.get("predictions", []):
        key = prediction["prediction_id"]
        if key in predictions:
            raise ValueError("Duplicate prediction ID in retained ledger")
        predictions[key] = prediction
    outcome_counts = {str(h): {"hits": 0, "misses": 0, "abstentions": 0}
                      for h in HORIZONS}
    seen = set()
    for outcome in ledger.get("outcomes", []):
        key = outcome["prediction_id"]
        horizon = outcome["horizon_hours"]
        if horizon not in HORIZONS:
            continue
        identity = (key, horizon)
        if identity in seen:
            raise ValueError("Duplicate outcome horizon")
        seen.add(identity)
        if key not in predictions:
            raise ValueError("Outcome references unknown retained prediction")
        status = outcome["status"]
        bucket = outcome_counts[str(horizon)]
        if status.startswith("ABSTAIN") or status in ("IMMATURE", "MISSING_CANDLES"):
            bucket["abstentions"] += 1
        elif status == "MATURE_HIT":
            bucket["hits"] += 1
        elif status == "MATURE_MISS":
            bucket["misses"] += 1
        else:
            raise ValueError("Unrecognized outcome status: " + status)
    result = {
        "schema": "public_paper_learning_handoff_v1",
        "ledger_generation": ledger.get("generation"),
        "retained_prediction_count": len(predictions),
        "archived_prediction_count": ledger.get("archived", {}).get("predictions", 0),
        "archived_matured_labels": ledger.get("archived", {}).get("matured_labels", 0),
        "archived_observed_30pct_hits": ledger.get("archived", {}).get("observed_30pct_hits", 0),
        "archived_gap_abstentions": ledger.get("archived", {}).get("gap_abstentions", 0),
        "outcome_counts": outcome_counts,
        "eligible_training_count": sum(v["hits"] + v["misses"] for v in outcome_counts.values()),
        "status": "NO_QUALIFIED_RULE",
        "source_authenticated": False,
        "measured_lift_verified": False,
        "promotion_authorized": False,
        "production_applied": False,
        "read_only": True,
    }
    result["evidence_digest"] = canonical_digest(result)
    return result

def process_ledger_file(path, output):
    source = Path(path)
    raw = source.read_bytes()
    ledger = json.loads(raw)
    result = learn_from_public_ledger(ledger)
    result["input_sha256"] = hashlib.sha256(raw).hexdigest()
    result["evidence_digest"] = canonical_digest({k: v for k, v in result.items() if k != "evidence_digest"})
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return result

def main(argv=None):
    parser = argparse.ArgumentParser(description="Read-only real paper ledger learning")
    parser.add_argument("ledger_json", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    result = process_ledger_file(args.ledger_json, args.output)
    print(json.dumps({"status": result["status"],
                      "retained_prediction_count": result["retained_prediction_count"],
                      "eligible_training_count": result["eligible_training_count"],
                      "evidence_digest": result["evidence_digest"]}, sort_keys=True))
    return result

if __name__ == "__main__":
    main()
