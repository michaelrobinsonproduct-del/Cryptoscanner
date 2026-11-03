import {test,expect} from "bun:test";
import {createCycleRunner} from "./cycle-runner";
import {createCycleHttpHandler} from "./cycle-http";
import {createPaperReceiptReader,parsePaperReceipt} from "./paper-receipt";
const now=new Date("2026-11-03T08:00:00Z"),asOf="2026-11-03T07:59:00Z";
const receipt={schema:1,mode:"PAPER_ONLY",buy_approved:false,scan_status:"WATCH",as_of:asOf,observed_markets:596,ohlc_screened:10,watch:[{pair:"TAOUSD"}],abstentions:[{pair:"ETHUSD"}]};
const deps={scan:async()=>({candidates:[]}),confirm:async()=>{throw Error("not called")},pause:async()=>{},now:()=>now};
test("real manual HTTP and scheduled paths read same Owner A receipt, retain independent scan status and no BUY",async()=>{
 let reads=0;const reader=createPaperReceiptReader("https://example.org/paper/latest.json",()=>now,async(_url,options)=>{reads++;expect(options?.method).toBe("GET");expect(options?.redirect).toBe("error");return new Response(JSON.stringify(receipt))} as any);
 const runner=createCycleRunner(deps,undefined,reader),http=createCycleHttpHandler(runner);
 const manual=await (await http(new Request("http://localhost/cycle"))).json(),scheduled=await runner.run("scheduled");
 expect(manual).toEqual(scheduled.result);expect(reads).toBe(2);
 expect(manual.scan_status).toBe("NO_DISCOVERY_CANDIDATES");
 expect(manual.paper_receipt).toEqual({status:"VERIFIED_RECEIPT",scan_status:"WATCH",as_of:asOf,watch_count:1,observed_markets:596,ohlc_screened:10,abstention_count:1,source:"paper_pov",buy_approved:false});
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
