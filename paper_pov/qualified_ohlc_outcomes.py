"""Read-only 5m closed-bar outcome reconstruction; never certify source authenticity."""
import datetime as dt
import hashlib
import json
import math
import argparse
from pathlib import Path
from .scanner import utc, atomic_json

HORIZONS = (1, 6, 24, 48)
STEP = dt.timedelta(minutes=5)
UTC = dt.timezone.utc


def positive(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise ValueError("Invalid numeric bar")
    n = float(x)
    if not math.isfinite(n) or n <= 0:
        raise ValueError("Invalid OHLC price")
    return n


def reconstruct(prediction, bars, *, observed_until, source_sha256):
    if not isinstance(source_sha256, str) or len(source_sha256) != 64 or any(
            c not in "0123456789abcdef" for c in source_sha256):
        raise ValueError("Missing source digest")
    if prediction.get("status") != "PAPER_WATCH":
        raise ValueError("Only paper WATCH predictions accepted")
    as_of = utc(prediction["as_of"])
    until = utc(observed_until)
    indexed = {}
    previous = None
    for bar in bars:
        at = utc(bar["open_at"])
        if int(at.timestamp()) % 300 or (previous is not None and at <= previous):
            raise ValueError("Unaligned, duplicate or unordered 5m bars")
        op, high, low, close = [positive(bar[k]) for k in ("open", "high", "low", "close")]
        if low > min(op, close) or high < max(op, close):
            raise ValueError("Inconsistent OHLC bar")
        indexed[at] = (op, high, low, close)
        previous = at
    entry_at = dt.datetime.fromtimestamp(
        (int(as_of.timestamp()) // 300 + 1) * 300, UTC)
    entry = indexed.get(entry_at)
    labels = []
    for hours in HORIZONS:
        target = entry_at + dt.timedelta(hours=hours)
        row = {"horizon_hours": hours, "target_at": target.isoformat()}
        if entry is None or entry_at + STEP > until:
            row.update(status="ABSTAIN_ENTRY", reason="Next closed entry bar missing")
        elif target > until:
            row.update(status="ABSTAIN_IMMATURE", reason="Horizon incomplete")
        else:
            count = int((target - entry_at) / STEP)
            forward = [indexed.get(entry_at + i * STEP) for i in range(1, count + 1)]
            if any(x is None for x in forward):
                row.update(status="ABSTAIN_GAP", reason="Missing required 5m interval")
            else:
                price = entry[0]
                peak = max(x[1] for x in forward)
                final = forward[-1][3]
                row.update(
                    status="MATURED_OBSERVED", entry_at=entry_at.isoformat(),
                    entry_price=price, final_close=final,
                    observed_peak_pct=round(100 * (peak / price - 1), 4),
                    return_pct=round(100 * (final / price - 1), 4),
                    observed_30pct_hit=peak >= 1.3 * price,
                    qualified_for_learning=False,
                    reason="Source authentication and executable liquidity not established")
        labels.append(row)
    return {
        "schema": "qualified_ohlc_outcomes_v1",
        "prediction_id": prediction["prediction_id"],
        "pair": prediction["pair"], "as_of": as_of.isoformat(),
        "source_sha256": source_sha256, "source_authenticated": False,
        "entry_method": "next_5m_bar_open_proxy",
        "labels": labels,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    raw = Path(args.input).read_bytes()
    payload = json.loads(raw)
    result = reconstruct(payload["prediction"], payload["bars"],
                         observed_until=payload["observed_until"],
                         source_sha256=hashlib.sha256(raw).hexdigest())
    atomic_json(args.output, result)
    print(json.dumps({"statuses": [x["status"] for x in result["labels"]],
                      "source_authenticated": False}, sort_keys=True))


if __name__ == "__main__":
    main()
