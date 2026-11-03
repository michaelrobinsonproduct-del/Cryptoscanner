import {createHash} from "node:crypto";
/** Read-only consumer of Owner A's read_snapshot() output, not the mutable latest.json. */
export type A2Snapshot={status:"VERIFIED_SNAPSHOT"|"UNAVAILABLE";as_of:string|null;scan_status:string|null;receipt_sha256:string|null;watch:Array<{pair:string;rank:number;status:"PAPER_WATCH";price:number;move15_pct:number;volume_accel:number;baseline_score:number;challenger_score:number;quote_observed_at:string;prediction_id:string}>;eligible_pairs:number|null;observed_markets:number|null;abstention_counts:Record<string,number>|null;source:"a2_verified_readonly";buy_approved:false;reason?:string};
export const unavailableA2Snapshot=(reason:string):A2Snapshot=>({status:"UNAVAILABLE",as_of:null,scan_status:null,receipt_sha256:null,watch:[],eligible_pairs:null,observed_markets:null,abstention_counts:null,source:"a2_verified_readonly",buy_approved:false,reason});
const count=(v:unknown)=>typeof v==="number"&&Number.isSafeInteger(v)&&v>=0;
const timestamp=(v:unknown)=>typeof v==="string"&&/(Z|[+-]\d\d:\d\d)$/.test(v)&&Number.isFinite(Date.parse(v));
export function parseA2Snapshot(raw:unknown,now:Date):A2Snapshot{
 if(!raw||typeof raw!=="object"||Array.isArray(raw))throw Error("invalid_a2_snapshot");
 const x=raw as Record<string,any>,at=Date.parse(x.as_of);
 if(!timestamp(x.as_of)||at>now.getTime()||now.getTime()-at>600000)throw Error("stale_a2_snapshot");
 if(!/^[a-f0-9]{64}$/.test(x.receipt_sha256)||!count(x.eligible_pairs)||!count(x.observed_markets)||x.observed_markets>x.eligible_pairs||!Array.isArray(x.watch)||x.watch.length>12||x.watch.length>x.observed_markets)throw Error("invalid_a2_snapshot_coverage");
 if(!["WATCH","ABSTAIN_NO_LIQUID_CANDIDATES","ABSTAIN_NO_QUALIFIED_OHLC"].includes(x.scan_status)||Boolean(x.watch.length)!==(x.scan_status==="WATCH"))throw Error("invalid_a2_snapshot_status");
 if(!x.abstention_counts||typeof x.abstention_counts!=="object"||Array.isArray(x.abstention_counts)||Object.entries(x.abstention_counts).some(([k,v])=>!k||!count(v)))throw Error("invalid_a2_abstentions");
 const seen=new Set<string>();
 const stablecoin=/^(?:USDT|USDC|DAI|FDUSD|TUSD|PYUSD|USDD|USDP|EURC|RLUSD|USDG|GUSD)(?:USD|USDT|USDC|EUR|GBP)?$/;
 if(x.watch.length>0&&x.observed_markets===0)throw Error("invalid_a2_snapshot_coverage");
 for(let i=0;i<x.watch.length;i++){
  const c=x.watch[i];if(!c||typeof c!=="object"||c.rank!==i+1||c.status!=="PAPER_WATCH"||c.buy_approved!==false||typeof c.pair!=="string"||!/^[A-Z0-9]{3,24}$/.test(c.pair)||seen.has(c.pair)||stablecoin.test(c.pair)||c.as_of!==x.as_of||c.quote_timestamp_semantics!=="client_observed_not_exchange_event_time")throw Error("invalid_a2_candidate");
  seen.add(c.pair);
  if(!timestamp(c.quote_observed_at)||Date.parse(c.quote_observed_at)>at||now.getTime()-Date.parse(c.quote_observed_at)>600000)throw Error("stale_a2_quote");
  for(const k of ["price","move15_pct","volume_accel","baseline_score","challenger_score","spread_bps"])if(typeof c[k]!=="number"||!Number.isFinite(c[k]))throw Error("invalid_a2_metric");
  if(c.price<=0||c.volume_accel<=0||c.spread_bps<0||c.spread_bps>10000||c.prediction_id!==createHash("sha256").update("paper-v1|"+x.as_of+"|"+c.pair).digest("hex"))throw Error("invalid_a2_market_metric");
 }
 return {status:"VERIFIED_SNAPSHOT",as_of:x.as_of,scan_status:x.scan_status,receipt_sha256:x.receipt_sha256,watch:x.watch.map((c:any)=>({pair:c.pair,rank:c.rank,status:c.status,price:c.price,move15_pct:c.move15_pct,volume_accel:c.volume_accel,baseline_score:c.baseline_score,challenger_score:c.challenger_score,quote_observed_at:c.quote_observed_at,prediction_id:c.prediction_id})),eligible_pairs:x.eligible_pairs,observed_markets:x.observed_markets,abstention_counts:x.abstention_counts,source:"a2_verified_readonly",buy_approved:false};
}
export function createA2SnapshotReader(url:string|undefined,now:()=>Date,fetcher:typeof fetch=fetch):()=>Promise<A2Snapshot>{
 return async()=>{if(!url)return unavailableA2Snapshot("not_configured");const u=new URL(url);if(u.protocol!=="https:"||u.username||u.password||u.hash)throw Error("unsafe_a2_url");
 const response=await fetcher(u.toString(),{method:"GET",redirect:"error",signal:AbortSignal.timeout(8000),headers:{accept:"application/json"}});if(!response.ok)throw Error("a2_http_"+response.status);const length=response.headers.get("content-length");if(length!==null&&(!/^\d+$/.test(length)||Number(length)>200000))throw Error("a2_oversized");
 const reader=response.body?.getReader();if(!reader)throw Error("a2_empty_body");let bytes=0;const chunks:Uint8Array[]=[];
 try{for(;;){const part=await reader.read();if(part.done)break;bytes+=part.value.byteLength;if(bytes>200000)throw Error("a2_oversized");chunks.push(part.value)}}finally{await reader.cancel().catch(()=>{})}
 const body=new TextDecoder("utf-8",{fatal:true}).decode(Buffer.concat(chunks));return parseA2Snapshot(JSON.parse(body),now());};
}
