# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T09:48:46.611295+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45794782622
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 149968fc7b5b110ef1f8d56f33c3935226d3aaa5 (atomic ledger/results publication)
**Ledger generation:** 1844 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 584; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SEI/USD | 0.03555 | 77.526 | 72.973 | +6.72% | +0.34% | 1.29x | 8.4 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | STRONG 74/100 | HIGH 60/100 | Watch | WATCH |
| 2 | INJ/USD | 6.255 | 75.040 | 76.423 | +5.06% | +0.84% | 0.44x | 4.8 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | LTC/USD | 43.78 | 73.873 | 71.394 | +2.51% | +0.48% | 1.01x | 2.3 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.07058 | 67.956 | 71.652 | +6.50% | -0.11% | 0.69x | 11.3 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | ADA/USD | 0.149178 | 64.531 | 69.890 | +2.34% | +0.40% | 0.27x | 3.0 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | LINK/USD | 9.254 | 63.563 | 70.273 | +2.32% | +0.34% | 0.16x | 1.9 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | QNT/USD | 148.21 | 59.910 | 63.992 | +2.35% | +0.31% | 0.44x | 3.4 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95332 | 59.580 | 67.474 | +1.79% | +0.15% | 0.13x | 0.1 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 60895.2 | 59.364 | 61.098 | +0.87% | +0.32% | 0.67x | 0.0 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 71.17 | 55.978 | 62.054 | +1.11% | +0.38% | 0.20x | 1.4 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0567558 | 54.020 | 60.128 | +1.42% | +0.27% | 0.26x | 0.5 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ETH/USD | 1702.57 | 53.652 | 60.006 | +0.72% | +0.35% | 0.19x | 0.1 | 2026-11-26T09:48:37.838597+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 76.423 | 6.255 | +0.84% | 0.44x |
| 2 | SEI/USD | 72.973 | 0.03555 | +0.34% | 1.29x |
| 3 | SYRUP/USD | 71.652 | 0.07058 | -0.11% | 0.69x |
| 4 | LTC/USD | 71.394 | 43.78 | +0.48% | 1.01x |
| 5 | LINK/USD | 70.273 | 9.254 | +0.34% | 0.16x |
| 6 | ADA/USD | 69.890 | 0.149178 | +0.40% | 0.27x |
| 7 | XRP/USD | 67.474 | 0.95332 | +0.15% | 0.13x |
| 8 | QNT/USD | 63.992 | 148.21 | +0.31% | 0.44x |
| 9 | SOL/USD | 62.054 | 71.17 | +0.38% | 0.20x |
| 10 | XBT/USD | 61.098 | 60895.2 | +0.32% | 0.67x |
| 11 | XDG/USD | 60.128 | 0.0567558 | +0.27% | 0.26x |
| 12 | ETH/USD | 60.006 | 1702.57 | +0.35% | 0.19x |

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

- Persisted scans: 1844; predictions: 15863; observations: 1117988.
- Matured sampled outcomes across 1/6/24/48h: 34370; gap abstentions: 24500. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45794782622 · **Generation:** 1844 · **Legacy run:** 45794782622
**Main quote time:** 2026-11-26T09:48:46.611295+00:00 · **Legacy report time:** 2026-11-26T09:49:51.696260+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD | 0.03555 | 77.53 | +0.34% | 1.29x | STRONG 74/100 | HIGH 60/100 | Watch |
| 2 | INJ/USD | 6.255 | 75.04 | +0.84% | 0.44x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 3 | LTC/USD ⭐ | 43.78 | 73.87 | +0.48% | 1.01x | STRONG 82/100 | HIGH 62/100 | Watch |
| 4 | SYRUP/USD | 0.07058 | 67.96 | -0.11% | 0.69x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 5 | ADA/USD | 0.149178 | 64.53 | +0.40% | 0.27x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 6 | LINK/USD | 9.254 | 63.56 | +0.34% | 0.16x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 7 | QNT/USD | 148.21 | 59.91 | +0.31% | 0.44x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.95332 | 59.58 | +0.15% | 0.13x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 60895.2 | 59.36 | +0.32% | 0.67x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 71.17 | 55.98 | +0.38% | 0.20x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0567558 | 54.02 | +0.27% | 0.26x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 12 | ETH/USD | 1702.57 | 53.65 | +0.35% | 0.19x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08068 | 77.05 | +0.65% | 2.16x | 5306 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 43.78 | 74.40 | +0.48% | 1.01x | 15525 | STRONG 82/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
