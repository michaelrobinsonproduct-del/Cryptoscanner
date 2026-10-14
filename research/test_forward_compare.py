"""Deterministic tests of forward comparison and stale observation rejection."""
from research.forward_compare import compare
def snap(t,prices):
    return {"captured_at":t,"universe":50,"records":prices}
def row(last,open,volume=15000,bid=None,ask=None):
    return {"last":last,"open":open,"bid":last*.999 if bid is None else bid,
        "ask":last*1.001 if ask is None else ask,"volume24":volume}
def test():
    old=snap("2026-10-14T00:00:00+00:00",{"BASE":row(10,9.8),"EARLY":row(10,10.1),"THIN":row(10,10.1,volume=10)})
    old["records"].update({f"BAD_{i}":row(-1,-1) for i in range(47)})
    new=snap("2026-10-14T00:30:00+00:00",{"BASE":row(10.2,9.8),"EARLY":row(10.6,10.1),"THIN":row(12,10.1)})
    before=repr(old)
    result=compare({"snapshot":old},new)
    assert result["baseline_summary"]["matched"]==1,result
    assert result["shadow_summary"]["matched"]==1,result
    assert result["shadow_summary"]["breakouts_5pct"]==1,result
    assert result["baseline_summary"]["breakouts_5pct"]==0,result
    assert repr(old)==before
    try:compare({"snapshot":old},snap("2026-10-14T03:00:00+00:00",new["records"]))
    except ValueError:pass
    else:raise AssertionError("Stale comparison must be rejected")
    print("PASS: forward returns, market exclusions, time guard, immutable inputs")
if __name__=="__main__":test()
