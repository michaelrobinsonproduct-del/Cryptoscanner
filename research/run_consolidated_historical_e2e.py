"""Single-run, isolated Kraken historical research pipeline.

Downloads each source once, keeps both ZIPs until all analysis completes, and
emits a single fail-closed report. No production connections or writes.
"""
import argparse
import csv
import hashlib
import io
import json
import math
import tempfile
import zipfile
from pathlib import Path

from acquire_kraken_historical_trades import download as download_trades, inspect as inspect_trades, resource_gate as trades_gate
from inventory_kraken_archive import download_verified as download_ohlc, resource_gate as ohlc_gate, EXPECTED_SHA256
from consolidated_historical_learning import read_member
from match_historical_trades_to_ohlcvt import aggregate, compare, parse_member
from reconstruct_forward_outcomes import Candle, reconstruct_as_of

TRADE_SHA256_OBSERVED = "4adddad07b0dbe11891a25137c1adfc11a9a5f63798680a6b88eae2b3a867cf9"
MAX_SAMPLE_ROWS = 250000
MAX_REPORT = 16384
HORIZONS = (1, 6, 24, 48)


def discover_schema(z, name):
    info = z.getinfo(name)
    if info.file_size > 64 * 1024 * 1024:
        raise RuntimeError("selected trade member exceeds bounded parser cap")
    with z.open(info) as raw:
        reader = csv.reader(io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline=""))
        rows = []
        for row in reader:
            if len(rows) == 3:
                break
            rows.append(row)
    if not rows or any(not row for row in rows):
        raise RuntimeError("empty source schema sample")
    return {"member": name, "columns": [len(x) for x in rows],
            "first_row_numeric": [is_number(x) for x in rows[0]],
            "sample_rows": len(rows)}


def is_number(value):
    try:
        return math.isfinite(float(value))
    except (ValueError, TypeError, OverflowError):
        return False


def candidate_trade_member(z, pair):
    name = pair + ".csv"
    matches = [x for x in z.infolist() if x.filename == name]
    if len(matches) != 1:
        raise RuntimeError("requested independent trade pair unavailable or duplicated")
    return name


def analyze(ohlc_z, trade_z, *, pair="0GEUR", schema_attested=False):
    """Never infer complete coverage merely from a ZIP or caller flag."""
    trade_name = candidate_trade_member(trade_z, pair)
    schema = discover_schema(trade_z, trade_name)
    result = {"pair": pair, "trade_csv_schema": schema,
              "timestamp_semantics": "not_independently_verified",
              "source_interval_completeness": "not_verified",
              "matched_candles": 0, "real_labels": 0,
              "held_out_evaluation": "not_authorized",
              "status": "abstain_pending_real_source_schema_and_completeness"}
    if schema["columns"] != [3, 3, 3] or not all(schema["first_row_numeric"]):
        result["status"] = "abstain_unknown_trade_csv_schema"
        return result
    # Parsing is a candidate, never an assertion of complete independent coverage.
    records = parse_member(trade_z, trade_name, schema_verified=True)
    result["trade_records_parsed"] = len(records)
    result["trade_first_timestamp"] = records[0][0]
    result["trade_last_timestamp"] = records[-1][0]
    if not (1710000000 < records[0][0] < 1800000000 and
            1710000000 < records[-1][0] < 1800000000):
        result["status"] = "abstain_trade_timestamp_range"
        return result
    ohlc_name = pair + "_5.csv"
    ohlc_rows = read_member(ohlc_z, ohlc_name)
    buckets, _ = aggregate(records)
    matching = [r for r in ohlc_rows if int(r[0]) in buckets]
    result["ohlc_rows_parsed"] = len(ohlc_rows)
    result["candidate_overlapping_candles"] = len(matching)
    result["comparison"] = compare(matching, records, independently_complete=False)
    result["status"] = "candidate_trade_and_ohlc_overlap_completeness_not_attested"
    return result


def run(output, *, pair="0GEUR"):
    output = Path(output)
    if output.exists():
        raise FileExistsError("refuse overwrite")
    with tempfile.TemporaryDirectory(prefix="kraken-historical-e2e-") as tmp:
        tmp = Path(tmp)
        ohlc_gate(tmp)
        trades_gate(tmp)
        trades_path = tmp / "trades.zip"
        ohlc_path = tmp / "ohlc.zip"
        trade_evidence = download_trades(trades_path)
        if trade_evidence["sha256_observed"] != TRADE_SHA256_OBSERVED:
            raise RuntimeError("trade archive identity changed since verified Phase 4")
        trade_meta = inspect_trades(trades_path)
        # Inspect actual source schema before spending 9GB on the OHLC archive.
        with zipfile.ZipFile(trades_path) as tz:
            trade_schema = discover_schema(tz, candidate_trade_member(tz, pair))
        if trade_schema["columns"] != [3, 3, 3] or not all(trade_schema["first_row_numeric"]):
            report = {"status": "blocked_unknown_real_trade_schema",
                      "trade_sha256_observed": trade_evidence["sha256_observed"],
                      "trade_archive_bytes": trade_evidence["bytes"],
                      "trade_csv_schema": trade_schema,
                      "archive_downloads_this_run": {"trade": 1, "ohlc": 0},
                      "real_labels": 0, "held_out_evaluation": "not_authorized",
                      "production_modified": False}
            payload = (json.dumps(report, sort_keys=True)+"\\n").encode()
            if len(payload) > MAX_REPORT:
                raise RuntimeError("report size cap")
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open("xb") as stream:
                stream.write(payload)
            return report
        ohlc_evidence = download_ohlc(ohlc_path, resources=ohlc_gate(tmp))
        if ohlc_evidence["sha256"] != EXPECTED_SHA256:
            raise RuntimeError("authenticated OHLC archive identity mismatch")
        with zipfile.ZipFile(trades_path) as tz, zipfile.ZipFile(ohlc_path) as oz:
            selected = pair + "_5.csv"
            if selected not in oz.namelist():
                raise RuntimeError("OHLC market member missing")
            # Bounded inspection; full rows are read only after schema verification.
            analysis = analyze(oz, tz, pair=pair)
            analysis["ohlc_member"] = selected
            analysis["ohlc_member_bytes"] = oz.getinfo(selected).file_size
        report = {"status": "completed_source_acquisition_evaluation_gated",
                  "trade_source": "official_kraken_2026q2_trade_zip",
                  "trade_sha256_observed": trade_evidence["sha256_observed"],
                  "trade_archive_bytes": trade_evidence["bytes"],
                  "trade_members": trade_meta["members"],
                  "ohlc_sha256_authenticated": ohlc_evidence["sha256"],
                  "ohlc_archive_bytes": ohlc_evidence["bytes"],
                  "analysis": analysis,
                  "archive_downloads_this_run": {"trade": 1, "ohlc": 1},
                  "source_data_retained_until_analysis_completed": True,
                  "independent_trade_digest_published": False,
                  "production_modified": False}
        payload = (json.dumps(report, sort_keys=True)+"\n").encode()
        if len(payload) > MAX_REPORT:
            raise RuntimeError("report size cap")
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as stream:
            stream.write(payload)
        return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--pair", default="0GEUR")
    args = parser.parse_args()
    print(json.dumps(run(args.output, pair=args.pair), sort_keys=True))
