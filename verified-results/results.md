# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T07:21:27.847253+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45347118929
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d6d94335636449b366171de7cc35730c6d12e116 (atomic ledger/results publication)
**Ledger generation:** 1543 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.44 | 91.497 | 79.273 | +4.06% | -0.56% | 2.72x | 8.3 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.542e-06 | 80.797 | 73.843 | +3.51% | +0.14% | 1.62x | 2.8 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.23 | 72.502 | 59.931 | +0.93% | -0.22% | 2.37x | 3.1 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0193 | 72.004 | 61.959 | +1.28% | -0.20% | 2.11x | 4.0 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04965 | 69.650 | 69.363 | +3.12% | +0.65% | 0.70x | 4.0 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XRP/USD | 0.9436 | 68.244 | 58.084 | +0.45% | -0.52% | 2.28x | 0.1 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 7 | INX/USD | 0.004123 | 63.548 | 57.456 | +5.77% | +0.94% | 1.14x | 29.2 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | MODERATE 57/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | DBR/USD | 0.01486 | 60.666 | 59.047 | +10.73% | +0.88% | 0.72x | 33.5 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | XMR/USD | 496.79 | 60.237 | 66.986 | +2.22% | -0.14% | 0.40x | 7.1 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | BABY/USD | 0.00895 | 56.005 | 63.266 | +5.29% | +0.22% | 0.16x | 11.2 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | PENGU/USD | 0.004461 | 54.865 | 40.536 | +0.86% | -0.13% | 2.53x | 2.2 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 12 | TIA/USD | 0.3429 | 53.866 | 45.307 | +2.11% | +0.26% | 1.72x | 2.9 | 2026-11-24T07:21:19.980970+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.273 | 25.44 | -0.56% | 2.72x |
| 2 | PEPE/USD | 73.843 | 3.542e-06 | +0.14% | 1.62x |
| 3 | NIGHT/USD | 69.363 | 0.04965 | +0.65% | 0.70x |
| 4 | XMR/USD | 66.986 | 496.79 | -0.14% | 0.40x |
| 5 | BABY/USD | 63.266 | 0.00895 | +0.22% | 0.16x |
| 6 | NEAR/USD | 61.959 | 3.0193 | -0.20% | 2.11x |
| 7 | HYPE/USD | 59.931 | 64.23 | -0.22% | 2.37x |
| 8 | DBR/USD | 59.047 | 0.01486 | +0.88% | 0.72x |
| 9 | XRP/USD | 58.084 | 0.9436 | -0.52% | 2.28x |
| 10 | INX/USD | 57.456 | 0.004123 | +0.94% | 1.14x |
| 11 | TIA/USD | 45.307 | 0.3429 | +0.26% | 1.72x |
| 12 | PENGU/USD | 40.536 | 0.004461 | -0.13% | 2.53x |

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

- Persisted scans: 1543; predictions: 13249; observations: 934785.
- Matured sampled outcomes across 1/6/24/48h: 24926; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45347118929 · **Generation:** 1543 · **Legacy run:** 45347118929
**Main quote time:** 2026-11-24T07:21:27.847253+00:00 · **Legacy report time:** 2026-11-24T07:22:13.954277+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.44 | 91.50 | -0.56% | 2.72x | STRONG 76/100 | HIGH 61/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.542e-06 | 80.80 | +0.14% | 1.62x | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD | 64.23 | 72.50 | -0.22% | 2.37x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | NEAR/USD | 3.0193 | 72.00 | -0.20% | 2.11x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD | 0.04965 | 69.65 | +0.65% | 0.70x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 6 | XRP/USD | 0.9436 | 68.24 | -0.52% | 2.28x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 7 | INX/USD ⭐ | 0.004123 | 63.55 | +0.94% | 1.14x | MODERATE 67/100 | EXTREME 86/100 | Do nothing |
| 8 | DBR/USD | 0.01486 | 60.67 | +0.88% | 0.72x | MODERATE 50/100 | EXTREME 94/100 | Do nothing |
| 9 | XMR/USD | 496.79 | 60.24 | -0.14% | 0.40x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | BABY/USD | 0.00895 | 56.01 | +0.22% | 0.16x | MODERATE 53/100 | VERY_HIGH 81/100 | Watch |
| 11 | PENGU/USD | 0.004461 | 54.86 | -0.13% | 2.53x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 12 | TIA/USD | 0.3429 | 53.87 | +0.26% | 1.72x | STRONG 72/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.544e-06 | 83.84 | +0.14% | 1.62x | 9171 | STRONG 87/100 | HIGH 55/100 | Watch |
| 2 | INX/USD ⭐ | 0.004123 | 74.36 | +0.94% | 1.14x | 3798 | STRONG 72/100 | EXTREME 86/100 | Do nothing |

**Same-run overlap:** PEPE/USD, INX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
