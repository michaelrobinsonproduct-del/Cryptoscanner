# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T21:55:25.355668+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43645317402
**Source SHA:** 8840e08661f263d95023082e1f03243120115b28
**Previous ledger commit:** 546b7eb5efb542d28bf92abdd7bb88199123c2bb (atomic ledger/results publication)
**Ledger generation:** 417 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 1s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 3.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PIEVERSE/USD | 1.8132 | 52.822 | 64.013 | +10.68% | -0.35% | 0.06x | 28.7 | 2026-11-14T21:55:24.497964+00:00 | Not calibrated | WEAK 21/100 | EXTREME 93/100 | Do nothing | WATCH |
| 2 | CAP/USD | 0.110285 | 51.365 | 53.996 | +3.04% | +0.47% | 0.50x | 7.8 | 2026-11-14T21:55:24.497964+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.04501 | 15.323 | 19.578 | +0.38% | -0.46% | 0.81x | 28.9 | 2026-11-14T21:55:24.497964+00:00 | Not calibrated | WEAK 3/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 64.013 | 1.8132 | -0.35% | 0.06x |
| 2 | CAP/USD | 53.996 | 0.110285 | +0.47% | 0.50x |
| 3 | MEGA/USD | 19.578 | 0.04501 | -0.46% | 0.81x |

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

- Persisted scans: 417; predictions: 3595; observations: 251045.
- Matured sampled outcomes across 1/6/24/48h: 3157; gap abstentions: 10574. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 0; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
