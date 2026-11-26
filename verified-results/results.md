# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T04:06:01.300051+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45752876468
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f6629338db620a83dd57c83c6b7f76800101036c (atomic ledger/results publication)
**Ledger generation:** 1810 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.21134 | 77.998 | 64.371 | +1.84% | +0.05% | 2.34x | 2.7 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SOL/USD | 71.12 | 76.627 | 61.557 | +1.04% | +0.01% | 2.62x | 1.4 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LTC/USD | 43.92 | 75.693 | 73.693 | +2.83% | -0.05% | 1.22x | 2.3 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XRP/USD | 0.96017 | 71.064 | 72.022 | +2.52% | +0.02% | 0.89x | 1.2 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XBT/USD | 60904 | 68.681 | 61.200 | +0.89% | +0.09% | 1.70x | 0.0 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6734 | 67.381 | 60.975 | +1.07% | -0.13% | 1.71x | 3.0 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 7 | BABY/USD | 0.00916 | 65.396 | 61.602 | +5.17% | -2.24% | 15.64x | 10.9 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 8 | XMR/USD | 518.65 | 64.459 | 56.434 | +0.33% | +0.09% | 1.76x | 1.7 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 9 | HBAR/USD | 0.05328 | 63.810 | 51.702 | +2.26% | -0.58% | 5.24x | 1.9 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ADA/USD | 0.148932 | 63.477 | 67.969 | +2.17% | -0.12% | 0.61x | 4.4 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | TAO/USD | 184.2841 | 61.957 | 62.649 | +1.48% | -0.02% | 0.94x | 5.5 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0570232 | 60.217 | 62.486 | +1.90% | +0.04% | 0.75x | 2.1 | 2026-11-26T04:05:53.627513+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 73.693 | 43.92 | -0.05% | 1.22x |
| 2 | XRP/USD | 72.022 | 0.96017 | +0.02% | 0.89x |
| 3 | ADA/USD | 67.969 | 0.148932 | -0.12% | 0.61x |
| 4 | LINK/USD | 64.371 | 9.21134 | +0.05% | 2.34x |
| 5 | TAO/USD | 62.649 | 184.2841 | -0.02% | 0.94x |
| 6 | XDG/USD | 62.486 | 0.0570232 | +0.04% | 0.75x |
| 7 | BABY/USD | 61.602 | 0.00916 | -2.24% | 15.64x |
| 8 | SOL/USD | 61.557 | 71.12 | +0.01% | 2.62x |
| 9 | XBT/USD | 61.200 | 60904 | +0.09% | 1.70x |
| 10 | SUI/USD | 60.975 | 0.6734 | -0.13% | 1.71x |
| 11 | XMR/USD | 56.434 | 518.65 | +0.09% | 1.76x |
| 12 | HBAR/USD | 51.702 | 0.05328 | -0.58% | 5.24x |

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

- Persisted scans: 1810; predictions: 15455; observations: 1097334.
- Matured sampled outcomes across 1/6/24/48h: 33539; gap abstentions: 23826. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45752876468 · **Generation:** 1810 · **Legacy run:** 45752876468
**Main quote time:** 2026-11-26T04:06:01.300051+00:00 · **Legacy report time:** 2026-11-26T04:07:01.861512+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.21134 | 78.00 | +0.05% | 2.34x | STRONG 84/100 | HIGH 55/100 | Watch |
| 2 | SOL/USD | 71.12 | 76.63 | +0.01% | 2.62x | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD | 43.92 | 75.69 | -0.05% | 1.22x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 4 | XRP/USD | 0.96017 | 71.06 | +0.02% | 0.89x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 5 | XBT/USD | 60904 | 68.68 | +0.09% | 1.70x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 6 | SUI/USD | 0.6734 | 67.38 | -0.13% | 1.71x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 7 | BABY/USD | 0.00916 | 65.40 | -2.24% | 15.64x | MODERATE 58/100 | VERY_HIGH 83/100 | Do nothing |
| 8 | XMR/USD | 518.65 | 64.46 | +0.09% | 1.76x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 9 | HBAR/USD | 0.05328 | 63.81 | -0.58% | 5.24x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 10 | ADA/USD | 0.148932 | 63.48 | -0.12% | 0.61x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | TAO/USD | 184.2841 | 61.96 | -0.02% | 0.94x | WEAK 36/100 | HIGH 68/100 | Watch |
| 12 | XDG/USD | 0.0570232 | 60.22 | +0.04% | 0.75x | MODERATE 50/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD | 0.07209 | 76.42 | +1.60% | 1.09x | 3567 | MODERATE 63/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
