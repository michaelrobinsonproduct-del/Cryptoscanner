# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T19:16:54.027600+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45468122081
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** edb8ad8f6ebd67bd714a457def81f104639e50b1 (atomic ledger/results publication)
**Ledger generation:** 1615 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.621e-05 | 82.718 | 72.773 | +6.30% | -0.06% | 2.03x | 6.5 | 2026-11-24T19:16:49.625465+00:00 | Not calibrated | STRONG 71/100 | HIGH 66/100 | Watch | WATCH |
| 2 | XMR/USD | 502.01 | 67.085 | 72.752 | +3.29% | -0.05% | 0.46x | 10.6 | 2026-11-24T19:16:49.625465+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | VVV/USD | 24.986 | 59.803 | 66.797 | +2.20% | -0.10% | 0.35x | 7.2 | 2026-11-24T19:16:49.625465+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.462e-06 | 51.841 | 49.323 | +1.17% | +0.35% | 1.08x | 5.8 | 2026-11-24T19:16:49.625465+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 5 | GBP/USD | 1.31139 | 51.066 | 59.296 | +0.62% | +0.04% | 0.16x | 0.2 | 2026-11-24T19:16:49.625465+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AUD/USD | 0.66474 | 44.251 | 44.658 | +0.32% | +0.03% | 0.94x | 1.2 | 2026-11-24T19:16:49.625465+00:00 | Not calibrated | WEAK 42/100 | HIGH 62/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04863 | 38.791 | 45.953 | +1.00% | +0.14% | 0.21x | 4.1 | 2026-11-24T19:16:49.625465+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 72.773 | 4.621e-05 | -0.06% | 2.03x |
| 2 | XMR/USD | 72.752 | 502.01 | -0.05% | 0.46x |
| 3 | VVV/USD | 66.797 | 24.986 | -0.10% | 0.35x |
| 4 | GBP/USD | 59.296 | 1.31139 | +0.04% | 0.16x |
| 5 | PEPE/USD | 49.323 | 3.462e-06 | +0.35% | 1.08x |
| 6 | NIGHT/USD | 45.953 | 0.04863 | +0.14% | 0.21x |
| 7 | AUD/USD | 44.658 | 0.66474 | +0.03% | 0.94x |

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

- Persisted scans: 1615; predictions: 13866; observations: 978627.
- Matured sampled outcomes across 1/6/24/48h: 28088; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45468122081 · **Generation:** 1615 · **Legacy run:** 45468122081
**Main quote time:** 2026-11-24T19:16:54.027600+00:00 · **Legacy report time:** 2026-11-24T19:17:51.208479+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.621e-05 | 82.72 | -0.06% | 2.03x | STRONG 71/100 | HIGH 66/100 | Watch |
| 2 | XMR/USD | 502.01 | 67.08 | -0.05% | 0.46x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | VVV/USD | 24.986 | 59.80 | -0.10% | 0.35x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.462e-06 | 51.84 | +0.35% | 1.08x | STRONG 71/100 | HIGH 62/100 | Watch |
| 5 | GBP/USD | 1.31139 | 51.07 | +0.04% | 0.16x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 6 | AUD/USD | 0.66474 | 44.25 | +0.03% | 0.94x | WEAK 42/100 | HIGH 62/100 | Watch |
| 7 | NIGHT/USD | 0.04863 | 38.79 | +0.14% | 0.21x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.462e-06 | 49.24 | +0.35% | 1.08x | 6690 | STRONG 70/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
