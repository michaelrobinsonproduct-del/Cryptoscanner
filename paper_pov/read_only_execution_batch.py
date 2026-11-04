"""Single read-only GitHub batch: focused tests, live WATCH, recovery observation.

No ledger writes, trade calls, workflow dispatches, or production mutation.
A stage failure is retained as evidence and makes the overall batch fail.
"""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

from paper_pov.scanner import scan, atomic_json


def stage(name, action, root):
    try:
        result = action()
        outcome = {"status": "PASS", "result": result}
    except Exception as exc:
        outcome = {"status": "FAIL", "error_type": type(exc).__name__,
                   "reason": str(exc)[:500]}
    atomic_json(root / (name + ".json"), outcome)
    return outcome


def run_tests(root):
    cmd = [sys.executable, "-m", "unittest", "paper_pov.test_missed_slot_recovery",
           "paper_pov.test_replay_downloaded_artifacts", "-v"]
    completed = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    (root / "focused-tests.log").write_text(completed.stdout + completed.stderr)
    if completed.returncode:
        raise RuntimeError("Focused tests failed (see focused-tests.log)")
    return {"test_command": " ".join(cmd), "exit_code": completed.returncode}


def run_live(root):
    report = scan()
    if report.get("mode") != "PAPER_ONLY" or report.get("buy_approved") is not False:
        raise ValueError("Unexpected trading-enabled scan")
    if not report.get("watch"):
        raise ValueError("No eligible WATCH candidates")
    atomic_json(root / "live-watch.json", report)
    return {"as_of": report["as_of"], "watch_count": len(report["watch"]),
            "eligible_pairs": report["eligible_pairs"],
            "observed_markets": report["observed_markets"],
            "quote_provenance": "client_observed_not_exchange_timestamp",
            "ledger_persisted": False, "production_applied": False}


def observe_recovery(root):
    # Observer-only mode is enforced by the existing module CLI contract.
    completed = subprocess.run(
        [sys.executable, "-m", "paper_pov.missed_slot_recovery"],
        capture_output=True, text=True, timeout=60)
    if completed.returncode:
        raise RuntimeError("Recovery observer failed: " + completed.stderr[-400:])
    report = json.loads(completed.stdout)
    if (report.get("writer_dispatched") is not False
            or report.get("ledger_persisted") is not False
            or report.get("production_applied") is not False):
        raise ValueError("Recovery observer attempted mutation")
    return report


def main():
    root = Path(os.getenv("BATCH_OUTPUT_DIR", "batch-evidence"))
    root.mkdir(parents=True, exist_ok=True)
    results = {}
    results["focused_tests"] = stage("focused-tests", lambda: run_tests(root), root)
    results["live_scan"] = stage("live-scan", lambda: run_live(root), root)
    results["recovery_observer"] = stage(
        "recovery-observer", lambda: observe_recovery(root), root)
    status = "PASS" if all(x["status"] == "PASS" for x in results.values()) else "FAIL"
    summary = {
        "schema": 1, "status": status, "stages": results,
        "run_id": os.getenv("GITHUB_RUN_ID", "LOCAL"),
        "source_sha": os.getenv("GITHUB_SHA", "LOCAL"),
        "completed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "production_applied": False, "ledger_persisted": False,
        "historical_learning_completed": False,
    }
    atomic_json(root / "batch-summary.json", summary)
    files = sorted(p for p in root.iterdir() if p.is_file() and p.name != "SHA256SUMS")
    (root / "SHA256SUMS").write_text("".join(
        hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.name + "\n"
        for p in files))
    print("BATCH_SUMMARY " + json.dumps(summary, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
