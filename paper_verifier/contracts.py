"""Fail-closed, paper-only prediction ledger and forward-label contract.

This validates declared provenance fields; it does NOT authenticate Kraken source
completeness or establish predictive lift. No network, trading, or writes.
"""
import datetime as dt
import hashlib
import json
import math
import re

ZERO_HASH = "0" * 64
HORIZONS = (1, 6, 24, 48)
STABLE_BASES = frozenset({"USDT", "USDC", "DAI", "TUSD", "PYUSD", "RLUSD",
                          "EURC", "FDUSD", "FRAX", "GUSD", "USDD"})
HEX64 = re.compile(r"^[0-9a-f]{64}$")
PAIR = re.compile(r"^[A-Z0-9]{2,20}/USD$")


class ContractError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ContractError(message)


def utc(value):
    require(isinstance(value, str), "timestamp must be text")
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ContractError("invalid timestamp") from exc
    require(parsed.tzinfo is not None and parsed.utcoffset() == dt.timedelta(0),
            "timestamp must have explicit UTC timezone")
    return parsed.astimezone(dt.timezone.utc)


def positive(value):
    return (type(value) in (int, float) and math.isfinite(value) and value > 0)


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def record_hash(record):
    body = {k: v for k, v in record.items() if k != "hash"}
    return digest(json.dumps(body, sort_keys=True, separators=(",", ":"),
                             allow_nan=False).encode("utf-8"))


def verify_ledger(records, *, now=None, max_records=5000):
    require(isinstance(records, list) and len(records) <= max_records,
            "ledger missing or exceeds bounded size")
    current_time = utc(now) if now is not None else None
    previous_hash, previous_time = ZERO_HASH, None
    identities = set()
    for record in records:
        require(isinstance(record, dict), "prediction must be an object")
        for key in ("prediction_id", "pair", "as_of", "source_observed_at",
                    "recorded_at", "source_sha256", "status", "prev_hash", "hash"):
            require(key in record, "missing prediction field: " + key)
        pair = record["pair"]
        require(isinstance(pair, str) and PAIR.fullmatch(pair) is not None,
                "pair must be normalized BASE/USD")
        require(pair.split("/")[0] not in STABLE_BASES, "stablecoin excluded")
        require(isinstance(record["prediction_id"], str)
                and 1 <= len(record["prediction_id"]) <= 128,
                "invalid prediction identity")
        as_of = utc(record["as_of"])
        source_at = utc(record["source_observed_at"])
        recorded = utc(record["recorded_at"])
        require(source_at <= as_of <= recorded, "prediction uses future source or backdating")
        require(as_of - source_at <= dt.timedelta(minutes=10), "stale source")
        require(recorded - as_of <= dt.timedelta(minutes=5), "late recording")
        if current_time is not None:
            require(recorded <= current_time, "prediction recorded in the future")
        if previous_time is not None:
            require(as_of >= previous_time, "ledger as-of timestamps regressed")
        require((record["prediction_id"], pair, record["as_of"]) not in identities,
                "duplicate prediction identity")
        identities.add((record["prediction_id"], pair, record["as_of"]))
        require(isinstance(record["source_sha256"], str)
                and HEX64.fullmatch(record["source_sha256"]) is not None,
                "missing or invalid source digest")
        require(record["status"] in ("PAPER_WATCH", "ABSTAIN"), "nonpaper status")
        if record["status"] == "PAPER_WATCH":
            require(positive(record.get("entry_price")), "invalid entry price")
            score = record.get("score")
            require(type(score) in (int, float) and math.isfinite(score)
                    and 0 <= score <= 100, "invalid paper score")
        else:
            require(record.get("entry_price") is None and record.get("score") is None
                    and isinstance(record.get("reason"), str)
                    and bool(record["reason"].strip()), "abstention must have reason and no signal")
        require(record["prev_hash"] == previous_hash, "broken history hash chain")
        require(isinstance(record["hash"], str) and record["hash"] == record_hash(record),
                "prediction mutated or hash invalid")
        previous_hash, previous_time = record["hash"], as_of
    return {"records": len(records), "head_sha256": previous_hash}


def verify_continuity(previous, current, *, genesis_authorized=False):
    require(previous is not None, "missing remote ledger; refuse silent reset")
    require(isinstance(previous, list) and isinstance(current, list), "invalid ledger")
    require(previous or genesis_authorized, "empty history requires explicit genesis")
    verify_ledger(previous)
    verify_ledger(current)
    require(len(current) >= len(previous), "history shrank")
    require(current[:len(previous)] == previous, "historical predictions rewritten")
    return len(current) - len(previous)


def verify_outcome(prediction, outcome, *, now):
    """Validate a claimed outcome; provider proof must be checked independently."""
    require(isinstance(prediction, dict) and isinstance(outcome, dict), "invalid outcome")
    require(prediction.get("status") == "PAPER_WATCH", "no label for abstention")
    require(outcome.get("prediction_id") == prediction.get("prediction_id"),
            "prediction/outcome identity mismatch")
    horizon = outcome.get("horizon_hours")
    require(type(horizon) is int and horizon in HORIZONS, "unsupported horizon")
    target = utc(prediction["as_of"]) + dt.timedelta(hours=horizon)
    require(utc(now) >= target, "immature outcome")
    if outcome.get("status") == "ABSTAIN":
        require(isinstance(outcome.get("reason"), str) and outcome["reason"].strip(),
                "outcome abstention reason required")
        require(outcome.get("return_pct") is None, "abstention cannot carry a label")
        return "ABSTAIN"
    require(outcome.get("status") == "EVALUATED", "invalid outcome status")
    proof = outcome.get("source_proof")
    require(isinstance(proof, dict) and proof.get("source") == "Kraken"
            and proof.get("interval_complete") is True,
            "missing independently verified complete source claim")
    require(isinstance(proof.get("sha256"), str)
            and HEX64.fullmatch(proof["sha256"]) is not None,
            "missing source artifact checksum")
    run_id = proof.get("verification_run_id")
    require(type(run_id) is int and run_id > 0, "missing source verification run")
    require(outcome.get("gap_count") == 0 and type(outcome.get("gap_count")) is int,
            "unverified gaps")
    require(positive(outcome.get("quote_liquidity_usd"))
            and outcome["quote_liquidity_usd"] >= 100000, "insufficient liquidity")
    spread = outcome.get("spread_bps")
    require(type(spread) in (int, float) and math.isfinite(spread)
            and 0 <= spread <= 45, "invalid or excessive spread")
    observed_at = utc(outcome["observed_at"])
    require(target <= observed_at <= target + dt.timedelta(minutes=15),
            "missing or late horizon observation")
    require(observed_at <= utc(now), "future price observation")
    require(positive(outcome.get("exit_price"))
            and positive(prediction.get("entry_price")), "invalid prices")
    claimed = outcome.get("return_pct")
    actual = 100 * (outcome["exit_price"] / prediction["entry_price"] - 1)
    require(type(claimed) in (int, float) and math.isfinite(claimed)
            and abs(claimed - actual) <= 0.0001,
            "outcome return inconsistent with source prices")
    return "EVALUATED"


def verify_artifact(data, expected_sha256):
    require(isinstance(data, bytes) and isinstance(expected_sha256, str)
            and HEX64.fullmatch(expected_sha256) is not None,
            "artifact digest contract invalid")
    require(digest(data) == expected_sha256, "artifact checksum mismatch")
    return True
