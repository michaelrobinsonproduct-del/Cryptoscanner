# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T00:56:09.539689+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45732070891
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4de3bb394a08a950be53f51d3bcbbd3bb5de83aa (atomic ledger/results publication)
**Ledger generation:** 1790 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 30.275 | 97.094 | 72.942 | +3.70% | +1.83% | 2.98x | 15.9 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | STRONG 99/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.01131 | 59.437 | 52.986 | +2.35% | +1.53% | 0.88x | 8.9 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 3 | LTC/USD | 42.98 | 56.494 | 58.262 | +0.63% | +0.23% | 0.71x | 2.3 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0665 | 52.674 | 58.321 | +0.54% | -0.35% | 0.61x | 1.0 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | ADA/USD | 0.146518 | 51.702 | 57.466 | +0.51% | -0.06% | 0.45x | 2.3 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | SUI/USD | 0.6701 | 50.962 | 58.246 | +0.57% | -0.16% | 0.35x | 1.5 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | TAO/USD | 183.08 | 49.115 | 57.395 | +0.82% | +0.11% | 0.12x | 6.7 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SOL/USD | 70.68 | 48.343 | 57.176 | +0.41% | -0.30% | 0.26x | 1.4 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | XDG/USD | 0.0563251 | 44.806 | 54.116 | +0.65% | -0.04% | 0.09x | 0.3 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | LINK/USD | 9.0933 | 43.245 | 51.257 | +0.54% | -0.21% | 0.30x | 3.1 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | AVAX/USD | 6.643 | 41.057 | 45.877 | +0.33% | -0.15% | 0.59x | 3.0 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XLM/USD | 0.128485 | 38.276 | 47.558 | +0.52% | -0.30% | 0.22x | 1.8 | 2026-11-26T00:56:02.797762+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 72.942 | 30.275 | +1.83% | 2.98x |
| 2 | NEAR/USD | 58.321 | 3.0665 | -0.35% | 0.61x |
| 3 | LTC/USD | 58.262 | 42.98 | +0.23% | 0.71x |
| 4 | SUI/USD | 58.246 | 0.6701 | -0.16% | 0.35x |
| 5 | ADA/USD | 57.466 | 0.146518 | -0.06% | 0.45x |
| 6 | TAO/USD | 57.395 | 183.08 | +0.11% | 0.12x |
| 7 | SOL/USD | 57.176 | 70.68 | -0.30% | 0.26x |
| 8 | XDG/USD | 54.116 | 0.0563251 | -0.04% | 0.09x |
| 9 | MON/USD | 52.986 | 0.01131 | +1.53% | 0.88x |
| 10 | LINK/USD | 51.257 | 9.0933 | -0.21% | 0.30x |
| 11 | XLM/USD | 47.558 | 0.128485 | -0.30% | 0.22x |
| 12 | AVAX/USD | 45.877 | 6.643 | -0.15% | 0.59x |

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

- Persisted scans: 1790; predictions: 15215; observations: 1085154.
- Matured sampled outcomes across 1/6/24/48h: 33080; gap abstentions: 23536. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45732070891 · **Generation:** 1790 · **Legacy run:** 45732070891
**Main quote time:** 2026-11-26T00:56:09.539689+00:00 · **Legacy report time:** 2026-11-26T00:57:17.347283+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 30.275 | 97.09 | +1.83% | 2.98x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | MON/USD | 0.01131 | 59.44 | +1.53% | 0.88x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 3 | LTC/USD | 42.98 | 56.49 | +0.23% | 0.71x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | NEAR/USD | 3.0665 | 52.67 | -0.35% | 0.61x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | ADA/USD | 0.146518 | 51.70 | -0.06% | 0.45x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | SUI/USD | 0.6701 | 50.96 | -0.16% | 0.35x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | TAO/USD | 183.08 | 49.12 | +0.11% | 0.12x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 8 | SOL/USD | 70.68 | 48.34 | -0.30% | 0.26x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | XDG/USD | 0.0563251 | 44.81 | -0.04% | 0.09x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | LINK/USD | 9.0933 | 43.24 | -0.21% | 0.30x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | AVAX/USD | 6.643 | 41.06 | -0.15% | 0.59x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XLM/USD | 0.128485 | 38.28 | -0.30% | 0.22x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 30.166 | 90.31 | +1.83% | 2.98x | 17733 | STRONG 100/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
