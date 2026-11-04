"""Read-only delivery adapter for authenticated GitHub paper-run transport.

The transport verifies GitHub run metadata and file checksums; that alone
never authorizes live WATCH delivery. No ledger writes or scanner dispatches.
"""
import argparse
import json
from .github_sealed_bundle_readback import read_run


def _writer_evidence(readback):
    """Project D's already-verified recovery report without equating scan cohorts."""
    if not isinstance(readback, dict) or readback.get("status") not in ("WRITER_CHECKSUM_ONLY", "VERIFIED_REMOTE_READBACK"):
        raise ValueError("writer recovery did not succeed")
    if (readback.get("remote_downloaded") is not True or
            readback.get("ledger_writer_invoked") is not False or
            readback.get("production_applied") is not False):
        raise ValueError("writer readback is not read-only")
    independent = readback.get("independently_authenticated")
    if independent is not (readback["status"] == "VERIFIED_REMOTE_READBACK"):
        raise ValueError("writer authentication claim inconsistent")
    run_id, sha = readback.get("run_id"), readback.get("source_sha")
    if not isinstance(run_id, str) or not run_id.isdigit() or int(run_id) <= 0 or not isinstance(sha, str) or len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha.lower()):
        raise ValueError("writer source identity invalid")
    persisted = readback.get("persisted_paper")
    if not isinstance(persisted, dict) or type(persisted.get("ledger_generation")) is not int or persisted["ledger_generation"] < 0 or not isinstance(persisted.get("scan_status"), str) or not persisted["scan_status"] or persisted.get("live_replay_performed") is not False:
        raise ValueError("writer persisted evidence invalid")
    reconciliation = readback.get("remote_ledger_reconciliation")
    status = "UNAVAILABLE"
    if reconciliation is not None:
        if (not isinstance(reconciliation, dict) or reconciliation.get("status") not in ("MATCH", "DIVERGED", "UNAVAILABLE") or reconciliation.get("independently_authenticated") is not False or reconciliation.get("production_applied") is not False):
            raise ValueError("writer reconciliation invalid")
        status = reconciliation["status"]
        if status == "UNAVAILABLE" and reconciliation.get("reason") != "REMOTE_LEDGER_QUERY_FAILED":
            raise ValueError("unexplained remote ledger unavailability")
        if status in ("MATCH", "DIVERGED"):
            import re
            a, z = reconciliation.get("recovered_sha256"), reconciliation.get("remote_sha256")
            if not all(isinstance(d, str) and re.fullmatch(r"[0-9a-f]{64}", d) for d in (a, z)) or (a == z) != (status == "MATCH"):
                raise ValueError("writer reconciliation digest contradiction")
    return {"source_run_id": int(run_id), "source_sha": sha,
            "recovery_status": readback["status"], "ledger_generation": persisted["ledger_generation"],
            "scan_status": persisted["scan_status"], "reconciliation_status": status,
            "independently_authenticated": independent, "same_scan_as_delivery": False,
            "live_watch_authorized": False, "production_applied": False}


def project_delivery(transport, writer_readback=None):
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
    writer = _writer_evidence(writer_readback) if writer_readback is not None else None
    return {"schema": "paper_delivery_readback_v1", "source_run_id": run_id,
            "source_sha": source_sha, "status": status, "historical_watch_count": historical_watch_count,
            "historical_coverage": coverage, "live_watch": [], "live_watch_authorized": False,
            "production_applied": False, "single_writer_read_only": True,\n            "writer_recovery": writer, "writer_reconciliation_status": writer["reconciliation_status"] if writer else "UNAVAILABLE"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    print(json.dumps(project_delivery(read_run(args.repo, args.run_id)), sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
