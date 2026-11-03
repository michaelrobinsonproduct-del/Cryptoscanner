import {test,expect} from "bun:test";
import {createHash} from "node:crypto";
import {createSourceHealthReader} from "./source-health";
import {createCycleRunner} from "./cycle-runner";
const run={run_id:12,event:"schedule",created_at:"2026-11-03T23:00:00Z",status:"completed",conclusion:"failure",source_sha:"a".repeat(40),url:"https://github.com/example/repo/actions/runs/12"};
const report={schema:"paper_source_run_health_v1",window_hours:24,observed_at:"2026-11-03T23:10:00Z",runs:[run],failed_count:1,pending_count:0,observed_run_count:1,production_applied:false,query_verified:true,status:"FAILURES_OBSERVED"};
function reader(x:any){const bytes=Buffer.from(JSON.stringify(x));const sha=createHash("sha256").update(bytes).digest("hex");return createSourceHealthReader("/tmp/health.json",sha,async()=>bytes)}
test("authenticated source-run failure is visible without implying production changes",async()=>{
 const x=await reader(report)();expect(x.status).toBe("FAILURES_OBSERVED");expect(x.failed_count).toBe(1);expect(x.production_applied).toBe(false);
});
test("forged no-failures report fails closed",async()=>{await expect(reader({...report,status:"NO_FAILURES_OBSERVED"})()).rejects.toThrow("source_health_state_mismatch")});
test("unverified source query fails closed on contradictory status",async()=>{await expect(reader({...report,query_verified:false})()).rejects.toThrow("source_health_query_status_mismatch")});
test("manual and scheduled share authenticated source health reporting",async()=>{
 const deps:any={scan:async()=>({markets:[]}),confirm:async()=>({}),pause:async()=>{},now:()=>new Date("2026-11-03T23:10:00Z")};
 const runner=createCycleRunner(deps,undefined,undefined,undefined,undefined,undefined,reader(report));
 const manual=await runner.run("manual"),scheduled=await runner.run("scheduled");
 expect(manual.ok).toBe(true);expect(scheduled.ok).toBe(true);
 expect(manual.result.source_run_health).toEqual(scheduled.result.source_run_health);
 expect(manual.result.source_run_health.status).toBe("FAILURES_OBSERVED");
});
