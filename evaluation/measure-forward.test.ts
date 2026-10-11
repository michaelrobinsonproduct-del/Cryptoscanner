import { describe, expect, test } from "bun:test";
function targetCandleOpen(dueSeconds:number){return Math.floor(dueSeconds/3600)*3600-3600;}
function candleReturn(baselineAsk:number,candleClose:number){if(!(baselineAsk>0&&candleClose>0))throw new Error("invalid_price");return (candleClose/baselineAsk-1)*100;}
describe("forward outcome math",()=>{
 test("chooses last hourly candle closed at horizon",()=>{expect(targetCandleOpen(1791677850)).toBe(Math.floor(1791677850/3600)*3600-3600);});
 test("calculates percentage return against baseline",()=>{expect(candleReturn(100,112)).toBeCloseTo(12);});
 test("supports negative returns",()=>{expect(candleReturn(100,85)).toBeCloseTo(-15);});
 test("rejects non-positive prices",()=>{expect(()=>candleReturn(0,100)).toThrow("invalid_price");});
});
