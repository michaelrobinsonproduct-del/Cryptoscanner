# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T07:16:18.383898+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45773853948
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3edd3cca71f13ac181b76a6b9249f3669540e2dd (atomic ledger/results publication)
**Ledger generation:** 1829 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.147955 | 81.356 | 65.459 | +1.50% | +0.18% | 5.69x | 0.1 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0643 | 75.018 | 57.489 | +0.47% | +0.51% | 3.20x | 1.6 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SKY/USD | 0.0438 | 73.399 | 61.137 | +4.58% | +0.48% | 1.98x | 9.1 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | INJ/USD | 6.096 | 70.939 | 57.330 | +2.38% | -0.28% | 2.82x | 3.3 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XMR/USD | 522.58 | 69.864 | 58.219 | +1.09% | +0.05% | 2.14x | 8.8 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LINK/USD | 9.15353 | 67.402 | 60.891 | +1.21% | +0.03% | 1.64x | 4.0 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95094 | 66.044 | 65.275 | +1.54% | +0.09% | 1.03x | 0.9 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 8 | SYRUP/USD | 0.07109 | 63.650 | 69.403 | +7.27% | -0.30% | 0.57x | 15.5 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | WEAK 32/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | HBAR/USD | 0.0533 | 63.608 | 51.337 | +2.30% | +1.02% | 1.71x | 3.8 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 10 | LTC/USD | 43.36 | 63.213 | 64.499 | +1.52% | -0.07% | 0.91x | 2.3 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128234 | 62.834 | 45.895 | +0.32% | +0.39% | 4.70x | 1.7 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 12 | SOL/USD | 70.84 | 58.181 | 58.769 | +0.64% | +0.30% | 0.79x | 1.4 | 2026-11-26T07:16:09.293328+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 69.403 | 0.07109 | -0.30% | 0.57x |
| 2 | ADA/USD | 65.459 | 0.147955 | +0.18% | 5.69x |
| 3 | XRP/USD | 65.275 | 0.95094 | +0.09% | 1.03x |
| 4 | LTC/USD | 64.499 | 43.36 | -0.07% | 0.91x |
| 5 | SKY/USD | 61.137 | 0.0438 | +0.48% | 1.98x |
| 6 | LINK/USD | 60.891 | 9.15353 | +0.03% | 1.64x |
| 7 | SOL/USD | 58.769 | 70.84 | +0.30% | 0.79x |
| 8 | XMR/USD | 58.219 | 522.58 | +0.05% | 2.14x |
| 9 | NEAR/USD | 57.489 | 3.0643 | +0.51% | 3.20x |
| 10 | INJ/USD | 57.330 | 6.096 | -0.28% | 2.82x |
| 11 | HBAR/USD | 51.337 | 0.0533 | +1.02% | 1.71x |
| 12 | XLM/USD | 45.895 | 0.128234 | +0.39% | 4.70x |

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

- Persisted scans: 1829; predictions: 15683; observations: 1108905.
- Matured sampled outcomes across 1/6/24/48h: 33998; gap abstentions: 24182. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45773853948 · **Generation:** 1829 · **Legacy run:** 45773853948
**Main quote time:** 2026-11-26T07:16:18.383898+00:00 · **Legacy report time:** 2026-11-26T07:17:29.860175+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.147955 | 81.36 | +0.18% | 5.69x | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD | 3.0643 | 75.02 | +0.51% | 3.20x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 3 | SKY/USD ⭐ | 0.0438 | 73.40 | +0.48% | 1.98x | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 4 | INJ/USD | 6.096 | 70.94 | -0.28% | 2.82x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | XMR/USD | 522.58 | 69.86 | +0.05% | 2.14x | STRONG 80/100 | HIGH 55/100 | Watch |
| 6 | LINK/USD | 9.15353 | 67.40 | +0.03% | 1.64x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 7 | XRP/USD ⭐ | 0.95094 | 66.04 | +0.09% | 1.03x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 8 | SYRUP/USD | 0.07109 | 63.65 | -0.30% | 0.57x | WEAK 32/100 | EXTREME 87/100 | Do nothing |
| 9 | HBAR/USD ⭐ | 0.0533 | 63.61 | +1.02% | 1.71x | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 10 | LTC/USD | 43.36 | 63.21 | -0.07% | 0.91x | WEAK 37/100 | HIGH 68/100 | Watch |
| 11 | XLM/USD | 0.128234 | 62.83 | +0.39% | 4.70x | STRONG 86/100 | HIGH 55/100 | Watch |
| 12 | SOL/USD | 70.84 | 58.18 | +0.30% | 0.79x | MODERATE 59/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04381 | 77.55 | +0.48% | 1.98x | 4067 | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.148064 | 72.67 | +0.18% | 5.69x | 12065 | STRONG 91/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD ⭐ | 0.95177 | 71.05 | +0.09% | 1.03x | 42558 | STRONG 71/100 | HIGH 62/100 | Watch |
| 4 | HBAR/USD ⭐ | 0.05334 | 68.25 | +1.02% | 1.71x | 6317 | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 5 | PUMP/USD | 0.002625 | 63.11 | +0.46% | 1.24x | 6343 | MODERATE 67/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ADA/USD, SKY/USD, XRP/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
