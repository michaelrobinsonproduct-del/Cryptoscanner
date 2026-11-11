"""Bounded, one-shot prospective Kraken evidence; never historical labels or trading."""
import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
import os
from pathlib import Path
import re
import ssl
import tempfile
import time
from urllib.request import Request, urlopen

HOST = "https://api.kraken.com"
MAX_BODY = 1_000_000
MAX_LATENCY = 10.0
MAX_EVENT_AGE = 600.0


def _num(x, positive=False):
    try:
        v = Decimal(str(x))
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("invalid source number") from None
    if not v.is_finite() or (positive and v <= 0):
        raise ValueError("invalid source number")
    return v


def _response(path):
    if not path.startswith("/0/public/") or "?" not in path:
        raise ValueError("invalid source endpoint")
    req = Request(HOST + path, headers={"User-Agent": "cryptoscanner-research-provenance/1.0",
                                        "Accept": "application/json"})
    with urlopen(req, timeout=10, context=ssl.create_default_context()) as resp:
        if resp.geturl() != HOST + path or resp.status != 200:
            raise ValueError("source redirect/status")
        raw = resp.read(MAX_BODY + 1)
    if len(raw) > MAX_BODY:
        raise ValueError("oversized source response")
    return raw


def _timed(path, transport, clock):
    before = float(clock())
    raw = transport(path)
    after = float(clock())
    if after < before or after - before > MAX_LATENCY:
        raise ValueError("untrusted receipt clock or excessive latency")
    if not isinstance(raw, bytes) or len(raw) > MAX_BODY:
        raise ValueError("invalid raw source")
    doc = json.loads(raw)
    if not isinstance(doc, dict) or doc.get("error") != [] or not isinstance(doc.get("result"), dict):
        raise ValueError("Kraken API error or malformed result")
    return doc["result"], {"url": HOST + path, "sha256": hashlib.sha256(raw).hexdigest(),
                           "request_started_at": before, "first_observed_at": after,
                           "receipt_latency_seconds": after - before}


def _market(result, trades=False):
    keys = [k for k in result if k != "last"]
    if len(keys) != 1 or not isinstance(result[keys[0]], list if trades else dict):
        raise ValueError("ambiguous Kraken market")
    if trades and "last" not in result:
        raise ValueError("missing trade cursor")
    return keys[0], result[keys[0]]


def _age(event, observed):
    age = float(_num(observed) - _num(event))
    if age < -2:
        raise ValueError("future event timestamp")
    return age


def capture(pair="XBTUSD", *, transport=_response, clock=time.time):
    if not isinstance(pair, str) or not re.fullmatch(r"[A-Z0-9]{3,12}", pair):
        raise ValueError("invalid pair")
    depth, d = _timed(f"/0/public/Depth?pair={pair}&count=2", transport, clock)
    trades, t = _timed(f"/0/public/Trades?pair={pair}&count=100", transport, clock)
    dk, book = _market(depth)
    tk, rows = _market(trades, trades=True)
    if dk != tk or not rows:
        raise ValueError("market mismatch or no trades")
    try:
        bid, ask = book["bids"][0], book["asks"][0]
    except (KeyError, IndexError, TypeError):
        raise ValueError("missing top of book") from None
    if len(bid) < 3 or len(ask) < 3:
        raise ValueError("book lacks exchange level timestamps")
    bp, bv, bt = _num(bid[0], True), _num(bid[1], True), _num(bid[2], True)
    ap, av, at = _num(ask[0], True), _num(ask[1], True), _num(ask[2], True)
    if ap < bp:
        raise ValueError("crossed book")
    if any(not isinstance(row, list) or len(row) < 3 for row in rows):
        raise ValueError("invalid trade row")
    newest = max(_num(row[2], True) for row in rows)
    ba, aa, ta = _age(bt, d["first_observed_at"]), _age(at, d["first_observed_at"]), _age(newest, t["first_observed_at"])
    qfresh = 0 <= ba <= MAX_EVENT_AGE and 0 <= aa <= MAX_EVENT_AGE
    tfresh = 0 <= ta <= MAX_EVENT_AGE
    return {
        "schema": 1, "pair_requested": pair, "pair_source": dk,
        "capture_mode": "PROSPECTIVE_TLS_KRAKEN_PUBLIC_GET",
        "source_authentication_limit": "HTTPS endpoint and response SHA256; Kraken public responses are not exchange-signed",
        "historical_first_observed_recovered": False,
        "depth_receipt": d, "trades_receipt": t,
        "best_bid": str(bp), "best_ask": str(ap),
        "bid_size": str(bv), "ask_size": str(av),
        "spread": str(ap - bp), "spread_bps": str((ap - bp) * 10000 / ((ap + bp) / 2)),
        "bid_level_event_at": str(bt), "ask_level_event_at": str(at),
        "newest_trade_event_at": str(newest),
        "bid_level_age_seconds": ba, "ask_level_age_seconds": aa, "newest_trade_age_seconds": ta,
        "quote_event_fresh_le600s": qfresh, "trade_event_fresh_le600s": tfresh,
        "eligible_point_in_time_snapshot": qfresh and tfresh,
        "authenticated_first_entry_episodes": 0,
        "held_out_lift": None, "production_applied": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pair", default="XBTUSD")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = capture(args.pair)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".kraken-provenance-", dir=output.parent)
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(result, f, sort_keys=True, indent=2)
            f.write("\n")
        os.replace(tmp, output)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    print("KRAKEN_PROSPECTIVE_CAPTURE", result["pair_source"],
          "snapshot_eligible", result["eligible_point_in_time_snapshot"],
          "historical_episodes", 0)


if __name__ == "__main__":
    main()
