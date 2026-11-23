# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T17:51:42.200195+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45231806760
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ca36dfd5c4d5f3f0feb61ae63adb155a1d174915 (atomic ledger/results publication)
**Ledger generation:** 1462 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.6898 | 96.435 | 90.678 | +5.20% | -1.31% | 2.23x | 1.5 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | STRONG 78/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | INJ/USD | 6.629 | 94.086 | 96.313 | +6.44% | -1.94% | 1.75x | 3.0 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | MODERATE 67/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | LTC/USD | 42 | 89.149 | 83.497 | +4.58% | -0.59% | 1.86x | 7.1 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | UNI/USD | 4.9283 | 80.850 | 85.471 | +5.28% | -1.26% | 1.17x | 4.6 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 5 | XRP/USD | 0.95747 | 79.891 | 77.170 | +3.23% | -0.96% | 1.75x | 0.8 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 73.6 | 78.706 | 83.756 | +4.21% | -0.81% | 0.90x | 1.4 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ADA/USD | 0.150454 | 77.981 | 80.930 | +4.05% | -0.97% | 1.19x | 4.8 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 8 | PAXG/USD | 3639.88 | 77.699 | 64.905 | +1.89% | -0.44% | 5.22x | 0.0 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 9 | HYPE/USD | 65.73 | 76.533 | 83.877 | +4.23% | -0.76% | 0.64x | 1.5 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | PENGU/USD | 0.004532 | 75.603 | 76.680 | +6.29% | -1.27% | 1.53x | 4.4 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0573112 | 73.511 | 80.662 | +3.67% | -1.25% | 0.91x | 0.0 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 12 | HBAR/USD | 0.05402 | 72.148 | 69.824 | +4.69% | -1.01% | 1.74x | 1.9 | 2026-11-23T17:51:35.753163+00:00 | Not calibrated | MODERATE 56/100 | HIGH 65/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 96.313 | 6.629 | -1.94% | 1.75x |
| 2 | SUI/USD | 90.678 | 0.6898 | -1.31% | 2.23x |
| 3 | UNI/USD | 85.471 | 4.9283 | -1.26% | 1.17x |
| 4 | HYPE/USD | 83.877 | 65.73 | -0.76% | 0.64x |
| 5 | SOL/USD | 83.756 | 73.6 | -0.81% | 0.90x |
| 6 | LTC/USD | 83.497 | 42 | -0.59% | 1.86x |
| 7 | ADA/USD | 80.930 | 0.150454 | -0.97% | 1.19x |
| 8 | XDG/USD | 80.662 | 0.0573112 | -1.25% | 0.91x |
| 9 | XRP/USD | 77.170 | 0.95747 | -0.96% | 1.75x |
| 10 | PENGU/USD | 76.680 | 0.004532 | -1.27% | 1.53x |
| 11 | HBAR/USD | 69.824 | 0.05402 | -1.01% | 1.74x |
| 12 | PAXG/USD | 64.905 | 3639.88 | -0.44% | 5.22x |

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

- Persisted scans: 1462; predictions: 12311; observations: 885460.
- Matured sampled outcomes across 1/6/24/48h: 21520; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45231806760 · **Generation:** 1462 · **Legacy run:** 45231806760
**Main quote time:** 2026-11-23T17:51:42.200195+00:00 · **Legacy report time:** 2026-11-23T17:52:50.730668+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD | 0.6898 | 96.43 | -1.31% | 2.23x | STRONG 78/100 | HIGH 65/100 | Do nothing |
| 2 | INJ/USD | 6.629 | 94.09 | -1.94% | 1.75x | MODERATE 67/100 | HIGH 65/100 | Do nothing |
| 3 | LTC/USD | 42 | 89.15 | -0.59% | 1.86x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | UNI/USD | 4.9283 | 80.85 | -1.26% | 1.17x | MODERATE 50/100 | VERY_HIGH 72/100 | Do nothing |
| 5 | XRP/USD | 0.95747 | 79.89 | -0.96% | 1.75x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD | 73.6 | 78.71 | -0.81% | 0.90x | WEAK 44/100 | HIGH 68/100 | Watch |
| 7 | ADA/USD | 0.150454 | 77.98 | -0.97% | 1.19x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 8 | PAXG/USD | 3639.88 | 77.70 | -0.44% | 5.22x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 9 | HYPE/USD | 65.73 | 76.53 | -0.76% | 0.64x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 10 | PENGU/USD | 0.004532 | 75.60 | -1.27% | 1.53x | MODERATE 58/100 | VERY_HIGH 70/100 | Do nothing |
| 11 | XDG/USD | 0.0573112 | 73.51 | -1.25% | 0.91x | WEAK 42/100 | VERY_HIGH 72/100 | Do nothing |
| 12 | HBAR/USD | 0.05402 | 72.15 | -1.01% | 1.74x | MODERATE 56/100 | HIGH 65/100 | Watch |

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
