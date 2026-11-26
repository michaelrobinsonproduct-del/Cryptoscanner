# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T15:41:42.103715+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45851277323
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 92a0c04acaf963573bd1a034e9b90de3fcf92c5f (atomic ledger/results publication)
**Ledger generation:** 1880 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5011 | 89.603 | 67.372 | +5.92% | +1.45% | 4.23x | 14.0 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | STRONG 95/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | ZRO/USD | 1.08 | 71.533 | 72.417 | +5.47% | +0.56% | 0.63x | 9.3 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | LTC/USD | 43.25 | 63.993 | 62.695 | +1.26% | +0.28% | 0.99x | 2.3 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04548 | 62.105 | 73.984 | +8.60% | -1.35% | 0.49x | 11.0 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | WEAK 31/100 | EXTREME 91/100 | Do nothing | WATCH |
| 5 | STBL/USD | 0.020729 | 60.894 | 65.074 | +9.76% | +0.80% | 0.18x | 21.7 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | ADA/USD | 0.147491 | 57.516 | 60.791 | +1.18% | +0.38% | 0.48x | 4.9 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HBAR/USD | 0.05344 | 55.681 | 52.430 | +2.57% | +0.26% | 1.19x | 3.7 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0563273 | 53.633 | 51.105 | +0.66% | +0.20% | 1.15x | 1.2 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SOL/USD | 70.65 | 53.601 | 56.878 | +0.37% | +0.54% | 0.40x | 1.4 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94333 | 52.575 | 60.007 | +0.72% | +0.25% | 0.13x | 0.1 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | LINK/USD | 9.12725 | 50.880 | 59.139 | +0.91% | +0.10% | 0.12x | 4.5 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | RENDER/USD | 1.302 | 41.509 | 28.421 | +0.39% | -0.38% | 3.88x | 15.4 | 2026-11-26T15:41:33.840486+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 73.984 | 0.04548 | -1.35% | 0.49x |
| 2 | ZRO/USD | 72.417 | 1.08 | +0.56% | 0.63x |
| 3 | AKT/USD | 67.372 | 0.5011 | +1.45% | 4.23x |
| 4 | STBL/USD | 65.074 | 0.020729 | +0.80% | 0.18x |
| 5 | LTC/USD | 62.695 | 43.25 | +0.28% | 0.99x |
| 6 | ADA/USD | 60.791 | 0.147491 | +0.38% | 0.48x |
| 7 | XRP/USD | 60.007 | 0.94333 | +0.25% | 0.13x |
| 8 | LINK/USD | 59.139 | 9.12725 | +0.10% | 0.12x |
| 9 | SOL/USD | 56.878 | 70.65 | +0.54% | 0.40x |
| 10 | HBAR/USD | 52.430 | 0.05344 | +0.26% | 1.19x |
| 11 | XDG/USD | 51.105 | 0.0563273 | +0.20% | 1.15x |
| 12 | RENDER/USD | 28.421 | 1.302 | -0.38% | 3.88x |

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

- Persisted scans: 1880; predictions: 16295; observations: 1139149.
- Matured sampled outcomes across 1/6/24/48h: 35234; gap abstentions: 25009. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45851277323 · **Generation:** 1880 · **Legacy run:** 45851277323
**Main quote time:** 2026-11-26T15:41:42.103715+00:00 · **Legacy report time:** 2026-11-26T15:43:03.797156+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5011 | 89.60 | +1.45% | 4.23x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | ZRO/USD | 1.08 | 71.53 | +0.56% | 0.63x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 3 | LTC/USD | 43.25 | 63.99 | +0.28% | 0.99x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 4 | SKY/USD | 0.04548 | 62.10 | -1.35% | 0.49x | WEAK 31/100 | EXTREME 91/100 | Do nothing |
| 5 | STBL/USD | 0.020729 | 60.89 | +0.80% | 0.18x | MODERATE 50/100 | EXTREME 94/100 | Do nothing |
| 6 | ADA/USD | 0.147491 | 57.52 | +0.38% | 0.48x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 7 | HBAR/USD ⭐ | 0.05344 | 55.68 | +0.26% | 1.19x | STRONG 73/100 | HIGH 67/100 | Watch |
| 8 | XDG/USD | 0.0563273 | 53.63 | +0.20% | 1.15x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 9 | SOL/USD | 70.65 | 53.60 | +0.54% | 0.40x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 10 | XRP/USD | 0.94333 | 52.57 | +0.25% | 0.13x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 11 | LINK/USD | 9.12725 | 50.88 | +0.10% | 0.12x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 12 | RENDER/USD | 1.302 | 41.51 | -0.38% | 3.88x | MODERATE 46/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5011 | 84.09 | +1.45% | 4.23x | 3010 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | HBAR/USD ⭐ | 0.05346 | 69.92 | +0.26% | 1.19x | 5609 | STRONG 80/100 | HIGH 67/100 | Watch |

**Same-run overlap:** AKT/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
