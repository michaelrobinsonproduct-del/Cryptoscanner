import {describe,expect,test} from "bun:test";
import {marketActionable,isQuarantined,type MarketEvidence} from "./market-evidence";
const now=1_000_000;
const good:MarketEvidence={tickerReceivedAtMs:now-100,bookReceivedAtMs:now-100,latestTradeAtMs:now-100,nowMs:now,maxFeedAgeMs:5000,maxTradeAgeMs:60000,bid:10,ask:10.01,wsHealthy:true,restFallbackVerified:false};
describe("market evidence fail-closed",()=>{
 test("accepts verified fresh book, ticker and trade",()=>expect(marketActionable(good)).toBe(true));
 test("rejects stale trade",()=>expect(marketActionable({...good,latestTradeAtMs:now-60001})).toBe(false));
 test("rejects stale ticker",()=>expect(marketActionable({...good,tickerReceivedAtMs:now-5001})).toBe(false));
 test("rejects stale book",()=>expect(marketActionable({...good,bookReceivedAtMs:now-5001})).toBe(false));
 test("rejects future timestamp",()=>expect(marketActionable({...good,latestTradeAtMs:now+1})).toBe(false));
 test("rejects missing trade",()=>expect(marketActionable({...good,latestTradeAtMs:null})).toBe(false));
 test("rejects bad spread",()=>expect(marketActionable({...good,ask:9})).toBe(false));
 test("rejects WS failure without verified fallback",()=>expect(marketActionable({...good,wsHealthy:false})).toBe(false));
 test("allows verified fresh REST fallback",()=>expect(marketActionable({...good,wsHealthy:false,restFallbackVerified:true})).toBe(true));
 test("rejects stale REST fallback",()=>expect(marketActionable({...good,wsHealthy:false,restFallbackVerified:true,bookReceivedAtMs:now-5001})).toBe(false));
});
describe("quarantine expiry",()=>{
 test("quarantines repeated recent failure",()=>expect(isQuarantined({failureCount:2,lastFailureAtMs:now-100,cooldownMs:1000},now)).toBe(true));
 test("expires quarantine at boundary",()=>expect(isQuarantined({failureCount:2,lastFailureAtMs:now-1000,cooldownMs:1000},now)).toBe(false));
 test("single failure is not quarantine",()=>expect(isQuarantined({failureCount:1,lastFailureAtMs:now-100,cooldownMs:1000},now)).toBe(false));
});
