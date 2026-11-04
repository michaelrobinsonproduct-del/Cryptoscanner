"""Strict, explicit-schema Kraken historical trade CSV adapter.

The official archive can vary by release. Caller MUST specify column mapping
and timestamp units from a separately authenticated schema manifest. No
guessing based on numeric magnitude or file names.
"""
import csv
import datetime as dt
import io
import math
from .verified_trade_bars import trades_to_bars, convert_verified_partition
from .archive_partition_gate import verify_partitions
from pathlib import Path

UTC = dt.timezone.utc
UNITS = {"seconds": 1, "milliseconds": 1000, "microseconds": 1000000, "nanoseconds": 1000000000}


def parse_trade_csv(raw, *, pair, schema):
    if schema.get("format") != "kraken_trade_csv_explicit_v1":
        raise ValueError("Missing explicit trade schema")
    unit = schema.get("timestamp_unit")
    if unit not in UNITS:
        raise ValueError("Unknown timestamp unit")
    fields = schema.get("columns")
    if not isinstance(fields, dict) or set(fields) != {"timestamp", "price", "volume"}:
        raise ValueError("Missing exact column mapping")
    if any(type(v) is not int or v < 0 for v in fields.values()) or len(set(fields.values())) != 3:
        raise ValueError("Invalid column indices")
    if schema.get("header") not in (True, False) or type(schema.get("header")) is not bool:
        raise ValueError("Explicit header flag required")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeError as exc:
        raise ValueError("Trade CSV is not UTF-8") from exc
    rows = csv.reader(io.StringIO(text, newline=""))
    trades = []
    expected_width = schema.get("column_count")
    if type(expected_width) is not int or expected_width <= max(fields.values()):
        raise ValueError("Invalid column count")
    for line, row in enumerate(rows):
        if line == 0 and schema["header"]:
            if len(row) != expected_width:
                raise ValueError("Header width mismatch")
            continue
        if not row:
            continue
        if len(row) != expected_width:
            raise ValueError("Trade row width mismatch")
        try:
            timestamp = float(row[fields["timestamp"]])
            if not math.isfinite(timestamp) or timestamp < 0:
                raise ValueError("Invalid timestamp")
            at = dt.datetime.fromtimestamp(timestamp / UNITS[unit], UTC)
            price = float(row[fields["price"]])
            volume = float(row[fields["volume"]])
        except (ValueError, OverflowError, OSError) as exc:
            raise ValueError("Invalid trade CSV row") from exc
        trades.append({"pair": pair, "timestamp": at.isoformat(),
                       "price": price, "volume": volume})
    return trades


def convert_pinned_csv(manifest, root, *, partition_file, pair, schema):
    """Read the pinned file after verification and aggregate to five-minute bars."""
    receipt = verify_partitions(manifest, root)
    matched = [p for p in receipt["partitions"] if p["file"] == partition_file]
    if len(matched) != 1:
        raise ValueError("Partition not in pinned manifest")
    base = Path(root).resolve(strict=True)
    path = (base / partition_file).resolve(strict=True)
    if not path.is_relative_to(base):
        raise ValueError("Unsafe partition")
    trades = parse_trade_csv(path.read_bytes(), pair=pair, schema=schema)
    result = convert_verified_partition(trades, pair=pair, verification=receipt,
                                        partition_file=partition_file)
    result["format"] = "kraken_trade_csv_explicit_v1"
    result["parsed_trade_count"] = len(trades)
    result["schema_authenticated"] = False
    return result
