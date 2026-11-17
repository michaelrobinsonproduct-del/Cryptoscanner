"""Bounded read-only continuity for immutable predictions, not a second ledger."""
import argparse
import datetime as dt
import json
from pathlib import Path
from .shadow_learning_evidence import canonical_digest, utc_time

SCHEMA = "paper_learning_prediction_cohort_v1"
RETENTION = dt.timedelta(days=14)
MAX_ROWS = 60000  # 12 WATCHs * 288 five-minute scans * 14 days, with slack.

def merge(current, previous=None):
    if previous is not None:
        if previous.get("schema") != SCHEMA or previous.get("digest") != canonical_digest(
                {k:v for k,v in previous.items() if k != "digest"}):
            raise ValueError("Invalid prior prediction cohort checksum")
        if previous.get("production_applied") is not False:
            raise ValueError("Unexpected promoted learning cohort")
    if not current.get("runs"):
        raise ValueError("No persisted writer history")
    now = utc_time(current["runs"][-1]["as_of"])
    if previous and utc_time(previous["as_of"]) > now:
        raise ValueError("Refuse learning cohort rollback")
    if previous and previous["ledger_generation"] > current["generation"]:
        raise ValueError("Refuse learning generation rollback")
    cutoff = now - RETENTION
    by_id = {}
    for row in (previous or {}).get("predictions", []) + current["predictions"]:
        stamp = utc_time(row["as_of"])
        if stamp > now:
            raise ValueError("Prediction from future writer")
        if stamp < cutoff:
            continue
        key = row["prediction_id"]
        if key in by_id and by_id[key] != row:
            raise ValueError("Immutable prediction changed")
        by_id[key] = row
    if len(by_id) > MAX_ROWS:
        raise ValueError("Learning cohort exceeds bounded retention capacity")
    result = {"schema": SCHEMA, "as_of": now.isoformat(),
              "ledger_generation": current["generation"], "ledger_sha256": current["sha256"],
              "predictions": sorted(by_id.values(), key=lambda p:(p["as_of"],p["prediction_id"])),
              "production_applied": False, "promotion_authorized": False}
    result["digest"] = canonical_digest(result)
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--previous", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    current = json.loads(args.ledger.read_text())
    previous = json.loads(args.previous.read_text()) if args.previous.is_file() else None
    result = merge(current, previous)
    args.output.write_text(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
    print(json.dumps({"learning_cohort_predictions": len(result["predictions"]),
                      "ledger_generation": result["ledger_generation"],
                      "prior_cohort_present": previous is not None,
                      "oldest_prediction": result["predictions"][0]["as_of"] if result["predictions"] else None}))

if __name__ == "__main__":
    main()
