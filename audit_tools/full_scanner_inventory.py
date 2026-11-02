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
        r=cmd("gh","api",path,"--paginate")
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
def main():
    files=cmd("git","ls-files")["output"].splitlines()
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
          "scripts":sorted(set(re.findall(r"(?:python|bun|node)\s+([A-Za-z0-9_./-]+\.(?:py|ts|mjs))",s)))})
    prs=gh("repos/michaelrobinsonproduct-del/Cryptoscanner/pulls?state=open&per_page=100")
    pr_rows=[]
    if isinstance(prs,list):
        for p in prs:
            n=p["number"]
            changed=gh(f"repos/michaelrobinsonproduct-del/Cryptoscanner/pulls/{n}/files?per_page=100")
            changed_files=[x["filename"] for x in changed] if isinstance(changed,list) else []
            overlaps=[f for f in changed_files if f in files]
            pr_rows.append({"number":n,"title":p["title"],"head_sha":p["head"]["sha"],"head_ref":p["head"]["ref"],
                "base_sha":p["base"]["sha"],"draft":p["draft"],"mergeable":p.get("mergeable"),
                "files":changed_files,"already_on_main_paths":overlaps,
                "file_api_error":changed.get("error") if isinstance(changed,dict) else None,
                "requires_semantic_review":True,"url":p["html_url"]})
    branches=gh("repos/michaelrobinsonproduct-del/Cryptoscanner/branches?per_page=100")
    main_ref=gh("repos/michaelrobinsonproduct-del/Cryptoscanner/git/ref/heads/main")
    ledger_ref=gh("repos/michaelrobinsonproduct-del/Cryptoscanner/git/ref/heads/paper-proof-ledger")
    runs_response=gh("repos/michaelrobinsonproduct-del/Cryptoscanner/actions/runs?per_page=30")
    runs=runs_response.get("workflow_runs",[]) if isinstance(runs_response,dict) else []
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
    data={"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "checkout_sha":cmd("git","rev-parse","HEAD")["output"].strip(),
        "main_sha":main_ref.get("object",{}).get("sha"),
        "ledger_sha":ledger_ref.get("object",{}).get("sha"),
        "files":files,"workflow_inventory":workflow_inventory,"python_imports":dict(imports),
        "open_prs":pr_rows,"branches":branches,
        "recent_runs":[{"id":r.get("id"),"name":r.get("name"),"event":r.get("event"),"status":r.get("status"),
          "conclusion":r.get("conclusion"),"head_sha":r.get("head_sha"),"created_at":r.get("created_at"),
          "run_started_at":r.get("run_started_at")} for r in runs] if isinstance(runs,list) else [],
        "api_errors":errors,
        "run_scope":"latest 30 repository-wide GitHub Actions runs, not complete history",
        "branch_scope":"all branches returned by paginated GitHub API"}
    out=ROOT/"audit-evidence";out.mkdir(exist_ok=True)
    (out/"scanner-inventory.json").write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
    lines=["# Scanner runtime and legacy inventory (read-only)","",
      f"Generated UTC: {data['created_utc']}","",
      f"Audit checkout SHA: `{data['checkout_sha']}`; remote main: `{data['main_sha']}`; remote ledger: `{data['ledger_sha']}`","",
      f"Tracked files: {len(files)}; workflows: {len(workflows)}; open PRs: {len(pr_rows)}","",
      "## Workflow inventory","",
      "| Workflow | Cron | Dispatch | Contents write | Ledger reference |","|---|---|---|---|---|"]
    for w in workflow_inventory:
        lines.append(f"| {w['path']} | {', '.join(w['schedule_cron']) or '-'} | {w['has_dispatch']} | {w['writes_contents']} | {w['ledger_ref']} |")
    lines+=["","## All open PRs (path overlap is NOT proof of equivalent behavior)","",
       "| PR | Head SHA | Changed files | Paths already present on main |","|---|---|---:|---:|"]
    for p in pr_rows:lines.append(f"| [#{p['number']}]({p['url']}) | `{p['head_sha'][:12]}` | {len(p['files'])} | {len(p['already_on_main_paths'])} |")
    lines+=["","## Evidence boundaries","",
      "- This is a machine-generated source and GitHub inventory, not proof of live deployment or functional equivalence.",
      "- Existing paths do not mean a PR's implementation is already merged.",
      "- Branches, PRs and workflows are not deleted or changed by this audit.",
      "- Runtime identification requires corroborating actual successful runs, deployment identity, and ledger history.",
      "- PR retirement must be based on semantic diff and confirmed consumers, not filename overlap."]
    (out/"scanner-inventory.md").write_text("\n".join(lines)+"\n")
    print(f"INVENTORY files={len(files)} workflows={len(workflows)} prs={len(pr_rows)} branches={len(branches) if isinstance(branches,list) else 'unknown'}")
if __name__=="__main__":main()
