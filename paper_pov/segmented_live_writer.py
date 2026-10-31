"""Fail-closed adapter for ONE GitHub Actions paper-ledger writer.

Stages a lossless legacy->segmented migration plus the next scan, or a normal
segmented append. No network, Git push, workflow dispatch, trading or Railway.
The workflow must perform a single non-force Git commit/push and invoke
verify-remote only AFTER fetching the remote branch again.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

from . import ledger, segmented_repository as segments, segmented_storage as storage

REMOTE_REF = "refs/remotes/origin/paper-proof-ledger"


def git(root, *args):
    try:
        return subprocess.run(["git", "-C", str(root), *args], check=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              timeout=60).stdout
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise ValueError("Required Git evidence unavailable: " + " ".join(args[:2])) from exc


def exact_commit(root, commit):
    if not segments._hex(commit, 40):
        raise ValueError("Expected exact 40-character Git commit")
    if git(root, "rev-parse", "--verify", commit + "^{commit}").decode().strip() != commit:
        raise ValueError("Git commit mismatch")
    return commit


def show(root, commit, path, limit):
    data = git(root, "show", commit + ":" + path)
    if len(data) > limit:
        raise ValueError("Git object exceeds storage bound")
    return data


def inventory(root, commit):
    """The Git commit is authoritative; never infer a missing segment."""
    state, mode = segments.read_git_state(root, exact_commit(root, commit), full_replay=True)
    if mode == "legacy":
        return state, mode, [segments.CHECKPOINT, segments.SNAPSHOT,
                             segments.MANIFEST]
    manifest_bytes = show(root, commit, segments.MANIFEST, segments.MAX_MANIFEST_BYTES)
    manifest = json.loads(manifest_bytes)
    _, _, entries = segments._check_manifest(manifest)
    paths = [segments.CHECKPOINT, segments.SNAPSHOT, segments.MANIFEST]
    paths.extend(segments._segment_path(e["generation"]) for e in entries)
    return state, mode, paths


def stage(root, base, report, source_sha, destination):
    """Produce a verified complete new Git storage tree, without changing Git."""
    root, destination = Path(root), Path(destination)
    if destination.exists():
        raise FileExistsError("Refuse to overwrite staged transaction")
    before, mode, paths = inventory(root, base)
    if not segments._hex(source_sha, 40):
        raise ValueError("Invalid source SHA")
    with tempfile.TemporaryDirectory(prefix="paper-transaction-") as temp:
        initial = Path(temp) / "initial"
        if mode == "legacy":
            raw = show(root, base, "paper-ledger.json", storage.MAX_RAW_BYTES)
            segments.stage_migration(raw, base, initial)
        else:
            initial.mkdir()
            for path in paths:
                limit = (segments.MAX_MANIFEST_BYTES if path == segments.MANIFEST else
                         storage.MAX_RAW_BYTES if path == segments.CHECKPOINT else
                         storage.MAX_PACKED_BYTES)
                segments._write(initial / path, show(root, base, path, limit))
            segments.verify_checkpoint_origin(initial, root)
            restored, _ = segments.read_state(initial, full_replay=True)
            if restored != before:
                raise ValueError("Source segmented state mismatch")
        info = segments.stage_append(initial, report, source_sha, destination)
    after, manifest = segments.read_state(destination, full_replay=True)
    if after["generation"] != before["generation"] + 1:
        raise ValueError("Storage generation did not advance exactly once")
    if manifest["head"]["ledger_sha256"] != after["sha256"]:
        raise ValueError("Manifest head mismatch")
    if info["scoreboard"] != ledger.scoreboard(after, storage.MAX_RAW_BYTES):
        raise ValueError("Scoreboard mismatch")
    return after, info


def changed_paths(root, base, staged):
    """Exactly the atomic transaction files, not all historical segments."""
    _, mode, _ = inventory(root, base)
    state, manifest = segments.read_state(staged, full_replay=True)
    new_segment = segments._segment_path(state["generation"])
    paths = [segments.MANIFEST, segments.SNAPSHOT, new_segment]
    if mode == "legacy":
        paths.append(segments.CHECKPOINT)
    else:
        old_checkpoint = show(root, base, segments.CHECKPOINT, storage.MAX_RAW_BYTES)
        if old_checkpoint != (Path(staged) / segments.CHECKPOINT).read_bytes():
            raise ValueError("Immutable checkpoint modified")
    return sorted(paths)


def apply(root, base, staged):
    """Stage exactly the intended paths in a CLEAN ledger worktree.

    Caller must checkout the exact remote ledger base before this call.
    All files enter ONE Git commit; a failure here must never be pushed.
    """
    root, staged = Path(root), Path(staged)
    exact_commit(root, base)
    if git(root, "rev-parse", "HEAD").decode().strip() != base:
        raise ValueError("Ledger worktree moved before apply")
    if git(root, "status", "--porcelain"):
        raise ValueError("Ledger worktree is not clean")
    paths = changed_paths(root, base, staged)
    for path in paths:
        source = staged / path
        data = segments._read(source, segments.MAX_MANIFEST_BYTES if path == segments.MANIFEST
                              else storage.MAX_RAW_BYTES if path == segments.CHECKPOINT
                              else storage.MAX_PACKED_BYTES)
        target = root / path
        if target.is_symlink() or any(p.is_symlink() for p in target.parents if p != root.parent):
            raise ValueError("Unsafe storage destination")
        target.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=target.parent, prefix=".paper-txn-",
                                         delete=False) as f:
            tmp = Path(f.name)
            try:
                f.write(data)
                f.flush()
                os.fsync(f.fileno())
            finally:
                pass
        os.replace(tmp, target)
    git(root, "add", "--", *paths)
    actual = sorted(git(root, "diff", "--cached", "--name-only").decode().splitlines())
    if actual != paths:
        raise ValueError("Unexpected staged Git changes")
    return paths


def verify_remote(root, base, new_commit, staged):
    """Verify remote ref, exact parent, changed-file inventory and ALL bytes."""
    root, staged = Path(root), Path(staged)
    exact_commit(root, base)
    exact_commit(root, new_commit)
    remote = git(root, "rev-parse", "--verify", REMOTE_REF).decode().strip()
    if remote != new_commit:
        raise ValueError("Remote ledger ref not at expected new commit")
    parents = git(root, "rev-list", "--parents", "-n", "1", new_commit).decode().split()
    if parents != [new_commit, base]:
        raise ValueError("Ledger commit does not extend exact expected base")
    paths = changed_paths(root, base, staged)
    actual = sorted(git(root, "diff", "--name-only", base, new_commit).decode().splitlines())
    if actual != paths:
        raise ValueError("Remote Git commit changed unexpected paths")
    for path in paths:
        local = segments._read(staged / path, segments.MAX_MANIFEST_BYTES if path == segments.MANIFEST
                               else storage.MAX_RAW_BYTES if path == segments.CHECKPOINT
                               else storage.MAX_PACKED_BYTES)
        if show(root, new_commit, path, len(local)) != local:
            raise ValueError("Remote storage bytes differ from staged transaction")
    expected, _ = segments.read_state(staged, full_replay=True)
    actual_state, mode = segments.read_git_state(root, new_commit, full_replay=True)
    if mode != "segmented" or actual_state != expected:
        raise ValueError("Remote ledger replay/identity mismatch")
    return {"generation": expected["generation"], "ledger_sha256": expected["sha256"],
            "remote_commit": new_commit, "verified_files": paths}


def main(argv=None):
    p = argparse.ArgumentParser(description="Git-only paper ledger single-writer staging")
    sub = p.add_subparsers(dest="command", required=True)
    for name in ("stage", "apply", "verify-remote"):
        s = sub.add_parser(name)
        s.add_argument("--repository", required=True)
        s.add_argument("--base", required=True)
        s.add_argument("--staged", required=True)
        if name == "stage":
            s.add_argument("--report", required=True)
            s.add_argument("--source-sha", required=True)
            s.add_argument("--next-ledger", required=True)
            s.add_argument("--scoreboard", required=True)
        if name == "verify-remote":
            s.add_argument("--commit", required=True)
    a = p.parse_args(argv)
    if a.command == "stage":
        report = json.loads(Path(a.report).read_bytes())
        state, info = stage(a.repository, a.base, report, a.source_sha, a.staged)
        for path, data in ((a.next_ledger, ledger.canonical(state)),
                           (a.scoreboard, ledger.canonical(info["scoreboard"]))):
            target = Path(path)
            if target.exists():
                raise FileExistsError("Refuse to replace staged output")
            target.parent.mkdir(parents=True, exist_ok=True)
            segments._write(target, data)
        result = {"generation": state["generation"], "ledger_sha256": state["sha256"],
                  "snapshot_sha256": info["snapshot_sha256"]}
    elif a.command == "apply":
        result = {"staged_files": apply(a.repository, a.base, a.staged)}
    else:
        result = verify_remote(a.repository, a.base, a.commit, a.staged)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
