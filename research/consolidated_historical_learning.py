"""Consolidated isolated research: one archive download, one evidence report.

Real labels require independently verified complete trade-to-OHLC match. This
workflow deliberately does not treat synthetic tests or a source assertion as
proof. No production credentials, writes, or network calls beyond archive.
"""
import argparse
import csv
import hashlib
import io
import json
import tempfile
import zipfile
from pathlib import Path
from inventory_kraken_archive import download_verified, resource_gate, EXPECTED_SHA256
from verify_trade_candle_provenance import verify_open_boundary
from reconstruct_forward_outcomes import Candle, reconstruct_as_of

MAX_CSV_BYTES = 64 * 1024 * 1024
MAX_ROWS = 200000
MAX_REPORT_BYTES = 16384
HORIZONS = (1, 6, 24, 48)


def read_member(z, name):
    if not name.endswith("_5.csv") or "/" in name or "\\" in name:
        raise ValueError("invalid member name")
    matches = [x for x in z.infolist() if x.filename == name]
    if len(matches) != 1 or matches[0].file_size > MAX_CSV_BYTES:
        raise ValueError("missing duplicate or oversized member")
    result = []
    with z.open(matches[0]) as stream:
        for row in csv.reader(io.TextIOWrapper(stream, encoding="utf-8", newline="")):
            if len(result) >= MAX_ROWS or len(row) != 7:
                raise ValueError("invalid source row or cap")
            result.append(tuple(float(x) for x in row))
    if not result:
        raise ValueError("empty member")
    return result


def assess(rows, *, independent_trades=None, independent_trade_source=False,
           source_complete=False, min_quote_volume=0):
    """No labels until exact real trade boundary and source completeness pass."""
    result = {"status": "abstain_independent_trade_provenance",
              "timestamp_open_verified": False, "real_labels": 0,
              "horizons": {}, "historical_pattern_evaluation": "not_authorized"}
    if not independent_trade_source or not source_complete or independent_trades is None:
        return result
    candle = rows[0]
    if len(candle) != 7:
        return result
    proof = verify_open_boundary(candle, independent_trades, independent_trade_source=True)
    result["boundary_status"] = proof["status"]
    if proof["status"] != "verified_open_boundary":
        return result
    result["timestamp_open_verified"] = True
    candles = [Candle(int(r[0]), r[2], r[4], r[5]) for r in rows]
    outcome = reconstruct_as_of(candles, int(candle[0]) + 300,
                                source_timestamp_semantics="candle_open_utc",
                                min_quote_volume=min_quote_volume)
    result["status"] = outcome["status"]
    result["horizons"] = outcome.get("horizons", {})
    result["real_labels"] = sum(x.get("status") == "mature" for x in result["horizons"].values())
    # Do not claim historical patterns or prediction skill from one observation.
    return result


def run(output, *, member=None):
    output = Path(output)
    if output.exists():
        raise FileExistsError("refuse overwrite")
    with tempfile.TemporaryDirectory(prefix="kraken-consolidated-") as tmp:
        p = Path(tmp) / "archive.zip"
        verified = download_verified(p, resources=resource_gate(tmp))
        if verified["sha256"] != EXPECTED_SHA256 or not verified["integrity_verified"]:
            raise RuntimeError("archive identity mismatch")
        with zipfile.ZipFile(p) as z:
            choices = sorted(x.filename for x in z.infolist() if x.filename.endswith("_5.csv")
                             and "/" not in x.filename and x.file_size <= MAX_CSV_BYTES)
            if not choices:
                raise RuntimeError("no bounded member")
            selected = member or choices[0]
            if selected not in choices:
                raise ValueError("requested member unavailable")
            rows = read_member(z, selected)
        # The archive itself is NOT an independent trade feed.
        evidence = assess(rows)
        report = {"archive_sha256": verified["sha256"], "archive_bytes": verified["bytes"],
                  "member": selected, "member_rows": len(rows),
                  "member_first_timestamp": rows[0][0],
                  "member_last_timestamp": rows[-1][0],
                  "source_verified": True, "trade_source_verified": False,
                  "evaluation": evidence, "production_modified": False,
                  "next_gate": "complete independent real Kraken trade capture for an archive-matching interval"}
        payload = (json.dumps(report, sort_keys=True) + "\n").encode()
        if len(payload) > MAX_REPORT_BYTES:
            raise RuntimeError("report exceeds cap")
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as out:
            out.write(payload)
        return report


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--member")
    args = ap.parse_args()
    print(json.dumps(run(args.output, member=args.member), sort_keys=True))
