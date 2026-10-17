"""Train adaptive research challenger on matured outcomes; production stays gated."""
import json
import math
import os
import sqlite3
from pathlib import Path

MIN_TRAIN = 100
MIN_TEST = 40
WEIGHTS = (0, 1, 2, 3, 5, 8)
VOLUME_WEIGHTS = (0, 2, 4, 6, 10, 15)

def score(row, momentum, volume):
    return row[4] + max(-25, min(25, row[2] * momentum)) + max(-15, min(15, (row[3] - 1) * volume))

def compare(rows, momentum, volume):
    grouped = {}
    for row in rows:
        grouped.setdefault(row[0], []).append(row)
    base, candidate = [], []
    for cohort in grouped.values():
        base.append(max(cohort, key=lambda r: r[4])[5])
        candidate.append(max(cohort, key=lambda r: score(r, momentum, volume))[5])
    n = len(base)
    return {"cohorts": n, "base_avg_pct": round(sum(base) / n, 4),
            "challenger_avg_pct": round(sum(candidate) / n, 4),
            "delta_pct": round((sum(candidate) - sum(base)) / n, 4)}

def evaluate(db_path):
    con = sqlite3.connect(f"file:{Path(db_path).resolve()}?mode=ro", uri=True)
    try:
        rows = con.execute("""SELECT f.run_at,f.pair,f.move_15m_pct,f.volume_accel,f.base_score,o.return_pct
            FROM candidate_features f JOIN outcomes o ON f.run_at=o.run_at AND f.pair=o.pair
            WHERE o.horizon_hours=1 AND f.move_15m_pct IS NOT NULL AND f.volume_accel IS NOT NULL
            ORDER BY f.run_at,f.pair""").fetchall()
        missed = con.execute("""SELECT COUNT(*) FROM market_observations m
            WHERE m.run_at >= datetime('now','-7 days')""").fetchone()[0]
    finally:
        con.close()
    result = {"mode": "SHADOW_ONLY", "samples": len(rows), "min_train": MIN_TRAIN,
              "min_test": MIN_TEST, "live_weights_modified": False, "buy_approved": False,
              "status": "INSUFFICIENT_DATA", "market_observations_recent": missed}
    times = sorted({r[0] for r in rows})
    if len(rows) < MIN_TRAIN + MIN_TEST or len(times) < 12:
        return result
    cut = times[max(1, int(len(times) * .7))]
    train = [r for r in rows if r[0] < cut]
    holdout = [r for r in rows if r[0] >= cut]
    if len(train) < MIN_TRAIN or len(holdout) < MIN_TEST:
        return result
    # Only training rows determine the weights. Later holdout is never used to tune.
    trials = [(compare(train, m, v)["delta_pct"], m, v)
              for m in WEIGHTS for v in VOLUME_WEIGHTS]
    gain, m, v = max(trials, key=lambda x: (x[0], -x[1], -x[2]))
    result.update({"status": "ADAPTIVE_SHADOW_EVALUATED",
                   "learned_weights": {"momentum": m, "volume": v},
                   "training_candidates": len(trials),
                   "train": compare(train, m, v),
                   "holdout": compare(holdout, m, v),
                   "promotion_eligible": False,
                   "promotion_reason": "Needs independent forward multi-horizon proof and missed-breakout recall validation"})
    return result

def main():
    folder = Path(os.getenv("SIMPLE_SCANNER_DATA_DIR", "simple_scanner/output"))
    report = evaluate(folder / "history.sqlite3")
    target = folder / "shadow_learning.json"
    tmp = folder / "shadow_learning.json.tmp"
    tmp.write_text(json.dumps(report, indent=2))
    tmp.replace(target)
    print("SHADOW_LEARNING", json.dumps(report), flush=True)

if __name__ == "__main__":
    main()
