# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T03:51:31.517066+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45936394247
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0aa9cbdd35d3ed37b486867f76d0a1bd7a8cf953 (atomic ledger/results publication)
**Ledger generation:** 1955 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 752.42 | 92.893 | 97.811 | +10.38% | +0.26% | 0.38x | 4.4 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | HYPE/USD | 65.79 | 91.070 | 93.644 | +5.74% | -0.71% | 1.10x | 3.0 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | MODERATE 56/100 | HIGH 68/100 | Watch | WATCH |
| 3 | W/USD | 0.00965 | 78.834 | 67.004 | +9.53% | +1.58% | 1.39x | 20.7 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | VVV/USD | 26.977 | 76.433 | 72.521 | +3.03% | +0.43% | 1.18x | 7.4 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 5 | SOL/USD | 72.72 | 68.937 | 71.876 | +2.51% | -0.32% | 0.86x | 1.4 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XBT/USD | 61407.2 | 66.272 | 65.512 | +1.50% | -0.13% | 1.14x | 0.0 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ETH/USD | 1726.83 | 65.961 | 71.209 | +2.32% | -0.09% | 0.52x | 0.1 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XRP/USD | 0.96046 | 61.504 | 67.889 | +1.88% | -0.27% | 0.50x | 0.5 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | LINK/USD | 9.48924 | 60.536 | 70.385 | +2.38% | -0.19% | 0.11x | 2.6 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.097 | 56.498 | 64.018 | +1.61% | -0.27% | 0.38x | 4.5 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | SUI/USD | 0.6808 | 56.447 | 67.517 | +1.96% | -0.34% | 0.06x | 1.5 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | PEARL/USD | 1.8499 | 48.025 | 33.588 | +0.30% | -0.11% | 2.93x | 6.0 | 2026-11-27T03:51:23.921654+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.811 | 752.42 | +0.26% | 0.38x |
| 2 | HYPE/USD | 93.644 | 65.79 | -0.71% | 1.10x |
| 3 | VVV/USD | 72.521 | 26.977 | +0.43% | 1.18x |
| 4 | SOL/USD | 71.876 | 72.72 | -0.32% | 0.86x |
| 5 | ETH/USD | 71.209 | 1726.83 | -0.09% | 0.52x |
| 6 | LINK/USD | 70.385 | 9.48924 | -0.19% | 0.11x |
| 7 | XRP/USD | 67.889 | 0.96046 | -0.27% | 0.50x |
| 8 | SUI/USD | 67.517 | 0.6808 | -0.34% | 0.06x |
| 9 | W/USD | 67.004 | 0.00965 | +1.58% | 1.39x |
| 10 | XBT/USD | 65.512 | 61407.2 | -0.13% | 1.14x |
| 11 | NEAR/USD | 64.018 | 3.097 | -0.27% | 0.38x |
| 12 | PEARL/USD | 33.588 | 1.8499 | -0.11% | 2.93x |

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

- Persisted scans: 1955; predictions: 17162; observations: 1184039.
- Matured sampled outcomes across 1/6/24/48h: 37742; gap abstentions: 25488. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45936394247 · **Generation:** 1955 · **Legacy run:** 45936394247
**Main quote time:** 2026-11-27T03:51:31.517066+00:00 · **Legacy report time:** 2026-11-27T03:52:11.867948+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 752.42 | 92.89 | +0.26% | 0.38x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 2 | HYPE/USD | 65.79 | 91.07 | -0.71% | 1.10x | MODERATE 56/100 | HIGH 68/100 | Watch |
| 3 | W/USD | 0.00965 | 78.83 | +1.58% | 1.39x | STRONG 74/100 | VERY_HIGH 72/100 | Watch |
| 4 | VVV/USD ⭐ | 26.977 | 76.43 | +0.43% | 1.18x | STRONG 83/100 | HIGH 62/100 | Watch |
| 5 | SOL/USD | 72.72 | 68.94 | -0.32% | 0.86x | WEAK 39/100 | HIGH 68/100 | Watch |
| 6 | XBT/USD | 61407.2 | 66.27 | -0.13% | 1.14x | WEAK 43/100 | HIGH 68/100 | Watch |
| 7 | ETH/USD | 1726.83 | 65.96 | -0.09% | 0.52x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 8 | XRP/USD | 0.96046 | 61.50 | -0.27% | 0.50x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | LINK/USD | 9.48924 | 60.54 | -0.19% | 0.11x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | NEAR/USD | 3.097 | 56.50 | -0.27% | 0.38x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | SUI/USD | 0.6808 | 56.45 | -0.34% | 0.06x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | PEARL/USD | 1.8499 | 48.03 | -0.11% | 2.93x | MODERATE 54/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.977 | 75.38 | +0.43% | 1.18x | 13941 | STRONG 83/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
