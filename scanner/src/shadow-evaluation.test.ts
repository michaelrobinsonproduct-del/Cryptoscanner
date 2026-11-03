import {test,expect} from "bun:test";
import {createCycleRunner} from "./cycle-runner";
import {evaluateShadowCandidate} from "./shadow-evaluation";
const stamp="2026-11-03T04:00:00Z",discovered="2026-11-03T03:59:00Z",source="a".repeat(64),ledger="b".repeat(64);
const row={pair:"TAOUSD",score:85,displacement_pct:1,discovered_at:discovered};
const quote={pair:"TAOUSD",success:true,twoSidedBook:true,executableBbo:true,recentTradeConfirmation:true,newestTradeAgeSeconds:5,bestAsk:100,bestBid:99,fetchedAt:"2026-11-03T03:59:30Z"};
const deps={scan:async()=>({candidates:[row]}),confirm:async()=>quote,pause:async()=>{},now:()=>new Date(stamp)};
const evidence={version:"challenger-v2",source_sha:source,outcome_ledger_sha:ledger,qualified:true,held_out_samples:42,held_out_lift:4,outcome_rows:1};
const outcomes=[{pair:"TAOUSD",observed_at:discovered,label:"HIT" as const,source_sha:source}];
test("manual and scheduled cycles attach same qualified versioned shadow result without changing baseline",async()=>{
 const r=createCycleRunner(deps,async()=>({evidence,outcomes}));
 const manual=await r.run("manual"),scheduled=await r.run("scheduled");
 expect(manual.ok).toBe(true);expect(manual.result).toEqual(scheduled.result);
 expect(manual.result.shadow_evaluation.candidates[0]).toMatchObject({status:"SCORED",baseline_score:85,challenger_score:89,outcome_label:"HIT",production_promoted:false});
 expect(manual.result.candidates[0]).toEqual(scheduled.result.candidates[0]);
});
test("unqualified or ambiguous ledger abstains without scoring",async()=>{
 const c={pair:"TAOUSD",score:85,discovered_at:discovered,decision:"WATCH"};
 expect(evaluateShadowCandidate(c,{...evidence,qualified:false},outcomes).status).toBe("ABSTAIN");
 expect(evaluateShadowCandidate(c,evidence,[...outcomes,...outcomes]).reason).toBe("missing_or_ambiguous_outcome");
 expect(evaluateShadowCandidate(c,evidence,[{...outcomes[0],source_sha:"c".repeat(64)}]).status).toBe("ABSTAIN");
});
test("ledger failure leaves baseline cycle working but records shadow abstention",async()=>{
 const r=createCycleRunner(deps,async()=>{throw Error("ledger unavailable")});
 const run=await r.run("manual");
 expect(run.ok).toBe(true);expect(run.result.candidates).toHaveLength(1);
 expect(run.result.shadow_evaluation.candidates[0]).toMatchObject({status:"ABSTAIN",reason:"unqualified_challenger",production_promoted:false});
});
