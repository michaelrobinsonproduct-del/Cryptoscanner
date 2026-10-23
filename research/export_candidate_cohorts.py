"""Read-only research exporter. Reject unverifiable feature timing and duplicate rows.

Do not infer feature observation time from run_at. Until actual persisted provenance
is demonstrated, this intentionally fails closed instead of exporting unsafe cohorts.
"""
import sqlite3
from pathlib import Path

def export_candidate_cohorts(db_path):
    con=sqlite3.connect("file:"+str(Path(db_path).resolve())+"?mode=ro",uri=True)
    try:
        required={"candidate_features","snapshots","market_signals","outcomes"}
        existing={r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if not required.issubset(existing):
            raise ValueError("required tables missing")
        feature_columns={r[1] for r in con.execute("PRAGMA table_info(candidate_features)")}
        if "features_observed_at" not in feature_columns:
            raise ValueError("BLOCKED: no independently stored feature observation timestamp")
        snapshot_columns={r[1] for r in con.execute("PRAGMA table_info(snapshots)")}
        market_columns={r[1] for r in con.execute("PRAGMA table_info(market_signals)")}
        if "observed_at" not in snapshot_columns or "observed_at" not in market_columns:
            raise ValueError("BLOCKED: snapshot or liquidity observation timestamp missing")
        for table in required:
            if table=="outcomes":
                keys="run_at,pair,horizon_hours"
            else:
                keys="run_at,pair"
            dup=con.execute("SELECT 1 FROM "+table+" GROUP BY "+keys+" HAVING COUNT(*)>1 LIMIT 1").fetchone()
            if dup:
                raise ValueError("BLOCKED: duplicate "+table+" observations")
        rows=con.execute("""SELECT f.run_at,f.pair,f.base_score,f.early_signal_score,
                   f.features_observed_at,s.price,s.observed_at,
                   m.spread_bps,m.notional_24h_usd,m.observed_at
                   FROM candidate_features f
                   JOIN snapshots s ON s.run_at=f.run_at AND s.pair=f.pair
                   LEFT JOIN market_signals m ON m.run_at=f.run_at AND m.pair=f.pair
                   WHERE f.early_signal_score IS NOT NULL
                   ORDER BY f.run_at,f.pair""").fetchall()
        from research.equal_budget_forward import _time
        outcomes={}
        for t,p,h,ret,observed in con.execute(
                "SELECT run_at,pair,horizon_hours,return_pct,evaluated_at FROM outcomes"):
            outcomes.setdefault((t,p),{})[str(h)]={"return_pct":ret,"evaluated_at":observed}
        exported=[]
        for t,p,base,challenger,features_at,price,price_at,spread,notional,market_at in rows:
            if not features_at or not price_at or not market_at:
                raise ValueError("BLOCKED: missing observation provenance")
            at=_time(t)
            if any(_time(x)>at for x in (features_at,price_at,market_at)):
                raise ValueError("BLOCKED: future feature, price or liquidity observation")
            if spread is None or notional is None:
                continue
            exported.append({"run_at":t,"features_observed_at":features_at,"pair":p,
                "baseline_score":base,"challenger_score":challenger,"price":price,
                "spread_bps":spread,"notional_usd":notional,
                "outcomes":outcomes.get((t,p),{})})
        return exported
    finally:
        con.close()
