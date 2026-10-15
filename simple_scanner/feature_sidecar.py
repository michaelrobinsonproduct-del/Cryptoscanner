"""Research-only feature storage. Explicit path required; never touches scanner history DB."""
import sqlite3
from pathlib import Path
from simple_scanner.market_feature_schema import validate_record

def persist_features(path, capture, *, observed_at, keep_runs=96, max_pairs=1000):
    """Append one complete, validated cohort atomically, with bounded retention.

    Caller must supply an isolated path. This function is never imported by scan.py.
    """
    p=Path(path).resolve()
    protected=Path("/data")
    if p.name in {"history.sqlite3","latest.json"} or p==protected or protected in p.parents:
        raise ValueError("protected production path")
    if p.suffix!=".sqlite3":
        raise ValueError("sidecar must use .sqlite3 extension")
    if type(keep_runs) is not int or not 2<=keep_runs<=1000:
        raise ValueError("invalid retention")
    if type(max_pairs) is not int or not 1<=max_pairs<=10000:
        raise ValueError("invalid pair limit")
    if not isinstance(capture,dict) or capture.get("status")!="DIAGNOSTIC_ONLY":
        raise ValueError("untrusted capture")
    records=capture.get("records")
    if not isinstance(records,list) or not records or len(records)>max_pairs:
        raise ValueError("invalid cohort size")
    if len({r.get("pair") for r in records if isinstance(r,dict)})!=len(records):
        raise ValueError("duplicate pairs")
    if any(r.get("observed_at")!=observed_at or
           not validate_record(r,observed_at=observed_at)["valid"] for r in records):
        raise ValueError("invalid point-in-time record")
    if p.exists() and (p.is_symlink() or not p.is_file()):
        raise ValueError("invalid destination")
    p.parent.mkdir(parents=True,exist_ok=True)
    con=sqlite3.connect(p,timeout=5)
    try:
        con.execute("CREATE TABLE IF NOT EXISTS market_features (observed_at TEXT NOT NULL,pair TEXT NOT NULL,price REAL NOT NULL,spread_bps REAL NOT NULL,notional_24h_usd REAL NOT NULL,move_24h_pct REAL NOT NULL,PRIMARY KEY(observed_at,pair))")
        with con:
            existing=con.execute("SELECT COUNT(*) FROM market_features WHERE observed_at=?",(observed_at,)).fetchone()[0]
            if existing:
                raise ValueError("cohort already stored")
            con.executemany("INSERT INTO market_features VALUES (?,?,?,?,?,?)",[
                (observed_at,r["pair"],r["price"],r["spread_bps"],r["notional_24h_usd"],r["move_24h_pct"]) for r in records])
            cutoff=con.execute("SELECT observed_at FROM market_features GROUP BY observed_at ORDER BY observed_at DESC LIMIT 1 OFFSET ?",(keep_runs-1,)).fetchone()
            if cutoff:
                con.execute("DELETE FROM market_features WHERE observed_at < ?",(cutoff[0],))
        if con.execute("PRAGMA integrity_check").fetchone()[0]!="ok":
            raise RuntimeError("sidecar integrity failure")
        return {"status":"STORED_RESEARCH_ONLY","rows":len(records),"path":str(p),
                "buy_approved":False,"production_modified":False}
    finally:
        con.close()
