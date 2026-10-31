"""Independent bounded Git-history audit for the public paper ledger.

This checks a first-parent sequence of immutable Git snapshots, not just the
latest parent transition. It is read-only and cannot certify exchange-complete
prices, 30-day artifact restoration, or predictive lift.
"""
import argparse
import hashlib
import json
from pathlib import Path

from paper_eval.continuity import verify_transition
from paper_pov import ledger
from paper_pov.scanner import atomic_json

MAX_TRANSITIONS = 16


def _sha(value):
    return (isinstance(value, str) and len(value) == 40
            and all(c in "0123456789abcdef" for c in value))


def verify_chain(entries, tip, max_transitions=MAX_TRANSITIONS):
    """entries are newest-first adjacent first-parent Git ledger snapshots.

    Caller must obtain commit ancestry independently from Git. Refuse a
    truncated history unless it reaches the explicit transition bound.
    """
    if type(max_transitions) is not int or not 1 <= max_transitions <= MAX_TRANSITIONS:
        raise ValueError("Invalid bounded transition limit")
    if not _sha(tip) or not isinstance(entries, list) or not entries:
        raise ValueError("Missing exact Git tip or ledger snapshots")
    if len(entries) > max_transitions + 1:
        raise ValueError("Unbounded ledger history input")
    commits = [e.get("commit") for e in entries if isinstance(e, dict)]
    if len(commits) != len(entries) or any(not _sha(c) for c in commits):
        raise ValueError("Invalid immutable ledger commit")
    if len(set(commits)) != len(commits) or commits[0] != tip:
        raise ValueError("Duplicate commit or ledger tip mismatch")
    for entry in entries:
        ledger.verify(entry["state"])
    latest = entries[0]["state"]
    oldest = entries[-1]["state"]
    # Every adjacent pair must be a genuine single append. A missing middle
    # generation, forged archive, or rewritten earlier prediction fails.
    transitions = []
    for newer, older in zip(entries, entries[1:]):
        transitions.append(verify_transition(older["state"], newer["state"]))
    if latest["generation"] - oldest["generation"] != len(transitions):
        raise ValueError("Skipped or repeated ledger generation")
    complete = oldest["generation"] == 0
    if not complete and len(transitions) != max_transitions:
        raise ValueError("History truncated before genesis or bounded limit")
    if complete and oldest["runs"]:
        raise ValueError("Generation-zero ledger is not empty")
    return {
        "schema": 1,
        "mode": "READ_ONLY_BOUNDED_PAPER_LEDGER_CHAIN",
        "tip_commit": tip,
        "tip_generation": latest["generation"],
        "tip_ledger_sha256": latest["sha256"],
        "oldest_commit": commits[-1],
        "oldest_generation": oldest["generation"],
        "snapshots_checked": len(entries),
        "transitions_checked": len(transitions),
        "max_transitions": max_transitions,
        "verified_to_genesis": complete,
        "bounded_history_only": not complete,
        "all_prior_transitions_immutable": True,
        "compacted_runs_verified": sum(x["compacted_runs"] for x in transitions),
        "compacted_sampled_hits_verified": sum(
            x["reconstructed_compacted_sampled_hits"] for x in transitions),
        "independent_held_out_lift": None,
        "production_applied": False,
        "limitations": ("Adjacent Git first-parent commits are supplied by the "
                        "read-only workflow; client-observed sampled quotes "
                        "are not authenticated exchange highs. Bounded chain "
                        "is not proof of 30-day artifact restore or strategy lift.")
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--tip", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    # TSV from 'git rev-list --first-parent'; each line is commit + local
    # immutable snapshot path. Never execute commands from manifest content.
    rows = [line.split("\t") for line in Path(args.manifest).read_text().splitlines()]
    if any(len(row) != 2 for row in rows):
        raise ValueError("Invalid Git snapshot manifest")
    entries = [{"commit": sha, "state": json.loads(Path(path).read_text())}
               for sha, path in rows]
    result = verify_chain(entries, args.tip)
    result["report_sha256"] = hashlib.sha256(ledger.canonical(result)).hexdigest()
    atomic_json(args.output, result)
    if json.loads(Path(args.output).read_text()) != result:
        raise ValueError("Atomic chain audit readback mismatch")
    print("PAPER_LEDGER_CHAIN_AUDIT", json.dumps({
        "tip_commit": result["tip_commit"],
        "tip_generation": result["tip_generation"],
        "transitions_checked": result["transitions_checked"],
        "verified_to_genesis": result["verified_to_genesis"],
        "bounded_history_only": result["bounded_history_only"],
        "report_sha256": result["report_sha256"],
        "production_applied": False
    }, sort_keys=True))


if __name__ == "__main__":
    main()
