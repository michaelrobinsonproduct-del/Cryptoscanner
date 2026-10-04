import { expect,test } from "bun:test";import { evaluatePromotion } from "../src/promotion";
const c={pair:"TEST/USD",score:90,discoveryPrice:100,discoveryAt:new Date().toISOString(),displacementPct:1};
const ok=(ask:number)=>({pair:c.pair,success:true,twoSidedBook:true,executableBbo:true,recentTradeConfirmation:true,newestTradeAgeSeconds:1,bestBid:ask-.1,bestAsk:ask,fetchedAt:new Date().toISOString()});
test("promotes only when independent gates remain early",()=>expect(evaluatePromotion(c,ok(101),ok(102)).decision).toBe("PROMOTION_ELIGIBLE"));
test("rejects stale trade",()=>expect(evaluatePromotion(c,{...ok(101),newestTradeAgeSeconds:301},ok(102)).decision).toBe("WATCH"));
test("rejects extension beyond discovery early gate",()=>expect(evaluatePromotion(c,ok(101),ok(106)).decision).toBe("WATCH"));
test("rejects already displaced discovery",()=>expect(evaluatePromotion({...c,displacementPct:4},ok(101),ok(102)).decision).toBe("WATCH"));
