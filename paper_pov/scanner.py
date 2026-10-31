"""Public Kraken, paper-only early-mover observations. No credentials or orders."""
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import tempfile
import time
import urllib.parse
import urllib.request

API = "https://api.kraken.com/0/public/"
STABLE = {"USD", "USDT", "USDC", "DAI", "PYUSD", "EURC", "RLUSD", "TUSD",
          "USDD", "FDUSD", "USDE", "FRAX", "GUSD", "BUSD", "ZUSD", "EUR"}
UTC = dt.timezone.utc

def utc(value):
    result = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError("naive timestamp")
    return result.astimezone(UTC)

def finite(value):
    v = float(value)
    if not math.isfinite(v):
        raise ValueError("nonfinite market value")
    return v

def fetch(path):
    request = urllib.request.Request(API + path, headers={
        "User-Agent": "Cryptoscanner-Public-Paper-POV/1.0",
        "Cache-Control": "no-cache"})
    with urllib.request.urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise RuntimeError("Kraken HTTP status not 200")
        payload = json.load(response)
    if not isinstance(payload, dict) or payload.get("error") or not isinstance(payload.get("result"), dict):
        raise ValueError("Kraken response error or invalid schema")
    return payload["result"]

def scan(api=fetch, clock=None, sleep=time.sleep, max_ohlc=24):
    """All timestamps are client-observed; no Kraken ticker exchange timestamp is asserted."""
    clock = clock or (lambda: dt.datetime.now(UTC))
    started = clock().astimezone(UTC)
    pairs = api("AssetPairs")
    eligible = {}
    for key, meta in pairs.items():
        if not isinstance(meta, dict) or meta.get("status") != "online":
            continue
        name = meta.get("wsname", "")
        if not isinstance(name, str) or not name.endswith("/USD"):
            continue
        base = name.split("/")[0].upper()
        if base in STABLE or base.endswith(".S") or base.endswith(".M"):
            continue
        eligible[key] = name
    if len(eligible) < 20:
        raise RuntimeError("Insufficient eligible Kraken USD universe")
    ticker = api("Ticker")
    quote_at = clock().astimezone(UTC)
    if not isinstance(ticker, dict) or not 0 <= (quote_at - started).total_seconds() <= 120:
        raise RuntimeError("Ticker request stale")
    observations = []
    screened = []
    matched = 0
    for pair, name in sorted(eligible.items()):
        t = ticker.get(pair)
        if not isinstance(t, dict):
            continue
        matched += 1
        try:
            price, bid, ask, op, volume = (finite(t["c"][0]), finite(t["b"][0]),
                finite(t["a"][0]), finite(t["o"]), finite(t["v"][1]))
            if min(price, bid, ask, op) <= 0 or ask < bid or volume < 0:
                continue
            # Kraken Ticker 'o' is today's UTC opening price, NOT the
            # rolling 24-hour opening price. Keep ranking arithmetic unchanged
            # while reporting its actual time reference.
            move_since_utc_open = 100 * (price / op - 1)
            spread = 10000 * (ask / bid - 1)
            notional = price * volume
            # Individually finite ticker inputs can overflow in arithmetic.
            # Never emit nonfinite market evidence or fail during JSON sealing.
            if not all(map(math.isfinite, (move_since_utc_open, spread, notional))):
                continue
            observations.append({"pair": pair, "symbol": name, "price": price,
                "spread_bps": round(spread, 4), "notional_24h_usd": round(notional, 2),
                "observed_at": quote_at.isoformat(), "source": "kraken_public_ticker_client_observed"})
            if not (0.25 <= move_since_utc_open <= 12 and spread <= 45 and notional >= 100000):
                continue
            baseline = round(min(45, move_since_utc_open * 7) + min(25, notional / 150000)
                             + max(0, 30 - spread / 2), 4)
            screened.append({"pair": pair, "symbol": name, "price": price,
                "move_since_utc_open_pct": round(move_since_utc_open, 4),
                "move_reference": "kraken_ticker_today_open_utc",
                "spread_bps": round(spread, 4),
                "notional_24h_usd": round(notional, 2), "baseline_score": baseline})
        except (KeyError, ValueError, TypeError, IndexError, ZeroDivisionError):
            continue
    if matched < max(20, math.ceil(len(eligible) * 0.8)):
        raise RuntimeError("Incomplete Kraken ticker universe coverage")
    if len(observations) < max(20, math.ceil(matched * 0.8)):
        raise RuntimeError("Insufficient valid ticker observations")
    screened.sort(key=lambda x: (-x["baseline_score"], x["pair"]))
    selected = []
    seen = set()
    for candidates, limit in ((screened, 12),
        (sorted(screened, key=lambda x: (x["move_since_utc_open_pct"], x["pair"])), 6),
        (sorted(screened, key=lambda x: (x["spread_bps"], x["pair"])), 6)):
        for item in candidates:
            if len(selected) >= max_ohlc:
                break
            if item["pair"] not in seen and limit > 0:
                selected.append(item.copy())
                seen.add(item["pair"])
                limit -= 1
    if not selected:
        raise RuntimeError("No liquid early-stage candidates")
    watch = []
    abstentions = []
    for item in selected:
        try:
            bars = api("OHLC?pair=" + urllib.parse.quote(item["pair"], safe="") + "&interval=5")
            # Kraken's response must identify exactly the requested market.
            # Never accept an unrelated result via first-dictionary-value order.
            if not isinstance(bars, dict) or set(bars) != {item["pair"], "last"}:
                raise ValueError("OHLC response pair mismatch")
            raw = bars[item["pair"]]
            if not isinstance(raw, list) or len(raw) < 14:
                raise ValueError("insufficient completed OHLC")
            closed = raw[:-1][-13:]  # Kraken last candle is not committed
            starts, closes, volumes = [], [], []
            for candle in closed:
                if not isinstance(candle, (list, tuple)) or len(candle) != 8:
                    raise ValueError("invalid OHLC row schema")
                stamp = finite(candle[0])
                if not stamp.is_integer() or int(stamp) % 300:
                    raise ValueError("unaligned OHLC timestamp")
                starts.append(int(stamp))
                opn, high, low, close, vwap, volume = (
                    finite(candle[i]) for i in (1, 2, 3, 4, 5, 6))
                count = finite(candle[7])
                if (min(opn, high, low, close, vwap, volume) <= 0
                        or not count.is_integer() or count <= 0
                        or low > min(opn, close, vwap)
                        or high < max(opn, close, vwap)):
                    raise ValueError("invalid or no-trade OHLC candle")
                closes.append(close)
                volumes.append(volume)
            if any(b - a != 300 for a, b in zip(starts, starts[1:])):
                raise ValueError("OHLC interval gap")
            # A missing/duplicated uncommitted tail must not disguise a
            # partially observed final completed candle.
            tail = raw[-1]
            if (not isinstance(tail, (list, tuple)) or len(tail) != 8
                    or finite(tail[0]) != starts[-1] + 300):
                raise ValueError("missing or invalid uncommitted OHLC tail")
            age = clock().astimezone(UTC).timestamp() - (starts[-1] + 300)
            if not 0 <= age <= 600:
                raise ValueError("stale or future completed OHLC")
            accel = sum(volumes[-6:]) / sum(volumes[-12:-6])
            move15 = 100 * (closes[-1] / closes[-4] - 1)
            if not all(map(math.isfinite, (accel, move15))):
                raise ValueError("nonfinite OHLC derived metric")
            challenger = round(item["baseline_score"] +
                max(-25, min(25, move15 * 5)) +
                max(-15, min(15, (accel - 1) * 10)), 4)
            item.update({"challenger_score": challenger,
                "move15_pct": round(move15, 4), "volume_accel": round(accel, 4),
                "ohlc_last_closed_at": dt.datetime.fromtimestamp(starts[-1] + 300, UTC).isoformat(),
                "ohlc_age_seconds": round(age), "status": "PAPER_WATCH"})
            watch.append(item)
        except (ValueError, TypeError, KeyError, StopIteration, IndexError, ZeroDivisionError) as exc:
            abstentions.append({"pair": item["pair"], "reason": str(exc)[:100]})
        sleep(0.15)
    completed = clock().astimezone(UTC)
    if not 0 <= (completed - quote_at).total_seconds() <= 180:
        raise RuntimeError("Quote observations expired during OHLC screening")
    if not watch:
        raise RuntimeError("No fresh contiguous liquid OHLC candidates")
    watch.sort(key=lambda x: (-x["challenger_score"], x["pair"]))
    watch = watch[:12]
    as_of = completed.isoformat()
    for rank, item in enumerate(watch, 1):
        item["rank"] = rank
        item["as_of"] = as_of
        item["quote_observed_at"] = quote_at.isoformat()
        item["prediction_id"] = hashlib.sha256(
            ("paper-v1|" + as_of + "|" + item["pair"]).encode()).hexdigest()
    return {"schema": 1, "mode": "PAPER_ONLY", "buy_approved": False,
        "source": "Kraken public REST (ticker client-observed; OHLC completed)",
        "started_at": started.isoformat(), "as_of": as_of,
        "ticker_move_reference": "kraken_ticker_today_open_utc",
        "eligible_pairs": len(eligible), "matched_tickers": matched,
        "observed_markets": len(observations), "ohlc_screened": len(selected),
        "watch": watch, "observations": observations, "abstentions": abstentions,
        "forward_labels": 0, "held_out_lift": None, "production_applied": False}

def atomic_json(path, report):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=".paper-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as handle:
            json.dump(report, handle, sort_keys=True, separators=(",", ":"), allow_nan=False)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)

def main():
    report = scan()
    atomic_json(os.getenv("PAPER_REPORT_PATH", "paper_pov/output/latest.json"), report)
    print("PAPER_SCAN " + json.dumps({k: report[k] for k in (
        "as_of", "eligible_pairs", "matched_tickers", "observed_markets",
        "ohlc_screened", "forward_labels", "production_applied")}, sort_keys=True))
    print("PAPER_WATCH " + json.dumps([{"symbol": x["symbol"], "rank": x["rank"],
        "prediction_id": x["prediction_id"], "baseline_score": x["baseline_score"],
        "challenger_score": x["challenger_score"]} for x in report["watch"]]))

if __name__ == "__main__":
    main()
