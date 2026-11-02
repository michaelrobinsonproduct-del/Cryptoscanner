"""Bounded hindsight-only OHLC entry candidates; never authenticated labels.

Entry proxy: five-minute candle close. Outcome proxy: maximum high of
subsequent candles. Missing intervals abstain. A fixed non-overlapping cohort
limits duplicate windows but is phase-sensitive, not an independent backtest.
No network, production, scoring, ledger or trading writes.
"""
import argparse
import csv
from collections import deque
from decimal import Decimal
import hashlib
import io
import json
from pathlib import Path
import zipfile

from research.kraken_archive_readiness import ARCHIVE_SHA, HORIZONS, STEP, inspect_retained


def _forward_max(values, width):
    """At i, max of values[i+1:i+width+1], or None if incomplete."""
    result = [None] * len(values)
    q = deque()
    for i in range(len(values) - 1, -1, -1):
        j = i + 1
        if j < len(values):
            while q and values[q[-1]] <= values[j]:
                q.pop()
            q.append(j)
        while q and q[0] > i + width:
            q.popleft()
        if i + width < len(values):
            result[i] = values[q[0]]
    return result


def _segments(rows):
    start = 0
    for i in range(1, len(rows)):
        if rows[i][0] != rows[i - 1][0] + STEP:
            yield rows[start:i]
            start = i
    yield rows[start:]


def inspect_candidates(path, *, expected_archive_sha=ARCHIVE_SHA):
    """Require verified retained members before counting price-path proxies."""
    readiness = inspect_retained(path, expected_archive_sha=expected_archive_sha)
    result = {str(h): {
        "contiguous_entry_windows": 0,
        "hindsight_high_ge20pct_windows": 0,
        "hindsight_high_ge30pct_windows": 0,
        "nonoverlap_cohort_entries": 0,
        "cohort_hindsight_ge20pct": 0,
        "cohort_hindsight_ge30pct": 0,
        "cohort_hindsight_lt30pct": 0,
        "cohort_markets": 0,
        "cohort_markets_ge30pct": 0,
    } for h in HORIZONS}
    with zipfile.ZipFile(path) as archive:
        manifest = json.loads(archive.read("manifest.json"))
        for name in sorted(manifest["markets"]):
            data = archive.read("candles/" + name)
            if hashlib.sha256(data).hexdigest() != manifest["markets"][name]["retained_sha256"]:
                raise ValueError("retained SHA changed after readiness audit")
            rows = [(int(row[0]), Decimal(row[4]), Decimal(row[2]))
                    for row in csv.reader(io.StringIO(data.decode("utf-8")))]
            for horizon in HORIZONS:
                width = horizon * 12
                out = result[str(horizon)]
                market_entries = market_positive = 0
                for segment in _segments(rows):
                    if len(segment) <= width:
                        continue
                    closes = [row[1] for row in segment]
                    future = _forward_max([row[2] for row in segment], width)
                    for i in range(len(segment) - width):
                        out["contiguous_entry_windows"] += 1
                        ratio = future[i] / closes[i]
                        out["hindsight_high_ge20pct_windows"] += ratio >= Decimal("1.2")
                        out["hindsight_high_ge30pct_windows"] += ratio >= Decimal("1.3")
                    # Twelve prior candles required; sample future horizons
                    # without overlap. This is not an executable-entry claim.
                    for i in range(12, len(segment) - width, width):
                        market_entries += 1
                        out["nonoverlap_cohort_entries"] += 1
                        ratio = future[i] / closes[i]
                        out["cohort_hindsight_ge20pct"] += ratio >= Decimal("1.2")
                        if ratio >= Decimal("1.3"):
                            market_positive += 1
                            out["cohort_hindsight_ge30pct"] += 1
                        else:
                            out["cohort_hindsight_lt30pct"] += 1
                out["cohort_markets"] += market_entries > 0
                out["cohort_markets_ge30pct"] += market_positive > 0
    for horizon in HORIZONS:
        out = result[str(horizon)]
        if out["contiguous_entry_windows"] != readiness["candidate_windows"][str(horizon)]:
            raise ValueError("candidate window conservation failed")
        if out["cohort_hindsight_ge30pct"] + out["cohort_hindsight_lt30pct"] != out["nonoverlap_cohort_entries"]:
            raise ValueError("cohort partition failed")
    return {
        "status": "DESCRIPTIVE_OHLC_CANDIDATES_ONLY_NOT_AUTHENTICATED_EPISODES",
        "source_archive_sha256_claim": expected_archive_sha,
        "retained_members_verified": True,
        "markets": readiness["markets"],
        "retained_rows": readiness["retained_rows"],
        "entry_proxy": "close_of_5m_candle",
        "outcome_proxy": "maximum_high_of_next_horizon_candles",
        "cohort_rule": "start_at_12th_prior_candle_index_then_stride_horizon",
        "first_observed_at_available": False,
        "complete_trade_path_verified": False,
        "point_in_time_liquidity_available": False,
        "authenticated_first_entry_episodes": 0,
        "held_out_lift": None,
        "production_applied": False,
        "horizons": result,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--retained-zip", required=True)
    parser.add_argument("--expected-archive-sha", default=ARCHIVE_SHA)
    parser.add_argument("--output")
    args = parser.parse_args()
    payload = json.dumps(inspect_candidates(args.retained_zip, expected_archive_sha=args.expected_archive_sha), sort_keys=True, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
