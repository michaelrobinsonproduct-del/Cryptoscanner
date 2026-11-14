# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T01:17:45.161962+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43539668603
**Source SHA:** d42e6419d43c62fa1d507fe5368a5182b699f713
**Previous ledger commit:** 60e4131747263fe02224ada8b4183f26a552e213 (atomic ledger/results publication)
**Ledger generation:** 375 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 215.5397 | 45.617 | 54.299 | +0.42% | -0.34% | 0.30x | 7.2 | 2026-11-14T01:17:38.203186+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 2 | RENDER/USD | 1.537 | 45.099 | 30.424 | +0.26% | -0.07% | 10.68x | 13.0 | 2026-11-14T01:17:38.203186+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | BMT/USD | 0.02336 | 34.556 | 36.537 | +3.87% | +0.65% | 0.48x | 42.8 | 2026-11-14T01:17:38.203186+00:00 | Not calibrated | WEAK 32/100 | EXTREME 100/100 | Do nothing | WATCH |
| 4 | VVV/USD | 19.054 | 31.723 | 40.313 | +0.30% | -0.07% | 0.18x | 7.4 | 2026-11-14T01:17:38.203186+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | MON/USD | 0.01681 | 27.136 | 29.066 | +0.36% | -0.12% | 0.87x | 11.9 | 2026-11-14T01:17:38.203186+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 54.299 | 215.5397 | -0.34% | 0.30x |
| 2 | VVV/USD | 40.313 | 19.054 | -0.07% | 0.18x |
| 3 | BMT/USD | 36.537 | 0.02336 | +0.65% | 0.48x |
| 4 | RENDER/USD | 30.424 | 1.537 | -0.07% | 10.68x |
| 5 | MON/USD | 29.066 | 0.01681 | -0.12% | 0.87x |

The baseline ordering is over this same confirmed WATCH pool, not an independent full-market baseline scan.
The separate legacy-inspired scanner publishes its own WATCH signals in a later, read-only GitHub artifact linked by this paper run ID.

**30%+ in 48h probability:** NOT CALIBRATED. The separate signal-confidence index (0–100) expresses current setup strength, NOT odds of a gain. Risk varies by spread, momentum and volume; every candidate remains speculative. The action is a research consideration, not an executed or authorized trade. A more substantial entry requires independently qualified held-out calibration.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 375; predictions: 3451; observations: 225580.
- Matured sampled outcomes across 1/6/24/48h: 2951; gap abstentions: 9957. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
