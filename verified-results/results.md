# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T13:21:02.995735+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45828037686
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1db9d8f1c14d47b7d7e2741a3df84c85c59888c3 (atomic ledger/results publication)
**Ledger generation:** 1866 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.23919 | 82.020 | 68.849 | +2.15% | -0.02% | 2.33x | 2.4 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 2 | INJ/USD | 6.165 | 79.711 | 66.569 | +3.54% | -0.37% | 2.73x | 3.2 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | QNT/USD | 150.13 | 70.221 | 74.186 | +3.68% | -0.40% | 0.80x | 0.7 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ETH/USD | 1704.46 | 67.854 | 60.789 | +0.83% | -0.01% | 1.71x | 0.1 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 5 | VELO/USD | 0.002399 | 66.057 | 66.117 | +5.64% | +0.33% | 0.83x | 8.3 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | LTC/USD | 43.59 | 64.073 | 68.276 | +2.06% | +0.05% | 0.56x | 2.3 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SEI/USD | 0.03631 | 60.624 | 74.055 | +9.01% | -1.44% | 0.38x | 8.3 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | WEAK 35/100 | EXTREME 85/100 | Do nothing | WATCH |
| 8 | ADA/USD | 0.148656 | 60.371 | 67.279 | +1.98% | -0.13% | 0.38x | 3.2 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0568317 | 56.958 | 61.172 | +1.56% | +0.09% | 0.53x | 0.9 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 70.93 | 56.498 | 59.665 | +0.77% | -0.01% | 0.69x | 1.4 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.94932 | 55.941 | 64.484 | +1.36% | -0.05% | 0.17x | 0.1 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XBT/USD | 60782.7 | 55.636 | 59.793 | +0.69% | +0.03% | 0.57x | 0.0 | 2026-11-26T13:20:56.120838+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 74.186 | 150.13 | -0.40% | 0.80x |
| 2 | SEI/USD | 74.055 | 0.03631 | -1.44% | 0.38x |
| 3 | LINK/USD | 68.849 | 9.23919 | -0.02% | 2.33x |
| 4 | LTC/USD | 68.276 | 43.59 | +0.05% | 0.56x |
| 5 | ADA/USD | 67.279 | 0.148656 | -0.13% | 0.38x |
| 6 | INJ/USD | 66.569 | 6.165 | -0.37% | 2.73x |
| 7 | VELO/USD | 66.117 | 0.002399 | +0.33% | 0.83x |
| 8 | XRP/USD | 64.484 | 0.94932 | -0.05% | 0.17x |
| 9 | XDG/USD | 61.172 | 0.0568317 | +0.09% | 0.53x |
| 10 | ETH/USD | 60.789 | 1704.46 | -0.01% | 1.71x |
| 11 | XBT/USD | 59.793 | 60782.7 | +0.03% | 0.57x |
| 12 | SOL/USD | 59.665 | 70.93 | -0.01% | 0.69x |

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

- Persisted scans: 1866; predictions: 16127; observations: 1130889.
- Matured sampled outcomes across 1/6/24/48h: 34898; gap abstentions: 24818. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45828037686 · **Generation:** 1866 · **Legacy run:** 45828037686
**Main quote time:** 2026-11-26T13:21:02.995735+00:00 · **Legacy report time:** 2026-11-26T13:22:08.288030+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.23919 | 82.02 | -0.02% | 2.33x | STRONG 71/100 | HIGH 61/100 | Watch |
| 2 | INJ/USD | 6.165 | 79.71 | -0.37% | 2.73x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | QNT/USD | 150.13 | 70.22 | -0.40% | 0.80x | WEAK 40/100 | HIGH 68/100 | Watch |
| 4 | ETH/USD | 1704.46 | 67.85 | -0.01% | 1.71x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 5 | VELO/USD | 0.002399 | 66.06 | +0.33% | 0.83x | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |
| 6 | LTC/USD | 43.59 | 64.07 | +0.05% | 0.56x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 7 | SEI/USD | 0.03631 | 60.62 | -1.44% | 0.38x | WEAK 35/100 | EXTREME 85/100 | Do nothing |
| 8 | ADA/USD | 0.148656 | 60.37 | -0.13% | 0.38x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | XDG/USD | 0.0568317 | 56.96 | +0.09% | 0.53x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 70.93 | 56.50 | -0.01% | 0.69x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XRP/USD | 0.94932 | 55.94 | -0.05% | 0.17x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XBT/USD | 60782.7 | 55.64 | +0.03% | 0.57x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

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
