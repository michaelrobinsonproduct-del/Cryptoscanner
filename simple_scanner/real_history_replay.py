"""Read-only replay of historical market observations against verified pair identities.

Operator supplies a safe SQLite backup and independently verified Kraken
canonical identities. No guesses from current AssetPairs for old delisted pairs.
Never writes the source DB or changes live scanner settings.
"""
import argparse
import json
from pathlib import Path
import sqlite3
from .historical_precursor import rank_precursors, crypto_pair
from .shadow_learning import early_accumulation_rank

def replay(db_path, identities_path):
    identities = json.loads(Path(identities_path).read_text())
    if not isinstance(identities, dict) or not identities:
        raise ValueError("Nonempty verified identity mapping required")
    con = sqlite3.connect(Path(db_path).resolve().as_uri()+"?mode=ro", uri=True)
    try:
        if con.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ValueError("Historical SQLite integrity failed")
        rows = con.execute("""SELECT s.run_at,s.pair,s.move24_pct,s.spread_bps,
            s.notional_24h_usd,
            (SELECT p.price FROM market_observations p WHERE p.pair=s.pair
             AND p.run_at<s.run_at ORDER BY p.run_at DESC LIMIT 1),
            n.price,
            (SELECT p.price FROM market_observations p WHERE p.pair=s.pair
             AND p.run_at<s.run_at ORDER BY p.run_at DESC LIMIT 1 OFFSET 1)
            FROM market_signals s JOIN market_observations n
            ON n.run_at=s.run_at AND n.pair=s.pair
            ORDER BY s.run_at,s.pair""").fetchall()
    finally:
        con.close()
    if not rows:
        raise ValueError("No actual historical observations available")
    by_run = {}
    for run,pair,move,spread,notional,previous,current,older in rows:
        by_run.setdefault(run,[]).append((pair,move,spread,notional,previous,current,older))
    missing = sorted({pair for row in rows for pair in [row[1]]
                      if pair not in identities or not isinstance(identities[pair],dict)
                      or not identities[pair].get("base")})
    if missing:
        return {"status":"BLOCKED_UNVERIFIED_IDENTITIES","rows":len(rows),
                "missing_count":len(missing),"missing_examples":missing[:20],
                "passed":False}
    unchanged = 0
    excluded = 0
    for cohort in by_run.values():
        eligible = {row[0] for row in cohort if crypto_pair(row[0], identities)}
        baseline = rank_precursors(cohort,limit=len(cohort))
        candidate = rank_precursors(cohort,limit=len(cohort),asset_pairs=identities)
        base_map = {x["pair"]:x for x in baseline}
        for x in candidate:
            if x["pair"] not in eligible or base_map.get(x["pair"]) != x:
                raise AssertionError("Precursor crypto score parity failure")
            unchanged += 1
        six = [row[:6] for row in cohort if row[5] is not None]
        accumulation = early_accumulation_rank(six,asset_pairs=identities)
        if any(x["pair"] not in eligible for x in accumulation):
            raise AssertionError("Accumulation identity filter failure")
        excluded += len(cohort)-len([row for row in cohort if row[0] in eligible])
    return {"status":"REAL_HISTORY_REPLAY_VERIFIED","passed":True,
            "rows":len(rows),"runs":len(by_run),"identity_verified":len(rows),
            "unchanged_precursor_candidates":unchanged,"excluded_fiat_stable_rows":excluded,
            "source":"production_sqlite_backup"}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--database",required=True)
    p.add_argument("--verified-identities",required=True)
    a=p.parse_args()
    result=replay(a.database,a.verified_identities)
    print(json.dumps(result,sort_keys=True))
    if not result["passed"]:
        raise SystemExit(2)

if __name__=="__main__":
    main()
