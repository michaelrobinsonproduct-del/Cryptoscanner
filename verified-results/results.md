# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:25:29.957681+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44576863103
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 25276e4691777c3ccad0f1a254819bc118454cf2 (atomic ledger/results publication)
**Ledger generation:** 824 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.609 | 101.237 | 80.872 | +4.33% | +1.07% | 9.03x | 8.9 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | BMT/USD | 0.02056 | 84.998 | 71.453 | +8.90% | -0.29% | 34.96x | 9.7 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5397 | 81.200 | 60.104 | +4.19% | +1.22% | 9.84x | 1.9 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | STRONG 96/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | HYPE/USD | 67.86 | 74.582 | 63.047 | +1.47% | +0.64% | 1.84x | 4.4 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XRP/USD | 0.97144 | 68.280 | 58.621 | +0.52% | +0.78% | 1.58x | 0.1 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 6 | PYTH/USD | 0.05538 | 67.516 | 61.507 | +4.97% | -0.34% | 1.77x | 10.8 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | SENT/USD | 0.021617 | 64.810 | 65.078 | +4.91% | -0.26% | 1.10x | 7.4 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | ADA/USD | 0.152806 | 62.888 | 59.563 | +1.03% | +0.81% | 0.93x | 5.2 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.803e-06 | 59.708 | 47.666 | +1.52% | +0.64% | 1.89x | 7.9 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 10 | TAO/USD | 193.6162 | 58.442 | 57.577 | +0.86% | +0.83% | 0.67x | 6.3 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | LUNA/USD | 4.8e-05 | 56.657 | 61.760 | +10.24% | +0.44% | 0.27x | 39.8 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | WEAK 43/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | INJ/USD | 7.123 | 54.494 | 53.573 | +2.03% | +0.84% | 0.67x | 8.4 | 2026-11-19T17:25:21.116393+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.872 | 22.609 | +1.07% | 9.03x |
| 2 | BMT/USD | 71.453 | 0.02056 | -0.29% | 34.96x |
| 3 | SENT/USD | 65.078 | 0.021617 | -0.26% | 1.10x |
| 4 | HYPE/USD | 63.047 | 67.86 | +0.64% | 1.84x |
| 5 | LUNA/USD | 61.760 | 4.8e-05 | +0.44% | 0.27x |
| 6 | PYTH/USD | 61.507 | 0.05538 | -0.34% | 1.77x |
| 7 | AKT/USD | 60.104 | 0.5397 | +1.22% | 9.84x |
| 8 | ADA/USD | 59.563 | 0.152806 | +0.81% | 0.93x |
| 9 | XRP/USD | 58.621 | 0.97144 | +0.78% | 1.58x |
| 10 | TAO/USD | 57.577 | 193.6162 | +0.83% | 0.67x |
| 11 | INJ/USD | 53.573 | 7.123 | +0.84% | 0.67x |
| 12 | PEPE/USD | 47.666 | 3.803e-06 | +0.64% | 1.89x |

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

- Persisted scans: 824; predictions: 7032; observations: 498163.
- Matured sampled outcomes across 1/6/24/48h: 7007; gap abstentions: 15436. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44576863103 · **Generation:** 824 · **Legacy run:** 44576863103
**Main quote time:** 2026-11-19T17:25:29.957681+00:00 · **Legacy report time:** 2026-11-19T17:26:22.657801+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.609 | 101.24 | +1.07% | 9.03x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | BMT/USD | 0.02056 | 85.00 | -0.29% | 34.96x | STRONG 72/100 | VERY_HIGH 73/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5397 | 81.20 | +1.22% | 9.84x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 4 | HYPE/USD ⭐ | 67.86 | 74.58 | +0.64% | 1.84x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD | 0.97144 | 68.28 | +0.78% | 1.58x | STRONG 79/100 | HIGH 55/100 | Watch |
| 6 | PYTH/USD | 0.05538 | 67.52 | -0.34% | 1.77x | MODERATE 49/100 | VERY_HIGH 72/100 | Watch |
| 7 | SENT/USD | 0.021617 | 64.81 | -0.26% | 1.10x | WEAK 42/100 | VERY_HIGH 73/100 | Watch |
| 8 | ADA/USD | 0.152806 | 62.89 | +0.81% | 0.93x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 9 | PEPE/USD | 3.803e-06 | 59.71 | +0.64% | 1.89x | STRONG 75/100 | HIGH 55/100 | Watch |
| 10 | TAO/USD | 193.6162 | 58.44 | +0.83% | 0.67x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 11 | LUNA/USD | 4.8e-05 | 56.66 | +0.44% | 0.27x | WEAK 43/100 | EXTREME 87/100 | Do nothing |
| 12 | INJ/USD | 7.123 | 54.49 | +0.84% | 0.67x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.661 | 96.22 | +1.07% | 9.03x | 12175 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | USELESS/USD | 0.09959 | 84.60 | +0.73% | 12.21x | 3199 | STRONG 87/100 | HIGH 67/100 | Consider small entry |
| 3 | AKT/USD ⭐ | 0.5458 | 82.79 | +1.22% | 9.84x | 3249 | STRONG 96/100 | VERY_HIGH 72/100 | Watch |
| 4 | HYPE/USD ⭐ | 68.09 | 70.15 | +0.64% | 1.84x | 12498 | STRONG 90/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD, AKT/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
