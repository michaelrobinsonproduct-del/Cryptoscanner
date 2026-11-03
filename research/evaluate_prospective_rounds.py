"""Research-only evaluation of retained rounds across independent capture jobs.

An explicit index of immutable batch directories is the input. The command
never collects, trades, scores or writes a production ledger.
"""
import argparse
import json
from pathlib import Path

from research.prospective_round_store import append_round, evaluate_index


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", required=True)
    parser.add_argument("--horizon-hours", type=int, choices=(1, 6, 24, 48), default=1)
    parser.add_argument("--append-batch", action="append", default=[])
    args = parser.parse_args()
    for batch in args.append_batch:
        append_round(args.index, batch)
    result = evaluate_index(args.index, args.horizon_hours)
    statuses = {}
    for outcome in result["outcomes"]:
        status = outcome["status"]
        statuses[status] = statuses.get(status, 0) + 1
    print("KRAKEN_PROSPECTIVE_ROUND_COVERAGE", json.dumps({
        "rounds_verified": result["rounds_verified"],
        "snapshots_verified": result["snapshots_verified"],
        "qualified_first_entry_episodes": result["qualified_first_entry_episodes"],
        "outcome_status_counts": statuses,
        "held_out_lift": result["held_out_lift"],
        "production_applied": result["production_applied"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
