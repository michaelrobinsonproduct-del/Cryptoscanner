"""Offline, bounded reconciliation of retained Kraken trade/OHLC evidence.

Candidate exact candle matches do not authenticate the full trade source, prove
interval completeness, or authorize predictive labels.
"""
import argparse
import csv
import hashlib
import io
import json
import zipfile
from math import isfinite
from pathlib import Path

from audit_trade_candidate_windows import audit_candidate_windows
from audit_point_in_time_candidates import audit_point_in_time_candidates
from diagnose_real_trade_candle_overlap import diagnose
from match_historical_trades_to_ohlcvt import parse_member, aggregate
from verify_trade_candle_provenance import verify_open_boundary
from inventory_kraken_archive import EXPECTED_SHA256

MAX_OHLC_ARTIFACT = 80 * 1024 * 1024
MAX_TRADE_ARTIFACT = 12 * 1024 * 1024
MAX_MARKETS = 4
STEP = 300
HORIZONS = (1, 6, 24, 48)


def _open_inner(path, member, cap):
    path = Path(path)
    if path.stat().st_size > cap:
        raise ValueError("outer artifact exceeds cap")
    with zipfile.ZipFile(path) as outer:
        names = outer.namelist()
        if names == [member]:
            info = outer.getinfo(member)
            if info.file_size > cap or info.flag_bits & 1:
                raise ValueError("unsafe inner archive")
            payload = outer.read(info)
            return zipfile.ZipFile(io.BytesIO(payload))
        if "manifest.json" in names and len(names) <= 65:
            # GitHub CLI unpacks the outer Actions artifact to this inner ZIP.
            # Retained member SHA checks still apply; this is not a GitHub
            # artifact digest authentication claim.
            return zipfile.ZipFile(path)
    raise ValueError("unexpected artifact members")


def _manifest(archive):
    if archive.namelist().count("manifest.json") != 1:
        raise ValueError("missing or duplicate manifest")
    if archive.getinfo("manifest.json").file_size > 128 * 1024:
        raise ValueError("oversized manifest")
    return json.loads(archive.read("manifest.json"))


def _trade_zip(name, payload):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr(name, payload)
    return zipfile.ZipFile(io.BytesIO(buffer.getvalue()))


def _candidate_windows(timestamps):
    observed = set(timestamps)
    return {str(h): sum(all(t + i * STEP in observed for i in range(1, h * 12 + 1))
                        for t in observed) for h in HORIZONS}


def _bounded_sha256(path, cap):
    path = Path(path)
    if not path.is_file() or path.stat().st_size > cap:
        raise ValueError("missing or oversized input artifact")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()



def _validate_retained_ohlc(payload, meta):
    """Revalidate untrusted retained bytes and source-tail gap accounting.

    A retained SHA alone only binds bytes to a self-reported manifest; it does
    not prove source origin, trade completeness, or eligibility for labels.
    """
    if not isinstance(meta, dict):
        raise ValueError("invalid OHLC provenance metadata")
    rows = []
    previous = None
    gaps = missing = current = longest = 0
    try:
        decoded = payload.decode("utf-8", errors="strict")
        reader = csv.reader(io.StringIO(decoded))
        for raw in reader:
            if len(raw) != 7:
                raise ValueError("invalid retained OHLC column count")
            row = tuple(float(value) for value in raw)
            if not all(isfinite(value) for value in row):
                raise ValueError("nonfinite retained OHLC value")
            timestamp, opening, high, low, close, volume, count = row
            if (timestamp < 0 or not timestamp.is_integer() or
                    int(timestamp) % STEP or
                    (previous is not None and timestamp <= previous)):
                raise ValueError("invalid retained OHLC timestamp order")
            if (min(opening, high, low, close) <= 0 or
                    not low <= opening <= high or not low <= close <= high or
                    volume < 0 or count < 0 or not count.is_integer()):
                raise ValueError("invalid retained OHLC candle values")
            if previous is not None and timestamp > previous + STEP:
                gaps += 1
                missing += int((timestamp - previous) // STEP - 1)
                current = 0
            current += 1
            longest = max(longest, current)
            rows.append(row)
            if len(rows) > 8000:
                raise ValueError("retained OHLC row cap")
            previous = timestamp
    except (UnicodeError, OverflowError, TypeError) as exc:
        raise ValueError("invalid retained OHLC encoding or value") from exc
    if not rows:
        raise ValueError("empty retained OHLC evidence")
    keys = ("retained_rows", "source_rows", "retained_first_open",
            "retained_last_open", "source_gap_events",
            "source_missing_intervals", "source_longest_contiguous")
    if any(type(meta.get(key)) is not int for key in keys):
        raise ValueError("invalid source-tail provenance metadata")
    if (meta["retained_rows"] != len(rows) or
            meta["source_rows"] < len(rows) or
            meta["retained_first_open"] != int(rows[0][0]) or
            meta["retained_last_open"] != int(rows[-1][0]) or
            meta["source_longest_contiguous"] < longest or
            meta["source_longest_contiguous"] > meta["source_rows"]):
        raise ValueError("OHLC retained source-tail provenance mismatch")
    if (meta["source_gap_events"] < gaps or
            meta["source_missing_intervals"] < missing):
        raise ValueError("OHLC source gap floor mismatch")
    if meta["source_rows"] == len(rows) and (
            meta["source_gap_events"] != gaps or
            meta["source_missing_intervals"] != missing or
            meta["source_longest_contiguous"] != longest):
        raise ValueError("OHLC full-retention gap metadata mismatch")
    return rows, {"gap_events": gaps, "missing_intervals": missing,
                  "longest_contiguous": longest}


def reconcile(ohlc_artifact, trade_artifact, *, expected_ohlc_digest=None,
              expected_trade_digest=None):
    """Inspect genuine retained source bytes; all labels stay gated."""
    o_path, t_path = Path(ohlc_artifact), Path(trade_artifact)
    o_digest = _bounded_sha256(o_path, MAX_OHLC_ARTIFACT)
    t_digest = _bounded_sha256(t_path, MAX_TRADE_ARTIFACT)
    if (expected_ohlc_digest and o_digest != expected_ohlc_digest or
            expected_trade_digest and t_digest != expected_trade_digest):
        raise ValueError("GitHub artifact SHA256 mismatch")
    with _open_inner(o_path, "reusable_ohlc_evidence.zip", MAX_OHLC_ARTIFACT) as candles, \
         _open_inner(t_path, "bounded_independent_trade_members.zip", MAX_TRADE_ARTIFACT) as trades:
        om, tm = _manifest(candles), _manifest(trades)
        if (om.get("schema") != 1 or om.get("source_archive_sha256") != EXPECTED_SHA256
                or om.get("independent_trade_completeness") is not False
                or tm.get("schema_version") != 1
                or tm.get("source_archive_full_sha256_verified") is not False
                or tm.get("real_labels") != 0):
            raise ValueError("untrusted evidence manifest")
        markets = tm.get("markets")
        if not isinstance(markets, dict) or not 1 <= len(markets) <= MAX_MARKETS:
            raise ValueError("invalid trade cohort")
        if (len(set(candles.namelist())) != len(candles.namelist()) or
                len(set(trades.namelist())) != len(trades.namelist())):
            raise ValueError("duplicate evidence member")
        reports = {}
        for market, meta in sorted(markets.items()):
            if (not market.endswith(".csv") or "/" in market or "\\" in market
                    or ".." in market):
                raise ValueError("unsafe market name")
            o_name = market.replace(".csv", "_5.csv")
            if o_name not in om.get("markets", {}):
                raise ValueError("trade market missing from OHLC cohort")
            ti = trades.getinfo("trades/" + market)
            if ti.file_size > 3 * 1024 * 1024 or ti.flag_bits & 1:
                raise ValueError("unsafe trade member")
            trade_bytes = trades.read(ti)
            if (hashlib.sha256(trade_bytes).hexdigest() != meta.get("member_sha256")
                    or len(trade_bytes) != meta.get("member_bytes")
                    or meta.get("member_crc_verified") is not True):
                raise ValueError("trade member SHA or size mismatch")
            # Parser checks observed 7-column schema, unique IDs and timestamps.
            # schema_verified=True is a parser precondition, NOT source attestation.
            with _trade_zip(market, trade_bytes) as one:
                parsed = parse_member(one, market, schema_verified=True)
            oi = candles.getinfo("candles/" + o_name)
            if oi.file_size > 64 * 1024 * 1024 or oi.flag_bits & 1:
                raise ValueError("unsafe OHLC member")
            ohlc_bytes = candles.read(oi)
            ometa = om["markets"][o_name]
            if hashlib.sha256(ohlc_bytes).hexdigest() != ometa["retained_sha256"]:
                raise ValueError("OHLC retained member SHA mismatch")
            ohlc, validated_gaps = _validate_retained_ohlc(ohlc_bytes, ometa)
            diagnostic = diagnose(ohlc, parsed)
            _, buckets = aggregate(parsed)
            source = {int(row[0]): row for row in ohlc}
            exact = {ts for ts, records in buckets.items()
                     if ts in source and verify_open_boundary(
                         source[ts], records, independent_trade_source=True
                     )["status"] == "verified_open_boundary"}
            audit = audit_candidate_windows(ohlc, exact)
            feature_audit = audit_point_in_time_candidates(ohlc, exact)
            # Full-source gap metadata is comparable only when every source
            # row was retained. Otherwise retained-tail gap counts are a
            # separate bounded subset, not a replacement for source totals.
            if ometa["source_rows"] == len(ohlc):
                if (ometa.get("source_gap_events") != audit["ohlc_interior_gap_events"]
                        or ometa.get("source_missing_intervals") != audit["ohlc_interior_missing_intervals"]):
                    raise ValueError("OHLC full-retention gap metadata mismatch")
            candidate_windows = _candidate_windows(exact)
            if any(candidate_windows[str(h)] != audit["horizons"][str(h)]["candidate_full_future_windows"]
                   for h in HORIZONS):
                raise AssertionError("candidate window accounting disagrees")
            reports[market] = {
                "trade_rows": len(parsed), "trade_buckets": len(buckets),
                "retained_ohlc_rows": len(ohlc),
                "exact_trade_ohlc_candidate_intervals": len(exact),
                "mismatch_counts": diagnostic.get("mismatch_counts", {}),
                "candidate_contiguous_horizon_windows": candidate_windows,
                "candidate_outcome_audit": audit,
                "point_in_time_feature_audit": feature_audit,
                "verified_complete_intervals": 0, "real_labels": 0,
                "no_trade_or_source_gap_semantics": "unknown",
                "ohlc_retained_interior_gap_events": audit["ohlc_interior_gap_events"],
                "ohlc_retained_missing_no_trade_candidate_intervals": audit["ohlc_interior_missing_intervals"],
                "ohlc_documented_no_trade_semantics_reference": audit["ohlc_gap_documentation_url"],
                "ohlc_gap_semantics_authorize_labels": False,
                "retained_source_tail_contract_verified": True,
                "retained_ohlc_structure_validated": True,
                "retained_ohlc_gap_floor_verified": True,
                "retained_ohlc_longest_contiguous": validated_gaps["longest_contiguous"],
            }
    return {"schema_version": 1,
            "status": "descriptive_candidate_outcomes_source_completeness_unverified",
            "source_ohlc_archive_sha256_in_retained_manifest": EXPECTED_SHA256,
            "source_trade_archive_sha256_verified": False,
            "input_ohlc_zip_sha256": o_digest,
            "input_trade_zip_sha256": t_digest,
            "markets": reports, "real_labels": 0,
            "held_out_evaluation": "not_authorized", "production_modified": False}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--ohlc", required=True)
    p.add_argument("--trades", required=True)
    p.add_argument("--ohlc-digest")
    p.add_argument("--trade-digest")
    a = p.parse_args()
    print(json.dumps(reconcile(a.ohlc, a.trades,
                               expected_ohlc_digest=a.ohlc_digest,
                               expected_trade_digest=a.trade_digest), sort_keys=True))
