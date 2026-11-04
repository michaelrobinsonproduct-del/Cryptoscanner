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
