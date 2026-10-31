"""Descriptive OHLC peak-window audit; NOT validated point-in-time labels.

Source OHLC candle-open semantics and independent trade completeness remain
unverified. Results cannot be used for scoring, held-out performance or trades.
"""
import argparse
from collections import deque
import csv
import io
import json
import zipfile

from build_reusable_ohlc_evidence import inspect, _validate, HORIZONS, STEP


def _peak_windows(segment, width):
    """Count complete windows and future-high >=30% entry-close observations."""
    high = [x[1] for x in segment]
    close = [x[2] for x in segment]
    queue = deque()
    total = hits = 0
    for i in range(len(segment) - 1, -1, -1):
        while queue and queue[0] > i + width:
            queue.popleft()
        if i + 1 < len(segment):
            while queue and high[queue[-1]] <= high[i + 1]:
                queue.pop()
            queue.append(i + 1)
        if i + width < len(segment):
            total += 1
            if high[queue[0]] >= close[i] * 1.30:
                hits += 1
    return total, hits


def audit(path, *, expected_archive_sha256):
    coverage = inspect(path, expected_archive_sha256=expected_archive_sha256)
    result = {}
    with zipfile.ZipFile(path) as source:
        manifest = json.loads(source.read("manifest.json"))
        for name in sorted(manifest["markets"]):
            payload = source.read("candles/" + name)
            segments = []
            segment = []
            previous = None
            for row in csv.reader(io.StringIO(payload.decode("utf-8"))):
                ts = _validate(row, previous)
                if previous is not None and ts != previous + STEP:
                    segments.append(segment)
                    segment = []
                segment.append((ts, float(row[2]), float(row[4])))
                previous = ts
            if segment:
                segments.append(segment)
            windows = {}
            for h in HORIZONS:
                counts = [_peak_windows(seg, h * 12) for seg in segments]
                total = sum(x[0] for x in counts)
                hits = sum(x[1] for x in counts)
                if total != coverage["coverage"][name]["candidate_windows"][str(h)]:
                    raise ValueError("descriptive window coverage mismatch")
                windows[str(h)] = {"complete_ohlc_windows": total,
                                   "unverified_peak_30_windows": hits}
            result[name] = windows
    return {"status": "descriptive_ohlc_only_no_validated_outcomes",
            "source_archive_sha256": expected_archive_sha256,
            "markets": len(result), "per_market": result,
            "independent_trade_completeness": False,
            "source_timestamp_semantics": "candle_open_candidate",
            "real_labels": 0, "held_out_evaluation": "not_authorized",
            "production_modified": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--expected-sha256", required=True)
    args = parser.parse_args()
    print(json.dumps(audit(args.evidence, expected_archive_sha256=args.expected_sha256),
                     sort_keys=True))
