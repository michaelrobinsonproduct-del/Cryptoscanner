/** Read-only bridge to Owner A's persisted PAPER_ONLY receipt. Never writes or re-scores. */
export type PaperReceipt={status:"VERIFIED_RECEIPT"|"UNAVAILABLE";scan_status:string|null;as_of:string|null;watch_count:number|null;observed_markets:number|null;eligible_pairs:number|null;ticker_rejections:Record<string,number>|null;ohlc_screened:number|null;abstention_count:number|null;source:"paper_pov";buy_approved:false;reason?:string};
const statuses=new Set(["WATCH","ABSTAIN_NO_LIQUID_CANDIDATES","ABSTAIN_NO_QUALIFIED_OHLC"]);
const count=(v:unknown)=>Number.isSafeInteger(v)&&Number(v)>=0;
export function parsePaperReceipt(value:unknown,now:Date):PaperReceipt{
 if(!value||typeof value!=="object"||Array.isArray(value))throw Error("invalid_paper_receipt");
 const x=value as Record<string,unknown>;
 if(x.mode!=="PAPER_ONLY"||x.buy_approved!==false||!statuses.has(String(x.scan_status)))throw Error("invalid_paper_receipt_mode");
 if(typeof x.as_of!=="string"||!Number.isFinite(Date.parse(x.as_of))||Date.parse(x.as_of)>now.getTime()||now.getTime()-Date.parse(x.as_of)>600000)throw Error("stale_paper_receipt");
 if(!Array.isArray(x.watch)||!Array.isArray(x.abstentions)||!count(x.observed_markets)||!count(x.ohlc_screened))throw Error("invalid_paper_coverage");
 if(x.watch.length>Number(x.ohlc_screened)||x.abstentions.length>Number(x.ohlc_screened)||x.watch.length+x.abstentions.length>Number(x.ohlc_screened))throw Error("inconsistent_paper_coverage");
 if(x.scan_status==="WATCH"&&x.watch.length===0||x.scan_status!=="WATCH"&&x.watch.length!==0||x.scan_status==="ABSTAIN_NO_LIQUID_CANDIDATES"&&Number(x.ohlc_screened)!==0)throw Error("inconsistent_paper_status");
 const categories=["missing_or_invalid_payload","invalid_price_or_volume","nonfinite_derived_metric"];
 let rejections:Record<string,number>|null=null;
 if(x.ticker_rejections!==undefined||x.eligible_pairs!==undefined){
  if(!count(x.eligible_pairs)||!x.ticker_rejections||typeof x.ticker_rejections!=="object"||Array.isArray(x.ticker_rejections))throw Error("invalid_ticker_coverage");
  const r=x.ticker_rejections as Record<string,unknown>;
  if(Object.keys(r).length!==categories.length||categories.some(k=>!count(r[k]))||Number(x.observed_markets)+categories.reduce((sum,k)=>sum+Number(r[k]),0)!==Number(x.eligible_pairs))throw Error("inconsistent_ticker_coverage");
  rejections=Object.fromEntries(categories.map(k=>[k,Number(r[k])]));
 }
 return {status:"VERIFIED_RECEIPT",scan_status:String(x.scan_status),as_of:x.as_of,watch_count:x.watch.length,observed_markets:Number(x.observed_markets),eligible_pairs:rejections?Number(x.eligible_pairs):null,ticker_rejections:rejections,ohlc_screened:Number(x.ohlc_screened),abstention_count:x.abstentions.length,source:"paper_pov",buy_approved:false};
}
export const unavailablePaperReceipt=(reason:string):PaperReceipt=>({status:"UNAVAILABLE",scan_status:null,as_of:null,watch_count:null,observed_markets:null,eligible_pairs:null,ticker_rejections:null,ohlc_screened:null,abstention_count:null,source:"paper_pov",buy_approved:false,reason});
export function createPaperReceiptReader(url:string|undefined,now:()=>Date,fetcher:typeof fetch=fetch):()=>Promise<PaperReceipt>{
 return async()=>{
  if(!url)return unavailablePaperReceipt("not_configured");
  const u=new URL(url);
  if(u.protocol!=="https:"||u.username||u.password||u.hash)throw Error("unsafe_paper_receipt_url");
  const response=await fetcher(u.toString(),{method:"GET",redirect:"error",signal:AbortSignal.timeout(8000),headers:{accept:"application/json"}});
  if(!response.ok)throw Error("paper_receipt_http_"+response.status);
  const body=await response.text();
  if(body.length>1000000)throw Error("paper_receipt_oversized");
  return parsePaperReceipt(JSON.parse(body),now());
 };
}
