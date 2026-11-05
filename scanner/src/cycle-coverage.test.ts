import {test,expect} from "bun:test";
import {createCycleRunner} from "./cycle-runner";
import {createCycleHttpHandler} from "./cycle-http";
const at="2026-11-03T04:00:00Z";
const row={pair:"TAOUSD",score:85,displacement_pct:1,discovered_at:"2026-11-03T03:59:00Z"};
const deps=(scan:any,confirm:any=async()=>{throw Error("quote upstream down")})=>({scan:async()=>scan,confirm,pause:async()=>{},now:()=>new Date(at)});
const request=()=>new Request("http://localhost/cycle");
test("manual HTTP and scheduled zero-WATCH parity retains confirmation abstention and coverage",async()=>{
 const runner=createCycleRunner(deps({candidates:[row]})),http=createCycleHttpHandler(runner);
 const manual=await http(request());expect(manual.status).toBe(200);
 const m=await manual.json(),s=await runner.run("scheduled");
 expect(s.result).toEqual(m);
 expect(m.scan_status).toBe("ABSTAIN_NO_QUALIFIED_CONFIRMATION");
 expect(m.coverage).toEqual({discovery_rows:1,selected_candidates:1,watch:0,promotion_eligible:0,abstentions:1,discarded_discovery_rows:0});
 expect(m.candidates[0]).toMatchObject({pair:"TAOUSD",decision:"ABSTAIN",reason:"confirmation_error"});
 const dashboard=await (await http(new Request("http://localhost/dashboard"))).json();
 expect(dashboard.last_result.scan_status).toBe(m.scan_status);
});
test("malformed discovery fails HTTP 502 rather than reporting successful empty scan",async()=>{
 const runner=createCycleRunner(deps({unexpected:true})),http=createCycleHttpHandler(runner);
 const r=await http(request());expect(r.status).toBe(502);
 expect((await r.json()).error).toContain("missing_discovery_candidates");
 expect((await http(new Request("http://localhost/health"))).status).toBe(200);
 expect(runner.snapshot().cycles).toBe(0);
});
test("genuinely empty and filtered discoveries have distinct truthful zero-coverage statuses",async()=>{
 const empty=await createCycleRunner(deps({candidates:[]})).run("scheduled");
 expect(empty.result.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
 expect(empty.result.coverage.discovery_rows).toBe(0);
 const filtered=await createCycleRunner(deps({candidates:[{...row,score:20}]})).run("scheduled");
 expect(filtered.result.scan_status).toBe("NO_QUALIFIED_DISCOVERY");
 expect(filtered.result.coverage.discarded_discovery_rows).toBe(1);
});
