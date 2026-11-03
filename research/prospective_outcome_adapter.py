"""E1 adapter: verify retained prospective batch receipts before outcome eligibility.

No backdating a snapshot to a five-minute grid; observation time is factual.
"""
import hashlib
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path

from research.source_qualified_outcomes import qualify


def _entry_ask_liquidity(raw, market, expected_ask, expected_bid=None, expected_ask_event=None, expected_bid_event=None):
    """Executable USD notional at first ask level, from SHA-verified raw depth.

    Only USD-quoted pairs qualify; other quote currencies require FX evidence.
    """
    doc = json.loads(raw)
    book = doc.get("result", {}).get(market)
    if not isinstance(book, dict):
        return None
    asks = book.get("asks")
    bids = book.get("bids")
    if not isinstance(bids, list) or not bids or len(bids[0]) < 3:
        raise ValueError("missing executable bid depth")
    if not isinstance(asks, list) or not asks or len(asks[0]) < 2:
        raise ValueError("missing executable ask depth")
    try:
        price, size = Decimal(str(asks[0][0])), Decimal(str(asks[0][1]))
        expected = Decimal(str(expected_ask))
        bid_price = Decimal(str(bids[0][0]))
        bid_time = Decimal(str(bids[0][2]))
        ask_time = Decimal(str(asks[0][2]))
    except (InvalidOperation, ValueError, TypeError, IndexError):
        raise ValueError("invalid executable ask depth") from None
    if not (bid_price.is_finite() and bid_time.is_finite() and ask_time.is_finite() and
            price.is_finite() and size.is_finite() and
            price > 0 and size > 0 and price == expected):
        raise ValueError("depth/evidence ask mismatch")
    if expected_bid is not None and bid_price != Decimal(str(expected_bid)):
        raise ValueError("depth/evidence bid mismatch")
    if expected_bid_event is not None and bid_time != Decimal(str(expected_bid_event)):
        raise ValueError("depth/evidence bid timestamp mismatch")
    if expected_ask_event is not None and ask_time != Decimal(str(expected_ask_event)):
        raise ValueError("depth/evidence ask timestamp mismatch")
    return price * size


def verified_rows(batch_directory):
    root = Path(batch_directory)
    manifest = json.loads((root / "manifest.json").read_bytes())
    if manifest.get("mode") != "ONE_SHOT_PROSPECTIVE_PUBLIC_TLS_RESEARCH_ONLY":
        raise ValueError("unsupported manifest")
    entries = manifest.get("entries")
    if not isinstance(entries, list) or len(entries) != manifest.get("pairs_requested"):
        raise ValueError("manifest coverage mismatch")
    if len({e.get("pair") for e in entries}) != len(entries):
        raise ValueError("duplicate pair")
    rows, abstentions = [], []
    for entry in entries:
        pair = entry["pair"]
        if entry["status"] != "ELIGIBLE":
            abstentions.append({"pair": pair, "reason": "NO_ELIGIBLE_SNAPSHOT"})
            continue
        receipts = entry["raw"]
        if len(receipts) != 2 or {r["stage"] for r in receipts} != {"depth", "trades"}:
            raise ValueError("incomplete source receipts")
        for receipt in receipts:
            filename = receipt["file"]
            if Path(filename).name != filename or "/" in filename or "\\" in filename:
                raise ValueError("unsafe receipt path")
            raw = (root / filename).read_bytes()
            if len(raw) != receipt["bytes"] or hashlib.sha256(raw).hexdigest() != receipt["sha256"]:
                raise ValueError("raw receipt mismatch")
        evidence_file = entry["evidence_file"]
        if Path(evidence_file).name != evidence_file:
            raise ValueError("unsafe evidence path")
        evidence = json.loads((root / evidence_file).read_bytes())
        if (evidence.get("pair_requested") != pair or
                evidence.get("pair_source") != entry["source_market"] or
                not evidence.get("eligible_point_in_time_snapshot")):
            raise ValueError("source identity mismatch")
        depth = next(r for r in receipts if r["stage"] == "depth")
        trades = next(r for r in receipts if r["stage"] == "trades")
        if (evidence["depth_receipt"]["sha256"] != depth["sha256"] or
                evidence["trades_receipt"]["sha256"] != trades["sha256"]):
            raise ValueError("evidence receipt mismatch")
        observed = evidence["depth_receipt"]["first_observed_at"]
        bid_event = float(evidence["bid_level_event_at"])
        ask_event = float(evidence["ask_level_event_at"])
        if not (0 <= observed - bid_event <= 600 and 0 <= observed - ask_event <= 600):
            raise ValueError("stale quote")
        try:
            bid = Decimal(str(evidence["best_bid"]))
            ask = Decimal(str(evidence["best_ask"]))
            trade_observed = float(evidence["trades_receipt"]["first_observed_at"])
            trade_event = float(evidence["newest_trade_event_at"])
        except (KeyError, TypeError, ValueError, InvalidOperation):
            raise ValueError("invalid market evidence") from None
        if not (bid.is_finite() and ask.is_finite() and 0 < bid <= ask):
            raise ValueError("crossed or invalid market book")
        if not (0 <= trade_observed - trade_event <= 600):
            raise ValueError("stale trade evidence")
        depth_raw = (root / depth["file"]).read_bytes()
        liquidity = _entry_ask_liquidity(depth_raw, entry["source_market"], evidence["best_ask"],
                                          evidence["best_bid"], ask_event, bid_event)
        if liquidity is not None and not pair.endswith("USD"):
            liquidity = None  # No quote-to-USD FX conversion is available.
        rows.append({"pair": pair, "event_at": bid_event,
                     "first_observed_at": observed,
                     "source_sha256": depth["sha256"],
                     "bid": evidence["best_bid"], "ask": evidence["best_ask"],
                     "ask_event_at": ask_event,
                     "trade_source_sha256": trades["sha256"],
                     "entry_liquidity_usd": float(liquidity) if liquidity is not None else None})
    return rows, abstentions


def coverage(batch_directory, horizon_hours=1):
    rows, abstentions = verified_rows(batch_directory)
    # One-shot batches do not provide contiguous future intervals. Never
    # manufacture missing timestamps or treat a single quote as an episode.
    results = [qualify(row, [], horizon_hours) for row in rows]
    return {"snapshots_verified": len(rows),
            "abstentions": abstentions,
            "qualified_first_entry_episodes": sum(
                r["status"] == "QUALIFIED_OBSERVED_PATH" for r in results),
            "outcome_statuses": [r["status"] for r in results],
            "held_out_lift": None, "production_applied": False}
