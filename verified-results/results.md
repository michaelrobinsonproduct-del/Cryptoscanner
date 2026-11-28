# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T06:57:33.212029+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46118760196
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 292c2a94103fb27623dd1f663985eef5e54ae87f (atomic ledger/results publication)
**Ledger generation:** 2120 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 429.25 | 93.654 | 92.662 | +5.40% | -1.08% | 1.64x | 0.2 | 2026-11-28T06:57:29.902044+00:00 | Not calibrated | MODERATE 67/100 | HIGH 65/100 | Watch | WATCH |
| 2 | VVV/USD | 26.339 | 50.808 | 55.772 | +2.29% | -0.16% | 0.58x | 11.0 | 2026-11-28T06:57:29.902044+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | ZEC/USD | 738.95 | 50.084 | 56.604 | +0.60% | -0.39% | 0.54x | 5.1 | 2026-11-28T06:57:29.902044+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | NEAR/USD | 3.0352 | 47.861 | 57.625 | +0.56% | -0.04% | 0.04x | 2.6 | 2026-11-28T06:57:29.902044+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | SHX/USD | 0.003367 | 40.852 | 19.845 | +0.57% | +1.20% | 16.69x | 29.7 | 2026-11-28T06:57:29.902044+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | SPACE/USD | 0.00424 | 19.068 | 35.221 | +1.48% | -1.40% | 0.08x | 11.8 | 2026-11-28T06:57:29.902044+00:00 | Not calibrated | WEAK 10/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 92.662 | 429.25 | -1.08% | 1.64x |
| 2 | NEAR/USD | 57.625 | 3.0352 | -0.04% | 0.04x |
| 3 | ZEC/USD | 56.604 | 738.95 | -0.39% | 0.54x |
| 4 | VVV/USD | 55.772 | 26.339 | -0.16% | 0.58x |
| 5 | SPACE/USD | 35.221 | 0.00424 | -1.40% | 0.08x |
| 6 | SHX/USD | 19.845 | 0.003367 | +1.20% | 16.69x |

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

- Persisted scans: 2120; predictions: 19002; observations: 1283766.
- Matured sampled outcomes across 1/6/24/48h: 44526; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46118760196 · **Generation:** 2120 · **Legacy run:** 46118760196
**Main quote time:** 2026-11-28T06:57:33.212029+00:00 · **Legacy report time:** 2026-11-28T06:58:15.100334+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 429.25 | 93.65 | -1.08% | 1.64x | MODERATE 67/100 | HIGH 65/100 | Watch |
| 2 | VVV/USD | 26.339 | 50.81 | -0.16% | 0.58x | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | ZEC/USD | 738.95 | 50.08 | -0.39% | 0.54x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | NEAR/USD | 3.0352 | 47.86 | -0.04% | 0.04x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | SHX/USD ⭐ | 0.003367 | 40.85 | +1.20% | 16.69x | STRONG 75/100 | VERY_HIGH 79/100 | Watch |
| 6 | SPACE/USD | 0.00424 | 19.07 | -1.40% | 0.08x | WEAK 10/100 | EXTREME 98/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 63.59 | 58.98 | +0.08% | 4.08x | 17209 | STRONG 74/100 | HIGH 55/100 | Watch |
| 2 | SHX/USD ⭐ | 0.003367 | 30.64 | +1.20% | 16.69x | 1415 | STRONG 70/100 | VERY_HIGH 79/100 | Watch |
| 3 | W/USD | 0.00923 | 15.90 | +0.11% | 1.23x | 1306 | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing |

**Same-run overlap:** SHX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
