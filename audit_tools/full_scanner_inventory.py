"""Read-only repository-wide scanner inventory. No deletion, merge, deployment or secrets."""
import ast, datetime, json, os, pathlib, re, subprocess, collections

ROOT=pathlib.Path(".")
def cmd(*args):
    try:
        p=subprocess.run(args,text=True,capture_output=True,timeout=120)
    except subprocess.TimeoutExpired as exc:
        return {"ok":False,"output":"","error":"Timed out after 120s: "+str(args[:3])}
    return {"ok":p.returncode==0,"output":p.stdout[:1000000],"error":p.stderr[:500]}
def gh(path):
    # Actions run history is very large: never paginate the entire repository.
    # Request one bounded page and project only the fields needed for evidence.
    if "/actions/runs?" in path:
        r=cmd("gh","api",path,"--jq",
              '{workflow_runs: [.workflow_runs[] | {id,name,event,status,conclusion,head_sha,created_at,run_started_at}]}')
    else:
        r=cmd("gh","api",path)
    if not r["ok"]: return {"error":r["error"]}
    try:
        text=r["output"].strip()
        if text.startswith("["):
            # gh --paginate may concatenate JSON arrays; parse each array if necessary
            decoder=json.JSONDecoder(); items=[]
            while text:
                obj,end=decoder.raw_decode(text);items.extend(obj if isinstance(obj,list) else [obj]);text=text[end:].strip()
            return items
        return json.loads(text)
    except Exception as exc:return {"error":str(exc)}
def gh_pages(resource, per_page=100, max_pages=20):
    """Fail closed on incomplete API pagination; never silently drop branches or PR files."""
    result=[]
    sep="&" if "?" in resource else "?"
    for page in range(1,max_pages+1):
        batch=gh(f"{resource}{sep}per_page={per_page}&page={page}")
        if not isinstance(batch,list):
            raise RuntimeError(f"GitHub pagination failure {resource} page {page}: {batch}")
        result.extend(batch)
        if len(batch)<per_page:
            return result
    raise RuntimeError(f"GitHub pagination limit reached for {resource}: {max_pages} pages")

def remote_main_blobs(main_sha, fetch=gh):
    """Enumerate the ACTUAL remote main tree, never the audit PR checkout.

    GitHub's recursive tree response can be truncated while still HTTP 200.
    Missing or truncated evidence must abort instead of implying path absence.
    """
    if not isinstance(main_sha,str) or not re.fullmatch(r"[0-9a-f]{40}",main_sha):
        raise RuntimeError("Remote main SHA missing or invalid")
    tree=fetch(f"repos/michaelrobinsonproduct-del/Cryptoscanner/git/trees/{main_sha}?recursive=1")
    if not isinstance(tree,dict) or tree.get("truncated") is not False or not isinstance(tree.get("tree"),list):
        raise RuntimeError("Remote main tree unavailable or truncated: cannot certify path overlap")
    blobs={}
    for entry in tree["tree"]:
        if not isinstance(entry,dict) or not isinstance(entry.get("path"),str) or entry.get("type") not in ("blob","tree"):
            raise RuntimeError("Malformed remote main tree entry")
        if entry["type"]=="blob":
            if entry["path"] in blobs or not isinstance(entry.get("sha"),str) or not re.fullmatch(r"[0-9a-f]{40}",entry["sha"]):
                raise RuntimeError("Duplicate path or invalid blob SHA in remote main tree")
            blobs[entry["path"]]=entry["sha"]
    return blobs


def remote_main_paths(main_sha, fetch=gh):
    """Backward-compatible path-only view of the exact remote main tree."""
    return set(remote_main_blobs(main_sha,fetch))


def compare_pr_blobs(changed, main_blobs):
    """Exact file-content equality is evidence; path overlap is not semantic parity."""
    result=[]
    for entry in changed:
        path=entry["filename"]
        pr_sha=entry.get("sha")
        main_sha=main_blobs.get(path)
        state=("NOT_ON_MAIN" if main_sha is None else
               "EXACT_BLOB_EQUAL" if pr_sha and pr_sha==main_sha else
               "DIFFERENT_BLOB_OR_UNKNOWN")
        result.append({"path":path,"pr_blob_sha":pr_sha,"main_blob_sha":main_sha,
                       "status":entry.get("status"),"comparison":state})
    return result


def reconcile_pr_snapshot(triage, pr_rows, current_main_sha, fetch_pr=gh):
    """Reconcile historical triage against CURRENT main, PR heads, and closed PRs.

    A matching filename or an old classification is never current semantic evidence.
    A snapshot classification is usable only while both main and PR head match.
    """
    prior_by_number={p["number"]:p for p in triage["prs"]}
    main_matches=triage.get("main_sha")==current_main_sha
    open_numbers=set()
    for p in pr_rows:
        n=p["number"]
        open_numbers.add(n)
        prior=prior_by_number.get(n,{})
        head_matches=prior.get("head_sha")==p["head_sha"]
        p["triage_snapshot_classification"]=prior.get("classification","unknown")
        p["triage_snapshot_main_matches"]=main_matches
        p["triage_snapshot_head_matches"]=head_matches
        p["triage_classification"]=prior.get("classification","unknown") if main_matches and head_matches else "unknown"
        p["classification_valid_for_current_main"]=main_matches and head_matches and bool(prior)
        p["triage_stale_reason"]=(
            "NEW_PR_NOT_IN_SNAPSHOT" if not prior else
            "MAIN_CHANGED_REQUIRES_SEMANTIC_REVIEW" if not main_matches else
            "PR_HEAD_CHANGED_REQUIRES_SEMANTIC_REVIEW" if not head_matches else None)
    closed=[]
    for n,prior in sorted(prior_by_number.items()):
        if n in open_numbers: continue
        current=fetch_pr(f"repos/michaelrobinsonproduct-del/Cryptoscanner/pulls/{n}")
        if not isinstance(current,dict) or current.get("state")!="closed":
            raise RuntimeError(f"PR #{n} missing from open list but closed state unverified: {current}")
        closed.append({"number":n,"snapshot_head_sha":prior.get("head_sha"),
                       "final_head_sha":current.get("head",{}).get("sha"),
                       "state":current["state"],"merged":bool(current.get("merged_at")),
                       "merged_at":current.get("merged_at"),
                       "merge_commit_sha":current.get("merge_commit_sha"),
                       "url":current.get("html_url"),
                       "snapshot_classification":prior.get("classification","unknown"),
                       "classification":"integrated" if current.get("merged_at") else "unknown",
                       "classification_basis":"GitHub merged_at, NOT semantic equivalence of any other PR" if current.get("merged_at") else "Closed without merge; semantic outcome unknown"})
    return closed

def build_consumer_graph(workflows, runtime, checkout_sha, main_sha):
    """Evidence-scoped dependency edges, not a certification of live invocation.

    Workflow edges come from the audit checkout. External edges come from a
    dated deployed-source snapshot and are explicitly NOT invocation proof.
    """
    edges=[]
    def edge(source,target,kind,evidence,observed_runtime=False):
        edges.append({"source":source,"target":target,"kind":kind,
                      "evidence":evidence,"observed_runtime":observed_runtime})
    for w in workflows:
        source="github-workflow:"+w["path"]
        for script in w["scripts"]:
            edge(source,"repo-script:"+script,"invokes_script",
                 "audit_checkout:"+checkout_sha)
        for module in w["python_modules"]:
            edge(source,"python-module:"+module,"invokes_module",
                 "audit_checkout:"+checkout_sha)
        if w["ledger_ref"]:
            edge(source,"github-ref:paper-proof-ledger","mentions_ledger_ref",
                 "audit_checkout:"+checkout_sha)
        for ref in w.get("branch_references",{}).get("checkout_refs",[]):
            edge(source,"github-ref:"+ref,"explicit_checkout_ref",
                 "audit_checkout:"+checkout_sha)
        for ref in w.get("branch_references",{}).get("branch_ref_mentions",[]):
            edge(source,"github-ref:"+ref,"static_branch_ref_mention",
                 "audit_checkout:"+checkout_sha)
    sb=runtime.get("supabase",{})
    for item in sb.get("sample_source_consumers",[])+sb.get("source_review",{}).get("additional_direct_table_consumers",[]):
        source="supabase-edge:"+item["function"]
        for table in item.get("tables",[]):
            edge(source,"supabase-table:"+table,"static_table_reference",
                 "external_snapshot:"+runtime["snapshot_utc"])
        for rpc in item.get("rpc",[]):
            edge(source,"supabase-rpc:"+rpc,"static_rpc_reference",
                 "external_snapshot:"+runtime["snapshot_utc"])
    static=runtime.get("static_consumers",{})
    if static.get("ios",{}).get("endpoint"):
        edge("ios:"+static["ios"]["source"],"railway-url:"+static["ios"]["endpoint"],
             "hardcoded_endpoint","external_snapshot:"+runtime["snapshot_utc"])
    for endpoint_key in ("collector_endpoint","confirmation_endpoint"):
        endpoint=static.get("bun",{}).get(endpoint_key)
        if endpoint:
            for source in static["bun"].get("sources",[]):
                edge("bun:"+source,"railway-url:"+endpoint,
                     "reported_static_endpoint","external_snapshot:"+runtime["snapshot_utc"])
    return {"schema":"cryptoscanner-consumer-graph-v1",
            "audit_checkout_sha":checkout_sha,"remote_main_sha":main_sha,
            "external_snapshot_utc":runtime["snapshot_utc"],
            "scope":"Partial static references only; not deployed caller reachability, pg_cron, dynamic references, or invocation evidence",
            "edges":sorted(edges,key=lambda e:(e["source"],e["target"],e["kind"])),
            "unknowns":["Supabase invocation/pg_cron and database schema",
                        "iOS client deployment and users",
                        "Bun external callers and Railway retained storage consumers",
                        "GitHub workflow dynamic shell dispatch and branch-pinned consumers"],
            "cleanup_authorized":False}



def workflow_branch_references(source):
    """Static checkout and durable branch refs, not live invocation evidence."""
    if not isinstance(source,str):
        raise ValueError("Workflow source must be text")
    lines=source.splitlines()
    checkouts=set()
    unresolved=[]
    for i,line in enumerate(lines):
        match=re.match(r"^(\s*)-\s+uses:\s*actions/checkout@[^\s#]+",line)
        if not match:
            continue
        indent=len(match.group(1))
        for following in lines[i+1:]:
            if re.match(r"^\s*-\s+(?:uses|name|run):",following) and len(following)-len(following.lstrip())<=indent:
                break
            ref=re.match(r"^\s+ref:\s*(.*?)\s*(?:#.*)?$",following)
            if ref:
                value=ref.group(1).strip().strip("'\"")
                if "$" in value or not re.fullmatch(r"[A-Za-z0-9._/-]+",value):
                    unresolved.append(value)
                else:
                    checkouts.add(value)
                break
    mentions=set()
    for line in lines:
        if not line.lstrip().startswith("#"):
            mentions.update(re.findall(r"refs/heads/([A-Za-z0-9._/-]+)",line))
    return {"checkout_refs":sorted(checkouts),
            "branch_ref_mentions":sorted(mentions),
            "unresolved_checkout_refs":sorted(set(unresolved))}


def main():
    tracked=cmd("git","ls-files")
    if not tracked["ok"]:
        raise RuntimeError("Unable to enumerate exact checkout tracked files: "+tracked["error"])
    files=tracked["output"].splitlines()
    workflows=[p for p in files if p.startswith(".github/workflows/") and p.endswith((".yml",".yaml"))]
    pyfiles=[p for p in files if p.endswith(".py")]
    imports=collections.defaultdict(list)
    for f in pyfiles:
        try:
            tree=ast.parse(pathlib.Path(f).read_text())
            for n in ast.walk(tree):
                if isinstance(n,ast.ImportFrom) and n.module: imports[n.module].append(f)
                if isinstance(n,ast.Import):
                    for alias in n.names:imports[alias.name].append(f)
        except (SyntaxError,UnicodeError):pass
    workflow_inventory=[]
    for p in workflows:
        s=pathlib.Path(p).read_text()
        workflow_inventory.append({"path":p,"schedule_cron":re.findall(r"cron:\s*([^\n]+)",s),
          "has_dispatch":"workflow_dispatch:" in s,"has_schedule":bool(re.search(r"^\s*schedule:",s,re.M)),
          "writes_contents":bool(re.search(r"contents:\s*write",s)),
          "ledger_ref":"paper-proof-ledger" in s,
          "python_modules":sorted(set(re.findall(r"python\s+-m\s+([A-Za-z0-9_.]+)",s))),
          "scripts":sorted(set(re.findall(r"(?:python|bun|node)\s+([A-Za-z0-9_./-]+\.(?:py|ts|mjs))",s))),
          "branch_references":workflow_branch_references(s)})
    triage=json.loads((ROOT/"audit_tools/pr_triage_20261102.json").read_text())
    triage_by_number={p["number"]:p for p in triage["prs"]}
    main_ref=gh("repos/michaelrobinsonproduct-del/Cryptoscanner/git/ref/heads/main")
    main_sha=main_ref.get("object",{}).get("sha") if isinstance(main_ref,dict) else None
    main_blobs=remote_main_blobs(main_sha)
    main_files=set(main_blobs)
    prs=gh_pages("repos/michaelrobinsonproduct-del/Cryptoscanner/pulls?state=open")
    pr_rows=[]
    if isinstance(prs,list):
        for p in prs:
            n=p["number"]
            changed=gh_pages(f"repos/michaelrobinsonproduct-del/Cryptoscanner/pulls/{n}/files")
            changed_files=[x["filename"] for x in changed] if isinstance(changed,list) else []
            overlaps=[f for f in changed_files if f in main_files]
            blob_comparisons=compare_pr_blobs(changed,main_blobs)
            prior=triage_by_number.get(n,{})
            same_head=prior.get("head_sha")==p["head"]["sha"]
            classification=prior.get("classification","unknown") if (same_head or n==121) else "unknown"
            pr_rows.append({"number":n,"title":p["title"],"head_sha":p["head"]["sha"],"head_ref":p["head"]["ref"],
                "triage_classification":classification,"triage_snapshot_head_matches":same_head,
                "triage_reason":prior.get("reason","No prior semantic classification"),
                "base_sha":p["base"]["sha"],"draft":p["draft"],"mergeable":p.get("mergeable"),
                "files":changed_files,"already_on_main_paths":overlaps,
                "exact_main_blob_matches":[x["path"] for x in blob_comparisons if x["comparison"]=="EXACT_BLOB_EQUAL"],
                "file_blob_comparisons":blob_comparisons,
                "file_api_error":changed.get("error") if isinstance(changed,dict) else None,
                "requires_semantic_review":True,"url":p["html_url"]})
    branches=gh_pages("repos/michaelrobinsonproduct-del/Cryptoscanner/branches")
    ledger_ref=gh("repos/michaelrobinsonproduct-del/Cryptoscanner/git/ref/heads/paper-proof-ledger")
    runs_response=gh("repos/michaelrobinsonproduct-del/Cryptoscanner/actions/runs?per_page=30")
    runs=runs_response.get("workflow_runs",[]) if isinstance(runs_response,dict) else []
    closed_prs_since_snapshot=reconcile_pr_snapshot(triage,pr_rows,main_ref.get("object",{}).get("sha")) if isinstance(prs,list) else []
    external_runtime=json.loads((ROOT/"audit_tools/external_runtime_20261102.json").read_text())
    runtime_snapshot_main_matches=external_runtime.get("repo_main_sha")==main_ref.get("object",{}).get("sha")
    errors={"prs":prs.get("error") if isinstance(prs,dict) else None,
            "branches":branches.get("error") if isinstance(branches,dict) else None,
            "runs":runs_response.get("error") if isinstance(runs_response,dict) else "Invalid runs response",
            "main_ref":main_ref.get("error") if isinstance(main_ref,dict) else "Invalid main ref",
            "ledger_ref":ledger_ref.get("error") if isinstance(ledger_ref,dict) else "Invalid ledger ref"}
    for p in pr_rows:
        if p.get("file_api_error"):
            errors["pr_files_"+str(p["number"])]=p["file_api_error"]
    if any(errors.values()) or not isinstance(prs,list) or not isinstance(branches,list):
        raise RuntimeError("Incomplete GitHub audit inventory: "+json.dumps(errors))
    package=json.loads((ROOT/"package.json").read_text()) if "package.json" in files else {}
    legacy_files=[p for p in files if p.startswith(("simple_scanner/","scanner/src/","evaluation/"))]
    data={"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "checkout_sha":cmd("git","rev-parse","HEAD")["output"].strip(),
        "main_sha":main_ref.get("object",{}).get("sha"),
        "ledger_sha":ledger_ref.get("object",{}).get("sha"),
        "files":files,"checkout_files":files,"main_files":sorted(main_files),
        "main_blob_shas":main_blobs,
        "main_workflows":sorted(p for p in main_files if p.startswith(".github/workflows/") and p.endswith((".yml",".yaml"))),
        "workflow_inventory":workflow_inventory,"python_imports":dict(imports),
        "package_scripts":package.get("scripts",{}),"legacy_files":legacy_files,
        "triage_snapshot_main_sha":triage.get("main_sha"),
        "triage_snapshot_main_matches":triage.get("main_sha")==main_ref.get("object",{}).get("sha"),
        "external_runtime_snapshot_utc":external_runtime.get("snapshot_utc"),
        "external_runtime_snapshot_main_sha":external_runtime.get("repo_main_sha"),
        "external_runtime_snapshot_main_matches":runtime_snapshot_main_matches,
        "closed_prs_since_snapshot":closed_prs_since_snapshot,
        "new_prs_since_snapshot":[p["number"] for p in pr_rows if p["triage_stale_reason"]=="NEW_PR_NOT_IN_SNAPSHOT"],
        "open_prs":pr_rows,"branches":branches,
        "recent_runs":[{"id":r.get("id"),"name":r.get("name"),"event":r.get("event"),"status":r.get("status"),
          "conclusion":r.get("conclusion"),"head_sha":r.get("head_sha"),"created_at":r.get("created_at"),
          "run_started_at":r.get("run_started_at")} for r in runs] if isinstance(runs,list) else [],
        "api_errors":errors,
        "run_scope":"latest 30 repository-wide GitHub Actions runs, not complete history",
        "branch_scope":"all branches across every API page, fail-closed if incomplete"}
    out=ROOT/"audit-evidence";out.mkdir(exist_ok=True)
    graph=build_consumer_graph(workflow_inventory,external_runtime,data["checkout_sha"],data["main_sha"])
    (out/"consumer-graph.json").write_text(json.dumps(graph,indent=2,sort_keys=True)+"\n")
    (out/"scanner-inventory.json").write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
    lines=["# Scanner runtime and legacy inventory (read-only)","",
      f"Generated UTC: {data['created_utc']}","",
      f"Audit checkout SHA: `{data['checkout_sha']}`; remote main: `{data['main_sha']}`; remote ledger: `{data['ledger_sha']}`","",
      f"Audit checkout files: {len(files)}; remote main files: {len(main_files)}; checkout workflows: {len(workflows)}; remote main workflows: {len(data['main_workflows'])}; open PRs: {len(pr_rows)}; branches: {len(branches)}","",
      "## Workflow inventory","",
      "| Workflow | Cron | Dispatch | Contents write | Ledger reference |","|---|---|---|---|---|"]
    for w in workflow_inventory:
        lines.append(f"| {w['path']} | {', '.join(w['schedule_cron']) or '-'} | {w['has_dispatch']} | {w['writes_contents']} | {w['ledger_ref']} |")
    lines+=["","## All open PRs (path overlap is NOT proof of equivalent behavior)","",
       "| PR | Head SHA | Triage | Snapshot head match | Changed files | Actual main path overlaps | Exact blob matches |","|---|---|---|---|---:|---:|---:|"]
    for p in pr_rows:lines.append(f"| [#{p['number']}]({p['url']}) | `{p['head_sha'][:12]}` | {p['triage_classification']} | {p['triage_snapshot_head_matches']} | {len(p['files'])} | {len(p['already_on_main_paths'])} | {len(p['exact_main_blob_matches'])} |")
    lines+=["","## Snapshot drift / closed PR reconciliation","",
      f"Triage snapshot main matches current main: {data['triage_snapshot_main_matches']}",
      f"External runtime snapshot main matches current main: {data['external_runtime_snapshot_main_matches']}",
      "A mismatch means historical runtime observations and PR classifications are NOT revalidated against current main.",
      ""]
    for p in closed_prs_since_snapshot:
        lines.append(f"- PR #{p['number']}: {'MERGED' if p['merged'] else 'CLOSED WITHOUT MERGE'}, final head `{p['final_head_sha']}`, merge `{p['merge_commit_sha']}` (snapshot had `{p['snapshot_head_sha']}`).")
    lines+=["","## Static consumer graph","",
      f"Evidence-scoped edges: {len(graph['edges'])}; graph artifact: consumer-graph.json",
      "All external runtime invocation status remains unverified; no cleanup authorization.",
      "","## Evidence boundaries","",
      "- This is a machine-generated source and GitHub inventory, not proof of live deployment or functional equivalence.",
      "- PR triage is a dated human review snapshot; drifted heads revert to unknown. The audit PR's own head necessarily advances as this inventory evolves.",
      "- Remote main path and blob comparisons use the exact SHA-bound Git tree, not the audit checkout; exact matching blobs prove only identical individual files, not whole-PR integration.",
      "- Existing paths do not mean a PR's implementation is already merged.",
      "- Branches, PRs and workflows are not deleted or changed by this audit.",
      "- Runtime identification requires corroborating actual successful runs, deployment identity, and ledger history.",
      "- PR retirement must be based on semantic diff and confirmed consumers, not filename overlap."]
    (out/"scanner-inventory.md").write_text("\n".join(lines)+"\n")
    print(f"INVENTORY files={len(files)} workflows={len(workflows)} prs={len(pr_rows)} branches={len(branches) if isinstance(branches,list) else 'unknown'}")
if __name__=="__main__":main()
