import {selectDiscoveryCandidates,classifyConfirmationFailure} from "./candidate-contract";
import {evaluatePromotion} from "./promotion";
export type Dependencies={scan:()=>Promise<any>;confirm:(pair:string)=>Promise<any>;pause:(ms:number)=>Promise<void>;now:()=>Date};
export async function executeCandidateCycle(d:Dependencies){
 const at=d.now().toISOString(), candidates:any[]=[];
 for(const x of selectDiscoveryCandidates(await d.scan())){
  const {pair,score,displacementPct,discoveredAt}=x;
  try {
   const first=await d.confirm(pair);await d.pause(2500);const second=await d.confirm(pair);
   const t=Date.parse(discoveredAt),now=d.now().getTime(),ask=Number(first.bestAsk);
   if(t>now||now-t>600000||!Number.isFinite(ask)||ask<=0){candidates.push({pair,decision:"ABSTAIN",reason:"stale_or_invalid_discovery"});continue}
   if(first.pair!==pair||second.pair!==pair){candidates.push({pair,decision:"ABSTAIN",reason:"confirmation_pair_mismatch"});continue}
   const result=evaluatePromotion({pair,score,displacementPct,discoveryPrice:ask,discoveryAt:discoveredAt},first,second);
   candidates.push({pair,score,displacement_pct:displacementPct,discovered_at:discoveredAt,...result,first,second});
  }catch(e){candidates.push(classifyConfirmationFailure(pair,e))}
 }
 return {mode:"shadow",control_untouched:true,at,candidates};
}
