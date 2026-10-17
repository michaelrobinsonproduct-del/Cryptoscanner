"""Train adaptive research challenger on matured outcomes; production stays gated."""
import datetime as dt
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

def evaluate_market_misses(con):
    """Learn market-wide screening thresholds from matured 1h observations.

    Training and later holdout are split by timestamp, never by random row.
    This learner cannot change production filters until forward proof exists.
    """
    tables = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if not {"market_signals", "market_observations", "snapshots"}.issubset(tables):
        return {"status": "AWAITING_MARKET_FEATURES", "samples": 0}
    rows = con.execute("""SELECT s.run_at,s.pair,s.move24_pct,s.spread_bps,s.notional_24h_usd,
        (SELECT 100*(o.price/m.price-1) FROM market_observations o
         WHERE o.pair=s.pair AND o.run_at>=datetime(s.run_at,'+1 hour')
           AND o.run_at<datetime(s.run_at,'+2 hours')
         ORDER BY o.run_at LIMIT 1) AS return_pct
        FROM market_signals s JOIN market_observations m
          ON m.run_at=s.run_at AND m.pair=s.pair
        WHERE s.run_at < datetime('now','-2 hours')
        ORDER BY s.run_at DESC LIMIT 12000""").fetchall()
    rows = [r for r in rows if r[5] is not None and all(math.isfinite(float(x)) for x in r[2:])]
    rows.sort(key=lambda r:(r[0],r[1]))
    positives = sum(r[5]>=5 for r in rows)
    report = {"status":"INSUFFICIENT_MARKET_OUTCOMES","samples":len(rows),"breakouts":positives}
    times=sorted({r[0] for r in rows})
    if len(rows)<1200 or positives<15 or len(times)<20:
        return report
    cutoff=times[int(len(times)*.7)]
    train=[r for r in rows if r[0]<cutoff]
    test=[r for r in rows if r[0]>=cutoff]
    def evaluate_rule(group, rule):
        tp=fp=fn=0
        for r in group:
            selected=rule(r)
            breakout=r[5]>=5
            tp+=bool(selected and breakout)
            fp+=bool(selected and not breakout)
            fn+=bool(not selected and breakout)
        return {"recall":round(tp/max(1,tp+fn),4),"precision":round(tp/max(1,tp+fp),4),
                "true_positives":tp,"false_positives":fp,"missed_breakouts":fn}
    baseline=lambda r: .25<=r[2]<=12 and r[3]<=45 and r[4]>=100000
    # Small, interpretable threshold grid; no holdout tuning.
    trials=[]
    for minimum_move in (-5, -2, 0, .25):
        for max_spread in (45, 75, 125):
            for min_notional in (25000,50000,100000):
                rule=lambda r,mm=minimum_move,ms=max_spread,mn=min_notional: mm<=r[2]<=12 and r[3]<=ms and r[4]>=mn
                metrics=evaluate_rule(train,rule)
                trials.append((metrics["recall"]-.00001*metrics["false_positives"],minimum_move,max_spread,min_notional,metrics))
    _,mm,ms,mn,train_metrics=max(trials,key=lambda x:x[0])
    learned=lambda r:mm<=r[2]<=12 and r[3]<=ms and r[4]>=mn
    report.update({"status":"MARKET_MISS_MODEL_EVALUATED",
                   "learned_filter":{"min_move24_pct":mm,"max_spread_bps":ms,"min_notional_usd":mn},
                   "train":train_metrics,"holdout":evaluate_rule(test,learned),
                   "baseline_holdout":evaluate_rule(test,baseline),
                   "production_adopted":False,
                   "promotion_reason":"Prospective validation and executable-liquidity checks pending"})
    return report

def evaluate(db_path):
    con = sqlite3.connect(f"file:{Path(db_path).resolve()}?mode=ro", uri=True)
    try:
        rows = con.execute("""SELECT f.run_at,f.pair,f.move_15m_pct,f.volume_accel,f.base_score,o.return_pct
            FROM candidate_features f JOIN outcomes o ON f.run_at=o.run_at AND f.pair=o.pair
            WHERE o.horizon_hours=1 AND f.move_15m_pct IS NOT NULL AND f.volume_accel IS NOT NULL
            ORDER BY f.run_at,f.pair""").fetchall()
        has_observations = con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='market_observations'").fetchone()
        missed = con.execute("SELECT COUNT(*) FROM market_observations").fetchone()[0] if has_observations else 0
        market_miss_model = evaluate_market_misses(con)
        # Audited misses: full-market observed jumps not present in watch snapshots.
        # Restrict to the last seven days and consecutive observations <=90m.
        miss_examples = []
        if has_observations and con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='snapshots'").fetchone():
            miss_examples = con.execute("""WITH sequence AS (
                SELECT pair,run_at,price,
                       LEAD(run_at) OVER (PARTITION BY pair ORDER BY run_at) next_at,
                       LEAD(price) OVER (PARTITION BY pair ORDER BY run_at) next_price
                FROM market_observations WHERE run_at >= ?
            )
            SELECT q.pair,q.run_at,ROUND(100*(q.next_price/q.price-1),2)
            FROM sequence q WHERE q.next_price >= q.price*1.05
              AND (julianday(q.next_at)-julianday(q.run_at))*1440 BETWEEN 0 AND 90
              AND NOT EXISTS (SELECT 1 FROM snapshots s WHERE s.run_at=q.run_at AND s.pair=q.pair)
            ORDER BY (q.next_price/q.price) DESC LIMIT 20
            """, ((dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=7)).isoformat(),)).fetchall()

    finally:
        con.close()
    result = {"mode": "SHADOW_ONLY", "samples": len(rows), "min_train": MIN_TRAIN,
              "min_test": MIN_TEST, "live_weights_modified": False, "buy_approved": False,
              "status": "INSUFFICIENT_DATA", "market_observations_total": missed,
              "missed_breakout_examples": [{"pair": p, "observed_at": t, "gain_pct": g}
                                            for p, t, g in miss_examples],
              "misses_included_in_weight_training": False,
              "market_miss_model": market_miss_model}
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
