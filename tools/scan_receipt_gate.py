"""Read-only fail-closed validation of scanner candidate receipts.

This helper does not certify a live exchange source or write production state.
"""
import argparse
import datetime as dt
import json
import math
from pathlib import Path


def parse_time(value):
    if not isinstance(value, str):
        raise ValueError("timestamp must be a string")
    stamp = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if stamp.tzinfo is None:
        raise ValueError("timestamp must be timezone-aware")
    return stamp.astimezone(dt.timezone.utc)


def validate_receipt(receipt, *, now, max_age_seconds=600):
    """Return machine-readable failures; accept only explicit source evidence."""
    if not isinstance(receipt, dict):
        return ["receipt_not_object"]
    if not isinstance(now, dt.datetime) or now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    if isinstance(max_age_seconds, bool) or not isinstance(max_age_seconds, int) or max_age_seconds <= 0:
        raise ValueError("max_age_seconds must be a positive integer")
    errors = []
    if receipt.get("source") != "kraken":
        errors.append("source_not_authenticated_kraken")
    status = receipt.get("status")
    if status not in ("WATCH", "ABSTAIN"):
        errors.append("invalid_status")
    if status == "WATCH" and receipt.get("source_authenticated") is not True:
        errors.append("watch_without_source_authentication")
    if status == "WATCH" and receipt.get("exchange_event_freshness_verified") is not True:
        errors.append("watch_without_exchange_freshness_evidence")
    for field in ("observed_at", "source_as_of"):
        try:
            age = (now.astimezone(dt.timezone.utc) - parse_time(receipt.get(field))).total_seconds()
            if age < 0:
                errors.append(field + "_future")
            elif age > max_age_seconds:
                errors.append(field + "_stale")
        except (ValueError, TypeError, OverflowError):
            errors.append(field + "_invalid")
    candidates = receipt.get("candidates")
    if not isinstance(candidates, list):
        return errors + ["candidates_not_array"]
    seen = set()
    for index, candidate in enumerate(candidates):
        prefix = "candidate_" + str(index) + "_"
        if not isinstance(candidate, dict):
            errors.append(prefix + "not_object")
            continue
        pair = candidate.get("pair")
        if not isinstance(pair, str) or not pair.strip():
            errors.append(prefix + "invalid_pair")
        elif pair in seen:
            errors.append(prefix + "duplicate_pair")
        else:
            seen.add(pair)
        price = candidate.get("price")
        if isinstance(price, bool) or not isinstance(price, (int, float)) or not math.isfinite(price) or price <= 0:
            errors.append(prefix + "invalid_price")
        if candidate.get("stablecoin_excluded") is not True:
            errors.append(prefix + "stablecoin_filter_unverified")
        try:
            age = (now.astimezone(dt.timezone.utc) - parse_time(candidate.get("quote_at"))).total_seconds()
            if age < 0 or age > max_age_seconds:
                errors.append(prefix + "quote_not_fresh")
        except (ValueError, TypeError, OverflowError):
            errors.append(prefix + "quote_timestamp_invalid")
    if status == "WATCH" and not candidates:
        errors.append("watch_without_candidates")
    if status == "ABSTAIN" and candidates:
        errors.append("abstain_with_candidates")
    return errors


def main():
    parser = argparse.ArgumentParser(description="Read-only candidate receipt gate")
    parser.add_argument("receipt", type=Path)
    parser.add_argument("--now", required=True, help="Explicit ISO 8601 time")
    args = parser.parse_args()
    try:
        errors = validate_receipt(json.loads(args.receipt.read_text()), now=parse_time(args.now))
    except (OSError, ValueError, TypeError) as exc:
        errors = ["receipt_unreadable_or_invalid:" + type(exc).__name__]
    print(json.dumps({"accepted": not errors, "errors": errors}, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
