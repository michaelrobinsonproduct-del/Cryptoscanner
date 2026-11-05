import {test,expect} from "bun:test";
import {createRecoveryStatusReader} from "./recovery-status";
import {createCycleRunner} from "./cycle-runner";
import {createCycleHttpHandler} from "./cycle-http";
const deps={scan:async()=>({candidates:[]}),confirm:async()=>{throw Error("unexpected")},pause:async()=>{},now:()=>new Date("2026-11-03T23:00:00Z")};
async function reader(receipt:unknown){
 const bytes=new TextEncoder().encode(JSON.stringify(receipt));
 const sha=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes))).map(x=>x.toString(16).padStart(2,"0")).join("");
 return createRecoveryStatusReader("/tmp/d-status.json",sha,async()=>bytes);
}
const valid={schema:"paper_recovery_consumer_v1",status:"VERIFIED_READBACK",download_outcome:"success",consume_outcome:"success",workflow_run_id:"41736851502",workflow_sha:"cde2ce23e7bd34be4c4abcd851069e2bac3a75c6",production_applied:false};
test("D recovery consumer readback appears identically in manual and scheduled output",async()=>{
 const runner=createCycleRunner(deps,undefined,undefined,undefined,undefined,await reader(valid));
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.recovery_status).toMatchObject({status:"VERIFIED_READBACK",production_applied:false,workflow_run_id:valid.workflow_run_id});
});
test("failed D readback remains visible and forged success fails closed",async()=>{
 const failed={...valid,status:"RECOVERY_CONSUMER_FAILED",consume_outcome:"failure"};
 const runner=createCycleRunner(deps,undefined,undefined,undefined,undefined,await reader(failed));
 expect((await runner.run("manual")).result.recovery_status.status).toBe("RECOVERY_CONSUMER_FAILED");
 const forged=createCycleRunner(deps,undefined,undefined,undefined,undefined,await reader({...failed,status:"VERIFIED_READBACK"}));
 const result=await forged.run("scheduled");
 expect(result.result.recovery_status.status).toBe("UNAVAILABLE");
 expect(result.result.candidates).toEqual([]);
});
test("real D status artifact can be consumed read-only when supplied",async()=>{
 const path=process.env.B_REAL_D_STATUS_FILE,sha=process.env.B_REAL_D_STATUS_SHA256;
 if(!path||!sha)return;
 const runner=createCycleRunner(deps,undefined,undefined,undefined,undefined,createRecoveryStatusReader(path,sha));
 const result=await runner.run("manual");
 expect(result.result.recovery_status.status).toBe("VERIFIED_READBACK");
 console.log("B_REAL_D_RECOVERY_CONSUMED",JSON.stringify(result.result.recovery_status));
});
