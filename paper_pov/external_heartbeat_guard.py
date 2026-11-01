"""Strict, side-effect-free authorization for the owner issue-comment heartbeat.

This does not dispatch workflows, fetch market data, or touch the ledger.
Only an independently reviewed GitHub workflow may consume its fixed intent.
"""
import argparse
import datetime as dt
import json
from pathlib import Path

REPOSITORY = "michaelrobinsonproduct-del/Cryptoscanner"
OWNER = "michaelrobinsonproduct-del"
OWNER_ID = 336805669
ISSUE_NUMBER = 34
COMMAND = "PAPER_RECOVERY_WAKE_V1"
WORKFLOW = "paper-recovery.yml"
REF = "main"
UTC = dt.timezone.utc
MAX_EVENT_AGE = dt.timedelta(minutes=30)
CLOCK_SKEW = dt.timedelta(minutes=2)


def _utc_timestamp(value):
    if not isinstance(value, str):
        raise ValueError("Missing immutable GitHub creation timestamp")
    try:
        timestamp = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Invalid GitHub creation timestamp") from exc
    if timestamp.tzinfo is None:
        raise ValueError("Naive GitHub creation timestamp")
    return timestamp.astimezone(UTC)


def _owner_identity(value):
    return (isinstance(value, dict)
            and value.get("login") == OWNER
            and type(value.get("id")) is int
            and value["id"] == OWNER_ID)


def authorize(event, *, repository, actor, ref, event_name, now=None):
    """Validate GitHub's event envelope, returning a fixed recovery-only intent.

    The issue body is NEVER a shell command or workflow name. A successful
    authorization is not proof of GitHub token permissions or dispatch.
    """
    if not isinstance(event, dict):
        raise ValueError("Malformed GitHub event")
    if (repository != REPOSITORY or actor != OWNER
            or ref != "refs/heads/main" or event_name != "issue_comment"):
        raise ValueError("Untrusted GitHub execution context")
    if event.get("action") != "created":
        raise ValueError("Only new comments can trigger the heartbeat")
    repo = event.get("repository")
    if (not isinstance(repo, dict) or repo.get("full_name") != REPOSITORY
            or repo.get("default_branch") != REF
            or not _owner_identity(repo.get("owner"))):
        raise ValueError("Unexpected repository or default branch")
    issue = event.get("issue")
    if (not isinstance(issue, dict)
            or type(issue.get("number")) is not int
            or issue["number"] != ISSUE_NUMBER
            or issue.get("pull_request") is not None
            or issue.get("state") != "open"):
        raise ValueError("Not the open issue #34")
    comment = event.get("comment")
    if not isinstance(comment, dict):
        raise ValueError("Missing immutable comment")
    if (type(comment.get("id")) is not int or comment["id"] <= 0
            or comment.get("body") != COMMAND
            or comment.get("author_association") != "OWNER"
            or not _owner_identity(comment.get("user"))
            or not _owner_identity(event.get("sender"))):
        raise ValueError("Untrusted author, sender, or exact command")
    timestamp = _utc_timestamp(comment.get("created_at"))
    current = dt.datetime.now(UTC) if now is None else now
    if not isinstance(current, dt.datetime) or current.tzinfo is None:
        raise ValueError("Untrusted local clock")
    current = current.astimezone(UTC)
    if timestamp > current + CLOCK_SKEW or current - timestamp > MAX_EVENT_AGE:
        raise ValueError("Stale or future-dated heartbeat")
    return {
        "schema": 1,
        "paper_only": True,
        "repository": REPOSITORY,
        "issue": ISSUE_NUMBER,
        "comment_id": comment["id"],
        "comment_created_at": timestamp.isoformat(),
        "workflow": WORKFLOW,
        "ref": REF,
        "action": "REQUEST_EXISTING_RECOVERY_CONTROLLER_ONLY",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--actor", required=True)
    parser.add_argument("--ref", required=True)
    parser.add_argument("--event-name", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.unlink(missing_ok=True)
    event = json.loads(Path(args.event).read_text())
    intent = authorize(event, repository=args.repository, actor=args.actor,
                       ref=args.ref, event_name=args.event_name)
    output.write_text(json.dumps(intent, sort_keys=True, allow_nan=False) + "\n")
    print("PAPER_OWNER_HEARTBEAT_AUTHORIZED", intent["comment_id"],
          "EXISTING_RECOVERY_ONLY")


if __name__ == "__main__":
    main()
