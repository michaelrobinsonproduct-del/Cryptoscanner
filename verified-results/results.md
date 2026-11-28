# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T03:17:28.258116+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46101889774
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1f16060446aac383dc198f033acd5b8f79989443 (atomic ledger/results publication)
**Ledger generation:** 2098 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0499 | 66.896 | 60.056 | +1.05% | +0.50% | 1.43x | 4.6 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 750.9 | 66.131 | 68.162 | +2.22% | +0.37% | 0.61x | 4.8 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.38 | 57.434 | 64.036 | +1.40% | +0.16% | 0.26x | 1.6 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XMR/USD | 414.5 | 56.722 | 54.139 | +1.78% | +0.33% | 1.09x | 26.6 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | VVV/USD | 26.147 | 55.054 | 53.414 | +1.55% | +0.26% | 1.04x | 8.4 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ONDO/USD | 0.28811 | 46.208 | 31.728 | +0.35% | -0.10% | 4.94x | 10.8 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | BCH/USD | 209.27 | 44.883 | 43.650 | +1.10% | +0.22% | 1.01x | 2.9 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 8 | CC/USD | 0.07575 | 44.833 | 45.026 | +2.16% | +0.37% | 0.79x | 9.2 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 52/100 | HIGH 67/100 | Watch | WATCH |
| 9 | SENT/USD | 0.024223 | 43.687 | 45.499 | +2.15% | +0.62% | 0.51x | 0.8 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | SEI/USD | 0.03881 | 40.444 | 34.815 | +1.04% | +1.46% | 0.83x | 10.3 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 11 | SPX/USD | 0.2741 | 34.325 | 23.506 | +0.62% | +0.44% | 1.86x | 25.6 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 12 | SHX/USD | 0.003366 | 25.113 | 15.108 | +0.54% | +0.15% | 1.93x | 38.7 | 2026-11-28T03:17:20.716782+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 68.162 | 750.9 | +0.37% | 0.61x |
| 2 | HYPE/USD | 64.036 | 64.38 | +0.16% | 0.26x |
| 3 | NEAR/USD | 60.056 | 3.0499 | +0.50% | 1.43x |
| 4 | XMR/USD | 54.139 | 414.5 | +0.33% | 1.09x |
| 5 | VVV/USD | 53.414 | 26.147 | +0.26% | 1.04x |
| 6 | SENT/USD | 45.499 | 0.024223 | +0.62% | 0.51x |
| 7 | CC/USD | 45.026 | 0.07575 | +0.37% | 0.79x |
| 8 | BCH/USD | 43.650 | 209.27 | +0.22% | 1.01x |
| 9 | SEI/USD | 34.815 | 0.03881 | +1.46% | 0.83x |
| 10 | ONDO/USD | 31.728 | 0.28811 | -0.10% | 4.94x |
| 11 | SPX/USD | 23.506 | 0.2741 | +0.44% | 1.86x |
| 12 | SHX/USD | 15.108 | 0.003366 | +0.15% | 1.93x |

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

- Persisted scans: 2098; predictions: 18835; observations: 1270434.
- Matured sampled outcomes across 1/6/24/48h: 43502; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46101889774 · **Generation:** 2098 · **Legacy run:** 46101889774
**Main quote time:** 2026-11-28T03:17:28.258116+00:00 · **Legacy report time:** 2026-11-28T03:18:12.615712+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0499 | 66.90 | +0.50% | 1.43x | STRONG 88/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 750.9 | 66.13 | +0.37% | 0.61x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD | 64.38 | 57.43 | +0.16% | 0.26x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 4 | XMR/USD ⭐ | 414.5 | 56.72 | +0.33% | 1.09x | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |
| 5 | VVV/USD ⭐ | 26.147 | 55.05 | +0.26% | 1.04x | STRONG 73/100 | HIGH 62/100 | Watch |
| 6 | ONDO/USD | 0.28811 | 46.21 | -0.10% | 4.94x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 7 | BCH/USD ⭐ | 209.27 | 44.88 | +0.22% | 1.01x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 8 | CC/USD | 0.07575 | 44.83 | +0.37% | 0.79x | MODERATE 52/100 | HIGH 67/100 | Watch |
| 9 | SENT/USD | 0.024223 | 43.69 | +0.62% | 0.51x | MODERATE 52/100 | VERY_HIGH 82/100 | Watch |
| 10 | SEI/USD | 0.03881 | 40.44 | +1.46% | 0.83x | MODERATE 45/100 | VERY_HIGH 73/100 | Watch |
| 11 | SPX/USD | 0.2741 | 34.32 | +0.44% | 1.86x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 12 | SHX/USD | 0.003366 | 25.11 | +0.15% | 1.93x | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 415.77 | 63.41 | +0.33% | 1.09x | 14686 | MODERATE 67/100 | VERY_HIGH 74/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.0499 | 61.28 | +0.50% | 1.43x | 13099 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD ⭐ | 26.147 | 51.54 | +0.26% | 1.04x | 8545 | STRONG 71/100 | HIGH 62/100 | Watch |
| 4 | BCH/USD ⭐ | 209.27 | 50.53 | +0.22% | 1.01x | 2983 | STRONG 70/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NEAR/USD, XMR/USD, VVV/USD, BCH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
