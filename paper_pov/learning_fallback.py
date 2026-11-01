"""Owner-authenticated read-only fallback when a completed PAPER writer has no learning run.

No network IO, scanner dispatch, ledger write, score promotion or trading.
All evidence is supplied by authenticated workflow API reads and a sealed ledger.
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
COMMAND = "/paper-learning-heartbeat"
PAPER = "Public Kraken Paper POV (scheduled, isolated ledger)"
PAPER_PATH = ".github/workflows/paper-pipeline.yml"
SHA = re.compile(r"^[0-9a-f]{40}$")
UTC = dt.timezone.utc


def stamp(value):
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ValueError("Missing strict UTC timestamp")
    value = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if value.utcoffset() != dt.timedelta(0):
        raise ValueError("Non-UTC timestamp")
    return value


def abstain(reason):
    return {"action": "ABSTAIN", "reason": reason, "paper_only": True}


def decide(event, paper_runs, learning_runs, comments, state, manifest,
           ledger_message, ledger_commit, *, repository, current_run_id,
           checkout_sha, now):
    """Fail closed on owner identity, run/ledger provenance, maturity and duplicates."""
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
            or not SHA.fullmatch(checkout_sha)
            or type(current_run_id) is not int or current_run_id <= 0):
        raise ValueError("Untrusted owner learning command")
    if not isinstance(now, dt.datetime) or now.tzinfo is None or now.utcoffset() is None:
        raise ValueError("Missing UTC evaluation time")
    now = now.astimezone(UTC)
    ledger.verify(state, MAX_RAW_BYTES)
    if (state.get("generation", 0) < 20 or not state.get("runs")
            or manifest.get("head", {}).get("generation") != state["generation"]
            or manifest.get("head", {}).get("ledger_sha256") != state["sha256"]
            or not isinstance(ledger_commit, str) or not SHA.fullmatch(ledger_commit)):
        raise ValueError("Unsealed or mismatched PAPER ledger")
    if not isinstance(paper_runs, list) or not paper_runs:
        raise ValueError("Missing authenticated PAPER run history")
    if not isinstance(learning_runs, list) or not isinstance(comments, list):
        raise ValueError("Missing learning or owner comment history")
    runs = sorted(paper_runs, key=lambda r: (stamp(r["created_at"]), r["id"]), reverse=True)
    writer = runs[0]
    if (type(writer.get("id")) is not int or writer["id"] <= 0
            or writer.get("name") != PAPER or writer.get("path") != PAPER_PATH
            or writer.get("repository", {}).get("full_name") != REPO
            or writer.get("head_repository", {}).get("full_name") != REPO
            or writer.get("head_branch") != "main"
            or writer.get("event") not in ("schedule", "workflow_dispatch")
            or writer.get("status") != "completed" or writer.get("conclusion") != "success"
            or writer.get("run_attempt") != 1
            or not isinstance(writer.get("head_sha"), str)
            or not SHA.fullmatch(writer["head_sha"])
            or state["runs"][-1]["source_sha"] != writer["head_sha"]
            or ledger_message != f"paper: atomic packed scan {writer['id']} source {writer['head_sha']}"):
        return abstain("LATEST_WRITER_NOT_EXACT_DURABLE_SUCCESS")
    started = stamp(writer["created_at"])
    completed = stamp(writer["updated_at"])
    as_of = dt.datetime.fromisoformat(state["runs"][-1]["as_of"])
    if as_of.tzinfo is None or as_of.utcoffset() is None:
        raise ValueError("Naive ledger as-of")
    as_of = as_of.astimezone(UTC)
    age = (now - completed).total_seconds()
    if not (started <= as_of <= completed <= now and 90 <= age <= 1800):
        return abstain("WRITER_NOT_MATURE_OR_TOO_OLD")
    command_id = event.get("comment", {}).get("id")
    if type(command_id) is not int or command_id <= 0:
        raise ValueError("Missing owner comment identity")
    exact_commands = [c for c in comments
                      if c.get("body") == COMMAND
                      and c.get("user", {}).get("login") == OWNER
                      and c.get("user", {}).get("id") == OWNER_ID
                      and stamp(c["created_at"]) >= completed]
    if len(exact_commands) != 1 or exact_commands[0].get("id") != command_id:
        return abstain("DUPLICATE_OR_MISSING_OWNER_COMMAND")
    if not (completed <= stamp(exact_commands[0]["created_at"]) <= now):
        return abstain("OWNER_COMMAND_TIME_INVALID")
    # The API returns at most 100 runs. Never infer absence of a native
    # workflow_run if the visible page does not reach this writer's start.
    if (len(learning_runs) >= 100 and
            min(stamp(item["created_at"]) for item in learning_runs) > started):
        return abstain("LEARNING_HISTORY_TRUNCATED")
    for learning in learning_runs:
        if type(learning.get("id")) is not int:
            raise ValueError("Untrusted learning run ID")
        if learning["id"] == current_run_id:
            continue
        if (learning.get("event") == "workflow_run"
                and stamp(learning["created_at"]) >= started):
            return abstain("AUTOMATIC_LEARNING_EXISTS_OR_AMBIGUOUS")
    return {"action": "RUN_READ_ONLY_LEARNING", "reason": "SEALED_WRITER_MISSING_AUTOMATIC_LEARNING",
            "paper_only": True, "writer_run_id": writer["id"],
            "writer_event": writer["event"], "writer_source_sha": writer["head_sha"],
            "ledger_commit": ledger_commit, "ledger_generation": state["generation"],
            "ledger_sha256": state["sha256"], "learning_source_sha": checkout_sha,
            "owner_command_id": command_id, "evaluation_as_of": state["runs"][-1]["as_of"]}


def main(argv=None):
    p = argparse.ArgumentParser()
    for name in ("event", "paper-runs", "learning-runs", "comments", "ledger",
                 "manifest", "ledger-message", "ledger-commit", "repository",
                 "current-run-id", "checkout-sha", "output"):
        p.add_argument("--" + name, required=True)
    a = p.parse_args(argv)
    read = lambda path: json.loads(Path(path).read_text())
    lines = [json.loads(line) for line in Path(a.comments).read_text().splitlines() if line.strip()]
    decision = decide(read(a.event), read(a.paper_runs)["workflow_runs"],
                      read(a.learning_runs)["workflow_runs"], lines, read(a.ledger),
                      read(a.manifest), Path(a.ledger_message).read_text().strip(),
                      Path(a.ledger_commit).read_text().strip(),
                      repository=a.repository, current_run_id=int(a.current_run_id),
                      checkout_sha=a.checkout_sha, now=dt.datetime.now(UTC))
    Path(a.output).write_text(json.dumps(decision, sort_keys=True) + "\n")
    print("PAPER_LEARNING_OWNER_FALLBACK", json.dumps(decision, sort_keys=True))
    return decision


if __name__ == "__main__":
    main()
