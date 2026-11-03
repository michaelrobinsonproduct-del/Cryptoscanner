/** Read-only D source pipeline health; does not certify quote freshness or promote scoring. */
export type SourceRunHealth={status:"SOURCE_QUERY_FAILED"|"FAILURES_OBSERVED"|"RUNS_PENDING"|"NO_RECENT_RUNS"|"NO_FAILURES_OBSERVED"|"UNAVAILABLE";observed_run_count:number;failed_count:number;pending_count:number;observed_at:string|null;production_applied:false;reason?:string};
export const unavailableSourceHealth=(reason:string):SourceRunHealth=>({status:"UNAVAILABLE",observed_run_count:0,failed_count:0,pending_count:0,observed_at:null,production_applied:false,reason});
export function createSourceHealthReader(path:string|undefined,sha:string|undefined,read:(p:string)=>Promise<Uint8Array>=p=>Bun.file(p).bytes()):()=>Promise<SourceRunHealth>{
 return async()=>{
  if(!path?.startsWith("/")||path.includes("\0")||!/^[a-f0-9]{64}$/i.test(sha||""))throw Error("untrusted_source_health");
  const bytes=await read(path);
  if(bytes.byteLength>100000)throw Error("oversized_source_health");
  const hash=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes))).map(v=>v.toString(16).padStart(2,"0")).join("");
  if(hash!==sha!.toLowerCase())throw Error("source_health_digest_mismatch");
  const x=JSON.parse(new TextDecoder("utf-8",{fatal:true}).decode(bytes));
  const statuses=["SOURCE_QUERY_FAILED","FAILURES_OBSERVED","RUNS_PENDING","NO_RECENT_RUNS","NO_FAILURES_OBSERVED"];
  if(x.schema!=="paper_source_run_health_v1"||x.production_applied!==false||x.window_hours!==24||!statuses.includes(x.status)||typeof x.query_verified!=="boolean"||!Array.isArray(x.runs)||x.runs.length>100||!Number.isFinite(Date.parse(x.observed_at)))throw Error("invalid_source_health");
  if(x.runs.some((r:any)=>!Number.isInteger(r.run_id)||r.run_id<=0||!["schedule","workflow_dispatch"].includes(r.event)||!["completed","queued","in_progress","waiting","pending","requested"].includes(r.status)||!Number.isFinite(Date.parse(r.created_at))||!/^[a-f0-9]{40}$/i.test(r.source_sha||"")||typeof r.url!=="string"||!r.url.startsWith("https://github.com/")))throw Error("invalid_source_health_run");
  if((x.status==="SOURCE_QUERY_FAILED")!==(!x.query_verified))throw Error("source_health_query_status_mismatch");
  const failed=x.runs.filter((r:any)=>["failure","timed_out","cancelled","action_required","startup_failure"].includes(r.conclusion)).length;
  const pending=x.runs.filter((r:any)=>r.status!=="completed").length;
  if(x.failed_count!==failed||x.pending_count!==pending||x.observed_run_count!==x.runs.length)throw Error("source_health_counts_mismatch");
  const expected=!x.query_verified?"SOURCE_QUERY_FAILED":failed?"FAILURES_OBSERVED":pending?"RUNS_PENDING":!x.runs.length?"NO_RECENT_RUNS":"NO_FAILURES_OBSERVED";
  if(x.status!==expected)throw Error("source_health_state_mismatch");
  return {status:x.status,observed_run_count:x.runs.length,failed_count:failed,pending_count:pending,observed_at:x.observed_at,production_applied:false};
 };
}
