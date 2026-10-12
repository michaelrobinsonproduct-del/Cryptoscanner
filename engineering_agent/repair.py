"""Isolated, opt-in engineering agent. No production deploy or trading actions."""
import base64
import json
import os
import pathlib
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from io import BytesIO

REPO = os.getenv("AGENT_REPO", "michaelrobinsonproduct-del/Cryptoscanner")
BASE = os.getenv("AGENT_BASE_BRANCH", "simplified-scanner-recovery-20261011")
ALLOWED = re.compile(r"^simple_scanner/[A-Za-z0-9_./-]+\.py$")
MAX_FILE_BYTES = 120_000

def request(url, token=None, data=None, method=None):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "kraken-engineering-agent"}
    if token:
        headers["Authorization"] = "Bearer " + token
    if data is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read()

def github(path, token, data=None, method=None):
    raw = request("https://api.github.com/repos/" + REPO + path, token, data, method)
    return json.loads(raw) if raw else {}

def valid_path(path):
    return isinstance(path, str) and bool(ALLOWED.fullmatch(path)) and ".." not in pathlib.PurePosixPath(path).parts

def validate_changes(changes):
    if not isinstance(changes, list) or not 1 <= len(changes) <= 3:
        raise ValueError("Expected 1-3 modified Python files")
    seen = set()
    for item in changes:
        if not isinstance(item, dict) or not valid_path(item.get("path")):
            raise ValueError("Unsafe file path")
        if item["path"] in seen or not isinstance(item.get("content"), str):
            raise ValueError("Duplicate path or invalid content")
        seen.add(item["path"])
        if len(item["content"].encode()) > MAX_FILE_BYTES:
            raise ValueError("File exceeds limit")
    return changes

def get_model_proposal(files, failure):
    url = os.environ["AGENT_MODEL_URL"]
    token = os.environ["AGENT_MODEL_TOKEN"]
    model = os.environ["AGENT_MODEL_NAME"]
    prompt = (
        "You are a careful Python reliability engineer. Diagnose ONE demonstrated bug. "
        "Return ONLY JSON with keys 'reason' and 'changes', where changes is a list of "
        "1-3 objects with path and COMPLETE replacement content. Edit only simple_scanner/*.py. "
        "Do not change credentials, trade execution, deployment, or data. "
        "If no justified fix exists return changes: [].\n"
        "Baseline failure:\n" + failure[-5000:] + "\nFiles:\n" + json.dumps(files)[:65000]
    )
    payload = {"model": model, "temperature": 0, "messages": [
        {"role": "system", "content": "Return only valid JSON, never markdown."},
        {"role": "user", "content": prompt}
    ]}
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        response = json.load(resp)
    content = response["choices"][0]["message"]["content"].strip()
    if content.startswith("```"):
        content = re.sub(r"^\x60{3}(?:json)?\s*|\s*\x60{3}$", "", content)
    return json.loads(content)

def test_suite(root):
    cmds = [
        ["python", "-m", "compileall", "-q", "simple_scanner"],
        ["python", "-m", "unittest", "discover", "-s", "simple_scanner", "-p", "test_*.py", "-v"]
    ]
    logs = []
    for cmd in cmds:
        try:
            proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=90,
                                  env={"PATH": os.getenv("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1"})
        except subprocess.TimeoutExpired:
            return False, "Timed out running " + " ".join(cmd)
        logs.append((proc.stdout + proc.stderr)[-8000:])
        if proc.returncode:
            return False, "\n".join(logs)
    return True, "\n".join(logs)

def safe_extract_zip(blob, destination):
    with zipfile.ZipFile(BytesIO(blob)) as archive:
        for entry in archive.infolist():
            name = pathlib.PurePosixPath(entry.filename)
            if ".." in name.parts or name.is_absolute():
                raise ValueError("Unsafe archive")
        archive.extractall(destination)
    roots = list(pathlib.Path(destination).iterdir())
    if len(roots) != 1 or not roots[0].is_dir():
        raise ValueError("Unexpected repository archive")
    return roots[0]

def run_once():
    required = ("AGENT_MODEL_URL", "AGENT_MODEL_TOKEN", "AGENT_MODEL_NAME", "AGENT_GITHUB_TOKEN")
    missing = [key for key in required if not os.getenv(key)]
    if missing:
        return {"status": "not_configured", "missing": missing}
    token = os.environ["AGENT_GITHUB_TOKEN"]
    ref = github("/git/ref/heads/" + urllib.parse.quote(BASE, safe=""), token)
    sha = ref["object"]["sha"]
    archive = request("https://api.github.com/repos/" + REPO + "/zipball/" + sha, token)
    with tempfile.TemporaryDirectory(prefix="kraken-agent-") as tmp:
        root = safe_extract_zip(archive, tmp)
        baseline_ok, baseline_log = test_suite(root)
        if baseline_ok:
            return {"status": "baseline_passed", "action": "no_unjustified_change", "sha": sha}
        files = {}
        for path in sorted((root / "simple_scanner").glob("*.py")):
            if path.stat().st_size <= 25000:
                files["simple_scanner/" + path.name] = path.read_text()
        proposal = get_model_proposal(files, baseline_log)
        changes = proposal.get("changes", [])
        if not changes:
            return {"status": "no_proposal", "reason": str(proposal.get("reason", ""))[:500]}
        validate_changes(changes)
        for item in changes:
            target = root / item["path"]
            if not target.is_file():
                raise ValueError("Only existing Python files can be edited")
            target.write_text(item["content"])
        passed, log = test_suite(root)
        if not passed:
            return {"status": "rejected_tests_failed", "details": log[-2000:]}
        branch = "agent/repair-" + str(int(time.time()))
        github("/git/refs", token, {"ref": "refs/heads/" + branch, "sha": sha})
        for item in changes:
            old = github("/contents/" + item["path"] + "?ref=" + urllib.parse.quote(BASE), token)
            github("/contents/" + item["path"], token, {
                "message": "Agent: tested isolated reliability repair",
                "content": base64.b64encode(item["content"].encode()).decode(),
                "sha": old["sha"], "branch": branch
            }, "PUT")
        pr = github("/pulls", token, {"title": "Agent: isolated verified repair",
            "head": branch, "base": BASE,
            "body": "Baseline failed; proposed fix passed Python compilation and unit tests. Human review required; no auto-merge or production deploy."})
        return {"status": "review_pr_created", "url": pr["html_url"], "reason": str(proposal.get("reason", ""))[:500]}

if __name__ == "__main__":
    print(json.dumps(run_once()))
