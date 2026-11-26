# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T03:36:29.834527+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45749796486
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ae77daddf4db3ec69695ead9df0883d24b58b07f (atomic ledger/results publication)
**Ledger generation:** 1807 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.14843 | 69.067 | 66.157 | +1.82% | +0.13% | 1.23x | 3.2 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 2 | SYRUP/USD | 0.06999 | 68.421 | 55.584 | +5.61% | +0.17% | 2.20x | 31.5 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | LTC/USD | 43.74 | 64.747 | 69.594 | +2.41% | +0.34% | 0.34x | 4.6 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | DOT/USD | 0.6709 | 60.644 | 45.644 | +1.91% | +0.00% | 3.70x | 1.5 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95461 | 60.027 | 68.439 | +1.93% | -0.24% | 0.28x | 0.1 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | QNT/USD | 145.23 | 59.044 | 45.896 | +0.30% | -0.37% | 9.70x | 8.3 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | AAVE/USD | 95.75 | 55.583 | 42.300 | +0.41% | -0.34% | 3.18x | 4.2 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0566632 | 54.694 | 58.178 | +1.26% | -0.11% | 0.70x | 0.9 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SUI/USD | 0.6728 | 54.031 | 61.086 | +0.98% | -0.04% | 0.32x | 1.5 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | SOL/USD | 70.95 | 53.763 | 59.864 | +0.80% | -0.28% | 0.53x | 1.4 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | PEPE/USD | 3.556e-06 | 51.678 | 58.361 | +2.07% | +0.23% | 0.22x | 2.8 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TAO/USD | 183.759 | 50.096 | 59.727 | +1.19% | -0.48% | 0.28x | 7.2 | 2026-11-26T03:36:21.679800+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 69.594 | 43.74 | +0.34% | 0.34x |
| 2 | XRP/USD | 68.439 | 0.95461 | -0.24% | 0.28x |
| 3 | ADA/USD | 66.157 | 0.14843 | +0.13% | 1.23x |
| 4 | SUI/USD | 61.086 | 0.6728 | -0.04% | 0.32x |
| 5 | SOL/USD | 59.864 | 70.95 | -0.28% | 0.53x |
| 6 | TAO/USD | 59.727 | 183.759 | -0.48% | 0.28x |
| 7 | PEPE/USD | 58.361 | 3.556e-06 | +0.23% | 0.22x |
| 8 | XDG/USD | 58.178 | 0.0566632 | -0.11% | 0.70x |
| 9 | SYRUP/USD | 55.584 | 0.06999 | +0.17% | 2.20x |
| 10 | QNT/USD | 45.896 | 145.23 | -0.37% | 9.70x |
| 11 | DOT/USD | 45.644 | 0.6709 | +0.00% | 3.70x |
| 12 | AAVE/USD | 42.300 | 95.75 | -0.34% | 3.18x |

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

- Persisted scans: 1807; predictions: 15419; observations: 1095507.
- Matured sampled outcomes across 1/6/24/48h: 33467; gap abstentions: 23792. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45749796486 · **Generation:** 1807 · **Legacy run:** 45749796486
**Main quote time:** 2026-11-26T03:36:29.834527+00:00 · **Legacy report time:** 2026-11-26T03:37:44.666386+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.14843 | 69.07 | +0.13% | 1.23x | STRONG 70/100 | HIGH 62/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.06999 | 68.42 | +0.17% | 2.20x | STRONG 79/100 | VERY_HIGH 72/100 | Watch |
| 3 | LTC/USD | 43.74 | 64.75 | +0.34% | 0.34x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 4 | DOT/USD | 0.6709 | 60.64 | +0.00% | 3.70x | STRONG 75/100 | HIGH 60/100 | Watch |
| 5 | XRP/USD | 0.95461 | 60.03 | -0.24% | 0.28x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 6 | QNT/USD | 145.23 | 59.04 | -0.37% | 9.70x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | AAVE/USD | 95.75 | 55.58 | -0.34% | 3.18x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | XDG/USD | 0.0566632 | 54.69 | -0.11% | 0.70x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SUI/USD | 0.6728 | 54.03 | -0.04% | 0.32x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | SOL/USD | 70.95 | 53.76 | -0.28% | 0.53x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | PEPE/USD | 3.556e-06 | 51.68 | +0.23% | 0.22x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 12 | TAO/USD | 183.759 | 50.10 | -0.48% | 0.28x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07006 | 76.52 | +0.17% | 2.20x | 3499 | STRONG 83/100 | VERY_HIGH 72/100 | Watch |
| 2 | DRV/USD | 0.36821 | 69.82 | +0.87% | 2.23x | 10763 | STRONG 80/100 | HIGH 67/100 | Watch |
| 3 | ADA/USD ⭐ | 0.148509 | 69.78 | +0.13% | 1.23x | 11342 | STRONG 70/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ADA/USD, SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
