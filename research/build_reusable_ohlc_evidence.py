"""Bounded, immutable, reusable OHLC research evidence from a verified source ZIP.

Retains source rows, not model labels. Independent trade completeness and
point-in-time feature provenance remain separate fail-closed gates.
"""
import argparse
import csv
from collections import deque
import hashlib
import io
import json
from math import isfinite
from pathlib import Path
import zipfile

MAX_MARKETS = 64
MAX_KEEP_ROWS = 8000
MAX_SOURCE_ROWS = 1500000
MAX_MEMBER_BYTES = 64 * 1024 * 1024
MAX_ARTIFACT_BYTES = 80 * 1024 * 1024
STEP = 300
HORIZONS = (1, 6, 24, 48)


def _entry(name, data, archive):
    info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    archive.writestr(info, data, compresslevel=6)


def _validate(row, previous):
    if len(row) != 7:
        raise ValueError("invalid OHLCVT column count")
    values = [float(v) for v in row]
    if not all(isfinite(v) for v in values):
        raise ValueError("nonfinite OHLCVT")
    ts, opening, high, low, close, volume, count = values
    if (not ts.is_integer() or int(ts) % STEP or (previous is not None and ts <= previous)
            or min(opening, high, low, close) <= 0 or not low <= opening <= high
            or not low <= close <= high or volume < 0 or count < 0 or not count.is_integer()):
        raise ValueError("invalid OHLCVT value or timestamp order")
    return int(ts)


def _market(archive, info, *, keep_rows):
    if info.file_size > MAX_MEMBER_BYTES or info.flag_bits & 1:
        raise ValueError("unsafe or oversized selected member")
    retained = deque(maxlen=keep_rows)
    previous = None
    rows = gaps = missing = current = longest = 0
    with archive.open(info) as raw:
        reader = csv.reader(io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline=""))
        for row in reader:
            rows += 1
            if rows > MAX_SOURCE_ROWS:
                raise ValueError("selected member row cap")
            ts = _validate(row, previous)
            if previous is not None and ts != previous + STEP:
                gaps += 1
                missing += (ts - previous) // STEP - 1
                current = 0
            current += 1
            longest = max(longest, current)
            retained.append(row)
            previous = ts
    if not retained:
        raise ValueError("empty selected member")
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerows(retained)
    payload = stream.getvalue().encode("utf-8")
    return payload, {"source_rows": rows, "source_gap_events": gaps,
                     "source_missing_intervals": missing,
                     "source_longest_contiguous": longest,
                     "retained_rows": len(retained),
                     "retained_first_open": int(float(retained[0][0])),
                     "retained_last_open": int(float(retained[-1][0])),
                     "retained_sha256": hashlib.sha256(payload).hexdigest(),
                     "source_member_crc32": info.CRC,
                     "source_member_bytes": info.file_size}


def build(archive_path, cohort_report, output_path, *, expected_archive_sha256, keep_rows=MAX_KEEP_ROWS):
    if not isinstance(keep_rows, int) or not 577 <= keep_rows <= MAX_KEEP_ROWS:
        raise ValueError("invalid retention cap")
    if (cohort_report.get("archive_sha256") != expected_archive_sha256
            or cohort_report.get("real_labels") != 0):
        raise ValueError("untrusted cohort source or labels")
    selected = cohort_report.get("selected", [])
    names = [x["member"] for x in selected]
    if not 1 <= len(names) <= MAX_MARKETS or len(set(names)) != len(names):
        raise ValueError("invalid selected market count")
    # Standalone SHA verification; no caller assertion can bypass source identity.
    digest = hashlib.sha256()
    with open(archive_path, "rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    if digest.hexdigest() != expected_archive_sha256:
        raise ValueError("source archive SHA256 mismatch")
    output = Path(output_path)
    if output.exists():
        raise FileExistsError("refuse overwrite")
    manifest = {"schema": 1, "source_archive_sha256": expected_archive_sha256,
                "selection": cohort_report["selection"],
                "markets": {}, "source_timestamp_semantics": "candle_open_candidate",
                "independent_trade_completeness": False, "real_labels": 0,
                "held_out_evaluation": "not_authorized"}
    created = False
    try:
        with zipfile.ZipFile(archive_path) as source:
            source_infos = source.infolist()
            if len({x.filename for x in source_infos}) != len(source_infos):
                raise ValueError("duplicate archive member names")
            lookup = {x.filename: x for x in source_infos}
            with output.open("xb") as dest:
                created = True
                with zipfile.ZipFile(dest, "w") as target:
                    for name in names:
                        if ("/" in name or "\\" in name or ".." in name or not name.endswith("_5.csv")
                                or name not in lookup):
                            raise ValueError("unsafe or missing selected market")
                        payload, meta = _market(source, lookup[name], keep_rows=keep_rows)
                        _entry("candles/" + name, payload, target)
                        manifest["markets"][name] = meta
                    _entry("manifest.json", json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode(), target)
        if output.stat().st_size > MAX_ARTIFACT_BYTES:
            raise ValueError("research evidence artifact exceeds cap")
        return manifest
    except BaseException:
        if created:
            output.unlink(missing_ok=True)
        raise


def inspect(path, *, expected_archive_sha256):
    """Verify retained source-row hashes and count candidate horizon windows only."""
    if Path(path).stat().st_size > MAX_ARTIFACT_BYTES:
        raise ValueError("artifact byte cap")
    with zipfile.ZipFile(path) as source:
        infos = source.infolist()
        if len({x.filename for x in infos}) != len(infos) or "manifest.json" not in source.namelist():
            raise ValueError("duplicate or missing artifact manifest")
        manifest = json.loads(source.read("manifest.json"))
        if (manifest.get("schema") != 1 or manifest.get("real_labels") != 0
                or manifest.get("source_archive_sha256") != expected_archive_sha256
                or manifest.get("independent_trade_completeness") is not False):
            raise ValueError("invalid evidence gate")
        markets = manifest.get("markets", {})
        if not 1 <= len(markets) <= MAX_MARKETS or len(infos) != len(markets) + 1:
            raise ValueError("unexpected evidence files")
        results = {}
        for name, meta in markets.items():
            if "/" in name or ".." in name or "\\" in name:
                raise ValueError("unsafe retained member")
            info = source.getinfo("candles/" + name)
            if info.file_size > MAX_MEMBER_BYTES:
                raise ValueError("retained member uncompressed cap")
            payload = source.read(info)
            if hashlib.sha256(payload).hexdigest() != meta["retained_sha256"]:
                raise ValueError("retained source hash mismatch")
            if len(payload) > MAX_MEMBER_BYTES:
                raise ValueError("retained member exceeds cap")
            timestamps = []
            previous = None
            for row in csv.reader(io.StringIO(payload.decode("utf-8"))):
                ts = _validate(row, previous)
                timestamps.append(ts)
                previous = ts
            if len(timestamps) != meta["retained_rows"] or len(timestamps) > MAX_KEEP_ROWS:
                raise ValueError("retained source row count mismatch")
            runs = []
            run = 0
            for i, ts in enumerate(timestamps):
                if i and ts != timestamps[i-1] + STEP:
                    runs.append(run)
                    run = 0
                run += 1
            runs.append(run)
            results[name] = {"retained_rows": len(timestamps),
                             "longest_contiguous": max(runs),
                             "candidate_windows": {str(h): sum(max(0, n - h * 12) for n in runs)
                                                   for h in HORIZONS}}
    return {"status": "reusable_source_evidence_validated_labels_gated",
            "markets": len(results), "coverage": results,
            "independent_trade_completeness": False, "real_labels": 0,
            "held_out_evaluation": "not_authorized"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive")
    parser.add_argument("--cohort")
    parser.add_argument("--output")
    parser.add_argument("--expected-sha256")
    parser.add_argument("--inspect")
    args = parser.parse_args()
    if args.inspect:
        print(json.dumps(inspect(args.inspect, expected_archive_sha256=args.expected_sha256), sort_keys=True))
    else:
        with open(args.cohort, encoding="utf-8") as stream:
            cohort = json.load(stream)
        print(json.dumps(build(args.archive, cohort, args.output,
                               expected_archive_sha256=args.expected_sha256), sort_keys=True))
