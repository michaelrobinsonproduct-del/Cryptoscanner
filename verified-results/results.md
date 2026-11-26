# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T06:48:16.428455+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45770297024
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b0a99b430907b5ef8ce3595b4ba9d92827e22107 (atomic ledger/results publication)
**Ledger generation:** 1826 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07042 | 79.111 | 67.450 | +6.26% | +1.07% | 1.63x | 17.1 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | STRONG 80/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 9.1378 | 72.137 | 57.653 | +1.03% | -0.10% | 3.47x | 5.8 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 43.31 | 65.318 | 63.679 | +1.40% | -0.25% | 1.29x | 2.3 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94807 | 64.975 | 63.181 | +1.23% | -0.14% | 1.25x | 0.8 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | WEAK 42/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002613 | 64.321 | 52.732 | +1.40% | -0.68% | 2.66x | 3.8 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 3.9381 | 61.397 | 65.787 | +11.22% | +0.73% | 0.20x | 33.4 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0562854 | 61.132 | 52.330 | +0.58% | -0.11% | 1.94x | 4.4 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SKY/USD | 0.04387 | 57.212 | 63.442 | +4.75% | +0.37% | 0.19x | 6.8 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | BNB/USD | 554.5 | 52.324 | 37.918 | +0.27% | -0.12% | 2.74x | 2.3 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ADA/USD | 0.147324 | 51.315 | 60.360 | +1.07% | -0.19% | 0.19x | 4.2 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | INJ/USD | 6.122 | 50.727 | 58.709 | +2.82% | -0.15% | 0.28x | 6.6 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XMR/USD | 523.4 | 50.621 | 57.328 | +1.25% | +0.31% | 0.17x | 12.8 | 2026-11-26T06:48:07.921272+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 67.450 | 0.07042 | +1.07% | 1.63x |
| 2 | PIEVERSE/USD | 65.787 | 3.9381 | +0.73% | 0.20x |
| 3 | LTC/USD | 63.679 | 43.31 | -0.25% | 1.29x |
| 4 | SKY/USD | 63.442 | 0.04387 | +0.37% | 0.19x |
| 5 | XRP/USD | 63.181 | 0.94807 | -0.14% | 1.25x |
| 6 | ADA/USD | 60.360 | 0.147324 | -0.19% | 0.19x |
| 7 | INJ/USD | 58.709 | 6.122 | -0.15% | 0.28x |
| 8 | LINK/USD | 57.653 | 9.1378 | -0.10% | 3.47x |
| 9 | XMR/USD | 57.328 | 523.4 | +0.31% | 0.17x |
| 10 | PUMP/USD | 52.732 | 0.002613 | -0.68% | 2.66x |
| 11 | XDG/USD | 52.330 | 0.0562854 | -0.11% | 1.94x |
| 12 | BNB/USD | 37.918 | 554.5 | -0.12% | 2.74x |

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

- Persisted scans: 1826; predictions: 15647; observations: 1107078.
- Matured sampled outcomes across 1/6/24/48h: 33935; gap abstentions: 24115. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45770297024 · **Generation:** 1826 · **Legacy run:** 45770297024
**Main quote time:** 2026-11-26T06:48:16.428455+00:00 · **Legacy report time:** 2026-11-26T06:49:36.684046+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07042 | 79.11 | +1.07% | 1.63x | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 2 | LINK/USD | 9.1378 | 72.14 | -0.10% | 3.47x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 43.31 | 65.32 | -0.25% | 1.29x | WEAK 43/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD | 0.94807 | 64.97 | -0.14% | 1.25x | WEAK 42/100 | HIGH 61/100 | Watch |
| 5 | PUMP/USD | 0.002613 | 64.32 | -0.68% | 2.66x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 6 | PIEVERSE/USD | 3.9381 | 61.40 | +0.73% | 0.20x | MODERATE 51/100 | VERY_HIGH 82/100 | Watch |
| 7 | XDG/USD | 0.0562854 | 61.13 | -0.11% | 1.94x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 8 | SKY/USD | 0.04387 | 57.21 | +0.37% | 0.19x | MODERATE 59/100 | VERY_HIGH 75/100 | Watch |
| 9 | BNB/USD | 554.5 | 52.32 | -0.12% | 2.74x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 10 | ADA/USD | 0.147324 | 51.31 | -0.19% | 0.19x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | INJ/USD | 6.122 | 50.73 | -0.15% | 0.28x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XMR/USD | 523.4 | 50.62 | +0.31% | 0.17x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HONEY/USD | 0.000235 | 94.66 | +2.68% | 1.41x | 14991 | STRONG 77/100 | VERY_HIGH 77/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.07042 | 77.02 | +1.07% | 1.63x | 3679 | STRONG 89/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
