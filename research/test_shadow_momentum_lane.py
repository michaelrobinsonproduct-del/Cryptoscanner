"""Regression checks: shadow discovery must preserve existing market safety gates."""
from research.shadow_momentum_lane import evaluate
def test():
    base={"last":10,"bid":9.99,"ask":10.01,"open":9.8,"volume24":15000}
    def row(**kwargs):return dict(base,**kwargs)
    snapshot={"captured_at":"2026-10-14T00:00:00+00:00","universe":5,
      "records":{"PASS":base,"EARLY":row(open=10.1),"WIDE":row(open=10.1,bid=9.8,ask=10.2),
        "THIN":row(open=10.1,volume24=100),"INVALID":row(last=-1)}}
    before=repr(snapshot)
    r=evaluate(snapshot)
    assert r["baseline_pairs"]==["PASS"],r
    assert r["shadow_pairs"]==["EARLY"],r
    assert r["combined_pool"]==2,r
    assert not r["trade_approval"] and not r["forward_returns_tested"]
    assert repr(snapshot)==before
    print("PASS: shadow lane excludes illiquid, wide-spread, invalid markets; no approvals or input mutation")
if __name__=="__main__":test()
