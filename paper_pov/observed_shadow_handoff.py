"""Read-only Kraken outcome to existing chronological shadow-learning adapter."""
import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .heldout_outcome_adapter import build_shadow_learning_state
from .shadow_learning_evidence import canonical_digest, utc_time

FEATURE_NAMES = ("baseline_score", "momentum_15m", "volume_acceleration")

def build_observed_shadow_handoff(ledger, observed, *, evaluation_asof_utc, candles=None):
    by_id = {p["prediction_id"]: p for p in ledger.get("predictions", [])}
    mature = {o["prediction_id"]: o for o in observed.get("outcomes", [])
              if o.get("horizon_hours") == 48 and o.get("coverage_complete") is True
              and type(o.get("hit")) is bool}
    result = {"schema": "observed_shadow_handoff_v1",
              "observed_complete_48h": len(mature),
              "feature_names": list(FEATURE_NAMES),
              "status": "INSUFFICIENT_DATA",
              "reason": "NO_CHRONOLOGICAL_TRAINING_COHORT",
              "feature_complete_predictions": 0,
              "source_authenticated": False,
              "promotion_authorized": False, "production_applied": False}
    by_pair = {}
    for candle in candles or []:
        by_pair.setdefault(candle["pair"], []).append(candle)
    for rows in by_pair.values():
        rows.sort(key=lambda c: c["timestamp_utc"])
    predictions = []
    for key, outcome in mature.items():
        p = by_id.get(key)
        if not p:
            continue
        entry_text = p.get("entry_utc") or p.get("as_of")
        entry = utc_time(entry_text)
        prior = [c for c in by_pair.get(p["pair"], [])
                 if utc_time(c["timestamp_utc"]) <= entry]
        if len(prior) < 7 or p.get("baseline_score") is None:
            continue
        last = prior[-1]
        before_15 = prior[-4]
        previous_volume = sum(float(c["volume"]) for c in prior[-7:-4])
        recent_volume = sum(float(c["volume"]) for c in prior[-4:-1])
        if float(before_15["close"]) <= 0 or previous_volume <= 0:
            continue
        features = {
            "baseline_score": float(p["baseline_score"]),
            "momentum_15m": float(last["close"]) / float(before_15["close"]) - 1,
            "volume_acceleration": recent_volume / previous_volume}
        predictions.append({
            "prediction_id": key, "pair": p["pair"],
            "entry_utc": entry_text,
            "feature_asof_utc": last["timestamp_utc"],
            "entry_price": p.get("entry_price") or p["price"],
            "features": features, "liquidity_qualified": False})
    result["feature_complete_predictions"] = len(predictions)
    result["excluded_without_point_in_time_features"] = len(mature) - len(predictions)
    result["training_predictions"] = 0
    result["heldout_predictions"] = 0
    if len(predictions) >= 4:
        entries = sorted(utc_time(p["entry_utc"]) for p in predictions)
        split = entries[len(entries) // 2]
        training_end = split - timedelta(hours=48)
        # The training window must contain 48h-matured outcomes before
        # the purge; recent Kraken OHLC may not reach back far enough.
        trainable = [p for p in predictions
                     if utc_time(p["entry_utc"]) + timedelta(hours=48) <= training_end]
        result["training_predictions"] = len(trainable)
        result["heldout_predictions"] = sum(utc_time(p["entry_utc"]) >= split for p in predictions)
        if trainable:
            baseline = {p["prediction_id"]: float(by_id[p["prediction_id"]]["baseline_score"]) >= 50
                        for p in predictions if utc_time(p["entry_utc"]) >= split}
            state = build_shadow_learning_state(
                predictions, candles, baseline,
                training_end_utc=training_end.isoformat(),
                holdout_start_utc=split.isoformat(),
                evaluation_asof_utc=evaluation_asof_utc,
                feature_names=FEATURE_NAMES)
            result["shadow_state"] = state
            result["status"] = ("SHADOW_EVALUATED" if state["comparison"]["status"] == "SHADOW_EVALUATED"
                                else "INSUFFICIENT_DATA")
            result["reason"] = state["comparison"]["status"]
    result["evidence_digest"] = canonical_digest(result)
    return result

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger_json", type=Path)
    parser.add_argument("observed_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--candles-json", type=Path)
    args = parser.parse_args(argv)
    candles = ([c for item in json.loads(args.candles_json.read_text())["results"]
                for c in item["candles"]] if args.candles_json else None)
    result = build_observed_shadow_handoff(
        json.loads(args.ledger_json.read_text()),
        json.loads(args.observed_json.read_text()),
        evaluation_asof_utc=datetime.now(timezone.utc).isoformat(),
        candles=candles)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "reason": result["reason"],
                      "observed_complete_48h": result["observed_complete_48h"],
                      "feature_complete_predictions": result["feature_complete_predictions"]}))
    return result

if __name__ == "__main__":
    main()
