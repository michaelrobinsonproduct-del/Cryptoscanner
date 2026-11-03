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
  const comparison=report.comparison;
  if(!decision||decision.decision!=="KEEP_BASELINE"||decision.production_applied!==false||!comparison||comparison.held_out_n!==0)throw Error("learning_report_not_baseline");
  return {decision:"KEEP_BASELINE",held_out_n:0,production_applied:false as const};
 };
}
