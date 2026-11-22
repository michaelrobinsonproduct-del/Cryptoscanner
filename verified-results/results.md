# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T20:11:03.615881+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45064825594
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 550902d86cf2a1aa6ef9b7806d0bd685dea25bfd (atomic ledger/results publication)
**Ledger generation:** 1330 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002565 | 94.471 | 82.378 | +9.43% | -0.58% | 4.59x | 7.8 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 25.952 | 93.823 | 81.107 | +4.22% | -0.46% | 2.91x | 6.9 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HYPE/USD | 62.3 | 80.994 | 66.315 | +1.73% | -0.06% | 8.25x | 1.6 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04841 | 79.359 | 86.658 | +9.33% | +0.04% | 0.25x | 12.4 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | PIEVERSE/USD | 3.6367 | 77.125 | 79.430 | +6.86% | +0.79% | 0.38x | 12.1 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | NEAR/USD | 2.9766 | 71.659 | 75.892 | +3.13% | -0.53% | 0.84x | 2.0 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XMR/USD | 493.39 | 68.266 | 53.206 | +0.32% | +0.19% | 2.41x | 8.1 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ETH/USD | 1711.67 | 67.575 | 67.200 | +1.75% | -0.10% | 1.09x | 0.1 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6548 | 64.628 | 62.106 | +1.16% | -0.23% | 1.37x | 1.5 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XBT/USD | 60650.3 | 59.979 | 61.520 | +0.93% | -0.02% | 0.85x | 0.0 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | LINK/USD | 8.78226 | 52.764 | 58.225 | +2.18% | -0.10% | 0.50x | 1.6 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | LTC/USD | 39.83 | 51.979 | 43.789 | +0.25% | -0.15% | 1.89x | 2.5 | 2026-11-22T20:10:55.888362+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 86.658 | 0.04841 | +0.04% | 0.25x |
| 2 | PUMP/USD | 82.378 | 0.002565 | -0.58% | 4.59x |
| 3 | VVV/USD | 81.107 | 25.952 | -0.46% | 2.91x |
| 4 | PIEVERSE/USD | 79.430 | 3.6367 | +0.79% | 0.38x |
| 5 | NEAR/USD | 75.892 | 2.9766 | -0.53% | 0.84x |
| 6 | ETH/USD | 67.200 | 1711.67 | -0.10% | 1.09x |
| 7 | HYPE/USD | 66.315 | 62.3 | -0.06% | 8.25x |
| 8 | SUI/USD | 62.106 | 0.6548 | -0.23% | 1.37x |
| 9 | XBT/USD | 61.520 | 60650.3 | -0.02% | 0.85x |
| 10 | LINK/USD | 58.225 | 8.78226 | -0.10% | 0.50x |
| 11 | XMR/USD | 53.206 | 493.39 | +0.19% | 2.41x |
| 12 | LTC/USD | 43.789 | 39.83 | -0.15% | 1.89x |

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

- Persisted scans: 1330; predictions: 10879; observations: 805078.
- Matured sampled outcomes across 1/6/24/48h: 16486; gap abstentions: 22346. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45064825594 · **Generation:** 1330 · **Legacy run:** 45064825594
**Main quote time:** 2026-11-22T20:11:03.615881+00:00 · **Legacy report time:** 2026-11-22T20:11:51.202930+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD | 0.002565 | 94.47 | -0.58% | 4.59x | STRONG 77/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD | 25.952 | 93.82 | -0.46% | 2.91x | STRONG 77/100 | HIGH 61/100 | Watch |
| 3 | HYPE/USD | 62.3 | 80.99 | -0.06% | 8.25x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD | 0.04841 | 79.36 | +0.04% | 0.25x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |
| 5 | PIEVERSE/USD | 3.6367 | 77.12 | +0.79% | 0.38x | MODERATE 64/100 | VERY_HIGH 76/100 | Watch |
| 6 | NEAR/USD | 2.9766 | 71.66 | -0.53% | 0.84x | WEAK 41/100 | HIGH 68/100 | Watch |
| 7 | XMR/USD | 493.39 | 68.27 | +0.19% | 2.41x | STRONG 79/100 | HIGH 55/100 | Watch |
| 8 | ETH/USD | 1711.67 | 67.57 | -0.10% | 1.09x | WEAK 44/100 | HIGH 68/100 | Watch |
| 9 | SUI/USD | 0.6548 | 64.63 | -0.23% | 1.37x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | XBT/USD | 60650.3 | 59.98 | -0.02% | 0.85x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | LINK/USD | 8.78226 | 52.76 | -0.10% | 0.50x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | LTC/USD | 39.83 | 51.98 | -0.15% | 1.89x | MODERATE 46/100 | HIGH 61/100 | Watch |

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
