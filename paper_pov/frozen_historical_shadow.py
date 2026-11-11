"""Frozen Kraken Q3 historical challenger, evaluated prospectively on paper WATCHs.

Read-only. Does not write canonical ledger or change published production scores.
Predictions older than the historical training cutoff are not considered
prospective. Missing past features/complete forward candles remain abstentions.
"""
import argparse
import datetime as dt
import hashlib
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path

from .shadow_learning_evidence import utc_time, canonical_digest

NAMES = ("momentum_5m", "momentum_15m", "momentum_60m",
         "volume_accel", "trade_accel", "volatility_60m")
UTC = dt.timezone.utc
BAR = dt.timedelta(minutes=5)
MAX_LAG = dt.timedelta(minutes=10)


def frozen_model(data):
    if data.get("schema") != "kraken_q3_frozen_shadow_v1":
        raise ValueError("Unrecognized frozen model source")
    stored = data.get("version")
    digest = hashlib.sha256(json.dumps({k: v for k, v in data.items()
                                       if k != "version"},
                                      sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if stored != digest:
        raise ValueError("Frozen historical challenger digest mismatch")
    if data.get("promotion_authorized") is not False or data.get("production_applied") is not False:
        raise ValueError("Refusing promoted historical model")
    m = data["training"]
    if m.get("status") != "SHADOW_ONLY" or tuple(m.get("feature_names", [])) != NAMES:
        raise ValueError("Frozen training feature contract mismatch")
    for name in NAMES:
        if any(name not in m[k] for k in ("means", "scales", "weights")):
            raise ValueError("Frozen feature missing")
        if m["scales"][name] <= 0 or not all(
                math.isfinite(float(m[k][name])) for k in ("means", "scales", "weights")):
            raise ValueError("Invalid frozen feature scale")
    return m


def completed_candles(data):
    per_pair = defaultdict(dict)
    for item in data.get("results", []):
        pair = item["pair"]
        for candle in item["candles"]:
            if candle["pair"] != pair:
                raise ValueError("Cross-market candle")
            moment = utc_time(candle["timestamp_utc"])
            if moment in per_pair[pair] and per_pair[pair][moment] != candle:
                raise ValueError("Conflicting Kraken candle")
            per_pair[pair][moment] = candle
    return {pair: sorted(((t, c) for t, c in rows.items()), key=lambda x: x[0])
            for pair, rows in per_pair.items()}


def features_at_entry(observations, entry):
    prev = [(time, row) for time, row in observations if time <= entry]
    if len(prev) < 13 or entry - prev[-1][0] > MAX_LAG:
        return None
    window = prev[-13:]
    if any(window[i][0] - window[i-1][0] != BAR for i in range(1, len(window))):
        return None
    bars = [row for _, row in window]
    if any("trades" not in row or not isinstance(row["trades"], (int, float))
           for row in bars):
        return None
    try:
        close = [float(row["close"]) for row in bars]
        vol = [float(row["volume"]) for row in bars]
        trades = [float(row["trades"]) for row in bars]
        if not all(math.isfinite(x) and x >= 0 for x in (*vol, *trades)):
            return None
        if not all(math.isfinite(x) and x > 0 for x in close):
            return None
        oldv, newv = sum(vol[:6]), sum(vol[6:12])
        oldt, newt = sum(trades[:6]), sum(trades[6:12])
        if oldv <= 0 or oldt <= 0:
            return None
        returns = [close[i] / close[i-1]-1 for i in range(1, 13)]
        return {
            "momentum_5m": close[-1]/close[-2]-1,
            "momentum_15m": close[-1]/close[-4]-1,
            "momentum_60m": close[-1]/close[0]-1,
            "volume_accel": min(100, newv/oldv),
            "trade_accel": min(100, newt/oldt),
            "volatility_60m": statistics.pstdev(returns),
        }
    except (ValueError, TypeError, ZeroDivisionError):
        return None


def observed_close_label(observations, entry, entry_price, hours, evaluated_at):
    """Only closed, complete future 5m bars fully after the prediction count."""
    if entry + dt.timedelta(hours=hours) > evaluated_at:
        return None
    if not math.isfinite(entry_price) or entry_price <= 0:
        return None
    floor = entry.replace(second=0, microsecond=0)
    floor -= dt.timedelta(minutes=floor.minute % 5)
    first = floor + (BAR if entry == floor else 2*BAR)
    target = entry + dt.timedelta(hours=hours)
    last = target.replace(second=0, microsecond=0)
    last -= dt.timedelta(minutes=last.minute % 5)
    expected = int((last-first)/BAR) + 1
    if expected <= 0:
        return None
    samples = [(t, float(r["close"])) for t, r in observations if first <= t <= last]
    if len(samples) != expected or samples[0][0] != first or samples[-1][0] != last:
        return None
    if any(samples[i][0]-samples[i-1][0] != BAR for i in range(1,len(samples))):
        return None
    return max(close for _, close in samples)/entry_price - 1


def _top_by_run(rows, key):
    by_run = defaultdict(list)
    for row in rows:
        by_run[row["run_id"]].append(row)
    return {run: sorted(v, key=lambda row: (-row[key], row["pair"], row["prediction_id"]))[0]
            for run, v in by_run.items()}


def prospectively_evaluate(ledger, observations, model_source, *, evaluated_at_utc):
    model = frozen_model(model_source)
    candles = completed_candles(observations)
    now = utc_time(evaluated_at_utc)
    train_end = utc_time(model_source["training_window_end"])
    eligible = []
    excluded = defaultdict(int)
    for p in ledger.get("predictions", []):
        entry_text = p.get("entry_utc") or p.get("as_of")
        if not entry_text or not p.get("pair") or not p.get("prediction_id"):
            excluded["MALFORMED_PREDICTION"] += 1
            continue
        entry = utc_time(entry_text)
        if entry <= train_end + dt.timedelta(hours=48):
            excluded["NOT_PROSPECTIVE"] += 1
            continue
        history = candles.get(p["pair"], [])
        features = features_at_entry(history, entry)
        if features is None:
            excluded["NO_COMPLETE_ASOF_FEATURES"] += 1
            continue
        if p.get("baseline_score") is None:
            excluded["NO_BASELINE_SCORE"] += 1
            continue
        price = float(p.get("entry_price") or p.get("price") or 0)
        if not math.isfinite(price) or price <= 0:
            excluded["INVALID_ENTRY_PRICE"] += 1
            continue
        score = sum((features[f]-model["means"][f])/model["scales"][f]
                    * model["weights"][f] for f in NAMES)
        label = observed_close_label(history, entry, price, 48, now)
        eligible.append({
            "prediction_id": p["prediction_id"], "run_id": p["run_id"],
            "pair": p["pair"], "entry_utc": entry.isoformat(),
            "baseline_score": float(p["baseline_score"]),
            "historical_proxy_momentum": abs(features["momentum_60m"]),
            "frozen_shadow_score": score, "features": features,
            "complete_48h_close_label": label,
            "hit30": label >= .30 if label is not None else None,
            "watch_authorized": False,
        })
    base = _top_by_run(eligible, "baseline_score")
    shadow = _top_by_run(eligible, "frozen_shadow_score")
    shared = sorted(set(base) & set(shadow))
    paired = [run for run in shared if base[run]["hit30"] is not None
              and shadow[run]["hit30"] is not None]
    b = [base[run] for run in paired]
    s = [shadow[run] for run in paired]
    summary = {
        "schema": "prospective_q3_shadow_v1",
        "model_version": model_source["version"],
        "model_source_zip_sha256": model_source["source_zip_sha256"],
        "evaluated_at_utc": now.isoformat(),
        "eligible_scored_watchs": len(eligible),
        "excluded": dict(sorted(excluded.items())),
        "paired_complete_scan_count": len(paired),
        "baseline_hits30": sum(x["hit30"] for x in b),
        "shadow_hits30": sum(x["hit30"] for x in s),
        "baseline_only_hit_scans": sum(x["hit30"] and not y["hit30"] for x,y in zip(b,s)),
        "shadow_only_hit_scans": sum(y["hit30"] and not x["hit30"] for x,y in zip(b,s)),
        "unmatured_or_incomplete_scan_count": len(shared)-len(paired),
        "risk": "HIGH_UNVALIDATED", "confidence": "NOT_CALIBRATED",
        "source_authenticated": False, "measured_lift_verified": False,
        "live_scoring_changed": False, "promotion_authorized": False,
        "production_applied": False,
        "limitations": [
            "Only live WATCH predictions are scored, not the full as-of Kraken universe",
            "Historical model was trained on Q3 hourly top12 notional-selected markets",
            "Future +30% target uses complete five-minute CLOSES, not executable fills",
            "Future candles are source-observed but not independently authenticated archive",
            "Comparisons require identical matured scans and cannot imply reliable lift",
        ],
    }
    summary["source_digest"] = canonical_digest(summary)
    return summary


def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("ledger_json",type=Path)
    p.add_argument("rolling_candles_json",type=Path)
    p.add_argument("frozen_model_json",type=Path)
    p.add_argument("--output",required=True,type=Path)
    args=p.parse_args(argv)
    result=prospectively_evaluate(json.loads(args.ledger_json.read_text()),
        json.loads(args.rolling_candles_json.read_text()),
        json.loads(args.frozen_model_json.read_text()),
        evaluated_at_utc=dt.datetime.now(UTC).isoformat())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({key:result[key] for key in (
        "model_version","eligible_scored_watchs","paired_complete_scan_count",
        "baseline_hits30","shadow_hits30","excluded")},sort_keys=True))
    return result


if __name__=="__main__":
    main()
