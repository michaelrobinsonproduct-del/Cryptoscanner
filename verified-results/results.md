# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T16:52:15.233210+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45441608442
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 021c1f92dd8ffdf827e55f8706c528b0874a84f4 (atomic ledger/results publication)
**Ledger generation:** 1600 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | GBP/USD | 1.31033 | 73.677 | 58.765 | +0.54% | -0.02% | 3.87x | 0.1 | 2026-11-24T16:52:12.669015+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 24.742 | 73.029 | 59.774 | +1.20% | +0.14% | 2.25x | 7.3 | 2026-11-24T16:52:12.669015+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XMR/USD | 495.86 | 65.723 | 63.619 | +2.02% | +0.14% | 1.14x | 11.1 | 2026-11-24T16:52:12.669015+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.65e-05 | 64.888 | 55.943 | +6.97% | +0.67% | 1.56x | 40.9 | 2026-11-24T16:52:12.669015+00:00 | Not calibrated | MODERATE 62/100 | EXTREME 89/100 | Do nothing | WATCH |
| 5 | 2Z/USD | 0.01612 | 39.334 | 39.358 | +3.00% | +0.44% | 0.78x | 24.8 | 2026-11-24T16:52:12.669015+00:00 | Not calibrated | WEAK 40/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.3217 | 35.087 | 49.088 | +4.08% | -1.18% | 0.19x | 24.9 | 2026-11-24T16:52:12.669015+00:00 | Not calibrated | WEAK 13/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 63.619 | 495.86 | +0.14% | 1.14x |
| 2 | VVV/USD | 59.774 | 24.742 | +0.14% | 2.25x |
| 3 | GBP/USD | 58.765 | 1.31033 | -0.02% | 3.87x |
| 4 | LUNA/USD | 55.943 | 4.65e-05 | +0.67% | 1.56x |
| 5 | ICNT/USD | 49.088 | 0.3217 | -1.18% | 0.19x |
| 6 | 2Z/USD | 39.358 | 0.01612 | +0.44% | 0.78x |

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

- Persisted scans: 1600; predictions: 13755; observations: 969492.
- Matured sampled outcomes across 1/6/24/48h: 27501; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45441608442 · **Generation:** 1600 · **Legacy run:** 45441608442
**Main quote time:** 2026-11-24T16:52:15.233210+00:00 · **Legacy report time:** 2026-11-24T16:53:28.553751+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | GBP/USD | 1.31033 | 73.68 | -0.02% | 3.87x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD ⭐ | 24.742 | 73.03 | +0.14% | 2.25x | STRONG 92/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD ⭐ | 495.86 | 65.72 | +0.14% | 1.14x | MODERATE 63/100 | HIGH 68/100 | Watch |
| 4 | LUNA/USD ⭐ | 4.65e-05 | 64.89 | +0.67% | 1.56x | STRONG 72/100 | EXTREME 89/100 | Do nothing |
| 5 | 2Z/USD | 0.01612 | 39.33 | +0.44% | 0.78x | WEAK 40/100 | EXTREME 86/100 | Do nothing |
| 6 | ICNT/USD | 0.3217 | 35.09 | -1.18% | 0.19x | WEAK 13/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.65e-05 | 65.14 | +0.67% | 1.56x | 1447 | STRONG 83/100 | VERY_HIGH 73/100 | Watch |
| 2 | XMR/USD ⭐ | 495.41 | 61.17 | +0.14% | 1.14x | 9302 | MODERATE 66/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD ⭐ | 24.682 | 53.93 | +0.14% | 2.25x | 14911 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, XMR/USD, LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
