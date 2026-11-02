"""Read-only authenticated Kraken Trades gap audit; never changes PAPER ledger.

A TLS-fetched source SHA binds exact response bytes, NOT an exchange signature.
Trade timestamps are real print times. No candles, imputed prices, fills, or
loosening of the existing 45-minute maximum observed gap.
"""
import argparse
import base64
from bisect import bisect_right
from collections import Counter, defaultdict
import datetime as dt
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode, urlparse, parse_qs
from urllib.request import urlopen

from paper_pov import ledger
from paper_pov.learning_outcomes import (
    GAP_REASONS, HORIZONS, MAX_GAP, _aware, _index, sampled_outcomes,
    coverage_summary,
)
from paper_pov.segmented_storage import MAX_RAW_BYTES

REVISION = "kraken-rest-public-trades-v1"
ENDPOINT = "https://api.kraken.com/0/public/Trades"
MAX_RESPONSE_BYTES = 256_000
MAX_PAGES = 3
MAX_PAIRS = 3
UTC = dt.timezone.utc


def _utc(value):
    return _aware(value)


def _decimal(value):
    if not isinstance(value, (str, int, float, Decimal)) or isinstance(value, bool):
        raise ValueError("Invalid trade decimal type")
    try:
        number = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError("Invalid trade decimal") from exc
    if not number.is_finite() or number <= 0:
        raise ValueError("Invalid trade decimal")
    return number


def _ns(when):
    """Exact UTC nanoseconds without floating-point timestamp rounding."""
    delta = _utc(when) - dt.datetime(1970, 1, 1, tzinfo=UTC)
    return ((delta.days * 86400 + delta.seconds) * 1_000_000_000
            + delta.microseconds * 1000)


def _trade_time(value):
    stamp = _decimal(value)
    # Kraken prints fractional UNIX seconds, often with 9 decimal places.
    # Retain every authentic nanosecond; do NOT round into fake microseconds.
    nanos = stamp * 1_000_000_000
    if nanos != nanos.to_integral_value():
        raise ValueError("Subnanosecond Kraken trade time unsupported")
    return int(nanos)


def _iso_ns(value):
    seconds, nanos = divmod(value, 1_000_000_000)
    base = dt.datetime(1970, 1, 1, tzinfo=UTC) + dt.timedelta(seconds=seconds)
    return base.strftime("%Y-%m-%dT%H:%M:%S") + ".%09d+00:00" % nanos


def _source_url(pair, since):
    if not isinstance(pair, str) or not pair.isascii() or not pair.isalnum():
        raise ValueError("Invalid Kraken pair")
    if type(since) is not int or since < 0:
        raise ValueError("Invalid Kraken since cursor")
    return ENDPOINT + "?" + urlencode({"pair": pair, "since": str(since)})


def _verify_page(page, pair, expected_since, evaluation_at):
    if not isinstance(page, dict) or page.get("revision") != REVISION:
        raise ValueError("Unknown Kraken source revision")
    url = page.get("request_url")
    if url != _source_url(pair, expected_since):
        raise ValueError("Source identity/endpoint or pagination cursor mismatch")
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "api.kraken.com" or parsed.path != "/0/public/Trades":
        raise ValueError("Untrusted Kraken endpoint")
    if parse_qs(parsed.query) != {"pair": [pair], "since": [str(expected_since)]}:
        raise ValueError("Unexpected Kraken query")
    raw64 = page.get("response_b64")
    if not isinstance(raw64, str) or len(raw64) > MAX_RESPONSE_BYTES * 2:
        raise ValueError("Missing or oversized Kraken response")
    try:
        raw = base64.b64decode(raw64, validate=True)
    except Exception as exc:
        raise ValueError("Invalid response encoding") from exc
    if not raw or len(raw) > MAX_RESPONSE_BYTES or hashlib.sha256(raw).hexdigest() != page.get("response_sha256"):
        raise ValueError("Kraken source SHA256 mismatch")
    retrieved = _utc(page.get("retrieved_at"))
    if retrieved > evaluation_at:
        raise ValueError("Source acquired after evaluation cutoff")
    payload = json.loads(raw, parse_float=Decimal)
    if not isinstance(payload, dict) or payload.get("error") != [] or not isinstance(payload.get("result"), dict):
        raise ValueError("Kraken API error or malformed response")
    result = payload["result"]
    if set(result) != {"last", pair}:
        # Kraken sometimes returns an alias: fail closed until authenticated
        # AssetPairs identity mapping is implemented.
        raise ValueError("Kraken response pair identity mismatch")
    cursor = result["last"]
    if not isinstance(cursor, str) or not cursor.isdigit() or int(cursor) <= expected_since:
        raise ValueError("Kraken pagination cursor did not advance")
    trades = result[pair]
    if not isinstance(trades, list) or len(trades) > 1000:
        raise ValueError("Invalid bounded trade page")
    parsed_trades = []
    for trade in trades:
        if not isinstance(trade, list) or len(trade) != 7:
            raise ValueError("Missing authenticated trade ID/fields")
        price, volume, at, side, ordertype, misc, trade_id = trade
        if side not in ("b", "s") or ordertype not in ("m", "l") or not isinstance(misc, str):
            raise ValueError("Invalid trade metadata")
        if not isinstance(trade_id, (str, int)) or isinstance(trade_id, bool) or not str(trade_id):
            raise ValueError("Missing Kraken trade ID")
        when = _trade_time(at)
        if when > _ns(retrieved):
            raise ValueError("Future trade in captured source")
        parsed_trades.append((when, str(trade_id), float(_decimal(price)), str(_decimal(volume))))
    if any(b[0] < a[0] for a, b in zip(parsed_trades, parsed_trades[1:])):
        raise ValueError("Nonmonotonic Kraken trade timestamps")
    return int(cursor), parsed_trades


def verify_sources(captures, evaluation_at):
    """Fail closed per pair; reject incomplete pagination and duplicate times.

    Source bytes must be captured by the read-only GitHub HTTPS workflow. A
    caller-provided hash alone does not authenticate an external origin.
    """
    if not isinstance(captures, list):
        raise ValueError("Source captures must be a list")
    verified = {}
    provenance = []
    for item in captures:
        if not isinstance(item, dict) or set(item) != {"pair", "start_since_ns", "pages"}:
            raise ValueError("Invalid source capture schema")
        pair = item["pair"]
        pages = item["pages"]
        if pair in verified or not isinstance(pages, list) or not 1 <= len(pages) <= MAX_PAGES:
            raise ValueError("Duplicate pair or invalid page count")
        cursor = item["start_since_ns"]
        if type(cursor) is not int or cursor < 0:
            raise ValueError("Invalid source start cursor")
        prints = []
        seen_ids = set()
        collapsed_same_timestamp = 0
        for page in pages:
            cursor, trades = _verify_page(page, pair, cursor, evaluation_at)
            for when, tid, price, volume in trades:
                if tid in seen_ids:
                    raise ValueError("Duplicate trade identity")
                if prints and when < prints[-1][0]:
                    raise ValueError("Nonmonotonic cross-page trades")
                seen_ids.add(tid)
                if prints and when == prints[-1][0]:
                    # Multiple authentic Kraken prints can share a nanosecond.
                    # Preserve exact raw page and ID provenance; use the LAST
                    # source-listed real print, not an invented average/candle.
                    prints[-1] = (when, price)
                    collapsed_same_timestamp += 1
                else:
                    prints.append((when, price))
            provenance.append({"pair": pair, "sha256": page["response_sha256"],
                               "request_url": page["request_url"],
                               "retrieved_at": page["retrieved_at"],
                               "trade_count": len(trades)})
        if not prints:
            raise ValueError("No authentic trade observations")
        verified[pair] = {"prints": prints,
                          "first": prints[0][0], "last": prints[-1][0],
                          "start_since_ns": item["start_since_ns"],
                          "last_cursor_ns": cursor,
                          "collapsed_same_timestamp_prints": collapsed_same_timestamp}
    return verified, provenance


def _recovery_row(row, original, trades, evaluation_at):
    if row["status"] != "ABSTAIN_GAP" or not trades:
        return None
    start, target = _ns(row["as_of"]), _ns(row["target_at"])
    gap_ns = 45 * 60 * 1_000_000_000
    # Proof must start no later than entry and extend past the target.
    if trades["start_since_ns"] > start or trades["last"] < target:
        return None
    merged = [(_ns(t), p) for t, p in original] + trades["prints"]
    stamps = [t for t, _ in merged]
    if len(stamps) != len(set(stamps)):
        raise ValueError("Duplicate original/recovered observation timestamps")
    merged.sort()
    lo = bisect_right(merged, (start, float("inf")))
    hi = bisect_right(merged, (target + gap_ns, float("inf")))
    within = [(t, p) for t, p in merged[lo:hi] if t <= target]
    anchors = [(t, p) for t, p in merged[lo:hi] if t >= target]
    if not within or not anchors:
        return None
    timeline = [start] + [t for t, _ in within] + [anchors[0][0]]
    if any(b - a > gap_ns for a, b in zip(timeline, timeline[1:])):
        return None
    entry = row["entry_price"]
    peak = 100 * (max([entry] + [p for _, p in within]) / entry - 1)
    return {"status": "MATURED_RECOVERED_TRADE_EVIDENCE",
            "observed_peak_pct": round(peak, 6),
            "observed_20pct_hit": peak >= 20,
            "observed_30pct_hit": peak >= 30,
            "anchor_at": _iso_ns(anchors[0][0])}


def audit(state, evaluation_at, captures=(), source_errors=()):
    now = _utc(evaluation_at)
    ledger.verify(state, MAX_RAW_BYTES)
    if not state["runs"] or now < _utc(state["runs"][-1]["as_of"]):
        raise ValueError("Evaluation precedes durable ledger")
    before_rows = sampled_outcomes(state, now)
    before = coverage_summary(before_rows)["by_horizon"]
    verified, provenance = verify_sources(list(captures), now)
    _, _, by_pair, _ = _index(state, now)
    after = json.loads(json.dumps(before))
    recovered_examples = []
    for row in before_rows:
        if row["status"] != "ABSTAIN_GAP":
            continue
        pair, h = row["pair"], str(row["horizon_hours"])
        update = _recovery_row(row, by_pair.get(pair, []), verified.get(pair), now)
        if update is None:
            continue
        after[h]["gap_abstentions"] -= 1
        after[h]["gap_reason_counts"][row["gap_reason"]] -= 1
        after[h]["matured_recovered_trade_evidence"] = after[h].get("matured_recovered_trade_evidence", 0) + 1
        after[h]["recovered_trade_20pct_windows"] = after[h].get("recovered_trade_20pct_windows", 0) + int(update["observed_20pct_hit"])
        after[h]["recovered_trade_30pct_windows"] = after[h].get("recovered_trade_30pct_windows", 0) + int(update["observed_30pct_hit"])
        if len(recovered_examples) < 30:
            recovered_examples.append({"pair": pair, "run_id": row["run_id"],
                "horizon_hours": row["horizon_hours"], "old_gap_reason": row["gap_reason"],
                **update})
    for h in HORIZONS:
        key = str(h)
        after[key].setdefault("matured_recovered_trade_evidence", 0)
        after[key].setdefault("recovered_trade_20pct_windows", 0)
        after[key].setdefault("recovered_trade_30pct_windows", 0)
        after[key]["still_missing"] = after[key]["gap_abstentions"]
        after[key]["eligible_before"] = before[key]["matured_observed"] + before[key]["gap_abstentions"]
        after[key]["eligible_after"] = after[key]["eligible_before"]
        before[key]["eligible_before"] = after[key]["eligible_before"]
        before[key]["retained_observations_only"] = True
        if after[key]["matured_recovered_trade_evidence"] + after[key]["gap_abstentions"] != before[key]["gap_abstentions"]:
            raise ValueError("Gap accounting failed")
    archived = state.get("archived", {})
    index = state.get("archive_index", [])
    run_intervals = []
    for a, b in zip(state["runs"], state["runs"][1:]):
        gap = _utc(b["as_of"]) - _utc(a["as_of"])
        if gap > MAX_GAP:
            run_intervals.append({
                "from_run_id": a["id"], "to_run_id": b["id"],
                "from_as_of": a["as_of"], "to_as_of": b["as_of"],
                "gap_minutes": round(gap.total_seconds() / 60, 6),
                "from_report_sha256": a["report_sha256"],
                "to_report_sha256": b["report_sha256"],
                "from_source_sha": a["source_sha"],
                "to_source_sha": b["source_sha"]})
    return {"schema": 1, "mode": "READ_ONLY_TRADE_GAP_AUDIT",
        "source_ledger_sha256": state["sha256"], "source_generation": state["generation"],
        "evaluation_at": now.isoformat(), "max_gap_minutes": 45,
        "source_revision": REVISION, "source_pages": provenance,
        "source_coverage": {pair: {"first_trade_utc": _iso_ns(s["first"]),
            "last_trade_utc": _iso_ns(s["last"]), "pages": sum(p["pair"] == pair for p in provenance),
            "requested_start_utc": _iso_ns(s["start_since_ns"]),
            "collapsed_same_timestamp_prints": s["collapsed_same_timestamp_prints"]}
            for pair, s in verified.items()},
        "no_trade_vs_missing": "UNPROVEN_WITHOUT_COMPLETE_SOURCE_COVERAGE",
        "source_errors": list(source_errors),
        "retained_run_interval_gaps": {"over_45m_count": len(run_intervals),
            "max_gap_minutes": max((x["gap_minutes"] for x in run_intervals), default=0),
            "source_bound_intervals": run_intervals},
        "retention": {"ledger_retention_hours": 50,
            "archived_runs_count": archived.get("scans", 0),
            "archived_observations_count": archived.get("observations", 0),
            "retained_archive_index_runs": len(index),
            "archived_rows_not_evaluable_from_current_snapshot": True},
        "before": before, "after": after,
        "recovered_examples": recovered_examples,
        "recovered_total_correlated_windows": sum(after[str(h)]["matured_recovered_trade_evidence"] for h in HORIZONS),
        "recovered_is_exchange_print_evidence_not_executable_fill": True,
        "source_is_https_captured_not_exchange_signed": True,
        "production_applied": False, "ledger_modified": False, "held_out_lift": None}


def capture_bounded(state, evaluation_at, max_pairs=MAX_PAIRS, max_pages=MAX_PAGES, opener=urlopen):
    """Actual bounded public HTTPS Kraken source acquisition; no credentials/writes."""
    now = _utc(evaluation_at)
    rows = sampled_outcomes(state, now)
    candidates = defaultdict(list)
    for row in rows:
        if (row["status"] == "ABSTAIN_GAP"
                and _utc(row["as_of"]) >= now - dt.timedelta(hours=49)
                and _utc(row["target_at"]) <= now):
            candidates[row["pair"]].append(row)
    ranked = sorted(candidates, key=lambda p: (
        min(r["horizon_hours"] for r in candidates[p]),
        -max(_utc(r["as_of"]).timestamp() for r in candidates[p]),
        -len(candidates[p]), p))[:max_pairs]
    # Compare illiquid-gap source behavior with a liquid-market control.
    # Do not invent a market: only use a control present in the sealed ledger.
    if max_pairs >= 3:
        for control in ("SOLUSD", "ETHUSD", "XBTUSD"):
            if control in candidates and control not in ranked:
                ranked[-1] = control
                break
    captures, errors = [], []
    for pair in ranked:
        start = min(_utc(r["as_of"]) for r in candidates[pair])
        since = max(0, _ns(start) - 1)
        pages = []
        attempted = {}
        try:
            for _ in range(max_pages):
                url = _source_url(pair, since)
                with opener(url, timeout=8) as response:
                    if response.geturl() != url:
                        raise ValueError("Unexpected HTTPS redirect")
                    raw = response.read(MAX_RESPONSE_BYTES + 1)
                if not raw or len(raw) > MAX_RESPONSE_BYTES:
                    raise ValueError("Empty or oversized Kraken response")
                payload = json.loads(raw, parse_float=Decimal)
                attempted = {"request_url": url, "source_sha256": hashlib.sha256(raw).hexdigest(),
                    "raw_response_b64": base64.b64encode(raw).decode("ascii"),
                    "requested_since_ns": since,
                    "response_last": str(payload.get("result", {}).get("last")) if isinstance(payload, dict) else None,
                    "response_pair_keys": sorted(k for k in payload.get("result", {}) if k != "last") if isinstance(payload, dict) and isinstance(payload.get("result"), dict) else [],
                    "returned_trade_count": sum(len(v) for k, v in payload.get("result", {}).items() if k != "last" and isinstance(v, list)) if isinstance(payload, dict) and isinstance(payload.get("result"), dict) else 0}
                if not isinstance(payload, dict) or payload.get("error") != []:
                    raise ValueError("Kraken API error")
                retrieved = dt.datetime.now(UTC).isoformat()
                page = {"revision": REVISION, "request_url": url,
                    "retrieved_at": retrieved, "response_sha256": hashlib.sha256(raw).hexdigest(),
                    "response_b64": base64.b64encode(raw).decode("ascii")}
                next_since, prints = _verify_page(page, pair, since, dt.datetime.now(UTC))
                pages.append(page)
                since = next_since
                if prints and prints[-1][0] >= max(_ns(r["target_at"]) for r in candidates[pair]):
                    break
            if pages:
                candidate = {"pair": pair, "start_since_ns": max(0, _ns(start)-1),
                             "pages": pages}
                verify_sources([candidate], dt.datetime.now(UTC))
                captures.append(candidate)
        except Exception as exc:
            errors.append({"pair": pair, "status": "SOURCE_ABSTAIN",
                           "reason": type(exc).__name__ + ": " + str(exc)[:160],
                           **attempted})
    return captures, errors


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--sources-output")
    parser.add_argument("--capture", action="store_true")
    args = parser.parse_args(argv)
    state = json.loads(Path(args.ledger).read_bytes())
    now = dt.datetime.now(UTC)
    captures, errors = capture_bounded(state, now) if args.capture else ([], [])
    report = audit(state, dt.datetime.now(UTC), captures, errors)
    Path(args.output).write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
    if args.sources_output:
        Path(args.sources_output).write_text(json.dumps(
            {"schema": 1, "source_revision": REVISION, "captures": captures,
             "errors": errors}, sort_keys=True) + "\n")
    print(json.dumps({"generation": report["source_generation"],
        "recovered": report["recovered_total_correlated_windows"],
        "source_errors": len(errors), "by_horizon": {h: {
            "eligible": report["before"][h]["eligible_before"],
            "immature": report["before"][h]["immature"],
            "gap_before": report["before"][h]["gap_abstentions"],
            "recovered": report["after"][h]["matured_recovered_trade_evidence"],
            "still_missing": report["after"][h]["still_missing"]}
            for h in map(str, HORIZONS)}}, sort_keys=True))


if __name__ == "__main__":
    main()
