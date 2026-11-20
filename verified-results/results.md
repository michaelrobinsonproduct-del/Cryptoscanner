# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T08:40:36.316285+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44704309531
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** e5427a941a2461d15d00e57763a27e270bc963f9 (atomic ledger/results publication)
**Ledger generation:** 955 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 606; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKR/USD | 0.01059 | 84.243 | 61.296 | +5.42% | +1.59% | 3.52x | 16.1 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | STRONG 92/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | PROS/USD | 0.5834 | 72.696 | 69.008 | +8.30% | +0.33% | 1.21x | 13.7 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | XLM/USD | 0.134139 | 58.230 | 60.839 | +1.08% | +0.31% | 0.58x | 3.5 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.4452 | 57.944 | 58.033 | +4.48% | -2.32% | 2.15x | 24.8 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 5 | XRP/USD | 0.96485 | 55.526 | 58.672 | +0.58% | +0.06% | 0.65x | 0.8 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.2716 | 48.447 | 35.870 | +0.80% | +0.36% | 2.08x | 4.7 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | STRONG 79/100 | HIGH 60/100 | Watch | WATCH |
| 7 | XTZ/USD | 0.20479 | 45.413 | 28.402 | +0.30% | +0.40% | 21.99x | 9.3 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | STRONG 78/100 | HIGH 67/100 | Watch | WATCH |
| 8 | STRK/USD | 0.03185 | 28.383 | 33.022 | +0.50% | -0.25% | 0.66x | 9.4 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | CRV/USD | 0.19315 | 27.863 | 34.731 | +0.53% | +0.02% | 0.30x | 13.5 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | TON/USD | 1.022 | 25.539 | 31.689 | +0.49% | +0.29% | 0.24x | 9.8 | 2026-11-20T08:40:29.133084+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 69.008 | 0.5834 | +0.33% | 1.21x |
| 2 | SKR/USD | 61.296 | 0.01059 | +1.59% | 3.52x |
| 3 | XLM/USD | 60.839 | 0.134139 | +0.31% | 0.58x |
| 4 | XRP/USD | 58.672 | 0.96485 | +0.06% | 0.65x |
| 5 | ICNT/USD | 58.033 | 0.4452 | -2.32% | 2.15x |
| 6 | ATOM/USD | 35.870 | 1.2716 | +0.36% | 2.08x |
| 7 | CRV/USD | 34.731 | 0.19315 | +0.02% | 0.30x |
| 8 | STRK/USD | 33.022 | 0.03185 | -0.25% | 0.66x |
| 9 | TON/USD | 31.689 | 1.022 | +0.29% | 0.24x |
| 10 | XTZ/USD | 28.402 | 0.20479 | +0.40% | 21.99x |

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

- Persisted scans: 955; predictions: 8116; observations: 577049.
- Matured sampled outcomes across 1/6/24/48h: 9631; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44704309531 · **Generation:** 955 · **Legacy run:** 44704309531
**Main quote time:** 2026-11-20T08:40:36.316285+00:00 · **Legacy report time:** 2026-11-20T08:41:19.777118+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKR/USD ⭐ | 0.01059 | 84.24 | +1.59% | 3.52x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | PROS/USD ⭐ | 0.5834 | 72.70 | +0.33% | 1.21x | STRONG 76/100 | VERY_HIGH 80/100 | Watch |
| 3 | XLM/USD | 0.134139 | 58.23 | +0.31% | 0.58x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 4 | ICNT/USD | 0.4452 | 57.94 | -2.32% | 2.15x | MODERATE 49/100 | VERY_HIGH 77/100 | Do nothing |
| 5 | XRP/USD | 0.96485 | 55.53 | +0.06% | 0.65x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 6 | ATOM/USD ⭐ | 1.2716 | 48.45 | +0.36% | 2.08x | STRONG 89/100 | HIGH 60/100 | Consider small entry |
| 7 | XTZ/USD | 0.20479 | 45.41 | +0.40% | 21.99x | STRONG 78/100 | HIGH 67/100 | Watch |
| 8 | STRK/USD | 0.03185 | 28.38 | -0.25% | 0.66x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | CRV/USD | 0.19315 | 27.86 | +0.02% | 0.30x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | TON/USD | 1.022 | 25.54 | +0.29% | 0.24x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKR/USD ⭐ | 0.010535 | 76.89 | +1.59% | 3.52x | 1832 | STRONG 98/100 | VERY_HIGH 73/100 | Watch |
| 2 | PROS/USD ⭐ | 0.5794 | 59.39 | +0.33% | 1.21x | 1088 | MODERATE 65/100 | EXTREME 86/100 | Do nothing |
| 3 | AUD/USD | 0.66703 | 47.79 | +0.08% | 1.77x | 3923 | MODERATE 59/100 | HIGH 55/100 | Watch |
| 4 | ATOM/USD ⭐ | 1.2716 | 42.56 | +0.36% | 2.08x | 3326 | STRONG 86/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SKR/USD, PROS/USD, ATOM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
