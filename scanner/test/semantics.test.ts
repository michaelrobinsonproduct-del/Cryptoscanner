import{expect,test}from"bun:test";import{isStillEarly,movePct}from"../src/semantics";
const discovery={price:50,at:"2026-10-03T00:00:00Z",source:"scan",window:"discovery_baseline" as const};
const r1={price:100,at:"2026-10-03T00:00:05Z",source:"kraken_rest",window:"refresh_1" as const};
const r2={price:101,at:"2026-10-03T00:00:08Z",source:"kraken_rest",window:"refresh_2" as const};
test("measures price movement",()=>expect(movePct(r1,r2)).toBeCloseTo(1));
test("still-early ignores stale discovery baseline",()=>expect(isStillEarly(r1,r2)).toBe(true));
test("rejects wrong window semantics",()=>expect(isStillEarly(discovery,r2)).toBe(false));
test("rejects excessive independent refresh extension",()=>expect(isStillEarly(r1,{...r2,price:103})).toBe(false));
