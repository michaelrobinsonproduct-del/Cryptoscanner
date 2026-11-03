import {test,expect} from "bun:test";
import {createReadOnlyShadowLoader} from "./shadow-artifacts";
import {createCycleRunner} from "./cycle-runner";
import {createCycleHttpHandler} from "./cycle-http";
const source="a".repeat(64),ledger="b".repeat(64),at="2026-11-03T04:00:00Z",discovered="2026-11-03T03:59:00Z";
const evidence={version:"v2",source_sha:source,outcome_ledger_sha:ledger,qualified:true,held_out_samples:42,held_out_lift:4,outcome_rows:1};
const outcomes=[{pair:"TAOUSD",observed_at:discovered,label:"HIT",source_sha:source}];
const digest=async(value:unknown)=>Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",new TextEncoder().encode(JSON.stringify(value))))).map(x=>x.toString(16).padStart(2,"0")).join("");
const quote={pair:"TAOUSD",success:true,twoSidedBook:true,executableBbo:true,recentTradeConfirmation:true,newestTradeAgeSeconds:5,bestAsk:100,bestBid:99,fetchedAt:"2026-11-03T03:59:30Z"};
const deps={scan:async()=>({candidates:[{pair:"TAOUSD",score:85,displacement_pct:1,discovered_at:discovered}]}),confirm:async()=>quote,pause:async()=>{},now:()=>new Date(at)};
test("HTTP manual and scheduled both load read-only outcome artifacts and shadow-score without promotion",async()=>{
 let gets=0;
 const verifiedEvidence={...evidence,outcome_ledger_sha:await digest(outcomes)};
 const fetcher=async(_url:any,opts:any)=>{gets++;expect(opts.method).toBe("GET");expect(opts.redirect).toBe("error");return new Response(JSON.stringify({evidence:verifiedEvidence,outcomes}),{status:200})};
 const runner=createCycleRunner(deps,createReadOnlyShadowLoader("https://example.org/ledger.json",fetcher as any));
 const manual=await (await createCycleHttpHandler(runner)(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);expect(gets).toBe(2);
 expect(manual.shadow_evaluation.candidates[0]).toMatchObject({status:"SCORED",challenger_score:89,production_promoted:false});
});
test("missing artifact URL and malformed or count-mismatched evidence abstain, baseline stays intact",async()=>{
 const missing=createCycleRunner(deps,createReadOnlyShadowLoader(undefined));
 const r=await missing.run("manual");expect(r.result.candidates).toHaveLength(1);
 expect(r.result.shadow_evaluation.candidates[0].status).toBe("ABSTAIN");
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
