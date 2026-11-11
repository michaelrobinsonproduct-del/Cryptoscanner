"""Carry forward observed Kraken OHLC across read-only learning artifacts.

No candle synthesis, interpolation, scoring changes or ledger writes. Archived
observations remain unverified source claims (not authenticated exchange history).
"""
import argparse
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

SCHEMA = "kraken_ohlc_observations_v1"
UTC = dt.timezone.utc
MAX_DAYS = 14


def _rows(item):
    if not isinstance(item, dict) or not isinstance(item.get("pair"), str):
        raise ValueError("Invalid pair evidence")
    if not isinstance(item.get("response_sha256"), str) or len(item["response_sha256"]) != 64:
        raise ValueError("Missing Kraken source digest")
    if not isinstance(item.get("candles"), list):
        raise ValueError("Missing observed candles")
    result = {}
    for row in item["candles"]:
        if row.get("pair") != item["pair"]:
            raise ValueError("Cross-pair candle")
        timestamp = dt.datetime.fromisoformat(row["timestamp_utc"].replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            raise ValueError("Naive candle timestamp")
        timestamp = timestamp.astimezone(UTC)
        close, high, volume = (float(row[k]) for k in ("close", "high", "volume"))
        if not all(math.isfinite(x) for x in (close, high, volume)) or not (0 < close <= high and volume >= 0):
            raise ValueError("Invalid observed candle")
        if "trades" in row and (type(row["trades"]) is not int or row["trades"] < 0):
            raise ValueError("Invalid observed trade count")
        key = timestamp.isoformat()
        if key in result and result[key] != row:
            raise ValueError("Conflicting duplicate candle")
        result[key] = row
    return result


def _merge_same_observation(prior, current, pair):
    # Legacy candles predate the Kraken trade-count field. Accept only
    # additive, source-observed enrichment; immutable historical OHLCV must
    # still match. Never invent trades or rewrite an existing trade count.
    keys = ("pair", "timestamp_utc", "close", "high", "volume")
    if any(prior.get(key) != current.get(key) for key in keys):
        raise ValueError("Kraken history overlap rewritten for " + pair)
    if ("trades" in prior and "trades" in current
            and prior["trades"] != current["trades"]):
        raise ValueError("Kraken history trade count rewritten for " + pair)
    return current if "trades" not in prior and "trades" in current else prior


def merge_observed_history(previous, fresh, *, keep_days=MAX_DAYS):
    """Merge actual 5m observations; disallow rewriting previously seen rows."""
    if type(keep_days) is not int or not 1 <= keep_days <= 30:
        raise ValueError("Invalid retention")
    if not isinstance(fresh, dict) or fresh.get("schema") != SCHEMA:
        raise ValueError("Missing new Kraken OHLC source")
    if previous is not None and (not isinstance(previous, dict) or previous.get("schema") != SCHEMA):
        raise ValueError("Invalid retained Kraken OHLC source")
    grouped = {}
    inputs = [(previous, "prior"), (fresh, "current")]
    for payload, source in inputs:
        if payload is None:
            continue
        for item in payload.get("results", []):
            pair = item["pair"]
            rows = _rows(item)
            if pair not in grouped:
                grouped[pair] = {"rows": {}, "sources": [], "key": item.get("kraken_pair_key")}
            group = grouped[pair]
            for stamp, candle in rows.items():
                if stamp in group["rows"]:
                    group["rows"][stamp] = _merge_same_observation(
                        group["rows"][stamp], candle, pair)
                else:
                    group["rows"][stamp] = candle
            group["sources"].append(item["response_sha256"])
            if source == "current":
                group["key"] = item.get("kraken_pair_key")
    timestamps = [dt.datetime.fromisoformat(t) for g in grouped.values() for t in g["rows"]]
    if not timestamps:
        raise ValueError("No observed candles")
    cutoff = max(timestamps) - dt.timedelta(days=keep_days)
    results = []
    for pair, group in sorted(grouped.items()):
        rows = [group["rows"][stamp] for stamp in sorted(group["rows"])
                if dt.datetime.fromisoformat(stamp) >= cutoff]
        if not rows:
            continue
        digest = hashlib.sha256("|".join(group["sources"]).encode()).hexdigest()
        results.append({"pair": pair, "kraken_pair_key": group["key"],
                        "source": "observed_kraken_ohlc_rolling",
                        "response_sha256": digest, "candles": rows,
                        "source_authenticated": False})
    return {"schema": SCHEMA, "results": results,
            "source_authenticated": False, "rolling": True,
            "retained_pairs": len(results),
            "retained_candles": sum(len(item["candles"]) for item in results)}


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--fresh", type=Path, required=True)
    parser.add_argument("--previous", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    fresh = json.loads(args.fresh.read_text())
    previous = json.loads(args.previous.read_text()) if args.previous and args.previous.is_file() else None
    result = merge_observed_history(previous, fresh)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
    print(json.dumps({"retained_pairs": result["retained_pairs"],
                      "retained_candles": result["retained_candles"],
                      "source_authenticated": False, "had_previous": previous is not None},
                     sort_keys=True))
    return result


if __name__ == "__main__":
    main()
