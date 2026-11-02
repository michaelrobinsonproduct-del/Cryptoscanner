"""Fail-closed, read-only integrity check for marketwide research artifacts.

This checks *artifact identity*, not exchange authentication or predictive lift.
The PAPER ledger is separately verified by segmented_repository full replay.
"""
import argparse
import hashlib
import json
from pathlib import Path

FILES = ("marketwide-outcomes.json", "marketwide-episodes.json",
         "marketwide-provenance.json")
LEDGER = "verified-paper-ledger.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_artifacts(directory, expected_head, expected_ledger_commit):
    base = Path(directory)
    if not isinstance(expected_head, str) or len(expected_head) != 40 or any(
            c not in "0123456789abcdef" for c in expected_head):
        raise ValueError("invalid expected exact source commit")
    if not isinstance(expected_ledger_commit, str) or len(expected_ledger_commit) != 40 or any(
            c not in "0123456789abcdef" for c in expected_ledger_commit):
        raise ValueError("invalid expected remote ledger commit")
    required = (*FILES, LEDGER, "marketwide-SHA256SUMS")
    for name in required:
        path = base / name
        if not path.is_file() or path.is_symlink():
            raise ValueError("missing or unsafe research evidence: " + name)
    lines = (base / "marketwide-SHA256SUMS").read_text().splitlines()
    expected = {}
    for line in lines:
        parts = line.split("  ", 1)
        if len(parts) != 2 or len(parts[0]) != 64 or any(
                c not in "0123456789abcdef" for c in parts[0]):
            raise ValueError("invalid SHA256SUMS entry")
        value, name = parts
        if name not in FILES or name in expected:
            raise ValueError("unexpected or repeated SHA256SUMS entry")
        expected[name] = value
    if set(expected) != set(FILES):
        raise ValueError("missing SHA256SUMS entry")
    for name in FILES:
        if digest(base / name) != expected[name]:
            raise ValueError("report checksum mismatch: " + name)
    ledger = json.loads((base / LEDGER).read_text())
    outcomes = json.loads((base / FILES[0]).read_text())
    episodes = json.loads((base / FILES[1]).read_text())
    provenance = json.loads((base / FILES[2]).read_text())
    if provenance.get("research_source_commit") != expected_head:
        raise ValueError("source head mismatch")
    if provenance.get("paper_ledger_branch_commit") != expected_ledger_commit:
        raise ValueError("remote ledger commit mismatch")
    for name, key in ((LEDGER, "verified_ledger_export_sha256"),
                      (FILES[0], "outcome_report_sha256"),
                      (FILES[1], "episode_report_sha256")):
        if provenance.get(key) != digest(base / name):
            raise ValueError("provenance checksum mismatch: " + name)
    if (episodes.get("source", {}).get("ledger_sha256") != ledger.get("sha256")
        or episodes.get("source", {}).get("generation") != ledger.get("generation")
        or episodes.get("source", {}).get("runs") != outcomes.get("observed_run_count")
        or episodes.get("source", {}).get("observations") != outcomes.get("observed_entry_count")
        or provenance.get("observed_run_count") != outcomes.get("observed_run_count")
        or provenance.get("observed_entry_count") != outcomes.get("observed_entry_count")):
        raise ValueError("cross-report ledger identity mismatch")
    for source in (outcomes, episodes.get("source", {}), provenance):
        if (source.get("source_authenticated") is not False
            or source.get("complete_market_history") is not False
            or source.get("eligible_for_model_promotion") is not False):
            raise ValueError("unverified research evidence claims authentication/promotion")
    return {"research_source_commit": expected_head,
            "ledger_sha256": ledger["sha256"],
            "generation": ledger["generation"],
            "reports_checked": len(FILES)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--directory", required=True)
    p.add_argument("--expected-head", required=True)
    p.add_argument("--expected-ledger-commit", required=True)
    args = p.parse_args()
    print(json.dumps(verify_artifacts(args.directory, args.expected_head,
                                      args.expected_ledger_commit),
                     sort_keys=True))


if __name__ == "__main__":
    main()
