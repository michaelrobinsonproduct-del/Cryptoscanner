"""Bounded read-only Git fetch for legacy and segmented paper ledger audits.

Never fetches the full historical Kraken archive, never changes a remote ref,
and never writes the paper ledger. The immutable checkpoint is fetched by SHA
only when the current ledger is segmented; failure is fatal, not a reset.
"""
import json
import re
import subprocess

REMOTE_REF = "refs/remotes/origin/paper-proof-ledger"
SOURCE_REF = "refs/heads/paper-proof-ledger"
SHA = re.compile(r"[0-9a-f]{40}\\Z")
MAX_MANIFEST_BYTES = 8_000_000


def _git(*args):
    return subprocess.run(["git", *args], check=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, timeout=120).stdout


def fetch_bounded():
    _git("fetch", "--no-tags", "--depth=64", "origin",
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
        _git("fetch", "--no-tags", "--depth=1", "origin", checkpoint)
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
