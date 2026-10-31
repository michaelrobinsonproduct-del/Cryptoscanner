"""Git-native, fail-closed repository layout for the single paper ledger writer.

Only stages files locally. The caller must commit all changed files in ONE Git
commit, non-force push with optimistic ref check, then independently fetch and
byte-compare the remote manifest, snapshot and new segment. This module NEVER
pushes, dispatches, schedules, trades, or modifies the live ledger branch.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile

from . import ledger, segmented_storage as storage

SCHEMA = "paper-git-segment-manifest-v1"
CHECKPOINT = "paper-ledger.checkpoint.json"
SNAPSHOT = "paper-ledger.packed.json"
MANIFEST = "paper-segment-manifest.json"
SEGMENTS = "paper-segments"
MAX_MANIFEST_BYTES = 8_000_000
MAX_SEGMENTS = 30_000


def sha(data):
    return hashlib.sha256(data).hexdigest()


def _hex(value, n):
    return isinstance(value, str) and len(value) == n and all(
        c in "0123456789abcdef" for c in value)


def _read(path, maximum):
    path = Path(path)
    if not path.is_file() or path.is_symlink():
        raise ValueError("Required regular storage file missing")
    if path.stat().st_size > maximum:
        raise ValueError("Storage file exceeds bounded size")
    return path.read_bytes()


def _write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def _replace(path, data):
    path = Path(path)
    temporary = path.with_name("." + path.name + ".new")
    _write(temporary, data)
    os.replace(temporary, path)


def _sync(directory):
    fd = os.open(str(directory), os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _staging(destination, previous=None):
    destination = Path(destination)
    if destination.exists():
        raise FileExistsError("Refuse to replace existing transaction directory")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".paper-repository-", dir=destination.parent))
    if previous is not None:
        shutil.copytree(previous, temporary, dirs_exist_ok=True, symlinks=True)
    return temporary


def _publish(temporary, destination):
    _sync(temporary)
    os.replace(temporary, destination)
    _sync(Path(destination).parent)


def _segment_path(generation):
    if type(generation) is not int or not 1 <= generation <= 99_999_999:
        raise ValueError("Invalid segment generation")
    return SEGMENTS + "/segment-%08d.json" % generation


def _manifest_bytes(manifest):
    data = ledger.canonical(manifest)
    if len(data) > MAX_MANIFEST_BYTES:
        raise ValueError("Manifest size limit reached; archive before continuing")
    return data


def _check_manifest(manifest):
    if not isinstance(manifest, dict) or set(manifest) != {
            "schema", "checkpoint", "head", "segments"} or manifest["schema"] != SCHEMA:
        raise ValueError("Invalid storage manifest schema")
    checkpoint = manifest["checkpoint"]
    head = manifest["head"]
    if not isinstance(checkpoint, dict) or set(checkpoint) != {
            "git_commit", "generation", "ledger_sha256", "file_sha256"}:
        raise ValueError("Invalid checkpoint metadata")
    if not _hex(checkpoint["git_commit"], 40) or not _hex(checkpoint["ledger_sha256"], 64) or not _hex(checkpoint["file_sha256"], 64):
        raise ValueError("Invalid checkpoint provenance")
    if type(checkpoint["generation"]) is not int or checkpoint["generation"] < 0:
        raise ValueError("Invalid checkpoint generation")
    if not isinstance(head, dict) or set(head) != {
            "generation", "ledger_sha256", "snapshot_sha256"}:
        raise ValueError("Invalid head metadata")
    if type(head["generation"]) is not int or head["generation"] < checkpoint["generation"] or not _hex(head["ledger_sha256"], 64) or not _hex(head["snapshot_sha256"], 64):
        raise ValueError("Invalid head provenance")
    entries = manifest["segments"]
    if not isinstance(entries, list) or len(entries) > MAX_SEGMENTS or len(entries) != head["generation"] - checkpoint["generation"]:
        raise ValueError("Missing, duplicated or excess segment inventory")
    prior = checkpoint["ledger_sha256"]
    for i, entry in enumerate(entries, checkpoint["generation"] + 1):
        if not isinstance(entry, dict) or set(entry) != {
                "generation", "segment_sha256", "before_sha256", "after_sha256"}:
            raise ValueError("Invalid segment entry")
        if entry["generation"] != i or not all(_hex(entry[k], 64) for k in (
                "segment_sha256", "before_sha256", "after_sha256")):
            raise ValueError("Invalid or noncontiguous segment entry")
        if entry["before_sha256"] != prior:
            raise ValueError("Broken segment digest chain")
        prior = entry["after_sha256"]
    if prior != head["ledger_sha256"]:
        raise ValueError("Manifest head chain mismatch")
    return checkpoint, head, entries


def read_state(directory, full_replay=False):
    """Verify all on-disk inventory and checksums; optionally replay every run."""
    root = Path(directory)
    manifest_data = _read(root / MANIFEST, MAX_MANIFEST_BYTES)
    manifest = json.loads(manifest_data)
    if ledger.canonical(manifest) != manifest_data:
        raise ValueError("Noncanonical manifest")
    checkpoint, head, entries = _check_manifest(manifest)
    expected = {CHECKPOINT, SNAPSHOT, MANIFEST}
    expected.update(_segment_path(e["generation"]) for e in entries)
    actual = {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file() or p.is_symlink()}
    if actual != expected or any(p.is_symlink() for p in root.rglob("*")):
        raise ValueError("Missing, unexpected or linked repository storage files")
    legacy_bytes = _read(root / CHECKPOINT, storage.MAX_RAW_BYTES)
    if sha(legacy_bytes) != checkpoint["file_sha256"]:
        raise ValueError("Checkpoint bytes changed")
    legacy = json.loads(legacy_bytes)
    ledger.verify(legacy, storage.MAX_RAW_BYTES)
    if legacy["generation"] != checkpoint["generation"] or legacy["sha256"] != checkpoint["ledger_sha256"]:
        raise ValueError("Checkpoint identity changed")
    snapshot = _read(root / SNAPSHOT, storage.MAX_PACKED_BYTES)
    if sha(snapshot) != head["snapshot_sha256"]:
        raise ValueError("Snapshot bytes changed")
    state = storage.unpack_snapshot(snapshot)
    if state["generation"] != head["generation"] or state["sha256"] != head["ledger_sha256"]:
        raise ValueError("Snapshot/manifest head mismatch")
    packed_segments = []
    for entry in entries:
        data = _read(root / _segment_path(entry["generation"]), storage.MAX_PACKED_BYTES)
        if sha(data) != entry["segment_sha256"] or storage.manifest_entry(data) != entry:
            raise ValueError("Segment bytes/manifest mismatch")
        packed_segments.append(data)
    if full_replay:
        replay = storage.replay_segments(packed_segments, storage.pack_snapshot(legacy))
        if replay != state:
            raise ValueError("Full historical replay does not match snapshot")
    elif entries:
        # Replaying the final transition proves that the snapshot matches the
        # most recent committed report; full replay is an independent audit.
        last = storage.read_segment(packed_segments[-1])
        if last["after_sha256"] != state["sha256"]:
            raise ValueError("Latest transition/head mismatch")
    return state, manifest


def stage_migration(legacy_bytes, checkpoint_git_sha, destination):
    """Create an immutable legacy checkpoint plus packed head, with no reset."""
    if not _hex(checkpoint_git_sha, 40):
        raise ValueError("Invalid immutable legacy Git commit")
    if not isinstance(legacy_bytes, bytes) or len(legacy_bytes) > storage.MAX_RAW_BYTES:
        raise ValueError("Invalid legacy ledger bytes")
    legacy = json.loads(legacy_bytes)
    ledger.verify(legacy, storage.MAX_RAW_BYTES)
    packed = storage.pack_snapshot(legacy)
    manifest = {"schema": SCHEMA,
                "checkpoint": {"git_commit": checkpoint_git_sha,
                               "generation": legacy["generation"],
                               "ledger_sha256": legacy["sha256"],
                               "file_sha256": sha(legacy_bytes)},
                "head": {"generation": legacy["generation"],
                         "ledger_sha256": legacy["sha256"],
                         "snapshot_sha256": sha(packed)},
                "segments": []}
    temporary = _staging(destination)
    try:
        _write(temporary / CHECKPOINT, legacy_bytes)
        _write(temporary / SNAPSHOT, packed)
        _write(temporary / MANIFEST, _manifest_bytes(manifest))
        result, _ = read_state(temporary, full_replay=True)
        if result != legacy:
            raise ValueError("Migration is not lossless")
        _publish(temporary, destination)
        return manifest
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def stage_append(previous, report, source_sha, destination):
    """Stage append-only transition; existing checkpoint/segments never change."""
    previous = Path(previous)
    before, old = read_state(previous)
    if len(old["segments"]) >= MAX_SEGMENTS:
        raise ValueError("Segment archive count limit reached")
    old_snapshot = _read(previous / SNAPSHOT, storage.MAX_PACKED_BYTES)
    packed, segment, score = storage.advance_segmented(old_snapshot, report, source_sha)
    after = storage.unpack_snapshot(packed)
    entry = storage.manifest_entry(segment)
    if entry["generation"] != before["generation"] + 1:
        raise ValueError("Noncontiguous new generation")
    if storage.replay_segments([segment], old_snapshot) != after:
        raise ValueError("New transition failed replay")
    new = {"schema": SCHEMA, "checkpoint": dict(old["checkpoint"]),
           "head": {"generation": after["generation"],
                    "ledger_sha256": after["sha256"],
                    "snapshot_sha256": sha(packed)},
           "segments": list(old["segments"]) + [entry]}
    temporary = _staging(destination, previous)
    try:
        _replace(temporary / SNAPSHOT, packed)
        _write(temporary / _segment_path(after["generation"]), segment)
        _replace(temporary / MANIFEST, _manifest_bytes(new))
        result, manifest = read_state(temporary)
        if result != after or manifest != new:
            raise ValueError("Staged transaction failed verification")
        _publish(temporary, destination)
        return {"generation": after["generation"], "ledger_sha256": after["sha256"],
                "segment_path": _segment_path(after["generation"]),
                "snapshot_sha256": sha(packed), "scoreboard": score}
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Stage/check paper Git storage; NEVER pushes")
    sub = parser.add_subparsers(dest="command", required=True)
    migrate = sub.add_parser("migrate")
    migrate.add_argument("--legacy-file", required=True)
    migrate.add_argument("--checkpoint-commit", required=True)
    migrate.add_argument("--destination", required=True)
    append = sub.add_parser("append")
    append.add_argument("--previous", required=True)
    append.add_argument("--report-file", required=True)
    append.add_argument("--source-sha", required=True)
    append.add_argument("--destination", required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("--directory", required=True)
    verify.add_argument("--full-replay", action="store_true")
    args = parser.parse_args(argv)
    if args.command == "migrate":
        m = stage_migration(_read(args.legacy_file, storage.MAX_RAW_BYTES),
                            args.checkpoint_commit, args.destination)
        output = {"generation": m["head"]["generation"],
                  "ledger_sha256": m["head"]["ledger_sha256"], "migrated": True}
    elif args.command == "append":
        output = stage_append(args.previous, json.loads(
            _read(args.report_file, storage.MAX_RAW_BYTES)), args.source_sha, args.destination)
    else:
        state, manifest = read_state(args.directory, args.full_replay)
        output = {"generation": state["generation"], "ledger_sha256": state["sha256"],
                  "segments": len(manifest["segments"]), "verified": True,
                  "full_replay": args.full_replay}
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
