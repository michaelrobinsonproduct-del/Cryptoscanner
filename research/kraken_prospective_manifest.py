"""Deterministic offline partitioning for prospective Kraken source collection.

Planning is not collection; no network, scheduling, or episode certification.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

PAIR = re.compile(r"[A-Z0-9]{3,12}\Z")


def plan(raw, *, expected=48, batch_size=8):
    if not isinstance(raw, dict) or set(raw) != {"pairs"}:
        raise ValueError("manifest must contain only pairs")
    pairs = raw["pairs"]
    if not isinstance(pairs, list) or len(pairs) != expected:
        raise ValueError("incomplete source universe")
    if not all(isinstance(p, str) and PAIR.fullmatch(p) for p in pairs):
        raise ValueError("invalid pair identity")
    if len(set(pairs)) != len(pairs):
        raise ValueError("duplicate pair identity")
    if not 1 <= batch_size <= 8:
        raise ValueError("unsafe batch size")
    canonical = sorted(pairs)
    groups = [canonical[i:i + batch_size] for i in range(0, len(canonical), batch_size)]
    assert sum(map(len, groups)) == expected
    receipt = hashlib.sha256(json.dumps(canonical, separators=(",", ":")).encode()).hexdigest()
    return {"mode": "OFFLINE_PLAN_ONLY", "requested": expected, "batch_count": len(groups),
            "universe_sha256": receipt, "batches": groups,
            "snapshots_collected": 0, "certified_first_entry_episodes": 0,
            "held_out_lift": None, "production_applied": False}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    result = plan(json.loads(Path(args.manifest).read_text()))
    out = Path(args.output)
    if out.exists():
        raise ValueError("refuse to overwrite prior plan")
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")


if __name__ == "__main__":
    main()
