# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T10:45:56.124832+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45804137479
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1d139d3eab0e03ca287ef3b85c2614743df9cc2c (atomic ledger/results publication)
**Ledger generation:** 1850 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 585; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.94694 | 75.366 | 62.389 | +1.11% | -0.40% | 3.32x | 0.7 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SYRUP/USD | 0.07053 | 72.578 | 66.719 | +6.43% | +0.03% | 1.57x | 21.3 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | SEI/USD | 0.03557 | 71.127 | 71.708 | +6.78% | -0.61% | 1.25x | 11.2 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | CC/USD | 0.07974 | 69.132 | 55.444 | +2.96% | -0.26% | 4.24x | 1.3 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | MODERATE 65/100 | HIGH 66/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0564837 | 67.475 | 56.955 | +0.94% | -0.26% | 2.18x | 0.0 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | TAO/USD | 183.4781 | 64.262 | 57.934 | +1.04% | -0.42% | 1.84x | 8.7 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ADA/USD | 0.147714 | 61.152 | 62.846 | +1.33% | -0.52% | 1.09x | 3.0 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 8 | INJ/USD | 6.17 | 60.038 | 65.840 | +3.63% | -0.39% | 0.61x | 6.5 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | LINK/USD | 9.1916 | 59.484 | 65.116 | +1.63% | -0.45% | 0.66x | 2.5 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | LTC/USD | 43.31 | 57.076 | 63.679 | +1.40% | -0.55% | 0.62x | 2.3 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | DCR/USD | 10.546 | 48.960 | 33.865 | +0.53% | +0.02% | 4.40x | 1.9 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 12 | XMR/USD | 518.92 | 47.556 | 51.594 | +0.38% | -1.03% | 1.11x | 12.1 | 2026-11-26T10:45:49.448695+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 78/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SEI/USD | 71.708 | 0.03557 | -0.61% | 1.25x |
| 2 | SYRUP/USD | 66.719 | 0.07053 | +0.03% | 1.57x |
| 3 | INJ/USD | 65.840 | 6.17 | -0.39% | 0.61x |
| 4 | LINK/USD | 65.116 | 9.1916 | -0.45% | 0.66x |
| 5 | LTC/USD | 63.679 | 43.31 | -0.55% | 0.62x |
| 6 | ADA/USD | 62.846 | 0.147714 | -0.52% | 1.09x |
| 7 | XRP/USD | 62.389 | 0.94694 | -0.40% | 3.32x |
| 8 | TAO/USD | 57.934 | 183.4781 | -0.42% | 1.84x |
| 9 | XDG/USD | 56.955 | 0.0564837 | -0.26% | 2.18x |
| 10 | CC/USD | 55.444 | 0.07974 | -0.26% | 4.24x |
| 11 | XMR/USD | 51.594 | 518.92 | -1.03% | 1.11x |
| 12 | DCR/USD | 33.865 | 10.546 | +0.02% | 4.40x |

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

- Persisted scans: 1850; predictions: 15935; observations: 1121495.
- Matured sampled outcomes across 1/6/24/48h: 34514; gap abstentions: 24586. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45804137479 · **Generation:** 1850 · **Legacy run:** 45804137479
**Main quote time:** 2026-11-26T10:45:56.124832+00:00 · **Legacy report time:** 2026-11-26T10:47:02.803494+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.94694 | 75.37 | -0.40% | 3.32x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | SYRUP/USD | 0.07053 | 72.58 | +0.03% | 1.57x | MODERATE 61/100 | VERY_HIGH 72/100 | Watch |
| 3 | SEI/USD | 0.03557 | 71.13 | -0.61% | 1.25x | WEAK 41/100 | VERY_HIGH 79/100 | Watch |
| 4 | CC/USD | 0.07974 | 69.13 | -0.26% | 4.24x | MODERATE 65/100 | HIGH 66/100 | Watch |
| 5 | XDG/USD | 0.0564837 | 67.47 | -0.26% | 2.18x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | TAO/USD | 183.4781 | 64.26 | -0.42% | 1.84x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 7 | ADA/USD | 0.147714 | 61.15 | -0.52% | 1.09x | WEAK 41/100 | HIGH 68/100 | Watch |
| 8 | INJ/USD | 6.17 | 60.04 | -0.39% | 0.61x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | LINK/USD | 9.1916 | 59.48 | -0.45% | 0.66x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | LTC/USD | 43.31 | 57.08 | -0.55% | 0.62x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | DCR/USD | 10.546 | 48.96 | +0.02% | 4.40x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 12 | XMR/USD | 518.92 | 47.56 | -1.03% | 1.11x | WEAK 29/100 | VERY_HIGH 78/100 | Do nothing |

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
