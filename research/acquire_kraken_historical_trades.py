"""Isolated full Kraken 2026Q2 trade ZIP acquisition and bounded source inventory.

Full-file SHA256 is recorded, not compared with an independently published
digest (none verified yet). Therefore this is NOT authenticated provenance.
No production access or outcome labels.
"""
import argparse
import hashlib
import json
import shutil
import tempfile
import time
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

from probe_kraken_historical_trade_archive import URL

EXPECTED_BYTES = 1334345194
MAX_SECONDS = 45 * 60
MIN_DISK = 6 * 1024**3
MIN_RAM = 2 * 1024**3
MAX_MEMBERS = 20000
MAX_UNCOMPRESSED = 100 * 1024**3
MAX_SINGLE_MEMBER = 4 * 1024**3
CHUNK = 1024 * 1024


def resource_gate(path):
    if shutil.disk_usage(path).free < MIN_DISK:
        raise RuntimeError("insufficient free disk")
    mem = Path("/proc/meminfo").read_text()
    available = next((int(x.split()[1])*1024 for x in mem.splitlines()
                      if x.startswith("MemAvailable:")), 0)
    if available < MIN_RAM:
        raise RuntimeError("insufficient available memory")
    return {"disk_gate": True, "memory_gate": True}


def download(path, opener=None, clock=None):
    opener = opener or urllib.request.urlopen
    clock = clock or time.monotonic
    start = clock()
    sha = hashlib.sha256()
    count = 0
    req = urllib.request.Request(URL, headers={"Accept-Encoding": "identity",
        "User-Agent": "Cryptoscanner-isolated-research/1.0"})
    # Never remove a pre-existing path on exclusive-create failure.
    created = False
    try:
        with open(path, "xb") as out:
            created = True
            with opener(req, timeout=30) as response:
                if response.status != 200 or response.headers.get("Content-Encoding", "identity").lower() != "identity":
                    raise RuntimeError("unexpected archive HTTP response")
                length = response.headers.get("Content-Length")
                if length is None or not length.isdecimal() or int(length) != EXPECTED_BYTES:
                    raise RuntimeError("unexpected archive size")
                while count < EXPECTED_BYTES:
                    if clock() - start >= MAX_SECONDS:
                        raise RuntimeError("archive acquisition timeout")
                    block = response.read(min(CHUNK, EXPECTED_BYTES-count))
                    if not block:
                        raise RuntimeError("truncated archive")
                    count += len(block)
                    out.write(block)
                    sha.update(block)
                if response.read(1):
                    raise RuntimeError("unexpected extra bytes")
        return {"bytes": count, "sha256_observed": sha.hexdigest(),
                "independent_sha256_verified": False}
    except BaseException:
        if created:
            Path(path).unlink(missing_ok=True)
        raise


def inspect(path):
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        if len(infos) > MAX_MEMBERS:
            raise RuntimeError("too many ZIP members")
        total = 0
        members = []
        for info in infos:
            name = info.filename
            p = PurePosixPath(name)
            if (not name or name.startswith("/") or "\\" in name or "\x00" in name
                    or ".." in p.parts or info.flag_bits & 1):
                raise RuntimeError("unsafe ZIP member")
            if info.file_size > MAX_SINGLE_MEMBER:
                raise RuntimeError("oversized ZIP member")
            total += info.file_size
            if total > MAX_UNCOMPRESSED:
                raise RuntimeError("uncompressed ZIP size cap")
            if not info.is_dir():
                members.append({"name": name, "bytes": info.file_size})
        if not members:
            raise RuntimeError("empty archive")
        return {"members": len(members), "uncompressed_bytes": total,
                "sample_members": members[:5], "zip_metadata_checked": True,
                "member_csv_semantics_verified": False}


def run(output):
    output = Path(output)
    if output.exists():
        raise FileExistsError("refuse overwrite")
    with tempfile.TemporaryDirectory(prefix="kraken-trades-") as tmp:
        resource_gate(tmp)
        archive = Path(tmp) / "trades.zip"
        evidence = download(archive)
        evidence.update(inspect(archive))
        evidence.update({"source": URL, "full_archive_acquired": True,
                         "independently_authenticated": False,
                         "exact_trade_to_ohlc_match_verified": False,
                         "real_historical_labels": 0, "held_out_patterns": "not_authorized",
                         "production_modified": False})
        raw = (json.dumps(evidence, sort_keys=True)+"\n").encode()
        if len(raw) > 8192:
            raise RuntimeError("report exceeds cap")
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as f:
            f.write(raw)
        return evidence


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--output", required=True)
    args = p.parse_args()
    print(json.dumps(run(args.output), sort_keys=True))
