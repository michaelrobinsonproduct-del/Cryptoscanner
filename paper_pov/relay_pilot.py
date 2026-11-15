"""Bounded two-run relay pilot. No market data or ledger writes."""
import base64
import datetime as dt
import json
import os
import time
import urllib.request

REPO = "michaelrobinsonproduct-del/Cryptoscanner"
WRITER = "paper-pipeline.yml"
RELAY = "paper-relay-pilot.yml"
UTC = dt.timezone.utc

def now():
    return dt.datetime.now(UTC)

def parse(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))

def next_slot(t):
    t = t.replace(second=0, microsecond=0) + dt.timedelta(minutes=1)
    while t.minute not in (24, 54):
        t += dt.timedelta(minutes=1)
    return t

def valid_result(r, run_id, source, at):
    age = (at - parse(r["as_of"])).total_seconds()
    return (str(r["run_id"]) == str(run_id)
            and r["source_sha"] == source
            and r["status"] == "SUCCESS_PAPER_ONLY"
            and r["remote_readback_verified"] is True
            and r["production_applied"] is False and r["buy_approved"] is False
            and 0 <= age <= 600 and 0 <= r["max_client_quote_age_seconds"] <= 600)

def action(runs, report, source, at):
    if any(r["status"] != "completed" for r in runs):
        return "ACTIVE"
    if report and valid_result(report, report["run_id"], source, at):
        return "FRESH"
    return "DISPATCH"

def api(path, body=None):
    url = "https://api.github.com/repos/" + REPO + "/" + path
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": "Bearer " + os.environ["GH_TOKEN"],
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2026-03-10",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)

def dispatch(workflow, inputs=None):
    data = api("actions/workflows/" + workflow + "/dispatches",
               {"ref": "main", "inputs": inputs or {}, "return_run_details": True})
    rid = int(data["workflow_run_id"])
    print("DISPATCH_ACCEPTED", workflow, rid, data["html_url"], flush=True)
    return rid

def canonical():
    data = api("contents/verified-results/results.json?ref=paper-proof-ledger")
    return json.loads(base64.b64decode(data["content"]))

def emit(message):
    print(message, flush=True)
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as stream:
        stream.write(message + "\n")

def wait_slot(target):
    delta = (parse(target) - now()).total_seconds()
    if not -180 <= delta <= 1800:
        raise RuntimeError("Target expired or exceeds bounded pilot wait")
    if delta > 0:
        time.sleep(delta)

def run():
    assert os.environ["GITHUB_REPOSITORY"] == REPO
    assert os.environ["GITHUB_REF"] == "refs/heads/main"
    assert os.environ["GITHUB_RUN_ATTEMPT"] == "1", "No pilot reruns"
    hop = int(os.environ["RELAY_HOP"])
    assert hop in (1, 2)
    source = os.environ["GITHUB_SHA"]
    assert api("git/ref/heads/main")["object"]["sha"] == source
    if hop == 2:
        parent = int(os.environ["RELAY_PARENT"])
        p = api("actions/runs/" + str(parent))
        assert p["path"].split("@")[0] == ".github/workflows/" + RELAY
        assert p["head_sha"] == source and p["head_branch"] == "main"
        assert p["status"] == "completed" and p["conclusion"] == "success"
    report = canonical()
    runs = api("actions/workflows/" + WRITER + "/runs?branch=main&per_page=100")["workflow_runs"]
    decision = action(runs, report, source, now())
    if decision == "ACTIVE":
        emit("ACTIVE_WRITER; no dispatch; pilot stops without claiming verification")
        raise RuntimeError("Existing writer active; avoid duplicate")
    if decision == "FRESH":
        emit("FRESH_EXISTING_CANONICAL " + str(report["run_id"]) + "; no duplicate dispatch")
    else:
        rid = dispatch(WRITER)
        deadline = time.monotonic() + 15 * 60
        while time.monotonic() < deadline:
            item = api("actions/runs/" + str(rid))
            assert item["head_sha"] == source and item["event"] == "workflow_dispatch"
            if item["status"] == "completed":
                assert item["conclusion"] == "success", "Writer failed"
                r = canonical()
                assert valid_result(r, rid, source, now()), "Canonical mismatch or stale"
                emit("EXACT_WRITER_VERIFIED " + str(rid) + " generation " + str(r["ledger_generation"]))
                break
            time.sleep(10)
        else:
            raise RuntimeError("Writer observation expired; no retry")
    if hop == 1:
        target = next_slot(now())
        successor = dispatch(RELAY, {"hop": "2", "parent": os.environ["GITHUB_RUN_ID"],
                                    "target": target.isoformat()})
        emit("SUCCESSOR_ACCEPTED " + str(successor) + " TARGET " + target.isoformat())
    else:
        emit("BOUNDED_RELAY_COMPLETE; no additional successor")

if __name__ == "__main__":
    run()
