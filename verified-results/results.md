# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T11:53:14.832558+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45608000167
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2d1d7b5576459fed1694bacc2b764ed502e33f56 (atomic ledger/results publication)
**Ledger generation:** 1714 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BABY/USD | 0.00874 | 94.370 | 66.459 | +5.81% | +2.58% | 29.99x | 11.4 | 2026-11-25T11:53:10.355470+00:00 | Not calibrated | STRONG 97/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | VVV/USD | 24.91 | 64.864 | 60.609 | +1.52% | +0.26% | 1.29x | 10.0 | 2026-11-25T11:53:10.355470+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 3 | MON/USD | 0.00987 | 63.754 | 73.051 | +4.22% | -0.50% | 0.32x | 10.1 | 2026-11-25T11:53:10.355470+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | TREAD/USD | 1.0348 | 60.201 | 53.975 | +3.53% | +0.37% | 1.44x | 3.9 | 2026-11-25T11:53:10.355470+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 5 | CT/USD | 0.1289 | 24.638 | 33.669 | +2.06% | -0.08% | 0.14x | 23.3 | 2026-11-25T11:53:10.355470+00:00 | Not calibrated | WEAK 7/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 73.051 | 0.00987 | -0.50% | 0.32x |
| 2 | BABY/USD | 66.459 | 0.00874 | +2.58% | 29.99x |
| 3 | VVV/USD | 60.609 | 24.91 | +0.26% | 1.29x |
| 4 | TREAD/USD | 53.975 | 1.0348 | +0.37% | 1.44x |
| 5 | CT/USD | 33.669 | 0.1289 | -0.08% | 0.14x |

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

- Persisted scans: 1714; predictions: 14488; observations: 1038897.
- Matured sampled outcomes across 1/6/24/48h: 31581; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45608000167 · **Generation:** 1714 · **Legacy run:** 45608000167
**Main quote time:** 2026-11-25T11:53:14.832558+00:00 · **Legacy report time:** 2026-11-25T11:54:26.290143+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00874 | 94.37 | +2.58% | 29.99x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD ⭐ | 24.91 | 64.86 | +0.26% | 1.29x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | MON/USD | 0.00987 | 63.75 | -0.50% | 0.32x | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | TREAD/USD ⭐ | 1.0348 | 60.20 | +0.37% | 1.44x | STRONG 85/100 | HIGH 67/100 | Watch |
| 5 | CT/USD | 0.1289 | 24.64 | -0.08% | 0.14x | WEAK 7/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00874 | 86.65 | +2.58% | 29.99x | 2997 | STRONG 98/100 | VERY_HIGH 79/100 | Watch |
| 2 | TREAD/USD ⭐ | 1.0349 | 71.47 | +0.37% | 1.44x | 2714 | STRONG 91/100 | HIGH 67/100 | Watch |
| 3 | VVV/USD ⭐ | 25.026 | 62.83 | +0.26% | 1.29x | 12725 | STRONG 71/100 | HIGH 61/100 | Watch |

**Same-run overlap:** BABY/USD, VVV/USD, TREAD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
