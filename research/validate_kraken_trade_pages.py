"""Fail-closed independent Kraken Trades REST page provenance validation.

Kraken Trades REST provides a bounded page, not proof of interval completeness
without a continuous cursor traversal from before to after the target interval.
This module validates local pages only; no network or production access.
"""
from math import isfinite

STEP = 300


def validate_trade_pages(pages, *, start, end, source="kraken_public_trades",
                         complete_cursor_chain=False, started_before_interval=False,
                         ended_after_interval=False):
    if (source != "kraken_public_trades" or complete_cursor_chain is not True or
            started_before_interval is not True or ended_after_interval is not True):
        return {"status": "unverified_complete_trade_interval", "trades": []}
    if type(start) is not int or type(end) is not int or start < 0 or start % STEP or end != start + STEP:
        return {"status": "invalid_interval", "trades": []}
    if not isinstance(pages, (list, tuple)) or not 1 <= len(pages) <= 1000:
        return {"status": "missing_or_oversized_pages", "trades": []}
    collected = []
    seen = set()
    previous_cursor = None
    previous_timestamp = None
    for i, page in enumerate(pages):
        if not isinstance(page, dict) or not isinstance(page.get("cursor"), str) or not page["cursor"]:
            return {"status": "invalid_cursor", "trades": []}
        if previous_cursor is not None and page.get("requested_since") != previous_cursor:
            return {"status": "broken_cursor_chain", "trades": []}
        previous_cursor = page["cursor"]
        rows = page.get("trades")
        if not isinstance(rows, list) or len(rows) > 1000:
            return {"status": "invalid_trade_page", "trades": []}
        for row in rows:
            if not isinstance(row, (list, tuple)) or len(row) != 4:
                return {"status": "invalid_trade_row", "trades": []}
            timestamp, price, volume, trade_id = row
            if (not all(type(v) in (int, float) and isfinite(v)
                        for v in (timestamp, price, volume)) or
                    timestamp < 0 or price <= 0 or volume <= 0):
                return {"status": "invalid_trade_row", "trades": []}
            if previous_timestamp is not None and timestamp < previous_timestamp:
                return {"status": "nonchronological_trade_page", "trades": []}
            previous_timestamp = timestamp
            if (type(trade_id) not in (str, int) or
                    not str(trade_id).strip() or str(trade_id) in seen):
                return {"status": "duplicate_or_invalid_trade_id", "trades": []}
            seen.add(str(trade_id))
            if start <= timestamp < end:
                collected.append((timestamp, price, volume, len(collected)))
            if len(collected) > 10000:
                return {"status": "trade_count_cap", "trades": []}
    if not collected:
        return {"status": "candidate_no_trades_requires_source_attestation", "trades": []}
    return {"status": "candidate_complete_trade_interval_requires_source_attestation",
            "trades": collected, "count": len(collected)}
