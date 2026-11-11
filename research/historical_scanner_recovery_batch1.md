# Historical scanner recovery — Batch 1

Status: evidence recovery complete; exact September production implementation not recovered. Research only; no production scoring changes.

## Chronology (from historical conversation records)

- 2026-09-06: MET surfaced as EARLY WATCH at about $0.213; reached about $0.2864 by Sep 11 (~34.5%). Attribution to a specific scheduled scanner unverified.
- 2026-09-07: KAS surfaced as SHADOW at about $0.030; reached about $0.0393 by Sep 10 (~31%). Attribution to a specific scheduled scanner unverified.
- 2026-09-20: after a PWT miss, :45 production scanner described as v2.2; off-Kraken activity triggered PRECURSOR WATCH even when Kraken was dormant; poor Kraken liquidity blocked trade approval but not discovery. Discussion says all four :00/:15/:30/:45 scans received analogous separation.
- 2026-09-22: :15 scanner described as v6.3; tracked cross-venue OI/participation acceleration and avoided chasing extended moves.
- 2026-09-24 02:29 UTC: review of several 10–40% successes including MET and KAS.
- 2026-09-24 02:31 UTC: :15 scanner upgraded to v7.0 outcome-learning precursor engine; v7.1 followed. These upgrades cannot explain signals generated Sep 6–7.
- 2026-09-24 21:37 UTC: :45 v2.2 described as inactivity/compression → first abnormal participation within ~5% extension → second independent channel acceleration; this retrospective description is not proof those rules existed Sep 6–7.

## Recovered artifacts

- Library file `kraken_simple_scanner.py` (created Oct 11) uses hourly closed candles, 1h and 6h momentum (25 points each), relative volume (20), acceleration (15), and a 24h extension penalty (up to 20). **This artifact postdates the September wins and must not be presented as the exact successful scanner.**
- Current GitHub `simple_scanner/scan.py` on `manual-scan-isolation-20261015` filters 24h move 0.25–12%, spread <=45bps, notional >=$100k before deeper 5m OHLC screening; this is a later implementation, not evidence of September scoring.
- GitHub branches searched: no specifically named September scanner snapshot found. Search is not proof no historical source exists.

## Findings and confidence

1. HIGH: MET/KAS reported as early surfaced 20%+ moves in early September; specific task attribution unverified.
2. HIGH: September 24 v7.0 came *after* those signals, so v7.0 was not their original generator.
3. MEDIUM: pre-v7 :15 and other scheduled scans used cross-venue/precursor discovery logic by Sep 20–22; cannot backdate this confidently to Sep 6.
4. LOW: Oct 11 simple scanner's scoring explains September results; chronology contradicts a direct attribution.

## Next verification

Find archived Sept 6–7 alert outputs, scheduled task prompts, logs, or exports to identify actual generating task/version and precise signal timestamps. Separate early watch from executable recommendations. Then evaluate forward gains and missed alerts with equal candidate budgets and no hindsight.

## Safety

No code, task schedules, scanner rankings, live weights, deployment, storage, or trading behavior modified in this batch.
