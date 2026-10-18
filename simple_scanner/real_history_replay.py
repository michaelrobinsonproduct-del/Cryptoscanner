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
    # A bare base label is not proof of historical provenance. Require an
    # operator-verifiable authoritative Kraken AssetPairs record for each pair.
    def has_provenance(item):
        return (isinstance(item, dict) and isinstance(item.get("base"), str)
                and bool(item["base"].strip())
                and item.get("source") == "kraken_assetpairs"
                and isinstance(item.get("observed_at"), str)
                and bool(item["observed_at"].strip())
                and isinstance(item.get("evidence_ref"), str)
                and bool(item["evidence_ref"].strip()))
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
                      if pair not in identities or not has_provenance(identities[pair])})
    if missing:
        return {"status":"BLOCKED_UNVERIFIED_IDENTITIES","rows":len(rows),
                "missing_count":len(missing),"missing_examples":missing[:20],
                "passed":False}
    unchanged = 0
    newly_eligible = 0
    excluded = 0
    for cohort in by_run.values():
        eligible = {row[0] for row in cohort if crypto_pair(row[0], identities)}
        baseline = rank_precursors(cohort,limit=len(cohort))
        candidate = rank_precursors(cohort,limit=len(cohort),asset_pairs=identities)
        base_map = {x["pair"]:x for x in baseline}
        for x in candidate:
            if x["pair"] not in eligible:
                raise AssertionError("Ineligible asset entered precursor rankings")
            # Canonical Kraken identity may legitimately admit a crypto pair
            # that the old suffix heuristic missed. Compare scores only for
            # pairs ranked by both; separately count newly eligible pairs.
            if x["pair"] in base_map:
                if base_map[x["pair"]] != x:
                    raise AssertionError("Precursor crypto score parity failure")
                unchanged += 1
            else:
                newly_eligible += 1
        six = [row[:6] for row in cohort if row[5] is not None]
        accumulation = early_accumulation_rank(six,asset_pairs=identities)
        if any(x["pair"] not in eligible for x in accumulation):
            raise AssertionError("Accumulation identity filter failure")
        excluded += len(cohort)-len([row for row in cohort if row[0] in eligible])
    return {"status":"REAL_HISTORY_REPLAY_VERIFIED","passed":True,
            "rows":len(rows),"runs":len(by_run),"identity_verified":len(rows),
            "unchanged_precursor_candidates":unchanged,"newly_eligible_candidates":newly_eligible,
            "excluded_fiat_stable_rows":excluded,
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
