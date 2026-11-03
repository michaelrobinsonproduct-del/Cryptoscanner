"""E1 durable, append-only index for verified Kraken prospective batch rounds.

Each committed record points to immutable source files in a batch directory.
This is research-only; never writes production ledger or modifies source bytes.
"""
import hashlib
import json
import os
from pathlib import Path

from research.prospective_outcome_adapter import verified_rows
from research.prospective_round_assembler import evaluate_rounds


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def append_round(index_path, batch_directory):
    index = Path(index_path)
    batch = Path(batch_directory).resolve(strict=True)
    manifest = batch / "manifest.json"
    verified, abstentions = verified_rows(batch)
    manifest_sha = _sha(manifest)
    record = {"batch": str(batch), "manifest_sha256": manifest_sha,
              "snapshots_verified": len(verified), "abstentions": len(abstentions)}
    index.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive append under an advisory lock, with fsync before returning.
    # Never rewrite previous records or silently accept a duplicate batch.
    import fcntl
    with index.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        handle.seek(0)
        existing = [json.loads(line) for line in handle if line.strip()]
        if any(r["batch"] == str(batch) for r in existing):
            raise ValueError("duplicate batch")
        handle.seek(0, os.SEEK_END)
        handle.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    return record


def evaluate_index(index_path, horizon_hours=1):
    index = Path(index_path)
    records = [json.loads(line) for line in index.read_text().splitlines() if line.strip()]
    if len({r["batch"] for r in records}) != len(records):
        raise ValueError("duplicate batch in index")
    for record in records:
        if _sha(Path(record["batch"]) / "manifest.json") != record["manifest_sha256"]:
            raise ValueError("manifest changed after index append")
    result = evaluate_rounds([r["batch"] for r in records], horizon_hours)
    if result["snapshots_verified"] != sum(r["snapshots_verified"] for r in records):
        raise ValueError("indexed snapshot coverage mismatch")
    return result
