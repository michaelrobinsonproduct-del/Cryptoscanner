export type ScanCycle = {cycleId:string; startedAt:string; completedAt:string|null; universe:number; scanned:number; failed:number; persisted:boolean; retrieved:boolean};
export function validateCycles(cycles:ScanCycle[], expectedIds:string[]):{ok:boolean;issues:string[]}{
 const issues:string[]=[];const seen=new Set<string>();const expected=new Set(expectedIds);
 if(expected.size!==expectedIds.length)issues.push("duplicate_expected_cycle_id");
 for(const c of cycles){
  if(seen.has(c.cycleId))issues.push("duplicate_cycle:"+c.cycleId);
  seen.add(c.cycleId);
  if(!expected.has(c.cycleId))issues.push("unexpected_cycle:"+c.cycleId);
  const started=Date.parse(c.startedAt),finished=c.completedAt===null?NaN:Date.parse(c.completedAt);
  if(!Number.isFinite(started)||!Number.isFinite(finished)||finished<started)issues.push("invalid_completion:"+c.cycleId);
  if(!Number.isSafeInteger(c.universe)||c.universe<=0||!Number.isSafeInteger(c.scanned)||c.scanned!==c.universe||!Number.isSafeInteger(c.failed)||c.failed!==0)issues.push("incomplete_coverage:"+c.cycleId);
  if(!c.persisted||!c.retrieved)issues.push("not_durable:"+c.cycleId);
 }
 for(const id of expected)if(!seen.has(id))issues.push("missing_cycle:"+id);
 if(expected.size===0)issues.push("missing_expected_schedule");
 return {ok:issues.length===0,issues};
}
