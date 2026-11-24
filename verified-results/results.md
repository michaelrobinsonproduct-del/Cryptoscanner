# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T04:41:35.436472+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45327906798
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2d28e030e0df508985d17d4103507d11a581f606 (atomic ledger/results publication)
**Ledger generation:** 1526 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01289 | 83.703 | 77.746 | +11.89% | -0.93% | 2.06x | 15.6 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 2 | XRP/USD | 0.95435 | 83.363 | 65.676 | +1.59% | +0.54% | 4.00x | 0.9 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | INX/USD | 0.00412 | 76.233 | 59.167 | +5.70% | +3.16% | 1.13x | 24.4 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | MODERATE 63/100 | EXTREME 96/100 | Do nothing | WATCH |
| 4 | PEPE/USD | 3.514e-06 | 73.218 | 64.552 | +2.69% | +0.80% | 1.47x | 8.5 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | HYPE/USD | 63.84 | 72.986 | 56.416 | +0.31% | +0.31% | 3.23x | 1.6 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | AI/USD | 0.0163 | 72.444 | 73.099 | +7.03% | -0.18% | 1.03x | 6.2 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 7 | VVV/USD | 25.194 | 71.657 | 72.983 | +3.05% | +1.25% | 0.24x | 6.8 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0565185 | 69.140 | 57.007 | +0.38% | +0.56% | 1.93x | 1.3 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.017 | 68.544 | 62.078 | +1.20% | +0.99% | 1.15x | 2.7 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 10 | AAVE/USD | 97.9 | 66.882 | 52.442 | +0.88% | -0.11% | 4.79x | 4.1 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 11 | LINK/USD | 9.09378 | 64.971 | 60.449 | +0.99% | +0.52% | 1.19x | 2.9 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 12 | AVAX/USD | 6.812 | 64.450 | 47.168 | +0.52% | +0.46% | 6.43x | 4.4 | 2026-11-24T04:41:26.363647+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 77.746 | 0.01289 | -0.93% | 2.06x |
| 2 | AI/USD | 73.099 | 0.0163 | -0.18% | 1.03x |
| 3 | VVV/USD | 72.983 | 25.194 | +1.25% | 0.24x |
| 4 | XRP/USD | 65.676 | 0.95435 | +0.54% | 4.00x |
| 5 | PEPE/USD | 64.552 | 3.514e-06 | +0.80% | 1.47x |
| 6 | NEAR/USD | 62.078 | 3.017 | +0.99% | 1.15x |
| 7 | LINK/USD | 60.449 | 9.09378 | +0.52% | 1.19x |
| 8 | INX/USD | 59.167 | 0.00412 | +3.16% | 1.13x |
| 9 | XDG/USD | 57.007 | 0.0565185 | +0.56% | 1.93x |
| 10 | HYPE/USD | 56.416 | 63.84 | +0.31% | 3.23x |
| 11 | AAVE/USD | 52.442 | 97.9 | -0.11% | 4.79x |
| 12 | AVAX/USD | 47.168 | 6.812 | +0.46% | 6.43x |

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

- Persisted scans: 1526; predictions: 13045; observations: 924432.
- Matured sampled outcomes across 1/6/24/48h: 24335; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45327906798 · **Generation:** 1526 · **Legacy run:** 45327906798
**Main quote time:** 2026-11-24T04:41:35.436472+00:00 · **Legacy report time:** 2026-11-24T04:42:46.514687+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01289 | 83.70 | -0.93% | 2.06x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 2 | XRP/USD ⭐ | 0.95435 | 83.36 | +0.54% | 4.00x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | INX/USD ⭐ | 0.00412 | 76.23 | +3.16% | 1.13x | STRONG 73/100 | EXTREME 96/100 | Do nothing |
| 4 | PEPE/USD ⭐ | 3.514e-06 | 73.22 | +0.80% | 1.47x | STRONG 92/100 | HIGH 55/100 | Watch |
| 5 | HYPE/USD | 63.84 | 72.99 | +0.31% | 3.23x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 6 | AI/USD | 0.0163 | 72.44 | -0.18% | 1.03x | MODERATE 46/100 | VERY_HIGH 80/100 | Watch |
| 7 | VVV/USD | 25.194 | 71.66 | +1.25% | 0.24x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 8 | XDG/USD ⭐ | 0.0565185 | 69.14 | +0.56% | 1.93x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 9 | NEAR/USD ⭐ | 3.017 | 68.54 | +0.99% | 1.15x | STRONG 79/100 | HIGH 62/100 | Watch |
| 10 | AAVE/USD | 97.9 | 66.88 | -0.11% | 4.79x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 11 | LINK/USD ⭐ | 9.09378 | 64.97 | +0.52% | 1.19x | STRONG 77/100 | HIGH 62/100 | Watch |
| 12 | AVAX/USD | 6.812 | 64.45 | +0.46% | 6.43x | STRONG 87/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INX/USD ⭐ | 0.004115 | 79.39 | +3.16% | 1.13x | 2995 | STRONG 70/100 | EXTREME 96/100 | Do nothing |
| 2 | XRP/USD ⭐ | 0.95347 | 79.39 | +0.54% | 4.00x | 46917 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | BABY/USD | 0.00897 | 79.12 | +1.36% | 2.15x | 2610 | STRONG 85/100 | VERY_HIGH 79/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.507e-06 | 68.10 | +0.80% | 1.47x | 9367 | STRONG 84/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.8865 | 63.44 | +0.64% | 5.09x | 9303 | STRONG 87/100 | HIGH 55/100 | Watch |
| 6 | NEAR/USD ⭐ | 3.0144 | 61.64 | +0.99% | 1.15x | 23600 | STRONG 76/100 | HIGH 62/100 | Watch |
| 7 | XDG/USD ⭐ | 0.0564602 | 59.09 | +0.56% | 1.93x | 11148 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 8 | LINK/USD ⭐ | 9.08678 | 57.45 | +0.52% | 1.19x | 8869 | STRONG 74/100 | HIGH 62/100 | Watch |
| 9 | XMR/USD | 492.11 | 53.13 | +0.25% | 1.09x | 11838 | MODERATE 57/100 | HIGH 68/100 | Watch |

**Same-run overlap:** XRP/USD, INX/USD, PEPE/USD, XDG/USD, NEAR/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
