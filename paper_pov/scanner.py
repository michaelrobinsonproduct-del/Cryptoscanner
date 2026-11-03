"""Public Kraken, paper-only early-mover observations. No credentials or orders."""
import datetime as dt
import fcntl
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
# Explicit fiat-pegged exclusions. Kraken's supported-stablecoins list includes
# non-USD pegs (notably BRL1); do not filter by the token's USD price.
# https://support.kraken.com/in/articles/stablecoins-supported-on-kraken
STABLE = {"USD", "USDT", "USDC", "DAI", "PYUSD", "EURC", "RLUSD", "TUSD",
          "USDD", "FDUSD", "USDE", "FRAX", "GUSD", "BUSD", "ZUSD", "EUR",
          "BRL1", "QCAD", "USDG", "USDQ", "USDS", "USDR", "USD1",
          "EURQ", "EURR", "EUROP", "EURT", "TGBP"}
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

def watch_contract(item, quote_at, completed):
    """Conservative, deterministic paper WATCH evidence; never implies exchange tick age."""
    age = (completed - quote_at).total_seconds()
    if not 0 <= age <= 600:
        raise ValueError("client-observed ticker quote outside 10-minute freshness window")
    spread = finite(item["spread_bps"])
    accel = finite(item["volume_accel"])
    move15 = finite(item["move15_pct"])
    if spread < 0 or accel <= 0:
        raise ValueError("invalid WATCH liquidity metrics")
    risk = "HIGH" if spread > 30 or accel < 0.8 or abs(move15) > 8 else "ELEVATED"
    return {
        "status": "PAPER_WATCH", "risk": risk,
        "quote_age_seconds": round(age),
        "quote_timestamp_semantics": "client_observed_not_exchange_event_time",
        "volume_acceleration_reference": "last_30m_over_prior_30m",
        "momentum_reference": "completed_5m_candles_15m",
        "buy_approved": False,
    }

def scan(api=fetch, clock=None, sleep=time.sleep, max_ohlc=24):
    """All timestamps are client-observed; no Kraken ticker exchange timestamp is asserted."""
    clock = clock or (lambda: dt.datetime.now(UTC))
    started = clock().astimezone(UTC)
    pairs = api("AssetPairs")
    eligible = {}
    online_usd_pairs = 0
    excluded_stablecoin_pairs = 0
    excluded_other_pairs = 0
    for key, meta in pairs.items():
        if not isinstance(meta, dict) or meta.get("status") != "online":
            continue
        name = meta.get("wsname", "")
        if not isinstance(name, str) or not name.endswith("/USD"):
            continue
        online_usd_pairs += 1
        base = name.split("/")[0].upper()
        if base in STABLE:
            excluded_stablecoin_pairs += 1
            continue
        if base.endswith(".S") or base.endswith(".M"):
            excluded_other_pairs += 1
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
    screening_rejections = {"below_early_move": 0, "above_early_move": 0,
                            "wide_spread": 0, "low_notional": 0}
    matched = 0
    ticker_rejections = {"missing_or_invalid_payload": 0, "invalid_price_or_volume": 0,
                         "nonfinite_derived_metric": 0}
    for pair, name in sorted(eligible.items()):
        t = ticker.get(pair)
        if not isinstance(t, dict):
            ticker_rejections["missing_or_invalid_payload"] += 1
            continue
        matched += 1
        try:
            price, bid, ask, op, volume = (finite(t["c"][0]), finite(t["b"][0]),
                finite(t["a"][0]), finite(t["o"]), finite(t["v"][1]))
            if min(price, bid, ask, op) <= 0 or ask < bid or volume < 0:
                ticker_rejections["invalid_price_or_volume"] += 1
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
                ticker_rejections["nonfinite_derived_metric"] += 1
                continue
            observations.append({"pair": pair, "symbol": name, "price": price,
                "spread_bps": round(spread, 4), "notional_24h_usd": round(notional, 2),
                "observed_at": quote_at.isoformat(), "source": "kraken_public_ticker_client_observed"})
            # Count every failed screen independently; one market can fail several.
            failed = False
            for rejected, condition in (
                ("below_early_move", move_since_utc_open < 0.25),
                ("above_early_move", move_since_utc_open > 12),
                ("wide_spread", spread > 45),
                ("low_notional", notional < 100000),
            ):
                if condition:
                    screening_rejections[rejected] += 1
                    failed = True
            if failed:
                continue
            baseline = round(min(45, move_since_utc_open * 7) + min(25, notional / 150000)
                             + max(0, 30 - spread / 2), 4)
            screened.append({"pair": pair, "symbol": name, "price": price,
                "move_since_utc_open_pct": round(move_since_utc_open, 4),
                "move_reference": "kraken_ticker_today_open_utc",
                "spread_bps": round(spread, 4),
                "notional_24h_usd": round(notional, 2), "baseline_score": baseline})
        except (KeyError, ValueError, TypeError, IndexError, ZeroDivisionError):
            ticker_rejections["missing_or_invalid_payload"] += 1
            continue
    if len(observations) + sum(ticker_rejections.values()) != len(eligible):
        raise RuntimeError("Ticker coverage accounting mismatch")
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
    watch = []
    abstentions = []
    abstention_counts = {"request_failure": 0, "stale_or_future_ohlc": 0,
                         "ohlc_gap_or_schema": 0, "invalid_market_metrics": 0}
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
            prior_volume = sum(volumes[-12:-6])
            if prior_volume <= 0:
                raise ValueError("invalid or no-trade OHLC prior volume")
            accel = sum(volumes[-6:]) / prior_volume
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
        except (ValueError, TypeError, KeyError, StopIteration, IndexError, ZeroDivisionError,
                OSError, TimeoutError, RuntimeError) as exc:
            # A failed Kraken OHLC request abstains this market rather than
            # discarding other independently validated candidates.
            reason = str(exc)[:100]
            if isinstance(exc, (OSError, TimeoutError, RuntimeError)):
                category = "request_failure"
            elif "stale or future completed OHLC" in reason:
                category = "stale_or_future_ohlc"
            elif any(term in reason for term in ("OHLC", "candle", "tail", "interval", "timestamp")):
                category = "ohlc_gap_or_schema"
            else:
                category = "invalid_market_metrics"
            abstention_counts[category] += 1
            abstentions.append({"pair": item["pair"], "category": category, "reason": reason})
        sleep(0.15)
    completed = clock().astimezone(UTC)
    if not 0 <= (completed - quote_at).total_seconds() <= 180:
        raise RuntimeError("Quote observations expired during OHLC screening")
    # A valid scan may have no qualified market: preserve its coverage and abstentions.
    # This is a successful paper observation, never a BUY or an invented WATCH.
    watch.sort(key=lambda x: (-x["challenger_score"], x["pair"]))
    watch = watch[:12]
    as_of = completed.isoformat()
    for rank, item in enumerate(watch, 1):
        item.update(watch_contract(item, quote_at, completed))
        item["rank"] = rank
        item["as_of"] = as_of
        item["quote_observed_at"] = quote_at.isoformat()
        item["prediction_id"] = hashlib.sha256(
            ("paper-v1|" + as_of + "|" + item["pair"]).encode()).hexdigest()
    return {"schema": 1, "mode": "PAPER_ONLY", "buy_approved": False,
        "scan_status": ("WATCH" if watch else
                        "ABSTAIN_NO_LIQUID_CANDIDATES" if not selected else
                        "ABSTAIN_NO_QUALIFIED_OHLC"),
        "source": "Kraken public REST (ticker client-observed; OHLC completed)",
        "started_at": started.isoformat(), "as_of": as_of,
        "ticker_move_reference": "kraken_ticker_today_open_utc",
        "eligible_pairs": len(eligible), "online_usd_pairs": online_usd_pairs,
        "excluded_stablecoin_pairs": excluded_stablecoin_pairs,
        "excluded_other_pairs": excluded_other_pairs, "matched_tickers": matched,
        "observed_markets": len(observations), "ticker_rejections": ticker_rejections,
        "screening_rejections": screening_rejections,
        "screened_markets": len(screened),
        "ohlc_screened": len(selected),
        "watch": watch, "observations": observations, "abstentions": abstentions,
        "abstention_counts": abstention_counts,
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

def persist_report(latest_path, report):
    """Serialize local paper receipt commits; never regress latest or delete another writer's file."""
    latest_path = Path(latest_path)
    stamp = utc(report["as_of"])
    payload = json.dumps(report, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    latest_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_dir = latest_path.parent / "receipts"
    receipt_dir.mkdir(parents=True, exist_ok=True)
    receipt = receipt_dir / (stamp.strftime("%Y%m%dT%H%M%S%fZ") + ".json")
    # Advisory lock is held across receipt creation, readback and latest update.
    # Separate lock inode is stable even as latest.json is atomically replaced.
    lock_path = latest_path.parent / ".paper-receipt.lock"
    with open(lock_path, "a+b") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        if latest_path.exists():
            current = json.loads(latest_path.read_text())
            current_stamp = utc(current["as_of"])
            if current_stamp > stamp:
                raise ValueError("out-of-order scan cannot replace newer latest")
            if current_stamp == stamp:
                # A retried job must not create another receipt or rewrite latest.
                # Same timestamp with different bytes is a conflict, not a replay.
                if latest_path.read_bytes() != payload or not receipt.exists():
                    raise ValueError("conflicting or incomplete same-timestamp scan replay")
                if receipt.read_bytes() != payload:
                    raise ValueError("same-timestamp receipt readback mismatch")
                return receipt
        fd = os.open(receipt, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        identity = os.fstat(fd)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            if receipt.read_bytes() != payload:
                raise IOError("scan receipt readback mismatch")
            atomic_json(latest_path, report)
            if latest_path.read_bytes() != payload:
                raise IOError("latest report readback mismatch")
        except BaseException:
            # Never unlink a receipt that another process has replaced.
            try:
                actual = receipt.stat()
                if (actual.st_dev, actual.st_ino) == (identity.st_dev, identity.st_ino):
                    receipt.unlink()
            except FileNotFoundError:
                pass
            raise
    return receipt

def main():
    report = scan()
    receipt = persist_report(os.getenv("PAPER_REPORT_PATH", "paper_pov/output/latest.json"), report)
    print("PAPER_RECEIPT " + str(receipt))
    print("PAPER_SCAN " + json.dumps({k: report[k] for k in (
        "as_of", "scan_status", "online_usd_pairs", "excluded_stablecoin_pairs",
        "excluded_other_pairs", "eligible_pairs", "matched_tickers",
        "observed_markets", "ticker_rejections", "screening_rejections",
        "screened_markets", "ohlc_screened", "abstention_counts", "forward_labels", "production_applied")}, sort_keys=True))
    print("PAPER_WATCH " + json.dumps([{"symbol": x["symbol"], "rank": x["rank"],
        "prediction_id": x["prediction_id"], "baseline_score": x["baseline_score"],
        "challenger_score": x["challenger_score"], "price": x["price"],
        "quote_observed_at": x["quote_observed_at"],
        "quote_timestamp_semantics": x["quote_timestamp_semantics"],
        "ohlc_last_closed_at": x["ohlc_last_closed_at"],
        "move15_pct": x["move15_pct"], "volume_accel": x["volume_accel"],
        "spread_bps": x["spread_bps"], "notional_24h_usd": x["notional_24h_usd"],
        "status": x["status"], "risk": x["risk"], "buy_approved": x["buy_approved"]} for x in report["watch"]]))

if __name__ == "__main__":
    main()
