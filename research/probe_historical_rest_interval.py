"""Bounded independent Kraken REST corroboration of ONE retained historical trade bucket.

A complete, bounded cursor walk can corroborate a retained archive bucket. It
cannot authenticate an entire quarterly ZIP, certify unobserved no-trade spans,
or authorize predictive labels. Fail closed on truncation, stale API history,
nonmonotone cursors, malformed trades, or source disagreement.
"""
import argparse
import io
import hashlib
import json
import math
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

from match_historical_trades_to_ohlcvt import parse_member, aggregate
from reconcile_retained_trade_evidence import _open_inner, _manifest, _validate_retained_ohlc, _bounded_sha256, MAX_OHLC_ARTIFACT
from verify_trade_candle_provenance import verify_open_boundary
from inventory_kraken_archive import EXPECTED_SHA256

BASE = "https://api.kraken.com/0/public/Trades"
MAX_PAGES = 4
MAX_PAGE_BYTES = 512 * 1024
MAX_TOTAL_BYTES = 2 * 1024 * 1024
MAX_EXPECTED_TRADES = 100
STEP = 300


def compare_rest_bucket(pair, start, expected, *, opener=None, gap_buckets=0):
    """Corroborate an observed bucket; optionally audit ONE following empty-gap candidate.

    Even a continuous REST cursor walk is not a source-completeness attestation.
    A candidate gap is NEVER a verified no-trade interval or a predictive label.
    """
    if (not isinstance(pair, str) or not pair.isalnum() or len(pair) > 24 or
            type(start) is not int or start < 0 or start % STEP or
            not isinstance(expected, list) or not 1 <= len(expected) <= MAX_EXPECTED_TRADES or
            type(gap_buckets) is not int or gap_buckets not in (0, 1)):
        raise ValueError("invalid bounded historical bucket request")
    if any(len(row) != 4 or not all(type(x) in (int, float) and math.isfinite(x) for x in row)
           or row[0] < start or row[0] >= start + STEP or row[1] <= 0 or row[2] <= 0
           for row in expected):
        raise ValueError("invalid retained source trades")
    if any(expected[i][0] > expected[i+1][0] for i in range(len(expected)-1)):
        raise ValueError("unsorted retained source trades")
    witness_end = start + STEP * (1 + gap_buckets)
    opener = opener or urllib.request.urlopen
    cursor = start * 1_000_000_000 - 1
    total = 0
    seen = []
    digests = []
    prior_time = -1.0
    seen_trade_ids = set()
    page_trace = []
    gap_has_trades = False
    first_after_end_trade_timestamp = None
    for page in range(MAX_PAGES):
        requested_since = cursor
        url = BASE + "?" + urllib.parse.urlencode({"pair": pair, "since": str(cursor), "count": 1000})
        req = urllib.request.Request(url, headers={"Accept-Encoding": "identity", "User-Agent": "Cryptoscanner-bounded-history/1.0"})
        with opener(req, timeout=15) as response:
            if response.status != 200 or response.headers.get("Content-Encoding", "identity").lower() != "identity":
                raise RuntimeError("invalid Kraken REST transport")
            raw = response.read(MAX_PAGE_BYTES + 1)
        if len(raw) > MAX_PAGE_BYTES or total + len(raw) > MAX_TOTAL_BYTES:
            raise RuntimeError("historical REST response budget exceeded")
        total += len(raw)
        digests.append(hashlib.sha256(raw).hexdigest())
        # A duplicate JSON key could silently replace source identity or cursor
        # provenance in Python's default JSON decoder. Fail closed instead.
        def unique_json_keys(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise RuntimeError("duplicate Kraken REST JSON key")
                result[key] = value
            return result
        data = json.loads(raw, object_pairs_hook=unique_json_keys)
        if not isinstance(data, dict) or data.get("error") or not isinstance(data.get("result"), dict):
            raise RuntimeError("Kraken historical REST error")
        result = data["result"]
        names = [name for name in result if name != "last"]
        if names != [pair] or not isinstance(result[names[0]], list) or len(result[names[0]]) > 1000:
            raise RuntimeError("invalid historical REST page")
        next_cursor = result.get("last")
        if (not isinstance(next_cursor, str) or not next_cursor.isdigit()
                or len(next_cursor) > 20 or (len(next_cursor) > 1 and next_cursor.startswith("0"))
                or int(next_cursor) <= cursor):
            raise RuntimeError("nonadvancing historical REST cursor")
        cursor = int(next_cursor)
        rows = result[names[0]]
        if not rows:
            return {"status": "abstain_empty_historical_rest_page", "real_labels": 0}
        page_first = None
        page_last = None
        reached_after = False
        for row in rows:
            if (not isinstance(row, list) or len(row) not in (6, 7) or
                    row[3] not in ("b", "s") or row[4] not in ("l", "m") or
                    not isinstance(row[5], str)):
                raise RuntimeError("invalid historical REST trade schema")
            if len(row) == 7:
                trade_id = row[6]
                if (isinstance(trade_id, bool) or not isinstance(trade_id, (str, int)) or
                        not str(trade_id) or str(trade_id) in seen_trade_ids):
                    raise RuntimeError("duplicate or invalid REST trade id")
                seen_trade_ids.add(str(trade_id))
            if any(type(value) is bool for value in row[:3]):
                raise RuntimeError("boolean Kraken REST numeric field")
            try:
                t, price, volume = float(row[2]), float(row[0]), float(row[1])
            except (TypeError, ValueError) as exc:
                raise RuntimeError("invalid historical REST trade") from exc
            if (not all(math.isfinite(x) for x in (t, price, volume)) or
                    t < 0 or price <= 0 or volume <= 0 or t < prior_time):
                raise RuntimeError("nonchronological or invalid historical REST trade")
            # A historical page must not silently return records older than
            # its requested nanosecond cursor (allow 1 microsecond float loss).
            if t + 1e-6 < requested_since / 1_000_000_000:
                raise RuntimeError("REST trade predates requested cursor")
            prior_time = t
            if page_first is None:
                page_first = t
            page_last = t
            if t >= witness_end:
                reached_after = True
                if first_after_end_trade_timestamp is None:
                    first_after_end_trade_timestamp = t
                continue
            if t >= start + STEP:
                gap_has_trades = True
                continue
            if t >= start:
                seen.append((t, price, volume))
                if len(seen) > MAX_EXPECTED_TRADES:
                    return {"status": "abstain_rest_bucket_over_cap", "real_labels": 0}
        # Kraken's pagination token is a nanosecond time cursor. A cursor
        # behind the latest returned trade cannot certify that intervening
        # source rows were traversed; reject rather than infer completeness.
        # Allow 10 microseconds for float conversion of source timestamps.
        if cursor / 1_000_000_000 + 1e-5 < page_last:
            raise RuntimeError("REST cursor predates returned trade")
        page_trace.append({
            "requested_since": str(requested_since),
            "returned_last": str(cursor),
            "rows": len(rows),
            "first_trade_timestamp": page_first,
            "last_inspected_timestamp": page_last,
            "page_sha256": digests[-1],
            "after_end_witness": reached_after,
            "first_after_end_trade_timestamp": first_after_end_trade_timestamp,
        })
        if reached_after:
            if not seen and page == 0 and float(rows[0][2]) >= witness_end:
                return {"status": "abstain_historical_range_unavailable", "real_labels": 0}
            # Exact row sequence is a bounded corroboration, not an authenticated
            # quarterly completeness certificate. No-trade intervals stay unknown.
            equal = len(seen) == len(expected) and all(
                abs(a[0] - b[0]) <= 1e-6 and
                math.isclose(a[1], b[1], rel_tol=1e-9, abs_tol=0) and
                math.isclose(a[2], b[2], rel_tol=1e-9, abs_tol=0)
                for a, b in zip(seen, expected))
            # A distant trade (possibly months later) is not a witness for
            # the immediately following retained bucket. Never call that a
            # corroborated empty gap, even when the preceding trades match.
            following_near = bool(gap_buckets and first_after_end_trade_timestamp is not None
                                  and first_after_end_trade_timestamp < witness_end + STEP)
            status = ("abstain_rest_archive_disagreement" if not equal else
                      "abstain_rest_gap_contains_trades" if gap_has_trades else
                      "abstain_rest_gap_following_witness_distant" if gap_buckets and not following_near else
                      "independent_rest_gap_candidate_correlated_not_complete" if gap_buckets else
                      "independent_rest_bucket_correlated")
            return {"status": status,
                    "market": pair, "bucket_open": start, "archive_trades": len(expected),
                    "rest_trades": len(seen), "pages": page+1, "bytes_transferred": total,
                    "rest_page_sha256": digests, "rest_cursor_trace": page_trace,
                    "after_end_witness": True,
                    "witness_end": witness_end,
                    "first_after_end_trade_timestamp": first_after_end_trade_timestamp,
                    "following_bucket_witness_near": following_near,
                    "candidate_empty_gap_buckets": [start + STEP] if gap_buckets and equal and not gap_has_trades and following_near else [],
                    "independent_complete_historical_intervals": 0,
                    "independent_quarterly_completeness_verified": False,
                    "no_trade_intervals_verified": 0, "real_labels": 0,
                    "production_modified": False}
    return {"status": "abstain_rest_pagination_or_history_limit", "market": pair,
            "bucket_open": start, "pages": MAX_PAGES, "bytes_transferred": total,
            "rest_cursor_trace": page_trace,
            "independent_quarterly_completeness_verified": False,
            "real_labels": 0, "production_modified": False}



def corroborate_retained_ohlc(ohlc_artifact, market, start, expected, rest_result):
    """Triangulate REST, retained trades and retained OHLC for one observed bucket.

    This validates a *correspondence*, not historical trade completeness or
    predictive-label eligibility. All missing or mismatching buckets abstain.
    """
    result = dict(rest_result)
    result["independent_complete_historical_intervals"] = 0
    result["independent_quarterly_completeness_verified"] = False
    result["real_labels"] = 0
    result["production_modified"] = False
    result["three_way_candle_correspondence"] = False
    if result.get("status") != "independent_rest_bucket_correlated":
        return result
    ohlc_digest = _bounded_sha256(ohlc_artifact, MAX_OHLC_ARTIFACT)
    with _open_inner(ohlc_artifact, "reusable_ohlc_evidence.zip", MAX_OHLC_ARTIFACT) as archive:
        manifest = _manifest(archive)
        if (manifest.get("schema") != 1 or
                manifest.get("source_archive_sha256") != EXPECTED_SHA256 or
                manifest.get("independent_trade_completeness") is not False or
                manifest.get("real_labels") != 0):
            raise ValueError("untrusted OHLC source manifest")
        member = market + "_5.csv"
        meta = manifest.get("markets", {}).get(member)
        if not isinstance(meta, dict):
            result["status"] = "abstain_ohlc_market_missing"
            return result
        name = "candles/" + member
        if name not in archive.namelist() or archive.namelist().count(name) != 1:
            raise ValueError("missing or duplicated retained OHLC member")
        info = archive.getinfo(name)
        if info.file_size > 64 * 1024 * 1024 or info.flag_bits & 1:
            raise ValueError("unsafe OHLC member")
        payload = archive.read(info)
        if hashlib.sha256(payload).hexdigest() != meta.get("retained_sha256"):
            raise ValueError("retained OHLC SHA256 mismatch")
        candles, _ = _validate_retained_ohlc(payload, meta)
    candle = next((row for row in candles if int(row[0]) == start), None)
    if candle is None:
        result["status"] = "abstain_ohlc_bucket_missing"
        return result
    boundary = verify_open_boundary(candle, expected, independent_trade_source=True)
    if boundary.get("status") != "verified_open_boundary":
        result["status"] = "abstain_rest_trade_ohlc_disagreement"
        result["boundary_check"] = boundary["status"]
        return result
    result.update(status="independent_rest_trade_ohlc_correlated",
                  three_way_candle_correspondence=True,
                  ohlc_candle_open=start,
                  ohlc_member_sha256=meta["retained_sha256"],
                  ohlc_artifact_sha256=ohlc_digest,
                  timestamp_semantics="observed_open_boundary_for_this_bucket_only")
    return result


def probe_retained(archive_path, *, opener=None, ohlc_artifact=None):
    """Choose first bounded real bucket from retained ZIP; never download source."""
    archive_path = Path(archive_path)
    if not archive_path.is_file() or archive_path.stat().st_size > 12*1024*1024:
        raise ValueError("missing or oversized retained trade archive")
    with zipfile.ZipFile(archive_path) as z:
        names = sorted(n for n in z.namelist() if n.startswith("trades/") and n.endswith(".csv"))
        if not 1 <= len(names) <= 4 or len(names) != len(set(names)):
            raise ValueError("invalid retained market selection")
        for name in names:
            market = name.removeprefix("trades/").removesuffix(".csv")
            if not market.isalnum():
                raise ValueError("invalid retained market name")
            # Existing parser enforces schema, IDs, source row chronology and cap.
            info = z.getinfo(name)
            if info.file_size > 3*1024*1024 or info.flag_bits & 1:
                raise ValueError("oversized or encrypted retained trade member")
            raw = z.read(info)
            # Reopen complete temporary in-memory ZIP for parser.
            tmp = io.BytesIO()
            with zipfile.ZipFile(tmp, "w") as scratch:
                scratch.writestr(market+".csv", raw)
            with zipfile.ZipFile(io.BytesIO(tmp.getvalue())) as inner:
                trades = parse_member(inner, market+".csv", schema_verified=True)
            _, buckets = aggregate(trades)
            for start, records in sorted(buckets.items()):
                if 1 <= len(records) <= MAX_EXPECTED_TRADES:
                    try:
                        rest = compare_rest_bucket(market, start, records, opener=opener)
                    except (OSError, RuntimeError, ValueError) as exc:
                        return {"status": "abstain_rest_transport_or_source_error",
                                "error_type": type(exc).__name__, "market": market,
                                "bucket_open": start, "real_labels": 0,
                                "independent_quarterly_completeness_verified": False,
                                "production_modified": False}
                    # Artifact integrity errors must propagate and fail the job;
                    # only genuine REST transport/source errors are abstentions.
                    return (corroborate_retained_ohlc(ohlc_artifact, market, start, records, rest)
                            if ohlc_artifact is not None else rest)
    return {"status": "abstain_no_bounded_retained_bucket", "real_labels": 0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained-trades", required=True)
    ap.add_argument("--ohlc", required=False)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    output = Path(args.output)
    if output.exists():
        raise FileExistsError("refuse historical probe overwrite")
    result = probe_retained(args.retained_trades, ohlc_artifact=args.ohlc)
    payload = (json.dumps(result, sort_keys=True) + "\n").encode()
    if len(payload) > 8192:
        raise ValueError("oversized historical probe report")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as dest:
        dest.write(payload)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
