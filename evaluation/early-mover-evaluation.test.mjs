import { test, expect } from "bun:test";
import { evaluateEarlyMoverSignals } from "./early-mover-evaluation.mjs";
const base = { market:"TEST/USD", at:"2026-10-01T00:00:00Z", capturedAt:"2026-10-01T00:00:01Z", referencePrice:1, tier:"research_watch" };
test("matured returns are measured only after the signal and never produce verified buys", () => {
 const x=evaluateEarlyMoverSignals([base],[{market:"TEST/USD",at:base.at,price:1},{market:"TEST/USD",at:"2026-10-01T12:00:00Z",price:1.5},{market:"TEST/USD",at:"2026-10-02T00:00:00Z",price:1.2}]);
 expect(x.signals[0].horizons[0].thresholds["50"]).toBe(true);
 expect(x.signals[0].buyVerified).toBe(false);
});
test("unmatured outcomes remain pending, not false negatives", () => {
 const x=evaluateEarlyMoverSignals([base],[{market:"TEST/USD",at:base.at,price:1}]);
 expect(x.signals[0].horizons[0].status).toBe("pending");
});
test("reject future-dated signal capture anomalies", () => {
 expect(() => evaluateEarlyMoverSignals([{...base,capturedAt:"2026-09-30T23:00:00Z"}],[{market:"TEST/USD",at:base.at,price:1}])).toThrow();
});
test("reject retrospective labels masquerading as live tiers", () => {
 expect(() => evaluateEarlyMoverSignals([{...base,tier:"verified_buy"}],[{market:"TEST/USD",at:base.at,price:1}])).toThrow();
});
