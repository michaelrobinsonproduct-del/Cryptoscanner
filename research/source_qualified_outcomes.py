"""E1: conservative point-in-time outcomes from independently observed source rows.

No candle high proxies, backdating, trading, scoring or production writes.
"""
from decimal import Decimal, InvalidOperation

STEP = 300
MAX_AGE = 600
SLOT_TOLERANCE = 60  # observed capture cadence, not exchange quote-update cadence


def _decimal(value):
    try:
        n = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("invalid price") from None
    if not n.is_finite() or n <= 0:
        raise ValueError("invalid price")
    return n


def qualify(entry, observations, horizon_hours=1):
    """Label only a fully observed contiguous forward path; otherwise abstain.

    Each row must be an independently received Kraken snapshot with its own
    first-observed timestamp and SHA256 source receipt. A missing slot, stale
    exchange event, duplicate slot or late receipt disqualifies the whole path.
    """
    if horizon_hours not in (1, 6, 24, 48):
        raise ValueError("unsupported horizon")
    expected = horizon_hours * 12
    rows = [entry, *observations]
    if len(rows) != expected + 1:
        return {"status": "ABSTAIN_INCOMPLETE", "expected_forward_slots": expected,
                "observed_forward_slots": len(observations)}
    try:
        start = float(entry["first_observed_at"])
        entry_price = _decimal(entry["ask"])
        max_price = entry_price
        for i, row in enumerate(rows):
            event = float(row["event_at"])
            observed = float(row["first_observed_at"])
            receipt = row["source_sha256"]
            if not isinstance(receipt, str) or len(receipt) != 64 or any(c not in "0123456789abcdef" for c in receipt):
                return {"status": "ABSTAIN_SOURCE_RECEIPT"}
            if row["pair"] != entry["pair"] or abs(observed - (start + i * STEP)) > SLOT_TOLERANCE:
                return {"status": "ABSTAIN_PATH_GAP"}
            if observed < event or observed - event > MAX_AGE:
                return {"status": "ABSTAIN_OBSERVATION_TIME"}
            if i and observed <= float(rows[i - 1]["first_observed_at"]):
                return {"status": "ABSTAIN_PATH_GAP"}
            if i:
                # Bid is executable sell-side proxy, not an OHLC hindsight high.
                max_price = max(max_price, _decimal(row["bid"]))
            else:
                _decimal(row["bid"])
    except (KeyError, TypeError, ValueError, OverflowError):
        return {"status": "ABSTAIN_INVALID_SOURCE"}
    return {"status": "QUALIFIED_OBSERVED_PATH", "forward_slots": expected,
            "ge30pct": max_price >= entry_price * Decimal("1.30"),
            "max_observed_bid_over_entry_ask": str(max_price / entry_price),
            "source": "prospective_observed_quotes_only", "held_out_lift": None,
            "production_applied": False}
