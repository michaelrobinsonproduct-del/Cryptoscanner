# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T09:56:24.637286+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45796339982
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 791478eccbd80c5aeebdab165282dfdcb9cb5d90 (atomic ledger/results publication)
**Ledger generation:** 1845 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 584; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.2441 | 74.078 | 69.413 | +2.21% | +0.02% | 1.46x | 2.1 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SEI/USD | 0.03552 | 73.044 | 71.573 | +6.63% | -0.17% | 1.23x | 11.3 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.061 | 72.370 | 56.404 | +0.36% | +0.19% | 9.77x | 2.3 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LTC/USD | 43.74 | 69.196 | 70.738 | +2.41% | +0.00% | 0.85x | 2.3 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 5 | INJ/USD | 6.251 | 69.196 | 76.751 | +4.99% | -0.18% | 0.33x | 3.2 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SYRUP/USD | 0.07062 | 63.950 | 69.514 | +6.56% | +0.00% | 0.44x | 15.6 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | ADA/USD | 0.148991 | 62.188 | 68.957 | +2.21% | -0.10% | 0.38x | 3.0 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95326 | 60.567 | 67.429 | +1.78% | +0.15% | 0.24x | 0.1 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 60855.1 | 60.416 | 60.633 | +0.81% | +0.06% | 0.95x | 0.0 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SOL/USD | 71.01 | 54.222 | 60.461 | +0.88% | -0.11% | 0.43x | 1.4 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1701.65 | 52.220 | 59.625 | +0.66% | -0.01% | 0.26x | 0.1 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XDG/USD | 0.0566514 | 52.026 | 58.980 | +1.24% | +0.00% | 0.30x | 0.0 | 2026-11-26T09:56:18.200390+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 76.751 | 6.251 | -0.18% | 0.33x |
| 2 | SEI/USD | 71.573 | 0.03552 | -0.17% | 1.23x |
| 3 | LTC/USD | 70.738 | 43.74 | +0.00% | 0.85x |
| 4 | SYRUP/USD | 69.514 | 0.07062 | +0.00% | 0.44x |
| 5 | LINK/USD | 69.413 | 9.2441 | +0.02% | 1.46x |
| 6 | ADA/USD | 68.957 | 0.148991 | -0.10% | 0.38x |
| 7 | XRP/USD | 67.429 | 0.95326 | +0.15% | 0.24x |
| 8 | XBT/USD | 60.633 | 60855.1 | +0.06% | 0.95x |
| 9 | SOL/USD | 60.461 | 71.01 | -0.11% | 0.43x |
| 10 | ETH/USD | 59.625 | 1701.65 | -0.01% | 0.26x |
| 11 | XDG/USD | 58.980 | 0.0566514 | +0.00% | 0.30x |
| 12 | NEAR/USD | 56.404 | 3.061 | +0.19% | 9.77x |

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

- Persisted scans: 1845; predictions: 15875; observations: 1118572.
- Matured sampled outcomes across 1/6/24/48h: 34394; gap abstentions: 24507. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45796339982 · **Generation:** 1845 · **Legacy run:** 45796339982
**Main quote time:** 2026-11-26T09:56:24.637286+00:00 · **Legacy report time:** 2026-11-26T09:57:43.372058+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.2441 | 74.08 | +0.02% | 1.46x | STRONG 72/100 | HIGH 55/100 | Watch |
| 2 | SEI/USD | 0.03552 | 73.04 | -0.17% | 1.23x | WEAK 42/100 | VERY_HIGH 79/100 | Watch |
| 3 | NEAR/USD | 3.061 | 72.37 | +0.19% | 9.77x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | LTC/USD | 43.74 | 69.20 | +0.00% | 0.85x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 5 | INJ/USD | 6.251 | 69.20 | -0.18% | 0.33x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 6 | SYRUP/USD | 0.07062 | 63.95 | +0.00% | 0.44x | MODERATE 47/100 | VERY_HIGH 81/100 | Watch |
| 7 | ADA/USD | 0.148991 | 62.19 | -0.10% | 0.38x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | XRP/USD | 0.95326 | 60.57 | +0.15% | 0.24x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 60855.1 | 60.42 | +0.06% | 0.95x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 10 | SOL/USD | 71.01 | 54.22 | -0.11% | 0.43x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ETH/USD | 1701.65 | 52.22 | -0.01% | 0.26x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XDG/USD | 0.0566514 | 52.03 | +0.00% | 0.30x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |

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
