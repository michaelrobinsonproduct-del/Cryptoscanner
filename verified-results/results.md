# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T09:02:22.606045+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45360949460
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a81b5f9df1db605c9f5a2c0c6f3dcb1acb916962 (atomic ledger/results publication)
**Ledger generation:** 1553 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 24.964 | 76.918 | 65.359 | +2.11% | -0.63% | 2.47x | 8.8 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.5e-06 | 75.425 | 63.548 | +2.28% | -0.45% | 2.41x | 5.7 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.558e-05 | 67.618 | 53.925 | +4.85% | -0.26% | 4.70x | 24.2 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 4 | BAT/USD | 0.07948 | 64.496 | 50.812 | +2.99% | -0.26% | 5.25x | 5.0 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 5 | MON/USD | 0.01278 | 64.418 | 82.815 | +10.94% | -2.21% | 0.26x | 7.8 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 6 | XMR/USD | 497.36 | 57.691 | 65.491 | +2.33% | -0.07% | 0.26x | 11.7 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | LINK/USD | 9.03197 | 53.219 | 54.318 | +0.30% | -0.19% | 0.99x | 5.6 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | JUP/USD | 0.2371 | 45.222 | 30.390 | +0.40% | -0.03% | 10.27x | 14.3 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | BABY/USD | 0.00902 | 39.291 | 58.776 | +6.12% | -5.16% | 1.55x | 33.4 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | ATOM/USD | 1.3029 | 33.280 | 39.945 | +1.61% | -0.07% | 0.37x | 9.2 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | XTZ/USD | 0.21367 | 22.102 | 26.342 | +0.38% | -0.51% | 0.83x | 14.5 | 2026-11-24T09:02:14.639846+00:00 | Not calibrated | WEAK 11/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 82.815 | 0.01278 | -2.21% | 0.26x |
| 2 | XMR/USD | 65.491 | 497.36 | -0.07% | 0.26x |
| 3 | VVV/USD | 65.359 | 24.964 | -0.63% | 2.47x |
| 4 | PEPE/USD | 63.548 | 3.5e-06 | -0.45% | 2.41x |
| 5 | BABY/USD | 58.776 | 0.00902 | -5.16% | 1.55x |
| 6 | LINK/USD | 54.318 | 9.03197 | -0.19% | 0.99x |
| 7 | LUNA/USD | 53.925 | 4.558e-05 | -0.26% | 4.70x |
| 8 | BAT/USD | 50.812 | 0.07948 | -0.26% | 5.25x |
| 9 | ATOM/USD | 39.945 | 1.3029 | -0.07% | 0.37x |
| 10 | JUP/USD | 30.390 | 0.2371 | -0.03% | 10.27x |
| 11 | XTZ/USD | 26.342 | 0.21367 | -0.51% | 0.83x |

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

- Persisted scans: 1553; predictions: 13367; observations: 940875.
- Matured sampled outcomes across 1/6/24/48h: 25349; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45360949460 · **Generation:** 1553 · **Legacy run:** 45360949460
**Main quote time:** 2026-11-24T09:02:22.606045+00:00 · **Legacy report time:** 2026-11-24T09:03:34.608868+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 24.964 | 76.92 | -0.63% | 2.47x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | PEPE/USD | 3.5e-06 | 75.43 | -0.45% | 2.41x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | LUNA/USD | 4.558e-05 | 67.62 | -0.26% | 4.70x | MODERATE 54/100 | VERY_HIGH 78/100 | Watch |
| 4 | BAT/USD | 0.07948 | 64.50 | -0.26% | 5.25x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 5 | MON/USD | 0.01278 | 64.42 | -2.21% | 0.26x | WEAK 37/100 | VERY_HIGH 80/100 | Do nothing |
| 6 | XMR/USD | 497.36 | 57.69 | -0.07% | 0.26x | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | LINK/USD | 9.03197 | 53.22 | -0.19% | 0.99x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 8 | JUP/USD | 0.2371 | 45.22 | -0.03% | 10.27x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 9 | BABY/USD | 0.00902 | 39.29 | -5.16% | 1.55x | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | ATOM/USD | 1.3029 | 33.28 | -0.07% | 0.37x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | XTZ/USD | 0.21367 | 22.10 | -0.51% | 0.83x | WEAK 11/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
