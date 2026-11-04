import type {createCycleRunner} from "./cycle-runner";
import {unavailableA2Snapshot} from "./a2-snapshot";
/** Cached paper WATCH must expire at dashboard read time, not only ingestion. */
export function createCycleHttpHandler(runner:ReturnType<typeof createCycleRunner>,now:()=>Date=()=>new Date()){
 const safeLast=(last:any)=>{
  if(!last?.a2_snapshot||last.a2_snapshot.status!=="VERIFIED_SNAPSHOT")return last;
  const a=last.a2_snapshot,clock=now().getTime();
  const fresh=(value:string)=>{const t=Date.parse(value);return Number.isFinite(t)&&t<=clock&&clock-t<=600000};
  if(fresh(a.as_of)&&a.watch.every((candidate:any)=>fresh(candidate.quote_observed_at)))return last;
  return {...last,a2_snapshot:unavailableA2Snapshot("expired_at_dashboard_read"),paper_watch:[],paper_watch_status:"ABSTAIN_A2_EXPIRED",live_watch_certified:false};
 };
 return async (req:Request):Promise<Response>=>{
  const path=new URL(req.url).pathname;
  if(path==="/health"){const s=runner.snapshot();return Response.json({mode:"shadow",running:s.running,cycles:s.cycles,lastError:s.lastError})}
  if(path==="/dashboard"){const s=runner.snapshot();return Response.json({mode:"shadow",running:s.running,cycles:s.cycles,last_error:s.lastError,last_result:safeLast(s.last)})}
  if(path==="/cycle"){const result=await runner.run("manual");return Response.json(result.ok?result.result:{error:result.error},{status:result.status})}
  return Response.json({endpoints:["/health","/dashboard","/cycle"]});
 };
}
