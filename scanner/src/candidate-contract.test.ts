import { test, expect } from "bun:test";
import { selectDiscoveryCandidates } from "./candidate-contract";

const valid = { pair: "TAOUSD", score: 85, displacement_pct: 1.5, discovered_at: "2026-11-02T20:00:00Z" };
test("manual and scheduled entry calls select identical candidates", () => {
  const scan = { candidates: [valid], fetched_at: "2026-11-02T20:01:00Z" };
  const manual = selectDiscoveryCandidates(scan);
  const scheduled = selectDiscoveryCandidates(scan);
  expect(manual).toEqual(scheduled);
  expect(manual).toEqual([{ pair: "TAOUSD", score: 85, displacementPct: 1.5, discoveredAt: valid.discovered_at }]);
});
test("fail closed on missing or invalid discovery provenance", () => {
  expect(selectDiscoveryCandidates({ candidates: [{ ...valid, discovered_at: undefined }] })).toEqual([]);
  expect(selectDiscoveryCandidates({ candidates: [{ ...valid, discovered_at: "invalid" }] })).toEqual([]);
  expect(selectDiscoveryCandidates({ candidates: [{ ...valid, score: "NaN" }] })).toEqual([]);
  expect(selectDiscoveryCandidates({ candidates: [{ ...valid, displacement_pct: Infinity }] })).toEqual([]);
});
test("collector fallback timestamp is preserved, not replaced by current time", () => {
  expect(selectDiscoveryCandidates({ results: [{ ...valid, discovered_at: undefined }], fetched_at: "2026-11-02T19:00:00Z" })[0].discoveredAt).toBe("2026-11-02T19:00:00Z");
});
test("reject malformed arrays and apply candidate limit before filtering", () => {
  expect(selectDiscoveryCandidates({ candidates: {} })).toEqual([]);
  expect(selectDiscoveryCandidates({ candidates: Array(20).fill({ score: 0 }).concat(valid) })).toEqual([]);
});
