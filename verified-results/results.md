# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T18:56:05.527988+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44592745430
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** dce73e6aef6e2acc48659ce0ac1909a4da989aba (atomic ledger/results publication)
**Ledger generation:** 839 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.653 | 83.554 | 82.513 | +4.53% | -0.63% | 1.42x | 8.4 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 2 | CT/USD | 0.1289 | 77.394 | 69.061 | +9.05% | -1.22% | 2.44x | 15.5 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | TAO/USD | 194.8444 | 71.257 | 61.240 | +1.50% | -1.00% | 4.53x | 6.2 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ADA/USD | 0.153316 | 68.387 | 62.552 | +1.36% | -0.70% | 1.93x | 4.0 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 74.01 | 67.836 | 58.798 | +0.64% | -0.48% | 2.15x | 1.4 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | HYPE/USD | 68.69 | 62.978 | 71.760 | +2.71% | -1.56% | 0.90x | 4.4 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5501 | 60.053 | 70.909 | +6.20% | -0.88% | 0.36x | 9.1 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97217 | 57.806 | 58.584 | +0.60% | -0.45% | 1.15x | 1.2 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 9 | PUMP/USD | 0.002696 | 57.644 | 63.715 | +3.85% | -1.06% | 0.92x | 11.2 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 10 | SKR/USD | 0.010125 | 56.628 | 64.399 | +5.11% | -0.64% | 0.54x | 4.9 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | WEAK 33/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | SENT/USD | 0.021366 | 56.144 | 56.682 | +3.69% | +0.56% | 0.66x | 7.0 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 12 | INJ/USD | 7.1 | 51.547 | 56.220 | +1.70% | -1.62% | 1.34x | 1.4 | 2026-11-19T18:55:57.191268+00:00 | Not calibrated | MODERATE 46/100 | HIGH 65/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.513 | 22.653 | -0.63% | 1.42x |
| 2 | HYPE/USD | 71.760 | 68.69 | -1.56% | 0.90x |
| 3 | AKT/USD | 70.909 | 0.5501 | -0.88% | 0.36x |
| 4 | CT/USD | 69.061 | 0.1289 | -1.22% | 2.44x |
| 5 | SKR/USD | 64.399 | 0.010125 | -0.64% | 0.54x |
| 6 | PUMP/USD | 63.715 | 0.002696 | -1.06% | 0.92x |
| 7 | ADA/USD | 62.552 | 0.153316 | -0.70% | 1.93x |
| 8 | TAO/USD | 61.240 | 194.8444 | -1.00% | 4.53x |
| 9 | SOL/USD | 58.798 | 74.01 | -0.48% | 2.15x |
| 10 | XRP/USD | 58.584 | 0.97217 | -0.45% | 1.15x |
| 11 | SENT/USD | 56.682 | 0.021366 | +0.56% | 0.66x |
| 12 | INJ/USD | 56.220 | 7.1 | -1.62% | 1.34x |

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

- Persisted scans: 839; predictions: 7212; observations: 507138.
- Matured sampled outcomes across 1/6/24/48h: 7211; gap abstentions: 15557. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44592745430 · **Generation:** 839 · **Legacy run:** 44592745430
**Main quote time:** 2026-11-19T18:56:05.527988+00:00 · **Legacy report time:** 2026-11-19T18:56:54.646816+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.653 | 83.55 | -0.63% | 1.42x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 2 | CT/USD | 0.1289 | 77.39 | -1.22% | 2.44x | MODERATE 64/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | TAO/USD | 194.8444 | 71.26 | -1.00% | 4.53x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | ADA/USD | 0.153316 | 68.39 | -0.70% | 1.93x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD | 74.01 | 67.84 | -0.48% | 2.15x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | HYPE/USD | 68.69 | 62.98 | -1.56% | 0.90x | WEAK 36/100 | VERY_HIGH 72/100 | Do nothing |
| 7 | AKT/USD | 0.5501 | 60.05 | -0.88% | 0.36x | WEAK 35/100 | VERY_HIGH 81/100 | Watch |
| 8 | XRP/USD | 0.97217 | 57.81 | -0.45% | 1.15x | WEAK 39/100 | HIGH 68/100 | Watch |
| 9 | PUMP/USD | 0.002696 | 57.64 | -1.06% | 0.92x | WEAK 29/100 | VERY_HIGH 78/100 | Do nothing |
| 10 | SKR/USD | 0.010125 | 56.63 | -0.64% | 0.54x | WEAK 33/100 | EXTREME 88/100 | Do nothing |
| 11 | SENT/USD | 0.021366 | 56.14 | +0.56% | 0.66x | MODERATE 58/100 | VERY_HIGH 75/100 | Watch |
| 12 | INJ/USD | 7.1 | 51.55 | -1.62% | 1.34x | MODERATE 46/100 | HIGH 65/100 | Do nothing |

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
