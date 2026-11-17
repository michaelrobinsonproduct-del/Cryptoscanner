// Existing paper writer only. No Kraken requests, waits, or ledger mutations.
export const REPO = "michaelrobinsonproduct-del/Cryptoscanner";
export const WRITER = "paper-pipeline.yml";
const age = (value, now) => (now - Date.parse(value)) / 1000;
const fresh = (value, now, max=600) => Number.isFinite(age(value,now)) && age(value,now)>=0 && age(value,now)<=max;
const sha = value => typeof value==="string" && /^[a-f0-9]{40}$/.test(value);
const checksum = value => typeof value==="string" && /^[a-f0-9]{64}$/.test(value);
const id = value => String(value);
export function verified(report, run, now) {
  const l=report?.independent_legacy_evidence, d=report?.dual_scanner_report;
  if (!report || !l || !d || !run || run.status!=="completed" || run.conclusion!=="success" ||
      run.head_branch!=="main" || run.path?.split("@")[0]!==".github/workflows/"+WRITER ||
      id(report.run_id)!==id(run.id) || !sha(report.source_sha) || report.source_sha!==run.head_sha ||
      report.status!=="SUCCESS_PAPER_ONLY" || report.remote_readback_verified!==true ||
      report.buy_approved!==false || report.production_applied!==false ||
      !Number.isSafeInteger(report.ledger_generation) || report.ledger_generation<1 ||
      !checksum(report.ledger_sha256) || !fresh(report.as_of,now) ||
      !Number.isFinite(report.max_client_quote_age_seconds) ||
      report.max_client_quote_age_seconds<0 || report.max_client_quote_age_seconds>600 ||
      l.independent_execution!==true || l.execution_location!=="SAME_WRITER_JOB" ||
      l.buy_approved!==false || l.production_applied!==false || l.trade_executed!==false ||
      id(l.run_id)!==id(run.id) || id(l.trigger_paper_run_id)!==id(run.id) ||
      l.source_sha!==run.head_sha || !fresh(l.as_of,now) ||
      id(d.writer_run_id)!==id(run.id) || id(d.legacy_run_id)!==id(run.id) ||
      d.ledger_sha256!==report.ledger_sha256) return false;
  const arrays=[report.candidates,l.candidates,d.challenger_watch,d.legacy_watch];
  if(!arrays.every(a=>Array.isArray(a) && a.every(c=>fresh(c.quote_observed_at,now)))) return false;
  // Compact score-only rank rows have no quote field by design; bind their
  // symbol to a timestamped candidate instead of treating them as quotes.
  const bySymbol=new Map(report.candidates.map(c=>[c.symbol,c]));
  const ranks=[report.rankings?.baseline,report.rankings?.challenger,d.baseline_rankings];
  return ranks.every(a=>Array.isArray(a) && a.every(c=>bySymbol.has(c.symbol) &&
    (c.quote_observed_at===undefined || fresh(c.quote_observed_at,now))));
}
// Reconcile an exact unresolved intent, never replay its POST. GitHub's
// native writer mutex is still authoritative if a late run appears.
// Require complete, fixed-window history; incomplete or inconsistent
// responses cannot retire an intent. Wait 30 minutes for delayed indexing.
const RECONCILE_GRACE_MS=30*60*1000;
async function reconcileAttempt(api,previous,now) {
  const at=Number(previous.slot);
  if(!Number.isSafeInteger(at) || at<=0 || String(at)!==previous.slot || at%300000!==0 || at>now)
    return {status:"AMBIGUOUS_STOP"};
  const range=encodeURIComponent(new Date(at).toISOString()+".."+new Date(now).toISOString());
  const path="actions/workflows/"+WRITER+"/runs?branch=main&created="+range+"&per_page=100";
  let count=null;
  const items=[];
  for(let page=1;page<=10;page++){
    const h=await api(path+"&page="+page);
    if(!Number.isSafeInteger(h?.total_count)||h.total_count<0||h.total_count>=1000||
       !Array.isArray(h.workflow_runs)||h.workflow_runs.length>100||
       (count!==null&&h.total_count!==count)) return {status:"AMBIGUOUS_HISTORY_INCOMPLETE"};
    count=h.total_count;
    const expected=Math.min(100,Math.max(0,count-items.length));
    if(h.workflow_runs.length!==expected)return {status:"AMBIGUOUS_HISTORY_INCOMPLETE"};
    items.push(...h.workflow_runs);
    if(items.length===count)break;
  }
  if(items.length!==count || new Set(items.map(r=>r?.id)).size!==count ||
     items.some(r=>!Number.isSafeInteger(r?.id)||r.id<=0||r.head_branch!=="main"||
       typeof r.display_title!=="string"||typeof r.event!=="string"||
       !Number.isFinite(Date.parse(r.created_at))||Date.parse(r.created_at)<at||Date.parse(r.created_at)>now))
    return {status:"AMBIGUOUS_HISTORY_INCOMPLETE"};
  const matches=items.filter(r=>r.display_title==="paper-api-"+previous.slot);
  if(matches.length===1 && matches[0].event==="workflow_dispatch")
    return {status:"MATCH",runId:matches[0].id};
  if(matches.length!==0)return {status:"AMBIGUOUS_STOP"};
  if(now-at<RECONCILE_GRACE_MS || items.some(r=>r.status!=="completed"))
    return {status:"AMBIGUOUS_STOP"};
  return {status:"NO_MATCH_AFTER_GRACE",count,checkedAt:new Date(now).toISOString()};
}

export async function tick({api,store,now,scheduled,enabled}) {
  if (!enabled) return {status:"STOPPED"};
  if (!Number.isFinite(scheduled) || now-scheduled<0 || now-scheduled>180000)
    return {status:"EXPIRED_SLOT"};
  const slot=String(Math.floor(scheduled/300000)*300000);
  const previous=await store.get("attempt");
  if (previous && !previous.terminal) {
    let runId=previous.runId;
    if (!runId) {
      const evidence=await reconcileAttempt(api,previous,now);
      if(evidence.status==="NO_MATCH_AFTER_GRACE") {
        // Archive the exact original attempt and evidence before releasing it.
        // Absence is not proof GitHub rejected it; never claim that or replay it.
        const retired={...previous,terminal:true,outcome:"NO_CORRELATED_RUN_AFTER_GRACE",
          reconciledAt:evidence.checkedAt,historyCount:evidence.count};
        await store.put("retired:"+previous.slot,retired);
        await store.put("attempt",retired);
        // Resume only on a later scheduled slot, never on the ambiguous one.
        return {status:"AMBIGUOUS_RETIRED",slot:previous.slot,historyCount:evidence.count};
      }
      if(evidence.status!=="MATCH")return {status:evidence.status,slot:previous.slot};
      runId=evidence.runId;
      await store.put("attempt",{...previous,runId});
    }
    const run=await api("actions/runs/"+runId);
    if(run.status!=="completed") return {status:"WRITER_ACTIVE",runId};
    if(run.conclusion!=="success" || id(run.id)!==id(runId) || !sha(run.head_sha) ||
       (previous.source!=null && run.head_sha!==previous.source) || run.head_branch!=="main" ||
       run.path?.split("@")[0]!==".github/workflows/"+WRITER ||
       run.display_title!=="paper-api-"+previous.slot || run.event!=="workflow_dispatch") {
      await store.put("attempt",{...previous,runId,terminal:true,outcome:"FAILED"});
      return {status:"WRITER_FAILED",runId};
    }
    // A completed, exact writer can no longer overlap. Persist terminal state
    // before the optional receipt read: verification failure cannot lock the clock.
    await store.put("attempt",{...previous,source:run.head_sha,runId,terminal:true,outcome:"RECEIPT_PENDING"});
    const r=await api("contents/verified-results/results.json?ref=paper-proof-ledger");
    if(!verified(r,run,now)) {
      // Never pretend an overwritten/stale receipt confirms the exact writer.
      // If the writer is terminal, release ownership for a different slot only.
      await store.put("attempt",{...previous,source:run.head_sha,runId,terminal:true,outcome:"UNVERIFIED"});
      return {status:"UNVERIFIED_WRITER",runId};
    }
    await store.put("attempt",{...previous,source:run.head_sha,runId,terminal:true,outcome:"VERIFIED",
      generation:r.ledger_generation,checksum:r.ledger_sha256,asOf:r.as_of});
    if(previous.slot===slot || fresh(r.as_of,now,240)) return {status:"VERIFIED",runId,generation:r.ledger_generation};
  }
  if(previous?.slot===slot) return {status:"SLOT_ALREADY_ATTEMPTED"};
  // Commission the exact same POST that works in GitHub recovery. Cloudflare
  // owns one durable intent per slot; GitHub already serializes every entry
  // path with its workflow-level single-writer concurrency group.
  // Do not depend on unrelated history, ledger or main-ref reads before POST.
  // The resulting run supplies the actual source SHA for receipt verification.
  const source=null;
  await store.put("attempt",{slot,source,terminal:false,runId:null});
  let accepted;
  try {
    // REST 2026-03-10 always returns run details; the old opt-in was removed.
    accepted=await api("actions/workflows/"+WRITER+"/dispatches",
      {ref:"main",inputs:{scheduler_request_id:slot}});
  } catch(error) {
    // Explicit GitHub rejection means no accepted dispatch. Keep this slot
    // terminal, allowing a later slot after the existing active-writer guards.
    // Network failures, timeouts and 5xx remain ambiguous and are not retried.
    if(/^GITHUB_HTTP_(400|401|403|404|422|429)$/.test(error?.message)) {
      await store.put("attempt",{slot,source,terminal:true,runId:null,outcome:"REJECTED",error:error.message});
      return {status:"DISPATCH_REJECTED",slot,error:error.message};
    }
    throw error;
  }
  if(!Number.isSafeInteger(accepted?.workflow_run_id) || accepted.workflow_run_id<1)
    throw Error("AMBIGUOUS_DISPATCH");
  await store.put("attempt",{slot,source,terminal:false,runId:accepted.workflow_run_id});
  return {status:"DISPATCH_ACCEPTED",runId:accepted.workflow_run_id,source,slot};
}
