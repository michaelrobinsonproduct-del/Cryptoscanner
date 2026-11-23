# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T15:11:43.933397+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45202048230
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4a25d4c0e89f5ddd0d5f95357fb3af6821607546 (atomic ledger/results publication)
**Ledger generation:** 1446 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.92 | 104.231 | 95.154 | +6.87% | -0.02% | 1.92x | 7.0 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SUI/USD | 0.7146 | 95.380 | 97.901 | +8.98% | +0.22% | 0.64x | 4.2 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 67.58 | 94.093 | 97.780 | +7.17% | +0.25% | 0.51x | 4.4 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XLM/USD | 0.135499 | 93.138 | 95.579 | +6.25% | +0.66% | 0.43x | 6.3 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ADA/USD | 0.15365 | 92.967 | 96.295 | +6.26% | +0.32% | 0.51x | 5.0 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XRP/USD | 0.99259 | 92.749 | 98.942 | +7.01% | +0.05% | 0.35x | 2.1 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ZEC/USD | 865.51 | 91.797 | 94.227 | +8.53% | +0.98% | 0.26x | 11.5 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | SOL/USD | 75.98 | 89.434 | 97.367 | +7.57% | -0.54% | 0.48x | 5.3 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0586795 | 88.261 | 95.343 | +6.14% | -0.34% | 0.46x | 5.3 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.1553 | 88.124 | 88.779 | +5.82% | -0.81% | 1.34x | 14.0 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | MODERATE 59/100 | HIGH 67/100 | Watch | WATCH |
| 11 | UNI/USD | 5.125 | 83.289 | 92.981 | +9.48% | -0.93% | 0.50x | 5.5 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | INJ/USD | 6.864 | 82.779 | 89.730 | +10.21% | -0.03% | 0.32x | 10.2 | 2026-11-23T15:11:37.703911+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 98.942 | 0.99259 | +0.05% | 0.35x |
| 2 | SUI/USD | 97.901 | 0.7146 | +0.22% | 0.64x |
| 3 | HYPE/USD | 97.780 | 67.58 | +0.25% | 0.51x |
| 4 | SOL/USD | 97.367 | 75.98 | -0.54% | 0.48x |
| 5 | ADA/USD | 96.295 | 0.15365 | +0.32% | 0.51x |
| 6 | XLM/USD | 95.579 | 0.135499 | +0.66% | 0.43x |
| 7 | XDG/USD | 95.343 | 0.0586795 | -0.34% | 0.46x |
| 8 | LTC/USD | 95.154 | 42.92 | -0.02% | 1.92x |
| 9 | ZEC/USD | 94.227 | 865.51 | +0.98% | 0.26x |
| 10 | UNI/USD | 92.981 | 5.125 | -0.93% | 0.50x |
| 11 | INJ/USD | 89.730 | 6.864 | -0.03% | 0.32x |
| 12 | NEAR/USD | 88.779 | 3.1553 | -0.81% | 1.34x |

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

- Persisted scans: 1446; predictions: 12119; observations: 875716.
- Matured sampled outcomes across 1/6/24/48h: 20716; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45202048230 · **Generation:** 1446 · **Legacy run:** 45202048230
**Main quote time:** 2026-11-23T15:11:43.933397+00:00 · **Legacy report time:** 2026-11-23T15:12:53.237486+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 42.92 | 104.23 | -0.02% | 1.92x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | SUI/USD | 0.7146 | 95.38 | +0.22% | 0.64x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD | 67.58 | 94.09 | +0.25% | 0.51x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 4 | XLM/USD | 0.135499 | 93.14 | +0.66% | 0.43x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 5 | ADA/USD | 0.15365 | 92.97 | +0.32% | 0.51x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 6 | XRP/USD | 0.99259 | 92.75 | +0.05% | 0.35x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 7 | ZEC/USD | 865.51 | 91.80 | +0.98% | 0.26x | STRONG 71/100 | VERY_HIGH 76/100 | Watch |
| 8 | SOL/USD | 75.98 | 89.43 | -0.54% | 0.48x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 9 | XDG/USD | 0.0586795 | 88.26 | -0.34% | 0.46x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 10 | NEAR/USD | 3.1553 | 88.12 | -0.81% | 1.34x | MODERATE 59/100 | HIGH 67/100 | Watch |
| 11 | UNI/USD | 5.125 | 83.29 | -0.93% | 0.50x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 12 | INJ/USD | 6.864 | 82.78 | -0.03% | 0.32x | WEAK 41/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
