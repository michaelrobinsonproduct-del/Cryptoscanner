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
