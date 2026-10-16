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
import time

MODULES = (
    "simple_scanner.scan",
    "simple_scanner.history",
    "simple_scanner.shadow_learning",
    "simple_scanner.dex_guard",
)
REQUIRED = ("SCAN_SUMMARY", "WATCH_SUMMARY", "HISTORY_PERSISTED", "SHADOW_LEARNING")

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
                for key in (*REQUIRED, "DEX_SUMMARY", "DEX_CACHE_REUSED",
                            "DEX_CIRCUIT_OPEN", "DEX_CIRCUIT_TRIPPED",
                            "DEX_STALE_CACHE", "DEX_SOURCE_ERRORS"):
                    if line.startswith(key + " "):
                        records[key] = line[len(key) + 1:]
            if result.returncode:
                print("SCAN_EXECUTION_FAILED " + json.dumps({
                    "origin": origin, "module": module,
                    "returncode": result.returncode,
                    "stderr_tail": result.stderr[-1200:],
                }), flush=True)
                return result.returncode
        dex_degraded = any(k in records for k in ("DEX_CIRCUIT_OPEN", "DEX_CIRCUIT_TRIPPED", "DEX_STALE_CACHE", "DEX_SOURCE_ERRORS"))
        missing = [k for k in REQUIRED if k not in records]
        dex_ok = any(k in records for k in (
            "DEX_SUMMARY", "DEX_CACHE_REUSED", "DEX_CIRCUIT_OPEN", "DEX_CIRCUIT_TRIPPED", "DEX_STALE_CACHE", "DEX_SOURCE_ERRORS"))
        if missing or not dex_ok:
            print("SCAN_INCOMPLETE " + json.dumps({
                "origin": origin, "missing": missing, "dex_record_present": dex_ok, "dex_degraded": dex_degraded,
            }), flush=True)
            return 1
        summary = json.loads(records["SCAN_SUMMARY"])
        if summary.get("buy_approved") is not False or summary.get("status") != "RESEARCH_ONLY":
            print("SCAN_INVALID_APPROVAL", flush=True)
            return 1
        latest = json.loads((data_dir / "latest.json").read_text())
        if latest.get("completed_at") != summary.get("completed_at"):
            print("SCAN_MISMATCHED_RUN", flush=True)
            return 1
        if dt.datetime.fromisoformat(summary["started_at"]) < started - dt.timedelta(seconds=5):
            print("SCAN_STALE_RUN", flush=True)
            return 1
        print("SCAN_EXECUTION_VERIFIED " + json.dumps({
            "origin": origin, "started_at": summary["started_at"],
            "completed_at": summary["completed_at"], "buy_approved": False,
            "shadow_present": True, "dex_record_present": dex_ok,
            "dex_degraded": dex_degraded,
        }), flush=True)
        return 0

if __name__ == "__main__":
    sys.exit(execute(sys.argv[1] if len(sys.argv) > 1 else "manual"))
