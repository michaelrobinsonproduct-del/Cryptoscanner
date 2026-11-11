import {describe,expect,test} from "bun:test";
import {validateCycles,type ScanCycle} from "./cycle-integrity";
const good:ScanCycle={cycleId:"2026-10-10T19:45:00Z",startedAt:"2026-10-10T19:45:01Z",completedAt:"2026-10-10T19:47:01Z",universe:619,scanned:619,failed:0,persisted:true,retrieved:true};
describe("scheduled cycle integrity",()=>{
 test("accepts complete durable cycle",()=>expect(validateCycles([good],[good.cycleId]).ok).toBe(true));
 test("rejects missing cycle",()=>expect(validateCycles([],[good.cycleId]).issues).toContain("missing_cycle:"+good.cycleId));
 test("rejects duplicate",()=>expect(validateCycles([good,good],[good.cycleId]).issues).toContain("duplicate_cycle:"+good.cycleId));
 test("rejects partial universe",()=>expect(validateCycles([{...good,scanned:618}],[good.cycleId]).ok).toBe(false));
 test("rejects failed market",()=>expect(validateCycles([{...good,failed:1}],[good.cycleId]).ok).toBe(false));
 test("rejects missing persistence",()=>expect(validateCycles([{...good,persisted:false}],[good.cycleId]).ok).toBe(false));
 test("rejects unreadable result",()=>expect(validateCycles([{...good,retrieved:false}],[good.cycleId]).ok).toBe(false));
 test("rejects incomplete scan",()=>expect(validateCycles([{...good,completedAt:null}],[good.cycleId]).ok).toBe(false));
 test("rejects unexpected manual cycle",()=>expect(validateCycles([good],["2026-10-10T20:00:00Z"]).ok).toBe(false));
 test("rejects missing schedule",()=>expect(validateCycles([],[]).ok).toBe(false));
});
