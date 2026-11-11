#!/usr/bin/env python3
"""Constrained auto-repair: diagnose, fix, validate, and emit evidence.
Only fixes a known, reproducible Python syntax defect: literal backslash-n
tokens between complete Python statements. Never guesses general repairs.
"""
import argparse
import ast
import json
from pathlib import Path
import sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--output", default=".project-pulse-repair")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    out = root / args.output
    out.mkdir(parents=True, exist_ok=True)
    results = []
    changed = []
    for file in sorted((root / ".github" / "scripts").glob("*.py")):
        relative = str(file.relative_to(root))
        original = file.read_text()
        try:
            ast.parse(original, filename=relative)
            continue
        except SyntaxError as error:
            observed = str(error)
        # Only repair the exact previously observed defect at the tail of a script.
        # Candidate must contain literal '\\n' separating statement boundaries.
        tail = original.rfind("\nif not runs and ERRORS:")
        if tail < 0:
            results.append({"file": relative, "status": "abstain", "reason": observed})
            continue
        prefix, suffix = original[:tail], original[tail:]
        if "\\n" not in suffix or "raise SystemExit(" not in suffix:
            results.append({"file": relative, "status": "abstain", "reason": observed})
            continue
        candidate = prefix + suffix.replace("\\n", "\n")
        try:
            ast.parse(candidate, filename=relative)
        except SyntaxError:
            results.append({"file": relative, "status": "abstain", "reason": "candidate still invalid"})
            continue
        file.write_text(candidate)
        changed.append(relative)
        results.append({"file": relative, "status": "fixed", "reason": "literal escaped newlines"})
    # Repair a second *observed* failure: unconditional summary reads of
    # downstream files that are absent when an upstream step fails.
    workflow_dir = root / ".github" / "workflows"
    for file in sorted(workflow_dir.glob("*.yml")):
        relative = str(file.relative_to(root))
        original = file.read_text()
        candidate = original
        for report in ("github-status.md", "project-plan.md"):
            line = 'cat project-pulse-output/' + report + ' >> "$GITHUB_STEP_SUMMARY"'
            guard = 'if [ -f project-pulse-output/' + report + ' ]; then ' + line + '; fi'
            # Only touch the original Project Pulse workflow and exact command.
            if file.name == "project-pulse.yml" and line in candidate and guard not in candidate:
                candidate = candidate.replace(line, guard)
        if candidate != original:
            file.write_text(candidate)
            changed.append(relative)
            results.append({"file": relative, "status": "fixed",
                            "reason": "guard missing downstream report in run summary"})
    # Validate all Python scripts without importing or executing them.
    for file in sorted((root / ".github" / "scripts").glob("*.py")):
        try:
            ast.parse(file.read_text(), filename=str(file))
        except SyntaxError as exc:
            results.append({"file": str(file.relative_to(root)), "status": "remaining-syntax-error",
                            "reason": str(exc)})
    summary = {"schema": 1, "changed": changed, "findings": results,
               "validation": "PASS" if not any(r["status"] == "remaining-syntax-error" for r in results) else "FAIL",
               "scope": "Two observed defects: escaped-newline Python syntax and missing downstream summary files"}
    (out / "repair.json").write_text(json.dumps(summary, indent=2) + "\n")
    (out / "repair.md").write_text("# Project Pulse targeted repair\n\n"
        + f"**Validation:** {summary['validation']}\n\n"
        + f"**Changed files:** {len(changed)}\n\n"
        + "\n".join(f"- {r['file']}: {r['status']} ({r['reason']})" for r in results) + "\n")
    print(json.dumps(summary))
    return 1 if summary["validation"] != "PASS" else 0

if __name__ == "__main__":
    sys.exit(main())
