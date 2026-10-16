// Pure, fail-closed reconciliation. No production IO, schedules or trade execution.
export function reconcileScanEvidence(input) {
  const { durable, recommendation, refresh, nowMs = Date.now(), maxAgeMs = 15 * 60_000 } = input || {};
  const errors = [];
  const stamp = value => typeof value === "string" && Number.isFinite(Date.parse(value)) ? Date.parse(value) : NaN;
  if (!durable || !recommendation) return { status: "UNVERIFIED", buyApproved: false, errors: ["missing_durable_or_recommendation"] };
  if (!durable.run_id || durable.run_id !== recommendation.run_id) errors.push("run_id_mismatch");
  const completed = stamp(durable.completed_at);
  const generated = stamp(recommendation.generated_at);
  if (!Number.isFinite(nowMs) || !Number.isFinite(maxAgeMs) || maxAgeMs <= 0) errors.push("invalid_clock_or_age_limit");
  if (!Number.isFinite(completed) || !Number.isFinite(generated)) errors.push("invalid_timestamp");
  else {
    if (generated < completed - 120_000) errors.push("report_precedes_scan");
    if (completed > nowMs + 10_000 || generated > nowMs + 10_000) errors.push("future_timestamp");
    if (nowMs - generated > maxAgeMs) errors.push("stale_report");
  }
  const u = durable.universe_count, s = durable.scanned_count, f = durable.failed_count;
  if (![u,s,f].every(x => Number.isSafeInteger(x) && x >= 0) || u === 0 || s + f !== u) errors.push("coverage_invalid");
  if (durable.persistence_verified !== true) errors.push("persistence_unverified");
  if (recommendation.verified_status !== "COMPLETE") errors.push("report_incomplete");
  if (!Array.isArray(recommendation.currently_actionable)) errors.push("actionable_list_missing");
  const verified = errors.length === 0;
  // Refresh snapshots are context only. They cannot independently approve an entry.
  return { status: verified ? "VERIFIED_REPORT" : "UNVERIFIED", buyApproved: false,
    eligibleForEntryReview: verified && recommendation.currently_actionable.length > 0,
    authoritativeActionable: verified ? recommendation.currently_actionable : [],
    refreshSnapshotOnly: refresh?.actionable_count ?? null, errors };
}
