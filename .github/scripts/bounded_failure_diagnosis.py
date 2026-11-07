#!/usr/bin/env python3
"""Turn bounded-run evidence into a deterministic, auditable next-run plan.

No code mutation, secret access, arbitrary shell execution, or production changes.
"""
import hashlib
import json
from pathlib import Path
import re

evidence = Path(".work-evidence")
records = []
for path in sorted(evidence.glob("task-*.json")):
    try:
        item = json.loads(path.read_text())
        if isinstance(item, dict) and "task" in item and "status" in item:
            records.append(item)
    except (ValueError, OSError):
        continue

def classify(item):
    log = str(item.get("log", ""))[-12000:]
    if item["status"] == "TIMEOUT":
        return "TIMEOUT", "Reduce task scope or inspect test hangs"
    if re.search(r"ModuleNotFoundError|ImportError|No module named", log):
        return "DEPENDENCY", "Inspect Python imports and CI dependencies"
    if re.search(r"AssertionError|FAIL:|Assertion failed", log):
        return "ASSERTION", "Inspect assertion and expected behavior"
    if re.search(r"FileNotFoundError|No such file or directory", log):
        return "MISSING_INPUT", "Inspect required fixture or artifact path"
    if re.search(r"PermissionError|403|401|unauthorized", log, re.I):
        return "ACCESS", "Inspect permissions; do not bypass access controls"
    if re.search(r"SyntaxError|IndentationError", log):
        return "SYNTAX", "Inspect indicated source location"
    return "UNCLASSIFIED", "Inspect full task evidence before proposing a fix"

findings = []
for item in records:
    if item["status"] == "PASS":
        continue
    kind, recommendation = classify(item)
    # Fingerprint stable failure content; never persist secrets or raw log in the plan.
    fingerprint = hashlib.sha256((str(item["task"]) + "|" + kind).encode()).hexdigest()[:16]
    findings.append({"task": item["task"], "status": item["status"],
                     "category": kind, "fingerprint": fingerprint,
                     "next_action": recommendation})
plan = {"schema": 1, "observations": len(records), "failures": len(findings),
        "next_actions": findings, "autonomous_code_repair": False,
        "note": "Diagnosis only; no claim of self-repair or learned improvement"}
evidence.mkdir(exist_ok=True)
(evidence / "next-run-plan.json").write_text(json.dumps(plan, indent=2) + "\n")
print(json.dumps({"observations": len(records), "failures": len(findings),
                  "categories": sorted({x["category"] for x in findings})}))
