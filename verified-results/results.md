# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T14:21:26.942121+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45837852879
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** adbc38454cf17a70e9bca17f5ffa74e57165489f (atomic ledger/results publication)
**Ledger generation:** 1872 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 589; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | FET/USD | 0.1157 | 87.838 | 69.794 | +6.64% | +0.61% | 10.48x | 17.3 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | STRONG 94/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 43.82 | 86.823 | 70.908 | +2.60% | +0.18% | 2.69x | 4.6 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 3 | WIF/USD | 0.1348 | 82.563 | 68.762 | +5.89% | +1.51% | 1.63x | 7.4 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | STRONG 86/100 | HIGH 67/100 | Consider small entry | WATCH |
| 4 | ZRO/USD | 1.108 | 82.176 | 75.600 | +8.20% | +0.00% | 1.66x | 18.1 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ADA/USD | 0.149043 | 79.971 | 69.341 | +2.25% | +0.10% | 2.01x | 2.8 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SOL/USD | 71.22 | 78.255 | 62.552 | +1.18% | +0.14% | 3.46x | 1.4 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 7 | LINK/USD | 9.26498 | 76.082 | 70.081 | +2.44% | +0.30% | 1.45x | 2.6 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0569729 | 73.776 | 61.713 | +1.81% | +0.22% | 2.10x | 0.0 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | QNT/USD | 150.4 | 71.703 | 71.219 | +3.87% | -0.56% | 1.33x | 4.7 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XBT/USD | 60731.9 | 71.339 | 59.204 | +0.60% | -0.09% | 2.26x | 0.0 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 11 | 2Z/USD | 0.01762 | 71.332 | 73.365 | +6.66% | +0.46% | 0.57x | 5.7 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 12 | SYRUP/USD | 0.07111 | 70.500 | 70.150 | +7.30% | -0.25% | 1.16x | 14.1 | 2026-11-26T14:21:19.241693+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 75.600 | 1.108 | +0.00% | 1.66x |
| 2 | 2Z/USD | 73.365 | 0.01762 | +0.46% | 0.57x |
| 3 | QNT/USD | 71.219 | 150.4 | -0.56% | 1.33x |
| 4 | LTC/USD | 70.908 | 43.82 | +0.18% | 2.69x |
| 5 | SYRUP/USD | 70.150 | 0.07111 | -0.25% | 1.16x |
| 6 | LINK/USD | 70.081 | 9.26498 | +0.30% | 1.45x |
| 7 | FET/USD | 69.794 | 0.1157 | +0.61% | 10.48x |
| 8 | ADA/USD | 69.341 | 0.149043 | +0.10% | 2.01x |
| 9 | WIF/USD | 68.762 | 0.1348 | +1.51% | 1.63x |
| 10 | SOL/USD | 62.552 | 71.22 | +0.14% | 3.46x |
| 11 | XDG/USD | 61.713 | 0.0569729 | +0.22% | 2.10x |
| 12 | XBT/USD | 59.204 | 60731.9 | -0.09% | 2.26x |

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

- Persisted scans: 1872; predictions: 16199; observations: 1134421.
- Matured sampled outcomes across 1/6/24/48h: 35042; gap abstentions: 24901. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45837852879 · **Generation:** 1872 · **Legacy run:** 45837852879
**Main quote time:** 2026-11-26T14:21:26.942121+00:00 · **Legacy report time:** 2026-11-26T14:22:48.882159+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | FET/USD | 0.1157 | 87.84 | +0.61% | 10.48x | STRONG 94/100 | HIGH 66/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 43.82 | 86.82 | +0.18% | 2.69x | STRONG 98/100 | HIGH 55/100 | Watch |
| 3 | WIF/USD | 0.1348 | 82.56 | +1.51% | 1.63x | STRONG 86/100 | HIGH 67/100 | Consider small entry |
| 4 | ZRO/USD | 1.108 | 82.18 | +0.00% | 1.66x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | ADA/USD ⭐ | 0.149043 | 79.97 | +0.10% | 2.01x | STRONG 95/100 | HIGH 55/100 | Watch |
| 6 | SOL/USD | 71.22 | 78.25 | +0.14% | 3.46x | STRONG 84/100 | HIGH 55/100 | Watch |
| 7 | LINK/USD ⭐ | 9.26498 | 76.08 | +0.30% | 1.45x | STRONG 93/100 | HIGH 55/100 | Watch |
| 8 | XDG/USD | 0.0569729 | 73.78 | +0.22% | 2.10x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 9 | QNT/USD | 150.4 | 71.70 | -0.56% | 1.33x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 10 | XBT/USD | 60731.9 | 71.34 | -0.09% | 2.26x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 11 | 2Z/USD | 0.01762 | 71.33 | +0.46% | 0.57x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 12 | SYRUP/USD | 0.07111 | 70.50 | -0.25% | 1.16x | WEAK 40/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 43.79 | 85.07 | +0.18% | 2.69x | 15656 | STRONG 98/100 | HIGH 55/100 | Watch |
| 2 | SKY/USD | 0.04702 | 84.00 | +1.03% | 3.46x | 5963 | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 3 | ADA/USD ⭐ | 0.148968 | 77.58 | +0.10% | 2.01x | 11982 | STRONG 94/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD ⭐ | 9.25935 | 77.40 | +0.30% | 1.45x | 8839 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LTC/USD, ADA/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
