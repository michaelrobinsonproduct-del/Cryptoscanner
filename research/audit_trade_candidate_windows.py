"""Strict descriptive audit of exact trade/OHLC candidate windows.

These windows are NOT independently complete trade history, executable fills,
predictive labels, a backtest, or a held-out improvement. Offline only.
"""
import math

STEP = 300
HORIZONS = (1, 6, 24, 48)
MAX_ROWS = 8000
# Official Kraken OHLCVT documentation, updated 2026-10-12, states that
# candles are emitted only for intervals with trades. This is a source
# semantics reference, NOT independent authentication of retained bytes.
SOURCE_GAP_DOCUMENTATION = "https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data"


def audit_candidate_windows(ohlc_rows, exact_timestamps):
    """Count candidate 30% peaks only when entry and every future candle match.

    Entry is the close of the candle opening at t, observable no earlier than
    t+300. The h-hour forward interval uses opens t+300 through t+h*3600.
    Missing future evidence abstains, never becomes a zero-return negative.
    """
    if not 0 < len(ohlc_rows) <= MAX_ROWS:
        raise ValueError("missing or oversized OHLC selection")
    source = {}
    previous = None
    for row in ohlc_rows:
        if len(row) != 7 or any(not isinstance(x, (int, float)) or
                                isinstance(x, bool) or not math.isfinite(x) for x in row):
            raise ValueError("invalid OHLC row")
        t, opening, high, low, close, volume, count = row
        if (t != int(t) or int(t) < 0 or int(t) % STEP or
                (previous is not None and t <= previous) or
                min(opening, high, low, close) <= 0 or
                low > opening or opening > high or low > close or close > high or
                volume < 0 or count < 0 or count != int(count)):
            raise ValueError("invalid OHLC chronology or values")
        source[int(t)] = row
        previous = t
    exact = set(exact_timestamps)
    if any(not isinstance(t, int) or isinstance(t, bool) or t not in source for t in exact):
        raise ValueError("unmatched or invalid exact candle timestamp")
    # The retained slice may end long before the present; missing future rows
    # are UNKNOWN beyond retained evidence, never claimed calendar-immature.
    last = max(source)
    # Count only interior gaps between retained source observations. The
    # retained slice's leading/trailing edges are UNKNOWN, never no-trade.
    observed_times = sorted(source)
    interior_gap_events = sum(b - a > STEP for a, b in zip(observed_times, observed_times[1:]))
    interior_missing_intervals = sum((b - a) // STEP - 1 for a, b in zip(observed_times, observed_times[1:]))
    result = {}
    for hours in HORIZONS:
        n = hours * 12
        complete = beyond_retained_end = gaps = peaks10 = peaks20 = peaks30 = 0
        largest = None
        first_entry = last_entry = None
        for t in sorted(exact):
            end = t + n * STEP
            if end > last:
                beyond_retained_end += 1
                continue
            future = [source.get(t + i * STEP) if t + i * STEP in exact else None
                      for i in range(1, n + 1)]
            if any(row is None for row in future):
                gaps += 1
                continue
            complete += 1
            first_entry = t if first_entry is None else first_entry
            last_entry = t
            peak_return = max(row[2] for row in future) / source[t][4] - 1.0
            largest = peak_return if largest is None else max(largest, peak_return)
            peaks10 += peak_return >= 0.10
            peaks20 += peak_return >= 0.20
            peaks30 += peak_return >= 0.30
        result[str(hours)] = {
            "candidate_entries": len(exact),
            "candidate_full_future_windows": complete,
            "excluded_beyond_retained_end": beyond_retained_end,
            "excluded_missing_exact_future": gaps,
            "descriptive_peak_10": peaks10,
            "descriptive_peak_20": peaks20,
            "descriptive_peak_30": peaks30,
            "largest_descriptive_peak_return": largest,
            "first_candidate_entry_open": first_entry,
            "last_candidate_entry_open": last_entry,
            "real_labels": 0,
        }
        if complete + beyond_retained_end + gaps != len(exact):
            raise AssertionError("candidate accounting mismatch")
    return {
        "status": "descriptive_candidates_source_completeness_unverified",
        "observation_timestamp_semantics": "candidate_candle_open_utc",
        "entry_as_of_offset_seconds": STEP,
        "source_gap_or_no_trade_semantics": "unknown_for_trade_completeness",
        "ohlc_interior_gap_events": interior_gap_events,
        "ohlc_interior_missing_intervals": interior_missing_intervals,
        "ohlc_gap_documentation_url": SOURCE_GAP_DOCUMENTATION,
        "ohlc_documented_semantics": "missing_candles_mean_no_trades_if_complete_source",
        "ohlc_gap_semantics_authorize_labels": False,
        "outside_retained_slice_semantics": "unknown",
        "candidate_exact_intervals": len(exact),
        "horizons": result,
        "real_labels": 0,
        "held_out_evaluation": "not_authorized",
        "executable_fill_verified": False,
    }
