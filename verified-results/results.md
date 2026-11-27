# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T14:52:03.887570+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46019384580
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7cdf6b7e6ccf1dde4807f7b62cbc570656540d33 (atomic ledger/results publication)
**Ledger generation:** 2022 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 604; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 728.85 | 97.942 | 92.155 | +6.92% | -1.84% | 5.15x | 15.7 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 2 | HYPE/USD | 63.76 | 77.705 | 69.973 | +2.48% | -1.45% | 6.24x | 4.7 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 69/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | LIGHTER/USD | 2.614 | 74.245 | 62.278 | +5.32% | -0.61% | 15.86x | 15.3 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | VVV/USD | 26.685 | 71.338 | 59.979 | +1.92% | -0.73% | 4.86x | 10.1 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 5 | KAVA/USD | 0.0271 | 70.741 | 57.579 | +8.84% | -0.37% | 3.36x | 36.9 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | PAXG/USD | 3628.55 | 67.687 | 53.949 | +2.02% | -0.25% | 14.08x | 3.4 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 7 | UNI/USD | 4.7288 | 65.477 | 59.760 | +1.69% | -1.86% | 15.51x | 9.7 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 63/100 | HIGH 65/100 | Do nothing | WATCH |
| 8 | XAUT/USD | 3631.4 | 63.148 | 49.566 | +2.01% | -0.28% | 216.48x | 2.2 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 9 | XDG/USD | 0.056821 | 59.196 | 53.179 | +0.79% | -1.80% | 5.99x | 1.5 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 60/100 | HIGH 65/100 | Do nothing | WATCH |
| 10 | FET/USD | 0.1253 | 59.184 | 51.658 | +4.07% | -1.49% | 7.42x | 23.9 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | RENDER/USD | 1.36 | 56.878 | 40.026 | +2.03% | +0.37% | 7.22x | 14.7 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Watch | WATCH |
| 12 | INJ/USD | 6.25 | 51.639 | 45.814 | +0.94% | -1.83% | 11.95x | 4.8 | 2026-11-27T14:51:55.554538+00:00 | Not calibrated | MODERATE 56/100 | HIGH 65/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 92.155 | 728.85 | -1.84% | 5.15x |
| 2 | HYPE/USD | 69.973 | 63.76 | -1.45% | 6.24x |
| 3 | LIGHTER/USD | 62.278 | 2.614 | -0.61% | 15.86x |
| 4 | VVV/USD | 59.979 | 26.685 | -0.73% | 4.86x |
| 5 | UNI/USD | 59.760 | 4.7288 | -1.86% | 15.51x |
| 6 | KAVA/USD | 57.579 | 0.0271 | -0.37% | 3.36x |
| 7 | PAXG/USD | 53.949 | 3628.55 | -0.25% | 14.08x |
| 8 | XDG/USD | 53.179 | 0.056821 | -1.80% | 5.99x |
| 9 | FET/USD | 51.658 | 0.1253 | -1.49% | 7.42x |
| 10 | XAUT/USD | 49.566 | 3631.4 | -0.28% | 216.48x |
| 11 | INJ/USD | 45.814 | 6.25 | -1.83% | 11.95x |
| 12 | RENDER/USD | 40.026 | 1.36 | +0.37% | 7.22x |

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

- Persisted scans: 2022; predictions: 17966; observations: 1224420.
- Matured sampled outcomes across 1/6/24/48h: 40121; gap abstentions: 25909. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46019384580 · **Generation:** 2022 · **Legacy run:** 46019384580
**Main quote time:** 2026-11-27T14:52:03.887570+00:00 · **Legacy report time:** 2026-11-27T14:52:42.423532+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 728.85 | 97.94 | -1.84% | 5.15x | STRONG 74/100 | VERY_HIGH 71/100 | Do nothing |
| 2 | HYPE/USD | 63.76 | 77.70 | -1.45% | 6.24x | MODERATE 69/100 | HIGH 65/100 | Do nothing |
| 3 | LIGHTER/USD | 2.614 | 74.24 | -0.61% | 15.86x | MODERATE 62/100 | VERY_HIGH 72/100 | Watch |
| 4 | VVV/USD | 26.685 | 71.34 | -0.73% | 4.86x | MODERATE 61/100 | HIGH 67/100 | Watch |
| 5 | KAVA/USD | 0.0271 | 70.74 | -0.37% | 3.36x | MODERATE 50/100 | EXTREME 85/100 | Do nothing |
| 6 | PAXG/USD | 3628.55 | 67.69 | -0.25% | 14.08x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 7 | UNI/USD | 4.7288 | 65.48 | -1.86% | 15.51x | MODERATE 63/100 | HIGH 65/100 | Do nothing |
| 8 | XAUT/USD | 3631.4 | 63.15 | -0.28% | 216.48x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 9 | XDG/USD | 0.056821 | 59.20 | -1.80% | 5.99x | MODERATE 60/100 | HIGH 65/100 | Do nothing |
| 10 | FET/USD | 0.1253 | 59.18 | -1.49% | 7.42x | MODERATE 50/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | RENDER/USD | 1.36 | 56.88 | +0.37% | 7.22x | STRONG 78/100 | HIGH 66/100 | Watch |
| 12 | INJ/USD | 6.25 | 51.64 | -1.83% | 11.95x | MODERATE 56/100 | HIGH 65/100 | Do nothing |

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
