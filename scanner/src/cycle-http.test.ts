import {test,expect} from "bun:test";
import {createCycleRunner} from "./cycle-runner";
import {createCycleHttpHandler} from "./cycle-http";
const at="2026-11-03T04:00:00Z";
const row={pair:"TAOUSD",score:85,displacement_pct:1,discovered_at:"2026-11-03T03:59:00Z"};
const quote={pair:"TAOUSD",success:true,twoSidedBook:true,executableBbo:true,recentTradeConfirmation:true,newestTradeAgeSeconds:5,bestAsk:100,bestBid:99,fetchedAt:"2026-11-03T03:59:30Z"};
const deps=(overrides:any={})=>({scan:async()=>({candidates:[row]}),confirm:async()=>quote,pause:async()=>{},now:()=>new Date(at),...overrides});
const req=(path:string)=>new Request("http://localhost"+path);
test("real HTTP /cycle and native scheduled entry emit identical candidate payload",async()=>{
 const runner=createCycleRunner(deps()),http=createCycleHttpHandler(runner);
 const response=await http(req("/cycle"));expect(response.status).toBe(200);
 const manual=await response.json(),scheduled=await runner.run("scheduled");
 expect(scheduled.ok).toBe(true);expect(manual).toEqual(scheduled.result);
 expect(manual.candidates).toHaveLength(1);expect(manual.candidates[0].discovered_at).toBe(row.discovered_at);
 const dashboard=await (await http(req("/dashboard"))).json();
 expect(dashboard.cycles).toBe(2);expect(dashboard.last_result).toEqual(manual);
});
test("HTTP concurrent /cycle returns 409 while scheduled scan owns lease",async()=>{
 let release!:()=>void;let scans=0;const wait=new Promise<void>(r=>{release=r});
 const runner=createCycleRunner(deps({scan:async()=>{scans++;await wait;return {candidates:[row]}}}));
 const scheduled=runner.run("scheduled"),http=createCycleHttpHandler(runner);
 const response=await http(req("/cycle"));
 expect(response.status).toBe(409);expect((await response.json()).error).toBe("cycle_already_running");
 expect(scans).toBe(1);release();expect((await scheduled).ok).toBe(true);
});
test("HTTP failure visible on health and dashboard, subsequent manual recovery clears it",async()=>{
 let n=0;const runner=createCycleRunner(deps({scan:async()=>{if(++n===1)throw Error("upstream down");return {candidates:[row]}}}));
 const http=createCycleHttpHandler(runner);
 const first=await http(req("/cycle"));expect(first.status).toBe(502);
 expect((await (await http(req("/health"))).json()).lastError).toContain("upstream down");
 expect((await (await http(req("/dashboard"))).json()).cycles).toBe(0);
 const recovered=await http(req("/cycle"));expect(recovered.status).toBe(200);
 const state=await (await http(req("/dashboard"))).json();
 expect(state.cycles).toBe(1);expect(state.last_error).toBeNull();
});

test("dashboard expires cached authenticated A2 paper WATCH without mutating stored scan",async()=>{
 const snapshot={status:"VERIFIED_SNAPSHOT" as const,as_of:"2026-11-03T04:00:00Z",scan_status:"WATCH",receipt_sha256:"a".repeat(64),watch:[{pair:"TAOUSD",quote_observed_at:"2026-11-03T03:59:00Z"}],eligible_pairs:1,observed_markets:1,abstention_counts:{},source:"a2_verified_readonly" as const,buy_approved:false as const};
 let clock=new Date("2026-11-03T04:01:00Z");
 const runner=createCycleRunner(deps(),undefined,undefined,async()=>snapshot as any);
 const http=createCycleHttpHandler(runner,()=>clock);
 await runner.run("scheduled");
 const fresh=await (await http(req("/dashboard"))).json();
 expect(fresh.last_result.a2_snapshot.status).toBe("VERIFIED_SNAPSHOT");
 expect(fresh.last_result.paper_watch).toHaveLength(1);
 const watchFresh=await http(req("/watch"));expect(watchFresh.headers.get("cache-control")).toBe("no-store");expect(await watchFresh.json()).toMatchObject({mode:"paper_only",status:"PAPER_ONLY_VERIFIED",live_watch_certified:false,scan_status:"WATCH",eligible_pairs:1,observed_markets:1,abstention_counts:{},watch:[{pair:"TAOUSD"}]});expect(fresh.last_result.paper_watch_status).toBe("PAPER_ONLY_VERIFIED");expect(fresh.last_result.live_watch_certified).toBe(false);
 clock=new Date("2026-11-03T04:10:01Z");
 const expired=await (await http(req("/dashboard"))).json();
 expect(expired.last_result.a2_snapshot).toMatchObject({status:"UNAVAILABLE",reason:"expired_at_dashboard_read",watch:[]});
 expect(expired.last_result.candidates).toHaveLength(1);
 expect(expired.last_result.paper_watch).toEqual([]);
 expect(await (await http(req("/watch"))).json()).toMatchObject({mode:"paper_only",status:"ABSTAIN_A2_EXPIRED",live_watch_certified:false,scan_status:null,eligible_pairs:null,observed_markets:null,abstention_counts:null,watch:[]});expect(expired.last_result.paper_watch_status).toBe("ABSTAIN_A2_EXPIRED");expect(expired.last_result.live_watch_certified).toBe(false);
 expect(runner.snapshot().last.a2_snapshot.status).toBe("VERIFIED_SNAPSHOT");
});
