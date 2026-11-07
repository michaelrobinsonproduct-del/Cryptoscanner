"""Export actual ranked scanner predictions from a sealed paper receipt for learning."""
import argparse
import hashlib
import json
from pathlib import Path

def export_predictions(latest_path, receipt_path):
    latest = Path(latest_path).read_bytes()
    receipt = Path(receipt_path).read_bytes()
    if latest != receipt:
        raise ValueError("immutable receipt does not match published scanner report")
    report = json.loads(latest)
    if report.get("mode") != "PAPER_ONLY" or report.get("production_applied") is not False:
        raise ValueError("not an isolated paper scanner receipt")
    if report.get("scan_status") not in ("WATCH", "ABSTAIN_NO_QUALIFIED_OHLC",
                                         "ABSTAIN_NO_LIQUID_CANDIDATES",
                                         "ABSTAIN_INCOMPLETE_TICKER_COVERAGE"):
        raise ValueError("unknown paper scanner status")
    if report.get("scan_status") != "WATCH" and report.get("watch"):
        raise ValueError("abstained scan has WATCH predictions")
    predictions = []
    for expected_rank, watch in enumerate(report.get("watch", []), 1):
        if watch["rank"] != expected_rank or watch.get("status") != "PAPER_WATCH" or watch.get("buy_approved") is not False:
            raise ValueError("invalid ranked paper WATCH")
        if watch.get("as_of") != report["as_of"] or watch.get("quote_timestamp_semantics") != "client_observed_not_exchange_event_time":
            raise ValueError("prediction quote provenance mismatch")
        predictions.append({
            "prediction_id": watch["prediction_id"],
            "pair": watch["pair"],
            "symbol": watch["symbol"],
            "entry_utc": report["as_of"],
            "feature_asof_utc": watch["ohlc_last_closed_at"],
            "entry_price": watch["price"],
            "baseline_score": watch["baseline_score"],
            "challenger_score": watch["challenger_score"],
            "rank": watch["rank"],
            "features": {
                "move15_pct": watch["move15_pct"],
                "volume_accel": watch["volume_accel"],
                "spread_bps": watch["spread_bps"],
                "notional_24h_usd": watch["notional_24h_usd"],
            },
            "liquidity_qualified": True,
            "paper_only": True,
            "future_outcome_authenticated": False,
        })
    if len({p["prediction_id"] for p in predictions}) != len(predictions):
        raise ValueError("duplicate prediction identities")
    return {
        "schema": "paper_prediction_export_v1",
        "receipt_sha256": hashlib.sha256(receipt).hexdigest(),
        "as_of": report["as_of"],
        "scan_status": report["scan_status"],
        "predictions": predictions,
        "qualified_outcomes": 0,
        "production_applied": False,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("latest")
    parser.add_argument("receipt")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = export_predictions(args.latest, args.receipt)
    Path(args.output).write_text(json.dumps(result, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"receipt_sha256": result["receipt_sha256"],
                      "prediction_count": len(result["predictions"]),
                      "scan_status": result["scan_status"]}, sort_keys=True))

if __name__ == "__main__":
    main()
