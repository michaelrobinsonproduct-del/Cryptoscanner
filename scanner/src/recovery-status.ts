/** Read-only D2 persisted recovery consumer outcome. Never turns historical evidence into live quote certification. */
export type RecoveryStatus={status:"VERIFIED_READBACK"|"RECOVERY_CONSUMER_FAILED"|"UNAVAILABLE";workflow_run_id:string|null;workflow_sha:string|null;production_applied:false;reason?:string};
export const unavailableRecovery=(reason:string):RecoveryStatus=>({status:"UNAVAILABLE",workflow_run_id:null,workflow_sha:null,production_applied:false,reason});
export function createRecoveryStatusReader(path:string|undefined,expectedSha:string|undefined,read:(path:string)=>Promise<Uint8Array>=p=>Bun.file(p).bytes()):()=>Promise<RecoveryStatus>{
 return async()=>{
  if(!path||!path.startsWith("/")||path.includes("\0")||!expectedSha||!/^[a-f0-9]{64}$/i.test(expectedSha))throw Error("untrusted_recovery_status_source");
  const bytes=await read(path);
  if(bytes.byteLength>10000)throw Error("oversized_recovery_status");
  const digest=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes))).map(v=>v.toString(16).padStart(2,"0")).join("");
  if(digest!==expectedSha.toLowerCase())throw Error("recovery_status_digest_mismatch");
  const x=JSON.parse(new TextDecoder("utf-8",{fatal:true}).decode(bytes));
  if(x?.schema!=="paper_recovery_consumer_v1"||x.production_applied!==false||
    !/^[0-9]+$/.test(String(x.workflow_run_id))||!/^[a-f0-9]{40}$/i.test(String(x.workflow_sha))||
    !["success","failure","cancelled","skipped"].includes(x.download_outcome)||
    !["success","failure","cancelled","skipped"].includes(x.consume_outcome)||
    !["VERIFIED_READBACK","RECOVERY_CONSUMER_FAILED"].includes(x.status)||
    (x.status==="VERIFIED_READBACK")!==(x.download_outcome==="success"&&x.consume_outcome==="success"))throw Error("invalid_recovery_status");
  return {status:x.status,workflow_run_id:String(x.workflow_run_id),workflow_sha:x.workflow_sha,production_applied:false};
 };
}
