"""Fetch observed Kraken 5-minute OHLC candles for paper outcome reconstruction.

Public REST OHLC is limited to recent candles. No missing intervals are filled.
This module never claims independently authenticated archive provenance.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

def fetch_kraken_ohlc(pair, *, interval=5):
    if interval != 5:
        raise ValueError("Only exact 5-minute outcome candles are supported")
    query = urlencode({"pair": pair, "interval": interval})
    url = "https://api.kraken.com/0/public/OHLC?" + query
    with urlopen(url, timeout=25) as response:
        raw = response.read()
    data = json.loads(raw)
    if data.get("error"):
        raise ValueError("Kraken OHLC error: " + repr(data["error"]))
    result = data["result"]
    keys = [k for k in result if k != "last"]
    if len(keys) != 1:
        raise ValueError("Ambiguous Kraken pair alias")
    key = keys[0]
    rows = []
    for candle in result[key]:
        epoch = int(candle[0])
        rows.append({"pair": pair, "timestamp_utc": datetime.fromtimestamp(
            epoch, tz=timezone.utc).isoformat(), "close": float(candle[4]),
            "high": float(candle[2]), "volume": float(candle[6])})
    # Kraken's last row is a live, uncommitted interval, not an outcome.
    rows = rows[:-1]
    return {"pair": pair, "kraken_pair_key": key,
            "source": "kraken_public_ohlc_rest",
            "response_sha256": hashlib.sha256(raw).hexdigest(),
            "candles": rows, "source_authenticated": False}

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("pairs_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    pairs = json.loads(args.pairs_json.read_text())
    if not isinstance(pairs, list) or len(pairs) > 30:
        raise ValueError("Expected at most 30 pairs")
    results = [fetch_kraken_ohlc(pair) for pair in sorted(set(pairs))]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"schema": "kraken_ohlc_observations_v1",
                                        "results": results, "source_authenticated": False},
                                       sort_keys=True, indent=2) + "\n")
    print(json.dumps({"pairs": len(results), "candles": sum(len(x["candles"]) for x in results)}))
    return results

if __name__ == "__main__":
    main()
