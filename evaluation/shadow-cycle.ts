import { mkdir } from "node:fs/promises";
import { evaluatePromotion } from "../scanner/src/promotion";
import type { DiscoveryCandidate, MarketConfirmation } from "../scanner/src/types";
const collector=process.env.CONTROL_COLLECTOR_URL||"https://kraken-collector-production.up.railway.app";
const kraken="https://api.kraken.com/0/public";
async function j(url:string){const r=await fetch(url,{signal:AbortSignal.timeout(45000)});if(!r.ok)throw new Error(String(r.status));return r.json() as Promise<any>}
async function independentConfirmation(pair:string):Promise<MarketConfirmation>{
const q="pair="+encodeURIComponent(pair);
const [t,d,tr]=await Promise.all(["Ticker?","Depth?","Trades?"].map(p=>j(kraken+"/"+p+q)));
for(const z of [t,d,tr])if(!Array.isArray(z.error)||z.error.length)throw Error("kraken_api_error:"+String(z.error));
const first=(o:any)=>Object.entries(o??{}).find(([k])=>k!=="last")?.[1] as any;
const tick=first(t.result),book=first(d.result),trades=first(tr.result);
const bestBid=Number(tick?.b?.[0]),bestAsk=Number(tick?.a?.[0]);
const twoSidedBook=!!book?.bids?.length&&!!book?.asks?.length;
const executableBbo=twoSidedBook&&bestBid>0&&bestAsk>=bestBid&&Number(book.bids[0][0])>0&&Number(book.asks[0][0])>=Number(book.bids[0][0]);
const age=trades?.length?Date.now()/1000-Number(trades[trades.length-1][2]):null;
const recentTradeConfirmation=age!==null&&age>=0&&age<=60;
return {pair,success:!!(executableBbo&&recentTradeConfirmation),twoSidedBook,executableBbo:!!executableBbo,recentTradeConfirmation,newestTradeAgeSeconds:age,bestBid,bestAsk,fetchedAt:new Date().toISOString()};
}
function confirmation(pair:string,z:any):MarketConfirmation{return{pair,success:!!z.success,twoSidedBook:!!z.two_sided_book,executableBbo:!!z.executable_bbo,recentTradeConfirmation:!!z.recent_trade_confirmation,newestTradeAgeSeconds:Number.isFinite(Number(z.newest_trade_age_seconds))?Number(z.newest_trade_age_seconds):null,bestBid:Number.isFinite(Number(z.best_bid))?Number(z.best_bid):null,bestAsk:Number.isFinite(Number(z.best_ask))?Number(z.best_ask):null,fetchedAt:String(z.fetched_at||new Date().toISOString())}}
const scan=await j(collector+"/scan");const rows=(scan.candidates??scan.results??scan.shortlist??[]).slice(0,20);const candidates:any[]=[];const watchlist:any[]=[];const diagnostics={rows:rows.length,missingPair:0,belowScore:0,displaced:0,attempted:0,missingScore:0,missingDisplacement:0};const observedFields=new Set<string>();const nestedFields:Record<string,Set<string>>={discovery_metrics:new Set(),live_validation:new Set()};
for(const x of rows){for(const field of Object.keys(x))observedFields.add(field);for(const field of Object.keys(nestedFields)){const value=x[field];if(value&&typeof value==="object"&&!Array.isArray(value))for(const key of Object.keys(value))nestedFields[field].add(key)}const pair=x.pair??x.symbol;if(!pair){diagnostics.missingPair++;continue}const rawScore=x.score??x.discovery_score,rawDisp=x.displacement_pct??x.displacementPct??x.discovery_metrics?.displacement_pct;const score=Number(rawScore),disp=Number(rawDisp);if(rawScore==null||!Number.isFinite(score)){diagnostics.missingScore++;watchlist.push({pair,reason:"missing_score",available_fields:Object.keys(x)});continue}if(rawDisp==null||!Number.isFinite(disp)){diagnostics.missingDisplacement++;watchlist.push({pair,score,reason:"missing_displacement",available_fields:Object.keys(x)});continue}if(score<80){diagnostics.belowScore++;watchlist.push({pair,score,displacement_pct:disp,reason:"score_below_80",discovery_at:String(x.discovered_at??scan.fetched_at??new Date().toISOString()),outcome_status:"pending_baseline"});continue}if(Math.abs(disp)>3){diagnostics.displaced++;watchlist.push({pair,score,displacement_pct:disp,reason:"displacement_above_3pct",discovery_at:String(x.discovered_at??scan.fetched_at??new Date().toISOString()),outcome_status:"pending_baseline"});continue}diagnostics.attempted++;try{const a=await independentConfirmation(pair);await Bun.sleep(2500);const b=await independentConfirmation(pair);const baseline=Number(a.bestAsk??0);const dc:DiscoveryCandidate={pair,score,displacementPct:disp,discoveryPrice:baseline,discoveryAt:String(x.discovered_at??scan.fetched_at??new Date().toISOString())};const decision=evaluatePromotion(dc,a,b);candidates.push({pair,score,displacement_pct:disp,...decision,first_trade_age_s:a.newestTradeAgeSeconds,second_trade_age_s:b.newestTradeAgeSeconds,entry_ask:baseline>0?baseline:null,second_ask:b.bestAsk,confirmation_at:b.fetchedAt,discovery_at:dc.discoveryAt,outcome_status:baseline>0?"pending_24h_48h_72h":"missing_baseline"})}catch(e){candidates.push({pair,score,displacement_pct:disp,decision:"WATCH",reason:"confirmation_error",error:String(e)})}}
// Capture a timestamped, independent reference ask for rejected candidates without altering promotion decisions.
for(const item of watchlist){
 if(item.reason!=="score_below_80"&&item.reason!=="displacement_above_3pct")continue;
 try{
  const baseline=await independentConfirmation(String(item.pair));
  const ask=Number(baseline.bestAsk);
  item.reference_ask=Number.isFinite(ask)&&ask>0?ask:null;
  item.reference_at=baseline.fetchedAt;
  item.reference_status=item.reference_ask!==null?"observed":"missing_ask";item.outcome_status=item.reference_ask!==null?"pending_24h_48h_72h":"missing_baseline";
 }catch(e){item.reference_ask=null;item.reference_status="reference_error";item.outcome_status="missing_baseline";item.reference_error=String(e)}
}
const result={service:"cryptoscanner-challenger",mode:"shadow",control_untouched:true,created_at:new Date().toISOString(),source_scan:{build:scan.build??scan.version??null,count:rows.length,diagnostics,observed_fields:[...observedFields].sort(),nested_fields:Object.fromEntries(Object.entries(nestedFields).map(([k,v])=>[k,[...v].sort()])),baseline_semantics:"refresh1_executable_ask"},watchlist,candidates};await mkdir("evaluation/out",{recursive:true});const name="evaluation/out/shadow-"+Date.now()+".json";await Bun.write(name,JSON.stringify(result,null,2));
const dbUrl=process.env.CHALLENGER_SUPABASE_URL;
const dbKey=process.env.CHALLENGER_SUPABASE_SERVICE_KEY;
if(dbUrl&&dbKey){
 const cycleId=name.split("/").pop()!.replace(".json","");
 const observations=[...candidates.map((x:any)=>({pair:x.pair,decision:x.decision,baseline_ask:x.entry_ask??null,baseline_at:x.confirmation_at??null,source_payload:x})),...watchlist.map((x:any)=>({pair:x.pair,decision:"WATCH",baseline_ask:x.reference_ask??null,baseline_at:x.reference_at??null,source_payload:x}))].map((x:any)=>({cycle_id:cycleId,pair:String(x.pair),observed_at:result.created_at,decision:x.decision==="PROMOTION_ELIGIBLE"?"PROMOTION_ELIGIBLE":"WATCH",baseline_ask:x.baseline_ask,baseline_at:x.baseline_ask?x.baseline_at:null,baseline_status:x.baseline_ask&&x.baseline_at?"observed":"missing_baseline",source_payload:x.source_payload}));
 const response=await fetch(dbUrl.replace(/\\/$/,"")+"/rest/v1/challenger_observations",{method:"POST",headers:{"apikey":dbKey,"Authorization":"Bearer "+dbKey,"Content-Type":"application/json","Prefer":"resolution=merge-duplicates"},body:JSON.stringify(observations),signal:AbortSignal.timeout(45000)});
 if(!response.ok)throw Error("observation_persistence_failed:"+response.status+":"+(await response.text()).slice(0,500));
 console.log(JSON.stringify({persisted_observations:observations.length,cycle_id:cycleId}));
}else console.log("observation_persistence_not_configured");
console.log(JSON.stringify({file:name,candidates:candidates.length,diagnostics,observed_fields:[...observedFields].sort(),nested_fields:Object.fromEntries(Object.entries(nestedFields).map(([k,v])=>[k,[...v].sort()])),promotable:candidates.filter(x=>x.decision==="PROMOTION_ELIGIBLE").length}));
