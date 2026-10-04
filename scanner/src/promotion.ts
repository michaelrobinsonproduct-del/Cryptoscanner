import type { DiscoveryCandidate, MarketConfirmation, Decision } from "./types";
import { newerRefresh, refreshExtensionPct } from "./refresh-baseline";
import { Reason } from "./reason-codes";

export interface PromotionResult { decision: Decision; reason: string; extensionPct: number | null }

const fresh = (c: MarketConfirmation) => c.success && c.twoSidedBook && c.executableBbo && c.recentTradeConfirmation && c.newestTradeAgeSeconds !== null && c.newestTradeAgeSeconds <= 300;

export function evaluatePromotion(candidate: DiscoveryCandidate, first: MarketConfirmation, second: MarketConfirmation): PromotionResult {
  if (candidate.score < 80) return { decision: "WATCH", reason: Reason.ScoreBelow, extensionPct: null };
  if (Math.abs(candidate.displacementPct) > 3) return { decision: "WATCH", reason: Reason.Displacement, extensionPct: null };
  if (!fresh(first) || !fresh(second)) return { decision: "WATCH", reason: Reason.Execution, extensionPct: null };
  if (!first.bestAsk || !second.bestAsk) return { decision: "WATCH", reason: Reason.MissingAsk, extensionPct: null };
  if (!newerRefresh(first.fetchedAt, second.fetchedAt)) return { decision: "WATCH", reason: Reason.RefreshOrder, extensionPct: null };
  const extensionPct = refreshExtensionPct(first.bestAsk, second.bestAsk);
  if (extensionPct === null || extensionPct > 2) return { decision: "WATCH", reason: Reason.Extension, extensionPct };
  return { decision: "PROMOTION_ELIGIBLE", reason: Reason.Pass, extensionPct };
}
