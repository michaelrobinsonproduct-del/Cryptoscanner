/** Prospective holdout scoring. Never use these metrics to backfill missing outcomes. */
export type Case={id:string;firstSeenAt:string;horizonEndAt:string;outcomePct:number|null;controlAlertAt:string|null;challengerAlertAt:string|null};
export type Metrics={total:number;eligible:number;missing:number;positive:number;controlRecall:number|null;challengerRecall:number|null;controlPrecision:number|null;challengerPrecision:number|null;controlEarlyHits:number;challengerEarlyHits:number};
export function evaluate(rows:Case[],thresholdPct=100):Metrics{
 const eligible=rows.filter(r=>r.outcomePct!==null&&Number.isFinite(r.outcomePct)&&Date.parse(r.horizonEndAt)<=Date.now());
 const positive=eligible.filter(r=>r.outcomePct!>=thresholdPct);
 const validAlert=(r:Case,k:"controlAlertAt"|"challengerAlertAt")=>{
  const a=r[k]&&Date.parse(r[k]!);
  return typeof a==="number"&&Number.isFinite(a)&&a>=Date.parse(r.firstSeenAt)&&a<Date.parse(r.horizonEndAt);
 };
 const score=(k:"controlAlertAt"|"challengerAlertAt")=>{
  const alerted=eligible.filter(r=>validAlert(r,k));
  const hits=positive.filter(r=>validAlert(r,k));
  return {recall:positive.length?hits.length/positive.length:null,precision:alerted.length?hits.length/alerted.length:null,hits:hits.length};
 };
 const a=score("controlAlertAt"),b=score("challengerAlertAt");
 return {total:rows.length,eligible:eligible.length,missing:rows.length-eligible.length,positive:positive.length,controlRecall:a.recall,challengerRecall:b.recall,controlPrecision:a.precision,challengerPrecision:b.precision,controlEarlyHits:a.hits,challengerEarlyHits:b.hits};
}
export function eligibleForPromotion(m:Metrics,minPositive=30){
 return m.positive>=minPositive&&m.controlRecall!==null&&m.challengerRecall!==null&&m.controlPrecision!==null&&m.challengerPrecision!==null&&m.challengerRecall>m.controlRecall&&m.challengerPrecision>=m.controlPrecision;
}
