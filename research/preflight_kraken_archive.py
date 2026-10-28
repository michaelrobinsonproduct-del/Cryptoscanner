"""Bounded archive acquisition preflight; never assembles or downloads a full archive.

On an isolated runner only. SHA-256 hashes here cover the received range, NOT the
official complete Kraken OHLCVT archive. No archive files or credentials are written.
"""
import argparse
import hashlib
import json
import re
import shutil
import time
import urllib.request
from pathlib import Path

BASE = "https://assets.kraken.com/marketing/institutions/Kraken_OHLCVT_Full_2026Q2.zip.part"
PARTS = 5
RANGE_BYTES = 65536
TOTAL_CAP = PARTS * RANGE_BYTES
MIN_FREE_DISK = 20 * 1024**3
MIN_AVAILABLE_MEMORY = 2 * 1024**3
MAX_PART_BYTES = 3 * 1024**3
TIMEOUT = 12
MAX_SECONDS = 90
EXPECTED_COMPLETE_SHA256 = "fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4"


def available_memory():
    values = Path("/proc/meminfo").read_text().splitlines()
    for line in values:
        if line.startswith("MemAvailable:"):
            return int(line.split()[1]) * 1024
    raise RuntimeError("Cannot determine available memory")


def preflight(disk_free=None, mem_free=None):
    disk = shutil.disk_usage(".").free if disk_free is None else disk_free
    memory = available_memory() if mem_free is None else mem_free
    if disk < MIN_FREE_DISK:
        raise RuntimeError("Insufficient free disk for future full archive acquisition")
    if memory < MIN_AVAILABLE_MEMORY:
        raise RuntimeError("Insufficient available memory")
    return {"free_disk_bytes": disk, "available_memory_bytes": memory}


def acquire(opener=None, clock=None, disk_free=None, mem_free=None):
    capacity = preflight(disk_free, mem_free)
    open_url = opener or urllib.request.urlopen
    now = clock or time.monotonic
    start = now()
    result = []
    for part in range(PARTS):
        if now() - start > MAX_SECONDS:
            raise RuntimeError("Total execution deadline exceeded")
        request = urllib.request.Request(
            BASE + f"{part:02d}",
            headers={"Range": f"bytes=0-{RANGE_BYTES-1}",
                     "User-Agent": "Cryptoscanner-research-capacity-preflight/1.0"},
        )
        with open_url(request, timeout=TIMEOUT) as response:
            if response.status != 206:
                raise RuntimeError(f"Part {part:02d}: HTTP range ignored")
            header = response.headers.get("Content-Range", "")
            match = re.fullmatch(r"bytes 0-65535/([0-9]+)", header)
            if not match:
                raise RuntimeError(f"Part {part:02d}: invalid Content-Range")
            total_size = int(match.group(1))
            if not RANGE_BYTES <= total_size <= MAX_PART_BYTES:
                raise RuntimeError(f"Part {part:02d}: implausible size")
            data = response.read(RANGE_BYTES + 1)
            if len(data) != RANGE_BYTES:
                raise RuntimeError(f"Part {part:02d}: truncated or oversized")
            result.append({"part": part, "part_size_bytes": total_size,
                           "sample_bytes": len(data),
                           "sample_sha256": hashlib.sha256(data).hexdigest()})
    total = sum(item["sample_bytes"] for item in result)
    if total != TOTAL_CAP:
        raise RuntimeError("Unexpected total sample bytes")
    return {"capacity": capacity, "parts": result, "total_sample_bytes": total,
            "archive_sha256_verified": False,
            "official_archive_sha256_expected": EXPECTED_COMPLETE_SHA256,
            "limitations": ["Only the first 65536 bytes of each part were retrieved",
                            "No full-archive SHA-256 verification",
                            "No historical observations or outcomes extracted"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.parse_args()
    print(json.dumps(acquire(), indent=2))
