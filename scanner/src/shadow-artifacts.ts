import type {ShadowEvidence,ShadowOutcome,ShadowScore} from "./shadow-evaluation";
export type ShadowArtifacts={evidence:ShadowEvidence|null;outcomes:ShadowOutcome[];scores:ShadowScore[]};
const sha=(v:unknown)=>typeof v==="string"&&/^[a-f0-9]{64}$/i.test(v);
export function parseShadowArtifacts(raw:unknown):ShadowArtifacts{
 if(!raw||typeof raw!=="object")throw Error("invalid_shadow_artifact");
 const a=raw as Record<string,unknown>,e=a.evidence as Record<string,unknown>|null,o=a.outcomes,s=a.scores??[];
 if(!e||typeof e!=="object"||!Array.isArray(o))throw Error("missing_shadow_evidence");
 if(typeof e.version!=="string"||!/^[-.a-zA-Z0-9_]{1,64}$/.test(e.version)||!sha(e.source_sha)||!sha(e.outcome_ledger_sha)||typeof e.qualified!=="boolean"||!Number.isInteger(e.held_out_samples)||!Number.isInteger(e.outcome_rows)||!(e.held_out_lift===null||typeof e.held_out_lift==="number"&&Number.isFinite(e.held_out_lift)))throw Error("invalid_shadow_evidence");
 if(o.length!==e.outcome_rows||o.length>10000)throw Error("shadow_ledger_count_mismatch");
 if(!sha(e.score_ledger_sha))throw Error("missing_score_ledger_digest");
 const outcomes:ShadowOutcome[]=o.map((v:unknown)=>{
  if(!v||typeof v!=="object")throw Error("invalid_outcome");
  const x=v as Record<string,unknown>;
  if(typeof x.pair!=="string"||!/^[A-Z0-9]{3,24}$/.test(x.pair)||typeof x.observed_at!=="string"||!Number.isFinite(Date.parse(x.observed_at))||!["HIT","MISS","ABSTAIN"].includes(String(x.label))||!sha(x.source_sha))throw Error("invalid_outcome");
  return {pair:x.pair,observed_at:x.observed_at,label:x.label as ShadowOutcome["label"],source_sha:x.source_sha as string};
 });
 if(!Array.isArray(s)||s.length>10000)throw Error("invalid_shadow_scores");
 const scores:ShadowScore[]=s.map((v:unknown)=>{
  if(!v||typeof v!=="object")throw Error("invalid_shadow_score");
  const x=v as Record<string,unknown>;
  if(typeof x.pair!=="string"||typeof x.observed_at!=="string"||typeof x.computed_at!=="string"||typeof x.version!=="string"||!Number.isFinite(Date.parse(x.observed_at))||!Number.isFinite(Date.parse(x.computed_at))||typeof x.score!=="number"||!Number.isFinite(x.score)||x.score<0||x.score>100||!sha(x.source_sha))throw Error("invalid_shadow_score");
  if(x.source_sha!==e.source_sha||x.version!==e.version||Date.parse(x.computed_at as string)>Date.parse(x.observed_at as string))throw Error("untrusted_or_leaky_shadow_score");
  return x as ShadowScore;
 });
 const scoreKeys=new Set(scores.map(x=>x.pair+"|"+x.observed_at+"|"+x.version));
 if(scoreKeys.size!==scores.length)throw Error("duplicate_shadow_score");
 return {evidence:e as unknown as ShadowEvidence,outcomes,scores};
}
export async function verifyShadowLedger(artifacts:ShadowArtifacts):Promise<ShadowArtifacts>{
 if(!artifacts.evidence)return artifacts;
 const digest=async(v:unknown)=>Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",new TextEncoder().encode(JSON.stringify(v))))).map(x=>x.toString(16).padStart(2,"0")).join("");
 if((await digest(artifacts.outcomes)).toLowerCase()!==artifacts.evidence.outcome_ledger_sha.toLowerCase())throw Error("shadow_ledger_digest_mismatch");
 if((await digest(artifacts.scores)).toLowerCase()!==artifacts.evidence.score_ledger_sha.toLowerCase())throw Error("shadow_score_digest_mismatch");
 return artifacts;
}
export function createReadOnlyShadowLoader(url:string|undefined,fetcher:typeof fetch=fetch,trustedSourceSha?:string):()=>Promise<ShadowArtifacts>{
 return async()=>{
  if(!url)return {evidence:null,outcomes:[],scores:[]};
  const u=new URL(url);
  if(u.protocol!=="https:"||u.username||u.password||u.hash)throw Error("unsafe_shadow_artifact_url");
  const response=await fetcher(u.toString(),{method:"GET",redirect:"error",signal:AbortSignal.timeout(8000),headers:{accept:"application/json"}});
  if(!response.ok)throw Error(`shadow_artifact_http_${response.status}`);
  const text=await response.text();
  if(text.length>2000000)throw Error("shadow_artifact_too_large");
  const verified=await verifyShadowLedger(parseShadowArtifacts(JSON.parse(text)));
  if(!trustedSourceSha||!sha(trustedSourceSha)||verified.evidence?.source_sha.toLowerCase()!==trustedSourceSha.toLowerCase())throw Error("untrusted_shadow_source");
  return verified;
 };
}
