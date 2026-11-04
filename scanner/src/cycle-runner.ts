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
   let baselineFailure:string|null=null;
   let result:Awaited<ReturnType<typeof executeCandidateCycle>>;
   try{result=await executeCandidateCycle(deps)}
   catch(error){
    if(!a2Snapshot)throw error;
    baselineFailure=String(error);
    result={mode:"shadow",control_untouched:true,at:deps.now().toISOString(),scan_status:"BASELINE_UNAVAILABLE",coverage:{discovery_rows:0,selected_candidates:0,watch:0,promotion_eligible:0,abstentions:0,discarded_discovery_rows:0},candidates:[]};
   }
   let output:any={...result,...(baselineFailure?{baseline_error:baselineFailure}:{} )};
   // E's authenticated qualification decision is an upstream gate, not merely
   // a parallel informational field. A shadow artifact cannot bypass KEEP_BASELINE.
   let learningAllowsShadow=false;
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
     output={...output,shadow_evaluation:attachShadowEvaluation(result,null,[]).shadow_evaluation,shadow_artifact_status:"REJECTED"};
    }else{
     try{const {evidence,outcomes,scores}=await shadow();output={...output,shadow_evaluation:attachShadowEvaluation(result,evidence,outcomes,scores).shadow_evaluation,shadow_artifact_status:evidence?"VERIFIED":"UNAVAILABLE"}}
     catch{output={...output,shadow_evaluation:attachShadowEvaluation(result,null,[]).shadow_evaluation,shadow_artifact_status:"REJECTED"}}
    }
   }
   if(recoveryStatus){try{output={...output,recovery_status:await recoveryStatus()}}catch{output={...output,recovery_status:unavailableRecovery("read_or_validation_failed")}}}
   if(sourceHealth){try{output={...output,source_run_health:await sourceHealth()}}catch{output={...output,source_run_health:unavailableSourceHealth("read_or_validation_failed")}}}
   if(paperReceipt){let receipt:PaperReceipt;try{receipt=await paperReceipt()}catch{receipt=unavailablePaperReceipt("read_or_validation_failed")};output={...output,paper_receipt:receipt}}
   if(a2Snapshot){let snapshot:A2Snapshot;try{snapshot=await a2Snapshot()}catch{snapshot=unavailableA2Snapshot("read_or_validation_failed")};if(baselineFailure&&snapshot.status!=="VERIFIED_SNAPSHOT")throw Error("both_baseline_and_a2_unavailable: "+baselineFailure);
    // Two independent read-only feeds may refer to different scanner runs.
    // Never display WATCH from A2 as reconciled with a conflicting paper receipt.
    const receipt=output.paper_receipt as PaperReceipt|undefined;
    const conflict=snapshot.status==="VERIFIED_SNAPSHOT"&&receipt?.status==="VERIFIED_RECEIPT"&&(
      receipt.as_of!==snapshot.as_of||receipt.scan_status!==snapshot.scan_status||
      receipt.watch_count!==snapshot.watch.length||
      receipt.observed_markets!==snapshot.observed_markets||
      (receipt.eligible_pairs!==null&&receipt.eligible_pairs!==snapshot.eligible_pairs)
    );
    const accepted=snapshot.status==="VERIFIED_SNAPSHOT"&&!conflict;
    output={...output,a2_snapshot:conflict?unavailableA2Snapshot("paper_receipt_a2_mismatch"):snapshot,paper_watch:accepted?snapshot.watch:[],paper_watch_status:conflict?"ABSTAIN_SOURCE_MISMATCH":accepted?"PAPER_ONLY_VERIFIED":"ABSTAIN_A2_UNAVAILABLE",live_watch_certified:false};
    if(baselineFailure&&!accepted)throw Error("both_baseline_and_a2_unavailable: "+baselineFailure);}
   last=output;lastError=null;cycles++;
   return {ok:true,status:200,origin,result:output};
  }catch(error){lastError=String(error);return {ok:false,status:502,origin,error:lastError}}
  finally{running=false}
 }
 return {run,snapshot:()=>({running,cycles,lastError,last})};
}
