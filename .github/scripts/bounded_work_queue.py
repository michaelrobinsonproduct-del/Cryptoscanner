#!/usr/bin/env python3
"""Bounded test/recovery inventory with durable pass-only checkpoints.

This is a diagnostic executor, not an autonomous code editor. It prioritizes
previous failures and unfinished work, never counts a failure as completed,
and writes a machine-readable plan for the next invocation.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

root = Path(__file__).resolve().parents[2]
out = root / ".work-evidence"
out.mkdir(exist_ok=True)
state_dir = root / ".bounded-state"
state_dir.mkdir(exist_ok=True)
checkpoint = state_dir / "checkpoint.json"
minutes = min(320, max(1, int(os.environ.get("REQUESTED_MINUTES", "5"))))
deadline = time.monotonic() + minutes * 60
reserve = 25

def load_state():
    try:
        raw = json.loads(checkpoint.read_text())
        if raw.get("schema") == 2:
            return raw
    except (ValueError, OSError):
        pass
    return {"schema": 2, "passed": [], "failures": {}, "attempts": {}}

def save_state():
    temp = checkpoint.with_suffix(".tmp")
    temp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    temp.replace(checkpoint)

state = load_state()
source_sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
if state.get("source_sha") != source_sha:
    # Do not reuse PASS verdicts from a different source revision.
    state = {"schema": 2, "passed": [], "failures": {}, "attempts": {}, "source_sha": source_sha}
# Enumerate only known test modules, not arbitrary commands.
test_files = sorted(p for p in root.rglob("test_*.py")
                    if not any(part in {".git", ".venv", "site-packages", ".bounded-state"}
                               for part in p.parts))
tasks = [("compile", [sys.executable, "-m", "compileall", "-q", "paper_pov"])]
tasks.extend((str(p.relative_to(root)), [sys.executable, "-m", "unittest", "discover",
              "-s", str(p.parent.relative_to(root)), "-p", p.name]) for p in test_files)
if len(tasks) < 4:
    raise SystemExit("INSUFFICIENT_BACKLOG")

# Previously failed tasks first; successful tasks are not needlessly rerun.
previous_failures = set(state["failures"])
tasks.sort(key=lambda item: (item[0] not in previous_failures, item[0]))
passed = set(state["passed"])
attempted = 0
failed_this_run = []
for key, command in tasks:
    if key in passed:
        continue
    remaining = deadline - time.monotonic()
    if remaining <= reserve + 10:
        break
    attempted += 1
    start = time.time()
    # Leave time for diagnostics, state persistence, and artifact upload.
    timeout = max(1, min(45, int(remaining-reserve)))
    try:
        result = subprocess.run(command, cwd=root, capture_output=True, text=True,
                                timeout=timeout)
        status = "PASS" if result.returncode == 0 else "FAIL"
        log = (result.stdout + "\n" + result.stderr)[-20000:]
    except subprocess.TimeoutExpired:
        status, log = "TIMEOUT", "Task exceeded bounded 45-second attempt"
    record = {"task": key, "status": status, "command": command, "start": start,
              "end": time.time(), "log": log}
    (out / ("task-%04d.json" % attempted)).write_text(json.dumps(record, indent=2))
    state["attempts"][key] = state["attempts"].get(key, 0) + 1
    if status == "PASS":
        passed.add(key)
        state["failures"].pop(key, None)
    else:
        failed_this_run.append(key)
        state["failures"][key] = {"status": status, "last_attempt": time.time(),
                                  "attempts": state["attempts"][key]}
    state["passed"] = sorted(passed)
    save_state()
    print(f"[{attempted}/{len(tasks)}] {status}: {key}", flush=True)

unfinished = [key for key, _ in tasks if key not in passed]
summary = {"discovered": len(tasks), "attempted_this_run": attempted,
           "passed_cumulative": len(passed), "failed_this_run": failed_this_run,
           "unresolved": unfinished, "unresolved_count": len(unfinished),
           "reason": "BACKLOG_RESOLVED" if not unfinished else
                     ("TIME_BUDGET" if deadline-time.monotonic() <= reserve+10
                      else "UNRESOLVED_FAILURES"),
           "work_seconds": minutes*60-max(0, deadline-time.monotonic())}
(out / "summary.json").write_text(json.dumps(summary, indent=2))
save_state()
print(json.dumps({k: v for k, v in summary.items() if k != "unresolved"}), flush=True)
# Exit normally when diagnostics were executed; failures remain explicitly unresolved.
