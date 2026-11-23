# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T15:51:44.066845+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45209546703
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b8d939aee7d14544dbd7021bb6308e1a9f21e8b6 (atomic ledger/results publication)
**Ledger generation:** 1450 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SOL/USD | 75.62 | 100.983 | 99.339 | +7.07% | -0.41% | 1.37x | 1.3 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | INJ/USD | 6.739 | 99.404 | 92.910 | +8.20% | -0.30% | 1.80x | 7.4 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ZEC/USD | 863.53 | 91.665 | 96.465 | +8.28% | -1.28% | 1.16x | 7.1 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 4 | SUI/USD | 0.7131 | 91.658 | 98.599 | +8.75% | -0.45% | 0.53x | 2.8 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | HYPE/USD | 67.14 | 90.987 | 97.768 | +6.47% | -0.86% | 0.75x | 4.5 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XRP/USD | 0.99131 | 90.586 | 97.629 | +6.88% | -0.95% | 0.77x | 4.7 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ADA/USD | 0.153546 | 86.733 | 96.076 | +6.18% | -0.80% | 0.47x | 4.4 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0585284 | 84.190 | 94.708 | +5.87% | -0.72% | 0.31x | 2.7 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | LTC/USD | 42.55 | 83.288 | 94.308 | +5.95% | -0.61% | 0.20x | 4.7 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.1414 | 81.276 | 89.474 | +5.36% | -0.45% | 0.41x | 6.0 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | QNT/USD | 160.46 | 81.018 | 90.658 | +11.87% | -0.54% | 0.30x | 18.7 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 12 | CC/USD | 0.07972 | 79.842 | 80.369 | +8.80% | +1.23% | 0.33x | 2.5 | 2026-11-23T15:51:37.479664+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 99.339 | 75.62 | -0.41% | 1.37x |
| 2 | SUI/USD | 98.599 | 0.7131 | -0.45% | 0.53x |
| 3 | HYPE/USD | 97.768 | 67.14 | -0.86% | 0.75x |
| 4 | XRP/USD | 97.629 | 0.99131 | -0.95% | 0.77x |
| 5 | ZEC/USD | 96.465 | 863.53 | -1.28% | 1.16x |
| 6 | ADA/USD | 96.076 | 0.153546 | -0.80% | 0.47x |
| 7 | XDG/USD | 94.708 | 0.0585284 | -0.72% | 0.31x |
| 8 | LTC/USD | 94.308 | 42.55 | -0.61% | 0.20x |
| 9 | INJ/USD | 92.910 | 6.739 | -0.30% | 1.80x |
| 10 | QNT/USD | 90.658 | 160.46 | -0.54% | 0.30x |
| 11 | NEAR/USD | 89.474 | 3.1414 | -0.45% | 0.41x |
| 12 | CC/USD | 80.369 | 0.07972 | +1.23% | 0.33x |

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

- Persisted scans: 1450; predictions: 12167; observations: 878152.
- Matured sampled outcomes across 1/6/24/48h: 20908; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45209546703 · **Generation:** 1450 · **Legacy run:** 45209546703
**Main quote time:** 2026-11-23T15:51:44.066845+00:00 · **Legacy report time:** 2026-11-23T15:52:38.055566+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD | 75.62 | 100.98 | -0.41% | 1.37x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | INJ/USD | 6.739 | 99.40 | -0.30% | 1.80x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | ZEC/USD | 863.53 | 91.67 | -1.28% | 1.16x | MODERATE 56/100 | VERY_HIGH 72/100 | Do nothing |
| 4 | SUI/USD | 0.7131 | 91.66 | -0.45% | 0.53x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 5 | HYPE/USD | 67.14 | 90.99 | -0.86% | 0.75x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 6 | XRP/USD | 0.99131 | 90.59 | -0.95% | 0.77x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 7 | ADA/USD | 0.153546 | 86.73 | -0.80% | 0.47x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 8 | XDG/USD | 0.0585284 | 84.19 | -0.72% | 0.31x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 9 | LTC/USD | 42.55 | 83.29 | -0.61% | 0.20x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 10 | NEAR/USD | 3.1414 | 81.28 | -0.45% | 0.41x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 11 | QNT/USD | 160.46 | 81.02 | -0.54% | 0.30x | WEAK 41/100 | VERY_HIGH 82/100 | Watch |
| 12 | CC/USD | 0.07972 | 79.84 | +1.23% | 0.33x | STRONG 70/100 | VERY_HIGH 75/100 | Watch |

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
