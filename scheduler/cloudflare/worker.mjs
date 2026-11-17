import {DurableObject} from "cloudflare:workers";
import {REPO,tick} from "./core.mjs";
function github(env) {
  if(!env.GITHUB_TOKEN) throw Error("MISSING_GITHUB_TOKEN");
  return async(path,body)=>{
    const headers={Authorization:"Bearer "+env.GITHUB_TOKEN,
      Accept:path.startsWith("contents/")?"application/vnd.github.raw+json":"application/vnd.github+json",
      "X-GitHub-Api-Version":"2026-03-10","User-Agent":"cryptoscanner-independent-scheduler"};
    if(body) headers["Content-Type"]="application/json";
    const res=await fetch("https://api.github.com/repos/"+REPO+"/"+path,
      {method:body?"POST":"GET",headers,body:body?JSON.stringify(body):undefined,
       signal:AbortSignal.timeout(8000),redirect:"error"});
    if(!res.ok) throw Error("GITHUB_HTTP_"+res.status);
    return res.json();
  };
}
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
    if(env.ENABLED!=="true") return;
    ctx.waitUntil(env.SCHEDULER.get(env.SCHEDULER.idFromName("single-writer-scheduler")).run(event.scheduledTime));
  }
};
