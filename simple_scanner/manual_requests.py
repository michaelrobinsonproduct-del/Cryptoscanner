"""Read-only GitHub issue request discovery. Not wired to production cron.

No token or API failure means no manual requests; scheduled scans continue.
No issue body is executed as code. This module never launches a scan.
"""
import datetime as dt
import json
from pathlib import Path
import os
import urllib.error
import urllib.parse
import urllib.request

REPO = "michaelrobinsonproduct-del/Cryptoscanner"
LABEL = "manual-scan-request"
MAX_REQUESTS = 20

def parse_requests(items, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    requests = []
    for item in items:
        if not isinstance(item, dict) or "pull_request" in item:
            continue
        if item.get("state") != "open" or item.get("title") != "MANUAL_SCAN_REQUEST":
            continue
        if LABEL not in [x.get("name") for x in item.get("labels", []) if isinstance(x, dict)]:
            continue
        number = item.get("number")
        if type(number) is not int or number <= 0:
            continue
        try:
            created = dt.datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
            if created.tzinfo is None or not (now - dt.timedelta(minutes=60) <= created <= now + dt.timedelta(minutes=1)):
                continue
        except (KeyError, ValueError, TypeError, AttributeError):
            continue
        requests.append({"issue_number": number, "created_at": created.isoformat()})
    return requests

def fetch_requests():
    token = os.environ.get("SIMPLE_SCANNER_GITHUB_TOKEN", "")
    if not token:
        return []
    query = urllib.parse.urlencode({"state": "open", "labels": LABEL, "per_page": MAX_REQUESTS})
    url = "https://api.github.com/repos/" + REPO + "/issues?" + query
    request = urllib.request.Request(url, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "kraken-simple-scanner-manual-request-reader",
    })
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            items = json.load(response)
        if not isinstance(items, list):
            return []
        return parse_requests(items)
    except (urllib.error.URLError, TimeoutError, ValueError, OSError):
        return []

def plan_requests(items, ledger, completed_at=None):
    """Pure idempotency planner: never execute duplicate issue IDs."""
    done = set(ledger.get("completed_issue_numbers", []))
    pending = [x for x in items if x["issue_number"] not in done]
    # One scheduled run can satisfy all requests present at its start.
    if completed_at:
        pending = [x for x in pending if dt.datetime.fromisoformat(x["created_at"]) <= completed_at]
    return pending

def read_ledger(data_dir):
    path = Path(data_dir) / "manual_request_ledger.json"
    try:
        data = json.loads(path.read_text())
        if isinstance(data, dict) and isinstance(data.get("completed_issue_numbers"), list):
            return data
    except FileNotFoundError:
        pass
    except (OSError, ValueError):
        pass
    # Corrupt state fails closed: caller must not acknowledge any request.
    return {"completed_issue_numbers": [], "ledger_valid": not path.exists()}

def acknowledge_requests(data_dir, requests, run_id):
    """Atomic local acknowledgment after a verified scan, never before."""
    directory = Path(data_dir)
    state = read_ledger(directory)
    if state.get("ledger_valid") is False:
        raise RuntimeError("Manual request ledger invalid; refusing acknowledgment")
    done = {n for n in state["completed_issue_numbers"] if type(n) is int and n > 0}
    done.update(r["issue_number"] for r in requests)
    payload = {"completed_issue_numbers": sorted(done), "last_verified_run_id": str(run_id)}
    import os
    import tempfile
    with tempfile.NamedTemporaryFile(mode="w", dir=directory, prefix=".manual_ledger_", delete=False) as f:
        temp = Path(f.name)
        json.dump(payload, f)
        f.flush()
        os.fsync(f.fileno())
    try:
        os.replace(temp, directory / "manual_request_ledger.json")
    finally:
        temp.unlink(missing_ok=True)
    return payload

def publish_results(requests, run):
    """Post a bounded research-only receipt to GitHub issues.

    No token means no publication; never include secrets or raw scan logs.
    The request stays open if GitHub refuses the receipt.
    """
    token = os.environ.get("SIMPLE_SCANNER_GITHUB_TOKEN", "")
    if not token or not requests:
        return []
    receipt = {
        "type": "MANUAL_SCAN_RESULT",
        "status": "VERIFIED",
        "completed_at": run["completed_at"],
        "buy_approved": False,
        "scan_origin": "scheduled",
        "learning": "SHADOW_ONLY",
        "dex_fresh": True,
    }
    body = "Verified scheduled scan satisfied this manual request.\\n\\n" + "```json\\n" + json.dumps(receipt, sort_keys=True) + "\\n```"
    delivered = []
    for item in requests:
        number = item["issue_number"]
        url = "https://api.github.com/repos/" + REPO + "/issues/" + str(number) + "/comments"
        request = urllib.request.Request(url, data=json.dumps({"body": body}).encode(), method="POST", headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "kraken-simple-scanner-manual-result",
        })
        try:
            with urllib.request.urlopen(request, timeout=5) as response:
                if response.status == 201:
                    delivered.append(item)
        except (urllib.error.URLError, TimeoutError, OSError):
            continue
    return delivered
