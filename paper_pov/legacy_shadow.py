"""Read-only independent legacy-INSPIRED momentum/volume Kraken PAPER signals.

Not the original legacy strategy. No baseline/challenger score reuse, trading,
ledger writes, model promotion, or measured predictive-lift claim.
"""
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import re
import time
import urllib.parse

from .scanner import STABLE, atomic_json, fetch

UTC = dt.timezone.utc
SOURCE = re.compile(r"[0-9a-f]{40}\Z")
RUN = re.compile(r"[0-9]+\Z")
CANONICAL = re.compile(r"[A-Z0-9][A-Z0-9._-]*/USD\Z")


def _number(value):
    if isinstance(value, bool):
        raise ValueError("Boolean market evidence")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError("Nonfinite market evidence")
    return result


def _now(clock):
    value = clock()
    if not isinstance(value, dt.datetime) or value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("Untrusted local clock")
    return value.astimezone(UTC)


def _closed_features(payload, pair, now):
    if not isinstance(payload, dict) or set(payload) != {pair, "last"}:
        raise ValueError("OHLC pair identity mismatch")
    raw = payload[pair]
    if not isinstance(raw, list) or len(raw) < 14:
        raise ValueError("Insufficient completed OHLC")
    rows = raw[:-1][-13:]
    starts, closes, volumes = [], [], []
    for candle in rows:
        if not isinstance(candle, (list, tuple)) or len(candle) != 8:
            raise ValueError("Invalid candle schema")
        stamp = _number(candle[0])
        if not stamp.is_integer() or int(stamp) % 300:
            raise ValueError("Unaligned candle")
        opn, high, low, close, vwap, volume = (_number(candle[i]) for i in (1, 2, 3, 4, 5, 6))
        count = _number(candle[7])
        if (min(opn, high, low, close, vwap, volume) <= 0 or not count.is_integer()
                or count <= 0 or low > min(opn, close, vwap)
                or high < max(opn, close, vwap)):
            raise ValueError("Invalid or empty completed candle")
        starts.append(int(stamp))
        closes.append(close)
        volumes.append(volume)
    if any(b - a != 300 for a, b in zip(starts, starts[1:])):
        raise ValueError("OHLC gap or duplicate")
    tail = raw[-1]
    if (not isinstance(tail, (list, tuple)) or len(tail) != 8
            or _number(tail[0]) != starts[-1] + 300):
        raise ValueError("Missing uncommitted candle tail")
    closed_at = dt.datetime.fromtimestamp(starts[-1] + 300, UTC)
    age = (now - closed_at).total_seconds()
    if not 0 <= age <= 600:
        raise ValueError("Stale or future completed candle")
    prior = sum(volumes[-12:-6])
    if prior <= 0:
        raise ValueError("Invalid previous volume")
    accel = sum(volumes[-6:]) / prior
    move15 = 100 * (closes[-1] / closes[-4] - 1)
    if not all(math.isfinite(x) for x in (accel, move15)):
        raise ValueError("Nonfinite candle features")
    return move15, accel, closed_at


def scan(*, api=fetch, clock=None, sleep=time.sleep, max_ohlc=16,
         run_id, source_sha, trigger_paper_run_id):
    """Separate public Kraken acquisition, strategy and GitHub run identity."""
    if (not isinstance(run_id, str) or not RUN.fullmatch(run_id)
            or not isinstance(trigger_paper_run_id, str)
            or not RUN.fullmatch(trigger_paper_run_id) or run_id == trigger_paper_run_id
            or not isinstance(source_sha, str) or not SOURCE.fullmatch(source_sha)):
        raise ValueError("Missing distinct immutable GitHub provenance")
    if type(max_ohlc) is not int or not 1 <= max_ohlc <= 24:
        raise ValueError("Unbounded Kraken requests")
    clock = clock or (lambda: dt.datetime.now(UTC))
    started = _now(clock)
    pairs = api("AssetPairs")
    if not isinstance(pairs, dict):
        raise ValueError("Invalid independent AssetPairs response")
    eligible = {}
    symbols = set()
    for pair, meta in pairs.items():
        if not isinstance(meta, dict) or meta.get("status") != "online":
            continue
        symbol = meta.get("wsname")
        if (not isinstance(symbol, str) or not CANONICAL.fullmatch(symbol)
                or symbol[:-4] in STABLE or symbol[:-4].endswith((".S", ".M"))):
            continue
        if symbol in symbols:
            raise ValueError("Duplicate canonical Kraken identity")
        symbols.add(symbol)
        eligible[pair] = symbol
    if len(eligible) < 20:
        raise ValueError("Insufficient independently eligible USD markets")
    ticker = api("Ticker")
    quote_at = _now(clock)
    if (not isinstance(ticker, dict)
            or not 0 <= (quote_at - started).total_seconds() <= 120):
        raise ValueError("Invalid or stale independent ticker response")
    matched = 0
    valid = 0
    precursors = []
    for pair, symbol in sorted(eligible.items()):
        row = ticker.get(pair)
        if not isinstance(row, dict):
            continue
        matched += 1
        try:
            price, bid, ask, opening, volume = (
                _number(row["c"][0]), _number(row["b"][0]),
                _number(row["a"][0]), _number(row["o"]), _number(row["v"][1]))
            if min(price, bid, ask, opening) <= 0 or ask < bid or volume < 0:
                continue
            spread = 10000 * (ask / bid - 1)
            move = 100 * (price / opening - 1)
            notional = price * volume
            if not all(math.isfinite(v) for v in (spread, move, notional)):
                continue
            valid += 1
            if 0.1 <= move <= 15 and spread <= 50 and notional >= 100000:
                precursors.append({"pair": pair, "symbol": symbol, "price": price,
                                   "move_utc_open": move, "spread": spread,
                                   "notional": notional})
        except (KeyError, TypeError, ValueError, IndexError, ZeroDivisionError, OverflowError):
            continue
    if (matched < max(20, math.ceil(len(eligible) * .8))
            or valid < max(20, math.ceil(matched * .8))):
        raise ValueError("Incomplete independent ticker universe")
    precursors.sort(key=lambda x: (-x["move_utc_open"], x["spread"],
                                   -x["notional"], x["symbol"]))
    picks = []
    rejects = 0
    cutoff = quote_at
    for item in precursors[:max_ohlc]:
        try:
            payload = api("OHLC?pair=" + urllib.parse.quote(item["pair"], safe="") + "&interval=5")
            move15, accel, closed_at = _closed_features(payload, item["pair"], _now(clock))
            if move15 < .05 or accel < 1:
                rejects += 1
                continue
            cutoff = max(cutoff, closed_at)
            # Distinct momentum/volume strategy, NOT current PAPER scoring.
            score = max(0, min(100, 18 + min(25, item["move_utc_open"] * 4)
                     + min(30, move15 * 8) + min(25, (accel - 1) * 15)
                     + min(15, math.log10(max(1, item["notional"] / 100000)) * 8)
                     - min(15, item["spread"] / 4)))
            picks.append({"symbol": item["symbol"], "price_usd": item["price"],
                          "legacy_score": round(score, 4),
                          "move15_pct": round(move15, 4),
                          "volume_accel": round(accel, 4),
                          "quote_observed_at": quote_at.isoformat(),
                          "ohlc_last_closed_at": closed_at.isoformat(),
                          "status": "WATCH_PAPER_ONLY"})
        except (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError, OverflowError):
            rejects += 1
        sleep(.15)
    completed = _now(clock)
    if not 0 <= (completed - quote_at).total_seconds() <= 180:
        raise ValueError("Independent quote expired before completion")
    picks.sort(key=lambda x: (-x["legacy_score"], x["symbol"]))
    picks = picks[:12]
    for rank, item in enumerate(picks, 1):
        item["rank"] = rank
    return {"schema": 1, "mode": "LEGACY_INSPIRED_SHADOW",
            "strategy_name": "independent-early-momentum-volume-v1-not-original",
            "independent_execution": True, "production_applied": False,
            "buy_approved": False, "run_id": run_id,
            "trigger_paper_run_id": trigger_paper_run_id,
            "source_sha": source_sha, "as_of": completed.isoformat(),
            "feature_cutoff_utc": cutoff.isoformat(),
            "ticker_reference": "Kraken today open UTC, not rolling 24h",
            "quote_timestamp_type": "client_observed_not_exchange_event",
            "status": "WATCH_PAPER_ONLY" if picks else "NO_SIGNALS",
            "eligible_usd_pairs": len(eligible), "matched_tickers": matched,
            "valid_tickers": valid, "ohlc_attempts": min(max_ohlc, len(precursors)),
            "ohlc_rejections": rejects, "candidates": picks,
            "held_out_lift": None, "trade_executed": False}


def main():
    report = scan(run_id=os.environ["PAPER_SHADOW_RUN_ID"],
                  source_sha=os.environ["PAPER_SHADOW_SOURCE_SHA"],
                  trigger_paper_run_id=os.environ["PAPER_TRIGGER_RUN_ID"])
    path = Path("paper_pov/output/legacy-shadow.json")
    atomic_json(path, report)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    (path.parent / "LEGACY_SHA256SUMS").write_text(digest + "  legacy-shadow.json\n")
    print("LEGACY_SHADOW " + json.dumps({"run_id": report["run_id"],
          "trigger_paper_run_id": report["trigger_paper_run_id"],
          "as_of": report["as_of"], "status": report["status"],
          "candidate_count": len(report["candidates"]),
          "sha256": digest}, sort_keys=True))
    return report


if __name__ == "__main__":
    main()
