import { describe, expect, test } from "bun:test";
import { targetCandleOpen, candleReturn, isClosedByDeadline, validBaseline } from "./forward-math";
describe("forward outcome math",()=>{
 test("chooses last hourly candle closed at horizon",()=>{const due=1791677850;expect(targetCandleOpen(due)).toBe(Math.floor(due/3600)*3600-3600);});
 test("calculates positive return against baseline",()=>{expect(candleReturn(100,112)).toBeCloseTo(12);});
 test("supports negative returns",()=>{expect(candleReturn(100,85)).toBeCloseTo(-15);});
 test("rejects zero and non-finite prices",()=>{expect(()=>candleReturn(0,100)).toThrow("invalid_price");expect(()=>candleReturn(100,Infinity)).toThrow("invalid_price");});
 test("rejects invalid deadlines",()=>{expect(()=>targetCandleOpen(NaN)).toThrow("invalid_outcome_deadline");});
 test("does not accept an unfinished candle",()=>{expect(isClosedByDeadline(100,3699999)).toBe(false);expect(isClosedByDeadline(100,3700000)).toBe(true);});\n test("rejects missing, invalid, and look-ahead baselines",()=>{expect(validBaseline(100,"2026-10-10T00:00:00Z",1791677850)).toBe(true);expect(validBaseline(100,"2026-10-13T00:00:00Z",1791677850)).toBe(false);expect(validBaseline(0,"2026-10-10T00:00:00Z",1791677850)).toBe(false);expect(validBaseline(100,"invalid",1791677850)).toBe(false);});
});
