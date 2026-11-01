"""Fail-closed public paper results for a failed GitHub Actions scan.

No prices, ledger generation, persistence or predictive outcomes are inferred.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

REPOSITORY = "michaelrobinsonproduct-del/Cryptoscanner"
HORIZONS = (1, 6, 24, 48)


def render_failure(run_id, source_sha, as_of=None):
    if not isinstance(run_id, str) or not re.fullmatch(r"[1-9][0-9]{0,19}", run_id):
        raise ValueError("Invalid GitHub run ID")
    if not isinstance(source_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", source_sha):
        raise ValueError("Invalid exact source SHA")
    as_of = as_of or dt.datetime.now(dt.timezone.utc)
    if as_of.tzinfo is None or as_of.utcoffset() is None:
        raise ValueError("UTC timestamp required")
    stamp = as_of.astimezone(dt.timezone.utc).isoformat()
    url = f"https://github.com/{REPOSITORY}/actions/runs/{run_id}"
    reason = "A required GitHub Actions step failed; inspect the run logs for the specific error."
    data = {
        "schema": 1, "status": "FAILED_PAPER_ONLY", "as_of": stamp,
        "run_id": run_id, "source_sha": source_sha, "run_url": url,
        "market_freshness_seconds": None, "exchange_event_freshness_verified": False,
        "eligible_pairs": None, "candidates": [], "stablecoin_exclusions_verified": None,
        "ledger_generation": None, "ledger_remote_readback_verified": None,
        "ledger_may_have_been_committed": True,
        "horizons": {str(h): {"status": "NOT_VERIFIED", "verified_matured_count": None,
                              "verified_hits": None} for h in HORIZONS},
        "missed_movers": None, "false_positives": None, "held_out_lift": None,
        "storage_recovery": "NOT_VERIFIED", "dex_freshness_gated": False,
        "buy_approved": False, "production_applied": False, "errors": [reason],
    }
    lines = [
        "# Kraken paper scanner — FAILED run",
        "",
        "**Status: FAILED — no successful scan or persisted generation is claimed.**",
        "",
        f"**UTC report time:** {stamp}",
        f"**GitHub run:** {url}",
        f"**Exact source SHA:** {source_sha}",
        "",
        "**Kraken freshness / eligible universe:** NOT VERIFIED.",
        "**Top 12 WATCH/BUY PAPER ONLY:** NOT AVAILABLE; no BUY authorized.",
        "**Stablecoin exclusions:** NOT VERIFIED for this failed run.",
        "**Ledger generation, atomic write, remote readback, recovery:** NOT VERIFIED. "
        "A partial workflow failure may occur after a successful ledger commit; "
        "inspect the remote ledger before any retry.",
        "**Learning and 1/6/24/48h outcomes:** NOT VERIFIED; no predictive improvement claimed.",
        "**Missed movers / false positives / baseline:** NOT VERIFIED.",
        "**DEX:** not used and not freshness-gated.",
        f"**Error:** {reason}",
        "",
    ]
    return data, "\n".join(lines)


def _atomic_write(path, content):
    path = Path(path)
    fd, temp = tempfile.mkstemp(prefix=".paper-failure-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def write_failure(directory, run_id, source_sha, as_of=None):
    data, markdown = render_failure(run_id, source_sha, as_of)
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    contents = {
        "results.json": (json.dumps(data, sort_keys=True, separators=(",", ":")) + "\n").encode(),
        "results.md": (markdown + "\n").encode(),
    }
    for name, content in contents.items():
        _atomic_write(directory / name, content)
    checksums = "".join(hashlib.sha256(contents[name]).hexdigest() + "  " + name + "\n"
                        for name in sorted(contents))
    _atomic_write(directory / "SHA256SUMS", checksums.encode())
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    result = write_failure(args.output_dir, args.run_id, args.source_sha)
    print("PAPER_FAILED_RESULTS_RECORDED", result["run_id"])


if __name__ == "__main__":
    main()
