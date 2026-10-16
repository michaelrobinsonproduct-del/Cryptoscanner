"""Shared, fail-closed execution wrapper for future cron and manual invocation.

This file is NOT wired to production. It must run inside the existing volume
mount, never from a second service with its own independent SQLite history.
"""
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys

MODULES = (
    "simple_scanner.scan",
    "simple_scanner.history",
    "simple_scanner.shadow_learning",
    "simple_scanner.dex_guard",
)
REQUIRED = ("SCAN_SUMMARY", "WATCH_SUMMARY", "HISTORY_PERSISTED")

def execute(origin="manual"):
    if origin not in ("manual", "cron"):
        raise ValueError("Invalid origin")
    data_dir = Path(os.environ.get("SIMPLE_SCANNER_DATA_DIR", "simple_scanner/output"))
    data_dir.mkdir(parents=True, exist_ok=True)
    lock_path = data_dir / "scan_execution.lock"
    with lock_path.open("a+") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("SCAN_BUSY " + json.dumps({"origin": origin}), flush=True)
            return 75
        started = dt.datetime.now(dt.timezone.utc)
        records = {}
        for module in MODULES:
            try:
                result = subprocess.run(
                    [sys.executable, "-m", module],
                    capture_output=True, text=True, timeout=240,
                    env=os.environ.copy(),
                )
            except subprocess.TimeoutExpired:
                print("SCAN_EXECUTION_TIMEOUT " + json.dumps({"module": module}), flush=True)
                return 124
            for line in result.stdout.splitlines():
                print(line, flush=True)
                for key in (*REQUIRED, "SHADOW_LEARNING", "DEX_SUMMARY", "DEX_CACHE_REUSED",
                            "DEX_CIRCUIT_OPEN", "DEX_CIRCUIT_TRIPPED",
                            "DEX_STALE_CACHE", "DEX_SOURCE_ERRORS"):
                    if line == key or line.startswith(key + " "):
                        records[key] = line[len(key):].strip()
            if result.returncode and module == "simple_scanner.shadow_learning":
                print("SHADOW_LEARNING_PARTIAL_FAILURE", flush=True)
                continue
            if result.returncode:
                print("SCAN_EXECUTION_FAILED " + json.dumps({
                    "origin": origin, "module": module,
                    "returncode": result.returncode,
                    "stderr_tail": result.stderr[-1200:],
                }), flush=True)
                return result.returncode
        dex_degraded = any(k in records for k in ("DEX_CIRCUIT_OPEN", "DEX_CIRCUIT_TRIPPED", "DEX_STALE_CACHE", "DEX_SOURCE_ERRORS"))
        shadow_ok = "SHADOW_LEARNING" in records
        if shadow_ok:
            try:
                shadow_record = json.loads(records["SHADOW_LEARNING"])
                shadow_ok = isinstance(shadow_record, dict) and shadow_record.get("mode") == "SHADOW_ONLY" and shadow_record.get("live_weights_modified") is False
            except (ValueError, TypeError):
                shadow_ok = False
        missing = [k for k in REQUIRED if k not in records]
        dex_ok = any(k in records for k in (
            "DEX_SUMMARY", "DEX_CACHE_REUSED", "DEX_CIRCUIT_OPEN", "DEX_CIRCUIT_TRIPPED", "DEX_STALE_CACHE", "DEX_SOURCE_ERRORS"))
        if missing or not dex_ok:
            print("SCAN_INCOMPLETE " + json.dumps({
                "origin": origin, "missing": missing, "dex_record_present": dex_ok, "dex_degraded": dex_degraded,
            }), flush=True)
            return 1
        try:
            summary = json.loads(records["SCAN_SUMMARY"])
            latest = json.loads((data_dir / "latest.json").read_text())
        except (ValueError, OSError) as exc:
            print("SCAN_INVALID_OUTPUT " + json.dumps({"reason": str(exc)[:240]}), flush=True)
            return 1
        if not isinstance(summary, dict) or not isinstance(latest, dict):
            print("SCAN_INVALID_OUTPUT_SCHEMA", flush=True)
            return 1
        if summary.get("buy_approved") is not False or summary.get("status") != "RESEARCH_ONLY":
            print("SCAN_INVALID_APPROVAL", flush=True)
            return 1
        if latest.get("buy_approved") is not False or latest.get("status") != "RESEARCH_ONLY":
            print("SCAN_INVALID_PERSISTED_APPROVAL", flush=True)
            return 1
        if latest.get("completed_at") != summary.get("completed_at"):
            print("SCAN_MISMATCHED_RUN", flush=True)
            return 1
        try:
            scan_started = dt.datetime.fromisoformat(summary["started_at"])
            scan_completed = dt.datetime.fromisoformat(summary["completed_at"])
            if scan_started.tzinfo is None or scan_completed.tzinfo is None:
                raise ValueError("scan timestamps must include timezone")
        except (ValueError, KeyError, TypeError) as exc:
            print("SCAN_INVALID_TIMESTAMP " + json.dumps({"reason": str(exc)[:240]}), flush=True)
            return 1
        if scan_started < started - dt.timedelta(seconds=5) or scan_started > scan_completed or scan_completed > dt.datetime.now(dt.timezone.utc) + dt.timedelta(seconds=5):
            print("SCAN_STALE_RUN", flush=True)
            return 1
        print("SCAN_EXECUTION_VERIFIED " + json.dumps({
            "origin": origin, "started_at": summary["started_at"],
            "completed_at": summary["completed_at"], "buy_approved": False,
            "shadow_present": shadow_ok, "dex_record_present": dex_ok,
            "dex_degraded": dex_degraded,
        }), flush=True)
        return 0

if __name__ == "__main__":
    sys.exit(execute(sys.argv[1] if len(sys.argv) > 1 else "manual"))
