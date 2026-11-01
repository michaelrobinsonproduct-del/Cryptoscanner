"""Read-only, fail-closed comparison of independently verified PAPER and legacy-inspired artifacts.

This module does NOT execute the legacy strategy or authenticate GitHub by itself.
Callers MUST verify source artifact bytes/digest against trusted GitHub metadata
before passing the expected digest; never manufacture shadow picks from PAPER
baseline/challenger scores. No trading, storage or scanner writer imports.
"""
import datetime as dt
import hashlib
import json
import math
import re

from .scanner import STABLE

HEX40 = re.compile(r"[0-9a-f]{40}\Z")
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
RUN = re.compile(r"[0-9]+\Z")
SYMBOL = re.compile(r"[A-Z0-9][A-Z0-9._-]*/USD\Z")
MAX_SKEW_SECONDS = 120
MAX_QUOTE_AGE_SECONDS = 600


def _utc(value):
    if not isinstance(value, str):
        raise ValueError("Missing UTC timestamp")
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("Naive timestamp")
    return parsed.astimezone(dt.timezone.utc)


def _sha(value, length):
    pattern = HEX40 if length == 40 else HEX64
    if not isinstance(value, str) or not pattern.fullmatch(value):
        raise ValueError("Missing immutable SHA provenance")


def _number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Invalid " + label)
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("Nonfinite " + label)
    return value


def _candidates(rows, *, as_of, legacy):
    if not isinstance(rows, list) or not 1 <= len(rows) <= 12:
        raise ValueError("Invalid independent candidate inventory")
    out = {}
    for i, item in enumerate(rows, 1):
        if not isinstance(item, dict):
            raise ValueError("Invalid candidate")
        symbol = item.get("symbol")
        if (not isinstance(symbol, str) or not SYMBOL.fullmatch(symbol) or symbol in out
                or symbol[:-4] in STABLE):
            raise ValueError("Ambiguous or duplicate canonical Kraken symbol")
        if item.get("rank") != i or type(item.get("rank")) is not int:
            raise ValueError("Invalid candidate ranking")
        if item.get("status") != "WATCH_PAPER_ONLY":
            raise ValueError("Only paper WATCH signals may be compared")
        price = _number(item.get("price_usd"), "price")
        if price <= 0:
            raise ValueError("Invalid price")
        observed = _utc(item.get("quote_observed_at"))
        age = (as_of - observed).total_seconds()
        if not 0 <= age <= MAX_QUOTE_AGE_SECONDS:
            raise ValueError("Missing, future or stale quote")
        if legacy:
            score = _number(item.get("legacy_score"), "independent legacy score")
            if "baseline_score" in item or "challenger_score" in item:
                raise ValueError("Legacy artifact cannot relabel current scanner scores")
        else:
            score = _number(item.get("challenger_score"), "PAPER score")
        out[symbol] = {"rank": i, "score": score, "price_usd": price}
    return out


def compare(current_artifact_bytes, legacy_artifact_bytes, *, expected_current_sha256,
            expected_current_run_id, expected_ledger_sha256,
            expected_legacy_sha256, expected_legacy_run_id):
    """Return verified overlap, or fail closed. Expected values must come from
    independent remote readback, never from the untrusted legacy payload.
    """
    _sha(expected_ledger_sha256, 64)
    _sha(expected_current_sha256, 64)
    _sha(expected_legacy_sha256, 64)
    if not isinstance(current_artifact_bytes, bytes):
        raise ValueError("Current artifact must be immutable bytes")
    if hashlib.sha256(current_artifact_bytes).hexdigest() != expected_current_sha256:
        raise ValueError("Current artifact digest mismatch")
    if not isinstance(legacy_artifact_bytes, bytes):
        raise ValueError("Shadow artifact must be immutable bytes")
    if hashlib.sha256(legacy_artifact_bytes).hexdigest() != expected_legacy_sha256:
        raise ValueError("Legacy artifact digest mismatch")
    try:
        current = json.loads(current_artifact_bytes)
        shadow = json.loads(legacy_artifact_bytes)
    except (ValueError, UnicodeError) as exc:
        raise ValueError("Invalid shadow JSON") from exc
    if not isinstance(current, dict) or not isinstance(shadow, dict):
        raise ValueError("Invalid report schemas")
    if (current.get("schema") != 1 or current.get("status") != "SUCCESS_PAPER_ONLY"
            or current.get("remote_readback_verified") is not True
            or current.get("ledger_sha256") != expected_ledger_sha256
            or current.get("production_applied") is not False
            or current.get("buy_approved") is not False):
        raise ValueError("Current PAPER report not independently anchored")
    _sha(current.get("source_sha"), 40)
    _sha(current.get("ledger_commit"), 40)
    if (not isinstance(expected_current_run_id, str) or not RUN.fullmatch(expected_current_run_id)
            or current.get("run_id") != expected_current_run_id):
        raise ValueError("Invalid PAPER run provenance")
    if (shadow.get("schema") != 1 or shadow.get("mode") != "LEGACY_INSPIRED_SHADOW"
            or shadow.get("independent_execution") is not True
            or shadow.get("production_applied") is not False
            or shadow.get("buy_approved") is not False
            or shadow.get("strategy_name") in (None, "", "baseline", "challenger")):
        raise ValueError("No independently identified legacy-inspired strategy")
    _sha(shadow.get("source_sha"), 40)
    # Time proximity alone does not prove this shadow belongs to this PAPER run.
    # Require the independent shadow execution to identify its actual trigger.
    if (not isinstance(shadow.get("trigger_paper_run_id"), str)
            or shadow["trigger_paper_run_id"] != current["run_id"]):
        raise ValueError("Shadow trigger PAPER run provenance mismatch")
    if (not isinstance(expected_legacy_run_id, str) or not RUN.fullmatch(expected_legacy_run_id)
            or shadow.get("run_id") != expected_legacy_run_id
            or shadow["run_id"] == current["run_id"]):
        raise ValueError("Independent shadow execution not proven")
    current_at, shadow_at = _utc(current.get("as_of")), _utc(shadow.get("as_of"))
    if abs((current_at - shadow_at).total_seconds()) > MAX_SKEW_SECONDS:
        raise ValueError("Scanner observations are not time-aligned")
    cutoff = _utc(shadow.get("feature_cutoff_utc"))
    if cutoff > shadow_at:
        raise ValueError("Shadow strategy used future features")
    main = _candidates(current.get("candidates"), as_of=current_at, legacy=False)
    other = _candidates(shadow.get("candidates"), as_of=shadow_at, legacy=True)
    overlap = []
    for symbol in sorted(main.keys() & other.keys(), key=lambda s: (main[s]["rank"], other[s]["rank"])):
        overlap.append({"symbol": symbol, "current_rank": main[symbol]["rank"],
                        "legacy_rank": other[symbol]["rank"],
                        "current_score": main[symbol]["score"],
                        "legacy_score": other[symbol]["score"],
                        "status": "DUAL_PAPER_WATCH"})
    return {"status": "VERIFIED_TIME_ALIGNED_OVERLAP", "as_of_current": current_at.isoformat(),
            "as_of_legacy": shadow_at.isoformat(), "current_run_id": current["run_id"],
            "legacy_run_id": shadow["run_id"], "ledger_sha256": expected_ledger_sha256,
            "legacy_artifact_sha256": expected_legacy_sha256,
            "current_count": len(main), "legacy_count": len(other),
            "overlap_count": len(overlap), "both_identified": overlap,
            "performance_lift": None, "trading_authorized": False,
            "note": "Agreement only; no held-out predictive lift or BUY authorization."}
