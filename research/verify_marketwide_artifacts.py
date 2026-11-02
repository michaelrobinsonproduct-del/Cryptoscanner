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


def load_strict_json(path):
    # Python's default json.loads accepts NaN/Infinity, which are not JSON
    # numbers and can silently contaminate descriptive research artifacts.
    def reject_nonfinite(value):
        raise ValueError("nonfinite research JSON value: " + value)
    return json.loads(path.read_text(), parse_constant=reject_nonfinite)


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
    ledger = load_strict_json((base / LEDGER))
    outcomes = load_strict_json((base / FILES[0]))
    episodes = load_strict_json((base / FILES[1]))
    provenance = load_strict_json((base / FILES[2]))
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
    # Check the two independent evaluator reports, not only their checksums.
    # An internally resealed artifact with inconsistent outcomes is invalid.
    horizons = ("1", "6", "24", "48")
    if (set(outcomes.get("horizons", {})) != set(horizons)
        or set(episodes.get("horizons", {})) != set(horizons)):
        raise ValueError("missing or unexpected evaluation horizon")
    matching = {
        "eligible": "eligible", "matured": "matured",
        "immature": "immature", "abstain_gap": "abstain_gap",
        "movers_20": "movers_20", "movers": "movers_30",
        "watch_eligible": "watch_eligible",
        "watch_immature": "watch_immature",
        "watch_abstain_gap": "watch_abstain_gap",
        "watch_matured": "watch_matured",
        "watch_positive_20": "watch_20",
        "watch_positive": "watch_30",
        "watch_false_positive_20": "watch_false_positive_20",
        "watch_false_positive_30": "watch_false_positive_30",
        "missed_20": "missed_20", "missed_30": "missed_30",
    }
    for horizon in horizons:
        window = outcomes["horizons"][horizon]
        episode = episodes["horizons"][horizon]
        coverage = episode["coverage"]
        if any(coverage.get(k) != window.get(v) for k, v in matching.items()):
            raise ValueError("cross-report outcome mismatch: " + horizon)
        if (coverage["eligible"] != outcomes["observed_entry_count"]
            or coverage["eligible"] != (coverage["matured"] +
                coverage["immature"] + coverage["abstain_gap"])
            or coverage["watch_eligible"] != (coverage["watch_matured"] +
                coverage["watch_immature"] + coverage["watch_abstain_gap"])
            or coverage["movers_20"] != coverage["watch_positive_20"] + coverage["missed_20"]
            or coverage["movers"] != coverage["watch_positive"] + coverage["missed_30"]
            or episode["missed_mover_episodes_20"] != (episode["unique_mover_episodes_20"] -
                episode["watch_captured_episodes_20"])
            or episode["missed_mover_episodes_30"] != (episode["unique_mover_episodes"] -
                episode["watch_captured_episodes"])):
            raise ValueError("cross-report cohort partition mismatch: " + horizon)
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
