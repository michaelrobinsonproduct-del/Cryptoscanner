import { targetCandleOpen, candleReturn, isClosedByDeadline, validBaseline } from "./forward-math";
// Prospective forward-outcome measurement: closed hourly Kraken candles only.
// Never substitute a late spot quote for a historical horizon price.
const url=process.env.CHALLENGER_SUPABASE_URL;
const key=process.env.CHALLENGER_SUPABASE_SERVICE_KEY;
if(!url||!key)throw Error("challenger_outcome_credentials_required");
const headers={apikey:key,Authorization:"Bearer "+key,"Content-Type":"application/json"};
const base=url.replace(/\/$/,"")+"/rest/v1/";
async function api(path:string,init:RequestInit={}){const r=await fetch(base+path,{...init,headers:{...headers,...init.headers},signal:AbortSignal.timeout(30000)});if(!r.ok)throw Error("supabase_"+r.status+":"+(await r.text()).slice(0,200));return r.status===204?null:r.json()}
const rows=await api("challenger_forward_outcomes?select=observation_id,horizon_hours,due_at,status,challenger_observations(pair,baseline_ask,baseline_at)&status=eq.pending&due_at=lte."+encodeURIComponent(new Date(Date.now()-3600000).toISOString())+"&limit=500");
let measured=0,missing=0;
const candleCache=new Map<string,number>();
for(const row of rows){
 const obs=row.challenger_observations;
 if(!obs||!String(obs.pair??"").trim()||!validBaseline(Number(obs.baseline_ask),String(obs.baseline_at??""),new Date(row.due_at).getTime()/1000)){missing++;console.log(JSON.stringify({observation_id:row.observation_id,horizon_hours:row.horizon_hours,status:"pending_retry",reason:"missing_or_invalid_baseline"}));continue;}
 const due=Math.floor(new Date(row.due_at).getTime()/1000);
 if(!Number.isFinite(due))throw Error("invalid_outcome_deadline");
 if(Date.now()-due*1000>29*24*3600*1000){await api("challenger_forward_outcomes?observation_id=eq."+row.observation_id+"&horizon_hours=eq."+row.horizon_hours+"&status=eq.pending",{method:"PATCH",headers:{"Prefer":"return=minimal"},body:JSON.stringify({status:"missing_price",measured_at:new Date().toISOString(),measurement_method:"unavailable_kraken_ohlc_retention_window"})});missing++;console.log(JSON.stringify({observation_id:row.observation_id,horizon_hours:row.horizon_hours,status:"missing_price",reason:"outside_kraken_ohlc_retention"}));continue;} // Terminally label outcomes that can no longer be recovered from Kraken hourly OHLC.
 // Use a fully closed candle ending at the horizon, never the unfinished current candle.
 const targetOpen=targetCandleOpen(due);
 const cacheKey=obs.pair+":"+targetOpen;
 let price=candleCache.get(cacheKey)??NaN;
 if(!Number.isFinite(price)){
  const kraken=await fetch("https://api.kraken.com/0/public/OHLC?pair="+encodeURIComponent(obs.pair)+"&interval=60&since="+(due-7200),{signal:AbortSignal.timeout(20000)}).then(r=>r.json());
  if(kraken.error?.length){missing++;console.log(JSON.stringify({observation_id:row.observation_id,horizon_hours:row.horizon_hours,status:"pending_retry",reason:"kraken_ohlc_error",errors:kraken.error}));continue;}
  const series=Object.entries(kraken.result??{}).filter(([name])=>name!=="last").map(([,v])=>v).find(Array.isArray) as any[]|undefined;
  const candle=series?.find(c=>Number(c[0])===targetOpen);
  price=candle?Number(candle[4]):NaN;
  if(Number.isFinite(price)&&price>0)candleCache.set(cacheKey,price);
 }
 const valid=Number.isFinite(price)&&price>0 && isClosedByDeadline(targetOpen,Date.now());
 if(!valid){missing++;continue;} // Missing historical candles remain pending for later retry.
 const payload={status:"measured",measured_at:new Date().toISOString(),ask_at_horizon:price,return_pct:candleReturn(Number(obs.baseline_ask),price),measurement_method:"kraken_hourly_candle_close_vs_initial_baseline_ask"};
 const updated=await api("challenger_forward_outcomes?observation_id=eq."+row.observation_id+"&horizon_hours=eq."+row.horizon_hours+"&status=eq.pending",{method:"PATCH",headers:{"Prefer":"return=representation"},body:JSON.stringify(payload)});
 if(!Array.isArray(updated)||updated.length!==1){missing++;console.log(JSON.stringify({observation_id:row.observation_id,horizon_hours:row.horizon_hours,status:"not_updated",reason:"concurrent_update_or_row_not_returned",rows_returned:Array.isArray(updated)?updated.length:null}));continue;}
 measured++;
}
console.log(JSON.stringify({pending_checked:rows.length,measured,missing,method:"hourly_closed_candle_close_vs_initial_executable_ask",caveat:"OHLC candle close is not an executable ask"}));
