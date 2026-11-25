# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T05:47:21.386065+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45555667558
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4cf9520f58d5f1a031210a0e140e9e6dcf2995ec (atomic ledger/results publication)
**Ledger generation:** 1677 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33146 | 73.787 | 66.971 | +5.47% | -0.60% | 1.98x | 16.6 | 2026-11-25T05:47:16.844865+00:00 | Not calibrated | MODERATE 52/100 | HIGH 67/100 | Watch | WATCH |
| 2 | MON/USD | 0.00998 | 69.896 | 76.000 | +5.39% | +0.00% | 0.39x | 20.1 | 2026-11-25T05:47:16.844865+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | VVV/USD | 24.878 | 54.618 | 60.681 | +1.39% | -0.95% | 0.87x | 8.0 | 2026-11-25T05:47:16.844865+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | PEPE/USD | 3.464e-06 | 48.763 | 41.617 | +0.32% | +0.49% | 1.47x | 8.7 | 2026-11-25T05:47:16.844865+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.07133 | 41.463 | 36.520 | +2.38% | +0.11% | 1.44x | 23.8 | 2026-11-25T05:47:16.844865+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 76.000 | 0.00998 | +0.00% | 0.39x |
| 2 | DRV/USD | 66.971 | 0.33146 | -0.60% | 1.98x |
| 3 | VVV/USD | 60.681 | 24.878 | -0.95% | 0.87x |
| 4 | PEPE/USD | 41.617 | 3.464e-06 | +0.49% | 1.47x |
| 5 | SYRUP/USD | 36.520 | 0.07133 | +0.11% | 1.44x |

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

- Persisted scans: 1677; predictions: 14233; observations: 1016384.
- Matured sampled outcomes across 1/6/24/48h: 30264; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45555667558 · **Generation:** 1677 · **Legacy run:** 45555667558
**Main quote time:** 2026-11-25T05:47:21.386065+00:00 · **Legacy report time:** 2026-11-25T05:48:21.941658+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.33146 | 73.79 | -0.60% | 1.98x | MODERATE 52/100 | HIGH 67/100 | Watch |
| 2 | MON/USD | 0.00998 | 69.90 | +0.00% | 0.39x | MODERATE 45/100 | VERY_HIGH 82/100 | Watch |
| 3 | VVV/USD | 24.878 | 54.62 | -0.95% | 0.87x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 4 | PEPE/USD ⭐ | 3.464e-06 | 48.76 | +0.49% | 1.47x | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | SYRUP/USD ⭐ | 0.07133 | 41.46 | +0.11% | 1.44x | MODERATE 56/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07133 | 53.74 | +0.11% | 1.44x | 3460 | MODERATE 62/100 | VERY_HIGH 72/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.463e-06 | 37.07 | +0.49% | 1.47x | 5396 | STRONG 74/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PEPE/USD, SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
