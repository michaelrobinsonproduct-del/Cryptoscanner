"""Lossless research checkpoint and exact-fit compact historical seed.

These are local/artifact formats, not a second canonical ledger or permanent
storage service. Preserve source hashes and every retained state row.
"""
import argparse
from collections import defaultdict
import gzip
import hashlib
import json
from pathlib import Path
from datetime import timedelta
from .shadow_learning_evidence import canonical_digest, utc_time

SEED_SCHEMA="market_wide_strict_seed_v1"
CHECKPOINT_SCHEMA="market_wide_partitioned_checkpoint_v1"
STATE_FIELDS=("anchors","outcomes","shadow_predictions","shadow_outcomes")


def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()


def write_gzip(path, rows):
    # Stable bytes for an identical payload, independent of run time/path.
    with Path(path).open("wb") as raw, gzip.GzipFile(filename="",fileobj=raw,mode="wb",mtime=0) as f:
        for row in rows:
            f.write((json.dumps(row,sort_keys=True,separators=(",",":"))+"\n").encode())


def read_rows(path):
    with gzip.open(path,"rt",encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def source_key(kind):
    if kind=="archive":
        return "source_archive_sha256","archive_sha256"
    if kind=="retained_observed":
        return "source_snapshot_set_sha256","snapshot_set_sha256"
    raise ValueError("Unknown historical source kind")


def validate_source(cohort,kind,expected):
    field,_=source_key(kind)
    if (cohort.get(field)!=expected or cohort.get("production_applied") is not False
            or cohort.get("source_authenticated") is not False):
        raise ValueError("Historical source provenance mismatch")
    if kind=="retained_observed" and (cohort.get("source_kind")!="RETAINED_KRAKEN_REST_ROLLING_SNAPSHOTS"
            or cohort.get("eligibility_scope")!="PREDICTION_SELECTED_HISTORY_NOT_FULL_MARKET"):
        raise ValueError("Unexpected retained observation scope")
    if any(r.get("source_sha256")!=expected for r in cohort["anchors"]+cohort["outcomes"]):
        raise ValueError("Historical row source digest mismatch")


def build_seed(sources, directory):
    """Keep every row pair eligible for the existing strict 48h fit.

    Omit only rows that the current trainer can never admit. No time cutoff:
    later maturation/purge can still admit an already complete archived label.
    Original full cohorts remain the authority for other research horizons.
    """
    directory=Path(directory)
    directory.mkdir(parents=True,exist_ok=True)
    receipts=[]
    for i,(kind,path,source_sha,expected_file_sha) in enumerate(sources):
        _,key=source_key(kind)
        original=file_sha(path)
        if original!=expected_file_sha:
            raise ValueError("Original historical cohort checksum mismatch")
        name=f"source-{i:02d}.jsonl.gz"
        counts={"examples":0,"positives":0,"original_anchors":0,"original_outcomes":0}
        def compact():
            for c in read_rows(path):
                validate_source(c,kind,source_sha)
                counts["original_anchors"]+=len(c["anchors"])
                counts["original_outcomes"]+=len(c["outcomes"])
                anchors={}
                for a in c["anchors"]:
                    if not a.get("feature_complete"):
                        continue
                    if a["prediction_id"] in anchors:
                        raise ValueError("Duplicate feature-complete seed anchor")
                    anchors[a["prediction_id"]]=a
                outcomes=[]
                used=set()
                for o in c["outcomes"]:
                    pid=o["prediction_id"]
                    if (o["horizon_hours"]!=48 or pid not in anchors or not o["coverage_complete"]
                            or type(o["hit"]) is not bool):
                        continue
                    if pid in used:
                        raise ValueError("Duplicate complete seed outcome")
                    if utc_time(o["label_mature_utc"])!=utc_time(anchors[pid]["entry_utc"])+timedelta(hours=48):
                        raise ValueError("Invalid seed maturity")
                    used.add(pid)
                    outcomes.append(o)
                    counts["examples"]+=1
                    counts["positives"]+=int(o["hit"])
                if used:
                    # Keep original rows byte-equivalent under canonical JSON.
                    yield dict(c,anchors=[a for pid,a in anchors.items() if pid in used],outcomes=outcomes)
        write_gzip(directory/name,compact())
        receipts.append({"kind":kind,key:source_sha,"cohort_sha256":original,
                         "seed_file":name,"seed_sha256":file_sha(directory/name),**counts})
    manifest={"schema":SEED_SCHEMA,"sources":receipts,"strict_48h_only":True,
              "original_cohorts_required_for_other_horizons":True,
              "source_authenticated":False,"production_applied":False,"promotion_authorized":False}
    manifest["digest"]=canonical_digest(manifest)
    (directory/"manifest.json").write_text(json.dumps(manifest,sort_keys=True)+chr(10))
    return manifest


def load_seed(directory, expected_sources):
    """Verify exact pinned original cohort receipts and compact file checksums."""
    directory=Path(directory)
    manifest=json.loads((directory/"manifest.json").read_text())
    if (manifest.get("schema")!=SEED_SCHEMA or manifest.get("digest")!=canonical_digest(
            {k:v for k,v in manifest.items() if k!="digest"}) or manifest.get("strict_48h_only") is not True
            or manifest.get("production_applied") is not False):
        raise ValueError("Invalid compact seed manifest")
    actual=[]
    for i,r in enumerate(manifest["sources"]):
        kind=r["kind"]
        _,key=source_key(kind)
        name=f"source-{i:02d}.jsonl.gz"
        if r["seed_file"]!=name or file_sha(directory/name)!=r["seed_sha256"]:
            raise ValueError("Compact seed file checksum mismatch")
        actual.append((kind,r[key],r["cohort_sha256"]))
    if actual!=list(expected_sources):
        raise ValueError("Compact seed original cohort receipt mismatch")
    return manifest


def pack_state(state,directory):
    """Split complete state by UTC entry-month, preserving original row order.

    This is a lossless checkpoint, not deletion or an active-memory cap fix.
    """
    directory=Path(directory)
    directory.mkdir(parents=True,exist_ok=True)
    if state.get("digest")!=canonical_digest({k:v for k,v in state.items() if k!="digest"}):
        raise ValueError("Invalid state checksum")
    groups=defaultdict(list)
    counts={}
    for field in STATE_FIELDS:
        if field not in state:
            continue
        counts[field]=len(state[field])
        for index,row in enumerate(state[field]):
            month=utc_time(row["entry_utc"]).strftime("%Y-%m")
            groups[month].append({"field":field,"index":index,"row":row})
    records=[]
    for month,rows in sorted(groups.items()):
        name=month+".jsonl.gz"
        write_gzip(directory/name,rows)
        records.append({"name":name,"sha256":file_sha(directory/name),"rows":len(rows)})
    manifest={"schema":CHECKPOINT_SCHEMA,"state_digest":state["digest"],
              "metadata":{k:v for k,v in state.items() if k not in STATE_FIELDS},
              "counts":counts,"partitions":records,"production_applied":False}
    manifest["digest"]=canonical_digest(manifest)
    (directory/"manifest.json").write_text(json.dumps(manifest,sort_keys=True)+chr(10))
    return manifest


def restore_state(directory):
    directory=Path(directory)
    manifest=json.loads((directory/"manifest.json").read_text())
    if (manifest.get("schema")!=CHECKPOINT_SCHEMA or manifest.get("digest")!=canonical_digest(
            {k:v for k,v in manifest.items() if k!="digest"}) or manifest.get("production_applied") is not False):
        raise ValueError("Invalid partition manifest")
    result=dict(manifest["metadata"])
    fields={field:{} for field in manifest["counts"]}
    if any(field not in STATE_FIELDS for field in fields):
        raise ValueError("Unexpected checkpoint field")
    names=set()
    import re
    for p in manifest["partitions"]:
        name=p["name"]
        if name in names or not re.fullmatch(r"[0-9]{4}-[0-9]{2}\.jsonl\.gz",name):
            raise ValueError("Invalid checkpoint partition identity")
        names.add(name)
        if file_sha(directory/name)!=p["sha256"]:
            raise ValueError("Partition checksum mismatch")
        n=0
        for item in read_rows(directory/name):
            field,index,row=item["field"],item["index"],item["row"]
            if (field not in fields or type(index) is not int or index<0
                    or index in fields[field] or utc_time(row["entry_utc"]).strftime("%Y-%m")!=name[:7]):
                raise ValueError("Invalid partition row identity")
            fields[field][index]=row
            n+=1
        if n!=p["rows"]:
            raise ValueError("Partition row count mismatch")
    for field,rows in fields.items():
        count=manifest["counts"][field]
        if set(rows)!=set(range(count)):
            raise ValueError("Missing checkpoint rows")
        result[field]=[rows[i] for i in range(count)]
    if (result.get("digest")!=manifest["state_digest"] or result["digest"]!=canonical_digest(
            {k:v for k,v in result.items() if k!="digest"})):
        raise ValueError("Restored state checksum mismatch")
    return result




COLD_SCHEMA="market_wide_cold_history_v1"

def cold_history(directory, expected):
    """Validate each immutable segment against the active state commitment."""
    directory=Path(directory)
    segments=[]
    seen=set()
    for rec in expected:
        name=rec["sha256"]+".jsonl.gz"
        if rec["sha256"] in seen or len(rec["sha256"])!=64 or any(c not in "0123456789abcdef" for c in rec["sha256"]):
            raise ValueError("Invalid cold segment identity")
        seen.add(rec["sha256"])
        if file_sha(directory/name)!=rec["sha256"]:
            raise ValueError("Cold history checksum mismatch")
        rows=list(read_rows(directory/name))
        if len(rows)!=1:
            raise ValueError("Invalid cold segment")
        segment=rows[0]
        if segment.get("schema")!=COLD_SCHEMA or segment["digest"]!=canonical_digest({k:v for k,v in segment.items() if k!="digest"}):
            raise ValueError("Invalid cold segment digest")
        if {k:len(segment[k]) for k in STATE_FIELDS}!=rec["counts"]:
            raise ValueError("Cold segment count mismatch")
        segments.append(segment)
    return segments


def compact_live_state(state,directory,*,previous_directory=None):
    """Seal old unrevisitable evidence while retaining active 72h windows.

    Completed and incomplete outcomes retain their exact original semantics.
    Archive an entire prospective batch together; never split matched groups.
    Historical evidence stays available to fitting and metric accounting.
    """
    import shutil
    if state.get("digest")!=canonical_digest({k:v for k,v in state.items() if k!="digest"}):
        raise ValueError("Invalid active state checksum")
    directory=Path(directory)
    directory.mkdir(parents=True,exist_ok=True)
    refs=list(state.get("cold_segments",[]))
    if refs:
        if previous_directory is None:
            raise ValueError("Missing prior cold history; refusing reset")
        cold_history(previous_directory,refs)
        for rec in refs:
            name=rec["sha256"]+".jsonl.gz"
            src=Path(previous_directory)/name
            dst=directory/name
            if src.resolve()!=dst.resolve():
                shutil.copyfile(src,dst)
    cutoff=utc_time(state["evaluation_asof_utc"])-timedelta(hours=72)
    old_anchor={a["prediction_id"] for a in state["anchors"] if utc_time(a["entry_utc"])<cutoff}
    groups=defaultdict(list)
    for p in state.get("shadow_predictions",[]):
        groups[p["batch_id"]].append(p)
    old_shadow={p["prediction_id"] for group in groups.values()
                if all(utc_time(p["entry_utc"])<cutoff for p in group) for p in group}
    active=dict(state)
    sealed={"schema":COLD_SCHEMA}
    for field in STATE_FIELDS:
        ids=old_anchor if field in ("anchors","outcomes") else old_shadow
        rows=state.get(field,[])
        sealed[field]=[row for row in rows if row["prediction_id"] in ids]
        active[field]=[row for row in rows if row["prediction_id"] not in ids]
        if len(sealed[field])+len(active[field])!=len(rows):
            raise ValueError("Cold split count mismatch")
    if any(sealed[k] for k in STATE_FIELDS):
        sealed["digest"]=canonical_digest(sealed)
        temporary=directory/"new-segment.jsonl.gz"
        write_gzip(temporary,[sealed])
        sha=file_sha(temporary)
        target=directory/(sha+".jsonl.gz")
        if target.exists():
            raise ValueError("Duplicate cold segment")
        temporary.rename(target)
        refs.append({"sha256":sha,"counts":{k:len(sealed[k]) for k in STATE_FIELDS}})
    active["cold_segments"]=refs
    active["digest"]=canonical_digest({k:v for k,v in active.items() if k!="digest"})
    # Require disjoint identities and whole batches across every retained segment.
    all_history=assemble_history(active,directory)
    for field in STATE_FIELDS:
        expected=len(state.get(field,[]))+sum(rec["counts"][field] for rec in state.get("cold_segments",[]))
        if len(all_history[field])!=expected:
            raise ValueError("Cold archive lost a retained row")
    return active


def assemble_history(state,directory):
    """Exact archive+active research history, with duplicate identity rejection."""
    segments=cold_history(directory,state.get("cold_segments",[]))
    result={}
    for field in STATE_FIELDS:
        by_key={}
        for group in segments+[state]:
            for row in group.get(field,[]):
                key=(row["prediction_id"],row["horizon_hours"]) if field in ("outcomes","shadow_outcomes") else row["prediction_id"]
                if key in by_key:
                    raise ValueError("Duplicate active/cold evidence identity")
                by_key[key]=row
        result[field]=[by_key[k] for k in sorted(by_key)]
    for a,o in (("anchors","outcomes"),("shadow_predictions","shadow_outcomes")):
        ids={row["prediction_id"] for row in result[a]}
        if any(row["prediction_id"] not in ids for row in result[o]):
            raise ValueError("Outcome missing source prediction")
    return result


def pack_seed_release(directory,archive):
    """Package only explicitly allowed compact seed files; never publish here."""
    import tarfile
    directory=Path(directory)
    manifest=json.loads((directory/"manifest.json").read_text())
    expected=[(x["kind"],x[source_key(x["kind"])[1]],x["cohort_sha256"]) for x in manifest["sources"]]
    load_seed(directory,expected)
    with Path(archive).open("wb") as raw, gzip.GzipFile(filename="",fileobj=raw,mode="wb",mtime=0) as compressed:
        with tarfile.open(fileobj=compressed,mode="w") as tar:
            for name in ["manifest.json"]+[x["seed_file"] for x in manifest["sources"]]:
                path=directory/name
                if not path.is_file() or path.is_symlink():
                    raise ValueError("Unexpected seed file")
                info=tarfile.TarInfo(name)
                info.size=path.stat().st_size
                info.mode=0o644
                info.mtime=0
                with path.open("rb") as payload:
                    tar.addfile(info,payload)
    return file_sha(archive)


def unpack_seed_release(archive,directory):
    """Do not extract arbitrary paths or links from an archive."""
    import re
    import tarfile
    directory=Path(directory)
    directory.mkdir(parents=True,exist_ok=True)
    names=set()
    with tarfile.open(archive,"r:gz") as tar:
        for member in tar:
            name=member.name
            if (not member.isfile() or name in names or member.size>512*1024*1024 or
                    not (name=="manifest.json" or re.fullmatch(r"source-[0-9]{2}\.jsonl\.gz",name))):
                raise ValueError("Unexpected training seed release member")
            names.add(name)
            with tar.extractfile(member) as raw, (directory/name).open("wb") as out:
                import shutil
                shutil.copyfileobj(raw,out)
    manifest=json.loads((directory/"manifest.json").read_text())
    if names!={"manifest.json"}|{r["seed_file"] for r in manifest["sources"]}:
        raise ValueError("Incomplete training seed release")
    expected=[(x["kind"],x[source_key(x["kind"])[1]],x["cohort_sha256"]) for x in manifest["sources"]]
    return load_seed(directory,expected)


def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest="command",required=True)
    q=sub.add_parser("seed")
    q.add_argument("--source",nargs=4,action="append",required=True,metavar=("KIND","PATH","SOURCE_SHA","COHORT_SHA"))
    q.add_argument("--directory",type=Path,required=True)
    q=sub.add_parser("pack")
    q.add_argument("--state",type=Path,required=True)
    q.add_argument("--directory",type=Path,required=True)
    q=sub.add_parser("restore")
    q.add_argument("--directory",type=Path,required=True)
    q.add_argument("--state",type=Path,required=True)
    q=sub.add_parser("pack-seed")
    q.add_argument("--directory",type=Path,required=True)
    q.add_argument("--archive",type=Path,required=True)
    q=sub.add_parser("unpack-seed")
    q.add_argument("--directory",type=Path,required=True)
    q.add_argument("--archive",type=Path,required=True)
    a=p.parse_args()
    if a.command=="pack-seed":
        print(pack_seed_release(a.directory,a.archive))
    elif a.command=="unpack-seed":
        print(json.dumps(unpack_seed_release(a.archive,a.directory),sort_keys=True))
    elif a.command=="seed":
        m=build_seed(a.source,a.directory)
        print(json.dumps(m,sort_keys=True))
    elif a.command=="pack":
        state=json.loads(a.state.read_text())
        m=pack_state(state,a.directory)
        if restore_state(a.directory)!=state:
            raise ValueError("Checkpoint round-trip mismatch")
        print(json.dumps({k:v for k,v in m.items() if k!="metadata"},sort_keys=True))
    else:
        a.state.write_text(json.dumps(restore_state(a.directory),sort_keys=True,separators=(",",":"))+chr(10))

if __name__=="__main__":
    main()
