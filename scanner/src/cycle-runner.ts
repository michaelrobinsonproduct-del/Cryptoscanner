import {executeCandidateCycle,type Dependencies} from "./candidate-cycle";
import {unavailablePaperReceipt,type PaperReceipt} from "./paper-receipt";
import {attachShadowEvaluation,type ShadowEvidence,type ShadowOutcome,type ShadowScore} from "./shadow-evaluation";
export function createCycleRunner(deps:Dependencies,shadow?:()=>Promise<{evidence:ShadowEvidence|null;outcomes:ShadowOutcome[];scores:ShadowScore[]}>,paperReceipt?:()=>Promise<PaperReceipt>){
 let running=false,cycles=0,last:any=null,lastError:string|null=null,lastOrigin:"manual"|"scheduled"|null=null,lastCompletedAt:string|null=null,failures=0;
 async function run(origin:"manual"|"scheduled"){
  if(running)return {ok:false,status:409,error:"cycle_already_running",origin};
  running=true;
  try{
   const result=await executeCandidateCycle(deps);
   let output=result;
   if(shadow){try{const {evidence,outcomes,scores}=await shadow();output={...attachShadowEvaluation(result,evidence,outcomes,scores),shadow_artifact_status:evidence?"VERIFIED":"UNAVAILABLE"}}catch{output={...attachShadowEvaluation(result,null,[]),shadow_artifact_status:"REJECTED"}}}
   if(paperReceipt){let receipt:PaperReceipt;try{receipt=await paperReceipt()}catch(error){receipt=unavailablePaperReceipt("read_or_validation_failed")};output={...output,paper_receipt:receipt}}
   last=output;lastError=null;lastOrigin=origin;lastCompletedAt=new Date().toISOString();cycles++;
   return {ok:true,status:200,origin,result:output};
  }catch(error){
   lastError=String(error);last=null;lastOrigin=origin;lastCompletedAt=new Date().toISOString();failures++;
   return {ok:false,status:502,origin,error:lastError};
  }finally{running=false}
 }
 return {run,snapshot:()=>({running,cycles,failures,lastError,last,lastOrigin,lastCompletedAt})};
}
