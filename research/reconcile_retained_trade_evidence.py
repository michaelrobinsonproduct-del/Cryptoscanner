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
from pathlib import Path

from audit_trade_candidate_windows import audit_candidate_windows
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
            ohlc = [tuple(float(v) for v in row) for row in
                    csv.reader(io.StringIO(ohlc_bytes.decode("utf-8", errors="strict")))]
            if not ohlc or len(ohlc) != ometa["retained_rows"] or len(ohlc) > 8000:
                raise ValueError("OHLC retained row count mismatch")
            # The original builder retains the final N *unfiltered* source
            # rows. Check that contract before interpreting interior absent
            # timestamps as documented no-trade candles. Never extrapolate
            # before the first or after the last retained source observation.
            if (type(ometa.get("source_rows")) is not int
                    or ometa["source_rows"] < len(ohlc)
                    or type(ometa.get("retained_first_open")) is not int
                    or type(ometa.get("retained_last_open")) is not int
                    or int(ohlc[0][0]) != ometa["retained_first_open"]
                    or int(ohlc[-1][0]) != ometa["retained_last_open"]):
                raise ValueError("OHLC retained source-tail provenance mismatch")
            diagnostic = diagnose(ohlc, parsed)
            _, buckets = aggregate(parsed)
            source = {int(row[0]): row for row in ohlc}
            exact = {ts for ts, records in buckets.items()
                     if ts in source and verify_open_boundary(
                         source[ts], records, independent_trade_source=True
                     )["status"] == "verified_open_boundary"}
            audit = audit_candidate_windows(ohlc, exact)
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
                "verified_complete_intervals": 0, "real_labels": 0,
                "no_trade_or_source_gap_semantics": "unknown",
                "ohlc_retained_interior_gap_events": audit["ohlc_interior_gap_events"],
                "ohlc_retained_missing_no_trade_candidate_intervals": audit["ohlc_interior_missing_intervals"],
                "ohlc_documented_no_trade_semantics_reference": audit["ohlc_gap_documentation_url"],
                "ohlc_gap_semantics_authorize_labels": False,
                "retained_source_tail_contract_verified": True,
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
