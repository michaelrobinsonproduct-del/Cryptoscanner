export type ShadowEvidence={version:string;source_sha:string;qualified:boolean;held_out_samples:number;held_out_lift:number|null;outcome_ledger_sha:string;score_ledger_sha:string;outcome_rows:number};
export type ShadowScore={pair:string;observed_at:string;version:string;score:number;computed_at:string;source_sha:string};
export type ShadowOutcome={pair:string;observed_at:string;label:"HIT"|"MISS"|"ABSTAIN";source_sha:string};
export type ShadowDecision={mode:"shadow_only";status:"SCORED"|"PENDING_OUTCOME"|"ABSTAIN";reason:string;challenger_version:string|null;baseline_score:number;challenger_score:number|null;outcome_label:string|null;production_promoted:false};
const sha=(v:unknown)=>typeof v==="string"&&/^[0-9a-f]{64}$/i.test(v);
export function evaluateShadowCandidate(candidate:{pair:string;score:number;discovered_at:string;decision:string},evidence:ShadowEvidence|null,outcomes:ShadowOutcome[],scores:ShadowScore[]=[]):ShadowDecision{
 const base={mode:"shadow_only" as const,baseline_score:candidate.score,challenger_version:evidence?.version??null,production_promoted:false as const};
 const abstain=(reason:string):ShadowDecision=>({...base,status:"ABSTAIN",reason,challenger_score:null,outcome_label:null});
 if(candidate.decision==="ABSTAIN"||!Number.isFinite(candidate.score)||!candidate.pair||!Number.isFinite(Date.parse(candidate.discovered_at)))return abstain("invalid_candidate");
 if(!evidence||!/^[-.a-zA-Z0-9_]{1,64}$/.test(evidence.version)||!sha(evidence.source_sha)||!sha(evidence.outcome_ledger_sha)||!evidence.qualified||!Number.isInteger(evidence.held_out_samples)||evidence.held_out_samples<=0||!Number.isInteger(evidence.outcome_rows)||evidence.outcome_rows<=0||!Number.isFinite(evidence.held_out_lift))return abstain("unqualified_challenger");
 const discoveryTime=Date.parse(candidate.discovered_at);
 const sameObservation=(timestamp:string)=>Date.parse(timestamp)===discoveryTime;
 const matches=scores.filter(s=>s.pair===candidate.pair&&sameObservation(s.observed_at)&&s.version===evidence.version&&s.source_sha===evidence.source_sha);
 if(matches.length!==1||!Number.isFinite(matches[0].score)||matches[0].score<0||matches[0].score>100||!Number.isFinite(Date.parse(matches[0].computed_at))||Date.parse(matches[0].computed_at)>Date.parse(candidate.discovered_at))return abstain("missing_or_leaky_challenger_score");
 const matching=outcomes.filter(x=>x.pair===candidate.pair&&sameObservation(x.observed_at));
 if(matching.length===0)
  return {...base,status:"PENDING_OUTCOME",reason:"outcome_not_mature",challenger_score:matches[0].score,outcome_label:null};
 if(matching.length===1&&matching[0].label==="ABSTAIN"&&matching[0].source_sha===evidence.source_sha)
  return {...base,status:"ABSTAIN",reason:"source_outcome_gap",challenger_score:matches[0].score,outcome_label:null};
 if(matching.length!==1||matching[0].source_sha!==evidence.source_sha||!["HIT","MISS"].includes(matching[0].label))return abstain("missing_or_ambiguous_outcome");
 return {...base,status:"SCORED",reason:"qualified_shadow_only",challenger_score:matches[0].score,outcome_label:matching[0].label};
}
export function attachShadowEvaluation(cycle:any,evidence:ShadowEvidence|null,outcomes:ShadowOutcome[],scores:ShadowScore[]=[]){
 // Index immutable source-qualified ledgers once per scan rather than scanning
 // up to 10,000 history rows separately for every discovered candidate.
 const key=(pair:string,at:string)=>pair+"|"+Date.parse(at);
 const outcomeIndex=new Map<string,ShadowOutcome[]>(),scoreIndex=new Map<string,ShadowScore[]>();
 for(const row of outcomes){const k=key(row.pair,row.observed_at);const bucket=outcomeIndex.get(k);if(bucket)bucket.push(row);else outcomeIndex.set(k,[row]);}
 for(const row of scores){const k=key(row.pair,row.observed_at);const bucket=scoreIndex.get(k);if(bucket)bucket.push(row);else scoreIndex.set(k,[row]);}
 const candidates=(cycle.candidates??[]).map((c:any)=>{
  const k=key(c.pair,c.discovered_at);
  return {pair:c.pair,...evaluateShadowCandidate(c,evidence,outcomeIndex.get(k)??[],scoreIndex.get(k)??[])};
 });
 const coverage={candidates:candidates.length,scored:candidates.filter((c:any)=>c.status==="SCORED").length,pending_outcome:candidates.filter((c:any)=>c.status==="PENDING_OUTCOME").length,abstained:candidates.filter((c:any)=>c.status==="ABSTAIN").length,authenticated_outcomes:candidates.filter((c:any)=>c.status==="SCORED").length,
  observed_hits:candidates.filter((c:any)=>c.status==="SCORED"&&c.outcome_label==="HIT").length,
  observed_misses:candidates.filter((c:any)=>c.status==="SCORED"&&c.outcome_label==="MISS").length,
  source_gap_abstentions:candidates.filter((c:any)=>c.reason==="source_outcome_gap").length,
  source_qualified:!!evidence?.qualified};
 return {...cycle,shadow_evaluation:{evidence_version:evidence?.version??null,production_promoted:false,coverage,candidates}};
}
