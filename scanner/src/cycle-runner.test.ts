import {test,expect} from "bun:test";
import {createCycleRunner} from "./cycle-runner";
const now="2026-11-03T04:00:00Z";
const row={pair:"TAOUSD",score:85,displacement_pct:1,discovered_at:"2026-11-03T03:59:00Z"};
const quote={pair:"TAOUSD",success:true,twoSidedBook:true,executableBbo:true,recentTradeConfirmation:true,newestTradeAgeSeconds:5,bestAsk:100,bestBid:99,fetchedAt:"2026-11-03T03:59:30Z"};
function deps(overrides:any={}){return {scan:async()=>({candidates:[row]}),confirm:async()=>quote,pause:async()=>{},now:()=>new Date(now),...overrides}}
test("manual and scheduled share exact candidate result schema and source evidence",async()=>{
 const r=createCycleRunner(deps());const manual=await r.run("manual"),scheduled=await r.run("scheduled");
 expect(manual.ok).toBe(true);expect(scheduled.ok).toBe(true);
 if(manual.ok&&scheduled.ok){expect(manual.result).toEqual(scheduled.result);expect(manual.result.candidates).toHaveLength(1);expect(manual.result.candidates[0].discovered_at).toBe(row.discovered_at)}
 expect(r.snapshot().cycles).toBe(2);
});
test("overlap returns 409 without a second discovery or confirmation",async()=>{
 let release!:()=>void,scans=0;
 const wait=new Promise<void>(resolve=>{release=resolve});
 const r=createCycleRunner(deps({scan:async()=>{scans++;await wait;return {candidates:[row]}}}));
 const first=r.run("scheduled");
 const blocked=await r.run("manual");
 expect(blocked).toEqual({ok:false,status:409,error:"cycle_already_running",origin:"manual"});
 expect(scans).toBe(1);release();expect((await first).ok).toBe(true);
 expect(r.snapshot().cycles).toBe(1);
});
test("failed scan is visible, does not increment success, and next cycle recovers",async()=>{
 let attempts=0;
 const r=createCycleRunner(deps({scan:async()=>{if(++attempts===1)throw Error("collector unavailable");return {candidates:[row]}}}));
 const failure=await r.run("scheduled");
 expect(failure.status).toBe(502);expect(r.snapshot().lastError).toContain("collector unavailable");
 expect(r.snapshot().cycles).toBe(0);
 const success=await r.run("manual");
 expect(success.ok).toBe(true);expect(r.snapshot().lastError).toBeNull();expect(r.snapshot().cycles).toBe(1);
});
test("stale discovery abstains identically for manual and scheduled",async()=>{
 const r=createCycleRunner(deps({scan:async()=>({candidates:[{...row,discovered_at:"2026-11-03T03:00:00Z"}]})}));
 const a=await r.run("manual"),b=await r.run("scheduled");
 expect(a.result).toEqual(b.result);expect(a.result.candidates[0].decision).toBe("ABSTAIN");
});
