import {test,expect} from "bun:test";
import {createHash} from "node:crypto";
import {parseA2Snapshot,createA2SnapshotReader} from "./a2-snapshot";
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
