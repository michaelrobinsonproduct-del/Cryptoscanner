# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:15:21.599935+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44442853734
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 1bd4b25264362c321082d8b3d4a06ca1c3bb44f2 (atomic ledger/results publication)
**Ledger generation:** 728 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.693e-05 | 86.198 | 54.803 | +7.79% | +3.28% | 5.94x | 44.9 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | STRONG 83/100 | EXTREME 92/100 | Do nothing | WATCH |
| 2 | CFG/USD | 0.0696 | 62.055 | 68.602 | +8.07% | -1.42% | 1.05x | 14.3 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | WEAK 36/100 | EXTREME 90/100 | Do nothing | WATCH |
| 3 | VVV/USD | 22.011 | 60.217 | 54.806 | +1.57% | +1.74% | 0.67x | 8.2 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | TRX/USD | 0.310636 | 58.807 | 43.159 | +0.44% | +0.13% | 18.87x | 0.0 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.3213 | 53.229 | 59.019 | +0.72% | +0.52% | 0.16x | 2.1 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ICP/USD | 2.243 | 52.300 | 56.405 | +2.98% | +0.63% | 0.28x | 4.5 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HYPE/USD | 67.05 | 48.247 | 56.033 | +0.25% | +0.16% | 0.14x | 1.5 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SENT/USD | 0.02164 | 46.288 | 50.668 | +5.02% | -0.50% | 0.81x | 32.0 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | WEAK 18/100 | EXTREME 92/100 | Do nothing | WATCH |
| 9 | TRUMP/USD | 0.951 | 41.668 | 34.019 | +0.63% | +0.42% | 1.55x | 10.5 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 10 | PAXG/USD | 3743.06 | 38.800 | 43.191 | +0.32% | -0.07% | 0.59x | 1.3 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ENA/USD | 0.1121 | 32.469 | 34.721 | +0.36% | +0.18% | 0.69x | 17.9 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | DRV/USD | 0.26653 | 25.940 | 33.275 | +0.70% | +0.04% | 0.24x | 9.8 | 2026-11-19T02:15:14.759959+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CFG/USD | 68.602 | 0.0696 | -1.42% | 1.05x |
| 2 | NEAR/USD | 59.019 | 3.3213 | +0.52% | 0.16x |
| 3 | ICP/USD | 56.405 | 2.243 | +0.63% | 0.28x |
| 4 | HYPE/USD | 56.033 | 67.05 | +0.16% | 0.14x |
| 5 | VVV/USD | 54.806 | 22.011 | +1.74% | 0.67x |
| 6 | LUNA/USD | 54.803 | 4.693e-05 | +3.28% | 5.94x |
| 7 | SENT/USD | 50.668 | 0.02164 | -0.50% | 0.81x |
| 8 | PAXG/USD | 43.191 | 3743.06 | -0.07% | 0.59x |
| 9 | TRX/USD | 43.159 | 0.310636 | +0.13% | 18.87x |
| 10 | ENA/USD | 34.721 | 0.1121 | +0.18% | 0.69x |
| 11 | TRUMP/USD | 34.019 | 0.951 | +0.42% | 1.55x |
| 12 | DRV/USD | 33.275 | 0.26653 | +0.04% | 0.24x |

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

- Persisted scans: 728; predictions: 5913; observations: 440359.
- Matured sampled outcomes across 1/6/24/48h: 5842; gap abstentions: 13482. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44442853734 · **Generation:** 728 · **Legacy run:** 44442853734
**Main quote time:** 2026-11-19T02:15:21.599935+00:00 · **Legacy report time:** 2026-11-19T02:16:06.815450+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.693e-05 | 86.20 | +3.28% | 5.94x | STRONG 93/100 | EXTREME 92/100 | Do nothing |
| 2 | CFG/USD | 0.0696 | 62.05 | -1.42% | 1.05x | WEAK 36/100 | EXTREME 90/100 | Do nothing |
| 3 | VVV/USD | 22.011 | 60.22 | +1.74% | 0.67x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 4 | TRX/USD ⭐ | 0.310636 | 58.81 | +0.13% | 18.87x | STRONG 84/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD | 3.3213 | 53.23 | +0.52% | 0.16x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 6 | ICP/USD | 2.243 | 52.30 | +0.63% | 0.28x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 7 | HYPE/USD | 67.05 | 48.25 | +0.16% | 0.14x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 8 | SENT/USD | 0.02164 | 46.29 | -0.50% | 0.81x | WEAK 18/100 | EXTREME 92/100 | Do nothing |
| 9 | TRUMP/USD | 0.951 | 41.67 | +0.42% | 1.55x | MODERATE 61/100 | HIGH 66/100 | Watch |
| 10 | PAXG/USD | 3743.06 | 38.80 | -0.07% | 0.59x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ENA/USD | 0.1121 | 32.47 | +0.18% | 0.69x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | DRV/USD | 0.26653 | 25.94 | +0.04% | 0.24x | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.694e-05 | 82.03 | +3.28% | 5.94x | 2000 | STRONG 91/100 | EXTREME 92/100 | Do nothing |
| 2 | TRX/USD ⭐ | 0.310436 | 54.06 | +0.13% | 18.87x | 4186 | STRONG 82/100 | HIGH 55/100 | Watch |
| 3 | PROS/USD | 0.6821 | 51.33 | +1.30% | 1.57x | 2674 | MODERATE 61/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** LUNA/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
