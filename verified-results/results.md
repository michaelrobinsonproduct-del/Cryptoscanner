# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:10:15.691619+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44321199425
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 5b2c11b22120b1ffc169d54a8c10014759e2784f (atomic ledger/results publication)
**Ledger generation:** 585 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05501 | 86.618 | 69.794 | +6.53% | +0.36% | 3.48x | 12.7 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | STRONG 93/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04709 | 78.015 | 77.605 | +4.90% | +0.73% | 0.68x | 10.6 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SENT/USD | 0.019443 | 67.121 | 55.971 | +4.15% | +0.55% | 1.84x | 8.2 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | STRONG 79/100 | HIGH 67/100 | Watch | WATCH |
| 4 | VVV/USD | 21.256 | 54.367 | 53.977 | +1.09% | +0.01% | 1.03x | 4.2 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 5 | CAP/USD | 0.102263 | 52.583 | 38.125 | +1.28% | -0.11% | 3.69x | 4.2 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | XRP/USD | 0.987 | 50.679 | 57.222 | +0.45% | +0.20% | 0.25x | 1.9 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | TRX/USD | 0.309613 | 49.815 | 45.338 | +0.56% | -0.02% | 1.46x | 0.5 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 8 | USELESS/USD | 0.09976 | 48.531 | 55.367 | +2.23% | +0.05% | 0.29x | 4.0 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5201 | 39.074 | 46.341 | +2.12% | -0.29% | 0.42x | 1.9 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | CC/USD | 0.08315 | 35.733 | 41.088 | +1.24% | +0.13% | 0.40x | 6.0 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | PEARL/USD | 1.8379 | 33.489 | 40.142 | +1.51% | -0.14% | 0.40x | 17.5 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 12 | W/USD | 0.009 | 29.877 | 31.637 | +0.78% | -0.44% | 1.05x | 11.1 | 2026-11-18T14:10:07.111948+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 77.605 | 0.04709 | +0.73% | 0.68x |
| 2 | MEGA/USD | 69.794 | 0.05501 | +0.36% | 3.48x |
| 3 | XRP/USD | 57.222 | 0.987 | +0.20% | 0.25x |
| 4 | SENT/USD | 55.971 | 0.019443 | +0.55% | 1.84x |
| 5 | USELESS/USD | 55.367 | 0.09976 | +0.05% | 0.29x |
| 6 | VVV/USD | 53.977 | 21.256 | +0.01% | 1.03x |
| 7 | AKT/USD | 46.341 | 0.5201 | -0.29% | 0.42x |
| 8 | TRX/USD | 45.338 | 0.309613 | -0.02% | 1.46x |
| 9 | CC/USD | 41.088 | 0.08315 | +0.13% | 0.40x |
| 10 | PEARL/USD | 40.142 | 1.8379 | -0.14% | 0.40x |
| 11 | CAP/USD | 38.125 | 0.102263 | -0.11% | 3.69x |
| 12 | W/USD | 31.637 | 0.009 | -0.44% | 1.05x |

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

- Persisted scans: 585; predictions: 4974; observations: 353272.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13117. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44321199425 · **Generation:** 585 · **Legacy run:** 44321199425
**Main quote time:** 2026-11-18T14:10:15.691619+00:00 · **Legacy report time:** 2026-11-18T14:10:43.341131+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05501 | 86.62 | +0.36% | 3.48x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | NIGHT/USD | 0.04709 | 78.01 | +0.73% | 0.68x | MODERATE 64/100 | VERY_HIGH 76/100 | Watch |
| 3 | SENT/USD ⭐ | 0.019443 | 67.12 | +0.55% | 1.84x | STRONG 89/100 | HIGH 67/100 | Consider small entry |
| 4 | VVV/USD | 21.256 | 54.37 | +0.01% | 1.03x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 5 | CAP/USD | 0.102263 | 52.58 | -0.11% | 3.69x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 6 | XRP/USD | 0.987 | 50.68 | +0.20% | 0.25x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 7 | TRX/USD | 0.309613 | 49.82 | -0.02% | 1.46x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 8 | USELESS/USD | 0.09976 | 48.53 | +0.05% | 0.29x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 9 | AKT/USD | 0.5201 | 39.07 | -0.29% | 0.42x | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | CC/USD | 0.08315 | 35.73 | +0.13% | 0.40x | WEAK 38/100 | VERY_HIGH 75/100 | Watch |
| 11 | PEARL/USD | 1.8379 | 33.49 | -0.14% | 0.40x | WEAK 17/100 | VERY_HIGH 82/100 | Do nothing |
| 12 | W/USD | 0.009 | 29.88 | -0.44% | 1.05x | WEAK 20/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019443 | 79.32 | +0.55% | 1.84x | 5677 | STRONG 95/100 | HIGH 67/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.05501 | 68.23 | +0.36% | 3.48x | 1252 | STRONG 89/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** MEGA/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
