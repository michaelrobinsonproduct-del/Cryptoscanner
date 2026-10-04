export interface CycleAudit{scheduledAt:string;observedAt:string|null;status:"OK"|"MISSING"|"LATE"}
export function audit(scheduled:string[],observed:string[],toleranceMinutes=5):CycleAudit[]{
 const parsed=observed.map(x=>({raw:x,ms:Date.parse(x)})).filter(x=>Number.isFinite(x.ms));
 return scheduled.map(s=>{const t=Date.parse(s);if(!Number.isFinite(t)||!parsed.length)return{scheduledAt:s,observedAt:null,status:"MISSING"};
 const nearest=parsed.reduce((a,b)=>Math.abs(b.ms-t)<Math.abs(a.ms-t)?b:a);const delta=Math.abs(nearest.ms-t);
 return{scheduledAt:s,observedAt:nearest.raw,status:delta<=toleranceMinutes*60000?"OK":"LATE"}});
}
