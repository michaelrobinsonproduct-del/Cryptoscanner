"""Conservative paper-only entry research. Never authorizes real trades."""
import datetime as dt
import json
from pathlib import Path

def assess(report, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    stamp = dt.datetime.fromisoformat(report["completed_at"].replace("Z", "+00:00"))
    age = (now-stamp).total_seconds()
    healthy = (report.get("health") == "COMPLETE" and report.get("failures") == 0
               and report.get("scanned") == report.get("universe")
               and 0 <= age <= 900)
    output = []
    for c in report.get("watch", []):
        reasons = []
        if not healthy: reasons.append("scan_unhealthy_or_stale")
        if c.get("signal_state") != "DOUBLE_CONFIRMED_RESEARCH_WATCH": reasons.append("not_double_confirmed")
        if c.get("continuity_state") == "DOWNGRADED_PRICE_OR_LIQUIDITY": reasons.append("deteriorating")
        if c.get("continuity_state") == "NEW_OR_UNVERIFIED": reasons.append("continuity_unverified")
        if not (0 < c.get("spread_bps", 1e9) <= 10): reasons.append("spread")
        if not (1 <= c.get("move24_pct", -1) <= 12): reasons.append("momentum")
        if c.get("score", 0) < 85: reasons.append("score")
        output.append({"pair":c["pair"],"status":"PAPER_ELIGIBLE" if not reasons else "RESEARCH_ONLY",
                       "reasons":reasons,"entry_approved":False,"real_trade_approved":False,
                       "paper_reference_price":c.get("price")})
    return {"mode":"PAPER_ONLY","scan_completed_at":report["completed_at"],
            "generated_at":now.isoformat(),"scan_healthy_and_fresh":healthy,
            "candidates":output,"real_trade_approvals":0,
            "note":"Paper eligibility is a hypothesis, not a validated profitable entry or buy signal."}

if __name__ == "__main__":
    report=json.loads(Path("rebuild_v2/output/latest.json").read_text())
    result=assess(report)
    Path("rebuild_v2/output/paper_entries.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"paper_eligible":sum(c["status"]=="PAPER_ELIGIBLE" for c in result["candidates"]),"real_trade_approvals":0}))
