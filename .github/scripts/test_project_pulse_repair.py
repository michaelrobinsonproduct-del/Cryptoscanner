#!/usr/bin/env python3
"""Executable regression: reproduce both real Project Pulse failures and repair them."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ENGINE = Path(__file__).with_name("project_pulse_repair.py").resolve()
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    scripts = root / ".github" / "scripts"
    workflows = root / ".github" / "workflows"
    scripts.mkdir(parents=True)
    workflows.mkdir(parents=True)
    broken = scripts / "project_pulse_plan.py"
    broken.write_text('runs=[]\nERRORS=[]\nif not runs and ERRORS:\\n    raise SystemExit("error")\\nprint("done")\n')
    workflow = workflows / "project-pulse.yml"
    workflow.write_text('run: |\n  cat project-pulse-output/github-status.md >> "$GITHUB_STEP_SUMMARY"\n'
                        '  cat project-pulse-output/project-plan.md >> "$GITHUB_STEP_SUMMARY"\n')
    result = subprocess.run([sys.executable, str(ENGINE), "--root", str(root)],
                            capture_output=True, text=True)
    if result.returncode:
        raise SystemExit(result.stderr + result.stdout)
    report = json.loads((root / ".project-pulse-repair" / "repair.json").read_text())
    assert len(report["changed"]) == 2, report
    compile(broken.read_text(), str(broken), "exec")
    assert 'if [ -f project-pulse-output/github-status.md ]; then' in workflow.read_text()
    assert 'if [ -f project-pulse-output/project-plan.md ]; then' in workflow.read_text()
    # Re-running must not generate duplicate guards or additional changes.
    rerun = subprocess.run([sys.executable, str(ENGINE), "--root", str(root)],
                           capture_output=True, text=True)
    assert rerun.returncode == 0, rerun.stderr
    second = json.loads((root / ".project-pulse-repair" / "repair.json").read_text())
    assert second["changed"] == [], second
    print(json.dumps({"fixture_repairs": 2, "validated": True, "idempotent": True}))
