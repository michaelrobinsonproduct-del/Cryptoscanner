"""Read-only observed Kraken OHLC -> existing shadow challenger integration."""
import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from .heldout_outcome_adapter import build_shadow_learning_state
from .shadow_learning_evidence import canonical_digest

def build_observed_shadow_handoff(ledger, observed, *, evaluation_asof_utc):
    source = observed.get("outcomes", [])
    by_id = {p["prediction_id"]: p for p in ledger.get("predictions", [])}
    qualified = [o for o in source if o.get("coverage_complete") is True
                 and o.get("horizon_hours") == 48 and type(o.get("hit")) is bool]
    feature_names = sorted(set.intersection(
        *(set(by_id[o["prediction_id"]].get("features", {})) for o in qualified)
    )) if qualified else []
    result = {"schema": "observed_shadow_handoff_v1",
              "observed_complete_48h": len(qualified),
              "feature_names": feature_names,
              "status": "NO_QUALIFIED_RULE",
              "source_authenticated": False,
              "promotion_authorized": False, "production_applied": False}
    if len(qualified) >= 4 and feature_names:
        predictions = []
        ids = {o["prediction_id"] for o in qualified}
        for p in ledger["predictions"]:
            if p["prediction_id"] not in ids:
                continue
            predictions.append({
                "prediction_id": p["prediction_id"], "pair": p["pair"],
                "entry_utc": p.get("entry_utc") or p["as_of"],
                "feature_asof_utc": p.get("feature_asof_utc") or p.get("entry_utc") or p["as_of"],
                "entry_price": p.get("entry_price") or p["price"],
                "features": p["features"], "liquidity_qualified": False})
        # Observed candles are passed separately by the caller; this handoff
        # deliberately never turns incomplete historical snapshots into labels.
        result["prediction_ids_with_features"] = [p["prediction_id"] for p in predictions]
    result["evidence_digest"] = canonical_digest(result)
    return result

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger_json", type=Path)
    parser.add_argument("observed_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    result = build_observed_shadow_handoff(json.loads(args.ledger_json.read_text()),
        json.loads(args.observed_json.read_text()),
        evaluation_asof_utc=datetime.now(timezone.utc).isoformat())
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"],
                      "observed_complete_48h": result["observed_complete_48h"]}))
    return result

if __name__ == "__main__":
    main()
