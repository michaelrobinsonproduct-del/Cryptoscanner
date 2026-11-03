export type ShadowEvidence={version:string;source_sha:string;qualified:boolean;held_out_samples:number;held_out_lift:number|null;outcome_ledger_sha:string;outcome_rows:number};
export type ShadowOutcome={pair:string;observed_at:string;label:"HIT"|"MISS"|"ABSTAIN";source_sha:string};
export type ShadowDecision={mode:"shadow_only";status:"SCORED"|"ABSTAIN";reason:string;challenger_version:string|null;baseline_score:number;challenger_score:number|null;outcome_label:string|null;production_promoted:false};
const sha=(v:unknown)=>typeof v==="string"&&/^[0-9a-f]{64}$/i.test(v);
export function evaluateShadowCandidate(candidate:{pair:string;score:number;discovered_at:string;decision:string},evidence:ShadowEvidence|null,outcomes:ShadowOutcome[]):ShadowDecision{
 const base={mode:"shadow_only" as const,baseline_score:candidate.score,challenger_version:evidence?.version??null,production_promoted:false as const};
 const abstain=(reason:string):ShadowDecision=>({...base,status:"ABSTAIN",reason,challenger_score:null,outcome_label:null});
 if(candidate.decision==="ABSTAIN"||!Number.isFinite(candidate.score)||!candidate.pair||!Number.isFinite(Date.parse(candidate.discovered_at)))return abstain("invalid_candidate");
 if(!evidence||!/^[-.a-zA-Z0-9_]{1,64}$/.test(evidence.version)||!sha(evidence.source_sha)||!sha(evidence.outcome_ledger_sha)||!evidence.qualified||!Number.isInteger(evidence.held_out_samples)||evidence.held_out_samples<=0||!Number.isInteger(evidence.outcome_rows)||evidence.outcome_rows<=0||!Number.isFinite(evidence.held_out_lift))return abstain("unqualified_challenger");
 const matching=outcomes.filter(x=>x.pair===candidate.pair&&x.observed_at===candidate.discovered_at);
 if(matching.length!==1||matching[0].source_sha!==evidence.source_sha||matching[0].label==="ABSTAIN"||!["HIT","MISS"].includes(matching[0].label))return abstain("missing_or_ambiguous_outcome");
 // Shadow-only comparison: bounded uplift annotation; never changes baseline or production decisions.
 const delta=Math.max(-10,Math.min(10,evidence.held_out_lift!));
 return {...base,status:"SCORED",reason:"qualified_shadow_only",challenger_score:Math.max(0,Math.min(100,candidate.score+delta)),outcome_label:matching[0].label};
}
export function attachShadowEvaluation(cycle:any,evidence:ShadowEvidence|null,outcomes:ShadowOutcome[]){
 return {...cycle,shadow_evaluation:{evidence_version:evidence?.version??null,production_promoted:false,candidates:(cycle.candidates??[]).map((c:any)=>({pair:c.pair,...evaluateShadowCandidate(c,evidence,outcomes)}))}};
}
