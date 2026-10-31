"""Validate an owner-only GitHub issue command before dispatching the existing paper scanner.

This module NEVER fetches market data or writes a ledger. The sole writer remains
.github/workflows/paper-pipeline.yml with its non-cancelling concurrency group.
"""
import argparse
import json
from pathlib import Path

REPOSITORY = "michaelrobinsonproduct-del/Cryptoscanner"
OWNER = "michaelrobinsonproduct-del"
ISSUE = 34
COMMAND = "/paper-scan"


def authorize(event, repository):
    """Return a fixed dispatch intent; fail closed on every untrusted field."""
    if not isinstance(event, dict) or repository != REPOSITORY:
        raise ValueError("Wrong repository or malformed event")
    if event.get("action") != "created":
        raise ValueError("Only newly created issue comments can trigger scans")
    if not isinstance(event.get("repository"), dict) or event["repository"].get("full_name") != REPOSITORY:
        raise ValueError("Event repository mismatch")
    issue = event.get("issue")
    if not isinstance(issue, dict) or type(issue.get("number")) is not int or issue["number"] != ISSUE:
        raise ValueError("Only the designated scanner issue can trigger scans")
    if issue.get("pull_request") is not None:
        raise ValueError("Pull request comments cannot trigger scans")
    comment = event.get("comment")
    sender = event.get("sender")
    if not isinstance(comment, dict) or not isinstance(sender, dict):
        raise ValueError("Missing authenticated GitHub comment identity")
    user = comment.get("user")
    if (not isinstance(user, dict) or user.get("login") != OWNER
            or sender.get("login") != OWNER
            or comment.get("author_association") != "OWNER"):
        raise ValueError("Only an owner-authored comment can trigger scans")
    if comment.get("body") != COMMAND:
        raise ValueError("Only the exact paper-scan command is accepted")
    if type(comment.get("id")) is not int or comment["id"] <= 0:
        raise ValueError("Missing immutable comment identifier")
    return {
        "repository": REPOSITORY, "issue": ISSUE,
        "comment_id": comment["id"], "workflow": "paper-pipeline.yml",
        "ref": "main", "paper_only": True,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    event = json.loads(Path(args.event).read_text())
    intent = authorize(event, args.repository)
    Path(args.output).write_text(json.dumps(intent, sort_keys=True) + "\n")
    print("PAPER_OWNER_COMMAND_AUTHORIZED", intent["comment_id"], intent["workflow"])


if __name__ == "__main__":
    main()
