# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T19:07:17.233496+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45466333622
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b099d963c01a07de029380a4b8be80747d9904fd (atomic ledger/results publication)
**Ledger generation:** 1614 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 503.9 | 77.577 | 78.667 | +3.68% | -0.18% | 0.98x | 4.2 | 2026-11-24T19:07:12.589504+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 2 | ZEUS/USD | 0.00467 | 69.102 | 54.959 | +6.62% | +2.19% | 1.32x | 42.9 | 2026-11-24T19:07:12.589504+00:00 | Not calibrated | MODERATE 65/100 | EXTREME 89/100 | Do nothing | WATCH |
| 3 | LUNA/USD | 4.621e-05 | 63.176 | 74.930 | +6.30% | -2.92% | 1.28x | 2.2 | 2026-11-24T19:07:12.589504+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 4 | VVV/USD | 24.931 | 60.488 | 68.428 | +1.98% | -0.26% | 0.34x | 0.8 | 2026-11-24T19:07:12.589504+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04841 | 54.867 | 41.718 | +0.54% | -0.37% | 4.63x | 6.2 | 2026-11-24T19:07:12.589504+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 6 | GBP/USD | 1.31126 | 52.442 | 59.074 | +0.61% | -0.01% | 0.34x | 0.5 | 2026-11-24T19:07:12.589504+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | AUD/USD | 0.66444 | 45.598 | 44.332 | +0.28% | -0.03% | 1.14x | 1.2 | 2026-11-24T19:07:12.589504+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | CT/USD | 0.1252 | 44.398 | 28.598 | +1.38% | +0.16% | 4.13x | 23.9 | 2026-11-24T19:07:12.589504+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 78.667 | 503.9 | -0.18% | 0.98x |
| 2 | LUNA/USD | 74.930 | 4.621e-05 | -2.92% | 1.28x |
| 3 | VVV/USD | 68.428 | 24.931 | -0.26% | 0.34x |
| 4 | GBP/USD | 59.074 | 1.31126 | -0.01% | 0.34x |
| 5 | ZEUS/USD | 54.959 | 0.00467 | +2.19% | 1.32x |
| 6 | AUD/USD | 44.332 | 0.66444 | -0.03% | 1.14x |
| 7 | NIGHT/USD | 41.718 | 0.04841 | -0.37% | 4.63x |
| 8 | CT/USD | 28.598 | 0.1252 | +0.16% | 4.13x |

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

- Persisted scans: 1614; predictions: 13859; observations: 978018.
- Matured sampled outcomes across 1/6/24/48h: 28052; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45466333622 · **Generation:** 1614 · **Legacy run:** 45466333622
**Main quote time:** 2026-11-24T19:07:17.233496+00:00 · **Legacy report time:** 2026-11-24T19:08:05.825274+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 503.9 | 77.58 | -0.18% | 0.98x | WEAK 44/100 | HIGH 68/100 | Watch |
| 2 | ZEUS/USD ⭐ | 0.00467 | 69.10 | +2.19% | 1.32x | STRONG 75/100 | EXTREME 89/100 | Do nothing |
| 3 | LUNA/USD | 4.621e-05 | 63.18 | -2.92% | 1.28x | WEAK 42/100 | VERY_HIGH 70/100 | Do nothing |
| 4 | VVV/USD | 24.931 | 60.49 | -0.26% | 0.34x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 5 | NIGHT/USD | 0.04841 | 54.87 | -0.37% | 4.63x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 6 | GBP/USD | 1.31126 | 52.44 | -0.01% | 0.34x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | AUD/USD | 0.66444 | 45.60 | -0.03% | 1.14x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 8 | CT/USD ⭐ | 0.1252 | 44.40 | +0.16% | 4.13x | MODERATE 67/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEUS/USD ⭐ | 0.00466 | 78.69 | +2.19% | 1.32x | 2884 | STRONG 79/100 | EXTREME 89/100 | Do nothing |
| 2 | CT/USD ⭐ | 0.1252 | 35.47 | +0.16% | 4.13x | 1190 | MODERATE 68/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** ZEUS/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
