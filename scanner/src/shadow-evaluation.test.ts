import {test,expect} from "bun:test";
import {createCycleRunner} from "./cycle-runner";
import {evaluateShadowCandidate} from "./shadow-evaluation";
const stamp="2026-11-03T04:00:00Z",discovered="2026-11-03T03:59:00Z",source="a".repeat(64),ledger="b".repeat(64);
const row={pair:"TAOUSD",score:85,displacement_pct:1,discovered_at:discovered};
const quote={pair:"TAOUSD",success:true,twoSidedBook:true,executableBbo:true,recentTradeConfirmation:true,newestTradeAgeSeconds:5,bestAsk:100,bestBid:99,fetchedAt:"2026-11-03T03:59:30Z"};
const deps={scan:async()=>({candidates:[row]}),confirm:async()=>quote,pause:async()=>{},now:()=>new Date(stamp)};
const evidence={version:"challenger-v2",source_sha:source,outcome_ledger_sha:ledger,score_ledger_sha:ledger,qualified:true,held_out_samples:42,held_out_lift:4,outcome_rows:1};
const scores=[{pair:"TAOUSD",observed_at:discovered,computed_at:"2026-11-03T03:58:00Z",version:"challenger-v2",score:89,source_sha:source}];
const outcomes=[{pair:"TAOUSD",observed_at:discovered,label:"HIT" as const,source_sha:source}];
test("manual and scheduled cycles attach same qualified versioned shadow result without changing baseline",async()=>{
 const r=createCycleRunner(deps,async()=>({evidence,outcomes,scores}));
 const manual=await r.run("manual"),scheduled=await r.run("scheduled");
 expect(manual.ok).toBe(true);expect(manual.result).toEqual(scheduled.result);
 expect(manual.result.shadow_evaluation.candidates[0]).toMatchObject({status:"SCORED",baseline_score:85,challenger_score:89,outcome_label:"HIT",production_promoted:false});
 expect(manual.result.candidates[0]).toEqual(scheduled.result.candidates[0]);
});
test("unqualified or ambiguous ledger abstains without scoring",async()=>{
 const c={pair:"TAOUSD",score:85,discovered_at:discovered,decision:"WATCH"};
 expect(evaluateShadowCandidate(c,{...evidence,qualified:false},outcomes).status).toBe("ABSTAIN");
 expect(evaluateShadowCandidate(c,evidence,[...outcomes,...outcomes],scores).reason).toBe("missing_or_ambiguous_outcome");
 expect(evaluateShadowCandidate(c,evidence,[{...outcomes[0],source_sha:"c".repeat(64)}],scores).status).toBe("ABSTAIN");
});
test("ledger failure leaves baseline cycle working but records shadow abstention",async()=>{
 const r=createCycleRunner(deps,async()=>{throw Error("ledger unavailable")});
 const run=await r.run("manual");
 expect(run.ok).toBe(true);expect(run.result.candidates).toHaveLength(1);
 expect(run.result.shadow_evaluation.candidates[0]).toMatchObject({status:"ABSTAIN",reason:"unqualified_challenger",production_promoted:false});
});

test("no invented uplift and no post-discovery challenger scoring",()=>{
 const c={pair:"TAOUSD",score:85,discovered_at:discovered,decision:"WATCH"};
 expect(evaluateShadowCandidate(c,evidence,outcomes).reason).toBe("missing_or_leaky_challenger_score");
 expect(evaluateShadowCandidate(c,evidence,outcomes,[{...scores[0],computed_at:"2026-11-03T04:01:00Z"}]).status).toBe("ABSTAIN");
});

test("qualified pre-discovery challenger score is visible pending outcome, never counted as hit",async()=>{
 const r=createCycleRunner(deps,async()=>({evidence,outcomes:[],scores}));
 const manual=await r.run("manual"),scheduled=await r.run("scheduled");
 expect(manual.result).toEqual(scheduled.result);
 expect(manual.result.shadow_evaluation.candidates[0]).toMatchObject({status:"PENDING_OUTCOME",reason:"outcome_not_mature",challenger_score:89,outcome_label:null,production_promoted:false});
 expect(manual.result.candidates[0].score).toBe(85);
});
test("gap-abstaining outcomes are explicit abstentions, duplicates or mismatched provenance fail closed",()=>{
 const c={pair:"TAOUSD",score:85,discovered_at:discovered,decision:"WATCH"};
 expect(evaluateShadowCandidate(c,evidence,[{...outcomes[0],label:"ABSTAIN"}],scores)).toMatchObject({status:"ABSTAIN",reason:"source_outcome_gap",production_promoted:false});
 expect(evaluateShadowCandidate(c,evidence,[...outcomes,...outcomes],scores).status).toBe("ABSTAIN");
 expect(evaluateShadowCandidate(c,evidence,[{...outcomes[0],source_sha:"c".repeat(64)}],scores).status).toBe("ABSTAIN");
 expect(evaluateShadowCandidate(c,{...evidence,qualified:false},[],scores).status).toBe("ABSTAIN");
});

test("shadow coverage distinguishes matured, pending and abstained without changing baseline",async()=>{
 const r=createCycleRunner(deps,async()=>({evidence,outcomes:[],scores}));
 const result=(await r.run("manual")).result;
 expect(result.shadow_evaluation.coverage).toEqual({candidates:1,scored:0,pending_outcome:1,abstained:0,authenticated_outcomes:0,source_qualified:true});
 expect(result.candidates[0].score).toBe(85);
 const fail=createCycleRunner(deps,async()=>{throw Error("unavailable")});
 const failed=(await fail.run("manual")).result;
 expect(failed.shadow_evaluation.coverage).toMatchObject({candidates:1,scored:0,pending_outcome:0,abstained:1,authenticated_outcomes:0,source_qualified:false});
});

test("B2 source-qualified outcomes and pre-discovery scores join across equivalent UTC timestamp formats",()=>{
 const c={pair:"TAOUSD",score:85,discovered_at:"2026-11-03T03:59:00.000+00:00",decision:"WATCH"};
 const result=evaluateShadowCandidate(c,evidence,outcomes,scores);
 expect(result).toMatchObject({status:"SCORED",outcome_label:"HIT",challenger_score:89,baseline_score:85,production_promoted:false});
});
