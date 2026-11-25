# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T11:42:20.402683+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45606480488
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e6c14ef216c9ebf095e7c96d939db5a659a93be6 (atomic ledger/results publication)
**Ledger generation:** 1713 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BABY/USD | 0.00866 | 79.263 | 59.607 | +4.84% | +0.93% | 20.55x | 11.6 | 2026-11-25T11:42:16.587374+00:00 | Not calibrated | STRONG 90/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | DRV/USD | 0.3357 | 69.915 | 74.028 | +6.82% | -0.33% | 0.75x | 17.9 | 2026-11-25T11:42:16.587374+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | MON/USD | 0.00988 | 63.604 | 68.738 | +4.33% | +0.20% | 0.39x | 20.3 | 2026-11-25T11:42:16.587374+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | TREAD/USD | 1.0314 | 54.556 | 51.091 | +3.19% | +0.86% | 0.92x | 4.8 | 2026-11-25T11:42:16.587374+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | VVV/USD | 24.874 | 53.617 | 57.342 | +1.37% | -0.06% | 0.66x | 14.5 | 2026-11-25T11:42:16.587374+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | CT/USD | 0.1281 | 29.512 | 29.148 | +1.43% | -1.53% | 1.80x | 23.5 | 2026-11-25T11:42:16.587374+00:00 | Not calibrated | WEAK 25/100 | EXTREME 89/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 74.028 | 0.3357 | -0.33% | 0.75x |
| 2 | MON/USD | 68.738 | 0.00988 | +0.20% | 0.39x |
| 3 | BABY/USD | 59.607 | 0.00866 | +0.93% | 20.55x |
| 4 | VVV/USD | 57.342 | 24.874 | -0.06% | 0.66x |
| 5 | TREAD/USD | 51.091 | 1.0314 | +0.86% | 0.92x |
| 6 | CT/USD | 29.148 | 0.1281 | -1.53% | 1.80x |

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

- Persisted scans: 1713; predictions: 14483; observations: 1038289.
- Matured sampled outcomes across 1/6/24/48h: 31529; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45606480488 · **Generation:** 1713 · **Legacy run:** 45606480488
**Main quote time:** 2026-11-25T11:42:20.402683+00:00 · **Legacy report time:** 2026-11-25T11:43:20.724726+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00866 | 79.26 | +0.93% | 20.55x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | DRV/USD | 0.3357 | 69.92 | -0.33% | 0.75x | WEAK 35/100 | VERY_HIGH 74/100 | Watch |
| 3 | MON/USD | 0.00988 | 63.60 | +0.20% | 0.39x | MODERATE 52/100 | VERY_HIGH 82/100 | Watch |
| 4 | TREAD/USD | 1.0314 | 54.56 | +0.86% | 0.92x | MODERATE 57/100 | VERY_HIGH 74/100 | Watch |
| 5 | VVV/USD | 24.874 | 53.62 | -0.06% | 0.66x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | CT/USD | 0.1281 | 29.51 | -1.53% | 1.80x | WEAK 25/100 | EXTREME 89/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00866 | 81.69 | +0.93% | 20.55x | 3014 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** BABY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
