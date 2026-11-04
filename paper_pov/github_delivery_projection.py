"""Read-only delivery adapter for authenticated GitHub paper-run transport.

The transport verifies GitHub run metadata and file checksums; that alone
never authorizes live WATCH delivery. No ledger writes or scanner dispatches.
"""
import argparse
import json
from .github_sealed_bundle_readback import read_run


def project_delivery(transport):
    if not isinstance(transport, dict):
        raise ValueError("invalid readback")
    run_id = transport.get("source_run_id")
    source_sha = transport.get("source_sha")
    if type(run_id) is not int or run_id <= 0 or not isinstance(source_sha, str) or len(source_sha) != 40 or any(c not in "0123456789abcdef" for c in source_sha.lower()):
        raise ValueError("invalid run provenance")
    if transport.get("watch_delivery_authorized") is not False or transport.get("publisher_authenticated") is not False:
        raise ValueError("unsupported WATCH authorization claim")
    if transport.get("sealed") is True:
        bundle = transport.get("bundle")
        if not isinstance(bundle, dict) or bundle.get("schema") != "paper_sealed_bundle_v1":
            raise ValueError("invalid sealed bundle")
        report = json.loads(bundle["receipt_json"])
        snapshot = bundle.get("candidate_snapshot")
        if not isinstance(report, dict) or not isinstance(snapshot, dict) or snapshot.get("watch") != report.get("watch"):
            raise ValueError("inconsistent candidate snapshot")
        historical_watch_count = len(report["watch"])
        status = "SEALED_HISTORICAL_READ_ONLY"
        coverage = {key: report.get(key) for key in ("eligible_pairs", "matched_tickers", "observed_markets", "ohlc_screened")}
    elif transport.get("sealed") is False and transport.get("artifact_status") == "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT":
        if not isinstance(transport.get("scoreboard"), dict):
            raise ValueError("invalid legacy scoreboard")
        historical_watch_count = None
        status = "LEGACY_CHECKSUM_ONLY"
        coverage = None
    else:
        raise ValueError("unsupported readback")
    return {"schema": "paper_delivery_readback_v1", "source_run_id": run_id,
            "source_sha": source_sha, "status": status, "historical_watch_count": historical_watch_count,
            "historical_coverage": coverage, "live_watch": [], "live_watch_authorized": False,
            "production_applied": False, "single_writer_read_only": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    print(json.dumps(project_delivery(read_run(args.repo, args.run_id)), sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
