# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T05:50:21.859299+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44467805725
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** cb2534147de8b8aa39409e438ddf10471343f8d9 (atomic ledger/results publication)
**Ledger generation:** 769 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.799 | 91.864 | 87.594 | +5.21% | +1.07% | 0.89x | 7.5 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | STRONG 76/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ZEC/USD | 937.82 | 84.232 | 72.990 | +2.84% | +0.27% | 1.99x | 3.7 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TAO/USD | 194.7473 | 78.481 | 62.715 | +1.45% | +0.15% | 6.66x | 4.9 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SUI/USD | 0.7214 | 70.842 | 56.741 | +0.35% | -0.18% | 10.71x | 1.4 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | TRX/USD | 0.311776 | 62.565 | 47.191 | +0.81% | +0.07% | 26.12x | 0.0 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ETH/USD | 1795.3 | 62.288 | 63.074 | +1.16% | -0.05% | 0.95x | 0.1 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 7 | HYPE/USD | 67.9 | 61.773 | 64.203 | +1.53% | +0.13% | 0.69x | 2.9 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.3713 | 58.578 | 69.056 | +2.24% | -0.65% | 0.28x | 3.3 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | ADA/USD | 0.152748 | 56.652 | 60.309 | +0.99% | +0.13% | 0.57x | 3.2 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LTC/USD | 44.4 | 56.466 | 56.664 | +0.89% | -0.04% | 1.00x | 2.3 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 11 | SOL/USD | 74.47 | 56.239 | 63.181 | +1.26% | -0.01% | 0.31x | 1.3 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XBT/USD | 63242.2 | 54.140 | 57.856 | +0.41% | -0.11% | 0.69x | 0.0 | 2026-11-19T05:50:14.414835+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 87.594 | 22.799 | +1.07% | 0.89x |
| 2 | ZEC/USD | 72.990 | 937.82 | +0.27% | 1.99x |
| 3 | NEAR/USD | 69.056 | 3.3713 | -0.65% | 0.28x |
| 4 | HYPE/USD | 64.203 | 67.9 | +0.13% | 0.69x |
| 5 | SOL/USD | 63.181 | 74.47 | -0.01% | 0.31x |
| 6 | ETH/USD | 63.074 | 1795.3 | -0.05% | 0.95x |
| 7 | TAO/USD | 62.715 | 194.7473 | +0.15% | 6.66x |
| 8 | ADA/USD | 60.309 | 0.152748 | +0.13% | 0.57x |
| 9 | XBT/USD | 57.856 | 63242.2 | -0.11% | 0.69x |
| 10 | SUI/USD | 56.741 | 0.7214 | -0.18% | 10.71x |
| 11 | LTC/USD | 56.664 | 44.4 | -0.04% | 1.00x |
| 12 | TRX/USD | 47.191 | 0.311776 | +0.07% | 26.12x |

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

- Persisted scans: 769; predictions: 6372; observations: 465327.
- Matured sampled outcomes across 1/6/24/48h: 6399; gap abstentions: 13789. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44467805725 · **Generation:** 769 · **Legacy run:** 44467805725
**Main quote time:** 2026-11-19T05:50:21.859299+00:00 · **Legacy report time:** 2026-11-19T05:51:03.153538+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.799 | 91.86 | +1.07% | 0.89x | STRONG 76/100 | HIGH 62/100 | Watch |
| 2 | ZEC/USD ⭐ | 937.82 | 84.23 | +0.27% | 1.99x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD | 194.7473 | 78.48 | +0.15% | 6.66x | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | SUI/USD | 0.7214 | 70.84 | -0.18% | 10.71x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | TRX/USD | 0.311776 | 62.57 | +0.07% | 26.12x | STRONG 76/100 | HIGH 55/100 | Watch |
| 6 | ETH/USD | 1795.3 | 62.29 | -0.05% | 0.95x | WEAK 36/100 | HIGH 68/100 | Watch |
| 7 | HYPE/USD | 67.9 | 61.77 | +0.13% | 0.69x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 8 | NEAR/USD | 3.3713 | 58.58 | -0.65% | 0.28x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | ADA/USD | 0.152748 | 56.65 | +0.13% | 0.57x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 10 | LTC/USD | 44.4 | 56.47 | -0.04% | 1.00x | WEAK 38/100 | HIGH 68/100 | Watch |
| 11 | SOL/USD | 74.47 | 56.24 | -0.01% | 0.31x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XBT/USD | 63242.2 | 54.14 | -0.11% | 0.69x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 936.41 | 82.55 | +0.27% | 1.99x | 22299 | STRONG 96/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
