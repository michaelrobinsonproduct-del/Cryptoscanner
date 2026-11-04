import {unavailableSourceHealth,type SourceRunHealth} from "./source-health";
import {unavailableRecovery,type RecoveryStatus} from "./recovery-status";
import {unavailableA2Snapshot,type A2Snapshot} from "./a2-snapshot";
import {executeCandidateCycle,type Dependencies} from "./candidate-cycle";
import {unavailablePaperReceipt,type PaperReceipt} from "./paper-receipt";
import {attachShadowEvaluation,type ShadowEvidence,type ShadowOutcome,type ShadowScore} from "./shadow-evaluation";
export function createCycleRunner(deps:Dependencies,shadow?:()=>Promise<{evidence:ShadowEvidence|null;outcomes:ShadowOutcome[];scores:ShadowScore[]}>,paperReceipt?:()=>Promise<PaperReceipt>,a2Snapshot?:()=>Promise<A2Snapshot>,learningReport?:()=>Promise<{decision:string;held_out_n:number;production_applied:false}>,recoveryStatus?:()=>Promise<RecoveryStatus>,sourceHealth?:()=>Promise<SourceRunHealth>){
 let running=false,cycles=0,last:any=null,lastError:string|null=null;
 async function run(origin:"manual"|"scheduled"){
  if(running)return {ok:false,status:409,error:"cycle_already_running",origin};
  running=true;
  try{
   const result=await executeCandidateCycle(deps);
   let output=result;
   // E's authenticated qualification decision is an upstream gate, not merely
   // a parallel informational field. A shadow artifact cannot bypass KEEP_BASELINE.
   let learningAllowsShadow=learningReport===undefined;
   if(learningReport){
    try{
     const gate=await learningReport();
     output={...output,learning_gate:{...gate,status:"VERIFIED_RESEARCH_ONLY"}};
     learningAllowsShadow=gate.decision==="SHADOW_ELIGIBLE_REVIEW"&&gate.held_out_n>0&&gate.production_applied===false;
    }catch{
     output={...output,learning_gate:{status:"REJECTED",decision:"KEEP_BASELINE",held_out_n:0,production_applied:false}};
     learningAllowsShadow=false;
    }
   }
   if(shadow){
    if(!learningAllowsShadow){
     output={...attachShadowEvaluation(result,null,[]),learning_gate:output.learning_gate,shadow_artifact_status:"REJECTED"};
    }else{
     try{const {evidence,outcomes,scores}=await shadow();output={...attachShadowEvaluation(result,evidence,outcomes,scores),learning_gate:output.learning_gate,shadow_artifact_status:evidence?"VERIFIED":"UNAVAILABLE"}}
     catch{output={...attachShadowEvaluation(result,null,[]),learning_gate:output.learning_gate,shadow_artifact_status:"REJECTED"}}
    }
   }
   if(recoveryStatus){try{output={...output,recovery_status:await recoveryStatus()}}catch{output={...output,recovery_status:unavailableRecovery("read_or_validation_failed")}}}
   if(sourceHealth){try{output={...output,source_run_health:await sourceHealth()}}catch{output={...output,source_run_health:unavailableSourceHealth("read_or_validation_failed")}}}
   if(paperReceipt){let receipt:PaperReceipt;try{receipt=await paperReceipt()}catch{receipt=unavailablePaperReceipt("read_or_validation_failed")};output={...output,paper_receipt:receipt}}
   if(a2Snapshot){let snapshot:A2Snapshot;try{snapshot=await a2Snapshot()}catch{snapshot=unavailableA2Snapshot("read_or_validation_failed")};output={...output,a2_snapshot:snapshot}}
   last=output;lastError=null;cycles++;
   return {ok:true,status:200,origin,result:output};
  }catch(error){lastError=String(error);return {ok:false,status:502,origin,error:lastError}}
  finally{running=false}
 }
 return {run,snapshot:()=>({running,cycles,lastError,last})};
}
