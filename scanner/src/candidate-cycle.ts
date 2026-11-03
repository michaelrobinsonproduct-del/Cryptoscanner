import {selectDiscoveryCandidates,classifyConfirmationFailure} from "./candidate-contract";
import {evaluatePromotion} from "./promotion";
export type Dependencies={scan:()=>Promise<any>;confirm:(pair:string)=>Promise<any>;pause:(ms:number)=>Promise<void>;now:()=>Date};
const MAX_AGE_MS=600000;
function validTime(value:unknown,now:number){if(typeof value!=="string"||!Number.isFinite(Date.parse(value)))return false;const t=Date.parse(value);return t<=now&&now-t<=MAX_AGE_MS}
function validQuote(x:any,pair:string,now:number){return x&&x.pair===pair&&validTime(x.fetchedAt,now)&&Number.isFinite(Number(x.bestAsk))&&Number(x.bestAsk)>0}
export async function executeCandidateCycle(d:Dependencies){
 const at=d.now().toISOString(), candidates:any[]=[];
 const scan=await d.scan();
 if(!scan||typeof scan!=="object"||Array.isArray(scan))throw Error("invalid_discovery_response");
 const raw=scan.candidates??scan.results??scan.shortlist;
 if(!Array.isArray(raw))throw Error("missing_discovery_candidates");
 const selected=selectDiscoveryCandidates(scan);
 for(const x of selected){
  const {pair,score,displacementPct,discoveredAt}=x;
  if(!validTime(discoveredAt,d.now().getTime())){candidates.push({pair,decision:"ABSTAIN",reason:"stale_or_invalid_discovery"});continue}
  try {
   const first=await d.confirm(pair);
   await d.pause(2500);
   const second=await d.confirm(pair);
   const now=d.now().getTime();
   if(!validTime(discoveredAt,now)){candidates.push({pair,decision:"ABSTAIN",reason:"stale_or_invalid_discovery"});continue}
   if(first?.pair!==pair||second?.pair!==pair){candidates.push({pair,decision:"ABSTAIN",reason:"confirmation_pair_mismatch"});continue}
   if(!validQuote(first,pair,now)||!validQuote(second,pair,now)){candidates.push({pair,decision:"ABSTAIN",reason:"stale_or_invalid_confirmation"});continue}
   const result=evaluatePromotion({pair,score,displacementPct,discoveryPrice:Number(first.bestAsk),discoveryAt:discoveredAt},first,second);
   candidates.push({pair,score,displacement_pct:displacementPct,discovered_at:discoveredAt,...result,first,second});
  }catch(e){candidates.push(classifyConfirmationFailure(pair,e))}
 }
 const abstentions=candidates.filter(x=>x.decision==="ABSTAIN").length;
 const watches=candidates.filter(x=>x.decision==="WATCH").length;
 const eligible=candidates.filter(x=>x.decision==="PROMOTION_ELIGIBLE").length;
 const status=raw.length===0?"NO_DISCOVERY_CANDIDATES":selected.length===0?"NO_QUALIFIED_DISCOVERY":eligible+watches===0?"ABSTAIN_NO_QUALIFIED_CONFIRMATION":"CANDIDATES_EVALUATED";
 return {mode:"shadow",control_untouched:true,at,scan_status:status,coverage:{discovery_rows:raw.length,selected_candidates:selected.length,watch:watches,promotion_eligible:eligible,abstentions,discarded_discovery_rows:raw.length-selected.length},candidates};
}
