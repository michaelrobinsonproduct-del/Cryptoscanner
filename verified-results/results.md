# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T05:01:30.192705+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45330150602
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f042e9a35d9274be9034297fd16dd512b043758e (atomic ledger/results publication)
**Ledger generation:** 1528 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.04991 | 67.575 | 54.709 | +0.50% | -0.43% | 6.88x | 7.6 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 25.146 | 65.007 | 72.200 | +2.85% | +0.02% | 0.27x | 5.6 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | AI/USD | 0.01614 | 63.003 | 69.897 | +5.97% | -0.50% | 0.56x | 6.2 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | WEAK 37/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | XRP/USD | 0.94942 | 62.207 | 61.683 | +1.07% | -0.41% | 1.26x | 1.6 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | WEAK 41/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.498e-06 | 55.266 | 61.141 | +2.22% | -0.43% | 0.63x | 8.6 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | BABY/USD | 0.00878 | 54.127 | 48.603 | +3.29% | -1.90% | 3.06x | 11.4 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 7 | XMR/USD | 489.82 | 50.763 | 56.182 | +0.78% | -0.66% | 0.79x | 8.6 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | DOT/USD | 0.6804 | 47.112 | 39.378 | +0.73% | -0.50% | 2.02x | 1.5 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 9 | NEAR/USD | 2.9967 | 44.571 | 55.633 | +0.52% | -0.48% | 0.13x | 6.0 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | NIGHT/USD | 0.04858 | 42.466 | 54.406 | +0.89% | -0.51% | 0.06x | 2.1 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | HBAR/USD | 0.05263 | 41.771 | 39.857 | +0.34% | -0.17% | 1.28x | 3.8 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | WEAK 31/100 | HIGH 61/100 | Do nothing | WATCH |
| 12 | UNI/USD | 4.869 | 41.405 | 52.046 | +0.64% | -0.38% | 0.13x | 5.5 | 2026-11-24T05:01:23.458181+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 72.200 | 25.146 | +0.02% | 0.27x |
| 2 | AI/USD | 69.897 | 0.01614 | -0.50% | 0.56x |
| 3 | XRP/USD | 61.683 | 0.94942 | -0.41% | 1.26x |
| 4 | PEPE/USD | 61.141 | 3.498e-06 | -0.43% | 0.63x |
| 5 | XMR/USD | 56.182 | 489.82 | -0.66% | 0.79x |
| 6 | NEAR/USD | 55.633 | 2.9967 | -0.48% | 0.13x |
| 7 | LINK/USD | 54.709 | 9.04991 | -0.43% | 6.88x |
| 8 | NIGHT/USD | 54.406 | 0.04858 | -0.51% | 0.06x |
| 9 | UNI/USD | 52.046 | 4.869 | -0.38% | 0.13x |
| 10 | BABY/USD | 48.603 | 0.00878 | -1.90% | 3.06x |
| 11 | HBAR/USD | 39.857 | 0.05263 | -0.17% | 1.28x |
| 12 | DOT/USD | 39.378 | 0.6804 | -0.50% | 2.02x |

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

- Persisted scans: 1528; predictions: 13069; observations: 925650.
- Matured sampled outcomes across 1/6/24/48h: 24403; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 136 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45330150602 · **Generation:** 1528 · **Legacy run:** 45330150602
**Main quote time:** 2026-11-24T05:01:30.192705+00:00 · **Legacy report time:** 2026-11-24T05:02:39.567784+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.04991 | 67.58 | -0.43% | 6.88x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD | 25.146 | 65.01 | +0.02% | 0.27x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 3 | AI/USD | 0.01614 | 63.00 | -0.50% | 0.56x | WEAK 37/100 | EXTREME 88/100 | Do nothing |
| 4 | XRP/USD | 0.94942 | 62.21 | -0.41% | 1.26x | WEAK 41/100 | HIGH 61/100 | Watch |
| 5 | PEPE/USD | 3.498e-06 | 55.27 | -0.43% | 0.63x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | BABY/USD | 0.00878 | 54.13 | -1.90% | 3.06x | MODERATE 52/100 | VERY_HIGH 83/100 | Do nothing |
| 7 | XMR/USD | 489.82 | 50.76 | -0.66% | 0.79x | WEAK 30/100 | HIGH 68/100 | Do nothing |
| 8 | DOT/USD | 0.6804 | 47.11 | -0.50% | 2.02x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 9 | NEAR/USD | 2.9967 | 44.57 | -0.48% | 0.13x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | NIGHT/USD | 0.04858 | 42.47 | -0.51% | 0.06x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | HBAR/USD | 0.05263 | 41.77 | -0.17% | 1.28x | WEAK 31/100 | HIGH 61/100 | Do nothing |
| 12 | UNI/USD | 4.869 | 41.40 | -0.38% | 0.13x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |

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
