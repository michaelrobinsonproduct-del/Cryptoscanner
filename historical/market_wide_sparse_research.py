"""Research-only archive sparse-window sensitivity, separate from strict labels.

Kraken documents omitted intervals as no trades in its downloadable OHLCVT:
https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data
Only a checksum-pinned official archive, a wholly valid member, and observed
trades bracketing the window qualify. No forward-fill, synthetic prices, or
inference from REST/sampled quote gaps. Retrospective candle-high target only.
"""
import argparse
from bisect import bisect_left, bisect_right
import csv
from datetime import datetime, timedelta, timezone
import gzip
import hashlib
import io
import json
from pathlib import Path
import tempfile
import zipfile

from historical.kraken_q3_48h_shadow import parse_bar, parse_market
from paper_pov.market_wide_learning import train_archive_shadow
from paper_pov.shadow_learning_evidence import utc_time, canonical_digest

POLICY = "PINNED_KRAKEN_ARCHIVE_BRACKETED_NO_TRADE_RESEARCH_ONLY"


def read_valid_member(raw, pair):
    rows = []
    for record in csv.reader(io.TextIOWrapper(raw, encoding="utf-8")):
        bar = parse_bar(record)
        # Reject (not silently discard) anomalous rows in this sensitivity.
        if bar is None or bar[3] <= 0:
            raise ValueError("Malformed or zero-trade archive row")
        stamp, close, volume, trades = bar
        at = datetime.fromtimestamp(stamp, timezone.utc) + timedelta(minutes=5)
        if rows and at <= rows[-1][0]:
            raise ValueError("Unordered or duplicate archive candle")
        rows.append((at, close, float(record[2])))
    if not rows:
        raise ValueError("Empty archive member")
    return rows


def bracketed_high_labels(cohort, rows, *, archive_start, archive_end):
    """Return a comparison-only copy. Never mutate the strict ledger labels."""
    start, end = utc_time(archive_start), utc_time(archive_end)
    stamps = [row[0] for row in rows]
    if any(b <= a for a,b in zip(stamps, stamps[1:])):
        raise ValueError("Invalid checked candle ordering")
    anchors = {a["prediction_id"]:a for a in cohort["anchors"]}
    counts = {str(h):{"new_hits":0,"new_nonhits":0,"unknown":0,"no_trade_intervals":0}
              for h in (1,6,24,48)}
    output = []
    for original in cohort["outcomes"]:
        row = dict(original)
        row["strict_coverage_complete"] = original["coverage_complete"]
        h = row["horizon_hours"]
        if row["coverage_complete"] or row["outcome_status"] != "MISSING_CANDLES":
            output.append(row)
            continue
        a = anchors[row["prediction_id"]]
        e = utc_time(a["entry_utc"])
        target = e + timedelta(hours=h)
        i = bisect_left(stamps,e)
        # Both endpoints lie within the stated archive window, with an observed
        # entry candle and a trade bracket at/after the horizon. Outside these
        # conditions never infer absence of trades.
        if (not start <= e < target <= end or i >= len(stamps)
                or stamps[i] != e or rows[i][1] != a["entry_price"]
                or not stamps or stamps[-1] < target):
            counts[str(h)]["unknown"] += 1
            output.append(row)
            continue
        last = bisect_right(stamps,target)
        actual = rows[i+1:last]
        missing = h*12-len(actual)
        if missing <= 0:
            # A strictly full window should already have a complete label.
            raise ValueError("Archive strict outcome contradicts complete raw window")
        high = max((r[2] for r in actual),default=None)
        hit = high is not None and high/a["entry_price"]-1 >= .30
        row.update(coverage_complete=True,hit=hit,outcome_status="MATURE",
                   comparison_label_policy=POLICY,strict_coverage_complete=False,
                   no_trade_intervals=missing,
                   max_favorable_return=high/a["entry_price"]-1 if high is not None else None,
                   close_return=None)
        if hit:
            cross=next(r[0] for r in actual if r[2]/a["entry_price"]-1 >= .30)
            row.update(observed_crossing_candle_close_utc=cross.isoformat(),
                       observed_lead_hours_upper_bound=(cross-e).total_seconds()/3600,
                       crossing_evidence="BRACKETED_ARCHIVE_RESEARCH_WINDOW")
        counts[str(h)]["new_hits" if hit else "new_nonhits"] += 1
        counts[str(h)]["no_trade_intervals"] += missing
        output.append(row)
    return dict(cohort,outcomes=output,comparison_label_policy=POLICY),counts


def run(archive, cohorts, *, expected_sha256, archive_start, archive_end):
    digest = hashlib.sha256()
    with Path(archive).open("rb") as raw:
        for chunk in iter(lambda:raw.read(4*1024*1024),b""):
            digest.update(chunk)
    if digest.hexdigest()!=expected_sha256:
        raise ValueError("Pinned archive checksum mismatch")
    totals = {str(h):{"new_hits":0,"new_nonhits":0,"unknown":0,"no_trade_intervals":0}
              for h in (1,6,24,48)}
    rejected = {}
    observed = 0
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)/"sparse-comparison.jsonl.gz"
        with zipfile.ZipFile(archive) as z, gzip.open(cohorts,"rt") as source, gzip.open(path,"wt") as dest:
            for line in source:
                c=json.loads(line)
                name=c["source_member"]
                pair=parse_market(name)
                if (c["source_archive_sha256"]!=expected_sha256 or pair is None
                        or any(a["pair"]!=pair for a in c["anchors"])
                        or any(o["pair"]!=pair for o in c["outcomes"])):
                    raise ValueError("Archive/cohort provenance mismatch")
                try:
                    with z.open(name) as raw:
                        rows=read_valid_member(raw,pair)
                except (ValueError,KeyError) as exc:
                    rejected[pair]=str(exc)
                    # Keep candidates and their strict outcomes; never select
                    # holdout candidates according to later data availability.
                    dest.write(line)
                    continue
                observed += 1
                upgraded,counts=bracketed_high_labels(c,rows,archive_start=archive_start,archive_end=archive_end)
                dest.write(json.dumps(upgraded,separators=(",",":"),sort_keys=True)+"\n")
                for h in totals:
                    for k in totals[h]:
                        totals[h][k]+=counts[h][k]
        result=train_archive_shadow(path,training_end_utc="2026-09-07T00:00:00Z",
                 holdout_start_utc="2026-09-09T00:00:00Z",evaluation_asof_utc="2026-09-15T00:00:00Z")
    # Retain numerical comparison only; do not export a deployable model from
    # this sensitivity. The cumulative strict training path remains separate.
    model=result.pop("model")
    result.pop("digest")
    out={"schema":"sparse_archive_research_comparison_v1","policy":POLICY,
         "archive_sha256":expected_sha256,"archive_start":archive_start,"archive_end":archive_end,
         "observed_valid_members":observed,"rejected_members":rejected,"reclassified":totals,
         "training_count":model["training_count"],"positive_count":model["positive_count"],
         "strict_training_unchanged":True,"comparison":result,
         "production_applied":False,"promotion_authorized":False,"measured_lift_verified":False}
    out["digest"]=canonical_digest(out)
    return out


def main():
    p=argparse.ArgumentParser()
    p.add_argument("archive",type=Path)
    p.add_argument("cohorts",type=Path)
    p.add_argument("--sha256",required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    result=run(a.archive,a.cohorts,expected_sha256=a.sha256,
               archive_start="2026-07-01T00:00:00Z",archive_end="2026-10-01T00:00:00Z")
    a.output.write_text(json.dumps(result,sort_keys=True)+"\n")
    print(json.dumps(result,sort_keys=True))


if __name__=="__main__":
    main()
