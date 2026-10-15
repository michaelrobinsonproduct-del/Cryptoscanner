"""Durable DEX discovery circuit breaker; never affects Kraken scan or approves buys."""
import datetime as dt
import json
import os
from pathlib import Path
from simple_scanner import dex

COOLDOWN_HOURS=3

def run():
    directory=Path(os.getenv("SIMPLE_SCANNER_DATA_DIR","simple_scanner/output"))
    directory.mkdir(parents=True,exist_ok=True)
    state=directory/"dex_circuit.json"
    now=dt.datetime.now(dt.timezone.utc)
    if state.exists():
        try:
            previous=json.loads(state.read_text())
            blocked=dt.datetime.fromisoformat(previous["blocked_at"])
            if now-blocked<dt.timedelta(hours=COOLDOWN_HOURS):
                print("DEX_CIRCUIT_OPEN "+json.dumps({"blocked_at":blocked.isoformat(),"retry_after":(blocked+dt.timedelta(hours=COOLDOWN_HOURS)).isoformat(),"buy_approved":False}),flush=True)
                return
        except (ValueError,TypeError,KeyError):
            pass
    try:
        dex.main()
    except Exception as exc:
        state.write_text(json.dumps({"blocked_at":now.isoformat(),"error":str(exc)}))
        print("DEX_CIRCUIT_TRIPPED "+json.dumps({"error":str(exc),"retry_after":(now+dt.timedelta(hours=COOLDOWN_HOURS)).isoformat(),"buy_approved":False}),flush=True)
    else:
        if state.exists(): state.unlink()

if __name__=="__main__":run()
