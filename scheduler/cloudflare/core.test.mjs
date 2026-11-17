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
 assert.equal(r.calls.filter(x=>x[1]).length,1);
 assert.deepEqual(r.calls.at(-1)[1],{ref:"main",inputs:{scheduler_request_id:String(Math.floor(now/300000)*300000)}});
});
test("existing active writer blocks dispatch",async()=>{
 const r=rig({["actions/workflows/"+WRITER+"/runs?branch=main&status=queued&per_page=1"]:()=>({total_count:1,workflow_runs:[{}]})});
 assert.equal((await r.go()).status,"EXISTING_WRITER_OR_RELAY");assert.equal(r.calls.filter(x=>x[1]).length,0);
});
test("lost response remains durable; no second dispatch",async()=>{
 const path="actions/workflows/"+WRITER+"/dispatches";
 const r=rig({[path]:()=>{throw Error("lost response")}});
 await assert.rejects(r.go(),/lost response/);assert.equal(r.data.get("attempt").runId,null);
 assert.equal((await r.go()).status,"AMBIGUOUS_STOP");
 assert.equal(r.calls.filter(x=>x[1]).length,1);
});
test("incomplete history fails before dispatch",async()=>{
 const r=rig({["actions/workflows/"+WRITER+"/runs?branch=main&status=queued&per_page=1"]:()=>({total_count:2,workflow_runs:[]})});
 await assert.rejects(r.go(),/INCOMPLETE/);assert.equal(r.calls.filter(x=>x[1]).length,0);
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

test("active guard uses one-row existence checks and parallel batches",async()=>{
 const r=rig();
 await r.go();
 const reads=r.calls.filter(([path])=>path.includes("&status="));
 assert.equal(reads.length,10);
 assert.ok(reads.every(([path])=>path.endsWith("&per_page=1")));
 const path="actions/workflows/"+WRITER+"/runs?branch=main&status=queued&per_page=1";
 const active=rig({[path]:()=>({total_count:42,workflow_runs:[{id:1}]})});
 assert.equal((await active.go()).status,"EXISTING_WRITER_OR_RELAY");
 assert.equal(active.calls.filter(x=>x[1]).length,0);
 const started=[];
 let release;
 const gate=new Promise(resolve=>{release=resolve});
 const api=async(path,body)=>{
   if(path.includes(WRITER+"/runs?")&&path.includes("&status=")) {
     started.push(path);
     if(started.length===5)release();
     await gate;
     return {total_count:0,workflow_runs:[]};
   }
   if(path.includes("/runs?"))return {total_count:0,workflow_runs:[]};
   if(path.startsWith("contents/"))return {as_of:new Date(now-601000).toISOString()};
   if(path==="git/ref/heads/main")return {object:{sha:source}};
   if(body)return {workflow_run_id:123};
   throw Error(path);
 };
 const data=new Map();
 const result=await tick({api,store:{get:async k=>data.get(k),put:async(k,v)=>data.set(k,v)},now,scheduled:now,enabled:true});
 assert.equal(started.length,5);
 assert.equal(result.runId,123);
});
