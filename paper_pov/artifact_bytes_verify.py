"""Offline, bounded verification of original PAPER artifact ZIP bytes.

This is NOT a GitHub downloader, a remote-ledger readback, a delivery receipt,
or exchange-event freshness proof. The caller must separately authenticate
the ZIP source and expected GitHub-reported digest.
"""
import argparse
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

from paper_pov import ledger

MAX_ARCHIVE_BYTES = 16 * 1024 * 1024
MAX_MEMBER_BYTES = 12 * 1024 * 1024
MAX_TOTAL_UNCOMPRESSED = 24 * 1024 * 1024
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
SOURCE_SHA = re.compile(r"[0-9a-f]{40}\Z")
FILES = {
    "ledger": {"latest.json", "scoreboard.json", "ledger.json", "SHA256SUMS"},
    "results": {"results.md", "results.json", "SHA256SUMS"},
}


def checked_zip(raw, reported_digest, kind):
    """Reject truncated, tampered, ambiguous, oversized or resealed ZIP members."""
    if kind not in FILES or not isinstance(raw, bytes) or not 0 < len(raw) <= MAX_ARCHIVE_BYTES:
        raise ValueError("invalid or oversized original artifact ZIP")
    if not isinstance(reported_digest, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", reported_digest):
        raise ValueError("missing GitHub artifact digest")
    digest = hashlib.sha256(raw).hexdigest()
    if digest != reported_digest[7:]:
        raise ValueError("original ZIP SHA256 mismatch")
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            members = archive.infolist()
            names = [m.filename for m in members]
            if len(names) != len(FILES[kind]) or set(names) != FILES[kind]:
                raise ValueError("missing, extra or duplicate ZIP member")
            if (any(m.is_dir() or m.file_size > MAX_MEMBER_BYTES or
                    m.flag_bits & 1 or (m.external_attr >> 16) & 0o170000 == 0o120000
                    for m in members) or
                    sum(m.file_size for m in members) > MAX_TOTAL_UNCOMPRESSED):
                raise ValueError("unsafe or oversized ZIP member")
            data = {m.filename: archive.read(m) for m in members}
    except (zipfile.BadZipFile, RuntimeError, EOFError, OSError) as exc:
        raise ValueError("invalid original artifact ZIP") from exc
    try:
        checksum_lines = data["SHA256SUMS"].decode("ascii").splitlines()
        expected = FILES[kind] - {"SHA256SUMS"}
        seen = set()
        for line in checksum_lines:
            match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9._-]+)", line)
            if not match or match.group(2) not in expected or match.group(2) in seen:
                raise ValueError("invalid internal SHA256SUMS inventory")
            seen.add(match.group(2))
            if hashlib.sha256(data[match.group(2)]).hexdigest() != match.group(1):
                raise ValueError("internal SHA256 mismatch")
        if seen != expected:
            raise ValueError("incomplete internal SHA256SUMS")
    except UnicodeError as exc:
        raise ValueError("non-ASCII internal SHA256SUMS") from exc
    return data


def verify_pair(ledger_zip, ledger_digest, results_zip, results_digest,
                *, run_id, source_sha, ledger_commit):
    """Independent original ZIP+internal checksums and ledger/result identity.

    This does not verify the actual Git remote ref or results delivery.
    """
    if (type(run_id) is not int or run_id <= 0 or
            not isinstance(source_sha, str) or not SOURCE_SHA.fullmatch(source_sha) or
            not isinstance(ledger_commit, str) or not SOURCE_SHA.fullmatch(ledger_commit)):
        raise ValueError("invalid immutable source/run/commit identity")
    lfiles = checked_zip(ledger_zip, ledger_digest, "ledger")
    rfiles = checked_zip(results_zip, results_digest, "results")
    try:
        state = ledger.verify(json.loads(lfiles["ledger.json"]))
        score = json.loads(lfiles["scoreboard.json"])
        latest = json.loads(lfiles["latest.json"])
        result = json.loads(rfiles["results.json"])
    except (UnicodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
        raise ValueError("invalid original PAPER JSON") from exc
    generation = state["generation"]
    if (type(generation) is not int or generation < 1 or
            not state["runs"] or
            state["runs"][-1]["as_of"] != result.get("as_of") or
            type(result.get("observed_markets")) is not int or
            result["observed_markets"] != state["runs"][-1]["observation_count"] or
            type(score.get("generation")) is not int or score["generation"] != generation or
            score.get("ledger_sha256") != state["sha256"] or
            result.get("ledger_sha256") != state["sha256"] or
            type(result.get("ledger_generation")) is not int or
            result["ledger_generation"] != generation or
            result.get("run_id") != str(run_id) or
            result.get("source_sha") != source_sha or
            result.get("ledger_commit") != ledger_commit or
            result.get("status") != "SUCCESS_PAPER_ONLY" or
            result.get("remote_readback_verified") is not True or
            result.get("buy_approved") is not False or
            result.get("exchange_event_freshness_verified") is not False or
            latest.get("mode") != "PAPER_ONLY" or
            latest.get("buy_approved") is not False or
            latest.get("as_of") != result.get("as_of") or
            (generation > 0 and (not state["runs"] or
                                 state["runs"][-1]["source_sha"] != source_sha))):
        raise ValueError("PAPER artifact identity or safety mismatch")
    # Independently bind each human-readable WATCH candidate to the actual
    # latest immutable ledger prediction. A self-resealed results.json cannot
    # invent a rank, price or score without detection.
    latest_run = state["runs"][-1]
    predictions = {p["rank"]: p for p in state["predictions"]
                   if p["run_id"] == latest_run["id"]}
    candidates = result.get("candidates")
    if (not isinstance(candidates, list) or
            len(candidates) != latest_run["watch_count"] or
            len(predictions) != latest_run["watch_count"]):
        raise ValueError("PAPER results candidate/ledger mismatch")
    for rank, candidate in enumerate(candidates, 1):
        expected = predictions.get(rank)
        if not isinstance(candidate, dict) or expected is None or (
                type(candidate.get("rank")) is not int or candidate["rank"] != rank or
                candidate.get("prediction_id") != expected["prediction_id"] or
                type(candidate.get("price_usd")) not in (int, float) or
                candidate["price_usd"] != expected["price"] or
                type(candidate.get("baseline_score")) not in (int, float) or
                candidate["baseline_score"] != expected["baseline_score"] or
                type(candidate.get("challenger_score")) not in (int, float) or
                candidate["challenger_score"] != expected["challenger_score"]):
            raise ValueError("PAPER results candidate/ledger mismatch")
    age = result.get("max_client_quote_age_seconds")
    if type(age) not in (int, float) or not 0 <= age <= 600:
        raise ValueError("client quote age missing, stale or invalid")
    return {"artifact_zip_bytes_independently_verified": True,
            "internal_sha256_verified": 5,
            "canonical_ledger_verified": True,
            "no_duplicate_scan_ids_verified": True,
            "ledger_generation": generation,
            "ledger_sha256": state["sha256"],
            "run_id": run_id, "source_sha": source_sha,
            "client_quote_age_seconds": age,
            "exchange_event_freshness_verified": False,
            "remote_ledger_readback_independently_verified": False,
            "results_delivery_verified": False}

def main():
    """One-command local, bounded verification of independently acquired ZIPs.

    Does not contact GitHub, write the ledger, or assert remote readback.
    """
    parser = argparse.ArgumentParser(description="Read-only PAPER artifact byte proof")
    parser.add_argument("--ledger-zip", required=True)
    parser.add_argument("--ledger-digest", required=True)
    parser.add_argument("--results-zip", required=True)
    parser.add_argument("--results-digest", required=True)
    parser.add_argument("--run-id", required=True, type=int)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--ledger-commit", required=True)
    args = parser.parse_args()

    def bounded_read(name):
        path = Path(name)
        if not 0 < path.stat().st_size <= MAX_ARCHIVE_BYTES:
            raise ValueError("oversized original artifact ZIP")
        return path.read_bytes()

    proof = verify_pair(
        bounded_read(args.ledger_zip), args.ledger_digest,
        bounded_read(args.results_zip), args.results_digest,
        run_id=args.run_id, source_sha=args.source_sha,
        ledger_commit=args.ledger_commit)
    print("PAPER_ARTIFACT_BYTES_READONLY " + json.dumps(proof, sort_keys=True))


if __name__ == "__main__":
    main()
