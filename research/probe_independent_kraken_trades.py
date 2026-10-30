"""Bounded read-only Kraken public Trades API probe for source availability.

This is NOT a complete historical trade archive. The public Trades endpoint may
only expose recent trades; do not equate a returned page with a complete 2026Q2
interval. Never use a synthetic completeness flag as proof.
"""
import argparse
import hashlib
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

URL = "https://api.kraken.com/0/public/Trades"
MAX_RESPONSE = 2_000_000
TIMEOUT = 15


def probe(pair="XBTUSD", opener=None):
    if not pair.isalnum() or len(pair) > 24:
        raise ValueError("invalid pair")
    opener = opener or urllib.request.urlopen
    url = URL + "?" + urllib.parse.urlencode({"pair": pair, "count": 1})
    req = urllib.request.Request(url, headers={"Accept-Encoding": "identity",
                                                "User-Agent": "Cryptoscanner-isolated-research/1.0"})
    with opener(req, timeout=TIMEOUT) as response:
        if response.status != 200:
            raise RuntimeError("unexpected HTTP status")
        if response.headers.get("Content-Encoding", "identity").lower() != "identity":
            raise RuntimeError("unexpected response encoding")
        raw = response.read(MAX_RESPONSE + 1)
    if len(raw) > MAX_RESPONSE:
        raise RuntimeError("oversized response")
    payload = json.loads(raw)
    if payload.get("error") or not isinstance(payload.get("result"), dict):
        raise RuntimeError("Kraken API error")
    result = payload["result"]
    keys = [k for k in result if k != "last"]
    if len(keys) != 1 or not isinstance(result[keys[0]], list):
        raise RuntimeError("unexpected Trades result")
    trades = result[keys[0]]
    timestamps = [float(row[2]) for row in trades if isinstance(row, list) and len(row) >= 3]
    return {"status": "recent_public_trade_probe_not_historical_completeness",
            "source_url": url, "requested_pair": pair,
            "returned_pair_key": keys[0], "response_sha256": hashlib.sha256(raw).hexdigest(),
            "observed_trade_count": len(trades), "min_trade_timestamp": min(timestamps) if timestamps else None,
            "max_trade_timestamp": max(timestamps) if timestamps else None,
            "cursor_present": "last" in result,
            "complete_2026q2_interval_verified": False,
            "timestamp_open_verified": False, "historical_labels": 0}


def run(output, pair="XBTUSD"):
    output = Path(output)
    if output.exists():
        raise FileExistsError("refuse overwrite")
    result = probe(pair)
    raw = (json.dumps(result, sort_keys=True) + "\n").encode()
    if len(raw) > 4096:
        raise RuntimeError("oversized evidence")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as dest:
        dest.write(raw)
    return result


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--pair", default="XBTUSD")
    args = ap.parse_args()
    print(json.dumps(run(args.output, args.pair), sort_keys=True))
