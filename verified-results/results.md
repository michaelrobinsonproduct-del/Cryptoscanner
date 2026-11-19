# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:25:29.685722+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44565758480
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 8b899979214138d95f8c0f8b0d4fb8a99d195730 (atomic ledger/results publication)
**Ledger generation:** 812 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 597; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKR/USD | 0.010397 | 80.567 | 64.507 | +7.93% | +0.21% | 2.59x | 23.1 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | STRONG 85/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | VVV/USD | 22.539 | 78.396 | 80.378 | +4.01% | +0.67% | 0.47x | 5.3 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PYTH/USD | 0.05618 | 63.682 | 68.290 | +6.48% | -0.85% | 0.96x | 17.8 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 4 | SYRUP/USD | 0.10185 | 63.680 | 70.071 | +7.26% | -0.52% | 0.62x | 12.8 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | WEAK 32/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | BILL/USD | 0.00434 | 63.326 | 64.270 | +9.87% | +0.70% | 0.56x | 23.0 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | BMT/USD | 0.02029 | 59.479 | 68.777 | +7.47% | -0.34% | 0.24x | 14.8 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | WEAK 30/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | HYPE/USD | 67.67 | 58.818 | 61.791 | +1.18% | -0.03% | 0.72x | 3.0 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | USELESS/USD | 0.10091 | 58.344 | 67.469 | +5.60% | -0.17% | 0.17x | 17.9 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | TRUST/USD | 0.0545 | 57.149 | 65.101 | +10.77% | -0.67% | 0.54x | 22.2 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | WEAK 24/100 | EXTREME 100/100 | Do nothing | WATCH |
| 10 | ZEC/USD | 921.39 | 54.161 | 60.400 | +1.04% | +0.39% | 0.18x | 3.7 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ADA/USD | 0.152481 | 53.476 | 58.907 | +0.81% | +0.23% | 0.34x | 3.5 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.97226 | 53.296 | 58.752 | +0.61% | +0.09% | 0.41x | 1.0 | 2026-11-19T16:25:20.836893+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.378 | 22.539 | +0.67% | 0.47x |
| 2 | SYRUP/USD | 70.071 | 0.10185 | -0.52% | 0.62x |
| 3 | BMT/USD | 68.777 | 0.02029 | -0.34% | 0.24x |
| 4 | PYTH/USD | 68.290 | 0.05618 | -0.85% | 0.96x |
| 5 | USELESS/USD | 67.469 | 0.10091 | -0.17% | 0.17x |
| 6 | TRUST/USD | 65.101 | 0.0545 | -0.67% | 0.54x |
| 7 | SKR/USD | 64.507 | 0.010397 | +0.21% | 2.59x |
| 8 | BILL/USD | 64.270 | 0.00434 | +0.70% | 0.56x |
| 9 | HYPE/USD | 61.791 | 67.67 | -0.03% | 0.72x |
| 10 | ZEC/USD | 60.400 | 921.39 | +0.39% | 0.18x |
| 11 | ADA/USD | 58.907 | 0.152481 | +0.23% | 0.34x |
| 12 | XRP/USD | 58.752 | 0.97226 | +0.09% | 0.41x |

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

- Persisted scans: 812; predictions: 6888; observations: 490990.
- Matured sampled outcomes across 1/6/24/48h: 6887; gap abstentions: 15342. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44565758480 · **Generation:** 812 · **Legacy run:** 44565758480
**Main quote time:** 2026-11-19T16:25:29.685722+00:00 · **Legacy report time:** 2026-11-19T16:26:15.668556+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKR/USD | 0.010397 | 80.57 | +0.21% | 2.59x | STRONG 85/100 | VERY_HIGH 79/100 | Watch |
| 2 | VVV/USD | 22.539 | 78.40 | +0.67% | 0.47x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 3 | PYTH/USD | 0.05618 | 63.68 | -0.85% | 0.96x | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing |
| 4 | SYRUP/USD | 0.10185 | 63.68 | -0.52% | 0.62x | WEAK 32/100 | EXTREME 94/100 | Do nothing |
| 5 | BILL/USD | 0.00434 | 63.33 | +0.70% | 0.56x | MODERATE 52/100 | EXTREME 94/100 | Do nothing |
| 6 | BMT/USD | 0.02029 | 59.48 | -0.34% | 0.24x | WEAK 30/100 | EXTREME 94/100 | Do nothing |
| 7 | HYPE/USD | 67.67 | 58.82 | -0.03% | 0.72x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | USELESS/USD | 0.10091 | 58.34 | -0.17% | 0.17x | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | TRUST/USD | 0.0545 | 57.15 | -0.67% | 0.54x | WEAK 24/100 | EXTREME 100/100 | Do nothing |
| 10 | ZEC/USD | 921.39 | 54.16 | +0.39% | 0.18x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 11 | ADA/USD | 0.152481 | 53.48 | +0.23% | 0.34x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.97226 | 53.30 | +0.09% | 0.41x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

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
