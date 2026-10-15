"""Explicitly invoked, research-only ticker feature capture pipeline.

Caller supplies an isolated storage path and already-fetched ticker data.
No network access, scheduler, live ranking or production database integration.
"""
from simple_scanner.ticker_feature_capture import extract_features
from simple_scanner.feature_sidecar import persist_features

def capture_to_sidecar(eligible, ticker, *, observed_at, path,
                       minimum_coverage_pct=80, keep_runs=96):
    if type(minimum_coverage_pct) not in (int,float) or not 0<minimum_coverage_pct<=100:
        raise ValueError("invalid coverage threshold")
    extracted=extract_features(eligible,ticker,observed_at=observed_at)
    if not eligible or extracted["coverage_pct"]<minimum_coverage_pct:
        return {"status":"REJECTED_INCOMPLETE_COVERAGE",
                "coverage_pct":extracted["coverage_pct"],
                "stored":False,"production_modified":False,"buy_approved":False}
    result=persist_features(path,extracted,observed_at=observed_at,keep_runs=keep_runs)
    return {"status":"STORED_RESEARCH_ONLY","coverage_pct":extracted["coverage_pct"],
            "stored":True,"rows":result["rows"],"production_modified":False,
            "buy_approved":False}
