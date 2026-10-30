"""Bounded isolated acquisition of original Kraken archive; no unsupported labels.

Uses the exact existing production-isolated inventory downloader, its fixed part
lengths, resource/time caps and SHA256. Never writes production or score outputs.
"""
import argparse
import json
import tempfile
from pathlib import Path
from inventory_kraken_archive import download_verified, resource_gate, EXPECTED_SHA256


def run(output):
    output = Path(output)
    if output.exists():
        raise FileExistsError("refuse overwrite")
    with tempfile.TemporaryDirectory(prefix="kraken-batch9-") as folder:
        archive = Path(folder) / "verified.zip"
        resources = resource_gate(folder)
        identity = download_verified(archive, resources=resources)
        if identity["sha256"] != EXPECTED_SHA256 or not identity["integrity_verified"]:
            raise RuntimeError("unverified archive")
        # Do not infer timestamp semantics from OHLC source itself.
        report = {
            "status": "verified_archive_only_trade_provenance_pending",
            "archive_sha256": identity["sha256"],
            "archive_bytes": identity["bytes"],
            "timestamp_open_verified": False,
            "complete_independent_trade_interval_verified": False,
            "real_historical_labels": 0,
            "horizons": {},
            "production_modified": False,
            "source": "Kraken OHLCVT Full 2026Q2",
            "reason": "independently complete trade-level evidence unavailable; fail closed",
        }
        payload = (json.dumps(report, sort_keys=True) + "\n").encode()
        if len(payload) > 4096:
            raise RuntimeError("report exceeds cap")
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as handle:
            handle.write(payload)
        return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    print(json.dumps(run(parser.parse_args().output), sort_keys=True))
