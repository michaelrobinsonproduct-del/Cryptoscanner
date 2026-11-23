"""Read-only old/new comparison on identical Kraken payloads and clock values."""
import collections
import datetime as dt
import json
import subprocess
from unittest.mock import patch
from . import legacy_shadow as legacy

def main():
    original = legacy._closed_features
    import types
    old = types.ModuleType("paper_pov.legacy_shadow_before")
    old.__package__ = "paper_pov"
    exec(compile(subprocess.check_output(["git", "show", "b271b90a2cae9e5307600070ce7d0e510fe68996:paper_pov/legacy_shadow.py"], text=True), "legacy_before", "exec"), old.__dict__)
    evidence = []
    def compare(payload, pair, now):
        try:
            old._closed_features(payload, pair, now)
            before = "VALID"
        except ValueError as exc:
            before = str(exc)
        try:
            result = original(payload, pair, now)
        except ValueError as exc:
            evidence.append({"pair": pair, "before": before, "after": str(exc)})
            raise
        rows = payload[pair][:-1][-13:]
        evidence.append({"pair": pair,
                         "before": before,
                         "after": "VALID",
                         "explicit_zero_trade_rows": sum(float(row[7]) == 0 for row in rows)})
        return result
    with patch.object(legacy, "_closed_features", compare):
        report = legacy.scan(run_id="1", source_sha="a"*40, trigger_paper_run_id="2")
    assert len(evidence) == report["ohlc_attempts"]
    before = collections.Counter(x["before"] for x in evidence)
    after = collections.Counter(x["after"] for x in evidence)
    print(json.dumps({"as_of": dt.datetime.now(dt.timezone.utc).isoformat(),
                      "attempts": len(evidence), "before": before, "after": after,
                      "recovered": sum(x["before"] != "VALID" and x["after"] == "VALID" for x in evidence),
                      "evidence": evidence}, sort_keys=True))
    assert after["VALID"] >= before["VALID"]
    if not any(x.get("explicit_zero_trade_rows", 0) for x in evidence):
        print("NO_LIVE_ZERO_TRADE_EXAMPLE_OBSERVED")

if __name__ == "__main__":
    main()
