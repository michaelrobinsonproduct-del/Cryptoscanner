import type { DiscoveryCandidate, MarketConfirmation, Decision } from "./types";
import { newerRefresh, refreshExtensionPct } from "./refresh-baseline";

export interface PromotionResult { decision: Decision; reason: string; extensionPct: number | null }

const fresh = (c: MarketConfirmation) => c.success && c.twoSidedBook && c.executableBbo && c.recentTradeConfirmation && c.newestTradeAgeSeconds !== null && c.newestTradeAgeSeconds <= 300;

export function evaluatePromotion(candidate: DiscoveryCandidate, first: MarketConfirmation, second: MarketConfirmation): PromotionResult {
  if (candidate.score < 80) return { decision: "WATCH", reason: "score_below_gate", extensionPct: null };
  if (Math.abs(candidate.displacementPct) > 3) return { decision: "WATCH", reason: "displacement_not_early", extensionPct: null };
  if (!fresh(first) || !fresh(second)) return { decision: "WATCH", reason: "execution_confirmation_failed", extensionPct: null };
  if (!first.bestAsk || !second.bestAsk) return { decision: "WATCH", reason: "missing_executable_ask", extensionPct: null };
  if (!newerRefresh(first.fetchedAt, second.fetchedAt)) return { decision: "WATCH", reason: "second_refresh_not_newer", extensionPct: null };
  const extensionPct = refreshExtensionPct(first.bestAsk, second.bestAsk);
  if (extensionPct === null || extensionPct > 2) return { decision: "WATCH", reason: "no_longer_early_between_independent_refreshes", extensionPct };
  return { decision: "PROMOTION_ELIGIBLE", reason: "all_independent_gates_passed", extensionPct };
}
