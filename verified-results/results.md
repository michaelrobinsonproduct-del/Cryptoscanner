# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T20:10:28.949618+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44605760963
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** e6e93bbd4013ea6891372593976ed248b1019321 (atomic ledger/results publication)
**Ledger generation:** 852 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5548 | 87.394 | 74.548 | +7.10% | -0.43% | 11.56x | 5.4 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 2 | VVV/USD | 22.341 | 84.764 | 72.165 | +3.09% | -0.48% | 10.49x | 9.0 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ADA/USD | 0.152136 | 69.525 | 56.913 | +0.58% | -0.48% | 3.36x | 4.3 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ALEO/USD | 0.03126 | 68.157 | 63.072 | +4.27% | +1.10% | 0.96x | 6.4 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | MODERATE 64/100 | HIGH 67/100 | Watch | WATCH |
| 5 | HYPE/USD | 67.17 | 67.265 | 56.546 | +0.43% | -0.86% | 3.20x | 3.0 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.09787 | 60.097 | 49.456 | +2.42% | -0.87% | 5.01x | 10.2 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |
| 7 | SKR/USD | 0.01009 | 54.350 | 59.387 | +4.74% | -0.10% | 0.55x | 9.9 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | WEAK 32/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.021068 | 51.410 | 45.943 | +2.25% | -0.64% | 1.87x | 8.1 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | MODERATE 46/100 | HIGH 66/100 | Watch | WATCH |
| 9 | CSPR/USD | 0.001791 | 48.396 | 76.592 | +9.67% | -4.50% | 0.43x | 0.6 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | WEAK 29/100 | EXTREME 85/100 | Do nothing | WATCH |
| 10 | TRX/USD | 0.310098 | 46.352 | 42.294 | +0.26% | -0.05% | 1.43x | 1.2 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |
| 11 | INJ/USD | 7.065 | 44.746 | 51.111 | +1.20% | -0.30% | 0.51x | 4.3 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | PYTH/USD | 0.05358 | 39.460 | 37.694 | +1.55% | -0.83% | 1.59x | 11.2 | 2026-11-19T20:10:21.505483+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CSPR/USD | 76.592 | 0.001791 | -4.50% | 0.43x |
| 2 | AKT/USD | 74.548 | 0.5548 | -0.43% | 11.56x |
| 3 | VVV/USD | 72.165 | 22.341 | -0.48% | 10.49x |
| 4 | ALEO/USD | 63.072 | 0.03126 | +1.10% | 0.96x |
| 5 | SKR/USD | 59.387 | 0.01009 | -0.10% | 0.55x |
| 6 | ADA/USD | 56.913 | 0.152136 | -0.48% | 3.36x |
| 7 | HYPE/USD | 56.546 | 67.17 | -0.86% | 3.20x |
| 8 | INJ/USD | 51.111 | 7.065 | -0.30% | 0.51x |
| 9 | USELESS/USD | 49.456 | 0.09787 | -0.87% | 5.01x |
| 10 | SENT/USD | 45.943 | 0.021068 | -0.64% | 1.87x |
| 11 | TRX/USD | 42.294 | 0.310098 | -0.05% | 1.43x |
| 12 | PYTH/USD | 37.694 | 0.05358 | -0.83% | 1.59x |

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

- Persisted scans: 852; predictions: 7368; observations: 514925.
- Matured sampled outcomes across 1/6/24/48h: 7427; gap abstentions: 15637. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44605760963 · **Generation:** 852 · **Legacy run:** 44605760963
**Main quote time:** 2026-11-19T20:10:28.949618+00:00 · **Legacy report time:** 2026-11-19T20:11:19.095556+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD | 0.5548 | 87.39 | -0.43% | 11.56x | STRONG 74/100 | HIGH 66/100 | Watch |
| 2 | VVV/USD | 22.341 | 84.76 | -0.48% | 10.49x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | ADA/USD | 0.152136 | 69.53 | -0.48% | 3.36x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | ALEO/USD | 0.03126 | 68.16 | +1.10% | 0.96x | MODERATE 64/100 | HIGH 67/100 | Watch |
| 5 | HYPE/USD | 67.17 | 67.27 | -0.86% | 3.20x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | USELESS/USD | 0.09787 | 60.10 | -0.87% | 5.01x | MODERATE 55/100 | HIGH 67/100 | Watch |
| 7 | SKR/USD | 0.01009 | 54.35 | -0.10% | 0.55x | WEAK 32/100 | EXTREME 88/100 | Do nothing |
| 8 | SENT/USD | 0.021068 | 51.41 | -0.64% | 1.87x | MODERATE 46/100 | HIGH 66/100 | Watch |
| 9 | CSPR/USD | 0.001791 | 48.40 | -4.50% | 0.43x | WEAK 29/100 | EXTREME 85/100 | Do nothing |
| 10 | TRX/USD | 0.310098 | 46.35 | -0.05% | 1.43x | WEAK 43/100 | HIGH 61/100 | Watch |
| 11 | INJ/USD | 7.065 | 44.75 | -0.30% | 0.51x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | PYTH/USD | 0.05358 | 39.46 | -0.83% | 1.59x | WEAK 35/100 | VERY_HIGH 72/100 | Watch |

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
