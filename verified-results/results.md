# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:55:32.449160+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44582177364
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** cb1f55de307875f81e2abf768c24a37af9d94926 (atomic ledger/results publication)
**Ledger generation:** 830 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1286 | 82.541 | 65.198 | +8.80% | +0.47% | 4.61x | 23.3 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | STRONG 86/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | VVV/USD | 22.73 | 81.750 | 85.906 | +4.89% | -0.08% | 0.63x | 6.6 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | HYPE/USD | 68.82 | 75.737 | 73.852 | +2.90% | +0.23% | 1.07x | 2.9 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5559 | 72.126 | 68.966 | +7.32% | +0.25% | 1.19x | 16.2 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | SKR/USD | 0.010198 | 67.186 | 69.201 | +5.87% | -0.68% | 1.14x | 5.9 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 6 | PUMP/USD | 0.002697 | 66.299 | 64.047 | +3.89% | -0.18% | 1.32x | 11.1 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |
| 7 | SOL/USD | 73.89 | 64.105 | 57.655 | +0.48% | -0.12% | 1.71x | 1.4 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ADA/USD | 0.153095 | 62.714 | 61.265 | +1.22% | -0.23% | 1.26x | 4.5 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | WEAK 41/100 | HIGH 61/100 | Watch | WATCH |
| 9 | INJ/USD | 7.132 | 59.612 | 55.716 | +2.16% | -0.43% | 1.61x | 5.6 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 10 | AVAX/USD | 7.047 | 58.724 | 47.505 | +0.37% | -0.07% | 2.16x | 4.3 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 11 | LIGHTER/USD | 2.863 | 56.946 | 66.374 | +5.49% | -0.35% | 0.23x | 14.0 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | WEAK 28/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | USELESS/USD | 0.09999 | 54.132 | 63.144 | +4.64% | -0.38% | 0.29x | 13.0 | 2026-11-19T17:55:23.818437+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 85.906 | 22.73 | -0.08% | 0.63x |
| 2 | HYPE/USD | 73.852 | 68.82 | +0.23% | 1.07x |
| 3 | SKR/USD | 69.201 | 0.010198 | -0.68% | 1.14x |
| 4 | AKT/USD | 68.966 | 0.5559 | +0.25% | 1.19x |
| 5 | LIGHTER/USD | 66.374 | 2.863 | -0.35% | 0.23x |
| 6 | CT/USD | 65.198 | 0.1286 | +0.47% | 4.61x |
| 7 | PUMP/USD | 64.047 | 0.002697 | -0.18% | 1.32x |
| 8 | USELESS/USD | 63.144 | 0.09999 | -0.38% | 0.29x |
| 9 | ADA/USD | 61.265 | 0.153095 | -0.23% | 1.26x |
| 10 | SOL/USD | 57.655 | 73.89 | -0.12% | 1.71x |
| 11 | INJ/USD | 55.716 | 7.132 | -0.43% | 1.61x |
| 12 | AVAX/USD | 47.505 | 7.047 | -0.07% | 2.16x |

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

- Persisted scans: 830; predictions: 7104; observations: 501751.
- Matured sampled outcomes across 1/6/24/48h: 7067; gap abstentions: 15462. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44582177364 · **Generation:** 830 · **Legacy run:** 44582177364
**Main quote time:** 2026-11-19T17:55:32.449160+00:00 · **Legacy report time:** 2026-11-19T17:56:32.175237+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1286 | 82.54 | +0.47% | 4.61x | STRONG 96/100 | VERY_HIGH 72/100 | Watch |
| 2 | VVV/USD | 22.73 | 81.75 | -0.08% | 0.63x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 3 | HYPE/USD ⭐ | 68.82 | 75.74 | +0.23% | 1.07x | STRONG 83/100 | HIGH 62/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5559 | 72.13 | +0.25% | 1.19x | STRONG 76/100 | VERY_HIGH 73/100 | Watch |
| 5 | SKR/USD | 0.010198 | 67.19 | -0.68% | 1.14x | WEAK 44/100 | VERY_HIGH 80/100 | Watch |
| 6 | PUMP/USD | 0.002697 | 66.30 | -0.18% | 1.32x | MODERATE 48/100 | HIGH 67/100 | Watch |
| 7 | SOL/USD | 73.89 | 64.11 | -0.12% | 1.71x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 8 | ADA/USD | 0.153095 | 62.71 | -0.23% | 1.26x | WEAK 41/100 | HIGH 61/100 | Watch |
| 9 | INJ/USD | 7.132 | 59.61 | -0.43% | 1.61x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 10 | AVAX/USD | 7.047 | 58.72 | -0.07% | 2.16x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 11 | LIGHTER/USD | 2.863 | 56.95 | -0.35% | 0.23x | WEAK 28/100 | EXTREME 87/100 | Do nothing |
| 12 | USELESS/USD | 0.09999 | 54.13 | -0.38% | 0.29x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 68.62 | 78.38 | +0.23% | 1.07x | 12790 | STRONG 84/100 | HIGH 62/100 | Watch |
| 2 | CT/USD ⭐ | 0.1286 | 76.61 | +0.47% | 4.61x | 2170 | STRONG 93/100 | VERY_HIGH 72/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5559 | 72.77 | +0.25% | 1.19x | 3314 | STRONG 76/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** CT/USD, HYPE/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
