# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T22:06:48.990108+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45276067009
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a3668a85ec2500c5ded7924865efb698f1c2f111 (atomic ledger/results publication)
**Ledger generation:** 1487 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 157.4 | 106.953 | 98.095 | +9.73% | +0.02% | 1.88x | 3.8 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 2 | INJ/USD | 6.414 | 89.927 | 72.274 | +2.99% | +0.53% | 2.58x | 3.1 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SHX/USD | 0.003659 | 87.315 | 74.966 | +8.41% | +1.27% | 1.60x | 2.7 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | STRONG 89/100 | HIGH 67/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.6736 | 86.769 | 73.366 | +2.73% | +0.36% | 2.16x | 1.5 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ALGO/USD | 0.08155 | 84.362 | 91.917 | +8.11% | +0.26% | 0.12x | 6.1 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.2585 | 76.990 | 72.877 | +7.38% | -0.33% | 1.58x | 10.3 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | JUP/USD | 0.23731 | 76.607 | 70.463 | +5.67% | +0.25% | 1.49x | 9.7 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 8 | CC/USD | 0.07741 | 74.482 | 73.992 | +5.65% | +0.39% | 0.85x | 3.9 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 9 | SOL/USD | 72.22 | 70.334 | 70.066 | +2.25% | +0.22% | 0.92x | 1.4 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 10 | LTC/USD | 41.36 | 69.402 | 73.495 | +2.99% | +0.22% | 0.48x | 4.8 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XLM/USD | 0.130982 | 69.400 | 73.233 | +2.71% | +0.27% | 0.48x | 1.5 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | CAP/USD | 0.102327 | 67.981 | 76.108 | +9.36% | -0.28% | 0.33x | 6.1 | 2026-11-23T22:06:40.830604+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 98.095 | 157.4 | +0.02% | 1.88x |
| 2 | ALGO/USD | 91.917 | 0.08155 | +0.26% | 0.12x |
| 3 | CAP/USD | 76.108 | 0.102327 | -0.28% | 0.33x |
| 4 | SHX/USD | 74.966 | 0.003659 | +1.27% | 1.60x |
| 5 | CC/USD | 73.992 | 0.07741 | +0.39% | 0.85x |
| 6 | LTC/USD | 73.495 | 41.36 | +0.22% | 0.48x |
| 7 | SUI/USD | 73.366 | 0.6736 | +0.36% | 2.16x |
| 8 | XLM/USD | 73.233 | 0.130982 | +0.27% | 0.48x |
| 9 | ATOM/USD | 72.877 | 1.2585 | -0.33% | 1.58x |
| 10 | INJ/USD | 72.274 | 6.414 | +0.53% | 2.58x |
| 11 | JUP/USD | 70.463 | 0.23731 | +0.25% | 1.49x |
| 12 | SOL/USD | 70.066 | 72.22 | +0.22% | 0.92x |

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

- Persisted scans: 1487; predictions: 12611; observations: 900685.
- Matured sampled outcomes across 1/6/24/48h: 22756; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45276067009 · **Generation:** 1487 · **Legacy run:** 45276067009
**Main quote time:** 2026-11-23T22:06:48.990108+00:00 · **Legacy report time:** 2026-11-23T22:07:45.763531+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 157.4 | 106.95 | +0.02% | 1.88x | STRONG 85/100 | HIGH 55/100 | Watch |
| 2 | INJ/USD ⭐ | 6.414 | 89.93 | +0.53% | 2.58x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SHX/USD ⭐ | 0.003659 | 87.32 | +1.27% | 1.60x | STRONG 99/100 | HIGH 67/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.6736 | 86.77 | +0.36% | 2.16x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ALGO/USD | 0.08155 | 84.36 | +0.26% | 0.12x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 6 | ATOM/USD | 1.2585 | 76.99 | -0.33% | 1.58x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 7 | JUP/USD ⭐ | 0.23731 | 76.61 | +0.25% | 1.49x | STRONG 93/100 | HIGH 60/100 | Watch |
| 8 | CC/USD | 0.07741 | 74.48 | +0.39% | 0.85x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 9 | SOL/USD | 72.22 | 70.33 | +0.22% | 0.92x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 10 | LTC/USD | 41.36 | 69.40 | +0.22% | 0.48x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 11 | XLM/USD | 0.130982 | 69.40 | +0.27% | 0.48x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 12 | CAP/USD | 0.102327 | 67.98 | -0.28% | 0.33x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.405 | 86.52 | +0.53% | 2.58x | 9263 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SHX/USD ⭐ | 0.003659 | 83.71 | +1.27% | 1.60x | 2302 | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6714 | 80.49 | +0.36% | 2.16x | 12214 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | JUP/USD ⭐ | 0.23731 | 79.21 | +0.25% | 1.49x | 4008 | STRONG 95/100 | HIGH 60/100 | Watch |
| 5 | KAS/USD | 0.027 | 74.90 | +0.22% | 1.01x | 4200 | MODERATE 67/100 | HIGH 68/100 | Watch |
| 6 | WINGS/USD | 0.002064 | 74.80 | +0.44% | 1.52x | 6277 | STRONG 72/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** INJ/USD, SHX/USD, SUI/USD, JUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
