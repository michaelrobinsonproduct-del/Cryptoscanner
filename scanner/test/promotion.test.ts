import { expect,test } from "bun:test";import { evaluatePromotion } from "../src/promotion";
const c={pair:"TEST/USD",score:90,discoveryPrice:100,discoveryAt:new Date().toISOString(),displacementPct:1};
const ok=(ask:number,offset=0)=>({pair:c.pair,success:true,twoSidedBook:true,executableBbo:true,recentTradeConfirmation:true,newestTradeAgeSeconds:1,bestBid:ask-.1,bestAsk:ask,fetchedAt:new Date(Date.now()+offset).toISOString()});
test("promotes only when independent gates remain early",()=>expect(evaluatePromotion(c,ok(101),ok(102,1000)).decision).toBe("PROMOTION_ELIGIBLE"));
test("rejects stale trade",()=>expect(evaluatePromotion(c,{...ok(101),newestTradeAgeSeconds:301},ok(102,1000)).decision).toBe("WATCH"));
test("rejects extension beyond independent refresh gate",()=>expect(evaluatePromotion(c,ok(101),ok(104,1000)).decision).toBe("WATCH"));
test("rejects already displaced discovery",()=>expect(evaluatePromotion({...c,displacementPct:4},ok(101),ok(102,1000)).decision).toBe("WATCH"));
test("rejects non-newer second refresh",()=>{const a=ok(101),b={...ok(101.5),fetchedAt:a.fetchedAt};expect(evaluatePromotion(c,a,b).reason).toBe("second_refresh_not_newer")});
