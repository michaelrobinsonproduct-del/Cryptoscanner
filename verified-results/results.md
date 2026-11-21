# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T02:20:31.228324+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44855259149
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 20a4318094873133f4edec3b16d4009dbd8274cc (atomic ledger/results publication)
**Ledger generation:** 1063 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XDG/USD | 0.0545509 | 59.070 | 58.283 | +0.51% | +0.15% | 1.00x | 0.6 | 2026-11-21T02:20:24.957337+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 2 | SKY/USD | 0.0444 | 58.462 | 42.559 | +1.28% | +0.18% | 7.11x | 4.5 | 2026-11-21T02:20:24.957337+00:00 | Not calibrated | STRONG 74/100 | HIGH 60/100 | Watch | WATCH |
| 3 | VVV/USD | 21.074 | 56.365 | 63.221 | +1.62% | -0.67% | 0.65x | 6.2 | 2026-11-21T02:20:24.957337+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | ADA/USD | 0.143271 | 55.962 | 56.051 | +0.29% | +0.11% | 0.94x | 2.0 | 2026-11-21T02:20:24.957337+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 5 | DCR/USD | 10.211 | 47.283 | 32.723 | +1.05% | -0.09% | 6.57x | 10.8 | 2026-11-21T02:20:24.957337+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | ALGO/USD | 0.07357 | 39.980 | 38.624 | +0.56% | +0.12% | 1.07x | 8.2 | 2026-11-21T02:20:24.957337+00:00 | Not calibrated | MODERATE 45/100 | HIGH 62/100 | Watch | WATCH |
| 7 | DOT/USD | 0.6656 | 33.569 | 37.624 | +0.70% | -0.12% | 0.65x | 3.0 | 2026-11-21T02:20:24.957337+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | AB/USD | 0.000527 | 15.488 | 17.786 | +0.38% | +0.76% | 0.39x | 38.0 | 2026-11-21T02:20:24.957337+00:00 | Not calibrated | WEAK 23/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 63.221 | 21.074 | -0.67% | 0.65x |
| 2 | XDG/USD | 58.283 | 0.0545509 | +0.15% | 1.00x |
| 3 | ADA/USD | 56.051 | 0.143271 | +0.11% | 0.94x |
| 4 | SKY/USD | 42.559 | 0.0444 | +0.18% | 7.11x |
| 5 | ALGO/USD | 38.624 | 0.07357 | +0.12% | 1.07x |
| 6 | DOT/USD | 37.624 | 0.6656 | -0.12% | 0.65x |
| 7 | DCR/USD | 32.723 | 10.211 | -0.09% | 6.57x |
| 8 | AB/USD | 17.786 | 0.000527 | +0.76% | 0.39x |

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

- Persisted scans: 1063; predictions: 8534; observations: 642664.
- Matured sampled outcomes across 1/6/24/48h: 10965; gap abstentions: 19385. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44855259149 · **Generation:** 1063 · **Legacy run:** 44855259149
**Main quote time:** 2026-11-21T02:20:31.228324+00:00 · **Legacy report time:** 2026-11-21T02:21:16.491282+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0545509 | 59.07 | +0.15% | 1.00x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 2 | SKY/USD ⭐ | 0.0444 | 58.46 | +0.18% | 7.11x | STRONG 84/100 | HIGH 60/100 | Watch |
| 3 | VVV/USD | 21.074 | 56.36 | -0.67% | 0.65x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | ADA/USD | 0.143271 | 55.96 | +0.11% | 0.94x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 5 | DCR/USD | 10.211 | 47.28 | -0.09% | 6.57x | MODERATE 49/100 | VERY_HIGH 79/100 | Watch |
| 6 | ALGO/USD ⭐ | 0.07357 | 39.98 | +0.12% | 1.07x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 7 | DOT/USD | 0.6656 | 33.57 | -0.12% | 0.65x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | AB/USD | 0.000527 | 15.49 | +0.76% | 0.39x | WEAK 23/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0545322 | 57.75 | +0.15% | 1.00x | 12034 | MODERATE 64/100 | HIGH 62/100 | Watch |
| 2 | SKY/USD ⭐ | 0.0444 | 55.38 | +0.18% | 7.11x | 5834 | STRONG 83/100 | HIGH 60/100 | Watch |
| 3 | ALGO/USD ⭐ | 0.07357 | 36.06 | +0.12% | 1.07x | 5273 | MODERATE 53/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XDG/USD, SKY/USD, ALGO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
