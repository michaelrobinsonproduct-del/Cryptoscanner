# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T07:32:11.336281+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45131472951
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 83c92b1e96e630df7ab8ab556d9077f1661e337a (atomic ledger/results publication)
**Ledger generation:** 1399 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BLESS/USD | 0.01799 | 73.672 | 62.554 | +11.79% | +1.82% | 1.20x | 42.2 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 84/100 | Watch | WATCH |
| 2 | AI/USD | 0.01615 | 69.803 | 66.808 | +10.47% | +2.21% | 0.19x | 18.7 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | MODERATE 60/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | SOL/USD | 71.99 | 69.569 | 67.784 | +1.93% | -0.17% | 1.26x | 1.4 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PAXG/USD | 3617.95 | 67.957 | 52.835 | +1.28% | +0.05% | 2.49x | 1.6 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 5 | UNI/USD | 4.7613 | 67.173 | 52.435 | +1.71% | -0.05% | 4.71x | 1.5 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0555347 | 63.469 | 49.352 | +0.45% | -0.18% | 2.80x | 1.4 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.9375 | 62.686 | 62.463 | +1.07% | -0.31% | 1.18x | 0.1 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 8 | KAS/USD | 0.02704 | 61.872 | 63.091 | +4.77% | +1.35% | 0.20x | 7.4 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6644 | 60.700 | 63.535 | +1.33% | -0.12% | 0.78x | 1.5 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XLM/USD | 0.128733 | 60.029 | 60.745 | +0.94% | +0.03% | 0.91x | 0.9 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 11 | NIGHT/USD | 0.05033 | 59.355 | 62.518 | +2.36% | -0.53% | 0.95x | 9.9 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 12 | LINK/USD | 8.90298 | 56.200 | 49.994 | +1.04% | +0.08% | 1.58x | 2.2 | 2026-11-23T07:32:03.612628+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 67.784 | 71.99 | -0.17% | 1.26x |
| 2 | AI/USD | 66.808 | 0.01615 | +2.21% | 0.19x |
| 3 | SUI/USD | 63.535 | 0.6644 | -0.12% | 0.78x |
| 4 | KAS/USD | 63.091 | 0.02704 | +1.35% | 0.20x |
| 5 | BLESS/USD | 62.554 | 0.01799 | +1.82% | 1.20x |
| 6 | NIGHT/USD | 62.518 | 0.05033 | -0.53% | 0.95x |
| 7 | XRP/USD | 62.463 | 0.9375 | -0.31% | 1.18x |
| 8 | XLM/USD | 60.745 | 0.128733 | +0.03% | 0.91x |
| 9 | PAXG/USD | 52.835 | 3617.95 | +0.05% | 2.49x |
| 10 | UNI/USD | 52.435 | 4.7613 | -0.05% | 4.71x |
| 11 | LINK/USD | 49.994 | 8.90298 | +0.08% | 1.58x |
| 12 | XDG/USD | 49.352 | 0.0555347 | -0.18% | 2.80x |

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

- Persisted scans: 1399; predictions: 11555; observations: 847095.
- Matured sampled outcomes across 1/6/24/48h: 18785; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 124 (sampled only; not a success-rate estimate).
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

**Writer:** 45131472951 · **Generation:** 1399 · **Legacy run:** 45131472951
**Main quote time:** 2026-11-23T07:32:11.336281+00:00 · **Legacy report time:** 2026-11-23T07:33:06.053171+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.01799 | 73.67 | +1.82% | 1.20x | MODERATE 67/100 | VERY_HIGH 84/100 | Watch |
| 2 | AI/USD | 0.01615 | 69.80 | +2.21% | 0.19x | MODERATE 60/100 | EXTREME 88/100 | Do nothing |
| 3 | SOL/USD | 71.99 | 69.57 | -0.17% | 1.26x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 4 | PAXG/USD | 3617.95 | 67.96 | +0.05% | 2.49x | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | UNI/USD | 4.7613 | 67.17 | -0.05% | 4.71x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | XDG/USD | 0.0555347 | 63.47 | -0.18% | 2.80x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.9375 | 62.69 | -0.31% | 1.18x | WEAK 41/100 | HIGH 68/100 | Watch |
| 8 | KAS/USD | 0.02704 | 61.87 | +1.35% | 0.20x | MODERATE 61/100 | VERY_HIGH 75/100 | Watch |
| 9 | SUI/USD | 0.6644 | 60.70 | -0.12% | 0.78x | WEAK 35/100 | HIGH 68/100 | Watch |
| 10 | XLM/USD | 0.128733 | 60.03 | +0.03% | 0.91x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 11 | NIGHT/USD | 0.05033 | 59.35 | -0.53% | 0.95x | WEAK 35/100 | HIGH 68/100 | Watch |
| 12 | LINK/USD | 8.90298 | 56.20 | +0.08% | 1.58x | MODERATE 63/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.01799 | 81.46 | +1.82% | 1.20x | 5653 | STRONG 76/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** BLESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
