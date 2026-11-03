import {test,expect} from "bun:test";
import {createHash} from "node:crypto";
import {parseA2Snapshot,createA2SnapshotReader,createA2VerifiedFileReader} from "./a2-snapshot";
import {createCycleRunner} from "./cycle-runner";
import {createCycleHttpHandler} from "./cycle-http";
const now=new Date("2026-11-03T20:00:00Z"),at="2026-11-03T19:59:00Z",quote="2026-11-03T19:58:00Z",pair="TAOUSD";
const prediction_id=createHash("sha256").update("paper-v1|"+at+"|"+pair).digest("hex");
const row={rank:1,status:"PAPER_WATCH",buy_approved:false,pair,as_of:at,quote_observed_at:quote,quote_timestamp_semantics:"client_observed_not_exchange_event_time",prediction_id,price:100,move15_pct:2,volume_accel:3,baseline_score:75,challenger_score:80,spread_bps:10};
const fixture={as_of:at,scan_status:"WATCH",receipt_sha256:"a".repeat(64),eligible_pairs:3,observed_markets:2,abstention_counts:{stale:1},watch:[row]};
const deps={scan:async()=>({candidates:[]}),confirm:async()=>{throw Error("not called")},pause:async()=>{},now:()=>now};
test("B1 HTTP and scheduled consume same A2 read-only snapshot, persist dashboard and preserve independent baseline",async()=>{
 let reads=0;const reader=createA2SnapshotReader("https://example.org/verified-a2",()=>now,(async(_url,options)=>{reads++;expect(options?.method).toBe("GET");return new Response(JSON.stringify(fixture))}) as any);
 const runner=createCycleRunner(deps,undefined,undefined,reader),http=createCycleHttpHandler(runner);
 const manual=await (await http(new Request("http://localhost/cycle"))).json(),scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);expect(reads).toBe(2);expect(manual.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
 expect(manual.a2_snapshot).toMatchObject({status:"VERIFIED_SNAPSHOT",receipt_sha256:fixture.receipt_sha256,watch:[{pair,rank:1,price:100}],buy_approved:false});
 expect((await (await http(new Request("http://localhost/dashboard"))).json()).last_result.a2_snapshot).toEqual(manual.a2_snapshot);
});
test("stale read-time quotes and malformed coverage fail closed, never invent WATCH",async()=>{
 expect(()=>parseA2Snapshot({...fixture,watch:[{...row,quote_observed_at:"2026-11-03T19:45:00Z"}]},now)).toThrow("stale_a2_quote");
 expect(()=>parseA2Snapshot({...fixture,observed_markets:0},now)).toThrow("invalid_a2_snapshot_coverage");
 expect(()=>parseA2Snapshot({...fixture,watch:[{...row,prediction_id:"b".repeat(64)}]},now)).toThrow("invalid_a2_market_metric");
 const runner=createCycleRunner(deps,undefined,undefined,createA2SnapshotReader("https://example.org/a2",()=>now,async()=>new Response(JSON.stringify({...fixture,watch:[{...row,price:-1}]})) as any));
 const result=await runner.run("manual");expect(result.ok).toBe(true);expect(result.result.a2_snapshot).toMatchObject({status:"UNAVAILABLE",watch:[],reason:"read_or_validation_failed"});expect(result.result.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
});
test("missing A2 endpoint and unsafe URL abstain",async()=>{expect(await createA2SnapshotReader(undefined,()=>now)()).toMatchObject({status:"UNAVAILABLE",reason:"not_configured"});await expect(createA2SnapshotReader("http://example.org",()=>now)()).rejects.toThrow("unsafe_a2_url")});

test("A2 reader bounds streamed bytes and rejects oversized declared content",async()=>{
 const oversized=()=>new Response("x".repeat(200001));
 await expect(createA2SnapshotReader("https://example.org/a2",()=>now,async()=>oversized())()).rejects.toThrow("a2_oversized");
 await expect(createA2SnapshotReader("https://example.org/a2",()=>now,async()=>new Response("{}",{headers:{"content-length":"200001"}}))()).rejects.toThrow("a2_oversized");
});
test("A2 rejects stablecoin candidates and impossible spread without altering baseline",async()=>{
 const coin="USDTUSD",id=createHash("sha256").update("paper-v1|"+at+"|"+coin).digest("hex");
 expect(()=>parseA2Snapshot({...fixture,watch:[{...row,pair:coin,prediction_id:id}]},now)).toThrow("invalid_a2_candidate");
 expect(()=>parseA2Snapshot({...fixture,watch:[{...row,spread_bps:10001}]},now)).toThrow("invalid_a2_market_metric");
 const runner=createCycleRunner(deps,undefined,undefined,createA2SnapshotReader("https://example.org/a2",()=>now,async()=>new Response(JSON.stringify({...fixture,watch:[{...row,pair:coin,prediction_id:id}]}))));
 const manual=await runner.run("manual"),scheduled=await runner.run("scheduled");
 expect(manual.result.a2_snapshot).toMatchObject({status:"UNAVAILABLE",watch:[]});
 expect(scheduled.result).toEqual(manual.result);
 expect(manual.result.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
});

import {mkdtemp,writeFile,rm} from "node:fs/promises";
import {tmpdir} from "node:os";
import {join} from "node:path";
test("B1 verified A2 file is shared by manual HTTP and scheduled, and expires fail closed",async()=>{
 const dir=await mkdtemp(join(tmpdir(),"a2-verified-"));
 try{
  const path=join(dir,"verified-snapshot.json");await writeFile(path,JSON.stringify(fixture));
  const runner=createCycleRunner(deps,undefined,undefined,createA2VerifiedFileReader(path,()=>now));
  const http=createCycleHttpHandler(runner);
  const manual=await (await http(new Request("http://localhost/cycle"))).json();
  const scheduled=await runner.run("scheduled");
  expect(manual).toEqual(scheduled.result);
  expect(manual.a2_snapshot).toMatchObject({status:"VERIFIED_SNAPSHOT",receipt_sha256:fixture.receipt_sha256,watch:[{pair:"TAOUSD"}]});
  expect((await (await http(new Request("http://localhost/dashboard"))).json()).last_result.a2_snapshot).toEqual(manual.a2_snapshot);
  const expired=createCycleRunner(deps,undefined,undefined,createA2VerifiedFileReader(path,()=>new Date("2026-11-03T20:20:00Z")));
  const failure=await expired.run("manual");
  expect(failure.result.a2_snapshot).toMatchObject({status:"UNAVAILABLE",reason:"read_or_validation_failed",watch:[]});
  expect(failure.result.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
 }finally{await rm(dir,{recursive:true,force:true})}
});

test("B1 actual authenticated A2 export feeds both entry points (CI real Kraken)",async()=>{
 const path=process.env.B1_REAL_A2_VERIFIED_FILE;
 if(!path)return;
 const raw=JSON.parse(await (await import("node:fs/promises")).readFile(path,"utf8"));
 const captured=new Date(Date.parse(raw.as_of)+2000);
 const actualDeps={...deps,now:()=>captured};
 const runner=createCycleRunner(actualDeps,undefined,undefined,createA2VerifiedFileReader(path,()=>captured));
 const http=createCycleHttpHandler(runner);
 const manual=await (await http(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.a2_snapshot).toMatchObject({status:"VERIFIED_SNAPSHOT",receipt_sha256:raw.receipt_sha256,eligible_pairs:raw.eligible_pairs,observed_markets:raw.observed_markets});
 expect(manual.a2_snapshot.watch.length).toBe(raw.watch.length);
 expect(manual.a2_snapshot.watch.map((c:any)=>c.prediction_id)).toEqual(raw.watch.map((c:any)=>c.prediction_id));
 expect(manual.a2_snapshot.buy_approved).toBe(false);
 expect((await (await http(new Request("http://localhost/dashboard"))).json()).last_result.a2_snapshot).toEqual(manual.a2_snapshot);
 console.log("B1_REAL_A2_MANUAL_SCHEDULED_PARITY",JSON.stringify({receipt_sha256:raw.receipt_sha256,eligible_pairs:raw.eligible_pairs,observed_markets:raw.observed_markets,watch_count:raw.watch.length,abstention_counts:raw.abstention_counts,source_time:raw.as_of,replay_clock:captured.toISOString()}));
});
