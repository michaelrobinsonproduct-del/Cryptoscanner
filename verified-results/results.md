# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:55:04.915523+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44240543635
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 791976bed7608fb4cbf9beffcdc478307345ca15 (atomic ledger/results publication)
**Ledger generation:** 536 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2887 | 59.854 | 57.339 | +4.56% | +1.16% | 0.67x | 13.9 | 2026-11-18T04:54:59.858238+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 2 | SENT/USD | 0.01933 | 55.169 | 52.883 | +3.54% | +1.32% | 0.57x | 5.7 | 2026-11-18T04:54:59.858238+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | XDC/USD | 0.03085 | 55.022 | 48.388 | +1.75% | -0.87% | 2.10x | 3.2 | 2026-11-18T04:54:59.858238+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 4 | UP/USD | 0.05542 | 52.746 | 58.684 | +4.59% | -0.07% | 0.44x | 10.8 | 2026-11-18T04:54:59.858238+00:00 | Not calibrated | WEAK 26/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | UAI/USD | 0.03369 | 42.411 | 28.596 | +0.93% | -0.24% | 4.94x | 17.8 | 2026-11-18T04:54:59.858238+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | PEARL/USD | 1.848 | 40.642 | 43.787 | +2.07% | +0.17% | 0.60x | 11.4 | 2026-11-18T04:54:59.858238+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | CC/USD | 0.08328 | 34.574 | 41.788 | +1.40% | -0.26% | 0.41x | 7.2 | 2026-11-18T04:54:59.858238+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | MELANIA/USD | 0.05 | 31.068 | 29.411 | +2.67% | +0.20% | 1.07x | 40.1 | 2026-11-18T04:54:59.858238+00:00 | Not calibrated | WEAK 36/100 | EXTREME 96/100 | Do nothing | WATCH |
| 9 | MEGA/USD | 0.05214 | 22.372 | 28.442 | +0.97% | +0.04% | 0.37x | 19.2 | 2026-11-18T04:54:59.858238+00:00 | Not calibrated | WEAK 26/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 58.684 | 0.05542 | -0.07% | 0.44x |
| 2 | ICNT/USD | 57.339 | 0.2887 | +1.16% | 0.67x |
| 3 | SENT/USD | 52.883 | 0.01933 | +1.32% | 0.57x |
| 4 | XDC/USD | 48.388 | 0.03085 | -0.87% | 2.10x |
| 5 | PEARL/USD | 43.787 | 1.848 | +0.17% | 0.60x |
| 6 | CC/USD | 41.788 | 0.08328 | -0.26% | 0.41x |
| 7 | MELANIA/USD | 29.411 | 0.05 | +0.20% | 1.07x |
| 8 | UAI/USD | 28.596 | 0.03369 | -0.24% | 4.94x |
| 9 | MEGA/USD | 28.442 | 0.05214 | +0.04% | 0.37x |

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

- Persisted scans: 536; predictions: 4530; observations: 323431.
- Matured sampled outcomes across 1/6/24/48h: 3593; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44240543635 · **Generation:** 536 · **Legacy run:** 44240543635
**Main quote time:** 2026-11-18T04:55:04.915523+00:00 · **Legacy report time:** 2026-11-18T04:55:23.528149+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.2887 | 59.85 | +1.16% | 0.67x | MODERATE 55/100 | VERY_HIGH 81/100 | Watch |
| 2 | SENT/USD | 0.01933 | 55.17 | +1.32% | 0.57x | MODERATE 58/100 | VERY_HIGH 82/100 | Watch |
| 3 | XDC/USD | 0.03085 | 55.02 | -0.87% | 2.10x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 4 | UP/USD | 0.05542 | 52.75 | -0.07% | 0.44x | WEAK 26/100 | EXTREME 87/100 | Do nothing |
| 5 | UAI/USD | 0.03369 | 42.41 | -0.24% | 4.94x | MODERATE 46/100 | VERY_HIGH 79/100 | Watch |
| 6 | PEARL/USD | 1.848 | 40.64 | +0.17% | 0.60x | WEAK 35/100 | VERY_HIGH 81/100 | Watch |
| 7 | CC/USD | 0.08328 | 34.57 | -0.26% | 0.41x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | MELANIA/USD ⭐ | 0.05 | 31.07 | +0.20% | 1.07x | MODERATE 46/100 | EXTREME 96/100 | Do nothing |
| 9 | MEGA/USD | 0.05214 | 22.37 | +0.04% | 0.37x | WEAK 26/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MELANIA/USD ⭐ | 0.05 | 38.76 | +0.20% | 1.07x | 649 | MODERATE 49/100 | EXTREME 96/100 | Do nothing |

**Same-run overlap:** MELANIA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
