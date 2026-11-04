import { test, expect } from "bun:test";
import { selectDiscoveryCandidates, classifyConfirmationFailure, confirmedPairIdentity } from "./candidate-contract";
const valid = { pair: "TAOUSD", score: 85, displacement_pct: 1.5, discovered_at: "2026-11-02T20:00:00Z" };
test("manual and scheduled selectors are deterministic", () => {
 const scan = { candidates: [valid], fetched_at: "2026-11-02T20:01:00Z" };
 expect(selectDiscoveryCandidates(scan)).toEqual(selectDiscoveryCandidates(scan));
 expect(selectDiscoveryCandidates(scan)).toEqual([{pair:"TAOUSD",score:85,displacementPct:1.5,discoveredAt:valid.discovered_at}]);
});
test("missing, invalid and nonfinite provenance abstains", () => {
 for (const candidate of [{...valid,discovered_at:undefined},{...valid,discovered_at:"invalid"},{...valid,score:"NaN"},{...valid,displacement_pct:Infinity}])
   expect(selectDiscoveryCandidates({candidates:[candidate]})).toEqual([]);
});
test("collector timestamp fallback remains source-qualified", () => {
 expect(selectDiscoveryCandidates({results:[{...valid,discovered_at:undefined}],fetched_at:"2026-11-02T19:00:00Z"})[0].discoveredAt).toBe("2026-11-02T19:00:00Z");
});
test("malformed arrays and first twenty VALID candidate limit", () => {
 expect(selectDiscoveryCandidates({candidates:{}})).toEqual([]);
 expect(selectDiscoveryCandidates({candidates:Array(20).fill({score:0}).concat(valid)})).toHaveLength(1);
 const rows=Array.from({length:25},(_,i)=>({...valid,pair:`PAIR${String(i).padStart(3,"0")}`}));
 expect(selectDiscoveryCandidates({candidates:rows})).toHaveLength(20);
});
test("duplicate pair only gets one confirmation and malformed pair is excluded", () => {
 expect(selectDiscoveryCandidates({candidates:[valid,{...valid,score:90},{...valid,pair:"TAO/../../bad"}]})).toHaveLength(1);
});
test("confirmation errors abstain rather than presenting a WATCH signal", () => {
 expect(classifyConfirmationFailure("TAOUSD",new Error("timeout")).decision).toBe("ABSTAIN");
});

test("confirmation identity must come from upstream payload, never requested-pair fallback", () => {
 expect(confirmedPairIdentity({pair:"TAOUSD"})).toBe("TAOUSD");
 expect(confirmedPairIdentity({symbol:"XRPUSD"})).toBe("XRPUSD");
 expect(confirmedPairIdentity({})).toBe("");
 expect(confirmedPairIdentity(null)).toBe("");
});
