export type MarketEvidence = { tickerReceivedAtMs: number | null; bookReceivedAtMs: number | null; latestTradeAtMs: number | null; nowMs: number; maxFeedAgeMs: number; maxTradeAgeMs: number; bid: number; ask: number; wsHealthy: boolean; restFallbackVerified: boolean };
export function marketActionable(x: MarketEvidence): boolean {
  const finite = [x.nowMs,x.maxFeedAgeMs,x.maxTradeAgeMs,x.bid,x.ask].every(Number.isFinite);
  if (!finite || x.maxFeedAgeMs <= 0 || x.maxTradeAgeMs <= 0 || x.bid <= 0 || x.ask < x.bid) return false;
  if (!x.wsHealthy && !x.restFallbackVerified) return false;
  for (const [timestamp,limit] of [[x.tickerReceivedAtMs,x.maxFeedAgeMs],[x.bookReceivedAtMs,x.maxFeedAgeMs],[x.latestTradeAtMs,x.maxTradeAgeMs]] as const) {
    if (timestamp === null || !Number.isFinite(timestamp) || timestamp > x.nowMs || x.nowMs-timestamp > limit) return false;
  }
  return true;
}
export type Quarantine = { failureCount: number; lastFailureAtMs: number; cooldownMs: number };
export function isQuarantined(q: Quarantine, nowMs: number): boolean {
  return q.failureCount >= 2 && Number.isFinite(q.lastFailureAtMs) && Number.isFinite(nowMs) && Number.isFinite(q.cooldownMs) && q.cooldownMs > 0 && nowMs >= q.lastFailureAtMs && nowMs-q.lastFailureAtMs < q.cooldownMs;
}
