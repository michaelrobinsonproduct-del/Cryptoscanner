"""Read-only C integration: combine authenticated historical parity and D recovery evidence.

Never turns legacy quote evidence into a certified trade signal.
"""
import argparse
import json
import re
from pathlib import Path


def combine(parity, recovery, snapshot=None):
    if parity.get("status") != "FIXTURE_OR_ARTIFACT_CONTRACT_VERIFIED_NOT_LIVE_PARITY":
        raise ValueError("Unverified parity contract")
    if parity.get("candidate_schema_parity") is not True or parity.get("same_source_sha") is not True:
        raise ValueError("Incompatible historical result schemas")
    if recovery.get("schema") != "paper_recovery_v1" or recovery.get("production_applied") is not False:
        raise ValueError("Invalid recovery receipt")
    runs = recovery.get("runs")
    if not isinstance(runs, dict):
        raise ValueError("Missing recovery runs")
    for name in ("manual", "scheduled"):
        run = runs.get(name)
        if not isinstance(run, dict):
            raise ValueError("Missing " + name + " recovery")
        if str(run.get("run_id")) != str(parity[name + "_run"]):
            raise ValueError("Mismatched " + name + " run identity")
        if run.get("generation") != parity[name + "_generation"] or run.get("watch") != parity[name + "_watch_count"]:
            raise ValueError("Mismatched " + name + " recovered candidates")
        if run.get("certified") is not False:
            raise ValueError("Legacy recovery falsely certified")
    recovered = recovery.get("all_recovered") is True and all(
        runs[n].get("status") == "ABSTAIN_LEGACY_QUOTE_EVIDENCE" for n in ("manual", "scheduled")
    )
    result = {
        "schema": "c_read_only_integration_v1",
        "production_applied": False,
        "historical_artifact_parity": True,
        "recovery_verified": recovered,
        "exchange_event_freshness_verified": False,
        "trading_approved": False,
        "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE" if recovered else "RECOVERY_FAILED",
        "manual_run": str(parity["manual_run"]),
        "scheduled_run": str(parity["scheduled_run"]),
        "manual_watch": parity["manual_watch_count"],
        "scheduled_watch": parity["scheduled_watch_count"],
        "a2_snapshot_attached": False,
    }
    if snapshot is not None:
        if not isinstance(snapshot, dict) or not isinstance(snapshot.get("receipt_sha256"), str) or re.fullmatch(r"[0-9a-f]{64}", snapshot["receipt_sha256"]) is None:
            raise ValueError("Missing A2 immutable receipt provenance")
        if snapshot.get("buy_approved") is True or snapshot.get("production_applied") is True:
            raise ValueError("A2 consumer attempted production approval")
        if not isinstance(snapshot.get("watch"), list) or not snapshot["watch"]:
            raise ValueError("A2 snapshot lacks WATCH candidates")
        if snapshot.get("scan_status") != "WATCH":
            raise ValueError("A2 snapshot has unexpected scan status")
        result["a2_snapshot_attached"] = True
        result["a2_receipt_sha256"] = snapshot["receipt_sha256"]
        result["a2_watch_count"] = len(snapshot["watch"]) if isinstance(snapshot.get("watch"), list) else 0
        # A2 capture and legacy runs are different cohorts; never assert identity or freshness parity.
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--parity", type=Path, required=True)
    parser.add_argument("--recovery", type=Path, required=True)
    parser.add_argument("--a2", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inputs = [json.loads(p.read_text()) for p in (args.parity, args.recovery)]
    snapshot = json.loads(args.a2.read_text()) if args.a2 else None
    result = combine(*inputs, snapshot)
    args.output.write_text(json.dumps(result, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
