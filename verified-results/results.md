# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T16:01:08.301847+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45854475927
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4ccb61395fb12a5ec10392368f679416ebc5ef07 (atomic ledger/results publication)
**Ledger generation:** 1882 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5024 | 83.675 | 68.276 | +6.19% | +0.08% | 2.85x | 15.9 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | STRONG 82/100 | HIGH 66/100 | Watch | WATCH |
| 2 | KNTQ/USD | 0.16094 | 76.964 | 71.889 | +6.27% | +0.73% | 1.14x | 6.8 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | FET/USD | 0.116 | 74.850 | 69.855 | +6.91% | +0.78% | 1.11x | 17.3 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | STBL/USD | 0.021152 | 72.011 | 67.694 | +12.00% | +1.93% | 0.47x | 16.5 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 61/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | SKY/USD | 0.04563 | 69.816 | 72.906 | +8.95% | +0.07% | 0.66x | 13.2 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | LTC/USD | 43.44 | 58.345 | 65.813 | +1.71% | +0.14% | 0.18x | 2.3 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | LINK/USD | 9.18544 | 57.475 | 63.838 | +1.56% | +0.34% | 0.19x | 4.1 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ADA/USD | 0.14824 | 57.225 | 64.199 | +1.69% | +0.25% | 0.18x | 5.3 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94801 | 57.026 | 62.925 | +1.22% | +0.21% | 0.31x | 1.3 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 60689.9 | 55.255 | 58.717 | +0.53% | +0.29% | 0.51x | 0.0 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.0607 | 54.703 | 55.519 | +0.35% | +0.95% | 0.44x | 3.9 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SOL/USD | 71.02 | 52.888 | 59.857 | +0.90% | +0.40% | 0.11x | 2.8 | 2026-11-26T16:01:00.314220+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 72.906 | 0.04563 | +0.07% | 0.66x |
| 2 | KNTQ/USD | 71.889 | 0.16094 | +0.73% | 1.14x |
| 3 | FET/USD | 69.855 | 0.116 | +0.78% | 1.11x |
| 4 | AKT/USD | 68.276 | 0.5024 | +0.08% | 2.85x |
| 5 | STBL/USD | 67.694 | 0.021152 | +1.93% | 0.47x |
| 6 | LTC/USD | 65.813 | 43.44 | +0.14% | 0.18x |
| 7 | ADA/USD | 64.199 | 0.14824 | +0.25% | 0.18x |
| 8 | LINK/USD | 63.838 | 9.18544 | +0.34% | 0.19x |
| 9 | XRP/USD | 62.925 | 0.94801 | +0.21% | 0.31x |
| 10 | SOL/USD | 59.857 | 71.02 | +0.40% | 0.11x |
| 11 | XBT/USD | 58.717 | 60689.9 | +0.29% | 0.51x |
| 12 | NEAR/USD | 55.519 | 3.0607 | +0.95% | 0.44x |

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

- Persisted scans: 1882; predictions: 16319; observations: 1140333.
- Matured sampled outcomes across 1/6/24/48h: 35270; gap abstentions: 25037. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45854475927 · **Generation:** 1882 · **Legacy run:** 45854475927
**Main quote time:** 2026-11-26T16:01:08.301847+00:00 · **Legacy report time:** 2026-11-26T16:01:45.382279+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5024 | 83.68 | +0.08% | 2.85x | STRONG 92/100 | HIGH 66/100 | Watch |
| 2 | KNTQ/USD ⭐ | 0.16094 | 76.96 | +0.73% | 1.14x | STRONG 83/100 | VERY_HIGH 74/100 | Watch |
| 3 | FET/USD ⭐ | 0.116 | 74.85 | +0.78% | 1.11x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 4 | STBL/USD | 0.021152 | 72.01 | +1.93% | 0.47x | MODERATE 61/100 | EXTREME 88/100 | Do nothing |
| 5 | SKY/USD | 0.04563 | 69.82 | +0.07% | 0.66x | MODERATE 50/100 | VERY_HIGH 81/100 | Watch |
| 6 | LTC/USD | 43.44 | 58.35 | +0.14% | 0.18x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 7 | LINK/USD | 9.18544 | 57.47 | +0.34% | 0.19x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 8 | ADA/USD | 0.14824 | 57.23 | +0.25% | 0.18x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 9 | XRP/USD | 0.94801 | 57.03 | +0.21% | 0.31x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 60689.9 | 55.26 | +0.29% | 0.51x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 11 | NEAR/USD | 3.0607 | 54.70 | +0.95% | 0.44x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 12 | SOL/USD | 71.02 | 52.89 | +0.40% | 0.11x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5024 | 79.36 | +0.08% | 2.85x | 2904 | STRONG 90/100 | HIGH 66/100 | Watch |
| 2 | KNTQ/USD ⭐ | 0.16094 | 78.11 | +0.73% | 1.14x | 1530 | STRONG 84/100 | VERY_HIGH 74/100 | Watch |
| 3 | FET/USD ⭐ | 0.1163 | 71.18 | +0.78% | 1.11x | 2194 | STRONG 71/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** AKT/USD, KNTQ/USD, FET/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
