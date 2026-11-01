"""Bounded read-only Git fetch for legacy and segmented paper ledger audits.

Never fetches the full historical Kraken archive, never changes a remote ref,
and never writes the paper ledger. The immutable checkpoint is fetched by SHA
only when the current ledger is segmented; failure is fatal, not a reset.
"""
import json
from pathlib import Path
import re
import subprocess

REMOTE_REF = "refs/remotes/origin/paper-proof-ledger"
SOURCE_REF = "refs/heads/paper-proof-ledger"
SHA = re.compile(r"[0-9a-f]{40}\Z")
MAX_MANIFEST_BYTES = 8_000_000
MAX_ANCESTRY_DEPTH = 512


def _git(*args):
    return subprocess.run(["git", *args], check=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, timeout=120).stdout


def _checkpoint_needs_fetch(checkpoint):
    """Do not turn an already fetched ancestor into a shallow boundary.

    Git fetch --depth=1 <checkpoint> can rewrite .git/shallow even when a
    previous deep ledger fetch supplied the complete legacy ancestry.
    The legacy verifier must retain proof back to generation zero.
    """
    present = subprocess.run(
        ["git", "cat-file", "-e", checkpoint + "^{commit}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)
    if present.returncode != 0:
        return True
    shallow_path = _git("rev-parse", "--git-path", "shallow").decode().strip()
    if not shallow_path:
        raise ValueError("Cannot inspect Git shallow boundary")
    path = Path(shallow_path)
    return path.is_file() and checkpoint in path.read_text().splitlines()


def fetch_bounded():
    # Fetch a bounded but sufficiently deep ledger ancestry so the legacy
    # reader can prove no earlier packed migration was silently removed.
    # A still-shallow ancestor fails closed in read_git_state.
    _git("fetch", "--no-tags", "--depth=" + str(MAX_ANCESTRY_DEPTH), "origin",
         SOURCE_REF + ":" + REMOTE_REF)
    head = _git("rev-parse", REMOTE_REF).decode().strip()
    if not SHA.fullmatch(head):
        raise ValueError("Invalid fetched ledger head")
    manifest_result = subprocess.run(
        ["git", "show", head + ":paper-segment-manifest.json"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    if manifest_result.returncode == 0:
        if len(manifest_result.stdout) > MAX_MANIFEST_BYTES:
            raise ValueError("Oversized segmented ledger manifest")
        try:
            manifest = json.loads(manifest_result.stdout)
            checkpoint = manifest["checkpoint"]["git_commit"]
        except (ValueError, KeyError, TypeError) as exc:
            raise ValueError("Invalid segmented checkpoint manifest") from exc
        if not isinstance(checkpoint, str) or not SHA.fullmatch(checkpoint):
            raise ValueError("Invalid segmented checkpoint commit")
        # The first bounded branch fetch normally already has this ancestor.
        # An unconditional depth=1 fetch destroys the ancestry needed by the
        # independent audit (observed after real gen13->14 migration).
        if _checkpoint_needs_fetch(checkpoint):
            _git("fetch", "--no-tags", "--depth=" + str(MAX_ANCESTRY_DEPTH),
                 "origin", checkpoint)
        _git("show", checkpoint + ":paper-ledger.json")
    else:
        # A partial migration is not a legacy fallback.
        if subprocess.run(["git", "cat-file", "-e",
                           head + ":paper-ledger.packed.json"],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL, timeout=30).returncode == 0:
            raise ValueError("Partially migrated Git ledger")
        _git("show", head + ":paper-ledger.json")
    return head


if __name__ == "__main__":
    print("PAPER_BOUNDED_LEDGER_HEAD=" + fetch_bounded())
