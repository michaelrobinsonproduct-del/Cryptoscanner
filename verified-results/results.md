# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T01:55:24.682615+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44852895656
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 717112f61d1b78029f789d8a456089aa21e7b3ca (atomic ledger/results publication)
**Ledger generation:** 1059 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.375 | 81.611 | 73.424 | +3.07% | +0.85% | 1.40x | 6.1 | 2026-11-21T01:55:16.858494+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04438 | 57.847 | 40.015 | +1.23% | +0.57% | 7.22x | 9.0 | 2026-11-21T01:55:16.858494+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 3 | DOT/USD | 0.665 | 34.942 | 36.272 | +0.61% | +0.56% | 0.59x | 4.5 | 2026-11-21T01:55:16.858494+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | CC/USD | 0.07496 | 32.359 | 36.006 | +0.55% | +0.48% | 0.39x | 8.0 | 2026-11-21T01:55:16.858494+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.04814 | 31.728 | 27.357 | +0.63% | -0.06% | 1.47x | 18.6 | 2026-11-21T01:55:16.858494+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 6 | DCR/USD | 10.139 | 31.483 | 29.631 | +0.34% | +0.20% | 1.09x | 6.9 | 2026-11-21T01:55:16.858494+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | CT/USD | 0.1234 | 28.635 | 33.032 | +1.90% | +0.41% | 0.36x | 24.4 | 2026-11-21T01:55:16.858494+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | PIEVERSE/USD | 3.0186 | 20.684 | 28.323 | +0.66% | -0.41% | 0.44x | 22.2 | 2026-11-21T01:55:16.858494+00:00 | Not calibrated | WEAK 5/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 73.424 | 21.375 | +0.85% | 1.40x |
| 2 | SKY/USD | 40.015 | 0.04438 | +0.57% | 7.22x |
| 3 | DOT/USD | 36.272 | 0.665 | +0.56% | 0.59x |
| 4 | CC/USD | 36.006 | 0.07496 | +0.48% | 0.39x |
| 5 | CT/USD | 33.032 | 0.1234 | +0.41% | 0.36x |
| 6 | DCR/USD | 29.631 | 10.139 | +0.20% | 1.09x |
| 7 | PIEVERSE/USD | 28.323 | 3.0186 | -0.41% | 0.44x |
| 8 | MEGA/USD | 27.357 | 0.04814 | -0.06% | 1.47x |

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

- Persisted scans: 1059; predictions: 8496; observations: 640232.
- Matured sampled outcomes across 1/6/24/48h: 10945; gap abstentions: 19286. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44852895656 · **Generation:** 1059 · **Legacy run:** 44852895656
**Main quote time:** 2026-11-21T01:55:24.682615+00:00 · **Legacy report time:** 2026-11-21T01:56:07.854558+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.375 | 81.61 | +0.85% | 1.40x | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04438 | 57.85 | +0.57% | 7.22x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 3 | DOT/USD | 0.665 | 34.94 | +0.56% | 0.59x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 4 | CC/USD | 0.07496 | 32.36 | +0.48% | 0.39x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |
| 5 | MEGA/USD | 0.04814 | 31.73 | -0.06% | 1.47x | WEAK 31/100 | VERY_HIGH 72/100 | Do nothing |
| 6 | DCR/USD | 10.139 | 31.48 | +0.20% | 1.09x | WEAK 41/100 | VERY_HIGH 74/100 | Watch |
| 7 | CT/USD | 0.1234 | 28.63 | +0.41% | 0.36x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 8 | PIEVERSE/USD | 3.0186 | 20.68 | -0.41% | 0.44x | WEAK 5/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.325 | 75.03 | +0.85% | 1.40x | 11676 | STRONG 88/100 | HIGH 61/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04438 | 51.47 | +0.57% | 7.22x | 5901 | STRONG 91/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** VVV/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
