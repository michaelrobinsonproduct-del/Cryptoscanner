import {DurableObject} from "cloudflare:workers";
import {tick} from "./core.mjs";
import {github} from "./github.mjs";
import {scheduled} from "./scheduled.mjs";
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
export default {scheduled};
