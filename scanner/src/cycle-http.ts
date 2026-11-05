import type {createCycleRunner} from "./cycle-runner";
export function createCycleHttpHandler(runner:ReturnType<typeof createCycleRunner>){
 return async (req:Request):Promise<Response>=>{
  const path=new URL(req.url).pathname;
  if(path==="/health"){const s=runner.snapshot();return Response.json({mode:"shadow",running:s.running,cycles:s.cycles,lastError:s.lastError})}
  if(path==="/dashboard"){const s=runner.snapshot();return Response.json({mode:"shadow",running:s.running,cycles:s.cycles,last_error:s.lastError,last_result:s.last})}
  if(path==="/cycle"){const result=await runner.run("manual");return Response.json(result.ok?result.result:{error:result.error},{status:result.status})}
  return Response.json({endpoints:["/health","/dashboard","/cycle"]});
 };
}
