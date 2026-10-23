"""Export ONLY point-in-time persisted candidate cohorts; never write to the live DB.

This is an observed-candidate comparison, not full-universe early discovery.
It cannot reconstruct the separate legacy precursor's historical scores.
"""
import argparse
import json
import sqlite3
from pathlib import Path

def export_candidate_cohorts(db_path):
    uri="file:"+str(Path(db_path).resolve())+"?mode=ro"
    con=sqlite3.connect(uri,uri=True)
    try:
        required={"candidate_features","snapshots","market_signals","outcomes"}
        existing={r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if not required.issubset(existing):
            raise ValueError("required point-in-time tables missing")
        rows=con.execute("""SELECT f.run_at,f.pair,f.base_score,f.early_signal_score,
                   s.price,m.spread_bps,m.notional_24h_usd
                   FROM candidate_features f
                   JOIN snapshots s ON s.run_at=f.run_at AND s.pair=f.pair
                   LEFT JOIN market_signals m ON m.run_at=f.run_at AND m.pair=f.pair
                   WHERE f.early_signal_score IS NOT NULL
                   ORDER BY f.run_at,f.pair""").fetchall()
        outcomes={}
        for t,p,h,ret,observed in con.execute(
                "SELECT run_at,pair,horizon_hours,return_pct,evaluated_at FROM outcomes"):
            outcomes.setdefault((t,p),{})[str(h)]={"return_pct":ret,"evaluated_at":observed}
        exported=[]
        for t,p,base,challenger,price,spread,notional in rows:
            if spread is None or notional is None:
                continue  # missing liquidity is not zero spread or executable liquidity
            exported.append({"run_at":t,"features_observed_at":t,"pair":p,
                "baseline_score":base,"challenger_score":challenger,"price":price,
                "spread_bps":spread,"notional_usd":notional,
                "outcomes":outcomes.get((t,p),{})})
        return exported
    finally:
        con.close()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("db",help="Existing SQLite path (read-only)")
    args=parser.parse_args()
    rows=export_candidate_cohorts(args.db)
    for row in rows:
        print(json.dumps(row,separators=(",",":")))

if __name__=="__main__":
    main()
