import type {ShadowEvidence,ShadowOutcome} from "./shadow-evaluation";
export type ShadowArtifacts={evidence:ShadowEvidence|null;outcomes:ShadowOutcome[]};
const sha=(v:unknown)=>typeof v==="string"&&/^[a-f0-9]{64}$/i.test(v);
export function parseShadowArtifacts(raw:unknown):ShadowArtifacts{
 if(!raw||typeof raw!=="object")throw Error("invalid_shadow_artifact");
 const a=raw as Record<string,unknown>,e=a.evidence as Record<string,unknown>|null,o=a.outcomes;
 if(!e||typeof e!=="object"||!Array.isArray(o))throw Error("missing_shadow_evidence");
 if(typeof e.version!=="string"||!/^[-.a-zA-Z0-9_]{1,64}$/.test(e.version)||!sha(e.source_sha)||!sha(e.outcome_ledger_sha)||typeof e.qualified!=="boolean"||!Number.isInteger(e.held_out_samples)||!Number.isInteger(e.outcome_rows)||!(e.held_out_lift===null||typeof e.held_out_lift==="number"&&Number.isFinite(e.held_out_lift)))throw Error("invalid_shadow_evidence");
 if(o.length!==e.outcome_rows||o.length>10000)throw Error("shadow_ledger_count_mismatch");
 const outcomes:ShadowOutcome[]=o.map((v:unknown)=>{
  if(!v||typeof v!=="object")throw Error("invalid_outcome");
  const x=v as Record<string,unknown>;
  if(typeof x.pair!=="string"||!/^[A-Z0-9]{3,24}$/.test(x.pair)||typeof x.observed_at!=="string"||!Number.isFinite(Date.parse(x.observed_at))||!["HIT","MISS","ABSTAIN"].includes(String(x.label))||!sha(x.source_sha))throw Error("invalid_outcome");
  return {pair:x.pair,observed_at:x.observed_at,label:x.label as ShadowOutcome["label"],source_sha:x.source_sha as string};
 });
 return {evidence:e as unknown as ShadowEvidence,outcomes};
}
export function createReadOnlyShadowLoader(url:string|undefined,fetcher:typeof fetch=fetch):()=>Promise<ShadowArtifacts>{
 return async()=>{
  if(!url)return {evidence:null,outcomes:[]};
  const u=new URL(url);
  if(u.protocol!=="https:"||u.username||u.password||u.hash)throw Error("unsafe_shadow_artifact_url");
  const response=await fetcher(u.toString(),{method:"GET",redirect:"error",signal:AbortSignal.timeout(8000),headers:{accept:"application/json"}});
  if(!response.ok)throw Error(`shadow_artifact_http_${response.status}`);
  const text=await response.text();
  if(text.length>2000000)throw Error("shadow_artifact_too_large");
  return parseShadowArtifacts(JSON.parse(text));
 };
}
