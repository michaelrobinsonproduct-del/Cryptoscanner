# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T06:17:41.349424+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46115686925
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c5545ed394fdbf27e879e32442c598e594fbe30c (atomic ledger/results publication)
**Ledger generation:** 2116 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 420.9 | 75.453 | 64.858 | +3.35% | +1.50% | 1.31x | 27.1 | 2026-11-28T06:17:38.503277+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 2 | ZEC/USD | 738.53 | 69.920 | 56.607 | +0.54% | -0.34% | 4.22x | 4.3 | 2026-11-28T06:17:38.503277+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 26.218 | 61.490 | 54.389 | +1.82% | +0.40% | 1.51x | 8.0 | 2026-11-28T06:17:38.503277+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004268 | 57.893 | 39.969 | +2.15% | +0.87% | 2.36x | 11.7 | 2026-11-28T06:17:38.503277+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | CFG/USD | 0.0631 | 56.542 | 62.081 | +11.88% | +0.16% | 0.37x | 31.7 | 2026-11-28T06:17:38.503277+00:00 | Not calibrated | WEAK 38/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | SENT/USD | 0.024314 | 56.209 | 46.717 | +2.53% | -1.10% | 4.09x | 4.1 | 2026-11-28T06:17:38.503277+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 77/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 64.858 | 420.9 | +1.50% | 1.31x |
| 2 | CFG/USD | 62.081 | 0.0631 | +0.16% | 0.37x |
| 3 | ZEC/USD | 56.607 | 738.53 | -0.34% | 4.22x |
| 4 | VVV/USD | 54.389 | 26.218 | +0.40% | 1.51x |
| 5 | SENT/USD | 46.717 | 0.024314 | -1.10% | 4.09x |
| 6 | SPACE/USD | 39.969 | 0.004268 | +0.87% | 2.36x |

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

- Persisted scans: 2116; predictions: 18973; observations: 1281342.
- Matured sampled outcomes across 1/6/24/48h: 44371; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46115686925 · **Generation:** 2116 · **Legacy run:** 46115686925
**Main quote time:** 2026-11-28T06:17:41.349424+00:00 · **Legacy report time:** 2026-11-28T06:18:38.092466+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 420.9 | 75.45 | +1.50% | 1.31x | STRONG 83/100 | HIGH 67/100 | Watch |
| 2 | ZEC/USD | 738.53 | 69.92 | -0.34% | 4.22x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD ⭐ | 26.218 | 61.49 | +0.40% | 1.51x | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 4 | SPACE/USD ⭐ | 0.004268 | 57.89 | +0.87% | 2.36x | STRONG 89/100 | VERY_HIGH 73/100 | Watch |
| 5 | CFG/USD | 0.0631 | 56.54 | +0.16% | 0.37x | WEAK 38/100 | EXTREME 87/100 | Do nothing |
| 6 | SENT/USD | 0.024314 | 56.21 | -1.10% | 4.09x | MODERATE 58/100 | VERY_HIGH 77/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 420.9 | 82.90 | +1.50% | 1.31x | 14911 | STRONG 86/100 | HIGH 67/100 | Watch |
| 2 | NEAR/USD | 3.0219 | 55.75 | +0.08% | 33.16x | 13641 | STRONG 73/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD ⭐ | 26.178 | 54.61 | +0.40% | 1.51x | 7998 | STRONG 82/100 | HIGH 55/100 | Consider small entry |
| 4 | SPACE/USD ⭐ | 0.004268 | 50.68 | +0.87% | 2.36x | 1960 | STRONG 90/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** XMR/USD, VVV/USD, SPACE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
