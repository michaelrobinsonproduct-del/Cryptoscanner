#!/usr/bin/env python3
"""Project Pulse: read-only, bounded repository briefing (stdlib only)."""
import argparse
import datetime as dt
import json
from pathlib import Path
import re
import subprocess
import sys

SKIP = {".git", ".venv", "venv", "node_modules", "__pycache__", ".bounded-state", ".work-evidence", "dist", "build"}
EXTENSIONS = {".py", ".js", ".ts", ".tsx", ".jsx", ".yml", ".yaml"}
MAX_BYTES = 120_000

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--out", default="project-pulse-output")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, text=True, capture_output=True)
    revision = sha.stdout.strip() if sha.returncode == 0 else "unknown"
    files = sorted(p for p in root.rglob("*") if p.is_file()
                   and not any(part in SKIP or part.startswith(".pytest_cache") for part in p.relative_to(root).parts))
    source = [p for p in files if p.suffix in EXTENSIONS]
    tests = [p for p in files if p.name.startswith("test_") and p.suffix == ".py"]
    workflows = [p for p in files if p.parent == root / ".github" / "workflows" and p.suffix in {".yml", ".yaml"}]
    flags = []
    for p in source:
        try:
            if p.stat().st_size > MAX_BYTES:
                continue
            for number, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if re.search(r"\b(TODO|FIXME|XXX)\b", line, re.I):
                    flags.append({"path": str(p.relative_to(root)), "line": number,
                                  "excerpt": line.strip()[:180]})
        except OSError:
            continue
    # Compile-only smoke check: no tests, network, credentials, or mutation.
    py_files = [str(p) for p in source if p.suffix == ".py"]
    syntax_errors = []
    for p in py_files:
        try:
            compile(Path(p).read_bytes(), p, "exec")
        except (SyntaxError, UnicodeError, ValueError) as e:
            syntax_errors.append({"path": str(Path(p).relative_to(root)), "error": str(e)[:250]})
        except OSError as e:
            syntax_errors.append({"path": str(Path(p).relative_to(root)), "error": str(e)[:250]})
    actions = []
    for error in syntax_errors:
        actions.append({"priority": "P0", "kind": "syntax", "detail": error})
    for flag in flags[:30]:
        actions.append({"priority": "P2", "kind": "review-marker", "detail": flag})
    if not actions:
        actions.append({"priority": "INFO", "kind": "none", "detail": "No syntax errors or review markers found"})
    report = {
        "schema": 1, "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "revision": revision, "files": len(files), "source_files": len(source),
        "python_tests": len(tests), "workflows": [str(p.relative_to(root)) for p in workflows],
        "syntax_errors": syntax_errors, "review_markers": flags,
        "next_actions": actions, "scope": "Static repository inventory and Python syntax only; no live CI or project completion claims"
    }
    (out / "pulse.json").write_text(json.dumps(report, indent=2) + "\n")
    lines = ["# Project Pulse", "", f"**Revision:** `{revision}`",
             f"**Generated (UTC):** {report['generated_utc']}", "",
             "## Snapshot", "",
             f"- Files: {len(files)}; source files: {len(source)}",
             f"- Python test modules: {len(tests)}; GitHub workflows: {len(workflows)}",
             f"- Python syntax issues: {len(syntax_errors)}; TODO/FIXME/XXX markers: {len(flags)}",
             "", "## Priority next actions", ""]
    for action in actions[:30]:
        detail = action["detail"]
        if isinstance(detail, dict):
            label = f"{detail.get('path', '?')}:{detail.get('line', '')} {detail.get('excerpt', detail.get('error', ''))}"
        else:
            label = detail
        lines.append(f"- **{action['priority']}** {action['kind']}: {label}")
    lines.extend(["", "## Workflows", ""])
    lines.extend(f"- `{p.relative_to(root)}`" for p in workflows)
    lines.extend(["", "## Limits", "", report["scope"], ""])
    (out / "pulse.md").write_text("\n".join(lines))
    print(json.dumps({"revision": revision, "source_files": len(source), "syntax_errors": len(syntax_errors),
                      "review_markers": len(flags), "output": str(out)}))
    return 1 if syntax_errors else 0

if __name__ == "__main__":
    sys.exit(main())
