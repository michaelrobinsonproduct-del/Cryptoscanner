"""Bounded OFFLINE validation of captured Kraken trade evidence for gap recovery.

This is not a downloader, exchange-signed proof, continuous quote reconstruction,
tradeable fill, or ledger writer. Captured source bytes MUST be independently
acquired from Kraken HTTPS and SHA-bound before use. Never use June 2026 archive
for November 2026 timestamps.
"""
import datetime as dt
from decimal import Decimal, InvalidOperation
import hashlib
import json

from paper_pov.learning_outcomes import _aware

UTC = dt.timezone.utc
REVISION = "kraken-public-trades-v1"
SOURCE_URL = "https://api.kraken.com/0/public/Trades"
MAX_TRADES = 1000
MAX_RAW_BYTES = 256000


def canonical(payload):
    return json.dumps(payload, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode("utf-8")


def _positive(value):
    if not isinstance(value, str):
        raise ValueError("Trade values require exact decimal strings")
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError("Invalid trade decimal") from exc
    if not result.is_finite() or result <= 0:
        raise ValueError("Nonpositive or nonfinite trade decimal")
    return result


def verify_captured_bucket(source, expected_pair, bucket_start, evaluation_at):
    """Return independent recovered trade prints, never synthetic OHLC quotes.

    Require all reported OHLC trades in this five-minute interval, identical
    open/high/low/close/volume, exact source hash, monotonic event timestamps,
    unique trade IDs and a closed bucket known before evaluation time.
    """
    if not isinstance(source, dict) or not isinstance(expected_pair, str) or not expected_pair:
        raise ValueError("Invalid recovery request")
    if source.get("revision") != REVISION or source.get("source_url") != SOURCE_URL:
        raise ValueError("Unknown Kraken source revision or endpoint")
    raw = source.get("raw_response")
    if not isinstance(raw, dict):
        raise ValueError("Missing captured source")
    data = canonical(raw)
    if len(data) > MAX_RAW_BYTES or hashlib.sha256(data).hexdigest() != source.get("raw_sha256"):
        raise ValueError("Unverified captured source checksum/size")
    start = _aware(bucket_start)
    now = _aware(evaluation_at)
    if start.second or start.microsecond or start.minute % 5:
        raise ValueError("Nonaligned UTC candle")
    end = start + dt.timedelta(minutes=5)
    retrieved = _aware(source["retrieved_at"])
    if retrieved < end or retrieved > now:
        raise ValueError("Incomplete or future captured source")
    if raw.get("pair") != expected_pair:
        raise ValueError("Kraken pair identity mismatch")
    candle = raw.get("candle")
    trades = raw.get("trades")
    if (not isinstance(candle, list) or len(candle) != 8
            or not isinstance(trades, list) or not 1 <= len(trades) <= MAX_TRADES):
        raise ValueError("Invalid bounded candle/trade rows")
    if int(start.timestamp()) != candle[0] or type(candle[7]) is not int or candle[7] != len(trades):
        raise ValueError("Incomplete trade count or wrong candle timestamp")
    seen = set()
    prices = []
    volumes = []
    observations = []
    previous = None
    for trade in trades:
        if not isinstance(trade, dict) or set(trade) != {"id", "at", "price", "volume"}:
            raise ValueError("Untrusted trade row schema")
        tid = trade["id"]
        if not isinstance(tid, str) or not tid or tid in seen:
            raise ValueError("Missing or duplicate trade ID")
        seen.add(tid)
        at = _aware(trade["at"])
        if not start <= at < end or at > retrieved or (previous is not None and at < previous):
            raise ValueError("Out-of-bucket, future or nonmonotonic trade")
        previous = at
        price = _positive(trade["price"])
        volume = _positive(trade["volume"])
        prices.append(price)
        volumes.append(volume)
        observations.append({"pair": expected_pair, "trade_id": tid,
                             "source_at_utc": at.isoformat(),
                             "price": str(price), "volume": str(volume)})
    op, high, low, close, vwap, vol = (_positive(candle[i]) for i in (1, 2, 3, 4, 5, 6))
    if (prices[0] != op or max(prices) != high or min(prices) != low
            or prices[-1] != close or sum(volumes) != vol
            or sum(p * v for p, v in zip(prices, volumes)) / vol != vwap):
        raise ValueError("Trades do not exactly reconstruct OHLC")
    return {
        "scope": "INDEPENDENT_CAPTURED_TRADE_PRINTS_ONLY",
        "source_revision": REVISION,
        "source_url": SOURCE_URL,
        "source_sha256": source["raw_sha256"],
        "retrieved_at_utc": retrieved.isoformat(),
        "bucket_start_utc": start.isoformat(),
        "bucket_end_utc": end.isoformat(),
        "pair": expected_pair,
        "trade_count": len(observations),
        "observations": observations,
        "complete_only_for_one_verified_bucket": True,
        "exchange_signed": False,
        "ledger_modified": False,
        "score_promoted": False
    }
