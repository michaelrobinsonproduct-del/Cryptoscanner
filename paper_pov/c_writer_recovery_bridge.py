"""Read-only bridge between C historical WATCH replay and D's restored real writer.

The C A2 capture and D paper-writer run are different cohorts. This module
publishes both without falsely claiming candidate or timestamp equality.
"""
import argparse
import json
from pathlib import Path

from paper_pov.c_candidate_handoff import consume, from_integration


def bridge(integration, readback, *, restored_latest=None):
    replay = consume(from_integration(integration))
    if not isinstance(readback, dict) or readback.get("status") not in (
        "WRITER_CHECKSUM_ONLY", "VERIFIED_REMOTE_READBACK"
    ):
        raise ValueError("D writer recovery has not succeeded")
    if readback.get("remote_downloaded") is not True or readback.get("ledger_writer_invoked") is not False:
        raise ValueError("D report is not a read-only remote recovery")
    if readback.get("production_applied") is not False:
        raise ValueError("D recovery changed production")
    run_id = readback.get("run_id")
    sha = readback.get("source_sha")
    if not isinstance(run_id, str) or not run_id.isdigit() or not isinstance(sha, str) or len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
        raise ValueError("D run identity missing")
    independent = readback.get("independently_authenticated")
    if independent is not (readback["status"] == "VERIFIED_REMOTE_READBACK"):
        raise ValueError("D independent verification status inconsistent")
    if restored_latest is not None:
        if not isinstance(restored_latest, dict):
            raise ValueError("Restored writer latest is not JSON object")
        # The writer's output is retained as separate provenance, not used to
        # fabricate parity with the historical A2 candidate cohort.
        if restored_latest.get("production_applied") is True or restored_latest.get("trading_approved") is True:
            raise ValueError("Restored writer report claims trading/production")
    persisted = readback.get("persisted_paper")
    if persisted is not None and (not isinstance(persisted, dict) or not isinstance(persisted.get("ledger_generation"), int) or not isinstance(persisted.get("scan_status"), str)):
        raise ValueError("D persisted writer evidence malformed")
    reconciliation = readback.get("remote_ledger_reconciliation")
    if reconciliation is not None and (not isinstance(reconciliation, dict) or reconciliation.get("status") not in ("MATCH", "DIVERGED", "UNAVAILABLE") or reconciliation.get("independently_authenticated") is not False):
        raise ValueError("D remote ledger comparison malformed")
    # A recovered historical receipt does not imply D persisted a paper ledger.
    # Keep replay usable while making the missing B writer prerequisite explicit.
    writer_delivery_ready = (
        readback["status"] == "VERIFIED_REMOTE_READBACK"
        and independent is True
        and isinstance(persisted, dict)
        and type(persisted.get("ledger_generation")) is int
        and persisted["ledger_generation"] >= 0
        and isinstance(persisted.get("scan_status"), str)
        and bool(persisted["scan_status"])
        and persisted.get("live_replay_performed") is False
        # A restored historical writer artifact is NOT sufficient to export a
        # current delivery receipt if the remote ledger has since diverged or
        # the independent reconciliation could not be completed.
        and isinstance(reconciliation, dict)
        and reconciliation.get("status") == "MATCH"
    )
    result = {
        "schema": "c_d_recovered_writer_bridge_v1",
        "status": "READ_ONLY_COHORTS_CONNECTED_NOT_LIVE",
        "historical_a2": replay,
        "writer_recovery": {
            "run_id": run_id,
            "source_sha": sha,
            "status": readback["status"],
            "independently_authenticated": independent,
            "artifact_id": readback.get("artifact_id"),
            "restored_latest_available": restored_latest is not None,
            "persisted_paper": persisted,
            "delivery_projection_ready": writer_delivery_ready,
            "delivery_blocker": (
                None if writer_delivery_ready else
                "D_REMOTE_READBACK_NOT_INDEPENDENTLY_AUTHENTICATED"
                if not independent else "D_REMOTE_LEDGER_RECONCILIATION_NOT_MATCH"
                if isinstance(reconciliation, dict) and reconciliation.get("status") != "MATCH"
                else "D_REMOTE_LEDGER_RECONCILIATION_MISSING"
                if reconciliation is None and isinstance(persisted, dict)
                else "D_PERSISTED_PAPER_MISSING_OR_INCOMPLETE"
            ),
            "remote_ledger_reconciliation": reconciliation,
        },
        "same_run_or_candidate_parity_claimed": False,
        "live_watch_certified": False,
        "trading_approved": False,
        "production_applied": False,
    }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--integration", type=Path, required=True)
    parser.add_argument("--readback", type=Path, required=True)
    parser.add_argument("--restored-latest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--bd-output", type=Path, help="Write B/D replay payload alongside recovered writer provenance")
    parser.add_argument("--writer-readback-output", type=Path, help="Export D readback for B delivery projection")
    args = parser.parse_args()
    result = bridge(
        json.loads(args.integration.read_text()),
        json.loads(args.readback.read_text()),
        restored_latest=json.loads(args.restored_latest.read_text()) if args.restored_latest else None,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True) + "\n")
    if args.writer_readback_output:
        # B requires persisted ledger evidence; never export a checksum-only D
        # report as a ready-to-consume delivery projection.
        if result["writer_recovery"]["delivery_projection_ready"]:
            args.writer_readback_output.parent.mkdir(parents=True, exist_ok=True)
            args.writer_readback_output.write_text(json.dumps(json.loads(args.readback.read_text()), sort_keys=True) + "\n")
        else:
            # Do not leave an earlier successful export at this path.
            args.writer_readback_output.unlink(missing_ok=True)
    if args.bd_output:
        args.bd_output.parent.mkdir(parents=True, exist_ok=True)
        args.bd_output.write_text(json.dumps(result["historical_a2"], sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "historical_watch": result["historical_a2"]["watch_count"], "writer_run": result["writer_recovery"]["run_id"], "writer_delivery_ready": result["writer_recovery"]["delivery_projection_ready"], "writer_delivery_blocker": result["writer_recovery"]["delivery_blocker"]}, sort_keys=True))


if __name__ == "__main__":
    main()
