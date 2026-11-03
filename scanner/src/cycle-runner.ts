import {executeCandidateCycle,type Dependencies} from "./candidate-cycle";
export function createCycleRunner(deps:Dependencies){
 let running=false,cycles=0,last:any=null,lastError:string|null=null;
 async function run(origin:"manual"|"scheduled"){
  if(running)return {ok:false,status:409,error:"cycle_already_running",origin};
  running=true;
  try{
   const result=await executeCandidateCycle(deps);
   last=result;lastError=null;cycles++;
   return {ok:true,status:200,origin,result};
  }catch(error){
   lastError=String(error);
   return {ok:false,status:502,origin,error:lastError};
  }finally{running=false}
 }
 return {run,snapshot:()=>({running,cycles,lastError,last})};
}
