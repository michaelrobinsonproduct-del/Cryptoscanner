import {test,expect} from "bun:test";
import {createCycleRunner} from "./cycle-runner";
import {createCycleHttpHandler} from "./cycle-http";
import {createPaperReceiptReader,parsePaperReceipt,parseSealedPaperBundle} from "./paper-receipt";
const now=new Date("2026-11-03T08:00:00Z"),asOf="2026-11-03T07:59:00Z";
const receipt={schema:1,mode:"PAPER_ONLY",buy_approved:false,scan_status:"WATCH",as_of:asOf,observed_markets:596,eligible_pairs:604,ticker_rejections:{missing_or_invalid_payload:5,invalid_price_or_volume:2,nonfinite_derived_metric:1},ohlc_screened:10,watch:[{pair:"TAOUSD"}],abstentions:[{pair:"ETHUSD"}]};
const deps={scan:async()=>({candidates:[]}),confirm:async()=>{throw Error("not called")},pause:async()=>{},now:()=>now};
test("real manual HTTP and scheduled paths read same Owner A receipt, retain independent scan status and no BUY",async()=>{
 let reads=0;const reader=createPaperReceiptReader("https://example.org/paper/latest.json",()=>now,(async(_url,options)=>{reads++;expect(options?.method).toBe("GET");expect(options?.redirect).toBe("error");return new Response(JSON.stringify(receipt))}) as any);
 const runner=createCycleRunner(deps,undefined,reader),http=createCycleHttpHandler(runner);
 const manual=await (await http(new Request("http://localhost/cycle"))).json(),scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);expect(reads).toBe(2);
 expect(manual.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
 expect(manual.paper_receipt).toMatchObject({status:"UNAVAILABLE",reason:"read_or_validation_failed",watch_count:null});
 expect((await (await http(new Request("http://localhost/dashboard"))).json()).last_result.paper_receipt).toEqual(manual.paper_receipt);
});
test("stale, inconsistent or untrusted paper receipts never invent zero WATCH",async()=>{
 expect(()=>parsePaperReceipt({...receipt,as_of:"2026-11-03T07:30:00Z"},now)).toThrow("stale_paper_receipt");
 expect(()=>parsePaperReceipt({...receipt,scan_status:"ABSTAIN_NO_LIQUID_CANDIDATES"},now)).toThrow("inconsistent_paper_status");
 const runner=createCycleRunner(deps,undefined,createPaperReceiptReader("https://example.org/receipt",()=>now,async()=>new Response(JSON.stringify({...receipt,watch:[]})) as any));
 const result=await runner.run("manual");
 expect(result.ok).toBe(true);expect(result.result.paper_receipt).toMatchObject({status:"UNAVAILABLE",watch_count:null,reason:"read_or_validation_failed"});
 expect(result.result.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
});
test("missing receipt URL and unsafe endpoint are fail-closed and never write",async()=>{
 const missing=await createPaperReceiptReader(undefined,()=>now)();
 expect(missing).toMatchObject({status:"UNAVAILABLE",watch_count:null,reason:"not_configured"});
 await expect(createPaperReceiptReader("http://example.org",()=>now)()).rejects.toThrow("unsafe_paper_receipt_url");
});

test("Owner A ticker coverage must reconcile and is visible in both HTTP paths",async()=>{
 const bad={...receipt,eligible_pairs:605};
 expect(()=>parsePaperReceipt(bad,now)).toThrow("inconsistent_ticker_coverage");
 expect(()=>parsePaperReceipt({...receipt,ticker_rejections:{...receipt.ticker_rejections,invalid_price_or_volume:-1}},now)).toThrow("inconsistent_ticker_coverage");
 const reader=createPaperReceiptReader("https://example.org/receipt",()=>now,async()=>new Response(JSON.stringify(receipt)) as any);
 const runner=createCycleRunner(deps,undefined,reader),http=createCycleHttpHandler(runner);
 const manual=await (await http(new Request("http://localhost/cycle"))).json();
 const scheduled=await runner.run("scheduled");
 expect(manual.paper_receipt).toEqual(scheduled.result.paper_receipt);
 expect(manual.paper_receipt.eligible_pairs).toBeNull();
 expect(manual.paper_receipt.reason).toBe("read_or_validation_failed");
});

test("sealed HTTP bundle binds raw immutable receipt and both projections",async()=>{
 const report={...receipt,observed_markets:1,eligible_pairs:9,preselection_universe:[{pair:"TAOUSD"}],preselection_decisions:{WATCH:1}};
 const raw=JSON.stringify(report);
 const digest=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",new TextEncoder().encode(raw)))).map(x=>x.toString(16).padStart(2,"0")).join("");
 const bundle={schema:"paper_sealed_bundle_v1",receipt_json:raw,candidate_snapshot:{receipt_sha256:digest,as_of:asOf,scan_status:"WATCH",watch:report.watch},preselection_universe:{receipt_sha256:digest,as_of:asOf,markets:report.preselection_universe,selection_decisions:report.preselection_decisions,future_outcomes_authenticated:false,qualified_for_learning:false,production_applied:false}};
 const result=await parseSealedPaperBundle(bundle,now);
 expect(result).toMatchObject({status:"VERIFIED_RECEIPT",receipt_sha256:digest,watch_count:1,preselection:[{pair:"TAOUSD"}]});
 await expect(parseSealedPaperBundle({...bundle,candidate_snapshot:{...bundle.candidate_snapshot,receipt_sha256:"0".repeat(64)}},now)).rejects.toThrow("paper_bundle_receipt_mismatch");
 await expect(parseSealedPaperBundle({...bundle,preselection_universe:{...bundle.preselection_universe,markets:[]}},now)).rejects.toThrow("paper_bundle_projection_mismatch");
});
