"""Recover actual retained five-minute candles for the post-Q3 historical gap.

These historical artifacts come from prediction-selected learning workflows,
not a complete exchange universe. Do not certify past eligibility, no-trade
intervals, exchange authentication, or executable returns from them.
"""
import argparse
from datetime import timedelta
import gzip
import hashlib
import json
from pathlib import Path
from .market_wide_learning import build_market_cohort
from .rolling_kraken_candles import SCHEMA, _rows, _merge_same_observation
from .shadow_learning_evidence import utc_time, canonical_digest

START="2026-10-01T00:00:00Z"


def recover_snapshots(paths, *, end_utc, cohort_path):
    start,end=utc_time(START),utc_time(end_utc)
    if not start<end<=start+timedelta(days=90):
        raise ValueError("Invalid post-Q3 recovery window")
    rows, receipts = {}, []
    for path in paths:
        raw=Path(path).read_bytes()
        digest=hashlib.sha256(raw).hexdigest()
        snapshot=json.loads(raw)
        if snapshot.get("schema")!=SCHEMA or snapshot.get("source_authenticated") is not False:
            raise ValueError("Unexpected rolling snapshot schema")
        receipts.append({"snapshot":Path(path).parent.name,"sha256":digest})
        for item in snapshot["results"]:
            pair=item["pair"]
            for stamp,row in _rows(item).items():
                t=utc_time(stamp)
                if not start-timedelta(hours=1)<=t<=end:
                    continue
                group=rows.setdefault(pair,{})
                if stamp in group:
                    group[stamp]=_merge_same_observation(group[stamp],row,pair)
                else:
                    group[stamp]=row
    source_digest=canonical_digest(sorted(receipts,key=lambda r:r["snapshot"]))
    counts={str(h):{"hits":0,"misses":0,"immature":0,"missing_candles":0} for h in (1,6,24,48)}
    anchors=features=bars=0
    markets_with_hits=set()
    dates={}
    Path(cohort_path).parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(cohort_path,"wt",encoding="utf-8") as out:
        for pair,group in sorted(rows.items()):
            candles=[group[k] for k in sorted(group)]
            if not candles:
                continue
            bars+=len(candles)
            for c in candles:
                day=utc_time(c["timestamp_utc"]).date().isoformat()
                dates.setdefault(day,set()).add(pair)
            cohort=build_market_cohort(candles,eligible_pairs=[pair],evaluation_asof_utc=end_utc,
                                      anchor_start_utc=START)
            for row in cohort["anchors"]+cohort["outcomes"]:
                row["source_sha256"]=source_digest
            cohort.update(source_kind="RETAINED_KRAKEN_REST_ROLLING_SNAPSHOTS",
                          source_snapshot_set_sha256=source_digest,
                          eligibility_scope="PREDICTION_SELECTED_HISTORY_NOT_FULL_MARKET")
            out.write(json.dumps(cohort,sort_keys=True,separators=(",",":"))+"\n")
            anchors+=len(cohort["anchors"])
            features+=cohort["feature_complete_anchors"]
            for h,value in cohort["per_horizon"].items():
                for k,n in value.items():
                    counts[h][k]+=n
                if value["hits"]:
                    markets_with_hits.add(pair)
    result={"schema":"post_q3_observed_recovery_v1","start_utc":START,"end_utc":end_utc,
            "snapshot_receipts":receipts,"snapshot_set_sha256":source_digest,
            "observed_pairs":len(rows),"observed_candles":bars,"anchors":anchors,
            "feature_complete_anchors":features,"per_horizon":counts,
            "markets_with_hits":sorted(markets_with_hits),
            "observed_pair_counts_by_day":{d:len(p) for d,p in sorted(dates.items())},
            "coverage_scope":"PARTIAL_PREDICTION_SELECTED_NOT_MARKET_WIDE",
            "source_authenticated":False,"production_applied":False,
            "promotion_authorized":False,"measured_lift_verified":False}
    result["digest"]=canonical_digest(result)
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument("snapshots",nargs="+",type=Path)
    p.add_argument("--end",required=True)
    p.add_argument("--cohorts",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path)
    a=p.parse_args()
    result=recover_snapshots(a.snapshots,end_utc=a.end,cohort_path=a.cohorts)
    a.output.write_text(json.dumps(result,sort_keys=True)+"\n")
    print(json.dumps(result,sort_keys=True))


if __name__=="__main__":
    main()
