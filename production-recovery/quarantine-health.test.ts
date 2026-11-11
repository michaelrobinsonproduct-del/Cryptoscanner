import { expect, test } from "bun:test";
import { quarantined, quarantineCount, quarantineUntil, DEFAULT_QUARANTINE_MS } from "./quarantine-health";

const now = 1000000;
const state = { failures: 2, lastFailure: now - 29999, lastSuccess: 0 };

test("metric agrees with enforcement", () => {
  expect(quarantineCount([state], now)).toBe(Number(quarantined(state, now)));
});

test("quarantine expires at exact boundary", () => {
  const expired = { ...state, lastFailure: now - DEFAULT_QUARANTINE_MS };
  expect(quarantined(expired, now)).toBe(false);
  expect(quarantineCount([expired], now)).toBe(0);
});

test("old failure excluded", () => {
  expect(quarantineCount([{ ...state, lastFailure: now - 120000 }], now)).toBe(0);
});

test("single failure excluded", () => {
  expect(quarantineCount([{ ...state, failures: 1 }], now)).toBe(0);
});

test("expiry timestamp agrees", () => {
  expect(quarantineUntil(state)).toBe(new Date(state.lastFailure + DEFAULT_QUARANTINE_MS).toISOString());
});
