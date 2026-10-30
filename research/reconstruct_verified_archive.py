"""Isolated, bounded, read-only reconstruction from a preverified Kraken ZIP.

This module NEVER downloads data, accesses production or writes outputs.
The caller must independently establish source archive SHA256 and timestamp
semantics; a matching SHA is checked here before reading any member.
"""
import csv
import hashlib
import io
import math
import zipfile
from pathlib import Path
from reconstruct_forward_outcomes import Candle, reconstruct_as_of

ARCHIVE_SHA256 = "fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4"
MAX_MEMBER_BYTES = 64 * 1024 * 1024
MAX_ROWS = 200000
MAX_ARCHIVE_BYTES = 9_000_000_000


def reconstruct_member(archive_path, member_name, observation_as_of, *,
                       archive_sha256=ARCHIVE_SHA256, verified_timestamp_semantics=False,
                       min_quote_volume=None):
    """Read one bounded 5m CSV, fail closed on unverifiable source provenance.

    Kraken OHLCVT field 5 is base volume, not quote volume. Quote liquidity
    estimated as close * base volume is only a proxy, not executed quote value.
    No results are returned unless independently confirmed candle-open
    semantics are explicitly supplied.
    """
    if not verified_timestamp_semantics:
        return {"status": "unverified_source_timestamp_semantics", "horizons": {}}
    if archive_sha256 != ARCHIVE_SHA256:
        raise ValueError("archive identity mismatch")
    p = Path(archive_path)
    if not p.is_file() or p.stat().st_size > MAX_ARCHIVE_BYTES:
        raise ValueError("archive missing or exceeds cap")
    digest = hashlib.sha256()
    with p.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    if digest.hexdigest() != ARCHIVE_SHA256:
        raise ValueError("archive SHA256 mismatch")
    if not member_name.endswith("_5.csv") or "/" in member_name or "\\" in member_name:
        raise ValueError("invalid member name")
    with zipfile.ZipFile(p) as z:
        matching = [info for info in z.infolist() if info.filename == member_name]
        if len(matching) != 1 or matching[0].file_size > MAX_MEMBER_BYTES:
            raise ValueError("missing, duplicate or oversized member")
        rows = []
        with z.open(matching[0]) as raw:
            for record in csv.reader(io.TextIOWrapper(raw, encoding="utf-8", newline="")):
                if not record:
                    continue
                if len(rows) >= MAX_ROWS or len(record) < 7:
                    raise ValueError("row limit or invalid source fields")
                t = float(record[0])
                high, close, volume = map(float, (record[2], record[4], record[5]))
                if not math.isfinite(t) or not t.is_integer():
                    raise ValueError("invalid source timestamp")
                rows.append(Candle(int(t), high, close, volume))
    return reconstruct_as_of(rows, observation_as_of,
                             source_timestamp_semantics="candle_open_utc",
                             min_quote_volume=min_quote_volume)
