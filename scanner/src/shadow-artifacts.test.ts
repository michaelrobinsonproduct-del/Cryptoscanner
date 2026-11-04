import {createLearningReportReader} from "./learning-report";
import {test,expect} from "bun:test";
import {createReadOnlyShadowLoader} from "./shadow-artifacts";
import {createCycleRunner} from "./cycle-runner";
import {createCycleHttpHandler} from "./cycle-http";
const source="a".repeat(64),ledger="b".repeat(64),at="2026-11-03T04:00:00Z",discovered="2026-11-03T03:59:00Z";
const evidence={version:"v2",source_sha:source,outcome_ledger_sha:ledger,score_ledger_sha:ledger,qualified:true,held_out_samples:42,held_out_lift:4,outcome_rows:1};
const scores=[{pair:"TAOUSD",observed_at:discovered,computed_at:"2026-11-03T03:58:00Z",version:"v2",score:89,source_sha:source}];
const outcomes=[{pair:"TAOUSD",observed_at:discovered,label:"HIT",source_sha:source}];
const digest=async(value:unknown)=>Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",new TextEncoder().encode(JSON.stringify(value))))).map(x=>x.toString(16).padStart(2,"0")).join("");
const comparison={held_out_n:42,held_out_lift:4,paper_predictions_examined:42,excluded:{}};
const researchDigest=await digest(comparison);
const researchGate={comparison,shadow_decision:{decision:"SHADOW_ELIGIBLE_REVIEW",challenger_version:"v2",evidence_sha256:researchDigest,production_applied:false,held_out_n:42,held_out_lift:4,active_shadow_version:"v2"}};
const gateUrl="https://example.org/research.json";
const quote={pair:"TAOUSD",success:true,twoSidedBook:true,executableBbo:true,recentTradeConfirmation:true,newestTradeAgeSeconds:5,bestAsk:100,bestBid:99,fetchedAt:"2026-11-03T03:59:30Z"};
const deps={scan:async()=>({candidates:[{pair:"TAOUSD",score:85,displacement_pct:1,discovered_at:discovered}]}),confirm:async()=>quote,pause:async()=>{},now:()=>new Date(at)};
test("HTTP manual and scheduled both load read-only outcome artifacts and shadow-score without promotion",async()=>{
 let gets=0;
 const verifiedEvidence={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const fetcher=async(url:any,opts:any)=>{gets++;expect(opts.method).toBe("GET");expect(opts.redirect).toBe("error");return new Response(JSON.stringify(url===gateUrl?researchGate:{evidence:verifiedEvidence,outcomes,scores}),{status:200})};
 const runner=createCycleRunner(deps,createReadOnlyShadowLoader("https://example.org/ledger.json",fetcher as any,source,gateUrl,researchDigest),undefined,undefined,async()=>({decision:"SHADOW_ELIGIBLE_REVIEW",held_out_n:42,production_applied:false as const}));
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);expect(gets).toBe(4);
 expect(manual.shadow_artifact_status).toBe("VERIFIED");
 expect(manual.shadow_evaluation.candidates[0]).toMatchObject({status:"SCORED",challenger_score:89,production_promoted:false});
});
test("missing artifact URL and malformed or count-mismatched evidence abstain, baseline stays intact",async()=>{
 const missing=createCycleRunner(deps,createReadOnlyShadowLoader(undefined));
 const r=await missing.run("manual");expect(r.result.candidates).toHaveLength(1);
 expect(r.result.shadow_evaluation.candidates[0].status).toBe("ABSTAIN");expect(r.result.shadow_artifact_status).toBe("REJECTED");
 const bad=createReadOnlyShadowLoader("https://example.org/ledger.json",async()=>new Response(JSON.stringify({evidence:{...evidence,outcome_rows:2},outcomes})) as any);
 await expect(bad()).rejects.toThrow("shadow_ledger_count_mismatch");
});
test("remote redirects, invalid URLs and HTTP errors fail closed without second writer",async()=>{
 const redirect=createReadOnlyShadowLoader("https://example.org/ledger.json",async()=>new Response("",{status:302}) as any);
 await expect(redirect()).rejects.toThrow("shadow_artifact_http_302");
 await expect(createReadOnlyShadowLoader("http://example.org/ledger.json")()).rejects.toThrow("unsafe_shadow_artifact_url");
});

test("tampered ledger digest is rejected before challenger scoring",async()=>{
 const loader=createReadOnlyShadowLoader("https://example.org/ledger.json",async()=>new Response(JSON.stringify({evidence,outcomes})) as any);
 await expect(loader()).rejects.toThrow("shadow_ledger_digest_mismatch");
});

test("self-consistent but untrusted source and missing challenger scores cannot score",async()=>{
 const verified={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const response=async()=>new Response(JSON.stringify({evidence:verified,outcomes,scores})) as any;
 await expect(createReadOnlyShadowLoader("https://example.org/ledger.json",response,"c".repeat(64))()).rejects.toThrow("untrusted_shadow_source");
 const empty={...verified,score_ledger_sha:await digest([])};
 const loader=createReadOnlyShadowLoader("https://example.org/ledger.json",async(url:any)=>new Response(JSON.stringify(url===gateUrl?researchGate:{evidence:empty,outcomes,scores:[]})) as any,source,gateUrl,researchDigest);
 const runner=createCycleRunner(deps,loader,undefined,undefined,async()=>({decision:"SHADOW_ELIGIBLE_REVIEW",held_out_n:42,production_applied:false as const}));const result=await runner.run("manual");
 expect(result.result.shadow_evaluation.candidates[0].reason).toBe("missing_or_leaky_challenger_score");
});

test("score ledger tampering, duplicate and future-derived scores fail closed",async()=>{
 const valid={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const load=(s:unknown[],e:unknown=valid)=>createReadOnlyShadowLoader("https://example.org/ledger.json",async()=>new Response(JSON.stringify({evidence:e,outcomes,scores:s})) as any,source)();
 await expect(load([{...scores[0],score:99}])).rejects.toThrow("shadow_score_digest_mismatch");
 await expect(load([...scores,...scores])).rejects.toThrow("duplicate_shadow_score");
 await expect(load([{...scores[0],computed_at:"2026-11-03T04:01:00Z"}])).rejects.toThrow("untrusted_or_leaky_shadow_score");
 await expect(load([{...scores[0],source_sha:"c".repeat(64)}])).rejects.toThrow("untrusted_or_leaky_shadow_score");
});

test("corrupt authenticated ledger is visibly rejected by both manual and scheduled entry, preserving baseline",async()=>{
 const loader=createReadOnlyShadowLoader("https://example.org/ledger.json",async()=>new Response(JSON.stringify({evidence,outcomes,scores})) as any,source);
 const runner=createCycleRunner(deps,loader);
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.shadow_artifact_status).toBe("REJECTED");
 expect(manual.candidates).toHaveLength(1);
 expect(manual.shadow_evaluation.coverage).toMatchObject({scored:0,abstained:1});
});

test("independent E3 decision gate rejects KEEP_BASELINE and source mismatch before shadow scoring",async()=>{
 const verified={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const loader=(gate:unknown)=>createReadOnlyShadowLoader("https://example.org/ledger.json",async(url:any)=>new Response(JSON.stringify(url===gateUrl?gate:{evidence:verified,outcomes,scores})) as any,source,gateUrl,researchDigest);
 await expect(loader({...researchGate,shadow_decision:{...researchGate.shadow_decision,decision:"KEEP_BASELINE"}})()).rejects.toThrow("research_gate_not_qualified");
 await expect(loader({...researchGate,shadow_decision:{...researchGate.shadow_decision,evidence_sha256:"c".repeat(64)}})()).rejects.toThrow("unqualified_research_gate");
 const runner=createCycleRunner(deps,loader({...researchGate,shadow_decision:{...researchGate.shadow_decision,decision:"KEEP_BASELINE"}}));
 const result=await runner.run("manual");
 expect(result.result.shadow_artifact_status).toBe("REJECTED");
 expect(result.result.shadow_evaluation.coverage).toMatchObject({scored:0,abstained:1});
 expect(result.result.candidates).toHaveLength(1);
});

test("missing research pin and missing independent gate fail closed across shared HTTP and scheduled entry",async()=>{
 const verified={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const fetcher=async(url:any)=>new Response(JSON.stringify(url===gateUrl?researchGate:{evidence:verified,outcomes,scores})) as any;
 const missingPin=createCycleRunner(deps,createReadOnlyShadowLoader("https://example.org/ledger.json",fetcher as any,source,gateUrl));
 const missingGate=createCycleRunner(deps,createReadOnlyShadowLoader("https://example.org/ledger.json",fetcher as any,source));
 for(const runner of [missingPin,missingGate]){
  const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
  const scheduled=await runner.run("scheduled");
  expect(manual).toEqual(scheduled.result);
  expect(manual.shadow_artifact_status).toBe("REJECTED");
  expect(manual.candidates).toHaveLength(1);
  expect(manual.shadow_evaluation.coverage).toMatchObject({scored:0,abstained:1});
 }
});

test("research comparison cannot claim more excluded plus held-out predictions than examined",async()=>{
 const verified={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const impossible={...researchGate,comparison:{...researchGate.comparison,excluded:{stale:1}}};
 const loader=createReadOnlyShadowLoader("https://example.org/ledger.json",async(url:any)=>new Response(JSON.stringify(url===gateUrl?impossible:{evidence:verified,outcomes,scores})) as any,source,gateUrl,researchDigest);
 await expect(loader()).rejects.toThrow("unqualified_research_gate");
 const runner=createCycleRunner(deps,loader);
 const result=await runner.run("manual");
 expect(result.result.shadow_artifact_status).toBe("REJECTED");
 expect(result.result.candidates).toHaveLength(1);
 expect(result.result.shadow_evaluation.coverage).toMatchObject({scored:0,abstained:1});
});

test("outcome source substitution and equivalent-timestamp duplicate identities abstain without baseline impact",async()=>{
 const verified={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const badSource=[{...outcomes[0],source_sha:"c".repeat(64)}];
 const duplicates=[outcomes[0],{...outcomes[0],observed_at:"2026-11-03T03:59:00.000Z"}];
 const build=(rows:unknown[])=>createReadOnlyShadowLoader("https://example.org/ledger.json",async()=>new Response(JSON.stringify({evidence:{...verified,outcome_rows:rows.length},outcomes:rows,scores})) as any,source);
 await expect(build(badSource)()).rejects.toThrow("untrusted_shadow_outcome");
 await expect(build(duplicates)()).rejects.toThrow("duplicate_shadow_outcome");
 const runner=createCycleRunner(deps,build(badSource));
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.candidates).toHaveLength(1);
 expect(manual.shadow_artifact_status).toBe("REJECTED");
 expect(manual.shadow_evaluation.coverage).toMatchObject({scored:0,abstained:1});
});
test("score duplicate identities normalize timestamp precision and malformed pairs are rejected",async()=>{
 const verified={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const load=(rows:unknown[])=>createReadOnlyShadowLoader("https://example.org/ledger.json",async()=>new Response(JSON.stringify({evidence:verified,outcomes,scores:rows})) as any,source)();
 await expect(load([scores[0],{...scores[0],observed_at:"2026-11-03T03:59:00.000Z"}])).rejects.toThrow("duplicate_shadow_score");
 await expect(load([{...scores[0],pair:"../BAD"}])).rejects.toThrow("untrusted_or_leaky_shadow_score");
});

test("tampered comparison with unchanged trusted digest is rejected before manual and scheduled shadow scoring",async()=>{
 const verified={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const altered={...researchGate,comparison:{...comparison,held_out_lift:5},shadow_decision:{...researchGate.shadow_decision,held_out_lift:5}};
 const loader=createReadOnlyShadowLoader("https://example.org/ledger.json",async(url:any)=>new Response(JSON.stringify(url===gateUrl?altered:{evidence:verified,outcomes,scores})) as any,source,gateUrl,researchDigest);
 await expect(loader()).rejects.toThrow("research_gate_content_digest_mismatch");
 const runner=createCycleRunner(deps,loader);
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.shadow_artifact_status).toBe("REJECTED");
 expect(manual.candidates).toHaveLength(1);
 expect(manual.shadow_evaluation.coverage).toMatchObject({scored:0,abstained:1});
});

// A self-consistent digest must not override impossible cohort accounting.
test("rehashing an impossible cohort cannot bypass held-out accounting and both entry points abstain",async()=>{
 const verified={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(scores)};
 const impossible={...comparison,excluded:{late:1}};
 const pinned=await digest(impossible);
 const gate={comparison:impossible,shadow_decision:{...researchGate.shadow_decision,evidence_sha256:pinned}};
 const loader=createReadOnlyShadowLoader("https://example.org/ledger.json",async(url:any)=>new Response(JSON.stringify(url===gateUrl?gate:{evidence:verified,outcomes,scores})) as any,source,gateUrl,pinned);
 await expect(loader()).rejects.toThrow("unqualified_research_gate");
 const runner=createCycleRunner(deps,loader);
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.shadow_artifact_status).toBe("REJECTED");
 expect(manual.candidates).toHaveLength(1);
 expect(manual.shadow_evaluation.coverage).toMatchObject({scored:0,abstained:1});
});

test("authenticated equivalent-instant timestamps score identically across manual HTTP and scheduled paths",async()=>{
 const alternateScores=[{...scores[0],observed_at:"2026-11-02T22:59:00-05:00"}];
 const alternateOutcomes=[{...outcomes[0],observed_at:"2026-11-03T03:59:00.000Z"}];
 const verified={...evidence,outcome_ledger_sha:await digest(alternateOutcomes),score_ledger_sha:await digest(alternateScores)};
 const loader=createReadOnlyShadowLoader("https://example.org/ledger.json",async(url:any)=>new Response(JSON.stringify(url===gateUrl?researchGate:{evidence:verified,outcomes:alternateOutcomes,scores:alternateScores})) as any,source,gateUrl,researchDigest);
 const runner=createCycleRunner(deps,loader,undefined,undefined,async()=>({decision:"SHADOW_ELIGIBLE_REVIEW",held_out_n:42,production_applied:false as const}));
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.shadow_artifact_status).toBe("VERIFIED");
 expect(manual.shadow_evaluation.coverage).toMatchObject({scored:1,abstained:0});
 expect(manual.shadow_evaluation.candidates[0]).toMatchObject({status:"SCORED",challenger_score:89,outcome_label:"HIT",production_promoted:false});
});
test("equivalent-instant scores remain subject to pre-discovery leakage rejection",async()=>{
 const altered=[{...scores[0],observed_at:"2026-11-02T22:59:00-05:00",computed_at:"2026-11-03T04:00:00Z"}];
 const verified={...evidence,outcome_ledger_sha:await digest(outcomes),score_ledger_sha:await digest(altered)};
 const loader=createReadOnlyShadowLoader("https://example.org/ledger.json",async(url:any)=>new Response(JSON.stringify(url===gateUrl?researchGate:{evidence:verified,outcomes,scores:altered})) as any,source,gateUrl,researchDigest);
 const runner=createCycleRunner(deps,loader);
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.shadow_artifact_status).toBe("REJECTED");
 expect(manual.candidates).toHaveLength(1);
 expect(manual.shadow_evaluation.coverage).toMatchObject({scored:0,abstained:1});
});

test("B2 authenticated E KEEP_BASELINE is identical on manual HTTP and scheduled with no promotion",async()=>{
 const raw=new TextEncoder().encode(JSON.stringify({mode:"REAL_PAPER_DESCRIPTIVE_NOT_AUTHENTICATED_DEPTH",ledger_sha256:"a".repeat(64),paper_predictions:357,paper_observations:22272,production_applied:false,horizons:Object.fromEntries([1,6,24,48].map(h=>[h,{paper_outcomes:0,held_out_n:0,authenticated_entry_labels:0,rule:"NO QUALIFIED RULE"}])),shadow_decision:{decision:"KEEP_BASELINE",held_out_n:0,production_applied:false}}));
 const sha=await crypto.subtle.digest("SHA-256",raw);
 const pin=Array.from(new Uint8Array(sha)).map(x=>x.toString(16).padStart(2,"0")).join("");
 const loader=createLearningReportReader("/read-only/e-report.json",pin,async()=>raw);
 const runner=createCycleRunner(deps,undefined,undefined,undefined,loader);
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);
 expect(manual.learning_gate).toEqual({status:"VERIFIED_RESEARCH_ONLY",decision:"KEEP_BASELINE",held_out_n:0,production_applied:false});
 expect(manual.candidates).toHaveLength(1);
 const corrupted=createCycleRunner(deps,undefined,undefined,undefined,createLearningReportReader("/read-only/e-report.json",pin,async()=>new TextEncoder().encode("{}")));
 const failed=await corrupted.run("manual");
 expect(failed.result.learning_gate).toMatchObject({status:"REJECTED",decision:"KEEP_BASELINE",production_applied:false});
 expect(failed.result.candidates).toHaveLength(1);
});
