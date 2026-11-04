"""Fail-closed read-only consumer of persisted A2 paper candidate snapshots."""
import argparse
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

from .scanner import STABLE

def read_snapshot(latest_path, now=None, max_age_seconds=600):
    latest = Path(latest_path)
    if latest.is_symlink() or not latest.is_file():
        raise ValueError("missing or linked latest snapshot")
    raw = latest.read_bytes()
    report = json.loads(raw)
    if not isinstance(report, dict):
        raise ValueError("invalid snapshot object")
    stamp = dt.datetime.fromisoformat(report["as_of"].replace("Z", "+00:00"))
    if stamp.tzinfo is None or stamp.utcoffset() is None:
        raise ValueError("naive scan timestamp")
    now = now if now is not None else dt.datetime.now(dt.timezone.utc)
    if now.tzinfo is None or now.utcoffset() is None:
        raise ValueError("naive verification clock")
    if not isinstance(max_age_seconds, (int, float)) or isinstance(max_age_seconds, bool) or not math.isfinite(max_age_seconds) or max_age_seconds <= 0 or max_age_seconds > 600:
        raise ValueError("invalid maximum quote age")
    age = (now - stamp).total_seconds()
    if not 0 <= age <= max_age_seconds:
        raise ValueError("stale or future paper snapshot")
    receipt = latest.parent / "receipts" / (stamp.astimezone(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + ".json")
    if receipt.parent.is_symlink() or receipt.is_symlink() or not receipt.is_file() or receipt.read_bytes() != raw:
        raise ValueError("missing or mismatched immutable receipt")
    if report.get("mode") != "PAPER_ONLY" or report.get("buy_approved") is not False:
        raise ValueError("non-paper report")
    watch = report.get("watch")
    if not isinstance(watch, list) or len(watch) > 12:
        raise ValueError("invalid watch collection")
    if watch and report.get("scan_status") != "WATCH":
        raise ValueError("scan status disagrees with candidates")
    if not watch and report.get("scan_status") not in {"ABSTAIN_NO_LIQUID_CANDIDATES", "ABSTAIN_NO_QUALIFIED_OHLC"}:
        raise ValueError("invalid abstention status")
    for field in ("eligible_pairs", "observed_markets"):
        value = report.get(field)
        if type(value) is not int or value < 0:
            raise ValueError("invalid coverage count: " + field)
    if report["observed_markets"] > report["eligible_pairs"]:
        raise ValueError("observed coverage exceeds eligible markets")
    abstentions = report.get("abstention_counts")
    if not isinstance(abstentions, dict) or any(not isinstance(k, str) or not k or type(v) is not int or v < 0 for k, v in abstentions.items()):
        raise ValueError("invalid abstention counts")
    if len(watch) > report["observed_markets"]:
        raise ValueError("watch exceeds observed markets")
    # Preserve deterministic challenger ranking in the sealed WATCH handoff.
    if any(not isinstance(c, dict) for c in watch):
        raise ValueError("invalid paper candidate contract")
    seen = set()
    previous_sort_key = None
    for rank, candidate in enumerate(watch, 1):
        if type(candidate.get("rank")) is not int or candidate["rank"] != rank or candidate.get("status") != "PAPER_WATCH" or candidate.get("buy_approved") is not False:
            raise ValueError("invalid paper candidate contract")
        pair = candidate.get("pair")
        if not isinstance(pair, str) or not pair or pair in seen:
            raise ValueError("duplicate or invalid pair")
        seen.add(pair)
        if not isinstance(candidate.get("symbol"), str) or candidate["symbol"].split("/")[0].upper() in STABLE:
            raise ValueError("stablecoin WATCH candidate prohibited")
        # B projects the displayed Kraken symbol from this sealed candidate.
        # Reject malformed/missing symbols at A readback instead of allowing a
        # downstream KeyError or a non-displayable persisted WATCH.
        symbol = candidate.get("symbol")
        if not isinstance(symbol, str) or not symbol or len(symbol) > 64 or any(ch.isspace() or ord(ch) < 33 for ch in symbol):
            raise ValueError("invalid WATCH display symbol")
        if candidate.get("as_of") != report["as_of"] or candidate.get("prediction_id") != hashlib.sha256(("paper-v1|" + report["as_of"] + "|" + pair).encode()).hexdigest():
            raise ValueError("candidate provenance mismatch")
        if candidate.get("quote_timestamp_semantics") != "client_observed_not_exchange_event_time":
            raise ValueError("unverified quote timestamp semantics")
        quote = dt.datetime.fromisoformat(candidate["quote_observed_at"].replace("Z", "+00:00"))
        if quote.tzinfo is None or quote.utcoffset() is None or not 0 <= (stamp - quote).total_seconds() <= 600:
            raise ValueError("stale candidate quote")
        # A fresh ticker cannot make stale completed OHLC momentum valid.
        closed_at_raw = candidate.get("ohlc_last_closed_at")
        if not isinstance(closed_at_raw, str):
            raise ValueError("missing completed OHLC provenance")
        closed_at = dt.datetime.fromisoformat(closed_at_raw.replace("Z", "+00:00"))
        if closed_at.tzinfo is None or closed_at.utcoffset() is None or not 0 <= (stamp - closed_at).total_seconds() <= 600:
            raise ValueError("stale completed OHLC evidence")
        if not 0 <= (now - closed_at).total_seconds() <= max_age_seconds:
            raise ValueError("expired completed OHLC at read time")
        # Scan freshness alone is insufficient: a quote may be 9m old at scan
        # time and 9m old again when read. Enforce the actual read-time age.
        quote_age = (now - quote).total_seconds()
        if not 0 <= quote_age <= max_age_seconds:
            raise ValueError("expired candidate quote at read time")
        for field in ("price", "move15_pct", "volume_accel", "baseline_score", "challenger_score", "spread_bps"):
            value = candidate.get(field)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError("invalid numeric candidate field: " + field)
        if candidate["price"] <= 0 or candidate["volume_accel"] <= 0 or candidate["spread_bps"] < 0:
            raise ValueError("invalid candidate market metrics")
        sort_key = (-candidate["challenger_score"], pair)
        if previous_sort_key is not None and sort_key < previous_sort_key:
            raise ValueError("WATCH challenger ranking mismatch")
        previous_sort_key = sort_key
        if (candidate.get("momentum_reference") != "completed_5m_candles_15m" or
                candidate.get("volume_acceleration_reference") != "last_30m_over_prior_30m"):
            raise ValueError("missing WATCH metric provenance")
        expected_risk = ("HIGH" if candidate["spread_bps"] > 30 or
                         candidate["volume_accel"] < 0.8 or abs(candidate["move15_pct"]) > 8
                         else "ELEVATED")
        if candidate.get("risk") != expected_risk:
            raise ValueError("invalid WATCH risk classification")
    if latest.is_symlink() or latest.read_bytes() != raw:
        raise ValueError("snapshot changed during verification")
    return {"as_of": report["as_of"], "scan_status": report["scan_status"],
            "eligible_pairs": report.get("eligible_pairs"), "observed_markets": report.get("observed_markets"),
            "abstention_counts": report.get("abstention_counts", {}), "watch": watch,
            "receipt_sha256": hashlib.sha256(raw).hexdigest(), "snapshot_age_seconds": round(age, 3),
            "quote_age_seconds": {c["pair"]: round((now - dt.datetime.fromisoformat(c["quote_observed_at"].replace("Z", "+00:00"))).total_seconds(), 3) for c in watch}}

def main():
    parser = argparse.ArgumentParser(description="Verify and emit immutable A2 paper candidate snapshot")
    parser.add_argument("latest", help="path to scanner latest.json")
    args = parser.parse_args()
    print(json.dumps(read_snapshot(args.latest), sort_keys=True, allow_nan=False))

if __name__ == "__main__":
    main()
