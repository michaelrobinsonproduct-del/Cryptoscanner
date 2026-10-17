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
        # Optional mailbox check, inside the shared lock. Failure cannot block cron.
        manual_pending = []
        if origin in ("cron", "manual") and os.environ.get("SIMPLE_SCANNER_GITHUB_TOKEN"):
            try:
                from .manual_requests import fetch_requests, read_ledger, plan_requests
                state = read_ledger(data_dir)
                if state.get("ledger_valid") is not False:
                    manual_pending = plan_requests(fetch_requests(), state, started)
                else:
                    print("MANUAL_REQUEST_LEDGER_INVALID", flush=True)
            except Exception as exc:
                print("MANUAL_REQUEST_CHECK_FAILED " + json.dumps({"error": type(exc).__name__}), flush=True)
        records = {}
        shadow_failed = False
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
                shadow_failed = True
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
        dex_fresh = False
        dex_key = "DEX_SUMMARY" if "DEX_SUMMARY" in records else "DEX_CACHE_REUSED"
        if dex_key in records:
            try:
                dex_record = json.loads(records[dex_key])
                observed = dt.datetime.fromisoformat(dex_record["observed_at"])
                if observed.tzinfo is None:
                    raise ValueError("DEX timestamp must include timezone")
                age = dt.datetime.now(dt.timezone.utc) - observed
                if dex_key == "DEX_SUMMARY" and (type(dex_record.get("errors")) is not int or dex_record["errors"] != 0):
                    dex_degraded = True
                if dex_key == "DEX_CACHE_REUSED" and (type(dex_record.get("candidates")) is not int):
                    dex_degraded = True
                dex_fresh = (observed.tzinfo is not None
                             and dt.timedelta(0) <= age <= dt.timedelta(minutes=61)
                             and dex_record.get("buy_approved") is False)
            except (ValueError, TypeError, KeyError):
                dex_fresh = False
        if not dex_fresh:
            dex_degraded = True
            print("DEX_FRESHNESS_UNVERIFIED " + json.dumps({"origin": origin, "record": dex_key if dex_key in records else None}), flush=True)
        shadow_ok = "SHADOW_LEARNING" in records and not shadow_failed
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
        try:
            history = json.loads(records["HISTORY_PERSISTED"])
        except (ValueError, TypeError):
            print("SCAN_INVALID_HISTORY_RECORD", flush=True)
            return 1
        if (not isinstance(history, dict)
                or history.get("history_db_integrity") != "ok"
                or history.get("buy_approved") is not False
                or history.get("model_updates") != "DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION"):
            print("SCAN_HISTORY_SAFETY_FAILED", flush=True)
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
        verified_status = "VERIFIED" if shadow_ok and not dex_degraded else "PARTIAL"
        print("SCAN_EXECUTION_VERIFIED " + json.dumps({
            "origin": origin, "started_at": summary["started_at"],
            "completed_at": summary["completed_at"], "buy_approved": False,
            "shadow_present": shadow_ok, "dex_record_present": dex_ok,
            "dex_degraded": dex_degraded, "dex_fresh": dex_fresh,
            "status": verified_status,
        }), flush=True)
        if manual_pending and verified_status == "VERIFIED":
            try:
                from .manual_requests import acknowledge_requests, publish_results
                watch = json.loads(records["WATCH_SUMMARY"])
                if not isinstance(watch, list):
                    print("MANUAL_WATCH_INVALID_SCHEMA", flush=True)
                    return 1
                delivered = publish_results(manual_pending, summary, watch, "FRESH" if dex_fresh and not dex_degraded else "DEGRADED", origin=origin)
                if not delivered:
                    print("MANUAL_RESULT_DELIVERY_PENDING", flush=True)
                acknowledged = acknowledge_requests(data_dir, delivered, summary["completed_at"])
                print("MANUAL_REQUESTS_SATISFIED " + json.dumps({
                    "issue_numbers": [r["issue_number"] for r in delivered],
                    "run_id": acknowledged["last_verified_run_id"],
                }), flush=True)
            except Exception as exc:
                print("MANUAL_REQUEST_ACK_FAILED " + json.dumps({"error": type(exc).__name__}), flush=True)
        return 0

if __name__ == "__main__":
    sys.exit(execute(sys.argv[1] if len(sys.argv) > 1 else "manual"))
