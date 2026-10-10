import {test,expect} from "bun:test";
import {evaluate,eligibleForPromotion,type Case} from "./prospective-quality";
const t=(hour:number)=>new Date(Date.UTC(2026,0,1,hour)).toISOString();
const row=(id:string,pct:number|null,control:string|null,challenger:string|null):Case=>({id,firstSeenAt:t(0),horizonEndAt:t(2),outcomePct:pct,controlAlertAt:control,challengerAlertAt:challenger});
test("excludes missing outcomes and scores early alerts",()=>{
 const m=evaluate([row("winner",150,null,t(1)),row("loser",0,t(1),null),row("missing",null,null,t(1))]);
 expect(m.total).toBe(3);expect(m.eligible).toBe(2);expect(m.missing).toBe(1);
 expect(m.controlRecall).toBe(0);expect(m.challengerRecall).toBe(1);
 expect(m.controlPrecision).toBe(0);expect(m.challengerPrecision).toBe(1);
});
test("rejects post-horizon alerts",()=>{
 const m=evaluate([row("winner",200,t(3),t(1))]);
 expect(m.controlRecall).toBe(0);expect(m.challengerRecall).toBe(1);
});
test("does not promote without enough positive outcomes",()=>{
 const m=evaluate([row("winner",200,null,t(1)),row("loser",0,t(1),null)]);
 expect(eligibleForPromotion(m)).toBe(false);
 expect(eligibleForPromotion(m,1)).toBe(true);
});
test("rejects weaker precision",()=>{
 const m=evaluate([row("winner",200,null,t(1)),row("loser",0,null,t(1))]);
 expect(eligibleForPromotion(m,1)).toBe(false);
});
