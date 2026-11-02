"""Read-only acceptance probe for converting a real paper ledger to packed storage.

Never writes Git refs, dispatches scans, promotes scoring or authenticates
market-event timestamps. This is migration readiness, not live activation.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

from . import ledger
from . import segmented_storage as storage
from .scanner import atomic_json

COMMIT_RE = re.compile(r"[0-9a-f]{40}")


def probe(raw, commit_sha):
    if not isinstance(commit_sha, str) or not COMMIT_RE.fullmatch(commit_sha):
        raise ValueError("Missing exact source ledger commit SHA")
    if not isinstance(raw, bytes) or not raw or len(raw) > ledger.MAX_BYTES:
        raise ValueError("Missing or oversized existing plain ledger")
    try:
        state = json.loads(raw)
    except (ValueError, UnicodeError) as exc:
        raise ValueError("Unparseable existing plain ledger") from exc
    ledger.verify(state)  # original stricter 12MB gate, not the expanded limit
    if raw != ledger.canonical(state):
        raise ValueError("Existing ledger bytes are not canonical")
    packed = storage.pack_snapshot(state)
    restored = storage.unpack_snapshot(packed)
    if restored != state or ledger.canonical(restored) != raw:
        raise ValueError("Lossless round-trip failed")
    if storage.pack_snapshot(restored) != packed:
        raise ValueError("Packed snapshot is nondeterministic")
    before = ledger.scoreboard(state)
    after = ledger.scoreboard(restored, storage.MAX_RAW_BYTES)
    if before != after or state["generation"] != before["actual_scans"]:
        raise ValueError("Scoreboard or generation regression")
    if state["generation"] < 1 or not state["runs"]:
        raise ValueError("No genuine persisted paper runs to migrate")
    evidence = {
        "status": "READ_ONLY_REAL_LEDGER_PACK_ROUNDTRIP_VERIFIED",
        "ledger_commit": commit_sha,
        "ledger_generation": state["generation"],
        "latest_scan_as_of": state["runs"][-1]["as_of"],
        "raw_bytes": len(raw),
        "packed_bytes": len(packed),
        "raw_file_sha256": hashlib.sha256(raw).hexdigest(),
        "packed_file_sha256": hashlib.sha256(packed).hexdigest(),
        "ledger_seal_sha256": state["sha256"],
        "actual_scans": before["actual_scans"],
        "immutable_predictions": before["immutable_predictions"],
        "market_observations": before["market_observations"],
        "matured_observed_labels": before["matured_labels"],
        "gap_abstentions": before["gap_abstentions"],
        "held_out_lift": None,
        "production_applied": False,
        "writer_migrated": False,
        "cadence_expanded": False,
    }
    return evidence, packed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--report-out", required=True)
    parser.add_argument("--packed-out", required=True)
    args = parser.parse_args()
    report, packed = probe(Path(args.ledger).read_bytes(), args.commit)
    output = Path(args.packed_out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(packed)  # artifact only, NEVER Git branch or ledger writer
    atomic_json(args.report_out, report)
    print("PAPER_LIVE_MIGRATION_ROUNDTRIP", json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
