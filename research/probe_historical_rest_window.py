"""Bounded independent REST corroboration across a contiguous observed 1h window.

This is a source-correspondence audit, NOT an authenticated quarterly trade
completeness certificate or a predictive-label generator. Unobserved no-trade
intervals remain unknown; any source disagreement aborts the window.
"""
import argparse
import hashlib
import io
import json
import time
import zipfile
from pathlib import Path

from match_historical_trades_to_ohlcvt import aggregate, parse_member
from probe_historical_rest_interval import (
    MAX_EXPECTED_TRADES, STEP, compare_rest_bucket, corroborate_retained_ohlc,
)

MAX_TRADE_ARTIFACT = 12 * 1024 * 1024
MAX_MEMBER_BYTES = 3 * 1024 * 1024
WINDOW_CANDLES = 12
MAX_TOTAL_REST_BYTES = 24 * 1024 * 1024


def select_observed_window(path, *, candles=WINDOW_CANDLES):
    """Require every five-minute bucket to have observed retained trades.

    Do not infer that missing buckets are no-trade periods. Reject duplicate
    ZIP entries, malformed source rows, or windows exceeding bounded caps.
    """
    if type(candles) is not int or not 2 <= candles <= WINDOW_CANDLES:
        raise ValueError("invalid bounded window length")
    path = Path(path)
    if not path.is_file() or path.stat().st_size > MAX_TRADE_ARTIFACT:
        raise ValueError("missing or oversized retained trade artifact")
    candidate = None
    with zipfile.ZipFile(path) as archive:
        names = sorted(n for n in archive.namelist() if n.startswith("trades/") and n.endswith(".csv"))
        if not 1 <= len(names) <= 4 or len(names) != len(set(names)):
            raise ValueError("invalid retained trade market selection")
        for name in names:
            market = name.removeprefix("trades/").removesuffix(".csv")
            if not market.isalnum() or len(market) > 24:
                raise ValueError("unsafe market identity")
            info = archive.getinfo(name)
            if info.file_size > MAX_MEMBER_BYTES or info.flag_bits & 1:
                raise ValueError("unsafe retained trade member")
            raw = archive.read(info)
            scratch = io.BytesIO()
            with zipfile.ZipFile(scratch, "w") as z:
                z.writestr(market + ".csv", raw)
            with zipfile.ZipFile(io.BytesIO(scratch.getvalue())) as z:
                records = parse_member(z, market + ".csv", schema_verified=True)
            _, buckets = aggregate(records)
            starts = sorted(buckets)
            # Validate every selected retained member, including those after
            # the first candidate. A malformed later market must not be
            # hidden by an early successful window selection.
            if candidate is None:
                for i in range(len(starts) - candles + 1):
                    window = starts[i:i+candles]
                    if (all(window[j] == window[0] + j * STEP for j in range(candles)) and
                            all(1 <= len(buckets[t]) <= MAX_EXPECTED_TRADES for t in window)):
                        candidate = market, [(t, buckets[t]) for t in window]
                        break
    return candidate


def corroborate_observed_window(trades_path, ohlc_path, *, opener=None,
                                candles=WINDOW_CANDLES, delay_seconds=0):
    if not isinstance(delay_seconds, (int, float)) or not 0 <= delay_seconds <= 2:
        raise ValueError("invalid REST pacing")
    selected = select_observed_window(trades_path, candles=candles)
    base = {
        "status": "abstain_no_contiguous_observed_window",
        "observed_buckets_correlated": 0,
        "independent_complete_historical_intervals": 0,
        "independent_quarterly_completeness_verified": False,
        "no_trade_intervals_verified": 0,
        "real_labels": 0,
        "held_out_lift": None,
        "production_modified": False,
        "source_trade_artifact_sha256": hashlib.sha256(Path(trades_path).read_bytes()).hexdigest(),
    }
    if selected is None:
        return base
    market, window = selected
    base.update(market=market, first_bucket_open=window[0][0],
                last_bucket_open=window[-1][0], requested_observed_buckets=len(window))
    digests = []
    pages = bytes_read = 0
    for i, (start, expected) in enumerate(window):
        if i and delay_seconds:
            time.sleep(delay_seconds)
        try:
            rest = compare_rest_bucket(market, start, expected, opener=opener)
        except (OSError, RuntimeError, ValueError) as exc:
            base.update(status="abstain_rest_transport_or_source_error",
                        first_unverified_bucket=start, error_type=type(exc).__name__)
            return base
        pages += rest.get("pages", 0)
        bytes_read += rest.get("bytes_transferred", 0)
        if bytes_read > MAX_TOTAL_REST_BYTES:
            raise RuntimeError("REST window total byte budget exceeded")
        if rest.get("status") != "independent_rest_bucket_correlated" or not rest.get("after_end_witness"):
            base.update(status=rest.get("status", "abstain_rest_bucket_unverified"),
                        first_unverified_bucket=start, rest_pages=pages,
                        rest_bytes_transferred=bytes_read)
            return base
        three = corroborate_retained_ohlc(ohlc_path, market, start, expected, rest)
        if three.get("status") != "independent_rest_trade_ohlc_correlated" or not three.get("three_way_candle_correspondence"):
            base.update(status=three.get("status", "abstain_three_way_disagreement"),
                        first_unverified_bucket=start, rest_pages=pages,
                        rest_bytes_transferred=bytes_read)
            return base
        digests.extend(rest["rest_page_sha256"])
        base["observed_buckets_correlated"] += 1
    base.update(status="independent_rest_observed_window_correlated_not_complete",
                rest_pages=pages, rest_bytes_transferred=bytes_read,
                rest_page_sha256=digests,
                timestamp_semantics="observed_open_boundary_only",
                limitation="No independent quarterly completeness or no-trade proof; no forward labels")
    return base


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--retained-trades", required=True)
    parser.add_argument("--ohlc", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--delay-seconds", type=float, default=1)
    args = parser.parse_args()
    target = Path(args.output)
    if target.exists():
        raise FileExistsError("refuse historical window report overwrite")
    result = corroborate_observed_window(
        args.retained_trades, args.ohlc, delay_seconds=args.delay_seconds)
    raw = (json.dumps(result, sort_keys=True) + "\n").encode()
    if len(raw) > 8192:
        raise ValueError("oversized bounded REST window report")
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as stream:
        stream.write(raw)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
