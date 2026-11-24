# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T18:37:33.962277+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45461008776
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** deef4e19e2148dda34bba94eaf21459c4b721cbf (atomic ledger/results publication)
**Ledger generation:** 1611 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 507.35 | 73.098 | 74.855 | +4.39% | +0.10% | 0.78x | 21.7 | 2026-11-24T18:37:29.250134+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31165 | 62.819 | 59.474 | +0.64% | +0.02% | 1.32x | 0.1 | 2026-11-24T18:37:29.250134+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 3 | VVV/USD | 24.961 | 57.209 | 65.485 | +2.10% | +0.02% | 0.16x | 8.4 | 2026-11-24T18:37:29.250134+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.763e-05 | 50.731 | 54.705 | +9.57% | +0.36% | 0.42x | 44.3 | 2026-11-24T18:37:29.250134+00:00 | Not calibrated | WEAK 40/100 | EXTREME 97/100 | Do nothing | WATCH |
| 5 | NIGHT/USD | 0.0488 | 45.592 | 47.702 | +1.35% | +0.45% | 0.56x | 6.1 | 2026-11-24T18:37:29.250134+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.433e-06 | 42.060 | 43.456 | +0.32% | -0.06% | 0.89x | 5.8 | 2026-11-24T18:37:29.250134+00:00 | Not calibrated | WEAK 26/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | AUD/USD | 0.6647 | 41.440 | 44.521 | +0.32% | +0.03% | 0.68x | 1.4 | 2026-11-24T18:37:29.250134+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | INX/USD | 0.003911 | 37.286 | 24.806 | +0.33% | +0.57% | 1.97x | 17.9 | 2026-11-24T18:37:29.250134+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | ZEUS/USD | 0.00461 | 36.295 | 46.389 | +5.25% | -0.86% | 0.42x | 43.5 | 2026-11-24T18:37:29.250134+00:00 | Not calibrated | WEAK 8/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 74.855 | 507.35 | +0.10% | 0.78x |
| 2 | VVV/USD | 65.485 | 24.961 | +0.02% | 0.16x |
| 3 | GBP/USD | 59.474 | 1.31165 | +0.02% | 1.32x |
| 4 | LUNA/USD | 54.705 | 4.763e-05 | +0.36% | 0.42x |
| 5 | NIGHT/USD | 47.702 | 0.0488 | +0.45% | 0.56x |
| 6 | ZEUS/USD | 46.389 | 0.00461 | -0.86% | 0.42x |
| 7 | AUD/USD | 44.521 | 0.6647 | +0.03% | 0.68x |
| 8 | PEPE/USD | 43.456 | 3.433e-06 | -0.06% | 0.89x |
| 9 | INX/USD | 24.806 | 0.003911 | +0.57% | 1.97x |

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

- Persisted scans: 1611; predictions: 13839; observations: 976191.
- Matured sampled outcomes across 1/6/24/48h: 27946; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45461008776 · **Generation:** 1611 · **Legacy run:** 45461008776
**Main quote time:** 2026-11-24T18:37:33.962277+00:00 · **Legacy report time:** 2026-11-24T18:38:36.392623+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 507.35 | 73.10 | +0.10% | 0.78x | MODERATE 47/100 | VERY_HIGH 74/100 | Watch |
| 2 | GBP/USD | 1.31165 | 62.82 | +0.02% | 1.32x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD | 24.961 | 57.21 | +0.02% | 0.16x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 4 | LUNA/USD | 4.763e-05 | 50.73 | +0.36% | 0.42x | WEAK 40/100 | EXTREME 97/100 | Do nothing |
| 5 | NIGHT/USD | 0.0488 | 45.59 | +0.45% | 0.56x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 6 | PEPE/USD | 3.433e-06 | 42.06 | -0.06% | 0.89x | WEAK 26/100 | HIGH 68/100 | Do nothing |
| 7 | AUD/USD | 0.6647 | 41.44 | +0.03% | 0.68x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |
| 8 | INX/USD ⭐ | 0.003911 | 37.29 | +0.57% | 1.97x | MODERATE 69/100 | VERY_HIGH 73/100 | Watch |
| 9 | ZEUS/USD | 0.00461 | 36.30 | -0.86% | 0.42x | WEAK 8/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INX/USD ⭐ | 0.003911 | 32.41 | +0.57% | 1.97x | 4302 | MODERATE 61/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** INX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
