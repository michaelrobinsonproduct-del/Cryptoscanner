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

def early_accumulation_rank(rows, asset_pairs=None):
    """Rank current market observations using only information available at scan time.

    Input: (pair, move24_pct, spread_bps, notional_24h_usd,
            previous_price, current_price). No future prices or order-book claims.
    """
    ranked = []
    from simple_scanner.historical_precursor import crypto_pair
    for pair, move24, spread, notional, previous, current in rows:
        if asset_pairs is not None and not crypto_pair(pair, asset_pairs):
            continue
        values = (move24, spread, notional, previous, current)
        if not all(isinstance(x, (int, float)) and math.isfinite(x) for x in values):
            continue
        if previous <= 0 or current <= 0 or spread < 0 or notional < 25000:
            continue
        # Avoid chasing an already extended 24-hour move.
        if move24 < -5 or move24 > 12 or spread > 125:
            continue
        change = 100 * (current / previous - 1)
        if change < -2 or change > 5:
            continue
        # Liquidity and narrow spread reward tradability; moderate price
        # acceleration rewards earlier entry. These are research heuristics.
        score = (min(30, max(0, change) * 10)
                 + min(30, math.log10(max(1, notional / 25000)) * 15)
                 + max(0, 25 - spread / 5)
                 + max(0, 15 - abs(move24 - 1.5) * 2))
        ranked.append({"pair": pair, "score": round(score, 3),
                       "recent_change_pct": round(change, 4),
                       "spread_bps": spread, "notional_24h_usd": notional})
    return sorted(ranked, key=lambda x: (-x["score"], x["pair"]))


def evaluate_early_accumulation(con):
    """Full-universe shadow screening without persistent tables or extra API calls."""
    if not {"market_signals", "market_observations"}.issubset(
            {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}):
        return {"status": "AWAITING_MARKET_HISTORY", "buy_approved": False}
    latest = con.execute("SELECT MAX(run_at) FROM market_signals").fetchone()[0]
    if not latest:
        return {"status": "AWAITING_MARKET_HISTORY", "buy_approved": False}
    # Prior observations must precede the current scan; use up to 90 minutes
    # because the existing scan cadence is 15 minutes.
    rows = con.execute("""SELECT s.pair,s.move24_pct,s.spread_bps,s.notional_24h_usd,
           (SELECT p.price FROM market_observations p
            WHERE p.pair=s.pair AND p.run_at<s.run_at
              AND julianday(p.run_at)>=julianday(s.run_at)-90.0/1440
            ORDER BY p.run_at DESC LIMIT 1),m.price
        FROM market_signals s JOIN market_observations m
          ON m.run_at=s.run_at AND m.pair=s.pair
        WHERE s.run_at=?""", (latest,)).fetchall()
    eligible = [r for r in rows if r[4] is not None]
    # Use the canonical metadata only when it belongs to this exact scan.
    # Missing metadata fails closed for the early-accumulation shadow.
    from simple_scanner.historical_precursor import load_same_run_asset_pairs
    asset_pairs = load_same_run_asset_pairs(latest)
    ranked = early_accumulation_rank(eligible, asset_pairs=asset_pairs) if asset_pairs is not None else []
    return {"status": "SHADOW_CANDIDATES" if asset_pairs is not None else "AWAITING_CANONICAL_ASSET_METADATA", "observed_at": latest,
            "universe_observed": len(rows), "history_eligible": len(eligible),
            "candidates": ranked[:12], "buy_approved": False,
            "live_weights_modified": False,
            "limitations": "No order-book imbalance, buyer/seller flow or full-market intraday volume collected"}


def validate_accumulation_history(con):
    """Time-separated, market-wide, read-only historical challenger evaluation.

    Only the immediately preceding observation is used for features. A future
    observation is used strictly for the label, never the ranking. Evaluation
    is descriptive: no parameter tuning or live promotion.
    """
    required = {"market_signals", "market_observations"}
    if not required.issubset({r[0] for r in con.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")}):
        return {"status": "AWAITING_HISTORY", "promotion_eligible": False}
    rows = con.execute("""SELECT s.run_at,s.pair,s.move24_pct,s.spread_bps,
             s.notional_24h_usd,prior.price,now.price,
             (SELECT later.price FROM market_observations later
              WHERE later.pair=s.pair
                AND julianday(later.run_at)>=julianday(s.run_at)+1.0/24
                AND julianday(later.run_at)<julianday(s.run_at)+2.0/24
              ORDER BY later.run_at LIMIT 1) AS future_price
        FROM market_signals s
        JOIN market_observations now ON now.run_at=s.run_at AND now.pair=s.pair
        LEFT JOIN market_observations prior ON prior.pair=s.pair
          AND prior.run_at=(SELECT MAX(p.run_at) FROM market_observations p
             WHERE p.pair=s.pair AND p.run_at<s.run_at
               AND julianday(p.run_at)>=julianday(s.run_at)-90.0/1440)
        WHERE s.run_at < ? ORDER BY s.run_at DESC LIMIT 6000""",
        ((dt.datetime.now(dt.timezone.utc)-dt.timedelta(hours=2)).isoformat(),)).fetchall()
    if not rows:
        return {"status": "INSUFFICIENT_MATURED_HISTORY", "samples": 0,
                "timestamps": 0, "promotion_eligible": False}
    # Historical observations do not retain canonical Kraken base IDs per run.
    # The latest.json metadata applies only to one exact run, never to past
    # cohorts. Refuse to report historical recall on an unidentified universe.
    from simple_scanner.historical_precursor import load_same_run_asset_pairs
    latest_run = con.execute("SELECT MAX(run_at) FROM market_signals").fetchone()[0]
    latest_identity = load_same_run_asset_pairs(latest_run) if latest_run else None
    return {"status": "AWAITING_HISTORICAL_CANONICAL_IDENTITIES",
            "samples": len(rows), "timestamps": len({r[0] for r in rows}),
            "identity_coverage": {"historical_rows_verified": 0,
                                  "historical_rows_total": len(rows),
                                  "latest_run_metadata_available": latest_identity is not None,
                                  "reason": "No immutable per-run Kraken base identity ledger"},
            "promotion_eligible": False, "live_weights_modified": False}
    usable = [r for r in rows if r[5] is not None and r[7] is not None
              and r[6] > 0 and r[7] > 0]
    times = sorted({r[0] for r in usable})
    if len(times) < 20 or len(usable) < 500:
        return {"status": "INSUFFICIENT_MATURED_HISTORY",
                "samples": len(usable), "timestamps": len(times),
                "promotion_eligible": False}
    cutoff = times[int(len(times)*0.7)]
    holdout = [r for r in usable if r[0] >= cutoff]
    by_time = {}
    for r in holdout:
        by_time.setdefault(r[0], []).append(r)
    results = {}
    for threshold in (5, 20, 50, 100):
        baseline_hits = challenger_hits = events = 0
        challenger_picks = 0
        for cohort in by_time.values():
            ranked = early_accumulation_rank([r[1:7] for r in cohort])
            top = {x["pair"] for x in ranked[:12]}
            challenger_picks += len(top)
            for r in cohort:
                breakout = 100*(r[7]/r[6]-1) >= threshold
                events += int(breakout)
                baseline = 0.25 <= r[2] <= 12 and r[3] <= 45 and r[4] >= 100000
                baseline_hits += int(breakout and baseline)
                challenger_hits += int(breakout and r[1] in top)
        results[str(threshold)+"pct_1h"] = {
            "events": events, "baseline_identified": baseline_hits,
            "challenger_identified": challenger_hits,
            "baseline_recall": round(baseline_hits/max(1,events),4),
            "challenger_recall": round(challenger_hits/max(1,events),4),
            "challenger_picks": challenger_picks}
    return {"status": "HISTORICAL_HOLDOUT_EVALUATED",
            "train_timestamps": len(times)-len(by_time),
            "holdout_timestamps": len(by_time), "holdout_rows": len(holdout),
            "metrics": results, "promotion_eligible": False,
            "caveats": "Descriptive holdout only; unequal selection budgets, no execution/slippage or prospective proof"}


def assess_challenger_promotion(validation):
    """Automated research gate: never authorize production scoring changes.

    This is deliberately independent of trading execution. A future release
    requires prospective evidence and an explicitly reviewed rollback path.
    """
    metrics = validation.get("metrics", {})
    if validation.get("status") != "HISTORICAL_HOLDOUT_EVALUATED":
        return {"status": "BLOCKED_INSUFFICIENT_EVIDENCE",
                "reasons": ["historical_holdout_unavailable"],
                "promotion_eligible": False, "live_weights_modified": False}
    reasons = []
    for threshold in ("20pct_1h", "50pct_1h", "100pct_1h"):
        m = metrics.get(threshold, {})
        if m.get("events", 0) < 10:
            reasons.append("insufficient_events_"+threshold)
        elif m.get("challenger_recall", 0) <= m.get("baseline_recall", 0):
            reasons.append("no_recall_advantage_"+threshold)
    # Backtests alone never establish forward robustness or execution quality.
    reasons.extend(["prospective_validation_pending",
                    "equal_budget_comparison_pending",
                    "slippage_and_liquidity_validation_pending",
                    "reviewed_rollback_not_configured"])
    return {"status": "SHADOW_EVIDENCE_REVIEW",
            "reasons": reasons, "promotion_eligible": False,
            "live_weights_modified": False,
            "next_action": "Accumulate independent forward cohorts; retain live model"}


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
         WHERE o.pair=s.pair AND julianday(o.run_at)>=julianday(s.run_at)+1.0/24
           AND julianday(o.run_at)<julianday(s.run_at)+2.0/24
         ORDER BY o.run_at LIMIT 1) AS return_pct
        FROM market_signals s JOIN market_observations m
          ON m.run_at=s.run_at AND m.pair=s.pair
        WHERE s.run_at < ?
        ORDER BY s.run_at DESC LIMIT 12000""",
        ((dt.datetime.now(dt.timezone.utc)-dt.timedelta(hours=2)).isoformat(),)).fetchall()
    rows = [r for r in rows if r[5] is not None and all(math.isfinite(float(x)) for x in r[2:])]
    # Track the proportion of mature feature rows with usable future prices.
    reportable_samples = len(rows)
    rows.sort(key=lambda r:(r[0],r[1]))
    positives = sum(r[5]>=5 for r in rows)
    report = {"status":"INSUFFICIENT_MARKET_OUTCOMES","samples":reportable_samples,"breakouts":positives}
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
    # Evaluate substantial breakouts separately. The existing 5% objective
    # remains unchanged; these are diagnostic metrics, not trading signals.
    large_breakout_metrics={}
    for threshold in (20, 50, 100):
        def metrics_for(group, rule):
            tp=fp=fn=0
            for row in group:
                picked=bool(rule(row))
                event=row[5]>=threshold
                tp+=int(picked and event)
                fp+=int(picked and not event)
                fn+=int(not picked and event)
            return {"events":tp+fn,"identified":tp,"missed":fn,
                    "precision":round(tp/max(1,tp+fp),4),
                    "recall":round(tp/max(1,tp+fn),4)}
        large_breakout_metrics[str(threshold)+"pct_1h"]={
            "baseline":metrics_for(test,baseline),
            "challenger":metrics_for(test,learned)}
    report.update({"status":"MARKET_MISS_MODEL_EVALUATED",
                   "learned_filter":{"min_move24_pct":mm,"max_spread_bps":ms,"min_notional_usd":mn},
                   "train":train_metrics,"holdout":evaluate_rule(test,learned),
                   "baseline_holdout":evaluate_rule(test,baseline),
                   "large_breakout_holdout":large_breakout_metrics,
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
        accumulation = evaluate_early_accumulation(con)
        accumulation_validation = validate_accumulation_history(con)
        promotion_gate = assess_challenger_promotion(accumulation_validation)
        from simple_scanner.historical_precursor import evaluate_precursor
        historical_precursor = evaluate_precursor(con)
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
              "market_miss_model": market_miss_model,
              "early_accumulation": accumulation,
              "early_accumulation_validation": accumulation_validation,
              "challenger_promotion_gate": promotion_gate,
              "historical_precursor": historical_precursor}
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
