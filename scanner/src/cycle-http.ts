import type {createCycleRunner} from "./cycle-runner";
export function createCycleHttpHandler(runner:ReturnType<typeof createCycleRunner>){
 return async (req:Request):Promise<Response>=>{
  const path=new URL(req.url).pathname;
  if(path==="/health"){const s=runner.snapshot();return Response.json({mode:"shadow",running:s.running,cycles:s.cycles,failures:s.failures,lastError:s.lastError,lastOrigin:s.lastOrigin,lastCompletedAt:s.lastCompletedAt})}
  if(path==="/dashboard"){const s=runner.snapshot();return Response.json({mode:"shadow",running:s.running,cycles:s.cycles,failures:s.failures,last_error:s.lastError,last_origin:s.lastOrigin,last_completed_at:s.lastCompletedAt,last_result:s.last})}
  if(path==="/watch"){const s=runner.snapshot();return Response.json(s.lastError?{status:"ABSTAIN_CYCLE_FAILED",error:s.lastError,origin:s.lastOrigin,completed_at:s.lastCompletedAt}:s.last??{status:"ABSTAIN_NO_COMPLETED_CYCLE"},{status:s.lastError?503:200})}
  if(path==="/cycle"){const result=await runner.run("manual");return Response.json(result.ok?result.result:{error:result.error},{status:result.status})}
  return Response.json({endpoints:["/health","/dashboard","/watch","/cycle"]});
 };
}
