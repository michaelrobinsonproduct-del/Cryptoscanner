# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T04:07:36.652674+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46105826834
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 07762c1506d731d1240e29380d4f912c4990b27e (atomic ledger/results publication)
**Ledger generation:** 2103 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 419.69 | 69.356 | 72.295 | +3.05% | -0.05% | 0.73x | 8.1 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | ZEC/USD | 749.47 | 63.567 | 67.731 | +2.03% | +0.20% | 0.48x | 2.9 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | VVV/USD | 25.939 | 63.255 | 47.134 | +0.74% | +0.22% | 3.01x | 8.5 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0491 | 62.233 | 60.690 | +1.02% | +0.12% | 1.09x | 3.0 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 5 | HYPE/USD | 64.35 | 56.105 | 63.703 | +1.35% | +0.23% | 0.12x | 1.6 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SENT/USD | 0.024465 | 51.349 | 51.002 | +3.17% | +0.73% | 0.67x | 4.1 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | CC/USD | 0.07543 | 43.887 | 45.337 | +1.73% | +0.21% | 0.75x | 2.6 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | BCH/USD | 209.22 | 39.083 | 42.986 | +1.07% | +0.11% | 0.55x | 2.9 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | W/USD | 0.00925 | 29.357 | 30.709 | +0.43% | +0.54% | 0.59x | 10.8 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | SPX/USD | 0.2742 | 27.736 | 25.595 | +0.66% | +0.22% | 1.10x | 21.9 | 2026-11-28T04:07:30.276659+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 72.295 | 419.69 | -0.05% | 0.73x |
| 2 | ZEC/USD | 67.731 | 749.47 | +0.20% | 0.48x |
| 3 | HYPE/USD | 63.703 | 64.35 | +0.23% | 0.12x |
| 4 | NEAR/USD | 60.690 | 3.0491 | +0.12% | 1.09x |
| 5 | SENT/USD | 51.002 | 0.024465 | +0.73% | 0.67x |
| 6 | VVV/USD | 47.134 | 25.939 | +0.22% | 3.01x |
| 7 | CC/USD | 45.337 | 0.07543 | +0.21% | 0.75x |
| 8 | BCH/USD | 42.986 | 209.22 | +0.11% | 0.55x |
| 9 | W/USD | 30.709 | 0.00925 | +0.54% | 0.59x |
| 10 | SPX/USD | 25.595 | 0.2742 | +0.22% | 1.10x |

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

- Persisted scans: 2103; predictions: 18883; observations: 1273464.
- Matured sampled outcomes across 1/6/24/48h: 43754; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46105826834 · **Generation:** 2103 · **Legacy run:** 46105826834
**Main quote time:** 2026-11-28T04:07:36.652674+00:00 · **Legacy report time:** 2026-11-28T04:08:17.880338+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 419.69 | 69.36 | -0.05% | 0.73x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 2 | ZEC/USD | 749.47 | 63.57 | +0.20% | 0.48x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 3 | VVV/USD ⭐ | 25.939 | 63.25 | +0.22% | 3.01x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD ⭐ | 3.0491 | 62.23 | +0.12% | 1.09x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 5 | HYPE/USD | 64.35 | 56.11 | +0.23% | 0.12x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 6 | SENT/USD | 0.024465 | 51.35 | +0.73% | 0.67x | MODERATE 56/100 | VERY_HIGH 82/100 | Watch |
| 7 | CC/USD | 0.07543 | 43.89 | +0.21% | 0.75x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 8 | BCH/USD | 209.22 | 39.08 | +0.11% | 0.55x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 9 | W/USD | 0.00925 | 29.36 | +0.54% | 0.59x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 10 | SPX/USD | 0.2742 | 27.74 | +0.22% | 1.10x | WEAK 39/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0482 | 59.42 | +0.12% | 1.09x | 13040 | MODERATE 65/100 | HIGH 62/100 | Watch |
| 2 | VVV/USD ⭐ | 25.939 | 49.26 | +0.22% | 3.01x | 8346 | STRONG 90/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
