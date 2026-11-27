# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T17:42:28.367414+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46043559855
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c0c7ef89e14d572312b9d83fc9f47ad1a76ad194 (atomic ledger/results publication)
**Ledger generation:** 2039 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 727.9 | 91.109 | 98.489 | +6.78% | -1.64% | 1.08x | 3.0 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 2 | XDG/USD | 0.0573033 | 63.948 | 66.254 | +1.65% | -0.62% | 1.08x | 0.6 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 3 | SPACE/USD | 0.00416 | 63.205 | 70.958 | +7.44% | -0.48% | 0.46x | 9.6 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | WEAK 37/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | HYPE/USD | 62.74 | 60.633 | 60.053 | +0.84% | -0.84% | 1.48x | 1.6 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04922 | 60.562 | 64.182 | +1.55% | -0.62% | 0.95x | 2.0 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SOL/USD | 71.34 | 56.970 | 58.246 | +0.56% | -0.67% | 1.21x | 1.4 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 7 | FET/USD | 0.1252 | 55.047 | 57.032 | +3.99% | -0.32% | 0.96x | 16.0 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 8 | UNI/USD | 4.7463 | 55.037 | 63.991 | +2.07% | -0.15% | 0.18x | 5.5 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | PAXG/USD | 3619.83 | 52.862 | 54.778 | +1.77% | +0.02% | 0.80x | 0.7 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | MODERATE 46/100 | HIGH 62/100 | Watch | WATCH |
| 10 | TON/USD | 0.982 | 44.423 | 41.427 | +1.97% | +0.00% | 1.30x | 10.2 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | WEAK 42/100 | HIGH 66/100 | Watch | WATCH |
| 11 | XAUT/USD | 3623.3 | 41.056 | 49.765 | +1.79% | +0.06% | 0.10x | 0.3 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XTZ/USD | 0.22225 | 33.793 | 29.571 | +0.67% | -0.29% | 1.57x | 12.1 | 2026-11-27T17:42:21.086099+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.489 | 727.9 | -1.64% | 1.08x |
| 2 | SPACE/USD | 70.958 | 0.00416 | -0.48% | 0.46x |
| 3 | XDG/USD | 66.254 | 0.0573033 | -0.62% | 1.08x |
| 4 | NIGHT/USD | 64.182 | 0.04922 | -0.62% | 0.95x |
| 5 | UNI/USD | 63.991 | 4.7463 | -0.15% | 0.18x |
| 6 | HYPE/USD | 60.053 | 62.74 | -0.84% | 1.48x |
| 7 | SOL/USD | 58.246 | 71.34 | -0.67% | 1.21x |
| 8 | FET/USD | 57.032 | 0.1252 | -0.32% | 0.96x |
| 9 | PAXG/USD | 54.778 | 3619.83 | +0.02% | 0.80x |
| 10 | XAUT/USD | 49.765 | 3623.3 | +0.06% | 0.10x |
| 11 | TON/USD | 41.427 | 0.982 | +0.00% | 1.30x |
| 12 | XTZ/USD | 29.571 | 0.22225 | -0.29% | 1.57x |

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

- Persisted scans: 2039; predictions: 18170; observations: 1234704.
- Matured sampled outcomes across 1/6/24/48h: 40750; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46043559855 · **Generation:** 2039 · **Legacy run:** 46043559855
**Main quote time:** 2026-11-27T17:42:28.367414+00:00 · **Legacy report time:** 2026-11-27T17:43:22.993273+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 727.9 | 91.11 | -1.64% | 1.08x | MODERATE 56/100 | VERY_HIGH 72/100 | Do nothing |
| 2 | XDG/USD | 0.0573033 | 63.95 | -0.62% | 1.08x | WEAK 42/100 | HIGH 68/100 | Watch |
| 3 | SPACE/USD | 0.00416 | 63.21 | -0.48% | 0.46x | WEAK 37/100 | EXTREME 88/100 | Do nothing |
| 4 | HYPE/USD | 62.74 | 60.63 | -0.84% | 1.48x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD | 0.04922 | 60.56 | -0.62% | 0.95x | WEAK 35/100 | HIGH 68/100 | Watch |
| 6 | SOL/USD | 71.34 | 56.97 | -0.67% | 1.21x | WEAK 38/100 | HIGH 68/100 | Watch |
| 7 | FET/USD | 0.1252 | 55.05 | -0.32% | 0.96x | WEAK 28/100 | VERY_HIGH 74/100 | Do nothing |
| 8 | UNI/USD | 4.7463 | 55.04 | -0.15% | 0.18x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | PAXG/USD | 3619.83 | 52.86 | +0.02% | 0.80x | MODERATE 46/100 | HIGH 62/100 | Watch |
| 10 | TON/USD | 0.982 | 44.42 | +0.00% | 1.30x | WEAK 42/100 | HIGH 66/100 | Watch |
| 11 | XAUT/USD | 3623.3 | 41.06 | +0.06% | 0.10x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |
| 12 | XTZ/USD | 0.22225 | 33.79 | -0.29% | 1.57x | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing |

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
