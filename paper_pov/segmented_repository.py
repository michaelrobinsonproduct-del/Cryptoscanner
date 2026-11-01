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
import subprocess
import tempfile

from . import ledger, segmented_storage as storage

SCHEMA = "paper-git-segment-manifest-v1"
CHECKPOINT = "paper-ledger.checkpoint.json"
SNAPSHOT = "paper-ledger.packed.json"
MANIFEST = "paper-segment-manifest.json"
SEGMENTS = "paper-segments"
MAX_MANIFEST_BYTES = 8_000_000
MAX_SEGMENTS = 30_000
# Aggregate active Git-tree budget, including immutable checkpoint and segments.
# The per-object 12 MB packed bound is NOT an aggregate ledger limit.
# Reserve 2 MB of headroom; fail closed before any new ledger commit.
MAX_ACTIVE_TREE_BYTES = 10_000_000


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


def active_storage_bytes(directory):
    """Count every active storage file, not only the compressed snapshot."""
    total = 0
    for path in Path(directory).rglob("*"):
        if path.is_symlink():
            raise ValueError("Linked storage file is prohibited")
        if path.is_file():
            total += path.stat().st_size
    return total


def _enforce_active_budget(directory):
    total = active_storage_bytes(directory)
    if total > MAX_ACTIVE_TREE_BYTES:
        raise ValueError("Aggregate active paper ledger storage budget exceeded; archive rollover required")
    return total


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
        if type(entry["generation"]) is not int or entry["generation"] != i or not all(_hex(entry[k], 64) for k in (
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
    checkpoint_payload = json.loads(legacy_bytes)
    if isinstance(checkpoint_payload, dict) and checkpoint_payload.get("format") == storage.FORMAT:
        # Rollover checkpoints are bounded packed snapshots. The initial
        # legacy checkpoint remains byte-exact and unchanged.
        legacy = storage.unpack_snapshot(legacy_bytes)
    else:
        legacy = checkpoint_payload
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
        _enforce_active_budget(temporary)
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
        active_bytes = _enforce_active_budget(temporary)
        _publish(temporary, destination)
        return {"generation": after["generation"], "active_storage_bytes": active_bytes,
                "active_storage_budget_bytes": MAX_ACTIVE_TREE_BYTES,
                "ledger_sha256": after["sha256"],
                "segment_path": _segment_path(after["generation"]),
                "snapshot_sha256": sha(packed), "scoreboard": score}
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def stage_rollover(previous, checkpoint_git_sha, destination):
    """Losslessly rebase the active segment inventory onto an immutable Git head.

    The previous Git commit remains the archived segment inventory. This
    stages only local files; the single writer MUST atomically commit deleted
    old segments together with the replacement checkpoint and manifest.
    """
    if not _hex(checkpoint_git_sha, 40):
        raise ValueError("Invalid rollover Git provenance")
    before, old = read_state(previous, full_replay=True)
    if not old["segments"]:
        raise ValueError("Refuse rollover without archived segment evidence")
    # A raw checkpoint can exceed the entire 10MB active-tree budget once
    # the 50h market observation window is populated. Store a second
    # SHA-bound packed snapshot, not an unbounded raw ledger copy.
    checkpoint_bytes = storage.pack_snapshot(before)
    snapshot = _read(Path(previous) / SNAPSHOT, storage.MAX_PACKED_BYTES)
    new = {"schema": SCHEMA,
           "checkpoint": {"git_commit": checkpoint_git_sha,
                          "generation": before["generation"],
                          "ledger_sha256": before["sha256"],
                          "file_sha256": sha(checkpoint_bytes)},
           "head": {"generation": before["generation"],
                    "ledger_sha256": before["sha256"],
                    "snapshot_sha256": sha(snapshot)},
           "segments": []}
    temporary = _staging(destination)
    try:
        _write(temporary / CHECKPOINT, checkpoint_bytes)
        _write(temporary / SNAPSHOT, snapshot)
        _write(temporary / MANIFEST, _manifest_bytes(new))
        restored, manifest = read_state(temporary, full_replay=True)
        if restored != before or manifest != new:
            raise ValueError("Rollover lost historical ledger state")
        _enforce_active_budget(temporary)
        _publish(temporary, destination)
        return new
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def verify_checkpoint_origin(directory, git_repository):
    """Verify checkpoint bytes against the exact immutable ancestor Git commit.

    Initial migration references a legacy JSON commit. A rollover references
    the previous packed commit, whose complete historical chain is recursively
    verified before its canonical ledger state can serve as a checkpoint.
    """
    _, manifest = read_state(directory)
    commit = manifest["checkpoint"]["git_commit"]
    checkpoint = _read(Path(directory) / CHECKPOINT, storage.MAX_RAW_BYTES)
    try:
        has_packed = _git_has(git_repository, commit, MANIFEST)
        has_snapshot = _git_has(git_repository, commit, SNAPSHOT)
        if has_packed != has_snapshot:
            raise ValueError("Partially archived checkpoint commit")
        if has_packed:
            state, mode = read_git_state(git_repository, commit, full_replay=True)
            if mode != "segmented" or storage.unpack_snapshot(checkpoint) != state:
                raise ValueError("Archived packed checkpoint differs from Git history")
        else:
            historical = _git(git_repository, "show", commit + ":paper-ledger.json")
            if len(historical) > storage.MAX_RAW_BYTES or historical != checkpoint:
                raise ValueError("Legacy checkpoint differs from immutable Git history")
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as exc:
        raise ValueError("Checkpoint Git commit unavailable") from exc
    return commit


def _git(repository, *args):
    try:
        return subprocess.run(
            ["git", "-C", str(repository), *args], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, timeout=30, check=True).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as exc:
        raise ValueError("Required Git evidence unavailable") from exc


def _git_has(repository, commit, path):
    result = subprocess.run(
        ["git", "-C", str(repository), "cat-file", "-e", commit + ":" + path],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)
    return result.returncode == 0


def read_git_state(repository, commit, full_replay=False):
    """Read legacy or packed Git commit with the SAME verified ledger contract.

    No remote access, no writer, and no fallback when a packed manifest or
    snapshot is partially present. Supports mixed old/new commits in audits.
    """
    if not _hex(commit, 40):
        raise ValueError("Git state requires an exact commit SHA")
    resolved = _git(repository, "rev-parse", "--verify", commit + "^{commit}").decode().strip()
    if resolved != commit:
        raise ValueError("Git commit identity mismatch")
    has_manifest = _git_has(repository, commit, MANIFEST)
    has_snapshot = _git_has(repository, commit, SNAPSHOT)
    if has_manifest != has_snapshot:
        raise ValueError("Partially migrated Git ledger commit")
    if not has_manifest:
        # Prove the ledger's OWN complete first-parent chain back to its
        # generation-zero introduction, not unrelated (possibly shallow)
        # repository history. Any packed ancestor on this chain is a fatal
        # downgrade, even after many later legacy-only commits.
        raw = _git(repository, "show", commit + ":paper-ledger.json")
        if len(raw) > storage.MAX_RAW_BYTES:
            raise ValueError("Legacy Git ledger exceeds bound")
        state = json.loads(raw)
        ledger.verify(state, storage.MAX_RAW_BYTES)
        generation = state["generation"]
        if generation > 510:
            raise ValueError("Legacy ancestry exceeds bounded verification limit")
        ancestry = _git(repository, "rev-list", "--first-parent",
                        "--max-count", str(generation + 2),
                        commit).decode().splitlines()
        if len(ancestry) < generation + 1 or ancestry[0] != commit:
            raise ValueError("Incomplete paper ledger ancestry before genesis")
        for offset, ancestor in enumerate(ancestry[:generation + 1]):
            if _git_has(repository, ancestor, MANIFEST) or _git_has(
                    repository, ancestor, SNAPSHOT):
                raise ValueError("Packed Git ledger was removed: unsafe downgrade")
            historical = _git(repository, "show", ancestor + ":paper-ledger.json")
            if len(historical) > storage.MAX_RAW_BYTES:
                raise ValueError("Historical Git ledger exceeds bound")
            old_state = json.loads(historical)
            ledger.verify(old_state, storage.MAX_RAW_BYTES)
            if old_state["generation"] != generation - offset:
                raise ValueError("Missing, repeated or regressing legacy generation")
        genesis = ancestry[generation]
        shallow_path = Path(_git(repository, "rev-parse", "--git-path",
                                 "shallow").decode().strip())
        if not shallow_path.is_absolute():
            shallow_path = Path(repository) / shallow_path
        if shallow_path.exists() and genesis in shallow_path.read_text().splitlines():
            raise ValueError("Incomplete Git ancestry at legacy genesis")
        # The generation-zero commit must introduce the ledger. Git shallow
        # boundaries are not proof that a parent lacks an older ledger.
        commit_lines = _git(repository, "cat-file", "-p", genesis).decode().splitlines()
        parents = [line.split()[1] for line in commit_lines if line.startswith("parent ")]
        if len(parents) > 1:
            raise ValueError("Legacy genesis has multiple parents")
        if parents:
            parent = parents[0]
            _git(repository, "cat-file", "-e", parent + "^{commit}")
            if (_git_has(repository, parent, "paper-ledger.json") or
                    _git_has(repository, parent, MANIFEST) or
                    _git_has(repository, parent, SNAPSHOT)):
                raise ValueError("Legacy genesis did not introduce ledger: unsafe downgrade")
        return state, "legacy"
    manifest_bytes = _git(repository, "show", commit + ":" + MANIFEST)
    if len(manifest_bytes) > MAX_MANIFEST_BYTES:
        raise ValueError("Git manifest exceeds bound")
    manifest = json.loads(manifest_bytes)
    checkpoint, _, entries = _check_manifest(manifest)
    origin = checkpoint["git_commit"]
    if origin == commit:
        raise ValueError("Checkpoint cannot point to its own commit")
    _git(repository, "merge-base", "--is-ancestor", origin, commit)
    with tempfile.TemporaryDirectory(prefix="paper-git-read-") as temp:
        root = Path(temp)
        for path in (MANIFEST, SNAPSHOT, CHECKPOINT):
            data = _git(repository, "show", commit + ":" + path)
            limit = MAX_MANIFEST_BYTES if path == MANIFEST else (
                storage.MAX_PACKED_BYTES if path == SNAPSHOT else storage.MAX_RAW_BYTES)
            if len(data) > limit:
                raise ValueError("Git storage blob exceeds bound")
            _write(root / path, data)
        for entry in entries:
            path = _segment_path(entry["generation"])
            data = _git(repository, "show", commit + ":" + path)
            if len(data) > storage.MAX_PACKED_BYTES:
                raise ValueError("Git segment exceeds bound")
            _write(root / path, data)
        state, _ = read_state(root, full_replay)
        verify_checkpoint_origin(root, repository)
        return state, "segmented"


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
    verify.add_argument("--git-repository", help="Require exact legacy Git commit readback")
    export = sub.add_parser("export-git")
    export.add_argument("--repository", required=True)
    export.add_argument("--commit", required=True)
    export.add_argument("--output", required=True)
    export.add_argument("--full-replay", action="store_true")
    args = parser.parse_args(argv)
    if args.command == "migrate":
        m = stage_migration(_read(args.legacy_file, storage.MAX_RAW_BYTES),
                            args.checkpoint_commit, args.destination)
        output = {"generation": m["head"]["generation"],
                  "ledger_sha256": m["head"]["ledger_sha256"], "migrated": True}
    elif args.command == "append":
        output = stage_append(args.previous, json.loads(
            _read(args.report_file, storage.MAX_RAW_BYTES)), args.source_sha, args.destination)
    elif args.command == "export-git":
        state, mode = read_git_state(args.repository, args.commit, args.full_replay)
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            raise FileExistsError("Refuse to overwrite existing Git audit export")
        _write(target, ledger.canonical(state))
        output = {"generation": state["generation"], "ledger_sha256": state["sha256"],
                  "mode": mode, "exported": True}
    else:
        state, manifest = read_state(args.directory, args.full_replay)
        if args.git_repository:
            verify_checkpoint_origin(args.directory, args.git_repository)
        output = {"generation": state["generation"], "ledger_sha256": state["sha256"],
                  "segments": len(manifest["segments"]), "verified": True,
                  "full_replay": args.full_replay}
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
