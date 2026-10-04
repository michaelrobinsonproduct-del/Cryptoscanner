import type { DiscoveryCandidate, MarketConfirmation, Decision } from "./types";

export interface PromotionResult { decision: Decision; reason: string; extensionPct: number | null }

const fresh = (c: MarketConfirmation) => c.success && c.twoSidedBook && c.executableBbo && c.recentTradeConfirmation && c.newestTradeAgeSeconds !== null && c.newestTradeAgeSeconds <= 300;

export function evaluatePromotion(candidate: DiscoveryCandidate, first: MarketConfirmation, second: MarketConfirmation): PromotionResult {
  if (candidate.score < 80) return { decision: "WATCH", reason: "score_below_gate", extensionPct: null };
  if (Math.abs(candidate.displacementPct) > 3) return { decision: "WATCH", reason: "displacement_not_early", extensionPct: null };
  if (!fresh(first) || !fresh(second)) return { decision: "WATCH", reason: "execution_confirmation_failed", extensionPct: null };
  if (!first.bestAsk || !second.bestAsk || candidate.discoveryPrice <= 0) return { decision: "WATCH", reason: "missing_price_baseline", extensionPct: null };
  const extensionPct = ((second.bestAsk / candidate.discoveryPrice) - 1) * 100;
  if (extensionPct > 5) return { decision: "WATCH", reason: "no_longer_early_vs_discovery", extensionPct };
  return { decision: "PROMOTION_ELIGIBLE", reason: "all_independent_gates_passed", extensionPct };
}
