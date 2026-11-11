/** Read-only E2/E3 research report; never authorize production promotion. */
export function createLearningReportReader(path:string|undefined,expectedSha:string|undefined,read:(path:string)=>Promise<Uint8Array>=p=>Bun.file(p).bytes()){
 return async()=>{
  if(!path||!expectedSha||!/^[a-f0-9]{64}$/i.test(expectedSha)||!path.startsWith("/")||path.includes("\0"))throw Error("missing_trusted_learning_report");
  const bytes=await read(path);
  if(bytes.byteLength>2_000_000)throw Error("oversized_learning_report");
  const digest=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes))).map(v=>v.toString(16).padStart(2,"0")).join("");
  if(digest!==expectedSha.toLowerCase())throw Error("learning_report_digest_mismatch");
  const report=JSON.parse(new TextDecoder("utf-8",{fatal:true}).decode(bytes));
  if(!report||typeof report!=="object"||report.production_applied!==false)throw Error("invalid_learning_report");
  const decision=report.shadow_decision;
  if(!decision||decision.decision!=="KEEP_BASELINE"||decision.production_applied!==false)throw Error("learning_report_not_baseline");
  // E's actual authenticated paper bridge emits per-horizon coverage, not a
  // synthetic comparison. Never convert descriptive labels into learning uplift.
  if(report.mode==="REAL_PAPER_DESCRIPTIVE_NOT_AUTHENTICATED_DEPTH"){
   if(!Number.isSafeInteger(report.paper_predictions)||report.paper_predictions<=0||
      !Number.isSafeInteger(report.paper_observations)||report.paper_observations<=0||
      !/^[a-f0-9]{64}$/.test(report.ledger_sha256)||!report.horizons||
      [1,6,24,48].some(h=>{
       const row=report.horizons[String(h)];
       return !row||row.held_out_n!==0||row.authenticated_entry_labels!==0||
         row.rule!=="NO QUALIFIED RULE"||!Number.isSafeInteger(row.paper_outcomes)||row.paper_outcomes<0;
      }))throw Error("unqualified_learning_horizon");
  }else if(!report.comparison||report.comparison.held_out_n!==0){
   throw Error("learning_report_not_baseline");
  }
  return {decision:"KEEP_BASELINE",held_out_n:0,production_applied:false as const};
 };
}
