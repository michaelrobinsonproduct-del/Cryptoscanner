"""Fail-closed bounded CSV trade parsing and independent 5m candle comparison.

Kraken historical trade archive CSV schema must be confirmed against real rows
before using this parser to authorize labels. Parsing alone is not provenance.
"""
import csv
import io
import math
import zipfile
from collections import defaultdict
from pathlib import PurePosixPath

from verify_trade_candle_provenance import verify_open_boundary

MAX_MEMBER_BYTES = 64 * 1024 * 1024
MAX_ROWS = 250000
MAX_INTERVAL_TRADES = 20000
STEP = 300


HEADER = ("timestamp", "price", "volume", "type", "order_type", "misc", "trade_id")


def parse_member(archive, name, *, schema_verified=False):
    if not schema_verified:
        raise RuntimeError("official header and source identity not verified")
    path = PurePosixPath(name)
    if not name.endswith(".csv") or len(path.parts) != 1 or ".." in path.parts or "\\\\" in name:
        raise ValueError("unsafe trade member")
    matches = [x for x in archive.infolist() if x.filename == name]
    if len(matches) != 1 or matches[0].file_size > MAX_MEMBER_BYTES or matches[0].flag_bits & 1:
        raise ValueError("missing duplicate encrypted or oversized member")
    records, seen_ids = [], set()
    with archive.open(matches[0]) as raw:
        reader = csv.reader(io.TextIOWrapper(raw, encoding="utf-8-sig", newline="", errors="strict"))
        header = next(reader, None)
        if header is None or tuple(x.strip() for x in header) != HEADER:
            raise ValueError("unrecognized official Kraken historical trade CSV header")
        for row in reader:
            if len(records) >= MAX_ROWS or len(row) != 7:
                raise ValueError("invalid trade CSV shape or row cap")
            timestamp, price, volume = map(float, row[:3])
            if not all(math.isfinite(x) for x in (timestamp, price, volume)) or timestamp < 0 or price <= 0 or volume <= 0:
                raise ValueError("invalid trade CSV values")
            if row[3] not in ("b", "s") or row[4] not in ("l", "m") or not row[6].strip():
                raise ValueError("invalid trade direction, order type or id")
            if row[6] in seen_ids:
                raise ValueError("duplicate trade id")
            seen_ids.add(row[6])
            records.append((timestamp, price, volume, len(records)))
    if not records:
        raise ValueError("empty trade CSV")
    if any(records[i][0] > records[i+1][0] for i in range(len(records)-1)):
        raise ValueError("trade timestamps out of order")
    return records


def aggregate(records):
    by_bucket = defaultdict(list)
    for record in records:
        if len(record) != 4 or record[0] < 0:
            raise ValueError("invalid trade record")
        start = int(record[0] // STEP) * STEP
        by_bucket[start].append(record)
        if len(by_bucket[start]) > MAX_INTERVAL_TRADES:
            raise ValueError("interval trade count cap")
    result = {}
    for start, rows in by_bucket.items():
        ordered = sorted(rows, key=lambda x: (x[0], x[3]))
        prices = [x[1] for x in ordered]
        result[start] = (start, prices[0], max(prices), min(prices), prices[-1],
                         sum(x[2] for x in ordered), len(ordered))
    return result, by_bucket


def compare(archive_rows, trades, *, independently_complete=False):
    """Only verified complete source can be accepted; mismatch always abstains."""
    if not independently_complete:
        return {"status": "abstain_unverified_trade_completeness", "verified_intervals": 0}
    # A caller's completeness assertion must never turn an empty, duplicated,
    # unaligned or malformed OHLC selection into a verified comparison.
    # This still does NOT authenticate the independent trade archive itself.
    if not archive_rows:
        return {"status": "missing_ohlc_evidence", "verified_intervals": 0}
    if len(archive_rows) > MAX_ROWS or len(trades) > MAX_ROWS:
        raise ValueError("comparison resource cap")
    starts = []
    for candle in archive_rows:
        if len(candle) != 7:
            return {"status": "invalid_ohlc_shape", "verified_intervals": 0}
        timestamp = candle[0]
        if (isinstance(timestamp, bool) or not isinstance(timestamp, (int, float))
                or not math.isfinite(timestamp) or timestamp != int(timestamp)
                or int(timestamp) < 0 or int(timestamp) % STEP):
            return {"status": "invalid_ohlc_timestamp", "verified_intervals": 0}
        starts.append(int(timestamp))
    if len(set(starts)) != len(starts):
        return {"status": "duplicate_ohlc_timestamp", "verified_intervals": 0}
    aggregated, buckets = aggregate(trades)
    verified = 0
    for candle, start in zip(archive_rows, starts):
        if start not in aggregated:
            return {"status": "missing_trade_interval", "verified_intervals": verified}
        result = verify_open_boundary(candle, buckets[start], independent_trade_source=True)
        if result["status"] != "verified_open_boundary":
            return {"status": result["status"], "verified_intervals": verified}
        verified += 1
    return {"status": "exact_trade_candle_match", "verified_intervals": verified,
            "timestamp_semantics": "candle_open_utc"}
