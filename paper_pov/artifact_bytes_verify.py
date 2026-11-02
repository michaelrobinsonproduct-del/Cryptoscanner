"""Offline, bounded verification of original PAPER artifact ZIP bytes.

This is NOT a GitHub downloader, a remote-ledger readback, a delivery receipt,
or exchange-event freshness proof. The caller must separately authenticate
the ZIP source and expected GitHub-reported digest.
"""
import hashlib
import io
import json
import re
import zipfile

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
    if (type(generation) is not int or generation < 0 or
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
