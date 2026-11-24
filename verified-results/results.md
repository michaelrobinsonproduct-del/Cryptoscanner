# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T07:11:33.447921+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45345831685
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9dfc964a4026c1503501249dd8984eeacadceac4 (atomic ledger/results publication)
**Ledger generation:** 1542 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.543 | 97.314 | 84.592 | +4.48% | -0.46% | 9.11x | 3.5 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.546e-06 | 76.114 | 74.650 | +3.62% | -0.11% | 1.20x | 2.8 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.0388 | 75.596 | 66.386 | +1.93% | +0.30% | 1.77x | 4.3 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | HYPE/USD | 64.29 | 72.220 | 60.595 | +1.02% | +0.14% | 2.09x | 3.1 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 5 | BABY/USD | 0.00911 | 69.541 | 60.354 | +7.18% | +0.22% | 1.81x | 32.9 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04955 | 64.880 | 65.002 | +2.91% | +0.83% | 0.57x | 10.1 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | LINK/USD | 9.09373 | 62.262 | 60.330 | +0.99% | -0.05% | 1.22x | 3.1 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XMR/USD | 497.44 | 62.150 | 66.821 | +2.35% | -0.11% | 0.59x | 9.3 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | AI/USD | 0.01671 | 56.453 | 69.840 | +9.72% | -1.13% | 0.23x | 12.0 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | WEAK 28/100 | EXTREME 98/100 | Do nothing | WATCH |
| 10 | XRP/USD | 0.94742 | 56.323 | 60.456 | +0.85% | -0.21% | 0.69x | 1.1 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | WLD/USD | 0.2437 | 53.905 | 49.042 | +2.27% | -0.12% | 1.55x | 4.1 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | MODERATE 47/100 | HIGH 66/100 | Watch | WATCH |
| 12 | 2Z/USD | 0.01637 | 53.133 | 59.883 | +4.60% | -0.30% | 0.48x | 6.1 | 2026-11-24T07:11:24.722757+00:00 | Not calibrated | WEAK 32/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 84.592 | 25.543 | -0.46% | 9.11x |
| 2 | PEPE/USD | 74.650 | 3.546e-06 | -0.11% | 1.20x |
| 3 | AI/USD | 69.840 | 0.01671 | -1.13% | 0.23x |
| 4 | XMR/USD | 66.821 | 497.44 | -0.11% | 0.59x |
| 5 | NEAR/USD | 66.386 | 3.0388 | +0.30% | 1.77x |
| 6 | NIGHT/USD | 65.002 | 0.04955 | +0.83% | 0.57x |
| 7 | HYPE/USD | 60.595 | 64.29 | +0.14% | 2.09x |
| 8 | XRP/USD | 60.456 | 0.94742 | -0.21% | 0.69x |
| 9 | BABY/USD | 60.354 | 0.00911 | +0.22% | 1.81x |
| 10 | LINK/USD | 60.330 | 9.09373 | -0.05% | 1.22x |
| 11 | 2Z/USD | 59.883 | 0.01637 | -0.30% | 0.48x |
| 12 | WLD/USD | 49.042 | 0.2437 | -0.12% | 1.55x |

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

- Persisted scans: 1542; predictions: 13237; observations: 934176.
- Matured sampled outcomes across 1/6/24/48h: 24887; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
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

**Writer:** 45345831685 · **Generation:** 1542 · **Legacy run:** 45345831685
**Main quote time:** 2026-11-24T07:11:33.447921+00:00 · **Legacy report time:** 2026-11-24T07:12:23.391615+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.543 | 97.31 | -0.46% | 9.11x | STRONG 79/100 | HIGH 61/100 | Watch |
| 2 | PEPE/USD | 3.546e-06 | 76.11 | -0.11% | 1.20x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 3 | NEAR/USD ⭐ | 3.0388 | 75.60 | +0.30% | 1.77x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD ⭐ | 64.29 | 72.22 | +0.14% | 2.09x | STRONG 91/100 | HIGH 55/100 | Watch |
| 5 | BABY/USD ⭐ | 0.00911 | 69.54 | +0.22% | 1.81x | STRONG 80/100 | VERY_HIGH 72/100 | Watch |
| 6 | NIGHT/USD | 0.04955 | 64.88 | +0.83% | 0.57x | MODERATE 57/100 | VERY_HIGH 76/100 | Watch |
| 7 | LINK/USD | 9.09373 | 62.26 | -0.05% | 1.22x | WEAK 41/100 | HIGH 68/100 | Watch |
| 8 | XMR/USD | 497.44 | 62.15 | -0.11% | 0.59x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | AI/USD | 0.01671 | 56.45 | -1.13% | 0.23x | WEAK 28/100 | EXTREME 98/100 | Do nothing |
| 10 | XRP/USD | 0.94742 | 56.32 | -0.21% | 0.69x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | WLD/USD | 0.2437 | 53.91 | -0.12% | 1.55x | MODERATE 47/100 | HIGH 66/100 | Watch |
| 12 | 2Z/USD | 0.01637 | 53.13 | -0.30% | 0.48x | WEAK 32/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BAT/USD | 0.08061 | 77.74 | +0.80% | 1.36x | 3400 | STRONG 84/100 | HIGH 60/100 | Watch |
| 2 | BABY/USD ⭐ | 0.00911 | 74.99 | +0.22% | 1.81x | 3593 | STRONG 87/100 | HIGH 66/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.0388 | 71.26 | +0.30% | 1.77x | 22988 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD ⭐ | 64.24 | 61.88 | +0.14% | 2.09x | 30185 | STRONG 86/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, HYPE/USD, BABY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
