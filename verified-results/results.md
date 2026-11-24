# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T17:22:23.943209+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45447304793
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 528d5e9d750b467c288bf94567d71c7abd08ffc0 (atomic ledger/results publication)
**Ledger generation:** 1603 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.074 | 79.426 | 70.927 | +2.56% | +2.06% | 0.82x | 4.0 | 2026-11-24T17:22:20.373378+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.708e-05 | 67.030 | 63.611 | +8.30% | +1.25% | 0.72x | 25.6 | 2026-11-24T17:22:20.373378+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | XMR/USD | 497.95 | 65.242 | 68.766 | +2.45% | +0.55% | 0.37x | 6.8 | 2026-11-24T17:22:20.373378+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ZEUS/USD | 0.00479 | 53.756 | 55.420 | +9.36% | -0.84% | 1.26x | 41.8 | 2026-11-24T17:22:20.373378+00:00 | Not calibrated | WEAK 22/100 | EXTREME 95/100 | Do nothing | WATCH |
| 5 | 2Z/USD | 0.01616 | 52.728 | 47.356 | +3.26% | +1.13% | 0.97x | 12.4 | 2026-11-24T17:22:20.373378+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 6 | GBP/USD | 1.31092 | 50.933 | 59.043 | +0.59% | -0.01% | 0.20x | 0.2 | 2026-11-24T17:22:20.373378+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | DBR/USD | 0.01373 | 46.489 | 33.081 | +2.31% | -0.29% | 2.49x | 29.2 | 2026-11-24T17:22:20.373378+00:00 | Not calibrated | WEAK 43/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 70.927 | 25.074 | +2.06% | 0.82x |
| 2 | XMR/USD | 68.766 | 497.95 | +0.55% | 0.37x |
| 3 | LUNA/USD | 63.611 | 4.708e-05 | +1.25% | 0.72x |
| 4 | GBP/USD | 59.043 | 1.31092 | -0.01% | 0.20x |
| 5 | ZEUS/USD | 55.420 | 0.00479 | -0.84% | 1.26x |
| 6 | 2Z/USD | 47.356 | 0.01616 | +1.13% | 0.97x |
| 7 | DBR/USD | 33.081 | 0.01373 | -0.29% | 2.49x |

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

- Persisted scans: 1603; predictions: 13775; observations: 971319.
- Matured sampled outcomes across 1/6/24/48h: 27618; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45447304793 · **Generation:** 1603 · **Legacy run:** 45447304793
**Main quote time:** 2026-11-24T17:22:23.943209+00:00 · **Legacy report time:** 2026-11-24T17:23:15.111481+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.074 | 79.43 | +2.06% | 0.82x | STRONG 70/100 | HIGH 62/100 | Watch |
| 2 | LUNA/USD | 4.708e-05 | 67.03 | +1.25% | 0.72x | MODERATE 54/100 | EXTREME 94/100 | Do nothing |
| 3 | XMR/USD | 497.95 | 65.24 | +0.55% | 0.37x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 4 | ZEUS/USD | 0.00479 | 53.76 | -0.84% | 1.26x | WEAK 22/100 | EXTREME 95/100 | Do nothing |
| 5 | 2Z/USD | 0.01616 | 52.73 | +1.13% | 0.97x | MODERATE 51/100 | VERY_HIGH 80/100 | Watch |
| 6 | GBP/USD | 1.31092 | 50.93 | -0.01% | 0.20x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | DBR/USD | 0.01373 | 46.49 | -0.29% | 2.49x | WEAK 43/100 | EXTREME 85/100 | Do nothing |

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
