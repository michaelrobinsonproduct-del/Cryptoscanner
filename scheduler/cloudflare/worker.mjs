import {DurableObject} from "cloudflare:workers";
import {tick} from "./core.mjs";
import {github} from "./github.mjs";
export class Scheduler extends DurableObject {
  busy=false;
  async run(scheduled) {
    if(this.busy) return {status:"BUSY"};
    this.busy=true;
    try {
      const result=await tick({api:github(this.env),store:this.ctx.storage,
        now:Date.now(),scheduled,enabled:this.env.ENABLED==="true"});
      console.log(JSON.stringify(result));
      return result;
    } finally {this.busy=false;}
  }
}
export default {
  async scheduled(event,env,ctx) {
    if(env.ENABLED!=="true") { console.log(JSON.stringify({status:"STOPPED",scheduled:event.scheduledTime})); return; }
    if(!env.GITHUB_TOKEN) { console.error(JSON.stringify({status:"MISSING_GITHUB_TOKEN",scheduled:event.scheduledTime})); throw Error("MISSING_GITHUB_TOKEN"); }
    console.log(JSON.stringify({status:"TICK_STARTED",scheduled:event.scheduledTime}));
    ctx.waitUntil(env.SCHEDULER.get(env.SCHEDULER.idFromName("single-writer-scheduler")).run(event.scheduledTime).catch(error=>{
      // Only log known status codes; never log credentials or response bodies.
      const code=/^(GITHUB_HTTP_\d{3}|GITHUB_REQUEST_TIMEOUT|GITHUB_RESPONSE_INVALID|GITHUB_TRANSPORT_ERROR|MISSING_GITHUB_TOKEN|INCOMPLETE_ACTIVE_HISTORY|NO_MAIN_SHA|AMBIGUOUS_DISPATCH)$/.test(error?.message)?error.message:"SCHEDULER_RUNTIME_ERROR";
      console.error(JSON.stringify({status:code,scheduled:event.scheduledTime}));
      throw Error(code);
    }));
  }
};
