"""Offline SQLite history audit. ONLY run on a consistent detached backup; immutable=1 ignores live WAL."""
import argparse
import json
import sqlite3
from pathlib import Path
TABLES=('snapshots','candidate_features','market_observations','market_signals','outcomes')
def audit(db_path):
    path=Path(db_path).resolve(strict=True)
    con=sqlite3.connect(path.as_uri()+'?mode=ro&immutable=1',uri=True)
    try:
        con.execute('PRAGMA query_only=ON')
        result={'database':str(path),'integrity':con.execute('PRAGMA integrity_check').fetchone()[0],'tables':{}}
        existing={r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        for table in TABLES:
            if table not in existing:
                result['tables'][table]={'status':'MISSING'};continue
            cols=[r[1] for r in con.execute(f'PRAGMA table_info({table})')]
            item={'status':'PRESENT','columns':cols,'rows':con.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]}
            if 'run_at' in cols:
                item['earliest_run_at'],item['latest_run_at'],item['distinct_timestamps']=con.execute(f'SELECT MIN(run_at),MAX(run_at),COUNT(DISTINCT run_at) FROM {table}').fetchone()
            if 'pair' in cols:
                item['distinct_pairs']=con.execute(f'SELECT COUNT(DISTINCT pair) FROM {table}').fetchone()[0]
                item['per_pair']=[{'pair':p,'rows':n,'first':a,'last':b} for p,n,a,b in con.execute(f'SELECT pair,COUNT(*),MIN(run_at),MAX(run_at) FROM {table} GROUP BY pair ORDER BY pair')]
            if 'run_at' in cols and 'pair' in cols:
                item['duplicate_pair_timestamps']=con.execute(f'SELECT COALESCE(SUM(n-1),0) FROM (SELECT COUNT(*) n FROM {table} GROUP BY run_at,pair HAVING COUNT(*)>1)').fetchone()[0]
                item['timestamp_gaps_over_90m']=[{'from':a,'to':b,'minutes':round(d,2)} for a,b,d in con.execute(f'''WITH t AS (SELECT DISTINCT run_at FROM {table}),q AS (SELECT run_at,LAG(run_at) OVER (ORDER BY run_at) prev FROM t) SELECT prev,run_at,(julianday(run_at)-julianday(prev))*1440 FROM q WHERE prev IS NOT NULL AND (julianday(run_at)-julianday(prev))*1440>90 ORDER BY prev LIMIT 100''')]
            if table=='outcomes' and 'horizon_hours' in cols:
                item['by_horizon']=[{'hours':h,'rows':n} for h,n in con.execute('SELECT horizon_hours,COUNT(*) FROM outcomes GROUP BY horizon_hours ORDER BY horizon_hours')]
                if {'snapshots','market_observations'}<=existing and {'evaluated_at','return_pct'}<=set(cols):
                    item['label_checks']={'orphaned_snapshots':con.execute('SELECT COUNT(*) FROM outcomes o LEFT JOIN snapshots s ON s.run_at=o.run_at AND s.pair=o.pair WHERE s.pair IS NULL').fetchone()[0],'missing_evaluation_observation':con.execute('SELECT COUNT(*) FROM outcomes o LEFT JOIN market_observations m ON m.run_at=o.evaluated_at AND m.pair=o.pair WHERE m.pair IS NULL').fetchone()[0],'return_mismatch_gt_0_02pp':con.execute('SELECT COUNT(*) FROM outcomes o JOIN snapshots s ON s.run_at=o.run_at AND s.pair=o.pair JOIN market_observations m ON m.run_at=o.evaluated_at AND m.pair=o.pair WHERE ABS(o.return_pct-100.0*(m.price/s.price-1))>0.02').fetchone()[0]}
            result['tables'][table]=item
        return result
    finally:con.close()
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('database');print(json.dumps(audit(p.parse_args().database),indent=2))
