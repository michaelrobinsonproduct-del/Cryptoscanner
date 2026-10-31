"""Local atomic staging for ONE future Git single-writer transaction.

Never pushes or schedules a scanner. Workflow integration must commit the
packed head and immutable segment in ONE non-force Git commit and verify
remote readback of both. Existing plain ledger remains untouched until an
independent migration gate explicitly authorizes conversion.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile

from . import ledger, segmented_storage as storage


def _write_sync(path, payload):
    with open(path, "xb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())


def _fsync_directory(directory):
    fd = os.open(str(directory), os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def prepare(previous_bytes, report, source_sha, destination):
    """Stage one complete atomic transaction in a new directory."""
    destination = Path(destination)
    if destination.exists():
        raise FileExistsError("Refuse to overwrite existing storage transaction")
    destination.parent.mkdir(parents=True, exist_ok=True)
    before = storage.unpack_snapshot(previous_bytes)
    packed, segment, score = storage.advance_segmented(
        previous_bytes, report, source_sha)
    after = storage.unpack_snapshot(packed)
    segment_name = "segment-%08d.json" % after["generation"]
    manifest = {"schema": "paper-segmented-transaction-v1",
                "generation": after["generation"],
                "previous_sha256": hashlib.sha256(previous_bytes).hexdigest(),
                "snapshot_sha256": hashlib.sha256(packed).hexdigest(),
                "segment_sha256": hashlib.sha256(segment).hexdigest(),
                "segment_name": segment_name,
                "before_ledger_sha256": before["sha256"],
                "after_ledger_sha256": after["sha256"]}
    staging = Path(tempfile.mkdtemp(prefix=".paper-txn-", dir=destination.parent))
    try:
        _write_sync(staging / "paper-ledger.packed.json", packed)
        _write_sync(staging / segment_name, segment)
        _write_sync(staging / "manifest.json", ledger.canonical(manifest))
        _write_sync(staging / "scoreboard.json", ledger.canonical(score))
        verify_prepared(previous_bytes, staging)
        _fsync_directory(staging)
        os.replace(staging, destination)
        _fsync_directory(destination.parent)
        return manifest
    finally:
        if staging.exists():
            shutil.rmtree(staging)


def verify_prepared(previous_bytes, directory):
    """Read back every staged byte and independently replay its transition."""
    directory = Path(directory)
    manifest = json.loads((directory / "manifest.json").read_bytes())
    if not isinstance(manifest, dict) or set(manifest) != {
            "schema", "generation", "previous_sha256", "snapshot_sha256",
            "segment_sha256", "segment_name", "before_ledger_sha256",
            "after_ledger_sha256"} or manifest["schema"] != "paper-segmented-transaction-v1":
        raise ValueError("Invalid transaction manifest")
    if (type(manifest["generation"]) is not int or manifest["generation"] < 1
            or manifest["segment_name"] != "segment-%08d.json" % manifest["generation"]):
        raise ValueError("Invalid transaction generation or filename")
    if {p.name for p in directory.iterdir()} != {
            "manifest.json", "scoreboard.json",
            "paper-ledger.packed.json", manifest["segment_name"]}:
        raise ValueError("Incomplete or unexpected transaction files")
    packed = (directory / "paper-ledger.packed.json").read_bytes()
    segment = (directory / manifest["segment_name"]).read_bytes()
    if (hashlib.sha256(previous_bytes).hexdigest() != manifest["previous_sha256"]
            or hashlib.sha256(packed).hexdigest() != manifest["snapshot_sha256"]
            or hashlib.sha256(segment).hexdigest() != manifest["segment_sha256"]):
        raise ValueError("Transaction byte checksum mismatch")
    before = storage.unpack_snapshot(previous_bytes)
    after = storage.unpack_snapshot(packed)
    replay = storage.replay_segments([segment], previous_bytes)
    if (after != replay or before["sha256"] != manifest["before_ledger_sha256"]
            or after["sha256"] != manifest["after_ledger_sha256"]
            or after["generation"] != manifest["generation"]):
        raise ValueError("Transaction ledger replay mismatch")
    score = json.loads((directory / "scoreboard.json").read_bytes())
    if score != ledger.scoreboard(after, storage.MAX_RAW_BYTES):
        raise ValueError("Transaction scoreboard mismatch")
    return manifest
