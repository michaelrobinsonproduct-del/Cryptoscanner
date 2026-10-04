export type Decision = "WATCH" | "PROMOTION_ELIGIBLE";

export interface DiscoveryCandidate {
  pair: string;
  score: number;
  discoveryPrice: number;
  discoveryAt: string;
  displacementPct: number;
}

export interface MarketConfirmation {
  pair: string;
  success: boolean;
  twoSidedBook: boolean;
  executableBbo: boolean;
  recentTradeConfirmation: boolean;
  newestTradeAgeSeconds: number | null;
  bestBid: number | null;
  bestAsk: number | null;
  fetchedAt: string;
}
