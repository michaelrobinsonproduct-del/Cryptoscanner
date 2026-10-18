# Historical Scanner Recovery — Batch 4 verification

Status: deployment and build tests PASS; new-version live scan and comparative efficacy PENDING.

- Batch 3 initial build failed on malformed literal backslash-n characters in historical_precursor.py. Corrected in commit dd7ead06af6658175da5f737e0601525b1796cec.
- Railway deployment 378ea241-547f-4651-ab8b-24ce2ee1d581 succeeded for that commit.
- Build executed compileall and unittest discovery: 101 tests, OK.
- New daemon startup recorded at 2026-10-18T00:53:12Z.
- Earlier deployment scan at 00:45Z verified cron, shadow, and DEX processing; this is NOT proof of a new-commit scan.
- No new-commit completed scan in inspected deployment logs at verification time. Do not claim the challenger produced live results yet.
- New challenger remains shadow-only, with no live scoring changes, buy approval or promotion.
- Current shadow report labels equal-budget prospective comparison as pending. No verified 20/50/100/500 percent multi-day improvement data.

Next: wait for the first completed scheduled scan on new deployment; inspect SHADOW_LEARNING historical_precursor output, SCAN_EXECUTION_VERIFIED, DEX status and storage. If any fail, diagnose and correct in one batch. Accumulate time-separated forward observations and compare top 12 against top 12; do not promote until independently validated and rollback reviewed.
