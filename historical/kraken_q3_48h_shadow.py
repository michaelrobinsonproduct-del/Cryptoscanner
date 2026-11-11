"""Read-only Kraken Q3 2026 OHLCVT as-of +30% historical shadow experiment.

Read the official Kraken five-minute OHLCVT ZIP directly. No future information
enters feature generation or as-of liquidity selection; unobserved intervals
are never filled. A frozen validation-independent challenger is evaluated on
the same chronological holdout candidates as a simple momentum proxy. This
does NOT replay the live scorer, establish executable fills, or promote models.
"""
import argparse
import csv
import datetime as dt
import hashlib
import heapq
import json
import math
import statistics
import zipfile
from collections import defaultdict
from pathlib import Path

FIVE_MIN = 300
HORIZONS = (1, 6, 24, 48)
FEATURES = ("momentum_5m", "momentum_15m", "momentum_60m",
            "volume_accel", "trade_accel", "volatility_60m")
TRAIN_END = int(dt.datetime(2026, 8, 14, tzinfo=dt.timezone.utc).timestamp())
VALID_START = int(dt.datetime(2026, 8, 18, tzinfo=dt.timezone.utc).timestamp())
VALID_END = int(dt.datetime(2026, 9, 1, tzinfo=dt.timezone.utc).timestamp())
TEST_START = int(dt.datetime(2026, 9, 5, tzinfo=dt.timezone.utc).timestamp())
TEST_END = int(dt.datetime(2026, 9, 28, tzinfo=dt.timezone.utc).timestamp())
START = int(dt.datetime(2026, 7, 1, tzinfo=dt.timezone.utc).timestamp())
MAX_NOTIONAL_CANDIDATES = 12
EXCLUDED_BASES = {"USDT", "USDC", "DAI", "PYUSD", "USD1", "TUSD", "USDD", "RLUSD", "EURC"}


def parse_bar(row):
    if len(row) < 7:
        return None
    try:
        stamp = float(row[0])
        if not stamp.is_integer() or not math.isfinite(stamp):
            return None
        timestamp = int(stamp)
        if timestamp % FIVE_MIN:
            return None
        op, hi, lo, close, vol, trades = map(float, row[1:7])
        if not all(math.isfinite(x) for x in (op, hi, lo, close, vol, trades)):
            return None
        if not (0 < lo <= min(op, close) <= max(op, close) <= hi):
            return None
        if vol < 0 or trades < 0:
            return None
    except (ValueError, OverflowError, TypeError):
        return None
    return (timestamp, close, vol, trades)


def parse_market(name):
    filename = Path(name).name
    if not filename.endswith("_5.csv"):
        return None
    pair = filename[:-6]
    if not pair.endswith("USD") or pair[:-3] in EXCLUDED_BASES:
        return None
    return pair


def split_for_stamp(stamp):
    if START <= stamp < TRAIN_END:
        return "train"
    if VALID_START <= stamp < VALID_END:
        return "validation"
    if TEST_START <= stamp < TEST_END:
        return "test"
    return "embargo"


def outcomes_for_anchor(bars, i, gap_prefix):
    """Never issue a binary miss if even one future five-minute bar is missing."""
    stamp, entry, _, _ = bars[i]
    outcomes = {}
    for hours in HORIZONS:
        end = i + hours * 12
        if end >= len(bars) or bars[end][0] != stamp + hours * 3600:
            outcomes[str(hours)] = None
            continue
        if gap_prefix[end] != gap_prefix[i]:
            outcomes[str(hours)] = None
            continue
        # Close maximum is an observable retrospective upper bound, not an execution.
        closes = (bar[1] for bar in bars[i + 1:end + 1])
        outcomes[str(hours)] = max(closes) / entry - 1
    return outcomes


def candidate_rows(pair, bars):
    """Yield one as-of hourly candidate; lookback cannot use a future candle."""
    bars = sorted(bars)
    unique = []
    for bar in bars:
        if unique and bar[0] == unique[-1][0]:
            if bar != unique[-1]:
                raise ValueError("Conflicting historical candle at " + str(bar[0]))
            continue
        unique.append(bar)
    bars = unique
    gaps = [0] * len(bars)
    for i in range(1, len(bars)):
        gaps[i] = gaps[i-1] + int(bars[i][0] - bars[i-1][0] != FIVE_MIN)
    for i in range(12, len(bars)):
        stamp, price, _, _ = bars[i]
        # Kraken rows are OPEN-timestamped. The observed close is not known
        # until the bar has finished five minutes later.
        asof = stamp + FIVE_MIN
        if asof % 3600 or not START <= asof < TEST_END:
            continue
        if bars[i-12][0] != stamp-3600 or gaps[i] != gaps[i-12]:
            continue
        before = bars[i-12:i-6]
        recent = bars[i-6:i]
        old_volume = sum(b[2] for b in before)
        new_volume = sum(b[2] for b in recent)
        old_trades = sum(b[3] for b in before)
        new_trades = sum(b[3] for b in recent)
        if old_volume <= 0 or old_trades <= 0:
            continue
        notional = price * (old_volume + new_volume)
        if notional < 100_000:
            continue
        returns = [bars[j][1] / bars[j-1][1] - 1 for j in range(i-11, i+1)]
        features = {
            "momentum_5m": price / bars[i-1][1] - 1,
            "momentum_15m": price / bars[i-3][1] - 1,
            "momentum_60m": price / bars[i-12][1] - 1,
            "volume_accel": min(100., new_volume / old_volume),
            "trade_accel": min(100., new_trades / old_trades),
            "volatility_60m": statistics.pstdev(returns),
        }
        if not all(math.isfinite(x) for x in features.values()):
            continue
        yield {"pair": pair, "at": asof, "notional_60m": notional,
               "features": features, "outcomes": outcomes_for_anchor(bars,i,gaps),
               "split": split_for_stamp(stamp), "entry_price": price}


def frozen_asof_universe(market_rows, top_n=MAX_NOTIONAL_CANDIDATES):
    """Select largest recent USD notional WITHOUT consulting forward outcomes."""
    heaps = defaultdict(list)
    for pair, bars in market_rows:
        for row in candidate_rows(pair, bars):
            if row["split"] == "embargo":
                continue
            key = (row["notional_60m"], row["pair"], row)
            heap = heaps[row["at"]]
            if len(heap) < top_n:
                heapq.heappush(heap, key)
            elif (key[0], key[1]) > (heap[0][0], heap[0][1]):
                heapq.heapreplace(heap, key)
    return [r for stamp in sorted(heaps)
            for _, _, r in sorted(heaps[stamp], key=lambda x: (-x[0], x[1]))]


def freeze_challenger(rows):
    """Learn standardized positive-minus-negative feature weights in training only."""
    train = [r for r in rows if r["split"] == "train"
             and r["outcomes"]["48"] is not None]
    positive = [r for r in train if r["outcomes"]["48"] >= .30]
    negative = [r for r in train if r["outcomes"]["48"] < .30]
    state = {"train_complete": len(train), "train_positive": len(positive),
             "train_negative": len(negative), "feature_names": list(FEATURES),
             "promotion_authorized": False, "production_applied": False}
    if len(positive) < 8 or len(negative) < 8:
        state["status"] = "INSUFFICIENT_LABEL_VARIETY"
        return state
    means = {f: sum(r["features"][f] for r in train)/len(train) for f in FEATURES}
    scales = {f: max((sum((r["features"][f]-means[f])**2 for r in train)
                      / len(train))**.5, 1e-8) for f in FEATURES}
    weights = {f: (
        sum((r["features"][f]-means[f])/scales[f] for r in positive)/len(positive)
        - sum((r["features"][f]-means[f])/scales[f] for r in negative)/len(negative)
    ) for f in FEATURES}
    state.update(status="SHADOW_ONLY", means=means, scales=scales, weights=weights)
    return state


def rank_score(row, model):
    return sum((row["features"][f]-model["means"][f]) / model["scales"][f]
               * model["weights"][f] for f in FEATURES)


def compare(rows, model, split):
    """Same preselected hourly universe and one selection per timestamp."""
    universe = defaultdict(list)
    for row in rows:
        if row["split"] == split:
            universe[row["at"]].append(row)
    methods = {
        "baseline_abs_60m": lambda row: abs(row["features"]["momentum_60m"]),
        "shadow_learned": lambda row: rank_score(row, model),
    } if model["status"] == "SHADOW_ONLY" else {
        "baseline_abs_60m": lambda row: abs(row["features"]["momentum_60m"]),
    }
    output = {}
    for name, scorer in methods.items():
        selected = [sorted(candidate, key=lambda r: (-scorer(r), r["pair"]))[0]
                    for _, candidate in sorted(universe.items()) if candidate]
        complete = [r for r in selected if r["outcomes"]["48"] is not None]
        hits = [r for r in complete if r["outcomes"]["48"] >= .30]
        early = [r for r in hits if abs(r["features"]["momentum_60m"]) <= .03]
        outcome_by_horizon = {str(h): {
            "complete": sum(r["outcomes"][str(h)] is not None for r in selected),
            "hits30": sum(r["outcomes"][str(h)] is not None
                          and r["outcomes"][str(h)] >= .30 for r in selected)}
            for h in HORIZONS}
        # Deduplicate repeated same-market positive hourly windows into pair-days.
        pairdays = sorted({(r["pair"], r["at"]//86400) for r in hits})
        output[name] = {
            "timestamps": len(selected), "complete_48h": len(complete),
            "48h_abstentions": len(selected)-len(complete),
            "hits30": len(hits), "misses": len(complete)-len(hits),
            "precision30_on_complete": len(hits)/len(complete) if complete else None,
            "early_hits30": len(early),
            "positive_pairdays": len(pairdays),
            "unique_positive_pairs": len({r["pair"] for r in hits}),
            "outcomes_by_horizon": outcome_by_horizon,
        }
    return output


def run_archive(zip_path):
    file_digest = hashlib.sha256()
    with open(zip_path,"rb") as source:
        for block in iter(lambda: source.read(4 * 1024 * 1024), b""):
            file_digest.update(block)
    counters = {"csv_files": 0, "usd_markets": 0, "valid_5m_bars": 0}
    def streams():
        with zipfile.ZipFile(zip_path) as z:
            members = sorted(n for n in z.namelist() if parse_market(n))
            for name in members:
                pair = parse_market(name)
                bars = []
                with z.open(name) as src:
                    import io
                    for line in csv.reader(io.TextIOWrapper(src,encoding="utf-8")):
                        bar = parse_bar(line)
                        if bar and START-3600 <= bar[0] <= TEST_END+48*3600:
                            bars.append(bar)
                counters["csv_files"] += 1
                if len(bars) >= 12+48*12:
                    counters["usd_markets"] += 1
                    counters["valid_5m_bars"] += len(bars)
                    yield pair, bars
    rows = frozen_asof_universe(streams())
    model = freeze_challenger(rows)
    evaluation = {s: compare(rows, model, s) for s in ("validation","test")}
    result = {
        "schema": "kraken_q3_48h_shadow_v1",
        "source": "https://assets.kraken.com/marketing/institutions/Kraken_OHLCVT_2026Q3.zip",
        "source_zip_sha256": file_digest.hexdigest(),
        "archive_coverage": "2026-07-01 through 2026-09-30",
        "label": "+30% max completed five-minute close within 1/6/24/48h",
        "selection": "top12 USD recent notional 60m at frozen hourly anchor, no outcome filtering",
        "split": {"train_end_exclusive": "2026-08-14", "validation": "Aug18-Aug31",
                  "test": "Sep05-Sep27", "embargo": ">=48h per horizon"},
        "rows_in_asof_universe": len(rows), "data": counters,
        "training": model, "evaluation": evaluation,
        "limitations": [
            "Not the live production baseline, no historic ticker bid/ask spread or fills",
            "Kraken OHLCVT omits no-trade intervals; incomplete 5m histories abstain",
            "Downloaded ZIP SHA is recorded, not independently pinned to published SHA",
            "Hourly anchors are correlated; pair-day metrics reduce duplicate impression",
            "No exchange-event-level entry execution or quote freshness claims",
            "Historical research only; no production promotion or trading",
        ],
        "source_authenticated": False, "promotion_authorized": False,
        "production_applied": False,
    }
    return result


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_path", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    result = run_archive(args.zip_path)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+"\n")
    print(json.dumps({"training": result["training"]["status"],
                      "rows": result["rows_in_asof_universe"],
                      "validation": result["evaluation"]["validation"],
                      "test": result["evaluation"]["test"]},sort_keys=True))
    return result


if __name__ == "__main__":
    main()
