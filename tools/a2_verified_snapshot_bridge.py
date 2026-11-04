"""Adapter for A2's verified snapshot shape; paper WATCH is never live-certified.

Input MUST be the output of paper_pov.a2_artifact_consumer.read_artifact_zip
or paper_pov.candidate_snapshot.read_snapshot, not arbitrary scanner JSON.
The adapter adds a conservative stablecoin exclusion check.
"""
import argparse
import json
import math
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("verified_snapshot", type=Path, nargs="?",
                        help="JSON emitted by the existing verified A2 consumer")
    parser.add_argument("--a2-zip", type=Path,
                        help="A2 immutable inner transport ZIP; verify using A2's source consumer first")
    args = parser.parse_args()
    try:
        if bool(args.verified_snapshot) == bool(args.a2_zip):
            raise ValueError("provide exactly one verified snapshot or --a2-zip")
        if args.a2_zip:
            # Import only when the A2 source PR is present. The A2 consumer
            # verifies immutable receipt bytes, source SHA, and read-time freshness.
            from paper_pov.a2_artifact_consumer import read_artifact_zip
            verified = read_artifact_zip(args.a2_zip)
        else:
            verified = json.loads(args.verified_snapshot.read_text())
        result = assess_verified_a2(verified)
    except (OSError, ValueError, TypeError, ImportError, KeyError, AssertionError, RuntimeError):
        result = {"accepted": False, "status": "INVALID_A2_SNAPSHOT", "errors": ["unreadable_snapshot"]}
    print(json.dumps(result, sort_keys=True))
    return 0 if result["accepted"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
