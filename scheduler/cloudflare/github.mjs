import {REPO,WRITER} from "./core.mjs";
export const REQUEST_TIMEOUT_MS=25000;
const stageFor=(path,body)=>{
  if(body) return "DISPATCH";
  if(path.startsWith("contents/")) return "LEDGER_READ";
  if(path==="git/ref/heads/main") return "MAIN_REF";
  if(path.startsWith("actions/runs/")) return "RUN_READ";
  if(path.startsWith("actions/workflows/")){
    const workflow=path.startsWith("actions/workflows/"+WRITER+"/")?"WRITER":"RELAY";
    const status=path.match(/[?&]status=(queued|in_progress|waiting|pending|requested)(?:&|$)/)?.[1];
    return status?workflow+"_ACTIVE_"+status.toUpperCase():workflow+"_HISTORY";
  }
  return "OTHER";
};
// Safe diagnostics only: never log token, request body, URL or response body.
export function github(env,{fetcher=fetch,log=console.log,clock=Date.now,timeoutSignal=ms=>AbortSignal.timeout(ms)}={}) {
  if(!env.GITHUB_TOKEN) throw Error("MISSING_GITHUB_TOKEN");
  return async(path,body)=>{
    const stage=stageFor(path,body), start=clock();
    const headers={Authorization:"Bearer "+env.GITHUB_TOKEN,
      Accept:path.startsWith("contents/")?"application/vnd.github.raw+json":"application/vnd.github+json",
      "X-GitHub-Api-Version":"2026-03-10","User-Agent":"cryptoscanner-independent-scheduler"};
    if(body) headers["Content-Type"]="application/json";
    const signal=timeoutSignal(REQUEST_TIMEOUT_MS);
    log(JSON.stringify({status:"GITHUB_REQUEST_STARTED",stage}));
    try {
      const res=await fetcher("https://api.github.com/repos/"+REPO+"/"+path,
        {method:body?"POST":"GET",headers,body:body?JSON.stringify(body):undefined,
         signal,redirect:"error"});
      if(!res.ok) throw Error("GITHUB_HTTP_"+res.status);
      const result=await res.json();
      log(JSON.stringify({status:"GITHUB_REQUEST_OK",stage,http_status:res.status,elapsed_ms:clock()-start}));
      return result;
    } catch(error) {
      const status=/^GITHUB_HTTP_\d{3}$/.test(error?.message)?error.message:
        signal.aborted||error?.name==="TimeoutError"?"GITHUB_REQUEST_TIMEOUT":
        error?.name==="SyntaxError"?"GITHUB_RESPONSE_INVALID":"GITHUB_TRANSPORT_ERROR";
      log(JSON.stringify({status,stage,elapsed_ms:clock()-start}));
      throw Error(status);
    }
  };
}
