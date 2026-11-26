# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T14:51:12.398455+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45842879117
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1d53f0ca553ee4b14495f6c5521a05435b62311b (atomic ledger/results publication)
**Ledger generation:** 1875 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 590; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | FET/USD | 0.115 | 80.055 | 66.788 | +5.99% | -0.35% | 6.03x | 17.4 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | XRP/USD | 0.95029 | 79.097 | 65.104 | +1.47% | -0.20% | 2.85x | 0.3 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LINK/USD | 9.2239 | 77.826 | 64.611 | +1.98% | -0.36% | 4.07x | 4.9 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SEI/USD | 0.03714 | 77.266 | 73.292 | +11.50% | -0.59% | 1.69x | 10.8 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | QNT/USD | 149.65 | 76.160 | 66.345 | +3.35% | -0.49% | 2.23x | 4.7 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ADA/USD | 0.148957 | 70.741 | 67.886 | +2.19% | -0.16% | 1.36x | 4.8 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XBT/USD | 60771.7 | 63.517 | 59.666 | +0.67% | -0.10% | 1.43x | 0.0 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ZRO/USD | 1.091 | 63.444 | 74.816 | +6.54% | -1.27% | 0.50x | 18.4 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | WEAK 32/100 | EXTREME 86/100 | Do nothing | WATCH |
| 9 | VELO/USD | 0.00253 | 62.732 | 68.074 | +11.40% | +0.32% | 0.31x | 15.8 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | LTC/USD | 43.67 | 62.206 | 69.589 | +2.25% | -0.50% | 0.51x | 2.3 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SOL/USD | 71.16 | 60.697 | 61.955 | +1.09% | -0.24% | 0.99x | 1.4 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 12 | ETH/USD | 1699.69 | 55.847 | 58.813 | +0.55% | -0.22% | 0.81x | 0.1 | 2026-11-26T14:51:04.751161+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 74.816 | 1.091 | -1.27% | 0.50x |
| 2 | SEI/USD | 73.292 | 0.03714 | -0.59% | 1.69x |
| 3 | LTC/USD | 69.589 | 43.67 | -0.50% | 0.51x |
| 4 | VELO/USD | 68.074 | 0.00253 | +0.32% | 0.31x |
| 5 | ADA/USD | 67.886 | 0.148957 | -0.16% | 1.36x |
| 6 | FET/USD | 66.788 | 0.115 | -0.35% | 6.03x |
| 7 | QNT/USD | 66.345 | 149.65 | -0.49% | 2.23x |
| 8 | XRP/USD | 65.104 | 0.95029 | -0.20% | 2.85x |
| 9 | LINK/USD | 64.611 | 9.2239 | -0.36% | 4.07x |
| 10 | SOL/USD | 61.955 | 71.16 | -0.24% | 0.99x |
| 11 | XBT/USD | 59.666 | 60771.7 | -0.10% | 1.43x |
| 12 | ETH/USD | 58.813 | 1699.69 | -0.22% | 0.81x |

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

- Persisted scans: 1875; predictions: 16235; observations: 1136190.
- Matured sampled outcomes across 1/6/24/48h: 35114; gap abstentions: 24944. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45842879117 · **Generation:** 1875 · **Legacy run:** 45842879117
**Main quote time:** 2026-11-26T14:51:12.398455+00:00 · **Legacy report time:** 2026-11-26T14:52:22.195433+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | FET/USD | 0.115 | 80.05 | -0.35% | 6.03x | MODERATE 65/100 | VERY_HIGH 72/100 | Watch |
| 2 | XRP/USD | 0.95029 | 79.10 | -0.20% | 2.85x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD | 9.2239 | 77.83 | -0.36% | 4.07x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | SEI/USD | 0.03714 | 77.27 | -0.59% | 1.69x | MODERATE 54/100 | VERY_HIGH 72/100 | Watch |
| 5 | QNT/USD | 149.65 | 76.16 | -0.49% | 2.23x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 6 | ADA/USD | 0.148957 | 70.74 | -0.16% | 1.36x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 7 | XBT/USD | 60771.7 | 63.52 | -0.10% | 1.43x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 8 | ZRO/USD | 1.091 | 63.44 | -1.27% | 0.50x | WEAK 32/100 | EXTREME 86/100 | Do nothing |
| 9 | VELO/USD | 0.00253 | 62.73 | +0.32% | 0.31x | MODERATE 56/100 | EXTREME 88/100 | Do nothing |
| 10 | LTC/USD | 43.67 | 62.21 | -0.50% | 0.51x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | SOL/USD | 71.16 | 60.70 | -0.24% | 0.99x | WEAK 35/100 | HIGH 68/100 | Watch |
| 12 | ETH/USD | 1699.69 | 55.85 | -0.22% | 0.81x | WEAK 33/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2Z/USD | 0.0181 | 80.48 | +2.13% | 3.20x | 2070 | STRONG 80/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
