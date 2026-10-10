import {expect,test} from "bun:test";
import {fallbackDecision} from "./fallback-policy";
test("fresh websocket eligible for further confirmation",()=>expect(fallbackDecision("WS_VALID",false,true,true,true)).toBe("ELIGIBLE_FOR_CONFIRMATION"));
test("quarantine without independently verified REST is WATCH",()=>expect(fallbackDecision("QUARANTINED",false,true,true,true)).toBe("WATCH"));
test("source failure with verified REST may continue confirmation",()=>expect(fallbackDecision("SOURCE_FAILED",true,true,true,true)).toBe("ELIGIBLE_FOR_CONFIRMATION"));
test("stale REST never qualifies",()=>expect(fallbackDecision("REST_VALID",true,false,true,true)).toBe("WATCH"));
test("stale state never qualifies",()=>expect(fallbackDecision("STALE",true,true,true,true)).toBe("WATCH"));
test("fallback cannot bypass stale order book",()=>expect(fallbackDecision("QUARANTINED",true,true,false,true)).toBe("WATCH"));
