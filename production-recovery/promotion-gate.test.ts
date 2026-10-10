import { describe, expect, test } from "bun:test";

// Promotion must fail closed. This is an isolated contract, not production wiring.
export type Evidence = {
  sourceRevisionVerified: boolean;
  testsPassed: boolean;
  deploymentHealthy: boolean;
  latestScanFresh: boolean;
  persistedAndRetrievable: boolean;
  rollbackVerified: boolean;
  duplicateCycleIds: number;
  observedCycles: number;
  expectedCycles: number;
};

export function mayPromote(e: Evidence): boolean {
  return e.sourceRevisionVerified && e.testsPassed && e.deploymentHealthy &&
    e.latestScanFresh && e.persistedAndRetrievable && e.rollbackVerified &&
    e.duplicateCycleIds === 0 && e.expectedCycles > 0 &&
    e.observedCycles >= e.expectedCycles;
}

const valid: Evidence = {
  sourceRevisionVerified: true, testsPassed: true, deploymentHealthy: true,
  latestScanFresh: true, persistedAndRetrievable: true, rollbackVerified: true,
  duplicateCycleIds: 0, observedCycles: 96, expectedCycles: 96,
};

describe("production promotion fail-closed contract", () => {
  test("accepts complete verified evidence", () => expect(mayPromote(valid)).toBe(true));
  for (const key of [
    "sourceRevisionVerified", "testsPassed", "deploymentHealthy",
    "latestScanFresh", "persistedAndRetrievable", "rollbackVerified",
  ] as const) {
    test(`rejects missing ${key}`, () => expect(mayPromote({ ...valid, [key]: false })).toBe(false));
  }
  test("rejects duplicate cycles", () => expect(mayPromote({ ...valid, duplicateCycleIds: 1 })).toBe(false));
  test("rejects missing cycles", () => expect(mayPromote({ ...valid, observedCycles: 95 })).toBe(false));
  test("rejects absent reliability history", () => expect(mayPromote({ ...valid, expectedCycles: 0 })).toBe(false));
});
