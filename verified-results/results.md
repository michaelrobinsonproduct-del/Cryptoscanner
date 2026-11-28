# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T16:33:14.824327+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46165425632
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f877c79e48a899e8a25bd095984692bb5228f1ce (atomic ledger/results publication)
**Ledger generation:** 2178 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05182 | 73.083 | 72.120 | +3.14% | +0.60% | 0.79x | 7.7 | 2026-11-28T16:33:11.504571+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XMR/USD | 417.3 | 71.558 | 68.046 | +2.46% | -0.64% | 1.67x | 8.4 | 2026-11-28T16:33:11.504571+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.726e-05 | 48.867 | 41.906 | +3.66% | +0.40% | 1.49x | 29.6 | 2026-11-28T16:33:11.504571+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | SENT/USD | 0.023997 | 39.600 | 35.733 | +1.19% | -0.14% | 1.46x | 7.9 | 2026-11-28T16:33:11.504571+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | XDC/USD | 0.02558 | 27.532 | 31.806 | +0.31% | -0.12% | 0.63x | 3.9 | 2026-11-28T16:33:11.504571+00:00 | Not calibrated | WEAK 19/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 72.120 | 0.05182 | +0.60% | 0.79x |
| 2 | XMR/USD | 68.046 | 417.3 | -0.64% | 1.67x |
| 3 | LUNA/USD | 41.906 | 4.726e-05 | +0.40% | 1.49x |
| 4 | SENT/USD | 35.733 | 0.023997 | -0.14% | 1.46x |
| 5 | XDC/USD | 31.806 | 0.02558 | -0.12% | 0.63x |

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

- Persisted scans: 2178; predictions: 19316; observations: 1318914.
- Matured sampled outcomes across 1/6/24/48h: 46711; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46165425632 · **Generation:** 2178 · **Legacy run:** 46165425632
**Main quote time:** 2026-11-28T16:33:14.824327+00:00 · **Legacy report time:** 2026-11-28T16:34:07.907019+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05182 | 73.08 | +0.60% | 0.79x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 2 | XMR/USD | 417.3 | 71.56 | -0.64% | 1.67x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 3 | LUNA/USD ⭐ | 4.726e-05 | 48.87 | +0.40% | 1.49x | MODERATE 69/100 | VERY_HIGH 79/100 | Watch |
| 4 | SENT/USD | 0.023997 | 39.60 | -0.14% | 1.46x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |
| 5 | XDC/USD | 0.02558 | 27.53 | -0.12% | 0.63x | WEAK 19/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.736e-05 | 60.64 | +0.40% | 1.49x | 1226 | STRONG 70/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
