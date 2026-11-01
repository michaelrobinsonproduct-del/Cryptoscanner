"""Fail-closed owner-authenticated READ-ONLY fallback for a missing legacy shadow.

Only a new, sealed, completed single PAPER writer may be shadowed. Never dispatches
the writer, modifies the ledger, trades, promotes scores, or claims predictive lift.
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

from paper_pov import ledger
from paper_pov.segmented_storage import MAX_RAW_BYTES

REPO = "michaelrobinsonproduct-del/Cryptoscanner"
OWNER = "michaelrobinsonproduct-del"
OWNER_ID = 336805669
PAPER = "Public Kraken Paper POV (scheduled, isolated ledger)"
PAPER_PATH = ".github/workflows/paper-pipeline.yml"
SHADOW = "Independent legacy-inspired PAPER shadow (read only)"
SHADOW_PATH = ".github/workflows/paper-legacy-shadow.yml"
COMMAND = "/paper-legacy-shadow-heartbeat"
SHA = re.compile(r"^[0-9a-f]{40}$")


def stamp(value):
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ValueError("Missing UTC provenance timestamp")
    result = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.utcoffset() != dt.timedelta(0):
        raise ValueError("Non-UTC provenance")
    return result


def _abstain(reason):
    return {"action": "ABSTAIN", "reason": reason}


def decide(event, paper_runs, shadow_runs, state, manifest, ledger_message,
           *, repository, current_run_id, checkout_sha, now):
    if (repository != REPO or event.get("repository", {}).get("full_name") != REPO
            or event.get("repository", {}).get("default_branch") != "main"
            or event.get("action") != "created"
            or event.get("issue", {}).get("number") != 34
            or event.get("issue", {}).get("pull_request") is not None
            or event.get("comment", {}).get("body") != COMMAND
            or event.get("comment", {}).get("user", {}).get("login") != OWNER
            or event.get("comment", {}).get("user", {}).get("id") != OWNER_ID
            or event.get("comment", {}).get("author_association") != "OWNER"
            or event.get("sender", {}).get("login") != OWNER
            or event.get("sender", {}).get("id") != OWNER_ID
            or not isinstance(checkout_sha, str) or not SHA.fullmatch(checkout_sha)
            or type(current_run_id) is not int or current_run_id < 1):
        raise ValueError("Unauthenticated owner shadow fallback")
    if not isinstance(now, dt.datetime) or now.tzinfo is None:
        raise ValueError("Invalid current clock")
    now = now.astimezone(dt.timezone.utc)
    comment_time = stamp(event["comment"].get("created_at"))
    if not dt.timedelta(0) <= now - comment_time <= dt.timedelta(minutes=10):
        return _abstain("STALE_OR_FUTURE_OWNER_COMMAND")
    if not isinstance(paper_runs, dict) or not isinstance(paper_runs.get("workflow_runs"), list):
        raise ValueError("Missing authoritative writer runs")
    if not isinstance(shadow_runs, dict) or not isinstance(shadow_runs.get("workflow_runs"), list):
        raise ValueError("Missing authoritative shadow runs")
    papers = paper_runs["workflow_runs"]
    if not papers or len(papers) >= 100:
        return _abstain("EMPTY_OR_PAGINATION_AMBIGUITY")
    for run in papers:
        if (run.get("name") != PAPER or run.get("path") != PAPER_PATH
                or run.get("repository", {}).get("full_name") != REPO
                or run.get("head_branch") != "main"):
            return _abstain("UNTRUSTED_WRITER_RUN_HISTORY")
    papers.sort(key=lambda r: stamp(r.get("created_at")), reverse=True)
    writer = papers[0]
    if any(r.get("status") != "completed" for r in papers[:3]):
        return _abstain("ACTIVE_OR_AMBIGUOUS_WRITER")
    if (writer.get("status") != "completed" or writer.get("conclusion") != "success"
            or writer.get("event") not in ("schedule", "workflow_dispatch")
            or type(writer.get("id")) is not int
            or type(writer.get("run_attempt")) is not int or writer["run_attempt"] < 1
            or not isinstance(writer.get("head_sha"), str)
            or not SHA.fullmatch(writer["head_sha"])):
        return _abstain("NO_TRUSTED_SUCCESSFUL_WRITER")
    finished = stamp(writer.get("updated_at"))
    if not dt.timedelta(0) <= comment_time - finished <= dt.timedelta(minutes=20):
        return _abstain("OWNER_COMMAND_NOT_AFTER_FRESH_COMPLETED_WRITER")
    if now - finished > dt.timedelta(minutes=25):
        return _abstain("WRITER_TOO_OLD")
    if not isinstance(ledger_message, str) or ledger_message.strip() != (
            f"paper: atomic packed scan {writer['id']} source {writer['head_sha']}"):
        return _abstain("LATEST_LEDGER_WRITER_IDENTITY_MISMATCH")
    ledger.verify(state, MAX_RAW_BYTES)
    if (not state.get("runs") or state["runs"][-1].get("source_sha") != writer["head_sha"]
            or manifest.get("head", {}).get("generation") != state.get("generation")
            or manifest.get("head", {}).get("ledger_sha256") != state.get("sha256")):
        return _abstain("SEALED_LEDGER_SOURCE_OR_SHA_MISMATCH")
    shadows = shadow_runs["workflow_runs"]
    if len(shadows) >= 100:
        return _abstain("SHADOW_PAGINATION_AMBIGUITY")
    for shadow in shadows:
        if shadow.get("id") == current_run_id:
            continue
        if (shadow.get("name") != SHADOW or shadow.get("path") != SHADOW_PATH
                or shadow.get("repository", {}).get("full_name") != REPO):
            return _abstain("UNTRUSTED_SHADOW_RUN_HISTORY")
        if stamp(shadow.get("created_at")) < stamp(writer["created_at"]):
            continue
        # GitHub emits a skipped issue_comment workflow run for every unrelated
        # comment because this workflow listens to issue_comment: created.
        # Such a run has executed no shadow job and cannot deduplicate a real
        # authenticated fallback. Active/queued or non-skipped attempts still
        # block, as does any native workflow_run after the writer.
        if (shadow.get("event") == "issue_comment"
                and shadow.get("status") == "completed"
                and shadow.get("conclusion") == "skipped"):
            continue
        if shadow.get("event") not in ("workflow_run", "issue_comment"):
            return _abstain("UNEXPECTED_SHADOW_EVENT")
        return _abstain("SHADOW_ALREADY_TRIGGERED_OR_IN_PROGRESS")
    return {"action": "RUN_SHADOW", "trigger_paper_run_id": writer["id"],
            "writer_source_sha": writer["head_sha"],
            "ledger_generation": state["generation"],
            "ledger_sha256": state["sha256"], "mode": "READ_ONLY_OWNER_FALLBACK"}


def main(argv=None):
    p = argparse.ArgumentParser()
    for arg in ("event", "paper-runs", "shadow-runs", "ledger", "manifest",
                "ledger-message", "repository", "current-run-id", "checkout-sha",
                "output"):
        p.add_argument("--" + arg, required=True)
    a = p.parse_args(argv)
    read = lambda x: json.loads(Path(x).read_text())
    result = decide(read(a.event), read(a.paper_runs), read(a.shadow_runs),
                    read(a.ledger), read(a.manifest),
                    Path(a.ledger_message).read_text(),
                    repository=a.repository, current_run_id=int(a.current_run_id),
                    checkout_sha=a.checkout_sha, now=dt.datetime.now(dt.timezone.utc))
    Path(a.output).write_text(json.dumps(result, sort_keys=True) + "\n")
    print("LEGACY_OWNER_FALLBACK " + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
