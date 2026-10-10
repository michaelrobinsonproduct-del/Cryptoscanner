"""Incremental Kraken spot 5m OHLC collector. Never claims unavailable deep history.

No trading, database writes, or scheduler. Persist --state and --output in durable
storage before using this as a recurring collection source.
"""
import argparse
import datetime as dt
import hashlib
import json
import math
import pathlib
import urllib.parse
import urllib.request

INTERVAL = 300
SOURCE = "kraken_rest_5m_incremental"
MAX_RESPONSE_BYTES = 5_000_000


def validate_candle(raw):
    if not isinstance(raw, list) or len(raw) < 8:
        raise ValueError("invalid candle shape")
    timestamp = raw[0]
    if isinstance(timestamp, bool) or not isinstance(timestamp, (int, float)):
        raise ValueError("invalid candle timestamp")
    timestamp = int(timestamp)
    if timestamp % INTERVAL:
        raise ValueError("unaligned candle timestamp")
    vals = []
    for value in raw[1:7]:
        if isinstance(value, bool):
            raise ValueError("boolean numeric field")
        try:
            value = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError("non-numeric candle field") from exc
        if not math.isfinite(value):
            raise ValueError("non-finite candle field")
        vals.append(value)
    op, hi, lo, close, vwap, volume = vals
    if min(op, hi, lo, close, vwap) <= 0 or volume < 0:
        raise ValueError("invalid candle price or volume")
    if lo > min(op, close, hi) or hi < max(op, close, lo):
        raise ValueError("inconsistent OHLC envelope")
    count = raw[7]
    if isinstance(count, bool) or not isinstance(count, (int, float)) or count < 0 or int(count) != count:
        raise ValueError("invalid trade count")
    return {"ts": timestamp, "open": op, "high": hi, "low": lo,
            "close": close, "vwap": vwap, "volume": volume, "trades": int(count)}


def fingerprint(candle):
    return hashlib.sha256(json.dumps(candle, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def validate_response(payload, pair, now_ts, previous=None, max_age_seconds=900):
    if not isinstance(payload, dict) or payload.get("error") != []:
        raise ValueError("Kraken API error or invalid payload")
    result = payload.get("result")
    if not isinstance(result, dict):
        raise ValueError("missing result")
    candidates = [v for k, v in result.items() if k != "last" and isinstance(v, list)]
    if len(candidates) != 1:
        raise ValueError("ambiguous pair response")
    # The last Kraken OHLC entry is the current, uncommitted candle.
    raw_rows = candidates[0]
    if len(raw_rows) < 2:
        raise ValueError("insufficient OHLC candles")
    now_ts = int(now_ts)
    if not isinstance(pair, str) or not pair.strip():
        raise ValueError("invalid pair")
    committed = [validate_candle(x) for x in raw_rows[:-1]]
    if not committed:
        raise ValueError("no committed candles")
    if any(c["ts"] + INTERVAL > now_ts - 30 for c in committed):
        raise ValueError("uncommitted or future candle in committed segment")
    for earlier, later in zip(committed, committed[1:]):
        if later["ts"] - earlier["ts"] != INTERVAL:
            raise ValueError("gap, duplicate, or out-of-order OHLC candle")
    newest = committed[-1]
    if now_ts - (newest["ts"] + INTERVAL) > max_age_seconds:
        raise ValueError("stale source")
    previous = previous or {}
    if previous and (previous.get("pair") != pair or previous.get("source") != SOURCE):
        raise ValueError("checkpoint identity mismatch")
    checkpoint = previous.get("last_committed_ts")
    if checkpoint is not None:
        if not isinstance(checkpoint, int) or isinstance(checkpoint, bool):
            raise ValueError("invalid checkpoint")
        if committed[0]["ts"] > checkpoint:
            raise ValueError("unrecoverable gap: OHLC API only supplies recent bars")
        overlap = next((c for c in committed if c["ts"] == checkpoint), None)
        if overlap is None or fingerprint(overlap) != previous.get("last_candle_sha256"):
            raise ValueError("checkpoint overlap absent or changed")
        new_rows = [c for c in committed if c["ts"] > checkpoint]
        if new_rows and new_rows[0]["ts"] != checkpoint + INTERVAL:
            raise ValueError("incremental gap")
    else:
        new_rows = committed
    state = {"source": SOURCE, "pair": pair, "last_committed_ts": newest["ts"],
             "last_candle_sha256": fingerprint(newest),
             "coverage_start_ts": previous.get("coverage_start_ts", committed[0]["ts"]),
             "deep_history_complete": False, "historical_gap_before_start": True,
             "validated_at": dt.datetime.fromtimestamp(now_ts, dt.timezone.utc).isoformat()}
    return new_rows, state


def fetch_kraken(pair, checkpoint=None):
    args = {"pair": pair, "interval": "5"}
    if checkpoint is not None:
        args["since"] = str(max(0, checkpoint - INTERVAL))
    url = "https://api.kraken.com/0/public/OHLC?" + urllib.parse.urlencode(args)
    request = urllib.request.Request(url, headers={"User-Agent": "KrakenRollingResearch/1.0", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(request, timeout=20) as response:
        raw = response.read(MAX_RESPONSE_BYTES + 1)
    if len(raw) > MAX_RESPONSE_BYTES:
        raise ValueError("oversized Kraken response")
    return json.loads(raw)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pair", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    state_path = pathlib.Path(args.state)
    previous = json.loads(state_path.read_text()) if state_path.exists() else None
    payload = fetch_kraken(args.pair, previous.get("last_committed_ts") if previous else None)
    now = int(dt.datetime.now(dt.timezone.utc).timestamp())
    rows, state = validate_response(payload, args.pair, now, previous)
    # Never advance a checkpoint unless the validated output was written.
    out = pathlib.Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps({"pair": args.pair, "source": SOURCE, **row}, separators=(",", ":")) + "\n")
        handle.flush()
    state_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = state_path.with_suffix(state_path.suffix + ".tmp")
    tmp.write_text(json.dumps(state, sort_keys=True) + "\n")
    tmp.replace(state_path)
    print(json.dumps({"pair": args.pair, "new_committed_candles": len(rows),
                      "latest": state["last_committed_ts"],
                      "deep_history_complete": False}))


if __name__ == "__main__":
    main()
