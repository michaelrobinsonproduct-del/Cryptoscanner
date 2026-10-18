"""Single-process Railway service: quarter-hour scheduled scans plus on-demand GitHub requests.

Development-only until deployment is explicitly validated. Run exactly ONE replica
with the existing /data mount; Railway cron must be disabled when using this daemon.
No second writer or additional Railway service may share the history database.
"""
import datetime as dt
import json
import os
import signal
import time
from pathlib import Path
from .execute_once import execute
from .manual_requests import fetch_requests, plan_requests, read_ledger

POLL_SECONDS = 30
MANUAL_COOLDOWN_SECONDS = 60
_stop = False

def stop(*_args):
    global _stop
    _stop = True

def quarter_hour_bucket(now):
    """UTC bucket number, monotonic over days and daylight saving transitions."""
    return int(now.timestamp()) // 900

def due_manual(data_dir, now):
    if not os.environ.get("SIMPLE_SCANNER_GITHUB_TOKEN"):
        return False
    state = read_ledger(data_dir)
    if state.get("ledger_valid") is False:
        print("MANUAL_REQUEST_LEDGER_INVALID", flush=True)
        return False
    try:
        return bool(plan_requests(fetch_requests(), state, now))
    except Exception as exc:
        print("MANUAL_REQUEST_CHECK_FAILED " + json.dumps({"error": type(exc).__name__}), flush=True)
        return False

def serve(*, sleep=time.sleep, clock=lambda: dt.datetime.now(dt.timezone.utc), run=execute):
    """One loop owns scheduled and manual runs, avoiding concurrent writers."""
    global _stop
    _stop = False
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    data_dir = Path(os.environ.get("SIMPLE_SCANNER_DATA_DIR", "simple_scanner/output"))
    data_dir.mkdir(parents=True, exist_ok=True)
    last_bucket = quarter_hour_bucket(clock())
    last_manual_attempt = float("-inf")
    print("SCANNER_DAEMON_READY " + json.dumps({"mode":"SINGLE_PROCESS", "scheduled_interval_minutes":15,
                                              "manual_poll_seconds":POLL_SECONDS}), flush=True)
    while not _stop:
        now = clock()
        bucket = quarter_hour_bucket(now)
        if bucket > last_bucket:
            last_bucket = bucket
            result = run("cron")
            print("DAEMON_CRON_EXIT " + json.dumps({"exit_code":result}), flush=True)
        elif time.monotonic() - last_manual_attempt >= MANUAL_COOLDOWN_SECONDS and due_manual(data_dir, now):
            last_manual_attempt = time.monotonic()
            print("DAEMON_MANUAL_REQUEST_ACCEPTED " + json.dumps({"at": now.isoformat()}), flush=True)
            result = run("manual")
            print("DAEMON_MANUAL_EXIT " + json.dumps({"exit_code":result}), flush=True)
        sleep(POLL_SECONDS)

if __name__ == "__main__":
    serve()
