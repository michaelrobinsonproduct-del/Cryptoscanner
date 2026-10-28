"""Research-only Kraken multipart archive integrity and full 5m CSV inventory.

Never contacts production. Only a small inventory JSON may survive the temporary ZIP.
No historical features or outcome labels are inferred from this inventory.
"""
import argparse
import csv
import hashlib
import io
import json
import math
import os
from pathlib import Path, PurePosixPath
import shutil
import tempfile
import time
import urllib.request
import zipfile

BASE = "https://assets.kraken.com/marketing/institutions/Kraken_OHLCVT_Full_2026Q2.zip.part"
SIZES = (2097152000, 2097152000, 2097152000, 2097152000, 583772104)
EXPECTED_SHA256 = "fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4"
MIN_DISK = 25 * 1024**3
MIN_MEMORY = 2 * 1024**3
MIN_REMAINING_DISK = 10 * 1024**3
MAX_SECONDS = 50 * 60
MAX_ZIP_MEMBERS = 20000
MAX_UNCOMPRESSED_BYTES = 120 * 1024**3
MAX_MEMBER_BYTES = 8 * 1024**3
MAX_MANIFEST_BYTES = 10 * 1024**2
CHUNK = 1024 * 1024


def resource_gate(path, memory=None):
    free = shutil.disk_usage(path).free
    if memory is None:
        lines = Path("/proc/meminfo").read_text().splitlines()
        memory = next((int(line.split()[1]) * 1024 for line in lines if line.startswith("MemAvailable:")), 0)
    if free < MIN_DISK or free - sum(SIZES) < MIN_REMAINING_DISK:
        raise RuntimeError("insufficient disk for bounded archive acquisition")
    if memory < MIN_MEMORY:
        raise RuntimeError("insufficient memory")
    return {"disk_free_bytes": free, "available_memory_bytes": memory}


def download_verified(path, opener=None, clock=None, resources=None):
    """Write exactly one temporary archive; never return an unverified path."""
    opener = opener or urllib.request.urlopen
    clock = clock or time.monotonic
    if resources is None:
        resources = resource_gate(path.parent)
    started = clock()
    digest = hashlib.sha256()
    count = 0
    try:
        with open(path, "xb") as out:
            for i, expected in enumerate(SIZES):
                if clock() - started >= MAX_SECONDS:
                    raise RuntimeError("archive acquisition deadline")
                req = urllib.request.Request(BASE + f"{i:02d}", headers={"Accept-Encoding": "identity", "User-Agent": "Cryptoscanner-research-inventory/1.0"})
                with opener(req, timeout=25) as response:
                    if response.status != 200:
                        raise RuntimeError("unexpected archive HTTP status")
                    length = response.headers.get("Content-Length")
                    if length is None or not length.isdecimal() or int(length) != expected:
                        raise RuntimeError("archive Content-Length mismatch")
                    if response.headers.get("Content-Encoding", "identity").lower() != "identity":
                        raise RuntimeError("unexpected archive encoding")
                    part_count = 0
                    while part_count < expected:
                        if clock() - started >= MAX_SECONDS:
                            raise RuntimeError("archive acquisition deadline")
                        block = response.read(min(CHUNK, expected - part_count))
                        if not block:
                            raise RuntimeError("truncated archive part")
                        part_count += len(block)
                        count += len(block)
                        if part_count > expected or count > sum(SIZES):
                            raise RuntimeError("archive byte cap exceeded")
                        out.write(block)
                        digest.update(block)
                    if response.read(1):
                        raise RuntimeError("extra archive part bytes")
        if count != sum(SIZES) or digest.hexdigest() != EXPECTED_SHA256:
            raise RuntimeError("full archive SHA256 mismatch")
        return {"sha256": digest.hexdigest(), "bytes": count, "integrity_verified": True, "resources": resources}
    except BaseException:
        path.unlink(missing_ok=True)
        raise


def safe_member(info):
    name = info.filename
    path = PurePosixPath(name)
    if not name or name.startswith("/") or "\\" in name or "\x00" in name or any(x == ".." for x in path.parts):
        raise RuntimeError("unsafe archive member name")
    if info.flag_bits & 1:
        raise RuntimeError("encrypted archive member")
    if info.file_size < 0 or info.file_size > MAX_MEMBER_BYTES:
        raise RuntimeError("archive member exceeds size cap")
    if info.is_dir():
        return False
    if not name.endswith("_5.csv"):
        return False
    return True


def inventory_member(archive, info, clock, started):
    """Read all source rows and CRC; no unbounded per-market row retention."""
    rows = invalid = duplicates = nonmonotonic = gaps = 0
    earliest = latest = previous = None
    with archive.open(info) as raw, io.TextIOWrapper(raw, encoding="utf-8", newline="", errors="strict") as stream:
        for record in csv.reader(stream):
            if clock() - started >= MAX_SECONDS:
                raise RuntimeError("archive inventory deadline")
            if not record:
                continue
            rows += 1
            try:
                if len(record) < 7:
                    raise ValueError("too few fields")
                t = float(record[0])
                o, hi, lo, close, volume, trades = map(float, record[1:7])
                if not all(math.isfinite(v) for v in (t, o, hi, lo, close, volume, trades)):
                    raise ValueError("nonfinite")
                if not t.is_integer() or int(t) % 300 != 0:
                    raise ValueError("timestamp alignment")
                if min(o, hi, lo, close) <= 0 or lo > hi or not lo <= o <= hi or not lo <= close <= hi or volume < 0 or trades < 0:
                    raise ValueError("invalid OHLCVT")
                timestamp = int(t)
            except (ValueError, TypeError, OverflowError):
                invalid += 1
                continue
            earliest = timestamp if earliest is None else min(earliest, timestamp)
            latest = timestamp if latest is None else max(latest, timestamp)
            if previous is not None:
                if timestamp == previous:
                    duplicates += 1
                elif timestamp < previous:
                    nonmonotonic += 1
                elif timestamp - previous > 300:
                    gaps += 1
            previous = timestamp
    return {"member": info.filename, "rows": rows, "invalid_rows": invalid, "adjacent_duplicates": duplicates,
            "out_of_order_rows": nonmonotonic, "gap_intervals": gaps, "earliest_epoch": earliest, "latest_epoch": latest,
            "uncompressed_bytes": info.file_size, "crc_checked": True}


def inspect_archive(path, clock=None):
    clock = clock or time.monotonic
    started = clock()
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        if not infos or len(infos) > MAX_ZIP_MEMBERS:
            raise RuntimeError("archive member count outside cap")
        total_uncompressed = sum(i.file_size for i in infos)
        if total_uncompressed > MAX_UNCOMPRESSED_BYTES:
            raise RuntimeError("archive uncompressed size exceeds cap")
        selected = [info for info in infos if safe_member(info)]
        if not selected:
            raise RuntimeError("no Kraken 5-minute CSV members")
        if len({i.filename for i in selected}) != len(selected):
            raise RuntimeError("duplicate 5-minute archive member name")
        results = [inventory_member(archive, info, clock, started) for info in selected]
    return {"source": "Kraken OHLCVT Full 2026Q2", "archive_members": len(infos),
            "five_minute_members": len(selected), "declared_uncompressed_bytes": total_uncompressed,
            "five_minute_csv_inventory": results, "historical_features_validated": False,
            "future_outcomes_validated": False, "full_year_coverage_validated": False,
            "production_ingested": False, "duplicate_detection_scope": "adjacent only; out-of-order rows counted"}


def run(output):
    if output.exists():
        raise FileExistsError("refusing to overwrite existing inventory")
    with tempfile.TemporaryDirectory(prefix="kraken-inventory-") as tmp:
        temp_path = Path(tmp) / "verified.zip"
        resources = resource_gate(tmp)
        verification = download_verified(temp_path, resources=resources)
        inventory = inspect_archive(temp_path)
        inventory["archive_verification"] = verification
        payload = (json.dumps(inventory, sort_keys=True, separators=(",", ":")) + "\n").encode()
        if len(payload) > MAX_MANIFEST_BYTES:
            raise RuntimeError("inventory manifest exceeds artifact cap")
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as dest:
            dest.write(payload)
    return {"manifest": str(output), "five_minute_members": inventory["five_minute_members"], "archive_sha256_verified": True,
            "historical_features_validated": False, "future_outcomes_validated": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="research/output/kraken_archive_inventory.json")
    print(json.dumps(run(Path(parser.parse_args().output)), sort_keys=True))
