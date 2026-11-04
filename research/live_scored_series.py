"""Research-only scored prospective series: one immutable entry score, then real depth.

Each later round is a distinct Kraken acquisition at its actual collection time.
Never re-score historical rows or synthesize a missing five-minute observation.
This module has no scheduler, production ledger writer or trading capability.
"""
import argparse
import json
import time
from pathlib import Path

from research.live_score_depth_round import run as capture_entry
from research.acquisition_receipt_pipeline import load_captures
from research.kraken_prospective_batch import collect, MAX_PAIRS
from research.prospective_round_store import append_round, evaluate_index

MAX_ROUNDS = 13
MIN_INTERVAL_SECONDS = 300


def capture_scored_series(output_root, *, rounds=13, interval_seconds=300,
                          clock=time.monotonic, sleep=time.sleep,
                          entry_capture=capture_entry, collector=collect,
                          indexer=append_round, evaluate=evaluate_index):
    """One scored entry plus up to twelve factual five-minute follow-up rounds."""
    if type(rounds) is not int or not 2 <= rounds <= MAX_ROUNDS:
        raise ValueError("series requires 2 to 13 real rounds")
    if type(interval_seconds) is not int or interval_seconds < MIN_INTERVAL_SECONDS:
        raise ValueError("series interval must be at least 300 seconds")
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    started = clock()
    entry_root = root / "entry"
    entry = entry_capture(entry_root)
    if entry.get("mode") != "RESEARCH_ONLY_PROSPECTIVE_SCORE_DEPTH" or entry.get("production_applied") is not False:
        raise ValueError("entry is not a research-only scored depth capture")
    scores = load_captures(entry_root / "scores")
    pairs = list(dict.fromkeys(row["pair"] for row in scores))
    if not 1 <= len(pairs) <= MAX_PAIRS:
        raise ValueError("invalid scored entry market universe")
    index = entry_root / "round-index.jsonl"
    if not index.is_file() or len(index.read_text().splitlines()) != 1:
        raise ValueError("entry depth round not indexed exactly once")
    for number in range(1, rounds):
        target = started + number * interval_seconds
        delay = target - clock()
        if delay > 0:
            sleep(delay)
        # A late acquisition remains a late observation; no catch-up/backdating.
        directory = root / ("depth-%03d" % number)
        collector(pairs, directory)
        indexer(index, directory)
    # This verifies every retained manifest and evaluates only genuine coverage.
    coverage = {str(h): evaluate(index, h) for h in (1, 6, 24, 48)}
    result = {"mode": "RESEARCH_ONLY_SCORED_PROSPECTIVE_SERIES",
              "rounds_indexed": rounds, "scored_pairs": pairs,
              "round_index": str(index), "coverage": coverage,
              "production_applied": False, "trading_approved": False}
    # An independent, create-only summary; originals and score receipts unchanged.
    with (root / "series-report.json").open("x", encoding="utf-8") as handle:
        json.dump(result, handle, sort_keys=True, allow_nan=False)
        handle.write("\n")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--rounds", type=int, default=13)
    parser.add_argument("--interval-seconds", type=int, default=300)
    args = parser.parse_args()
    print(json.dumps(capture_scored_series(args.output_root, rounds=args.rounds,
                 interval_seconds=args.interval_seconds), sort_keys=True))


if __name__ == "__main__":
    main()
