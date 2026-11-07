#!/usr/bin/env python3
"""Bounded, resumable, fail-closed work executor. No idle loops or repeated tasks."""
import json, os, pathlib, subprocess, time
root = pathlib.Path(__file__).resolve().parents[2]
queue_path = root / ".github" / "bounded-work-queue.json"
out = root / ".work-evidence"
out.mkdir(exist_ok=True)
minutes = min(320, max(1, int(os.environ.get("REQUESTED_MINUTES", "320"))))
deadline = time.monotonic() + minutes * 60
queue = json.loads(queue_path.read_text())
if not isinstance(queue, list) or not queue:
    raise SystemExit("NO_WORK: populate a substantive task queue; never burn runtime idling")
completed = set()
checkpoint = out / "checkpoint.json"
if checkpoint.exists():
    completed = set(json.loads(checkpoint.read_text()).get("completed", []))
allowed = {"python_compile": ["python3", "-m", "compileall", "-q", "paper_pov"],
           "trigger_contract": ["python3", "-m", "unittest", "paper_pov.test_workflow_trigger_guard"],
           "report_contract": ["python3", "-m", "unittest", "paper_pov.test_results_report"]}
for task in queue:
    if not isinstance(task, dict) or set(task) != {"id", "action"}:
        raise SystemExit("INVALID_TASK")
    key, action = task["id"], task["action"]
    if key in completed:
        continue
    if action not in allowed:
        raise SystemExit("UNAUTHORIZED_ACTION: " + str(action))
    remaining = deadline - time.monotonic()
    if remaining < 120:
        break
    start = time.time()
    try:
        result = subprocess.run(allowed[action], cwd=root, text=True, capture_output=True,
                                timeout=min(remaining - 60, 1800), check=False)
        status = "PASS" if result.returncode == 0 else "FAIL"
        log = (result.stdout + "\n" + result.stderr)[-30000:]
    except subprocess.TimeoutExpired:
        status, log = "TIMEOUT", "Task exceeded bounded execution window"
    (out / (str(key).replace("/", "_") + ".json")).write_text(
        json.dumps({"id": key, "action": action, "status": status, "started": start,
                    "finished": time.time(), "log": log}, indent=2))
    if status != "PASS":
        checkpoint.write_text(json.dumps({"completed": sorted(completed), "failed": key}, indent=2))
        raise SystemExit("STOP_ON_FAILURE: " + str(key))
    completed.add(key)
    checkpoint.write_text(json.dumps({"completed": sorted(completed)}, indent=2))
print(json.dumps({"completed": sorted(completed), "remaining": len(queue)-len(completed),
                  "reason": "QUEUE_COMPLETE" if len(completed)==len(queue) else "TIME_BUDGET"}))
