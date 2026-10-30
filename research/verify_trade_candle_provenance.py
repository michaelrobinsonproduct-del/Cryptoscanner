"""Offline independent trade-to-OHLC candle-boundary verification.

Trade timestamps must originate from independently captured, source-identified
Kraken time-and-sales records, NOT derived from the OHLC file being checked.
No network, trading, archive downloads, or production reads/writes.
"""
from math import isfinite

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
    if any(not isinstance(x, (int, float)) or not isfinite(x) for x in values):
        return {"status": "invalid_evidence"}
    if timestamp % STEP or count != len(trades) or count <= 0:
        return {"status": "incomplete_evidence"}
    if any(len(t) != 4 or any(not isinstance(v, (int, float)) or not isfinite(v) for v in t) for t in trades):
        return {"status": "invalid_evidence"}
    ordered = sorted(trades, key=lambda t: (t[0], t[3]))
    if any(t[0] < timestamp or t[0] >= timestamp + STEP or t[1] <= 0 or t[2] <= 0 for t in ordered):
        return {"status": "timestamp_boundary_mismatch"}
    prices = [t[1] for t in ordered]
    if not (abs(prices[0] - opening) <= max(1e-8, abs(opening)*1e-9)
            and abs(prices[-1] - close) <= max(1e-8, abs(close)*1e-9)
            and abs(max(prices) - high) <= max(1e-8, abs(high)*1e-9)
            and abs(min(prices) - low) <= max(1e-8, abs(low)*1e-9)
            and abs(sum(t[2] for t in ordered) - volume) <= max(1e-8, abs(volume)*1e-8)):
        return {"status": "aggregation_mismatch"}
    return {"status": "verified_open_boundary", "candle_open": timestamp,
            "candle_close_as_of": timestamp + STEP, "trades": len(ordered)}
