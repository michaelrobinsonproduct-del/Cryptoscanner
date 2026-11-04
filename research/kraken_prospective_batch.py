"""Bounded, one-shot multi-market Kraken provenance batch. Research only.

Each response is retained byte-for-byte with a SHA256 receipt. This is NOT
continuous historical coverage, an exchange signature, or a trading signal.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import time

from research.kraken_prospective_provenance import _response, capture

MAX_PAIRS = 8
MAX_SECONDS = 180
PAIR_RE = re.compile(r"[A-Z0-9]{3,12}\Z")


def _atomic_new(path, raw):
    """Never silently replace existing evidence in this one-shot directory."""
    path = Path(path)
    if path.exists():
        raise ValueError("evidence path already exists")
    fd, tmp = tempfile.mkstemp(prefix=".source-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        # Caller uses a fresh directory; refuse pre-existing destination.
        if path.exists():
            raise ValueError("evidence path already exists")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def collect(pairs, directory, *, transport=_response, clock=time.time,
            monotonic=time.monotonic, sleep=time.sleep, max_seconds=MAX_SECONDS):
    pairs = list(pairs)
    if not 1 <= len(pairs) <= MAX_PAIRS or len(set(pairs)) != len(pairs):
        raise ValueError("invalid batch size or duplicate pair")
    if any(not isinstance(p, str) or not PAIR_RE.fullmatch(p) for p in pairs):
        raise ValueError("invalid pair in batch")
    if not 0 < max_seconds <= MAX_SECONDS:
        raise ValueError("invalid bounded time budget")
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=False)
    started = monotonic()
    entries = []
    for index, pair in enumerate(pairs):
        if monotonic() - started >= max_seconds:
            entries.append({"pair": pair, "status": "SKIPPED_BUDGET", "raw": []})
            continue
        raw_receipts = []

        def recording_transport(path):
            raw = transport(path)
            if not isinstance(raw, bytes):
                raise ValueError("source response must be bytes")
            stage = "depth" if "/Depth?" in path else "trades" if "/Trades?" in path else None
            if stage is None or any(r["stage"] == stage for r in raw_receipts):
                raise ValueError("unexpected or duplicate source endpoint")
            filename = f"{index:02d}-{pair}-{stage}.json"
            digest = hashlib.sha256(raw).hexdigest()
            _atomic_new(directory / filename, raw)
            raw_receipts.append({"stage": stage, "file": filename, "sha256": digest,
                                 "bytes": len(raw)})
            return raw

        try:
            evidence = capture(pair, transport=recording_transport, clock=clock)
            if len(raw_receipts) != 2 or evidence["depth_receipt"]["sha256"] != raw_receipts[0]["sha256"] or evidence["trades_receipt"]["sha256"] != raw_receipts[1]["sha256"]:
                raise ValueError("source receipt mismatch")
            filename = f"{index:02d}-{pair}-evidence.json"
            _atomic_new(directory / filename, (json.dumps(evidence, sort_keys=True, indent=2) + "\n").encode())
            entries.append({"pair": pair, "status": "ELIGIBLE" if evidence["eligible_point_in_time_snapshot"] else "STALE",
                            "evidence_file": filename, "source_market": evidence["pair_source"],
                            "raw": raw_receipts})
        except Exception as exc:
            # Preserve any partial raw evidence and the failure class; never claim coverage.
            entries.append({"pair": pair, "status": "INVALID",
                            "failure_class": type(exc).__name__, "raw": raw_receipts})
        if index + 1 < len(pairs):
            sleep(0.75)
    summary = {
        "schema": 1, "mode": "ONE_SHOT_PROSPECTIVE_PUBLIC_TLS_RESEARCH_ONLY",
        "source_limit": "TLS and response SHA256 are not exchange-signed",
        "pairs_requested": len(pairs),
        "pairs_eligible": sum(e["status"] == "ELIGIBLE" for e in entries),
        "pairs_stale": sum(e["status"] == "STALE" for e in entries),
        "pairs_invalid": sum(e["status"] == "INVALID" for e in entries),
        "pairs_budget_skipped": sum(e["status"] == "SKIPPED_BUDGET" for e in entries),
        "historical_first_observed_recovered": False,
        "certified_first_entry_episodes": 0, "held_out_lift": None,
        "production_applied": False, "entries": entries,
    }
    assert sum(summary[k] for k in ("pairs_eligible", "pairs_stale", "pairs_invalid", "pairs_budget_skipped")) == len(pairs)
    _atomic_new(directory / "manifest.json", (json.dumps(summary, sort_keys=True, indent=2) + "\n").encode())
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", default="XBTUSD,ETHUSD,SOLUSD,XRPUSD")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--round-index", help="append verified batch to durable research index")
    args = parser.parse_args()
    result = collect(args.pairs.split(","), args.output_dir)
    if args.round_index:
        from research.prospective_round_store import append_round
        receipt = append_round(args.round_index, args.output_dir)
        print("KRAKEN_ROUND_INDEXED", json.dumps(receipt, sort_keys=True))
    print("KRAKEN_PROSPECTIVE_BATCH", json.dumps({k: result[k] for k in
          ("pairs_requested", "pairs_eligible", "pairs_stale", "pairs_invalid", "pairs_budget_skipped")},
          sort_keys=True))


if __name__ == "__main__":
    main()
