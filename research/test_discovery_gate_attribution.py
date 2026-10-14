"""Deterministic parity tests for live scanner eligibility gates."""
from research.discovery_gate_attribution import classify,summarize
BASE={"last":10,"bid":9.99,"ask":10.01,"open":9.8,"volume24":15000}
def test():
    assert classify(BASE)==["passes_initial_gates"]
    def change(**kwargs):return dict(BASE,**kwargs)
    assert classify(change(open=10.1))==["daily_move_below_0_25pct"]
    assert classify(change(open=8))==["daily_move_above_12pct"]
    assert classify(change(bid=9.9,ask=10.1))==["spread_above_45bps"]
    assert classify(change(volume24=100))==["notional_below_100k"]
    assert classify(change(last=float("nan")))==["invalid_market_data"]
    assert classify(change(ask=9.5))==["invalid_market_data"]
    assert classify(change(open=10.1,volume24=100))==["daily_move_below_0_25pct","notional_below_100k"]
    data={"pass":BASE,"reject":change(open=10.1,volume24=100)}
    before=repr(data)
    result=summarize(data)
    assert result["reason_counts"]["passes_initial_gates"]==1
    assert result["reason_counts"]["notional_below_100k"]==1
    assert repr(data)==before
    print("PASS: threshold parity, multiple rejection reasons, invalid data, immutable inputs")
if __name__=="__main__":test()
