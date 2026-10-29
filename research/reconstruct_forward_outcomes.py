"""Offline-only point-in-time forward-outcome reconstruction from observed 5m candles.

No database, network, production writer or interpolation. Timestamps are UTC epoch
seconds. Features are intentionally not inferred from future candles.
"""
from dataclasses import dataclass
from math import isfinite

HORIZONS_HOURS = (1, 6, 24, 48)
STEP = 300

@dataclass(frozen=True)
class Candle:
    timestamp: int
    high: float
    close: float
    volume: float

def reconstruct(candles, observation_timestamp, *, min_quote_volume=None):
    """Return strict, mature, gap-aware labels, or reasons for abstention.

    A horizon is mature only if the exact horizon-end candle exists; missing
    intermediate candles are never treated as zero movement or interpolated.
    Price return is max observed future high / entry close - 1, with a
    separately reported coverage ratio; strict labels require full coverage.
    """
    if not isinstance(observation_timestamp, int) or isinstance(observation_timestamp, bool):
        raise ValueError("timestamp must be integer UTC epoch seconds")
    if observation_timestamp % STEP:
        raise ValueError("timestamp must align to 5m UTC")
    if min_quote_volume is not None and (not isfinite(min_quote_volume) or min_quote_volume < 0):
        raise ValueError("invalid liquidity threshold")
    by_time = {}
    for c in candles:
        if not isinstance(c.timestamp, int) or isinstance(c.timestamp, bool) or c.timestamp % STEP:
            raise ValueError("invalid candle timestamp")
        if any(not isfinite(v) for v in (c.high, c.close, c.volume)):
            raise ValueError("nonfinite candle")
        if c.high <= 0 or c.close <= 0 or c.high < c.close or c.volume < 0:
            raise ValueError("invalid candle values")
        if c.timestamp in by_time:
            raise ValueError("duplicate candle timestamp")
        by_time[c.timestamp] = c
    entry = by_time.get(observation_timestamp)
    if entry is None:
        return {"status": "missing_entry", "horizons": {}}
    if min_quote_volume is not None and entry.volume * entry.close < min_quote_volume:
        return {"status": "insufficient_entry_liquidity", "horizons": {}}
    latest = max(by_time)
    horizons = {}
    for h in HORIZONS_HOURS:
        end = observation_timestamp + h * 3600
        expected = h * 12
        future = [by_time[t] for t in range(observation_timestamp + STEP, end + STEP, STEP) if t in by_time]
        coverage = len(future) / expected
        if latest < end:
            horizons[str(h)] = {"status": "immature", "coverage": coverage}
        elif end not in by_time or len(future) != expected:
            horizons[str(h)] = {"status": "gap", "coverage": coverage}
        else:
            peak = max(c.high for c in future)
            ret = peak / entry.close - 1
            horizons[str(h)] = {"status": "mature", "coverage": 1.0,
                                "peak_return": ret,
                                "hit_10": ret >= .10, "hit_20": ret >= .20,
                                "hit_30": ret >= .30}
    return {"status": "ok", "entry_timestamp": observation_timestamp,
            "entry_close": entry.close, "horizons": horizons}
