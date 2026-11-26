# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T19:41:04.472780+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45885273271
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a9029173c22bcc28bef06f43463043b18f2041cc (atomic ledger/results publication)
**Ledger generation:** 1904 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38459 | 91.253 | 82.424 | +7.49% | -1.23% | 2.53x | 0.3 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | STRONG 76/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | ZRO/USD | 1.111 | 87.016 | 72.466 | +8.50% | -0.09% | 2.78x | 18.0 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | INJ/USD | 6.278 | 79.053 | 75.526 | +5.44% | +0.46% | 1.12x | 4.8 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ADA/USD | 0.150556 | 75.758 | 77.451 | +3.28% | -0.24% | 0.95x | 1.1 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 5 | SKY/USD | 0.04547 | 74.311 | 76.461 | +8.57% | +0.11% | 0.73x | 6.6 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | LINK/USD | 9.26803 | 73.879 | 69.660 | +2.47% | -0.20% | 1.52x | 2.3 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95262 | 68.248 | 66.951 | +1.71% | -0.18% | 1.22x | 0.1 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 8 | FET/USD | 0.1209 | 67.945 | 70.236 | +11.43% | -0.17% | 0.85x | 16.6 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 9 | ETH/USD | 1703.36 | 66.080 | 60.333 | +0.77% | +0.11% | 1.52x | 0.1 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 10 | AKT/USD | 0.507 | 64.120 | 72.045 | +7.17% | -0.26% | 0.34x | 11.9 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | WEAK 32/100 | EXTREME 87/100 | Do nothing | WATCH |
| 11 | SOL/USD | 71.32 | 60.297 | 63.547 | +1.32% | -0.03% | 0.69x | 1.4 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | HBAR/USD | 0.05462 | 59.531 | 68.018 | +4.84% | -0.18% | 0.24x | 1.8 | 2026-11-26T19:40:57.746040+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 82.424 | 0.38459 | -1.23% | 2.53x |
| 2 | ADA/USD | 77.451 | 0.150556 | -0.24% | 0.95x |
| 3 | SKY/USD | 76.461 | 0.04547 | +0.11% | 0.73x |
| 4 | INJ/USD | 75.526 | 6.278 | +0.46% | 1.12x |
| 5 | ZRO/USD | 72.466 | 1.111 | -0.09% | 2.78x |
| 6 | AKT/USD | 72.045 | 0.507 | -0.26% | 0.34x |
| 7 | FET/USD | 70.236 | 0.1209 | -0.17% | 0.85x |
| 8 | LINK/USD | 69.660 | 9.26803 | -0.20% | 1.52x |
| 9 | HBAR/USD | 68.018 | 0.05462 | -0.18% | 0.24x |
| 10 | XRP/USD | 66.951 | 0.95262 | -0.18% | 1.22x |
| 11 | SOL/USD | 63.547 | 71.32 | -0.03% | 0.69x |
| 12 | ETH/USD | 60.333 | 1703.36 | +0.11% | 1.52x |

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

- Persisted scans: 1904; predictions: 16583; observations: 1153430.
- Matured sampled outcomes across 1/6/24/48h: 35960; gap abstentions: 25195. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45885273271 · **Generation:** 1904 · **Legacy run:** 45885273271
**Main quote time:** 2026-11-26T19:41:04.472780+00:00 · **Legacy report time:** 2026-11-26T19:41:48.233738+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.38459 | 91.25 | -1.23% | 2.53x | STRONG 76/100 | HIGH 65/100 | Do nothing |
| 2 | ZRO/USD | 1.111 | 87.02 | -0.09% | 2.78x | MODERATE 69/100 | VERY_HIGH 72/100 | Watch |
| 3 | INJ/USD ⭐ | 6.278 | 79.05 | +0.46% | 1.12x | STRONG 85/100 | HIGH 62/100 | Watch |
| 4 | ADA/USD | 0.150556 | 75.76 | -0.24% | 0.95x | WEAK 43/100 | HIGH 68/100 | Watch |
| 5 | SKY/USD | 0.04547 | 74.31 | +0.11% | 0.73x | MODERATE 57/100 | VERY_HIGH 75/100 | Watch |
| 6 | LINK/USD | 9.26803 | 73.88 | -0.20% | 1.52x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.95262 | 68.25 | -0.18% | 1.22x | WEAK 44/100 | HIGH 68/100 | Watch |
| 8 | FET/USD | 0.1209 | 67.95 | -0.17% | 0.85x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 9 | ETH/USD | 1703.36 | 66.08 | +0.11% | 1.52x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 10 | AKT/USD | 0.507 | 64.12 | -0.26% | 0.34x | WEAK 32/100 | EXTREME 87/100 | Do nothing |
| 11 | SOL/USD | 71.32 | 60.30 | -0.03% | 0.69x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | HBAR/USD | 0.05462 | 59.53 | -0.18% | 0.24x | WEAK 35/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.283 | 80.04 | +0.46% | 1.12x | 5528 | STRONG 85/100 | HIGH 62/100 | Watch |
| 2 | TREAD/USD | 1.2319 | 74.87 | +0.40% | 1.70x | 2996 | MODERATE 67/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
