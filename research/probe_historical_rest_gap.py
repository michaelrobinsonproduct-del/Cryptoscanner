"""Bounded historical REST gap-candidate audit; NEVER certify no-trade or labels.

Requires retained source trades bracketing one absent five-minute bucket, a
SHA-checked retained OHLC candle on both sides, and no OHLC candle in the gap.
The public REST cursor walk is independently compared, but is not an official
historical completeness attestation. All output remains research-only.
"""
import argparse
import hashlib
import io
import json
import zipfile
from pathlib import Path

from inventory_kraken_archive import EXPECTED_SHA256
from match_historical_trades_to_ohlcvt import parse_member, aggregate
from probe_historical_rest_interval import (
    MAX_EXPECTED_TRADES, STEP, compare_rest_bucket, corroborate_retained_ohlc,
)
from reconcile_retained_trade_evidence import (
    _bounded_sha256, _manifest, _open_inner, _validate_retained_ohlc,
    MAX_OHLC_ARTIFACT,
)

MAX_TRADE_ARTIFACT = 12 * 1024 * 1024
MAX_MEMBER_BYTES = 3 * 1024 * 1024


def load_ohlc_starts(path, market):
    """Verify the retained OHLC source-tail contract before checking a gap."""
    digest = _bounded_sha256(path, MAX_OHLC_ARTIFACT)
    with _open_inner(path, "reusable_ohlc_evidence.zip", MAX_OHLC_ARTIFACT) as archive:
        manifest = _manifest(archive)
        if (manifest.get("schema") != 1 or
                manifest.get("source_archive_sha256") != EXPECTED_SHA256 or
                manifest.get("independent_trade_completeness") is not False or
                manifest.get("real_labels") != 0):
            raise ValueError("untrusted retained OHLC manifest")
        member = market + "_5.csv"
        meta = manifest.get("markets", {}).get(member)
        name = "candles/" + member
        if not isinstance(meta, dict) or archive.namelist().count(name) != 1:
            raise ValueError("missing or duplicate retained OHLC market")
        info = archive.getinfo(name)
        if info.file_size > 64 * 1024 * 1024 or info.flag_bits & 1:
            raise ValueError("unsafe retained OHLC member")
        payload = archive.read(info)
        if hashlib.sha256(payload).hexdigest() != meta.get("retained_sha256"):
            raise ValueError("retained OHLC SHA mismatch")
        candles, _ = _validate_retained_ohlc(payload, meta)
    return {int(row[0]) for row in candles}, digest


def select_bracketed_gap(trades_path, ohlc_path, *, candidate_index=0):
    """Select one bounded single-gap candidate, validating ALL trade members."""
    path = Path(trades_path)
    if not path.is_file() or path.stat().st_size > MAX_TRADE_ARTIFACT:
        raise ValueError("missing or oversized retained trade evidence")
    if type(candidate_index) is not int or not 0 <= candidate_index <= 3:
        raise ValueError("candidate index must be a bounded integer 0..3")
    # Validate every retained trade member before consulting the OHLC source.
    # A malformed later market must not be hidden by an earlier candidate.
    candidate_markets = []
    with zipfile.ZipFile(path) as archive:
        # A retained evidence ZIP is at most four trade CSVs plus one manifest.
        # Do not silently ignore extra, duplicate, encrypted, linked or unusual
        # entries: they can disguise an inconsistent retained source package.
        infos = archive.infolist()
        all_names = [info.filename for info in infos]
        if (not 1 <= len(infos) <= 5 or len(all_names) != len(set(all_names))):
            raise ValueError("duplicate or oversized retained evidence member list")
        for info in infos:
            name = info.filename
            if (name != "manifest.json" and not
                    (name.startswith("trades/") and name.endswith(".csv"))):
                raise ValueError("unexpected retained evidence member")
            mode = (info.external_attr >> 16) & 0o170000
            if (info.is_dir() or mode == 0o120000 or info.flag_bits & 1 or
                    info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED)):
                raise ValueError("unsafe retained evidence ZIP entry")
            if name == "manifest.json" and info.file_size > 128 * 1024:
                raise ValueError("oversized retained evidence manifest")
        names = sorted(n for n in all_names
                       if n.startswith("trades/") and n.endswith(".csv"))
        if not 1 <= len(names) <= 4 or len(names) != len(set(names)):
            raise ValueError("invalid trade member selection")
        for name in names:
            market = name.removeprefix("trades/").removesuffix(".csv")
            if not market.isalnum() or len(market) > 24:
                raise ValueError("unsafe trade market")
            info = archive.getinfo(name)
            if info.file_size > MAX_MEMBER_BYTES or info.flag_bits & 1:
                raise ValueError("unsafe trade member")
            raw = archive.read(info)
            scratch = io.BytesIO()
            with zipfile.ZipFile(scratch, "w") as z:
                z.writestr(market + ".csv", raw)
            with zipfile.ZipFile(io.BytesIO(scratch.getvalue())) as z:
                records = parse_member(z, market + ".csv", schema_verified=True)
            _, buckets = aggregate(records)
            starts = sorted(buckets)
            gaps = []
            for start in starts:
                if (start + 2 * STEP in buckets and start + STEP not in buckets and
                        1 <= len(buckets[start]) <= MAX_EXPECTED_TRADES and
                        1 <= len(buckets[start + 2 * STEP]) <= MAX_EXPECTED_TRADES):
                    gaps.append(start)
            if gaps:
                candidate_markets.append((market, buckets, gaps))
    # Index only gaps corroborated by both observed OHLC bracket candles.
    # A candidate rejected by the OHLC evidence must not prevent examining
    # a later bounded candidate; no missing interval is declared no-trade.
    remaining = candidate_index
    for market, buckets, gaps in candidate_markets:
        ohlc_starts, digest = load_ohlc_starts(ohlc_path, market)
        for start in gaps:
            if (start in ohlc_starts and start + 2 * STEP in ohlc_starts and
                    start + STEP not in ohlc_starts):
                if remaining == 0:
                    return (market, start, buckets[start],
                            buckets[start + 2 * STEP], digest)
                remaining -= 1
    return None

def audit_bracketed_gap(trades_path, ohlc_path, *, opener=None, candidate_index=0):
    base = {
        "status": "abstain_no_bracketed_retained_gap",
        "candidate_index": candidate_index,
        "candidate_empty_gap_buckets": [],
        "independent_complete_historical_intervals": 0,
        "independent_quarterly_completeness_verified": False,
        "no_trade_intervals_verified": 0,
        "real_labels": 0,
        "held_out_lift": None,
        "production_modified": False,
        "source_trade_artifact_sha256": _bounded_sha256(trades_path, MAX_TRADE_ARTIFACT),
    }
    selected = select_bracketed_gap(trades_path, ohlc_path, candidate_index=candidate_index)
    if selected is None:
        return base
    market, start, expected, following, ohlc_sha = selected
    base.update(market=market, preceding_bucket_open=start,
                candidate_gap_open=start + STEP, following_bucket_open=start + 2 * STEP,
                retained_ohlc_artifact_sha256=ohlc_sha)
    try:
        rest = compare_rest_bucket(market, start, expected, opener=opener, gap_buckets=1)
    except (OSError, RuntimeError, ValueError) as exc:
        base.update(status="abstain_rest_transport_or_source_error",
                    error_type=type(exc).__name__)
        return base
    base.update(rest_pages=rest.get("pages", 0),
                rest_bytes_transferred=rest.get("bytes_transferred", 0),
                rest_cursor_trace=rest.get("rest_cursor_trace", []))
    if (rest.get("status") != "independent_rest_gap_candidate_correlated_not_complete" or
            rest.get("following_bucket_witness_near") is not True):
        base["status"] = rest.get("status", "abstain_rest_gap_unverified")
        if base["status"] == "independent_rest_gap_candidate_correlated_not_complete":
            base["status"] = "abstain_rest_missing_near_following_witness"
        return base
    # Reuse exact observed-candle SHA and boundary verification; do not turn
    # a candidate REST gap into an authenticated source-complete interval.
    observed = corroborate_retained_ohlc(
        ohlc_path, market, start, expected,
        dict(rest, status="independent_rest_bucket_correlated"))
    if (observed.get("status") != "independent_rest_trade_ohlc_correlated" or
            observed.get("three_way_candle_correspondence") is not True):
        base["status"] = observed.get("status", "abstain_ohlc_mismatch")
        return base
    # Authenticate the *following* observed bucket independently. A distant
    # after-end witness does not establish that this retained candle existed
    # in the REST source, and neither side certifies the empty gap itself.
    try:
        next_rest = compare_rest_bucket(market, start + 2 * STEP, following, opener=opener)
    except (OSError, RuntimeError, ValueError) as exc:
        base.update(status="abstain_following_rest_transport_or_source_error",
                    following_error_type=type(exc).__name__)
        return base
    base.update(following_rest_pages=next_rest.get("pages", 0),
                following_rest_bytes_transferred=next_rest.get("bytes_transferred", 0),
                following_rest_cursor_trace=next_rest.get("rest_cursor_trace", []))
    if (next_rest.get("status") != "independent_rest_bucket_correlated" or
            next_rest.get("after_end_witness") is not True):
        base.update(status="abstain_following_rest_bucket_unverified",
                    following_rest_status=next_rest.get("status", "unknown"))
        return base
    next_observed = corroborate_retained_ohlc(
        ohlc_path, market, start + 2 * STEP, following, next_rest)
    if (next_observed.get("status") != "independent_rest_trade_ohlc_correlated" or
            next_observed.get("three_way_candle_correspondence") is not True):
        base.update(status="abstain_following_rest_ohlc_disagreement",
                    following_ohlc_status=next_observed.get("status", "unknown"))
        return base
    base.update(status="independent_rest_bracketed_gap_candidate_not_complete",
                candidate_empty_gap_buckets=[start + STEP],
                preceding_observed_candle_correlated=True,
                following_observed_candle_correlated=True,
                total_rest_bytes_transferred=base["rest_bytes_transferred"] + base["following_rest_bytes_transferred"],
                limitation="REST observed gap candidate is NOT certified historical no-trade completeness")
    return base


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--retained-trades", required=True)
    parser.add_argument("--ohlc", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--candidate-index", type=int, default=0,
                        help="0..3: select an alternate OHLC-bracketed gap candidate")
    args = parser.parse_args()
    target = Path(args.output)
    if target.exists():
        raise FileExistsError("refuse historical gap report overwrite")
    result = audit_bracketed_gap(args.retained_trades, args.ohlc,
                                 candidate_index=args.candidate_index)
    raw = (json.dumps(result, sort_keys=True) + "\n").encode()
    if len(raw) > 8192:
        raise ValueError("oversized historical gap report")
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as output:
        output.write(raw)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
