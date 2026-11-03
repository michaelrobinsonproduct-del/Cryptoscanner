import {executeCandidateCycle,type Dependencies} from "./candidate-cycle";
import {attachShadowEvaluation,type ShadowEvidence,type ShadowOutcome} from "./shadow-evaluation";
export function createCycleRunner(deps:Dependencies,shadow?:()=>Promise<{evidence:ShadowEvidence|null;outcomes:ShadowOutcome[]}>){
 let running=false,cycles=0,last:any=null,lastError:string|null=null;
 async function run(origin:"manual"|"scheduled"){
  if(running)return {ok:false,status:409,error:"cycle_already_running",origin};
  running=true;
  try{
   const result=await executeCandidateCycle(deps);
   let output=result;
   if(shadow){try{const {evidence,outcomes}=await shadow();output=attachShadowEvaluation(result,evidence,outcomes)}catch{output=attachShadowEvaluation(result,null,[])}}
   last=output;lastError=null;cycles++;
   return {ok:true,status:200,origin,result:output};
  }catch(error){
   lastError=String(error);
   return {ok:false,status:502,origin,error:lastError};
  }finally{running=false}
 }
 return {run,snapshot:()=>({running,cycles,lastError,last})};
}
