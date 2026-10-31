"""Bounded reusable independent Kraken trade-member evidence, research only.

Reads only byte ranges of the official historical trade ZIP. A verified ZIP
member CRC and HTTPS source do NOT authenticate the entire remote archive,
prove all trades were published, or authorize historical labels.
"""
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import re
import urllib.request
import zipfile

from probe_kraken_historical_trade_archive import URL

EXPECTED_BYTES = 1334345194
MAX_TRANSFER = 24 * 1024 * 1024
MAX_REQUEST = 4 * 1024 * 1024
MAX_MEMBER_COMPRESSED = 2 * 1024 * 1024
MAX_MEMBER_BYTES = 3 * 1024 * 1024
MAX_EVIDENCE_BYTES = 12 * 1024 * 1024
MAX_MARKETS = 4


class RangeZipReader(io.RawIOBase):
    """Strict seekable HTTP 206 reader; refuses unbounded GET and byte drift."""
    def __init__(self, url, *, expected_bytes, opener=None, budget=MAX_TRANSFER):
        super().__init__()
        if not url.startswith("https://assets.kraken.com/") or expected_bytes <= 65536:
            raise ValueError("untrusted source or archive length")
        self.url = url
        self.size = expected_bytes
        self.pos = 0
        self.opener = opener or urllib.request.urlopen
        self.budget = budget
        self.transferred = 0
        self.requests = 0
        # A byte-range ZIP reader must not silently splice different remote
        # object revisions into a single apparently valid source archive.
        self._etag = None
        self._last_modified = None
        self._validator_initialized = False

    @property
    def source_validator(self):
        return {"strong_etag": self._etag, "last_modified": self._last_modified,
                "revision_pinned": bool(self._etag or self._last_modified)}

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_END:
            offset += self.size
        elif whence == io.SEEK_CUR:
            offset += self.pos
        elif whence != io.SEEK_SET:
            raise ValueError("unsupported seek")
        if offset < 0 or offset > self.size:
            raise ValueError("range seek outside source")
        self.pos = offset
        return self.pos

    def read(self, size=-1):
        if size is None or size < 0:
            size = self.size - self.pos
        size = min(size, self.size - self.pos)
        if size == 0:
            return b""
        if size > MAX_REQUEST or self.transferred + size > self.budget:
            raise ValueError("remote range request or total transfer cap")
        start, end = self.pos, self.pos + size - 1
        headers = {
            "Range": f"bytes={start}-{end}",
            "Accept-Encoding": "identity",
            "User-Agent": "Cryptoscanner-isolated-range-research/1.0",
        }
        if self._etag or self._last_modified:
            headers["If-Range"] = self._etag or self._last_modified
        req = urllib.request.Request(self.url, headers=headers)
        with self.opener(req, timeout=25) as response:
            if response.status != 206:
                raise RuntimeError("source ignored byte-range request")
            if response.headers.get("Content-Encoding", "identity").lower() != "identity":
                raise RuntimeError("unexpected range content encoding")
            if response.headers.get("Content-Range") != f"bytes {start}-{end}/{self.size}":
                raise RuntimeError("source range or total size changed")
            length = response.headers.get("Content-Length")
            if length is not None and (not length.isdecimal() or int(length) != size):
                raise RuntimeError("source response length changed")
            etag = response.headers.get("ETag")
            # Weak ETags are not strong byte-identity validators.
            strong_etag = etag if etag and not etag.lstrip().startswith("W/") else None
            modified = response.headers.get("Last-Modified")
            if self._validator_initialized:
                if self._etag and strong_etag != self._etag:
                    raise RuntimeError("remote source ETag changed or disappeared")
                if self._last_modified and modified != self._last_modified:
                    raise RuntimeError("remote source Last-Modified changed or disappeared")
                if not self._etag and strong_etag:
                    # Later validators cannot retroactively attest earlier ranges.
                    raise RuntimeError("remote source validator appeared mid-read")
            else:
                self._etag = strong_etag
                self._last_modified = modified
                self._validator_initialized = True
            payload = response.read(size + 1)
        if len(payload) != size:
            raise RuntimeError("truncated or oversized range")
        self.transferred += size
        self.requests += 1
        self.pos += size
        return payload


def _market_names(selection):
    selected = selection.get("selected")
    if not isinstance(selected, list) or len(selected) > 64 or not selected:
        raise ValueError("invalid market selection")
    names = []
    for entry in selected:
        name = entry.get("member") if isinstance(entry, dict) else None
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9]+_5\.csv", name):
            raise ValueError("invalid selected market member")
        names.append(name[:-6] + ".csv")
    if len(set(names)) != len(names):
        raise ValueError("duplicate selected market")
    return names


def _schema(raw):
    reader = csv.reader(io.StringIO(raw.decode("utf-8-sig", errors="strict")))
    lengths = set()
    count = 0
    first = None
    last = None
    monotonic = True
    previous = None
    for row in reader:
        count += 1
        lengths.add(len(row))
        if count > 100000:
            raise ValueError("bounded trade row cap")
        try:
            ts = float(row[0])
            valid = math.isfinite(ts) and ts >= 0
        except (ValueError, IndexError, OverflowError):
            valid = False
        if valid:
            first = ts if first is None else first
            last = ts
            if previous is not None and ts < previous:
                monotonic = False
            previous = ts
        elif count != 1:
            monotonic = False
    return {"rows": count, "column_counts": sorted(lengths),
            "first_numeric_timestamp": first, "last_numeric_timestamp": last,
            "numeric_timestamps_monotonic_candidate": monotonic,
            "official_csv_schema_verified": False}


def collect(selection, *, opener=None, url=URL, expected_bytes=EXPECTED_BYTES,
            budget=MAX_TRANSFER, max_markets=MAX_MARKETS):
    if not 1 <= max_markets <= MAX_MARKETS:
        raise ValueError("invalid market cap")
    wanted = _market_names(selection)
    remote = RangeZipReader(url, expected_bytes=expected_bytes,
                            opener=opener, budget=budget)
    files = {}
    summaries = {}
    with zipfile.ZipFile(remote, "r") as archive:
        infos = archive.infolist()
        if len(infos) > 20000:
            raise ValueError("remote ZIP member cap")
        by_name = {}
        for info in infos:
            if info.filename in by_name:
                raise ValueError("duplicate remote ZIP member")
            by_name[info.filename] = info
        for name in wanted:
            info = by_name.get(name)
            if info is None or info.is_dir():
                continue
            if (info.flag_bits & 1 or info.compress_type not in
                    (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED)
                    or info.compress_size > MAX_MEMBER_COMPRESSED
                    or info.file_size > MAX_MEMBER_BYTES):
                continue
            raw = archive.read(info)  # zipfile verifies CRC32
            if len(raw) != info.file_size:
                raise RuntimeError("incomplete trade ZIP member")
            files[name] = raw
            summaries[name] = {
                "member_bytes": len(raw), "compressed_bytes": info.compress_size,
                "member_sha256": hashlib.sha256(raw).hexdigest(),
                "zip_member_crc32": info.CRC, "schema_observation": _schema(raw),
                "member_crc_verified": True,
                "full_source_archive_sha256_verified": False,
                "independent_trade_interval_completeness_verified": False,
            }
            if len(files) >= max_markets:
                break
    manifest = {
        "schema_version": 1,
        "status": "bounded_independent_trade_members_not_verified_labels"
                  if files else "no_eligible_bounded_trade_members",
        "source_url": url, "source_archive_bytes_expected": expected_bytes,
        "source_archive_full_sha256_verified": False,
        "source_member_crc_checked": bool(files),
        "range_requests": remote.requests,
        "range_bytes_transferred": remote.transferred,
        "source_revision_validator": remote.source_validator,
        "selection_count": len(wanted), "retained_markets": len(files),
        "markets": summaries, "real_labels": 0,
        "held_out_evaluation": "not_authorized",
        "production_modified": False,
    }
    return manifest, files


def write_evidence(path, selection, **kwargs):
    output = Path(path)
    if output.exists():
        raise FileExistsError("refuse evidence overwrite")
    manifest, files = collect(selection, **kwargs)
    with io.BytesIO() as buffer:
        with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, data in sorted(files.items()):
                archive.writestr("trades/" + name, data)
            archive.writestr("manifest.json", json.dumps(manifest, sort_keys=True) + "\n")
        payload = buffer.getvalue()
    if len(payload) > MAX_EVIDENCE_BYTES:
        raise ValueError("retained evidence size cap")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as stream:
        stream.write(payload)
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--selection", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    selection = json.loads(Path(args.selection).read_text(encoding="utf-8"))
    print(json.dumps(write_evidence(args.output, selection), sort_keys=True))
