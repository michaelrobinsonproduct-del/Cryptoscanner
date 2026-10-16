"""Read-only GitHub issue request discovery. Not wired to production cron.

No token or API failure means no manual requests; scheduled scans continue.
No issue body is executed as code. This module never launches a scan.
"""
import datetime as dt
import json
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
