# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T03:37:29.346985+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45540927118
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 00974de5feef8299c314050080ef19ffa2cbe8de (atomic ledger/results publication)
**Ledger generation:** 1664 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.34259 | 77.277 | 58.254 | +9.01% | +3.09% | 1.36x | 43.7 | 2026-11-25T03:37:24.422138+00:00 | Not calibrated | MODERATE 69/100 | EXTREME 92/100 | Do nothing | WATCH |
| 2 | MON/USD | 0.00987 | 63.720 | 67.750 | +4.22% | +1.04% | 0.08x | 20.3 | 2026-11-25T03:37:24.422138+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | XMR/USD | 511.96 | 59.358 | 54.485 | +0.46% | +0.38% | 1.30x | 3.1 | 2026-11-25T03:37:24.422138+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.07167 | 56.408 | 46.251 | +2.87% | -0.97% | 5.00x | 11.2 | 2026-11-25T03:37:24.422138+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | XPL/USD | 0.0446 | 49.259 | 33.135 | +1.36% | +0.22% | 3.44x | 22.4 | 2026-11-25T03:37:24.422138+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | VVV/USD | 24.676 | 47.456 | 54.071 | +0.56% | -1.33% | 1.01x | 9.7 | 2026-11-25T03:37:24.422138+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 7 | BAT/USD | 0.07628 | 46.477 | 29.497 | +0.26% | +0.40% | 8.31x | 9.2 | 2026-11-25T03:37:24.422138+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 67.750 | 0.00987 | +1.04% | 0.08x |
| 2 | DRV/USD | 58.254 | 0.34259 | +3.09% | 1.36x |
| 3 | XMR/USD | 54.485 | 511.96 | +0.38% | 1.30x |
| 4 | VVV/USD | 54.071 | 24.676 | -1.33% | 1.01x |
| 5 | SYRUP/USD | 46.251 | 0.07167 | -0.97% | 5.00x |
| 6 | XPL/USD | 33.135 | 0.0446 | +0.22% | 3.44x |
| 7 | BAT/USD | 29.497 | 0.07628 | +0.40% | 8.31x |

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

- Persisted scans: 1664; predictions: 14157; observations: 1008467.
- Matured sampled outcomes across 1/6/24/48h: 29838; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45540927118 · **Generation:** 1664 · **Legacy run:** 45540927118
**Main quote time:** 2026-11-25T03:37:29.346985+00:00 · **Legacy report time:** 2026-11-25T03:38:44.627174+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.34259 | 77.28 | +3.09% | 1.36x | MODERATE 69/100 | EXTREME 92/100 | Do nothing |
| 2 | MON/USD | 0.00987 | 63.72 | +1.04% | 0.08x | MODERATE 52/100 | VERY_HIGH 82/100 | Watch |
| 3 | XMR/USD ⭐ | 511.96 | 59.36 | +0.38% | 1.30x | STRONG 75/100 | HIGH 55/100 | Watch |
| 4 | SYRUP/USD | 0.07167 | 56.41 | -0.97% | 5.00x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 5 | XPL/USD ⭐ | 0.0446 | 49.26 | +0.22% | 3.44x | STRONG 80/100 | VERY_HIGH 72/100 | Watch |
| 6 | VVV/USD | 24.676 | 47.46 | -1.33% | 1.01x | WEAK 34/100 | VERY_HIGH 72/100 | Do nothing |
| 7 | BAT/USD ⭐ | 0.07628 | 46.48 | +0.40% | 8.31x | STRONG 88/100 | HIGH 60/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD | 0.308474 | 48.31 | +0.20% | 1.53x | 3578 | MODERATE 69/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 513.04 | 46.21 | +0.38% | 1.30x | 6840 | MODERATE 63/100 | HIGH 61/100 | Watch |
| 3 | XPL/USD ⭐ | 0.0446 | 40.09 | +0.22% | 3.44x | 1461 | STRONG 75/100 | VERY_HIGH 72/100 | Watch |
| 4 | BAT/USD ⭐ | 0.07632 | 36.32 | +0.40% | 8.31x | 3578 | STRONG 73/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** XMR/USD, XPL/USD, BAT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
