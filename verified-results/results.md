# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T16:51:01.614028+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45862303688
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fc9f48aa398dda9921c0f956923f76b8c955c530 (atomic ledger/results publication)
**Ledger generation:** 1887 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 594; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 149.86 | 80.801 | 66.699 | +3.49% | +1.04% | 1.89x | 4.7 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | WIF/USD | 0.136 | 71.745 | 69.024 | +6.83% | +1.19% | 0.68x | 14.7 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | MODERATE 61/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | LTC/USD | 43.53 | 71.497 | 67.291 | +1.92% | +0.23% | 1.31x | 2.3 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PIEVERSE/USD | 3.9492 | 71.391 | 73.251 | +11.53% | +0.02% | 0.81x | 24.3 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | LINK/USD | 9.17478 | 71.020 | 64.477 | +1.44% | +0.27% | 1.52x | 1.2 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | SKY/USD | 0.04543 | 69.424 | 75.235 | +8.48% | -1.37% | 1.10x | 8.8 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 7 | STBL/USD | 0.020383 | 66.416 | 72.317 | +7.93% | -0.21% | 0.52x | 7.4 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | WEAK 38/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | ADA/USD | 0.148488 | 64.656 | 66.132 | +1.86% | +0.48% | 0.61x | 3.8 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | GWEI/USD | 0.010365 | 62.604 | 65.704 | +6.53% | +0.08% | 0.65x | 20.3 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | WEAK 41/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | SOL/USD | 70.9 | 62.035 | 59.366 | +0.72% | +0.52% | 1.00x | 1.4 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XRP/USD | 0.94901 | 57.617 | 63.884 | +1.33% | +0.49% | 0.13x | 0.8 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0566859 | 52.996 | 54.846 | +1.30% | +0.49% | 0.57x | 0.2 | 2026-11-26T16:50:55.302874+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.235 | 0.04543 | -1.37% | 1.10x |
| 2 | PIEVERSE/USD | 73.251 | 3.9492 | +0.02% | 0.81x |
| 3 | STBL/USD | 72.317 | 0.020383 | -0.21% | 0.52x |
| 4 | WIF/USD | 69.024 | 0.136 | +1.19% | 0.68x |
| 5 | LTC/USD | 67.291 | 43.53 | +0.23% | 1.31x |
| 6 | QNT/USD | 66.699 | 149.86 | +1.04% | 1.89x |
| 7 | ADA/USD | 66.132 | 0.148488 | +0.48% | 0.61x |
| 8 | GWEI/USD | 65.704 | 0.010365 | +0.08% | 0.65x |
| 9 | LINK/USD | 64.477 | 9.17478 | +0.27% | 1.52x |
| 10 | XRP/USD | 63.884 | 0.94901 | +0.49% | 0.13x |
| 11 | SOL/USD | 59.366 | 70.9 | +0.52% | 1.00x |
| 12 | XDG/USD | 54.846 | 0.0566859 | +0.49% | 0.57x |

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

- Persisted scans: 1887; predictions: 16379; observations: 1143298.
- Matured sampled outcomes across 1/6/24/48h: 35390; gap abstentions: 25076. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45862303688 · **Generation:** 1887 · **Legacy run:** 45862303688
**Main quote time:** 2026-11-26T16:51:01.614028+00:00 · **Legacy report time:** 2026-11-26T16:51:38.165588+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 149.86 | 80.80 | +1.04% | 1.89x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | WIF/USD | 0.136 | 71.74 | +1.19% | 0.68x | MODERATE 61/100 | EXTREME 88/100 | Do nothing |
| 3 | LTC/USD | 43.53 | 71.50 | +0.23% | 1.31x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | PIEVERSE/USD | 3.9492 | 71.39 | +0.02% | 0.81x | MODERATE 46/100 | VERY_HIGH 74/100 | Watch |
| 5 | LINK/USD | 9.17478 | 71.02 | +0.27% | 1.52x | STRONG 81/100 | HIGH 55/100 | Consider small entry |
| 6 | SKY/USD | 0.04543 | 69.42 | -1.37% | 1.10x | MODERATE 45/100 | VERY_HIGH 77/100 | Do nothing |
| 7 | STBL/USD | 0.020383 | 66.42 | -0.21% | 0.52x | WEAK 38/100 | EXTREME 88/100 | Do nothing |
| 8 | ADA/USD | 0.148488 | 64.66 | +0.48% | 0.61x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 9 | GWEI/USD | 0.010365 | 62.60 | +0.08% | 0.65x | WEAK 41/100 | EXTREME 94/100 | Do nothing |
| 10 | SOL/USD | 70.9 | 62.03 | +0.52% | 1.00x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 11 | XRP/USD | 0.94901 | 57.62 | +0.49% | 0.13x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0566859 | 53.00 | +0.49% | 0.57x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 6.173 | 86.37 | +0.54% | 2.56x | 6402 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 2 | QNT/USD ⭐ | 149.86 | 85.02 | +1.04% | 1.89x | 7721 | STRONG 98/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** QNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
