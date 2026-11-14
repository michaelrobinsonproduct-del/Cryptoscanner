# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T11:55:49.339899+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43592130061
**Source SHA:** 67728a7c03aae3088f31b72a3eaa363009058226
**Previous ledger commit:** 02b0f08ed3118bcad1185bd9f607d7c74eb0d013 (atomic ledger/results publication)
**Ledger generation:** 397 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PIEVERSE/USD | 1.7756 | 66.155 | 68.460 | +8.39% | +0.07% | 0.73x | 16.4 | 2026-11-14T11:55:45.229089+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | NIGHT/USD | 0.04722 | 63.218 | 51.893 | +0.73% | +0.53% | 1.87x | 2.1 | 2026-11-14T11:55:45.229089+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 3 | CAP/USD | 0.108088 | 54.020 | 41.597 | +0.99% | -0.52% | 3.35x | 3.0 | 2026-11-14T11:55:45.229089+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 4 | XMR/USD | 534.9 | 53.282 | 50.535 | +1.12% | +0.17% | 1.19x | 24.7 | 2026-11-14T11:55:45.229089+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | BMT/USD | 0.02309 | 39.795 | 32.282 | +2.67% | +1.18% | 1.16x | 34.7 | 2026-11-14T11:55:45.229089+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | TRX/USD | 0.312821 | 36.270 | 39.343 | +0.34% | +0.09% | 0.65x | 0.0 | 2026-11-14T11:55:45.229089+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | TON/USD | 1.097 | 29.396 | 33.297 | +0.55% | -0.27% | 0.75x | 18.2 | 2026-11-14T11:55:45.229089+00:00 | Not calibrated | WEAK 15/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 68.460 | 1.7756 | +0.07% | 0.73x |
| 2 | NIGHT/USD | 51.893 | 0.04722 | +0.53% | 1.87x |
| 3 | XMR/USD | 50.535 | 534.9 | +0.17% | 1.19x |
| 4 | CAP/USD | 41.597 | 0.108088 | -0.52% | 3.35x |
| 5 | TRX/USD | 39.343 | 0.312821 | +0.09% | 0.65x |
| 6 | TON/USD | 33.297 | 1.097 | -0.27% | 0.75x |
| 7 | BMT/USD | 32.282 | 0.02309 | +1.18% | 1.16x |

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

- Persisted scans: 397; predictions: 3535; observations: 238924.
- Matured sampled outcomes across 1/6/24/48h: 3117; gap abstentions: 10245. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
