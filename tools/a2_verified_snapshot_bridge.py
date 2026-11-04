"""Adapter for A2's verified snapshot shape; paper WATCH is never live-certified.

Input MUST be the output of paper_pov.a2_artifact_consumer.read_artifact_zip
or paper_pov.candidate_snapshot.read_snapshot, not arbitrary scanner JSON.
The adapter adds a conservative stablecoin exclusion check.
"""
import argparse
import datetime as dt
import hashlib
import json
import math
import os
import zipfile
from pathlib import Path

from tools.scan_receipt_gate import is_stablecoin_pair


def assess_verified_a2(snapshot):
    errors = []
    if not isinstance(snapshot, dict):
        return {"accepted": False, "paper_watch_count": 0, "live_watch_certified": False,
                "status": "INVALID_A2_SNAPSHOT", "errors": ["not_object"]}
    digest = snapshot.get("receipt_sha256")
    if not isinstance(digest, str) or len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
        errors.append("invalid_receipt_digest")
    if snapshot.get("scan_status") not in ("WATCH", "ABSTAIN_NO_LIQUID_CANDIDATES", "ABSTAIN_NO_QUALIFIED_OHLC"):
        errors.append("invalid_scan_status")
    watch = snapshot.get("watch")
    if not isinstance(watch, list) or len(watch) > 12:
        errors.append("invalid_watch_collection")
        watch = []
    if bool(watch) != (snapshot.get("scan_status") == "WATCH"):
        errors.append("inconsistent_watch_status")
    ages = snapshot.get("quote_age_seconds")
    if not isinstance(ages, dict) or set(ages) != {c.get("pair") for c in watch if isinstance(c, dict)}:
        errors.append("invalid_quote_age_coverage")
        ages = {}
    age = snapshot.get("snapshot_age_seconds")
    if type(age) not in (int, float) or not math.isfinite(age) or not 0 <= age <= 600:
        errors.append("snapshot_expired")
    seen = set()
    for rank, candidate in enumerate(watch, 1):
        if not isinstance(candidate, dict):
            errors.append("invalid_candidate")
            continue
        pair = candidate.get("pair")
        if not isinstance(pair, str) or not pair or pair in seen:
            errors.append("invalid_or_duplicate_pair")
        else:
            seen.add(pair)
            if is_stablecoin_pair(pair):
                errors.append("stablecoin_pair")
        if candidate.get("rank") != rank or candidate.get("status") != "PAPER_WATCH" or candidate.get("buy_approved") is not False:
            errors.append("invalid_paper_candidate")
        if candidate.get("quote_timestamp_semantics") != "client_observed_not_exchange_event_time":
            errors.append("unexpected_quote_semantics")
        quote_age = ages.get(pair) if isinstance(pair, str) else None
        if type(quote_age) not in (int, float) or not math.isfinite(quote_age) or not 0 <= quote_age <= 600:
            errors.append("quote_expired")
    return {"accepted": not errors, "paper_watch_count": len(watch) if not errors else 0,
            "live_watch_certified": False,
            "status": "PAPER_WATCH_NOT_EXCHANGE_EVENT_CERTIFIED" if not errors and watch else
                      "PAPER_ABSTAIN" if not errors else "INVALID_A2_SNAPSHOT",
            "receipt_sha256": digest if not errors else None, "errors": errors}


def read_scanner_receipt_zip(path, *, now=None, max_age_seconds=600):
    """Verify a raw two-member scanner artifact and enforce read-time freshness."""
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [item.filename for item in infos]
        if len(names) != 2 or len(set(names)) != 2 or "latest.json" not in names:
            raise ValueError("invalid scanner receipt archive members")
        receipts = [n for n in names if n.startswith("receipts/") and n.endswith(".json") and n.count("/") == 1]
        if len(receipts) != 1:
            raise ValueError("missing immutable scanner receipt")
        for item in infos:
            if item.is_dir() or item.file_size > 200000 or item.compress_size > 500000:
                raise ValueError("unsafe scanner receipt member")
        raw = archive.read("latest.json")
        if raw != archive.read(receipts[0]):
            raise ValueError("latest report differs from immutable receipt")
    report = json.loads(raw)
    if not isinstance(report, dict) or report.get("mode") != "PAPER_ONLY" or report.get("buy_approved") is not False or report.get("production_applied") is not False:
        raise ValueError("unsafe scanner report")
    stamp = dt.datetime.fromisoformat(report["as_of"].replace("Z", "+00:00"))
    if stamp.tzinfo is None:
        raise ValueError("naive scanner timestamp")
    now = now or dt.datetime.now(dt.timezone.utc)
    age = (now - stamp).total_seconds()
    if not 0 <= age <= max_age_seconds:
        raise ValueError("stale or future scanner receipt")
    watch = report.get("watch")
    if not isinstance(watch, list) or len(watch) > 12:
        raise ValueError("invalid scanner candidate list")
    quote_ages = {}
    for candidate in watch:
        if not isinstance(candidate, dict):
            raise ValueError("invalid scanner candidate")
        quote_stamp = dt.datetime.fromisoformat(candidate["quote_observed_at"].replace("Z", "+00:00"))
        quote_age = (now - quote_stamp).total_seconds()
        if quote_stamp.tzinfo is None or not 0 <= quote_age <= max_age_seconds:
            raise ValueError("stale or future candidate quote")
        quote_ages[candidate["pair"]] = quote_age
    return {"as_of": report["as_of"], "scan_status": report["scan_status"],
            "eligible_pairs": report["eligible_pairs"], "observed_markets": report["observed_markets"],
            "watch": watch, "quote_age_seconds": quote_ages, "snapshot_age_seconds": age,
            "receipt_sha256": hashlib.sha256(raw).hexdigest()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--a2-zip", type=Path,
                        help="Immutable A2 3-member transport ZIP or verified 2-member paper scanner ZIP")
    parser.add_argument("--output", type=Path,
                        help="New read-only, verified paper candidate handoff JSON; never overwrite")
    args = parser.parse_args()
    try:
        if not args.a2_zip:
            raise ValueError("A2 immutable ZIP is required")
        if args.a2_zip:
            # Preserve the established 3-member A2 transport consumer; also accept
            # the actual two-member scanner receipt artifact after strict verification.
            with zipfile.ZipFile(args.a2_zip) as archive:
                names = archive.namelist()
            if "verified-snapshot.json" in names:
                from paper_pov.a2_artifact_consumer import read_artifact_zip
                verified = read_artifact_zip(args.a2_zip)
            else:
                verified = read_scanner_receipt_zip(args.a2_zip)
        result = assess_verified_a2(verified)
        if result["accepted"] and args.output:
            if args.output.is_symlink() or args.output.exists():
                raise FileExistsError("verified handoff already exists")
            # No direct trade or live certification. Carry only verifier-approved
            # paper candidates and their receipt identity into downstream readers.
            payload = {"schema": 1, "mode": "VERIFIED_PAPER_WATCH_HANDOFF",
                       "receipt_sha256": result["receipt_sha256"],
                       "scan_status": verified["scan_status"],
                       "watch": verified["watch"],
                       "quote_age_seconds": verified["quote_age_seconds"],
                       "snapshot_age_seconds": verified["snapshot_age_seconds"],
                       "eligible_pairs": verified["eligible_pairs"],
                       "observed_markets": verified["observed_markets"],
                       "live_watch_certified": False,
                       "production_applied": False, "trading_approved": False}
            raw = (json.dumps(payload, sort_keys=True, separators=(",", ":"),
                              allow_nan=False) + "\\n").encode()
            # O_EXCL is the only writer path: no replacement or partial promotion
            # after invalid source/quote proof. Consumer can hash exact bytes.
            fd = os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "wb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
    except (OSError, ValueError, TypeError, ImportError, KeyError, AssertionError, RuntimeError):
        result = {"accepted": False, "status": "INVALID_A2_SNAPSHOT", "errors": ["unreadable_snapshot"]}
    print(json.dumps(result, sort_keys=True))
    return 0 if result["accepted"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
