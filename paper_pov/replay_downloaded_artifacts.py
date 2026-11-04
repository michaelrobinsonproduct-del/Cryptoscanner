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
from .failure_report import render_failure

MAX_FILE = 16 * 1024 * 1024
LEDGER_FILES = {"latest.json", "scoreboard.json", "ledger.json", "SHA256SUMS"}
SLOT_RECEIPT = "slot_receipt.json"
RESULT_FILES = {"results.json", "results.md", "SHA256SUMS"}


def read_archive(path, expected, optional=frozenset()):
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
            if base not in expected | set(optional) or base in files or entry.file_size > MAX_FILE:
                raise ValueError("Unexpected, duplicate or oversized artifact entry")
            with archive.open(entry) as stream:
                content = stream.read(MAX_FILE + 1)
            if len(content) != entry.file_size or len(content) > MAX_FILE:
                raise ValueError("Truncated or oversized artifact entry")
            files[base] = content
        if not expected <= set(files) or set(files) - expected - set(optional):
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
    ledger = read_archive(ledger_zip, LEDGER_FILES, {SLOT_RECEIPT})
    results = read_archive(results_zip, RESULT_FILES)
    verify_checksums(ledger, (LEDGER_FILES - {"SHA256SUMS"}) | ({SLOT_RECEIPT} if SLOT_RECEIPT in ledger else set()))
    verify_checksums(results, RESULT_FILES - {"SHA256SUMS"})
    slot_identity = None
    if SLOT_RECEIPT in ledger:
        receipt = json.loads(ledger[SLOT_RECEIPT])
        if (not isinstance(receipt, dict) or receipt.get("schema") != 1
                or receipt.get("run_id") != str(run_id)
                or receipt.get("source_sha") != source_sha
                or receipt.get("historical_quotes_reconstructed") is not False):
            raise ValueError("Slot receipt identity mismatch")
        if set(receipt) != {"schema", "slot_identity", "run_id", "source_sha", "historical_quotes_reconstructed"}:
            raise ValueError("Unexpected slot receipt fields")
        slot_identity = receipt.get("slot_identity")
        if slot_identity != "MANUAL":
            from .missed_slot_recovery import utc, SLOT_MINUTES
            stamp = utc(slot_identity)
            if (stamp.minute not in SLOT_MINUTES or stamp.second or stamp.microsecond
                    or stamp.isoformat() != slot_identity):
                raise ValueError("Invalid slot receipt identity")
    scan = json.loads(ledger["latest.json"])
    score = json.loads(ledger["scoreboard.json"])
    state = json.loads(ledger["ledger.json"])
    if (score.get("ledger_sha256") != state.get("sha256")
            or score.get("generation") != state.get("generation")):
        raise ValueError("Ledger/scoreboard identity mismatch")
    # Check immutable identity before classifying missing evidence. A forged
    # run/source/ledger reference is an integrity failure, never an abstention.
    payload = json.loads(results["results.json"])
    if not isinstance(payload, dict) or any(
            payload.get(key) != expected for key, expected in (
                ("run_id", str(run_id)), ("source_sha", source_sha),
                ("ledger_commit", ledger_commit),
                ("ledger_generation", score["generation"]),
                ("ledger_sha256", score["ledger_sha256"]))):
        raise ValueError("Published artifact identity mismatch")
    # A missing quote-evidence array is an abstention ONLY if the rest of the
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
    return {"run_id": str(run_id), "slot_identity": slot_identity,
            "generation": score["generation"],
            "eligible_pairs": published["eligible_pairs"],
            "observed_markets": published["observed_markets"],
            "watch_candidates": len(published["candidates"]),
            "abstentions": published["abstentions"],
            "max_client_quote_age_seconds": published["max_client_quote_age_seconds"],
            "status": published["status"], "exchange_event_freshness_verified": False}


def replay_visible_result(ledger_zip=None, results_zip=None, failure_zip=None, *,
                          run_id, source_sha, ledger_commit=None):
    """Return a truthful read-only result for success OR a failed paper run.

    Failed runs cannot claim a persisted generation or WATCH. A caller must
    explicitly choose exactly one artifact path; no fallback from corrupted
    success artifacts to an apparently legitimate failure receipt.
    """
    if failure_zip is not None:
        if ledger_zip is not None or results_zip is not None or ledger_commit is not None:
            raise ValueError("Mixed success and failure evidence")
        if not re.fullmatch(r"[0-9]+", str(run_id)) or not re.fullmatch(r"[0-9a-f]{40}", source_sha):
            raise ValueError("Invalid failed-run identity")
        files = read_archive(failure_zip, RESULT_FILES)
        verify_checksums(files, RESULT_FILES - {"SHA256SUMS"})
        payload = json.loads(files["results.json"])
        if (not isinstance(payload, dict) or payload.get("status") != "FAILED_PAPER_ONLY"
                or str(payload.get("run_id")) != str(run_id)
                or payload.get("source_sha") != source_sha):
            raise ValueError("Failed-run artifact identity mismatch")
        # Verify both the payload and human report against canonical rendering.
        from .scanner import utc
        expected, markdown = render_failure(str(run_id), source_sha, utc(payload["as_of"]))
        if payload != expected or files["results.md"] != (markdown + "\n").encode():
            raise ValueError("Failed-run report differs from canonical renderer")
        return {"status": "FAILED_PAPER_ONLY", "certified": False,
                "run_id": str(run_id), "source_sha": source_sha,
                "ledger_persisted": None, "watch_candidates": None,
                "exchange_event_freshness_verified": False}
    if ledger_zip is None or results_zip is None or ledger_commit is None:
        raise ValueError("Incomplete successful-run evidence")
    return replay(ledger_zip, results_zip, run_id=run_id,
                  source_sha=source_sha, ledger_commit=ledger_commit)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger-zip")
    parser.add_argument("--results-zip")
    parser.add_argument("--failure-zip")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--ledger-commit")
    args = parser.parse_args()
    if args.failure_zip:
        result = replay_visible_result(
            failure_zip=args.failure_zip, ledger_zip=args.ledger_zip,
            results_zip=args.results_zip, run_id=args.run_id,
            source_sha=args.source_sha, ledger_commit=args.ledger_commit)
        print(json.dumps(result, sort_keys=True))
        return 2
    if not all((args.ledger_zip, args.results_zip, args.ledger_commit)):
        parser.error("successful replay requires both ZIPs and ledger commit")
    try:
        result = replay_visible_result(
            args.ledger_zip, args.results_zip, run_id=args.run_id,
            source_sha=args.source_sha, ledger_commit=args.ledger_commit)
    except ValueError as exc:
        if str(exc) != "Missing independent quote evidence":
            raise
        print(json.dumps({
            "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE",
            "certified": False, "run_id": str(args.run_id),
            "reason": "Missing independent quote evidence",
            "exchange_event_freshness_verified": False,
        }, sort_keys=True))
        return 2
    print(json.dumps({"certified": True, **result}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
