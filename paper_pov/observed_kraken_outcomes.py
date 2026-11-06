"""Reconstruct genuine paper prediction forward outcomes from recent Kraken OHLC."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from .heldout_outcome_adapter import reconstruct_forward_outcomes
from .shadow_learning_evidence import canonical_digest

def process_observed_outcomes(ledger, observations, *, evaluation_asof_utc):
    by_pair = {item["pair"]: item for item in observations["results"]}
    predictions = []
    for p in ledger["predictions"]:
        pair = p.get("pair")
        entry = p.get("entry_utc") or p.get("as_of")
        feature = p.get("feature_asof_utc") or entry
        price = p.get("entry_price") or p.get("price")
        if pair not in by_pair or not entry or not price:
            continue
        predictions.append({"prediction_id": p["prediction_id"], "pair": pair,
                            "entry_utc": entry, "feature_asof_utc": feature,
                            "entry_price": price, "liquidity_qualified": False,
                            "source_sha256": by_pair[pair]["response_sha256"]})
    candles = [c for item in observations["results"] for c in item["candles"]]
    outcomes = reconstruct_forward_outcomes(predictions, candles,
                                             evaluation_asof_utc=evaluation_asof_utc)
    result = {"schema": "observed_kraken_paper_outcomes_v1",
              "predictions_covered": len(predictions),
              "outcomes": outcomes,
              "complete_5m_outcomes": sum(x["coverage_complete"] for x in outcomes),
              "source_authenticated": False,
              "promotion_authorized": False, "production_applied": False}
    result["evidence_digest"] = canonical_digest(result)
    return result

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger_json", type=Path)
    parser.add_argument("observations_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    result = process_observed_outcomes(json.loads(args.ledger_json.read_text()),
                                       json.loads(args.observations_json.read_text()),
                                       evaluation_asof_utc=datetime.now(timezone.utc).isoformat())
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"predictions_covered": result["predictions_covered"],
                      "complete_5m_outcomes": result["complete_5m_outcomes"]}))
    return result

if __name__ == "__main__":
    main()
