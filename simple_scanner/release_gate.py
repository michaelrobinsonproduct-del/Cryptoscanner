"""Fail-closed release evidence gate. Never deploys or mutates production."""
import argparse
import json
from pathlib import Path

REQUIRED = ("actual_history_replay", "identity_coverage", "scoring_parity",
            "learning_invariance", "end_to_end", "rollback_verified")

def validate(evidence, expected_sha):
    if not isinstance(evidence, dict) or evidence.get("commit_sha") != expected_sha:
        raise ValueError("Evidence must match exact release commit")
    for key in REQUIRED:
        record = evidence.get(key)
        if not isinstance(record, dict) or record.get("passed") is not True:
            raise ValueError("Missing passing release gate: " + key)
    replay = evidence["actual_history_replay"]
    if replay.get("source") != "production_sqlite_backup" or type(replay.get("rows")) is not int or replay["rows"] <= 0:
        raise ValueError("Real historical replay evidence required")
    identity = evidence["identity_coverage"]
    if type(identity.get("verified")) is not int or type(identity.get("total")) is not int or identity["verified"] <= 0 or identity["verified"] != identity["total"]:
        raise ValueError("Canonical identities must cover all evaluated rows")
    if evidence["rollback_verified"].get("production_commit"):
        if not isinstance(evidence["rollback_verified"]["production_commit"], str):
            raise ValueError("Rollback commit invalid")
    return True

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--commit-sha", required=True)
    args = parser.parse_args()
    validate(json.loads(Path(args.evidence).read_text()), args.commit_sha)
    print("RELEASE_GATE_PASS " + args.commit_sha)

if __name__ == "__main__":
    main()
