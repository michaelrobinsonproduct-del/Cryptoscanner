# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:35:19.207322+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44556339830
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 7022d0a76958058c5037b20478d88825f5b1a815 (atomic ledger/results publication)
**Ledger generation:** 803 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUST/USD | 0.05479 | 86.391 | 70.642 | +11.36% | +3.97% | 0.59x | 11.0 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | MODERATE 68/100 | EXTREME 98/100 | Do nothing | WATCH |
| 2 | VVV/USD | 22.643 | 78.126 | 82.643 | +4.49% | -1.60% | 1.35x | 7.5 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | MODERATE 59/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | PYTH/USD | 0.05644 | 70.910 | 70.968 | +6.97% | +0.12% | 0.93x | 12.4 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | HYPE/USD | 68.2 | 62.344 | 67.349 | +1.97% | -0.29% | 0.65x | 2.9 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5482 | 59.974 | 63.166 | +5.83% | -0.35% | 0.85x | 18.3 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | WEAK 30/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | SKR/USD | 0.01033 | 58.823 | 69.701 | +7.24% | -1.16% | 0.49x | 12.6 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | WEAK 29/100 | EXTREME 98/100 | Do nothing | WATCH |
| 7 | XRP/USD | 0.97485 | 57.018 | 61.091 | +0.88% | -0.58% | 0.88x | 0.1 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | SOL/USD | 74.22 | 56.946 | 60.799 | +0.92% | -0.26% | 0.74x | 1.3 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | USELESS/USD | 0.10247 | 55.329 | 70.442 | +7.23% | -1.32% | 0.15x | 23.4 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | WEAK 23/100 | EXTREME 92/100 | Do nothing | WATCH |
| 10 | SYRUP/USD | 0.1036 | 53.708 | 66.223 | +9.10% | -1.34% | 0.42x | 20.3 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | WEAK 22/100 | EXTREME 100/100 | Do nothing | WATCH |
| 11 | BNB/USD | 586.75 | 43.350 | 47.173 | +0.94% | -0.34% | 0.79x | 2.0 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | WEAK 27/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | CSPR/USD | 0.00167 | 40.104 | 46.708 | +2.26% | -0.26% | 0.47x | 0.6 | 2026-11-19T15:35:11.026258+00:00 | Not calibrated | WEAK 25/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.643 | 22.643 | -1.60% | 1.35x |
| 2 | PYTH/USD | 70.968 | 0.05644 | +0.12% | 0.93x |
| 3 | TRUST/USD | 70.642 | 0.05479 | +3.97% | 0.59x |
| 4 | USELESS/USD | 70.442 | 0.10247 | -1.32% | 0.15x |
| 5 | SKR/USD | 69.701 | 0.01033 | -1.16% | 0.49x |
| 6 | HYPE/USD | 67.349 | 68.2 | -0.29% | 0.65x |
| 7 | SYRUP/USD | 66.223 | 0.1036 | -1.34% | 0.42x |
| 8 | AKT/USD | 63.166 | 0.5482 | -0.35% | 0.85x |
| 9 | XRP/USD | 61.091 | 0.97485 | -0.58% | 0.88x |
| 10 | SOL/USD | 60.799 | 74.22 | -0.26% | 0.74x |
| 11 | BNB/USD | 47.173 | 586.75 | -0.34% | 0.79x |
| 12 | CSPR/USD | 46.708 | 0.00167 | -0.26% | 0.47x |

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

- Persisted scans: 803; predictions: 6780; observations: 485623.
- Matured sampled outcomes across 1/6/24/48h: 6779; gap abstentions: 15225. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44556339830 · **Generation:** 803 · **Legacy run:** 44556339830
**Main quote time:** 2026-11-19T15:35:19.207322+00:00 · **Legacy report time:** 2026-11-19T15:35:56.498573+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD | 0.05479 | 86.39 | +3.97% | 0.59x | MODERATE 68/100 | EXTREME 98/100 | Do nothing |
| 2 | VVV/USD | 22.643 | 78.13 | -1.60% | 1.35x | MODERATE 59/100 | HIGH 65/100 | Do nothing |
| 3 | PYTH/USD | 0.05644 | 70.91 | +0.12% | 0.93x | MODERATE 50/100 | VERY_HIGH 73/100 | Watch |
| 4 | HYPE/USD | 68.2 | 62.34 | -0.29% | 0.65x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 5 | AKT/USD | 0.5482 | 59.97 | -0.35% | 0.85x | WEAK 30/100 | EXTREME 86/100 | Do nothing |
| 6 | SKR/USD | 0.01033 | 58.82 | -1.16% | 0.49x | WEAK 29/100 | EXTREME 98/100 | Do nothing |
| 7 | XRP/USD | 0.97485 | 57.02 | -0.58% | 0.88x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 8 | SOL/USD | 74.22 | 56.95 | -0.26% | 0.74x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | USELESS/USD | 0.10247 | 55.33 | -1.32% | 0.15x | WEAK 23/100 | EXTREME 92/100 | Do nothing |
| 10 | SYRUP/USD | 0.1036 | 53.71 | -1.34% | 0.42x | WEAK 22/100 | EXTREME 100/100 | Do nothing |
| 11 | BNB/USD | 586.75 | 43.35 | -0.34% | 0.79x | WEAK 27/100 | HIGH 68/100 | Do nothing |
| 12 | CSPR/USD | 0.00167 | 40.10 | -0.26% | 0.47x | WEAK 25/100 | EXTREME 88/100 | Do nothing |

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
