# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T22:22:23.224980+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46075935693
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 58c421cb2d63fe60d334c8bb077cfb3b1ee73bd7 (atomic ledger/results publication)
**Ledger generation:** 2068 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 722.61 | 93.231 | 95.115 | +6.01% | -0.74% | 1.18x | 3.9 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | MODERATE 57/100 | HIGH 68/100 | Watch | WATCH |
| 2 | HYPE/USD | 63.44 | 80.505 | 67.937 | +1.96% | -0.49% | 27.92x | 1.6 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04992 | 76.870 | 74.939 | +2.99% | +0.04% | 1.17x | 2.0 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XAUT/USD | 3650.9 | 70.339 | 54.654 | +2.56% | +0.14% | 6.83x | 2.5 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 71.5 | 68.117 | 59.826 | +0.79% | -0.38% | 2.02x | 1.4 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0572221 | 66.904 | 65.516 | +1.50% | -0.31% | 1.30x | 0.0 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |
| 7 | UNI/USD | 4.8019 | 66.487 | 72.466 | +3.26% | -0.61% | 0.71x | 4.0 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | LIGHTER/USD | 2.621 | 65.178 | 62.996 | +5.60% | -0.76% | 1.60x | 19.1 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | PAXG/USD | 3646.87 | 62.309 | 61.575 | +2.53% | +0.12% | 1.01x | 0.3 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 10 | TREAD/USD | 1.3431 | 58.078 | 60.628 | +11.76% | -0.66% | 1.08x | 30.5 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | WEAK 29/100 | EXTREME 92/100 | Do nothing | WATCH |
| 11 | LTC/USD | 44.18 | 57.476 | 59.658 | +1.01% | -0.32% | 0.94x | 4.5 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | RENDER/USD | 1.391 | 57.033 | 59.886 | +4.35% | -0.36% | 0.89x | 7.2 | 2026-11-27T22:22:15.534604+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 95.115 | 722.61 | -0.74% | 1.18x |
| 2 | NIGHT/USD | 74.939 | 0.04992 | +0.04% | 1.17x |
| 3 | UNI/USD | 72.466 | 4.8019 | -0.61% | 0.71x |
| 4 | HYPE/USD | 67.937 | 63.44 | -0.49% | 27.92x |
| 5 | XDG/USD | 65.516 | 0.0572221 | -0.31% | 1.30x |
| 6 | LIGHTER/USD | 62.996 | 2.621 | -0.76% | 1.60x |
| 7 | PAXG/USD | 61.575 | 3646.87 | +0.12% | 1.01x |
| 8 | TREAD/USD | 60.628 | 1.3431 | -0.66% | 1.08x |
| 9 | RENDER/USD | 59.886 | 1.391 | -0.36% | 0.89x |
| 10 | SOL/USD | 59.826 | 71.5 | -0.38% | 2.02x |
| 11 | LTC/USD | 59.658 | 44.18 | -0.32% | 0.94x |
| 12 | XAUT/USD | 54.654 | 3650.9 | +0.14% | 6.83x |

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

- Persisted scans: 2068; predictions: 18518; observations: 1252256.
- Matured sampled outcomes across 1/6/24/48h: 42143; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
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

**Writer:** 46075935693 · **Generation:** 2068 · **Legacy run:** 46075935693
**Main quote time:** 2026-11-27T22:22:23.224980+00:00 · **Legacy report time:** 2026-11-27T22:23:04.762879+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 722.61 | 93.23 | -0.74% | 1.18x | MODERATE 57/100 | HIGH 68/100 | Watch |
| 2 | HYPE/USD | 63.44 | 80.51 | -0.49% | 27.92x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | NIGHT/USD | 0.04992 | 76.87 | +0.04% | 1.17x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 4 | XAUT/USD ⭐ | 3650.9 | 70.34 | +0.14% | 6.83x | STRONG 90/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD | 71.5 | 68.12 | -0.38% | 2.02x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | XDG/USD | 0.0572221 | 66.90 | -0.31% | 1.30x | WEAK 43/100 | HIGH 61/100 | Watch |
| 7 | UNI/USD | 4.8019 | 66.49 | -0.61% | 0.71x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 8 | LIGHTER/USD | 2.621 | 65.18 | -0.76% | 1.60x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 9 | PAXG/USD ⭐ | 3646.87 | 62.31 | +0.12% | 1.01x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 10 | TREAD/USD | 1.3431 | 58.08 | -0.66% | 1.08x | WEAK 29/100 | EXTREME 92/100 | Do nothing |
| 11 | LTC/USD | 44.18 | 57.48 | -0.32% | 0.94x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 12 | RENDER/USD | 1.391 | 57.03 | -0.36% | 0.89x | WEAK 34/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3646.81 | 75.33 | +0.12% | 1.01x | 5335 | STRONG 73/100 | HIGH 62/100 | Watch |
| 2 | XAUT/USD ⭐ | 3650.9 | 74.47 | +0.14% | 6.83x | 2457 | STRONG 92/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XAUT/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
