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
    return {
        "status": "official_manifest_structurally_inspected_not_authenticated",
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "manifest_bytes": len(raw),
        "manifest_top_level_keys": sorted(str(k) for k in obj)[:64],
        "manifest_top_level_key_count": len(obj),
        "selected_members": metadata,
    }


def probe(selection, *, opener=None, url=URL, expected_bytes=EXPECTED_BYTES):
    wanted = _market_names(selection)[:MAX_MARKETS]
    remote = RangeZipReader(url, expected_bytes=expected_bytes,
                            opener=opener, budget=MAX_TRANSFER)
    with zipfile.ZipFile(remote) as archive:
        result = inspect_archive(archive, wanted)
    result.update({
        "source_url": url,
        "source_expected_archive_bytes": expected_bytes,
        "range_bytes_transferred": remote.transferred,
        "range_requests": remote.requests,
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
    args = ap.parse_args()
    selection = json.loads(Path(args.selection).read_text())
    report = probe(selection)
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
