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


def reconstruct_as_of(candles, observation_as_of, *, min_quote_volume=None,
                      source_timestamp_semantics=None):
    """Fail-closed labels for Kraken 5m OPEN-timestamped candles.

    observation_as_of is the exact close boundary of the entry candle, i.e.
    source opening timestamp + 300 seconds. Only fully closed entry candles
    may supply entry close and volume. Future labels use complete candles
    opening at or after observation_as_of; their 1/6/24/48h boundaries are
    measured from observation_as_of, not from the entry candle opening.
    This is an offline research label, not evidence of executable fills.
    """
    if source_timestamp_semantics != "candle_open_utc":
        return {"status": "unverified_source_timestamp_semantics", "horizons": {}}
    if not isinstance(observation_as_of, int) or isinstance(observation_as_of, bool) or observation_as_of % STEP:
        raise ValueError("as-of timestamp must align to 5m UTC")
    entry_open = observation_as_of - STEP
    # The existing strict reconstruction expects entry at observation_timestamp.
    # Rebase timestamps by one candle, so horizons include exactly the
    # candles opening [as_of, as_of + horizon - STEP].
    shifted = [Candle(c.timestamp + STEP, c.high, c.close, c.volume) for c in candles]
    result = reconstruct(shifted, observation_as_of, min_quote_volume=min_quote_volume)
    if result["status"] == "ok":
        result["observation_as_of"] = observation_as_of
        result["entry_source_open"] = entry_open
        result["source_timestamp_semantics"] = source_timestamp_semantics
    return result
