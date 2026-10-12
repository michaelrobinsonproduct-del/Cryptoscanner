"""Conservative shadow-only learning. Never changes live rankings or approves buys."""
import json, os, sqlite3, math
from pathlib import Path

MIN_TRAIN=100
MIN_TEST=40
FEATURES=("move_15m_pct","volume_accel","base_score")
def evaluate(db_path):
    con=sqlite3.connect(f"file:{Path(db_path).resolve()}?mode=ro",uri=True)
    try:
        rows=con.execute("""SELECT f.run_at,f.pair,f.move_15m_pct,f.volume_accel,f.base_score,o.return_pct
            FROM candidate_features f JOIN outcomes o ON f.run_at=o.run_at AND f.pair=o.pair
            WHERE o.horizon_hours=1 AND f.move_15m_pct IS NOT NULL AND f.volume_accel IS NOT NULL
            ORDER BY f.run_at,f.pair""").fetchall()
    finally: con.close()
    result={"mode":"SHADOW_ONLY","samples":len(rows),"min_train":MIN_TRAIN,"min_test":MIN_TEST,
            "live_weights_modified":False,"buy_approved":False,"status":"INSUFFICIENT_DATA"}
    # Partition by observation timestamp, never random rows from the same scan.
    times=sorted({r[0] for r in rows})
    if len(rows)<MIN_TRAIN+MIN_TEST or len(times)<12: return result
    cut=times[max(1,int(len(times)*.7))]
    train=[r for r in rows if r[0]<cut]; test=[r for r in rows if r[0]>=cut]
    if len(train)<MIN_TRAIN or len(test)<MIN_TEST: return result
    # Evaluate predeclared, bounded challenger; no optimization on test outcomes.
    def challenger(r): return r[4]+max(-25,min(25,r[2]*5))+max(-15,min(15,(r[3]-1)*10))
    def compare(group):
        grouped={}
        for r in group: grouped.setdefault(r[0],[]).append(r)
        base=[]; alt=[]
        for cohort in grouped.values():
            base.append(max(cohort,key=lambda r:r[4])[5])
            alt.append(max(cohort,key=challenger)[5])
        return {"cohorts":len(grouped),"base_avg_pct":round(sum(base)/len(base),4),
                "challenger_avg_pct":round(sum(alt)/len(alt),4),
                "delta_pct":round((sum(alt)-sum(base))/len(base),4)}
    result.update({"status":"SHADOW_EVALUATED","train":compare(train),"holdout":compare(test),
                   "promotion_eligible":False,"promotion_reason":"Manual review and multi-horizon validation required"})
    return result

def main():
    folder=Path(os.getenv("SIMPLE_SCANNER_DATA_DIR","simple_scanner/output"))
    report=evaluate(folder/"history.sqlite3")
    target=folder/"shadow_learning.json"
    tmp=folder/"shadow_learning.json.tmp"
    tmp.write_text(json.dumps(report,indent=2))
    tmp.replace(target)
    print("SHADOW_LEARNING",json.dumps(report),flush=True)
if __name__=="__main__":main()
