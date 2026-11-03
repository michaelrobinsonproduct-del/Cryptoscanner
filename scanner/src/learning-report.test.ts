import {test,expect} from "bun:test";
import {createHash} from "node:crypto";
import {createLearningReportReader} from "./learning-report";
import {createCycleRunner} from "./cycle-runner";
import {createCycleHttpHandler} from "./cycle-http";
const fixture={mode:"REAL_PAPER_DESCRIPTIVE_NOT_AUTHENTICATED_DEPTH",ledger_sha256:"a".repeat(64),paper_predictions:357,paper_observations:22272,production_applied:false,shadow_decision:{decision:"KEEP_BASELINE",production_applied:false},horizons:Object.fromEntries([1,6,24,48].map(h=>[String(h),{paper_outcomes:0,held_out_n:0,authenticated_entry_labels:0,rule:"NO QUALIFIED RULE"}]))};
const deps={scan:async()=>({candidates:[]}),confirm:async()=>{throw Error("unexpected")},pause:async()=>{},now:()=>new Date("2026-11-03T23:00:00Z")};
async function reader(report:any){const bytes=Buffer.from(JSON.stringify(report));const sha=createHash("sha256").update(bytes).digest("hex");return createLearningReportReader("/tmp/e-report.json",sha,async()=>bytes)}
test("actual E descriptive horizon schema gives identical KEEP_BASELINE for manual HTTP and scheduled",async()=>{
 const runner=createCycleRunner(deps,undefined,undefined,undefined,await reader(fixture)),http=createCycleHttpHandler(runner);
 const manual=await (await http(new Request("http://localhost/cycle"))).json(),scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.learning_gate).toEqual({decision:"KEEP_BASELINE",held_out_n:0,production_applied:false,status:"VERIFIED_RESEARCH_ONLY"});
 expect(manual.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
});
test("fabricated authenticated label or held-out sample is rejected without changing baseline",async()=>{
 for(const field of ["held_out_n","authenticated_entry_labels"]){
  const modified=structuredClone(fixture);(modified.horizons as any)["6"][field]=1;
  const runner=createCycleRunner(deps,undefined,undefined,undefined,await reader(modified));
  const manual=await runner.run("manual"),scheduled=await runner.run("scheduled");
  expect(manual.result).toEqual(scheduled.result);
  expect(manual.result.learning_gate).toMatchObject({status:"REJECTED",decision:"KEEP_BASELINE",production_applied:false});
  expect(manual.result.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
 }
});
test("real authenticated E GitHub artifact is consumed through both paths when supplied",async()=>{
 const path=process.env.B2_REAL_E_REPORT_FILE,sha=process.env.B2_REAL_E_REPORT_SHA256;
 if(!path||!sha)return;
 const runner=createCycleRunner(deps,undefined,undefined,undefined,createLearningReportReader(path,sha));
 const http=createCycleHttpHandler(runner);
 const manual=await (await http(new Request("http://localhost/cycle"))).json(),scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.learning_gate).toMatchObject({status:"VERIFIED_RESEARCH_ONLY",decision:"KEEP_BASELINE",held_out_n:0,production_applied:false});
 console.log("B2_REAL_E_KEEP_BASELINE_MANUAL_SCHEDULED",JSON.stringify(manual.learning_gate));
});
