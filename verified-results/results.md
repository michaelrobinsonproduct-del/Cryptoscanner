# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T11:21:37.344232+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45164168874
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 04b6ae721826bdbaeeb2138f01d30a5d14187b2c (atomic ledger/results publication)
**Ledger generation:** 1423 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 155.92 | 97.727 | 88.230 | +8.70% | +2.12% | 0.89x | 8.3 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | STRONG 79/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08237 | 94.925 | 75.268 | +9.20% | +0.93% | 4.23x | 8.5 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | JUP/USD | 0.24129 | 86.691 | 74.221 | +7.45% | +0.18% | 2.16x | 12.0 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | STRONG 83/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6702 | 84.808 | 68.986 | +2.21% | +0.16% | 6.00x | 3.0 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 72.33 | 68.631 | 71.157 | +2.41% | +0.21% | 0.64x | 1.4 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XRP/USD | 0.93933 | 65.752 | 63.844 | +1.27% | -0.01% | 1.20x | 0.1 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 7 | HYPE/USD | 63.88 | 65.527 | 62.537 | +1.30% | -0.51% | 1.56x | 3.1 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 8 | PAXG/USD | 3607.86 | 65.377 | 50.833 | +1.00% | -0.09% | 2.82x | 1.1 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XLM/USD | 0.129064 | 63.450 | 62.642 | +1.20% | +0.11% | 1.03x | 0.1 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XMR/USD | 502.21 | 57.189 | 65.856 | +1.72% | -0.05% | 0.16x | 2.4 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ADA/USD | 0.145898 | 53.820 | 55.413 | +0.90% | +0.11% | 0.79x | 1.9 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 12 | TRX/USD | 0.307516 | 50.322 | 42.052 | +0.77% | +0.37% | 1.64x | 1.5 | 2026-11-23T11:21:31.016937+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 88.230 | 155.92 | +2.12% | 0.89x |
| 2 | ALGO/USD | 75.268 | 0.08237 | +0.93% | 4.23x |
| 3 | JUP/USD | 74.221 | 0.24129 | +0.18% | 2.16x |
| 4 | SOL/USD | 71.157 | 72.33 | +0.21% | 0.64x |
| 5 | SUI/USD | 68.986 | 0.6702 | +0.16% | 6.00x |
| 6 | XMR/USD | 65.856 | 502.21 | -0.05% | 0.16x |
| 7 | XRP/USD | 63.844 | 0.93933 | -0.01% | 1.20x |
| 8 | XLM/USD | 62.642 | 0.129064 | +0.11% | 1.03x |
| 9 | HYPE/USD | 62.537 | 63.88 | -0.51% | 1.56x |
| 10 | ADA/USD | 55.413 | 0.145898 | +0.11% | 0.79x |
| 11 | PAXG/USD | 50.833 | 3607.86 | -0.09% | 2.82x |
| 12 | TRX/USD | 42.052 | 0.307516 | +0.37% | 1.64x |

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

- Persisted scans: 1423; predictions: 11843; observations: 861710.
- Matured sampled outcomes across 1/6/24/48h: 19624; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45164168874 · **Generation:** 1423 · **Legacy run:** 45164168874
**Main quote time:** 2026-11-23T11:21:37.344232+00:00 · **Legacy report time:** 2026-11-23T11:22:43.673662+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 155.92 | 97.73 | +2.12% | 0.89x | STRONG 79/100 | HIGH 62/100 | Watch |
| 2 | ALGO/USD ⭐ | 0.08237 | 94.93 | +0.93% | 4.23x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | JUP/USD ⭐ | 0.24129 | 86.69 | +0.18% | 2.16x | STRONG 93/100 | HIGH 66/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6702 | 84.81 | +0.16% | 6.00x | STRONG 97/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD | 72.33 | 68.63 | +0.21% | 0.64x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 6 | XRP/USD | 0.93933 | 65.75 | -0.01% | 1.20x | WEAK 43/100 | HIGH 68/100 | Watch |
| 7 | HYPE/USD | 63.88 | 65.53 | -0.51% | 1.56x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 8 | PAXG/USD | 3607.86 | 65.38 | -0.09% | 2.82x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 9 | XLM/USD ⭐ | 0.129064 | 63.45 | +0.11% | 1.03x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 10 | XMR/USD | 502.21 | 57.19 | -0.05% | 0.16x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ADA/USD | 0.145898 | 53.82 | +0.11% | 0.79x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 12 | TRX/USD | 0.307516 | 50.32 | +0.37% | 1.64x | STRONG 70/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.08239 | 83.96 | +0.93% | 4.23x | 3390 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.6697 | 83.13 | +0.16% | 6.00x | 5713 | STRONG 97/100 | HIGH 55/100 | Watch |
| 3 | JUP/USD ⭐ | 0.24076 | 78.31 | +0.18% | 2.16x | 3499 | STRONG 94/100 | HIGH 60/100 | Watch |
| 4 | ICP/USD | 2.055 | 69.25 | +0.59% | 2.25x | 1465 | STRONG 90/100 | HIGH 60/100 | Watch |
| 5 | XLM/USD ⭐ | 0.129162 | 64.14 | +0.11% | 1.03x | 12390 | MODERATE 67/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ALGO/USD, JUP/USD, SUI/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
