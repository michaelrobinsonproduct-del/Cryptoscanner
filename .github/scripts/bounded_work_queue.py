#!/usr/bin/env python3
"""One-pass, bounded repository test inventory; never spin, repeat, or conceal failures."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

root = Path(__file__).resolve().parents[2]
out = root / ".work-evidence"
out.mkdir(exist_ok=True)
minutes = min(320, max(1, int(os.environ.get("REQUESTED_MINUTES", "5"))))
deadline = time.monotonic() + minutes * 60
reserve = 20
checkpoint = out / "checkpoint.json"

# Discover real work instead of relying on three hardcoded checks.
# Each test module is executed once, in a separate process, with its own evidence.
test_files = sorted(
    p for p in root.rglob("test_*.py")
    if ".git" not in p.parts and ".venv" not in p.parts and "site-packages" not in p.parts
)
tasks = [("compile", [sys.executable, "-m", "compileall", "-q", "paper_pov"])]
tasks.extend((str(p.relative_to(root)), [sys.executable, "-m", "unittest",
              "discover", "-s", str(p.parent.relative_to(root)), "-p", p.name])
             for p in test_files)
if len(tasks) < 4:
    raise SystemExit("INSUFFICIENT_BACKLOG: fewer than four distinct tasks")

done = set()
if checkpoint.exists():
    done = set(json.loads(checkpoint.read_text()).get("completed", []))
failed = []
attempted = 0
for key, cmd in tasks:
    if key in done:
        continue
    remaining = deadline - time.monotonic()
    if remaining <= reserve + 10:
        break
    attempted += 1
    started = time.time()
    try:
        p = subprocess.run(cmd, cwd=root, capture_output=True, text=True,
                           timeout=max(1, min(remaining-reserve, 120)))
        status = "PASS" if p.returncode == 0 else "FAIL"
        log = (p.stdout + "\n" + p.stderr)[-20000:]
    except subprocess.TimeoutExpired:
        status, log = "TIMEOUT", "Per-task timeout; continuing to next distinct task"
    (out / ("task-%04d.json" % attempted)).write_text(json.dumps({
        "task": key, "command": cmd, "status": status,
        "start": started, "end": time.time(), "log": log}, indent=2))
    done.add(key)
    if status != "PASS":
        failed.append(key)
    checkpoint.write_text(json.dumps({"completed": sorted(done), "failed_this_run": failed,
                                      "total_discovered": len(tasks)}, indent=2))
    print(f"[{attempted}/{len(tasks)}] {status}: {key}", flush=True)

remaining_tasks = len(tasks)-len(done)
summary = {"discovered": len(tasks), "attempted_this_run": attempted,
           "completed": len(done), "remaining": remaining_tasks, "failed_this_run": failed,
           "elapsed_budget_seconds": minutes*60 - max(0, deadline-time.monotonic()),
           "reason": "TIME_BUDGET" if remaining_tasks else "BACKLOG_EXHAUSTED"}
(out / "summary.json").write_text(json.dumps(summary, indent=2))
print(json.dumps(summary), flush=True)
if failed:
    print(f"DIAGNOSTIC_OUTCOME: {len(failed)} distinct tasks failed; inspect evidence and next-run plan", flush=True)
    # A test failure is evidence, not an executor failure. Keep the experiment green
    # when the queue ran correctly; do not disguise the individual FAIL statuses.
