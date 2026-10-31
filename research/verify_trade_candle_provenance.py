"""Offline independent trade-to-OHLC candle-boundary verification.

Trade timestamps must originate from independently captured, source-identified
Kraken time-and-sales records, NOT derived from the OHLC file being checked.
No network, trading, archive downloads, or production reads/writes.
"""
from math import isfinite, isclose

STEP = 300


def verify_open_boundary(candle, trades, *, independent_trade_source=False):
    """Return verified only for exact, independently sourced trade aggregation.

    candle = (timestamp, open, high, low, close, base_volume, count)
    trades = (epoch_seconds, price, base_volume, stable_order) for every trade
    in that interval, including boundaries. A partial trade sample abstains.
    """
    if not independent_trade_source:
        return {"status": "unverified_independent_trade_source"}
    if len(candle) != 7 or not trades:
        return {"status": "incomplete_evidence"}
    timestamp, opening, high, low, close, volume, count = candle
    values = [timestamp, opening, high, low, close, volume, count]
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x)
           for x in values):
        return {"status": "invalid_evidence"}
    # A source candle is an opening-time 5-minute bucket, not an arbitrary
    # point in time. Integer-valued floats are accepted from source CSVs.
    if (timestamp < 0 or timestamp != int(timestamp) or timestamp % STEP or
            count <= 0 or count != int(count) or count != len(trades) or
            min(opening, high, low, close) <= 0 or
            low > opening or opening > high or low > close or close > high or
            volume <= 0):
        return {"status": "incomplete_evidence"}
    if any(len(t) != 4 or any(isinstance(v, bool) or
            not isinstance(v, (int, float)) or not isfinite(v) for v in t)
           for t in trades):
        return {"status": "invalid_evidence"}
    # Stable order is source-row order. Duplicate or fractional order values
    # can silently invent the open/close of same-timestamp trades.
    order_ids = [t[3] for t in trades]
    if any(v < 0 or v != int(v) for v in order_ids) or len(set(order_ids)) != len(order_ids):
        return {"status": "invalid_evidence"}
    ordered = sorted(trades, key=lambda t: (t[0], t[3]))
    if any(t[0] < timestamp or t[0] >= timestamp + STEP or t[1] <= 0 or t[2] <= 0 for t in ordered):
        return {"status": "timestamp_boundary_mismatch"}
    prices = [t[1] for t in ordered]
    # Never use an absolute 1e-8 tolerance: for micro-priced assets that
    # can accept a 100% price discrepancy or orders-of-magnitude volume drift.
    # Relative tolerance absorbs floating-point CSV arithmetic without
    # manufacturing agreement for small early-mover prices or volumes.
    if not (isclose(prices[0], opening, rel_tol=1e-9, abs_tol=0.0)
            and isclose(prices[-1], close, rel_tol=1e-9, abs_tol=0.0)
            and isclose(max(prices), high, rel_tol=1e-9, abs_tol=0.0)
            and isclose(min(prices), low, rel_tol=1e-9, abs_tol=0.0)
            and isclose(sum(t[2] for t in ordered), volume,
                        rel_tol=1e-8, abs_tol=0.0)):
        return {"status": "aggregation_mismatch"}
    return {"status": "verified_open_boundary", "candle_open": timestamp,
            "candle_close_as_of": timestamp + STEP, "trades": len(ordered)}
