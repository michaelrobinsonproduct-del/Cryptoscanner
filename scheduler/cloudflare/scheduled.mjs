// Cloudflare RPC returns a custom thenable, not a native Promise.
// The scheduled invocation must await the actual result instead of calling
// a method on the RPC pipeline or ending before its outcome is known.
export async function scheduled(event,env) {
  if(env.ENABLED!=="true") { console.log(JSON.stringify({status:"STOPPED",scheduled:event.scheduledTime})); return; }
  if(!env.GITHUB_TOKEN) { console.error(JSON.stringify({status:"MISSING_GITHUB_TOKEN",scheduled:event.scheduledTime})); throw Error("MISSING_GITHUB_TOKEN"); }
  console.log(JSON.stringify({status:"TICK_STARTED",scheduled:event.scheduledTime}));
  try {
    const stub=env.SCHEDULER.get(env.SCHEDULER.idFromName("single-writer-scheduler"));
    const result=await stub.run(event.scheduledTime);
    console.log(JSON.stringify({status:"TICK_FINISHED",result:result?.status,slot:result?.slot,runId:result?.runId,scheduled:event.scheduledTime}));
    return result;
  } catch(error) {
    // Never log arbitrary exception messages, credentials or response bodies.
    const code=/^(GITHUB_HTTP_\d{3}|GITHUB_REQUEST_TIMEOUT|GITHUB_RESPONSE_INVALID|GITHUB_TRANSPORT_ERROR|MISSING_GITHUB_TOKEN|INCOMPLETE_ACTIVE_HISTORY|NO_MAIN_SHA|AMBIGUOUS_DISPATCH)$/.test(error?.message)?error.message:"SCHEDULER_RUNTIME_ERROR";
    console.error(JSON.stringify({status:code,scheduled:event.scheduledTime}));
    throw Error(code);
  }
}
