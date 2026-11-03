"""Offline read-only replay of two downloaded GitHub Actions paper artifacts.

No GitHub credentials, network, ledger writes, or trading permissions required.
Both ZIPs must originate from the same run; the caller supplies the expected
immutable run/source/ledger identities from independently inspected job logs.
"""
import argparse
import sys
import hashlib
import json
import re
import tempfile
import zipfile
from pathlib import Path
from .results_report import verify_published, render

MAX_FILE = 16 * 1024 * 1024
LEDGER_FILES = {"latest.json", "scoreboard.json", "ledger.json", "SHA256SUMS"}
RESULT_FILES = {"results.json", "results.md", "SHA256SUMS"}


def read_archive(path, expected):
    with zipfile.ZipFile(path) as archive:
        files = {}
        for entry in archive.infolist():
            name = entry.filename
            # Accept Actions' flattened or paper_pov/output-prefixed layouts,
            # but never traverse, follow symlinks, or accept duplicate basenames.
            parts = Path(name).parts
            if (entry.is_dir() or not parts or any(p in (".", "..") for p in parts)
                    or name.startswith("/") or "\\" in name
                    or (entry.external_attr >> 16) & 0o170000 == 0o120000):
                raise ValueError("Unsafe artifact ZIP entry")
            base = parts[-1]
            if base not in expected or base in files or entry.file_size > MAX_FILE:
                raise ValueError("Unexpected, duplicate or oversized artifact entry")
            with archive.open(entry) as stream:
                content = stream.read(MAX_FILE + 1)
            if len(content) != entry.file_size or len(content) > MAX_FILE:
                raise ValueError("Truncated or oversized artifact entry")
            files[base] = content
        if set(files) != expected:
            raise ValueError("Incomplete artifact ZIP")
        return files


def verify_checksums(files, names):
    lines = files["SHA256SUMS"].decode("ascii").splitlines()
    if len(lines) != len(names):
        raise ValueError("Incorrect artifact manifest length")
    seen = set()
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9.]+)", line)
        if not match or match[2] not in names or match[2] in seen:
            raise ValueError("Invalid artifact checksum manifest")
        seen.add(match[2])
        if hashlib.sha256(files[match[2]]).hexdigest() != match[1]:
            raise ValueError("Artifact checksum mismatch")
    if seen != names:
        raise ValueError("Missing artifact checksum entries")


def replay(ledger_zip, results_zip, *, run_id, source_sha, ledger_commit):
    if not re.fullmatch(r"[0-9]+", str(run_id)):
        raise ValueError("Invalid run identity")
    if not all(re.fullmatch(r"[0-9a-f]{40}", s) for s in (source_sha, ledger_commit)):
        raise ValueError("Invalid commit identity")
    ledger = read_archive(ledger_zip, LEDGER_FILES)
    results = read_archive(results_zip, RESULT_FILES)
    verify_checksums(ledger, LEDGER_FILES - {"SHA256SUMS"})
    verify_checksums(results, RESULT_FILES - {"SHA256SUMS"})
    scan = json.loads(ledger["latest.json"])
    score = json.loads(ledger["scoreboard.json"])
    state = json.loads(ledger["ledger.json"])
    if (score.get("ledger_sha256") != state.get("sha256")
            or score.get("generation") != state.get("generation")):
        raise ValueError("Ledger/scoreboard identity mismatch")
    # Check immutable identity before classifying missing evidence. A forged\n    # run/source/ledger reference is an integrity failure, never an abstention.\n    payload = json.loads(results["results.json"])\n    if not isinstance(payload, dict) or any((\n            payload.get(key) != expected for key, expected in (\n                ("run_id", str(run_id)), ("source_sha", source_sha),\n                ("ledger_commit", ledger_commit),\n                ("ledger_generation", score["generation"]),\n                ("ledger_sha256", score["ledger_sha256"]))):\n        raise ValueError("Published artifact identity mismatch")\n    # A missing quote-evidence array is an abstention ONLY if the rest of the
    # publication still agrees with independently retained, checksummed source.
    # Otherwise erased evidence plus a recomputed checksum could hide forgery.
    payload = json.loads(results["results.json"])
    if isinstance(payload, dict) and "quote_evidence" not in payload:
        expected, expected_md = render(
            scan, score, run_id=run_id, source_sha=source_sha,
            ledger_commit=ledger_commit, event=payload.get("github_event"),
            originating_cron=payload.get("originating_cron"))
        if (any(payload.get(key) != value for key, value in expected.items()
                if key != "quote_evidence")
                or results["results.md"] != (expected_md + "\n").encode()):
            raise ValueError("Legacy publication differs from retained evidence")
        raise ValueError("Missing independent quote evidence")
    with tempfile.TemporaryDirectory(prefix="paper-replay-") as tmp:
        directory = Path(tmp)
        for name, content in results.items():
            (directory / name).write_bytes(content)
        published = verify_published(
            directory, run_id=run_id, source_sha=source_sha,
            ledger_commit=ledger_commit, ledger_sha256=score["ledger_sha256"],
            scan=scan, scoreboard=score)
    return {"run_id": str(run_id), "generation": score["generation"],
            "eligible_pairs": published["eligible_pairs"],
            "observed_markets": published["observed_markets"],
            "watch_candidates": len(published["candidates"]),
            "abstentions": published["abstentions"],
            "max_client_quote_age_seconds": published["max_client_quote_age_seconds"],
            "status": published["status"], "exchange_event_freshness_verified": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger-zip", required=True)
    parser.add_argument("--results-zip", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--ledger-commit", required=True)
    args = parser.parse_args()
    try:
        result = replay(args.ledger_zip, args.results_zip, run_id=args.run_id,
                        source_sha=args.source_sha, ledger_commit=args.ledger_commit)
    except ValueError as exc:
        # A legacy publication lacks per-quote evidence. Report non-certification
        # without treating any other integrity or identity failure as legacy.
        if str(exc) != "Missing independent quote evidence":
            raise
        print(json.dumps({
            "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE",
            "certified": False,
            "run_id": str(args.run_id),
            "reason": "Missing independent quote evidence",
            "exchange_event_freshness_verified": False,
        }, sort_keys=True))
        return 2
    print(json.dumps({"certified": True, **result}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
