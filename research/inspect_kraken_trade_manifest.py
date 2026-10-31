"""Bounded official Kraken quarterly trade MANIFEST inspection (research only).

A manifest embedded in the same ZIP is useful provenance metadata, NOT an
independently authenticated archive checksum or proof of complete trade history.
Never authorizes point-in-time labels or production promotion.
"""
import argparse
import hashlib
import json
import stat
import zipfile
from pathlib import Path

from probe_bounded_trade_members import (
    RangeZipReader, EXPECTED_BYTES, _market_names, MAX_MARKETS,
)
from probe_kraken_historical_trade_archive import URL

MAX_MANIFEST_BYTES = 256 * 1024
MAX_ARCHIVE_MEMBERS = 20000
MAX_TRANSFER = 8 * 1024 * 1024
MAX_REPORT_BYTES = 32 * 1024


def retained_trade_market_names(path):
    """Use actual retained trade markets, not the first four requested pairs."""
    path = Path(path)
    if not path.is_file() or path.stat().st_size > 12 * 1024 * 1024:
        raise ValueError("missing or oversized retained trade evidence")
    with zipfile.ZipFile(path) as archive:
        if archive.namelist().count("manifest.json") != 1:
            raise ValueError("invalid retained trade manifest")
        info = archive.getinfo("manifest.json")
        if info.file_size > 128 * 1024 or info.flag_bits & 1:
            raise ValueError("unsafe retained trade manifest")
        obj = json.loads(archive.read(info))
        markets = obj.get("markets") if isinstance(obj, dict) else None
        if not isinstance(markets, dict) or not 1 <= len(markets) <= MAX_MARKETS:
            raise ValueError("invalid retained trade market count")
        for name in markets:
            if (not isinstance(name, str) or not name.endswith(".csv")
                    or "/" in name or "\\\\" in name or ".." in name
                    or archive.namelist().count("trades/" + name) != 1):
                raise ValueError("unsafe or missing retained trade market")
        return sorted(markets)


def inspect_archive(archive, wanted):
    """Inspect ZIP directory and manifest without reading any market CSV."""
    if not isinstance(wanted, (list, tuple)) or len(wanted) > MAX_MARKETS:
        raise ValueError("invalid bounded market selection")
    if len(set(wanted)) != len(wanted):
        raise ValueError("duplicate selected market")
    infos = archive.infolist()
    if not 1 <= len(infos) <= MAX_ARCHIVE_MEMBERS:
        raise ValueError("archive member count cap")
    names = [x.filename for x in infos]
    if len(set(names)) != len(names):
        raise ValueError("duplicate ZIP member names")
    by_name = {x.filename: x for x in infos}
    manifest = by_name.get("MANIFEST.json")
    if manifest is None:
        return {"status": "missing_official_manifest", "manifest_sha256": None,
                "manifest_top_level_keys": [], "selected_members": {}}
    if (manifest.is_dir() or manifest.flag_bits & 1 or
            manifest.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED) or
            manifest.file_size <= 0 or manifest.file_size > MAX_MANIFEST_BYTES or
            manifest.compress_size > MAX_MANIFEST_BYTES or
            stat.S_ISLNK(manifest.external_attr >> 16)):
        raise ValueError("unsafe or oversized official manifest")
    raw = archive.read(manifest)  # CRC verified by zipfile
    if len(raw) != manifest.file_size:
        raise ValueError("manifest byte count mismatch")
    try:
        obj = json.loads(raw.decode("utf-8-sig", errors="strict"))
    except (UnicodeError, ValueError) as exc:
        raise ValueError("invalid official manifest JSON") from exc
    if not isinstance(obj, dict):
        raise ValueError("official manifest must be a JSON object")
    # Report structural metadata only: the archive itself does not attest its
    # contents cryptographically, and unknown manifest keys are not claims.
    metadata = {}
    for name in wanted:
        if not isinstance(name, str) or not name.endswith(".csv") or "/" in name or "\\" in name or ".." in name:
            raise ValueError("unsafe selected member name")
        info = by_name.get(name)
        metadata[name] = ({
            "present": True, "zip_uncompressed_bytes": info.file_size,
            "zip_compressed_bytes": info.compress_size, "zip_crc32": info.CRC,
            "member_full_sha256_verified": False,
        } if info is not None and not info.is_dir() else {"present": False})
    # Surface bounded, *untrusted* manifest structure to determine whether
    # published metadata can support future independent completeness checks.
    def scalar(value):
        if value is None or isinstance(value, (bool, int, float)):
            return value
        if isinstance(value, str) and len(value) <= 128:
            return value
        return {"type": type(value).__name__}

    def shape(value):
        if isinstance(value, dict):
            return {"type": "dict", "count": len(value),
                    "keys": sorted(str(k) for k in value)[:24]}
        if isinstance(value, list):
            return {"type": "list", "count": len(value),
                    "first_item_keys": (sorted(str(k) for k in value[0])[:24]
                                        if value and isinstance(value[0], dict) else [])}
        return {"type": type(value).__name__, "value": scalar(value)}

    summary = {key: shape(obj[key]) for key in
               ("files", "coverage", "columns", "schema_1_differences")
               if key in obj}
    summary["scalars"] = {key: scalar(obj[key]) for key in
                          ("schema_version", "product", "release", "generated",
                           "has_header", "pairs", "rows") if key in obj}
    files = obj.get("files")
    selected_entries = {}
    if isinstance(files, dict):
        for name in wanted:
            if name in files:
                selected_entries[name] = shape(files[name])
                if isinstance(files[name], dict):
                    selected_entries[name]["scalar_fields"] = {
                        str(k): scalar(v) for k, v in files[name].items()
                        if str(k) in ("sha256", "rows", "first", "last", "min_ts",
                                      "max_ts", "size", "bytes", "checksum", "crc32")}
    elif isinstance(files, list):
        for entry in files:
            if not isinstance(entry, dict):
                continue
            name = next((entry[k] for k in ("name", "file", "filename", "path")
                         if isinstance(entry.get(k), str)), None)
            if name in wanted and name not in selected_entries:
                selected_entries[name] = shape(entry)
                selected_entries[name]["scalar_fields"] = {
                    str(k): scalar(v) for k, v in entry.items()
                    if str(k) in ("sha256", "rows", "first", "last", "min_ts",
                                  "max_ts", "size", "bytes", "checksum", "crc32")}
    summary["selected_file_entries"] = selected_entries
    # A quarterly manifest is not a signed completeness statement. Nevertheless
    # reconcile its bounded structural claims against the ZIP central directory.
    listed = set()
    if isinstance(files, dict):
        listed = {k for k in files if isinstance(k, str)}
    elif isinstance(files, list):
        for entry in files:
            if isinstance(entry, str):
                listed.add(entry)
            elif isinstance(entry, dict):
                name = next((entry[k] for k in ("name", "file", "filename", "path")
                             if isinstance(entry.get(k), str)), None)
                if name:
                    listed.add(name)
    pair_count = obj.get("pairs")
    # Kraken's observed 2026Q2 schema uses scalar "files": 1399,
    # not a per-file list. Do not turn absent listing into false missing
    # members or claim that a matching count proves complete trades.
    declared_count = (len(files) if isinstance(files, (dict, list))
                      else files if type(files) is int and
                      0 <= files <= MAX_ARCHIVE_MEMBERS else None)
    listing_available = isinstance(files, (dict, list))
    zip_csv_count = sum(x.filename.endswith(".csv") and not x.is_dir()
                        for x in infos)
    structural = {
        "manifest_file_count": declared_count,
        "manifest_pair_count": pair_count if type(pair_count) is int else None,
        "file_count_matches_pair_count": (
            declared_count == pair_count if declared_count is not None
            and type(pair_count) is int else None),
        "zip_csv_member_count": zip_csv_count,
        "manifest_file_count_matches_zip_csv_count": (
            declared_count == zip_csv_count if declared_count is not None else None),
        "manifest_per_file_listing_available": listing_available,
        "listed_selected_members": {
            name: name in listed if listing_available else None for name in wanted},
        "selected_members_present_in_zip": {
            name: name in by_name and not by_name[name].is_dir() for name in wanted},
        "listed_selected_members_in_zip": {
            name: name in by_name and name in listed if listing_available else None
            for name in wanted},
        "source_authenticated": False,
        "complete_trade_intervals_verified": 0,
    }
    coverage = obj.get("coverage")
    if isinstance(coverage, dict):
        structural["coverage_fields"] = {
            key: scalar(coverage[key]) for key in ("start", "end")
            if key in coverage}
    summary["structural_consistency"] = structural
    return {
        "status": "official_manifest_structurally_inspected_not_authenticated",
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "manifest_bytes": len(raw),
        "manifest_top_level_keys": sorted(str(k) for k in obj)[:64],
        "manifest_top_level_key_count": len(obj),
        "manifest_schema_summary": summary,
        "selected_members": metadata,
    }


def probe(selection, *, opener=None, url=URL, expected_bytes=EXPECTED_BYTES, retained_trade_evidence=None):
    wanted = (retained_trade_market_names(retained_trade_evidence)
              if retained_trade_evidence is not None else _market_names(selection)[:MAX_MARKETS])
    remote = RangeZipReader(url, expected_bytes=expected_bytes,
                            opener=opener, budget=MAX_TRANSFER)
    with zipfile.ZipFile(remote) as archive:
        result = inspect_archive(archive, wanted)
    result.update({
        "source_url": url,
        "source_expected_archive_bytes": expected_bytes,
        "range_bytes_transferred": remote.transferred,
        "range_requests": remote.requests,
        "source_revision_validator": remote.source_validator,
        "source_archive_full_sha256_verified": False,
        "independent_trade_interval_completeness_verified": False,
        "source_manifest_independently_authenticated": False,
        "real_labels": 0,
        "held_out_evaluation": "not_authorized",
        "production_modified": False,
    })
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selection", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--retained-trades")
    args = ap.parse_args()
    selection = json.loads(Path(args.selection).read_text())
    report = probe(selection, retained_trade_evidence=args.retained_trades)
    payload = (json.dumps(report, sort_keys=True) + "\n").encode()
    if len(payload) > MAX_REPORT_BYTES:
        raise ValueError("manifest report exceeds cap")
    path = Path(args.output)
    if path.exists():
        raise FileExistsError("refuse to overwrite existing report")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(payload)
    print(json.dumps({"status": report["status"],
                      "manifest_sha256": report["manifest_sha256"],
                      "range_bytes_transferred": report["range_bytes_transferred"],
                      "real_labels": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
