"""Fail-closed provenance for read-only learning triggered by a completed PAPER writer.

No dispatch, writer, promotion or external IO. The workflow independently reads
the GitHub API and sealed ledger before producing sampled-quote evidence.
"""
import argparse
import json
import re
from pathlib import Path

from paper_pov import ledger
from paper_pov.segmented_storage import MAX_RAW_BYTES

REPO = "michaelrobinsonproduct-del/Cryptoscanner"
NAME = "Public Kraken Paper POV (scheduled, isolated ledger)"
PATH = ".github/workflows/paper-pipeline.yml"
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def verify_run(event, api, repository, checkout_sha):
    if repository != REPO or event.get("action") != "completed":
        raise ValueError("Untrusted repository or incomplete workflow event")
    if event.get("repository", {}).get("full_name") != REPO:
        raise ValueError("Event repository mismatch")
    triggered = event.get("workflow_run")
    if not isinstance(triggered, dict):
        raise ValueError("Missing triggering workflow")
    fields = ("id", "run_attempt", "head_sha", "head_branch", "event",
              "name", "path", "status", "conclusion")
    if any(triggered.get(k) != api.get(k) for k in fields):
        raise ValueError("GitHub API and event provenance mismatch")
    if (type(api.get("id")) is not int or api["id"] <= 0 or
            type(api.get("run_attempt")) is not int or api["run_attempt"] < 1 or
            api.get("name") != NAME or api.get("path") != PATH or
            api.get("status") != "completed" or api.get("conclusion") != "success" or
            api.get("event") not in ("schedule", "workflow_dispatch") or
            api.get("head_branch") != "main" or
            api.get("repository", {}).get("full_name") != REPO or
            api.get("head_repository", {}).get("full_name") != REPO or
            not isinstance(api.get("head_sha"), str) or
            not SHA40.fullmatch(api["head_sha"]) or
            not isinstance(checkout_sha, str) or not SHA40.fullmatch(checkout_sha)):
        raise ValueError("Not a successful trusted main PAPER writer")
    return {"writer_run_id": api["id"], "writer_run_attempt": api["run_attempt"],
            "writer_source_sha": api["head_sha"], "writer_event": api["event"],
            "learning_source_sha": checkout_sha}


def select_commit(lines, provenance):
    subject = ("paper: atomic packed scan " + str(provenance["writer_run_id"]) +
               " source " + provenance["writer_source_sha"])
    matches = []
    for line in lines.splitlines():
        sha, separator, message = line.partition(" ")
        if separator and message == subject:
            if not SHA40.fullmatch(sha):
                raise ValueError("Malformed matching ledger commit")
            matches.append(sha)
    if len(matches) != 1:
        raise ValueError("Missing or duplicate immutable writer ledger commit")
    return matches[0]


def verify_export(state, manifest, provenance):
    ledger.verify(state, MAX_RAW_BYTES)
    if (state.get("generation", 0) < 20 or not state.get("runs") or
            state["runs"][-1]["source_sha"] != provenance["writer_source_sha"] or
            manifest.get("head", {}).get("generation") != state["generation"] or
            manifest.get("head", {}).get("ledger_sha256") != state["sha256"]):
        raise ValueError("Sealed ledger generation/source/checksum mismatch")
    return {"generation": state["generation"], "ledger_sha256": state["sha256"],
            **provenance}


def main(argv=None):
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="command", required=True)
    a = sub.add_parser("verify-run")
    for arg in ("event", "api", "repository", "checkout-sha"):
        a.add_argument("--" + arg, required=True)
    b = sub.add_parser("select-commit")
    b.add_argument("--provenance", required=True)
    b.add_argument("--commits", required=True)
    c = sub.add_parser("verify-ledger")
    for arg in ("provenance", "ledger", "manifest"):
        c.add_argument("--" + arg, required=True)
    args = p.parse_args(argv)
    load = lambda path: json.loads(Path(path).read_text())
    if args.command == "verify-run":
        print(json.dumps(verify_run(load(args.event), load(args.api),
                                    args.repository, args.checkout_sha), sort_keys=True))
    elif args.command == "select-commit":
        print(select_commit(Path(args.commits).read_text(), load(args.provenance)))
    else:
        print(json.dumps(verify_export(load(args.ledger), load(args.manifest),
                                       load(args.provenance)), sort_keys=True))


if __name__ == "__main__":
    main()
