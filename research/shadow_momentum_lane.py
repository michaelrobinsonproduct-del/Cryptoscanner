"""Offline shadow-lane comparison from independently captured Kraken ticker data.

This is eligibility discovery, NOT a backtest, early-entry signal, or trading approval.
No production scanner or network calls.
"""
import argparse
import json
from collections import Counter
from research.discovery_gate_attribution import classify

def evaluate(snapshot):
    records=snapshot["records"]
    reasons={p:classify(r) for p,r in records.items()}
    baseline=sorted(p for p,r in reasons.items() if r==["passes_initial_gates"])
    shadow=sorted(p for p,r in reasons.items() if r==["daily_move_below_0_25pct"])
    # Enforce no relaxation of spread/notional/validity gates in shadow lane.
    assert not set(baseline)&set(shadow)
    assert all(reasons[p]==["daily_move_below_0_25pct"] for p in shadow)
    assert len(records)>=max(50,int(snapshot["universe"]*.8))
    return {"mode":"OFFLINE_SHADOW_ONLY","captured_at":snapshot["captured_at"],
      "universe":snapshot["universe"],"matched":len(records),
      "baseline_pass":len(baseline),"shadow_momentum_only":len(shadow),
      "combined_pool":len(baseline)+len(shadow),
      "baseline_pairs":baseline,"shadow_pairs":shadow,
      "spread_limit_unchanged":True,"notional_limit_unchanged":True,
      "ohlc_signals_tested":False,"forward_returns_tested":False,
      "trade_approval":False,
      "caveat":"Snapshot eligibility only; no evidence yet of predictive power or safe OHLC request budget."}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("snapshot")
    p.add_argument("--output",default="discovery-shadow-lane.json")
    args=p.parse_args()
    with open(args.snapshot,encoding="utf-8") as f: snapshot=json.load(f)
    result=evaluate(snapshot)
    with open(args.output,"w",encoding="utf-8") as f:json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k not in ("baseline_pairs","shadow_pairs")},sort_keys=True))
