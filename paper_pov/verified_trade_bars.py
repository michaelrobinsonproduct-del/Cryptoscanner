"""Offline trade-to-five-minute OHLCV conversion after pinned archive verification.

Input contract is normalized UTC trade records (pair, timestamp, price, volume).
Raw Kraken ZIP/CSV layouts require a separately verified source-specific adapter.
No trading, network calls, or production writes.
"""
import datetime as dt
import json
import math
from collections import defaultdict
from .scanner import utc

UTC = dt.timezone.utc


def _positive(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Non-numeric trade")
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError("Non-positive trade price or volume")
    return number


def trades_to_bars(trades, *, pair):
    """Aggregate time-ordered normalized trades; do not synthesize empty bars."""
    if not isinstance(trades, list) or not isinstance(pair, str) or not pair:
        raise ValueError("Invalid trades or pair")
    buckets = {}
    last = None
    for trade in trades:
        if trade.get("pair") != pair:
            raise ValueError("Cross-market trade in partition")
        at = utc(trade["timestamp"])
        if last is not None and at < last:
            raise ValueError("Out-of-order trade timestamps")
        last = at
        price = _positive(trade["price"])
        volume = _positive(trade["volume"])
        opened = dt.datetime.fromtimestamp(int(at.timestamp()) // 300 * 300, UTC)
        key = opened.isoformat()
        bar = buckets.get(key)
        if bar is None:
            buckets[key] = {"open_at": key, "open": price, "high": price,
                            "low": price, "close": price, "volume": volume,
                            "trade_count": 1}
        else:
            bar["high"] = max(bar["high"], price)
            bar["low"] = min(bar["low"], price)
            bar["close"] = price
            bar["volume"] += volume
            bar["trade_count"] += 1
    return list(buckets.values())


def convert_verified_partition(trades, *, pair, verification, partition_file):
    """Require matching pinned partition receipt, without claiming Kraken auth."""
    if verification.get("schema") != "archive_partition_verification_v1":
        raise ValueError("Missing partition verification receipt")
    if verification.get("status") != "BYTES_MATCH_PINNED_MANIFEST":
        raise ValueError("Unverified partition")
    matches = [p for p in verification.get("partitions", [])
               if p.get("file") == partition_file]
    if len(matches) != 1:
        raise ValueError("Partition not present in verification receipt")
    bars = trades_to_bars(trades, pair=pair)
    return {"schema": "verified_partition_ohlcv_v1", "pair": pair,
            "partition_file": partition_file, "partition_sha256": matches[0]["sha256"],
            "bars": bars, "bar_count": len(bars),
            "source_authenticated": False, "qualified_for_learning": False,
            "production_applied": False,
            "reason": "Manifest publisher and raw Kraken trade schema not independently authenticated"}

def convert_manifest_partition(manifest, root, *, partition_file, pair):
    """Read exactly the verified normalized JSONL bytes from the pinned partition.

    Every row is parsed from the same file whose digest was checked. This is
    not a Kraken raw-trade format adapter and never certifies source identity.
    """
    from pathlib import Path
    from .archive_partition_gate import verify_partitions
    receipt = verify_partitions(manifest, root)
    path = (Path(root).resolve() / partition_file).resolve(strict=True)
    if not path.is_relative_to(Path(root).resolve()):
        raise ValueError("Unsafe partition path")
    if not any(p["file"] == partition_file for p in receipt["partitions"]):
        raise ValueError("Unpinned partition")
    with path.open("r", encoding="utf-8") as stream:
        trades = [json.loads(line) for line in stream if line.strip()]
    result = convert_verified_partition(trades, pair=pair,
                                        verification=receipt,
                                        partition_file=partition_file)
    result["format"] = "normalized_trade_jsonl_v1"
    return result


def main():
    import argparse
    from pathlib import Path
    from .scanner import atomic_json
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--root", required=True)
    parser.add_argument("--partition", required=True)
    parser.add_argument("--pair", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    manifest = json.loads(Path(args.manifest).read_text())
    result = convert_manifest_partition(manifest, args.root,
                                        partition_file=args.partition, pair=args.pair)
    atomic_json(args.output, result)
    print(json.dumps({"pair": result["pair"], "bar_count": result["bar_count"],
                      "source_authenticated": False}, sort_keys=True))


if __name__ == "__main__":
    main()
