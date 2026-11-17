"""Read-only Cloudflare diagnostics. Public CI output strictly allowlisted."""
import json, os, time, re, urllib.request, urllib.error, datetime
TOKEN=os.environ.get("CLOUDFLARE_API_TOKEN","")
ACCOUNT="a54fdd300aa0160b9c8e50d520e71ed1"
NAME="cryptoscanner-independent-scheduler"
BASE="https://api.cloudflare.com/client/v4"
ROOT=f"/accounts/{ACCOUNT}/workers/scripts/{NAME}"
def emit(kind, **data):
    print(json.dumps({"diagnostic":kind,**data}),flush=True)
def call(label,path,body=None):
    req=urllib.request.Request(BASE+path,data=None if body is None else json.dumps(body).encode(),
        headers={"Authorization":"Bearer "+TOKEN,"Content-Type":"application/json","User-Agent":"Cryptoscanner-diagnostic"},
        method="GET" if body is None else "POST")
    try:
        with urllib.request.urlopen(req,timeout=25) as res:
            obj=json.load(res)
            emit(label,http=res.status,success=obj.get("success") is True)
            return obj.get("result")
    except urllib.error.HTTPError as e:
        try: codes=[x.get("code") for x in json.load(e).get("errors",[]) if isinstance(x.get("code"),int)]
        except Exception: codes=[]
        emit(label,http=e.code,error_codes=codes,content_type=("json" if "json" in e.headers.get("Content-Type","") else "other"))
    except Exception as e:
        emit(label,error_type=type(e).__name__)
    return None
def safeid(x):
    return x if isinstance(x,str) and re.fullmatch("[a-fA-F0-9-]{32,36}",x) else None
if not TOKEN:
    emit("TOKEN",present=False)
    raise SystemExit(1)
emit("TOKEN",present=True)
# Only inspect this Worker; never print secret values, raw response or unrelated account data.
for label,path in [("USER_TOKEN_VERIFY","/user/tokens/verify"),("ACCOUNT_TOKEN_VERIFY",f"/accounts/{ACCOUNT}/tokens/verify"),("SCRIPT_SETTINGS",ROOT+"/script-settings"),("LIST_WORKERS",f"/accounts/{ACCOUNT}/workers/scripts")]:
    reply=call(label,path)
    if label.endswith("VERIFY") and isinstance(reply,dict):emit(label+"_STATE",active=reply.get("status")=="active")
    if label=="LIST_WORKERS" and isinstance(reply,list):
        emit("WORKER_FOUND",count=len(reply),present=any(x.get("id")==NAME for x in reply),scanner_names=[x.get("id") for x in reply if isinstance(x.get("id"),str) and re.fullmatch(r"cryptoscanner[-a-zA-Z0-9]*",x["id"])])
        for x in reply:
            n=x.get("id")
            if isinstance(n,str) and n!=NAME and re.fullmatch(r"cryptoscanner[-a-zA-Z0-9]*",n):
                alt=f"/accounts/{ACCOUNT}/workers/scripts/{n}"
                call("ALTERNATE_SETTINGS",alt+"/settings")
                call("ALTERNATE_SCHEDULES",alt+"/schedules")
a=call("ACCOUNT_LIST","/accounts")
if isinstance(a,list):emit("ACCOUNT_SCOPE",count=len(a),expected_account_visible=any(x.get("id")==ACCOUNT for x in a))
s=call("SETTINGS",ROOT+"/settings")
if isinstance(s,dict):
    bindings=s.get("bindings",[])
    emit("CONFIG",github_token_binding=any(b.get("name")=="GITHUB_TOKEN" and b.get("type")=="secret_text" for b in bindings),
         enabled_value=next((b.get("text")=="true" for b in bindings if b.get("name")=="ENABLED"),None),
         scheduler_binding=any(b.get("name")=="SCHEDULER" and b.get("type")=="durable_object_namespace" for b in bindings),
         observability_enabled=(s.get("observability") or {}).get("enabled"),
         compatibility_date=s.get("compatibility_date") if re.fullmatch(r"\d{4}-\d{2}-\d{2}",str(s.get("compatibility_date"))) else None)
s=call("SCHEDULES",ROOT+"/schedules")
if isinstance(s,dict): s=s.get("schedules",[])
if isinstance(s,list): emit("CRON",schedules=[x["cron"] for x in s if isinstance(x,dict) and re.fullmatch(r"[0-9*/ ,\-]+",str(x.get("cron","")))])
s=call("DEPLOYMENTS",ROOT+"/deployments")
if isinstance(s,dict):
    emit("DEPLOYMENT",versions=[{"id":safeid(v.get("version_id")),"percentage":v.get("percentage")} for d in s.get("deployments",[])[:1] for v in d.get("versions",[])])
now=int(time.time()*1000)
# Query stored logs. Only structured scheduler statuses and invocation metadata are emitted.
q={"queryId":"cryptoscanner-runtime-diagnostic","timeframe":{"from":now-12*3600000,"to":now},"limit":500,
   "parameters":{"datasets":[],"filters":[{"key":"$metadata.service","operation":"eq","type":"string","value":NAME}],"filterCombination":"and","view":"events"}}
s=call("TELEMETRY","/accounts/"+ACCOUNT+"/workers/observability/telemetry/query",q)
if isinstance(s,dict):
    ev=s.get("events") or {}
    events=ev.get("events") or []
    emit("EVENT_COUNT",count=ev.get("count"),returned=len(events),has_events="events" in s,has_run="run" in s,known_sections=[k for k in ("run","statistics","events","invocations","calculations","traces","series") if k in s])
    run=s.get("run") or {}
    if isinstance(run,dict):emit("QUERY_STATE",status=run.get("status") if run.get("status") in ("completed","success","failed","error","running","pending","COMPLETED","SUCCESS","FAILED","ERROR","RUNNING","PENDING") else None)
    for e in sorted(events,key=lambda e:e.get("timestamp",0)):
        source=e.get("source")
        meta=e.get("$metadata") or {}
        w=e.get("$workers") or {}
        if w.get("scriptName") not in (None,NAME) or meta.get("service") not in (None,NAME): continue
        parsed=None
        for v in [source,source.get("message") if isinstance(source,dict) else None,meta.get("message")]:
            if isinstance(v,list) and len(v)==1:v=v[0]
            if isinstance(v,str):
                try:v=json.loads(v)
                except Exception:continue
            if isinstance(v,dict) and isinstance(v.get("status"),str):parsed=v;break
        out={"timestamp":e.get("timestamp")}
        for k in ("eventType","outcome"):
            v=w.get(k)
            if isinstance(v,str) and re.fullmatch(r"[A-Za-z_]{1,40}",v):out[k]=v
        for k in ("wallTimeMs","cpuTimeMs"):
            if isinstance(w.get(k),(int,float)):out[k]=w[k]
        if parsed:
            for k in ("status","stage","result","error"):
                v=parsed.get(k)
                if isinstance(v,str) and re.fullmatch(r"[A-Z_0-9]{1,70}",v):out[k]=v
            for k in ("slot","scheduled","runId","elapsed_ms","http_status","historyCount"):
                v=parsed.get(k)
                if isinstance(v,(int,float)) or isinstance(v,str) and re.fullmatch(r"[0-9]{1,20}",v):out[k]=v
        # Map known error signatures; never print free-form messages.
        err=str(meta.get("error",""))+" "+str(meta.get("message",""))+" "+str(source)
        signatures={"TIMEOUT":r"timed?\s*out|timeout","RPC":r"rpc|durable object","FETCH":r"fetch|network","LIMIT":r"exceeded|limit","AUTH":r"unauthorized|forbidden|authentication","TYPE_ERROR":r"TypeError","ABORT":r"AbortError","NO_SUCH_METHOD":r"not a function|no such method","EXCEPTION":r"exception"}
        found=[k for k,v in signatures.items() if re.search(v,err,re.I)]
        if found:out["error_categories"]=found
        if len(out)>1:emit("EVENT",**out)

# No-filter key discovery: only report whether the known worker fields exist.
k=call("TELEMETRY_KEYS","/accounts/"+ACCOUNT+"/workers/observability/telemetry/keys",{"timeframe":{"from":now-12*3600000,"to":now},"datasets":[]})
if isinstance(k,list):emit("KEYS",count=len(k),service_key=any(x.get("key")=="$metadata.service" for x in k),script_key=any(x.get("key")=="$workers.scriptName" for x in k))
