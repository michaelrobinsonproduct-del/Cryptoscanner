"""Bounded, fail-closed readiness audit of retained Kraken OHLC evidence.

Source OHLCVT candle-open timestamps are NOT first-observed-at timestamps.
Verified retained rows are descriptive only: zero authenticated first-entry
episodes until independent trade completeness and decision-time features exist.
No network, ledger, production, model or scoring writes.
"""
import argparse
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

ARCHIVE_SHA = "fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4"
MAX_ARTIFACT = 80 * 1024 * 1024
MAX_MEMBER = 64 * 1024 * 1024
MAX_MARKETS = 64
MAX_ROWS = 8000
HORIZONS = (1, 6, 24, 48)
STEP = 300


def _positive_number(value):
    try:
        d = Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("invalid OHLCVT decimal") from None
    if not d.is_finite():
        raise ValueError("nonfinite OHLCVT")
    return d


def inspect_retained(path, *, expected_archive_sha=ARCHIVE_SHA):
    """Hash-check retained members, count uninterrupted candidate windows.

    A retained member hash does not reauthenticate the original 9GB ZIP,
    establish completeness of independent trades, or provide observation time.
    """
    path = Path(path)
    if path.stat().st_size > MAX_ARTIFACT:
        raise ValueError("oversized retained artifact")
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(set(names)) != len(names) or "manifest.json" not in names:
            raise ValueError("duplicate or missing manifest")
        manifest_info = archive.getinfo("manifest.json")
        if manifest_info.file_size > 1024 * 1024:
            raise ValueError("oversized manifest")
        manifest = json.loads(archive.read(manifest_info))
        if (manifest.get("schema") != 1
                or manifest.get("source_archive_sha256") != expected_archive_sha
                or manifest.get("real_labels") != 0
                or manifest.get("independent_trade_completeness") is not False
                or manifest.get("source_timestamp_semantics") != "candle_open_candidate"
                or manifest.get("held_out_evaluation") != "not_authorized"):
            raise ValueError("untrusted retained provenance or promoted labels")
        markets = manifest.get("markets")
        if not isinstance(markets, dict) or not 1 <= len(markets) <= MAX_MARKETS:
            raise ValueError("invalid market inventory")
        if set(names) != {"manifest.json"} | {"candles/" + n for n in markets}:
            raise ValueError("unexpected or missing retained member")
        per_market = {}
        totals = {str(h): 0 for h in HORIZONS}
        total_rows = 0
        for name in sorted(markets):
            if not re.fullmatch(r"[A-Za-z0-9]+_5\.csv", name):
                raise ValueError("unsafe retained member")
            meta = markets[name]
            info = archive.getinfo("candles/" + name)
            if info.file_size > MAX_MEMBER or info.flag_bits & 1:
                raise ValueError("unsafe retained member size or encryption")
            payload = archive.read(info)
            if hashlib.sha256(payload).hexdigest() != meta.get("retained_sha256"):
                raise ValueError("retained member SHA256 mismatch")
            previous = None
            first = None
            count = 0
            spans = []
            span = 0
            for row in csv.reader(io.StringIO(payload.decode("utf-8", errors="strict"))):
                if len(row) != 7:
                    raise ValueError("invalid OHLCVT columns")
                ts, op, hi, lo, cl, volume, trades = map(_positive_number, row)
                if (ts != int(ts) or int(ts) % STEP
                        or (previous is not None and ts <= previous)
                        or min(op, hi, lo, cl) <= 0
                        or lo > min(op, cl) or hi < max(op, cl)
                        or volume < 0 or trades < 0 or trades != int(trades)):
                    raise ValueError("invalid OHLCVT row")
                t = int(ts)
                if previous is not None and t != previous + STEP:
                    spans.append(span)
                    span = 0
                span += 1
                previous = t
                first = t if first is None else first
                count += 1
                if count > MAX_ROWS:
                    raise ValueError("retained row cap exceeded")
            if count == 0:
                raise ValueError("empty retained member")
            spans.append(span)
            if (meta.get("retained_rows") != count
                    or meta.get("retained_first_open") != first
                    or meta.get("retained_last_open") != previous):
                raise ValueError("retained metadata mismatch")
            windows = {str(h): sum(max(0, n - h * 12) for n in spans)
                       for h in HORIZONS}
            for h, n in windows.items():
                totals[h] += n
            per_market[name] = {"retained_rows": count,
                                "contiguous_segments": len(spans),
                                "candidate_windows": windows,
                                "authenticated_first_entry_episodes": 0}
            total_rows += count
    return {
        "status": "RETAINED_OHLC_VERIFIED_HISTORICAL_LABELS_BLOCKED",
        "source_archive_sha256_claim": expected_archive_sha,
        "full_source_archive_reverified_this_run": False,
        "retained_member_hashes_verified": True,
        "markets": len(per_market),
        "retained_rows": total_rows,
        "candidate_windows": totals,
        "authenticated_first_entry_episodes": 0,
        "source_timestamp_semantics": "candle_open_candidate",
        "has_first_observed_at": False,
        "independent_trade_completeness": False,
        "held_out_lift": None,
        "production_applied": False,
        "missing_for_authenticated_learning": [
            "source_authenticated_complete_trade_paths",
            "quote_event_and_first_observed_timestamps",
            "as_of_entry_bid_ask_spread_depth_volume",
            "independent_first_entry_positive_negative_episodes",
        ],
        "per_market": per_market,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--retained-zip", required=True)
    parser.add_argument("--expected-archive-sha", default=ARCHIVE_SHA)
    parser.add_argument("--output")
    args = parser.parse_args()
    report = inspect_retained(args.retained_zip, expected_archive_sha=args.expected_archive_sha)
    payload = json.dumps(report, sort_keys=True, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
