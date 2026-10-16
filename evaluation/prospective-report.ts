import {readFile,mkdir,writeFile} from "node:fs/promises";
import {evaluate,eligibleForPromotion,type Case} from "./prospective-quality";
const source=process.argv[2];
if(!source)throw new Error("Usage: bun run evaluation/prospective-report.ts <prospective-cases.json> [output.json]");
const raw=JSON.parse(await readFile(source,"utf8"));
if(!Array.isArray(raw))throw new Error("Expected JSON array of prospective cases");
const rows:Case[]=raw;
const ids=new Set<string>();
for(const r of rows){
 if(!r||typeof r.id!=="string"||ids.has(r.id)||!Number.isFinite(Date.parse(r.firstSeenAt))||!Number.isFinite(Date.parse(r.horizonEndAt))||Date.parse(r.firstSeenAt)>=Date.parse(r.horizonEndAt))throw new Error("Invalid or duplicate prospective case");
 if(r.outcomePct!==null&&(typeof r.outcomePct!=="number"||!Number.isFinite(r.outcomePct)))throw new Error("Invalid outcome");
 for(const k of ["controlAlertAt","challengerAlertAt"] as const)if(r[k]!==null&&!Number.isFinite(Date.parse(r[k]!)))throw new Error("Invalid alert time");
 ids.add(r.id);
}
const metrics=evaluate(rows);
const report={generated_at:new Date().toISOString(),source,mode:"offline_holdout_only",metrics,promotion_eligible:eligibleForPromotion(metrics),production_modified:false};
const output=process.argv[3]||"evaluation/out/prospective-report.json";
await mkdir(output.slice(0,output.lastIndexOf("/"))||".",{recursive:true});
await writeFile(output,JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify(report));
