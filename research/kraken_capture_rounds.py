"""Bounded manual Kraken prospective capture rounds, research-only.

No scheduler, no production writer, no scoring. Each round has its own
immutable directory and is appended to the verified research index.
"""
import argparse
import json
from pathlib import Path
import time

from research.kraken_prospective_batch import collect, MAX_PAIRS
from research.prospective_round_store import append_round, evaluate_index

MAX_ROUNDS = 13  # entry plus twelve five-minute forward slots for a 1h outcome
MIN_INTERVAL_SECONDS = 300


def capture_rounds(pairs, output_root, *, rounds=2, interval_seconds=300,
                   collector=collect, clock=time.monotonic, sleep=time.sleep):
    pairs = list(pairs)
    if not 1 <= rounds <= MAX_ROUNDS:
        raise ValueError("rounds out of bounds")
    if not 1 <= len(pairs) <= MAX_PAIRS or len(set(pairs)) != len(pairs):
        raise ValueError("invalid market universe")
    if interval_seconds < MIN_INTERVAL_SECONDS:
        raise ValueError("interval must be at least five minutes")
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    index = root / "rounds.jsonl"
    started = clock()
    records = []
    for number in range(rounds):
        target = started + number * interval_seconds
        wait = target - clock()
        if wait > 0:
            sleep(wait)
        directory = root / ("round-%03d" % number)
        collector(pairs, directory)
        records.append(append_round(index, directory))
    return {"rounds_indexed": len(records),
            "index": str(index),
            "coverage": evaluate_index(index, 1)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", default="XBTUSD,ETHUSD,SOLUSD,XRPUSD")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--rounds", type=int, default=2)
    parser.add_argument("--interval-seconds", type=int, default=300)
    args = parser.parse_args()
    result = capture_rounds(args.pairs.split(","), args.output_root,
                            rounds=args.rounds,
                            interval_seconds=args.interval_seconds)
    print("KRAKEN_ROUND_CAPTURE", json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
