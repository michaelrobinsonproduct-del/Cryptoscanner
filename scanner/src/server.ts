import {createCycleHttpHandler} from "./cycle-http";
import {createReadOnlyShadowLoader} from "./shadow-artifacts";
import {createCycleRunner} from "./cycle-runner";
const port=Number(process.env.PORT||3000),controlUrl=process.env.CONTROL_COLLECTOR_URL||"https://kraken-collector-production.up.railway.app",confirmUrl=process.env.CONTROL_CONFIRM_URL||"https://kraken-rest-confirm-production.up.railway.app";
async function json(url:string){const r=await fetch(url,{signal:AbortSignal.timeout(45000)});if(!r.ok)throw Error(`HTTP ${r.status}`);return r.json() as Promise<any>}
async function confirm(pair:string){const x=await json(`${confirmUrl}/confirm?pair=${encodeURIComponent(pair)}`);return {pair:x.pair??x.symbol??pair,success:!!x.success,twoSidedBook:!!(x.two_sided_book??x.twoSidedBook),executableBbo:!!(x.executable_bbo??x.executableBbo),recentTradeConfirmation:!!(x.recent_trade_confirmation??x.recentTradeConfirmation),newestTradeAgeSeconds:x.newest_trade_age_seconds??x.newestTradeAgeSeconds??null,bestBid:x.best_bid??x.bestBid??null,bestAsk:x.best_ask??x.bestAsk??null,fetchedAt:x.fetched_at??x.fetchedAt??""}}
const deps={scan:()=>json(`${controlUrl}/scan`),confirm,pause:(ms:number)=>Bun.sleep(ms),now:()=>new Date()};
const runner=createCycleRunner(deps,createReadOnlyShadowLoader(process.env.SHADOW_ARTIFACT_URL,fetch,process.env.SHADOW_TRUSTED_SOURCE_SHA));
setTimeout(()=>{void(async()=>{for(;;){await runner.run("scheduled");await Bun.sleep(300000)}})()},5000);
Bun.serve({port,fetch:createCycleHttpHandler(runner)});
