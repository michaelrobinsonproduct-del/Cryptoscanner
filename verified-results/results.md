# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T03:45:55.499242+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45750836610
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4961aba027d4b33801914e7881c34407ee7bb767 (atomic ledger/results publication)
**Ledger generation:** 1808 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07072 | 75.961 | 67.844 | +6.71% | +0.28% | 1.67x | 18.4 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | XDG/USD | 0.0568 | 74.924 | 59.903 | +1.50% | +0.00% | 2.83x | 0.9 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LTC/USD | 43.84 | 71.880 | 71.239 | +2.65% | +0.44% | 0.85x | 4.6 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ADA/USD | 0.148889 | 69.921 | 68.298 | +2.14% | +0.15% | 1.09x | 3.4 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 5 | LINK/USD | 9.19552 | 67.390 | 63.431 | +1.67% | +0.17% | 1.31x | 1.9 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95676 | 62.526 | 69.158 | +2.16% | +0.07% | 0.30x | 1.9 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | PIEVERSE/USD | 3.8344 | 61.552 | 59.286 | +8.29% | +2.33% | 0.06x | 41.5 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 97/100 | Do nothing | WATCH |
| 8 | SOL/USD | 71.06 | 59.967 | 60.959 | +0.95% | -0.01% | 0.91x | 1.4 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 9 | AAVE/USD | 95.71 | 54.830 | 42.014 | +0.37% | -0.44% | 2.80x | 4.2 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6725 | 54.554 | 60.027 | +0.93% | -0.31% | 0.61x | 3.0 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1695.76 | 54.434 | 57.186 | +0.32% | +0.00% | 0.72x | 0.1 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | HYPE/USD | 61.79 | 52.836 | 56.122 | +0.28% | -0.10% | 0.72x | 1.6 | 2026-11-26T03:45:46.403122+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 71.239 | 43.84 | +0.44% | 0.85x |
| 2 | XRP/USD | 69.158 | 0.95676 | +0.07% | 0.30x |
| 3 | ADA/USD | 68.298 | 0.148889 | +0.15% | 1.09x |
| 4 | SYRUP/USD | 67.844 | 0.07072 | +0.28% | 1.67x |
| 5 | LINK/USD | 63.431 | 9.19552 | +0.17% | 1.31x |
| 6 | SOL/USD | 60.959 | 71.06 | -0.01% | 0.91x |
| 7 | SUI/USD | 60.027 | 0.6725 | -0.31% | 0.61x |
| 8 | XDG/USD | 59.903 | 0.0568 | +0.00% | 2.83x |
| 9 | PIEVERSE/USD | 59.286 | 3.8344 | +2.33% | 0.06x |
| 10 | ETH/USD | 57.186 | 1695.76 | +0.00% | 0.72x |
| 11 | HYPE/USD | 56.122 | 61.79 | -0.10% | 0.72x |
| 12 | AAVE/USD | 42.014 | 95.71 | -0.44% | 2.80x |

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

- Persisted scans: 1808; predictions: 15431; observations: 1096116.
- Matured sampled outcomes across 1/6/24/48h: 33491; gap abstentions: 23804. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45750836610 · **Generation:** 1808 · **Legacy run:** 45750836610
**Main quote time:** 2026-11-26T03:45:55.499242+00:00 · **Legacy report time:** 2026-11-26T03:46:47.168710+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07072 | 75.96 | +0.28% | 1.67x | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 2 | XDG/USD | 0.0568 | 74.92 | +0.00% | 2.83x | STRONG 82/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD | 43.84 | 71.88 | +0.44% | 0.85x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 4 | ADA/USD ⭐ | 0.148889 | 69.92 | +0.15% | 1.09x | STRONG 70/100 | HIGH 62/100 | Watch |
| 5 | LINK/USD ⭐ | 9.19552 | 67.39 | +0.17% | 1.31x | STRONG 79/100 | HIGH 55/100 | Watch |
| 6 | XRP/USD | 0.95676 | 62.53 | +0.07% | 0.30x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 7 | PIEVERSE/USD | 3.8344 | 61.55 | +2.33% | 0.06x | MODERATE 46/100 | EXTREME 97/100 | Do nothing |
| 8 | SOL/USD | 71.06 | 59.97 | -0.01% | 0.91x | WEAK 35/100 | HIGH 68/100 | Watch |
| 9 | AAVE/USD | 95.71 | 54.83 | -0.44% | 2.80x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 10 | SUI/USD | 0.6725 | 54.55 | -0.31% | 0.61x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ETH/USD | 1695.76 | 54.43 | +0.00% | 0.72x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 12 | HYPE/USD | 61.79 | 52.84 | -0.10% | 0.72x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07072 | 74.75 | +0.28% | 1.67x | 3502 | STRONG 82/100 | VERY_HIGH 72/100 | Watch |
| 2 | ADA/USD ⭐ | 0.148854 | 74.70 | +0.15% | 1.09x | 11372 | STRONG 72/100 | HIGH 62/100 | Watch |
| 3 | LINK/USD ⭐ | 9.2074 | 67.81 | +0.17% | 1.31x | 9004 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SYRUP/USD, ADA/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
