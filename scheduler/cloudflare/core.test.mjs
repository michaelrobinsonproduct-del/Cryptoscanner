import test from "node:test";
import assert from "node:assert/strict";
import {tick,verified,WRITER} from "./core.mjs";
const now=Date.parse("2026-11-17T01:34:00Z"), source="a".repeat(40), sum="b".repeat(64);
function rig(overrides={}) {
  const data=new Map(),calls=[];
  const store={get:async k=>data.get(k),put:async(k,v)=>data.set(k,v)};
  const api=async(path,body)=>{
    calls.push([path,body]);
    if(overrides[path]) return overrides[path](body);
    if(path.includes("/runs?")) return {total_count:0,workflow_runs:[]};
    if(path.startsWith("contents/")) return {as_of:new Date(now-601000).toISOString()};
    if(path==="git/ref/heads/main") return {object:{sha:source}};
    if(path.endsWith("/dispatches")) return {workflow_run_id:123};
    throw Error(path);
  };
  const go=(extra={})=>tick({api,store,now,scheduled:now,enabled:true,...extra});
  return {data,calls,go};
}
test("stopped and expired do not call GitHub",async()=>{
 const r=rig();assert.equal((await r.go({enabled:false})).status,"STOPPED");
 assert.equal((await r.go({scheduled:now-181000})).status,"EXPIRED_SLOT");assert.equal(r.calls.length,0);
});
test("exact single dispatch and durable ID",async()=>{
 const r=rig();const v=await r.go();assert.equal(v.runId,123);
 assert.equal(r.data.get("attempt").runId,123);
 assert.equal(r.calls.length,1); // POST is the first and only network request on a new slot
 assert.deepEqual(r.calls.at(-1)[1],{ref:"main",inputs:{scheduler_request_id:String(Math.floor(now/300000)*300000)}});
});

test("lost response remains durable; no second dispatch",async()=>{
 const path="actions/workflows/"+WRITER+"/dispatches";
 const r=rig({[path]:()=>{throw Error("lost response")}});
 await assert.rejects(r.go(),/lost response/);assert.equal(r.data.get("attempt").runId,null);
 assert.equal((await r.go()).status,"AMBIGUOUS_STOP");
 assert.equal(r.calls.filter(x=>x[1]).length,1);
});

test("exact published receipt with both scanners and quote times",()=>{
 const t=new Date(now-1000).toISOString(), c={symbol:"ABC/USD",quote_observed_at:t}, ranking={symbol:"ABC/USD",rank:1,score:40};
 const run={id:123,head_sha:source,head_branch:"main",path:".github/workflows/"+WRITER,status:"completed",conclusion:"success"};
 const report={run_id:"123",source_sha:source,status:"SUCCESS_PAPER_ONLY",remote_readback_verified:true,buy_approved:false,production_applied:false,ledger_generation:1,ledger_sha256:sum,as_of:t,max_client_quote_age_seconds:1,candidates:[c],rankings:{baseline:[ranking],challenger:[ranking]},independent_legacy_evidence:{independent_execution:true,execution_location:"SAME_WRITER_JOB",buy_approved:false,production_applied:false,trade_executed:false,run_id:"123",trigger_paper_run_id:"123",source_sha:source,as_of:t,candidates:[c]},dual_scanner_report:{writer_run_id:"123",legacy_run_id:"123",ledger_sha256:sum,baseline_rankings:[ranking],challenger_watch:[c],legacy_watch:[c]}};
 assert.equal(verified(report,run,now),true);
 assert.equal(verified({...report,run_id:"124"},run,now),false);
 assert.equal(verified(report,run,now+601000),false);
 assert.equal(verified({...report,candidates:[{quote_observed_at:"bad"}]},run,now),false);
 assert.equal(verified({...report,rankings:{baseline:[{symbol:"OTHER/USD"}],challenger:[ranking]}},run,now),false);
});

test("explicit rejection releases only the later slot, never retries current slot",async()=>{
 const path="actions/workflows/"+WRITER+"/dispatches";
 let n=0;
 const r=rig({[path]:()=>{if(++n===1)throw Error("GITHUB_HTTP_422");return {workflow_run_id:124}}});
 const first=await r.go();
 assert.equal(first.status,"DISPATCH_REJECTED");
 assert.equal(first.error,"GITHUB_HTTP_422");
 assert.equal(r.data.get("attempt").terminal,true);
 assert.equal((await r.go()).status,"SLOT_ALREADY_ATTEMPTED");
 assert.equal((await r.go({now:now+300000,scheduled:now+300000})).runId,124);
 assert.equal(n,2);
});
test("server error stays ambiguous and never blindly redispatches",async()=>{
 const path="actions/workflows/"+WRITER+"/dispatches";
 const r=rig({[path]:()=>{throw Error("GITHUB_HTTP_502")}});
 await assert.rejects(r.go(),/GITHUB_HTTP_502/);
 assert.equal((await r.go()).status,"AMBIGUOUS_STOP");
 assert.equal(r.calls.filter(x=>x[1]).length,1);
});

import {github,REQUEST_TIMEOUT_MS} from "./github.mjs";
test("GitHub transport allows slow responses within 25 seconds and logs safe stage",async()=>{
 const logs=[];let timeout;let elapsed=0;
 const api=github({GITHUB_TOKEN:"test-secret"},{log:x=>logs.push(JSON.parse(x)),clock:()=>elapsed,
 timeoutSignal:ms=>{timeout=ms;return {aborted:false}},fetcher:async(url,options)=>{
  elapsed=8034;assert.equal(options.method,"GET");
  return {ok:true,status:200,json:async()=>({total_count:0,workflow_runs:[]})};
 }});
 await api("actions/workflows/"+WRITER+"/runs?branch=main&status=queued&per_page=1");
 assert.equal(timeout,25000);assert.equal(REQUEST_TIMEOUT_MS,25000);
 assert.deepEqual(logs.map(x=>x.status),["GITHUB_REQUEST_STARTED","GITHUB_REQUEST_OK"]);
 assert.equal(logs[1].stage,"WRITER_ACTIVE_QUEUED");assert.equal(logs[1].elapsed_ms,8034);
 assert.equal(JSON.stringify(logs).includes("test-secret"),false);
});
test("GitHub timeout is identified, POST is never replayed, secrets omitted",async()=>{
 const logs=[];let n=0;
 const api=github({GITHUB_TOKEN:"test-secret"},{log:x=>logs.push(JSON.parse(x)),
 timeoutSignal:()=>({aborted:true}),fetcher:async()=>{n++;throw Error("test-secret")}});
 await assert.rejects(api("actions/workflows/"+WRITER+"/dispatches",{ref:"main"}),/GITHUB_REQUEST_TIMEOUT/);
 assert.equal(n,1);assert.equal(logs.at(-1).stage,"DISPATCH");
 assert.equal(JSON.stringify(logs).includes("test-secret"),false);
});
test("explicit HTTP status is preserved for core rejection handling",async()=>{
 const api=github({GITHUB_TOKEN:"test-secret"},{log:()=>{},timeoutSignal:()=>({aborted:false}),
 fetcher:async()=>({ok:false,status:422})});
 await assert.rejects(api("actions/workflows/"+WRITER+"/dispatches",{ref:"main"}),/GITHUB_HTTP_422/);
});



test("accepted Cloudflare writer prevents duplicate request while active",async()=>{
 const r=rig({"actions/runs/123":()=>({status:"in_progress"})});
 await r.go();
 assert.equal((await r.go({now:now+300000,scheduled:now+300000})).status,"WRITER_ACTIVE");
 assert.equal(r.calls.filter(x=>x[1]).length,1);
});
test("exact terminal run derives source from GitHub; receipt read failure cannot lock later slots",async()=>{
 const slot=String(Math.floor(now/300000)*300000);
 const r=rig({"actions/runs/123":()=>({id:123,head_sha:source,head_branch:"main",path:".github/workflows/"+WRITER,status:"completed",conclusion:"success",event:"workflow_dispatch",display_title:"paper-api-"+slot}),
 "contents/verified-results/results.json?ref=paper-proof-ledger":()=>{throw Error("GITHUB_REQUEST_TIMEOUT")}});
 await r.go();
 await assert.rejects(r.go({now:now+300000,scheduled:now+300000}),/GITHUB_REQUEST_TIMEOUT/);
 assert.equal(r.data.get("attempt").terminal,true);
 assert.equal(r.data.get("attempt").source,source);
 assert.equal((await r.go({now:now+600000,scheduled:now+600000})).status,"DISPATCH_ACCEPTED");
});
test("legacy unresolved durable intent is preserved, never erased during migration",async()=>{
 const r=rig();
 r.data.set("attempt",{slot:"old",source,terminal:false,runId:null});
 assert.equal((await r.go()).status,"AMBIGUOUS_STOP");
 assert.equal(r.calls.filter(x=>x[1]).length,0);
});

import {scheduled as scheduledHandler} from "./scheduled.mjs";
test("scheduled handler awaits a Cloudflare-style thenable with no native catch method",async()=>{
 let resolve,called=0,finished=false;
 const pending=new Promise(r=>{resolve=r});
 const env={ENABLED:"true",GITHUB_TOKEN:"test-secret",SCHEDULER:{
  idFromName:name=>{assert.equal(name,"single-writer-scheduler");return name},
  get:()=>({run:at=>{called++;assert.equal(at,now);return {then:(ok,no)=>pending.then(ok,no)}}})
 }};
 const task=scheduledHandler({scheduledTime:now},env).then(result=>{finished=true;return result});
 await Promise.resolve();
 assert.equal(called,1);assert.equal(finished,false);
 resolve({status:"DISPATCH_ACCEPTED",runId:123});
 assert.deepEqual(await task,{status:"DISPATCH_ACCEPTED",runId:123});
 assert.equal(finished,true);
});
test("scheduled handler observes errors from RPC thenable without making another request",async()=>{
 let called=0;
 const env={ENABLED:"true",GITHUB_TOKEN:"test-secret",SCHEDULER:{
  idFromName:name=>name,get:()=>({run:()=>{called++;return {then:(ok,no)=>no(Error("GITHUB_REQUEST_TIMEOUT"))}}})
 }};
 await assert.rejects(scheduledHandler({scheduledTime:now},env),/GITHUB_REQUEST_TIMEOUT/);
 assert.equal(called,1);
});
test("actual HTTP Request matches the documented GitHub dispatch wire contract",async()=>{
 const slot=String(Math.floor(now/300000)*300000);
 const api=github({GITHUB_TOKEN:"test-secret"},{log:()=>{},fetcher:async(url,options)=>{
  const request=new Request(url,options);
  assert.equal(request.url,"https://api.github.com/repos/michaelrobinsonproduct-del/Cryptoscanner/actions/workflows/paper-pipeline.yml/dispatches");
  assert.equal(request.method,"POST");
  assert.equal(request.headers.get("authorization"),"Bearer test-secret");
  assert.equal(request.headers.get("accept"),"application/vnd.github+json");
  assert.equal(request.headers.get("content-type"),"application/json");
  assert.equal(request.headers.get("x-github-api-version"),"2026-03-10");
  assert.equal(request.headers.get("user-agent"),"cryptoscanner-independent-scheduler");
  assert.deepEqual(await request.json(),{ref:"main",inputs:{scheduler_request_id:slot}});
  return new Response(JSON.stringify({workflow_run_id:123,run_url:"https://api.github.com/repos/example/example/actions/runs/123",html_url:"https://github.com/example/example/actions/runs/123"}),{status:200,headers:{"content-type":"application/json"}});
 }});
 const result=await api("actions/workflows/"+WRITER+"/dispatches",{ref:"main",inputs:{scheduler_request_id:slot}});
 assert.equal(result.workflow_run_id,123);
});
