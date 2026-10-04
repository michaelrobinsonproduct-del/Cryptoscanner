import {expect,test} from "bun:test";import {comparable,deviationPct} from "../src/freshness";
const a={source:"kraken",price:100,observedAt:"2026-10-03T12:00:00Z"};
test("accepts timestamp-comparable quotes",()=>expect(comparable(a,{source:"x",price:101,observedAt:"2026-10-03T12:00:10Z"})).toBe(true));
test("rejects asynchronous quotes",()=>expect(comparable(a,{source:"x",price:101,observedAt:"2026-10-03T12:01:00Z"})).toBe(false));
test("does not calculate deviation from stale quote",()=>expect(deviationPct(a,{source:"x",price:101,observedAt:"2026-10-03T12:01:00Z"})).toBe(null));
