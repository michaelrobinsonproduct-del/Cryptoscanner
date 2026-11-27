# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T21:52:42.824760+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46072769880
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 78e7ee1d15bbb412080f74084d2a308e11b10c4d (atomic ledger/results publication)
**Ledger generation:** 2065 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 735.98 | 96.394 | 99.864 | +7.97% | -0.05% | 0.68x | 0.3 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04999 | 89.558 | 75.953 | +3.14% | -0.28% | 3.49x | 2.0 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PAXG/USD | 3642.94 | 75.434 | 60.520 | +2.42% | -0.02% | 38.39x | 0.0 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 4 | HYPE/USD | 63.97 | 74.058 | 73.125 | +2.81% | -0.09% | 1.14x | 3.1 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 5 | SOL/USD | 71.9 | 71.542 | 63.777 | +1.35% | +0.11% | 1.72x | 1.4 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0575724 | 71.405 | 69.866 | +2.12% | -0.08% | 1.19x | 0.0 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 7 | LINK/USD | 9.31743 | 70.360 | 57.284 | +0.53% | -0.38% | 50.25x | 2.8 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 8 | RENDER/USD | 1.407 | 60.571 | 64.908 | +5.55% | +0.43% | 0.35x | 14.2 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6735 | 59.587 | 59.595 | +0.87% | -0.07% | 1.04x | 3.0 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | WLD/USD | 0.2457 | 59.554 | 44.351 | +1.65% | +0.04% | 9.24x | 4.1 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 11 | LTC/USD | 44.37 | 59.000 | 63.955 | +1.44% | +0.07% | 0.47x | 2.3 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TAO/USD | 187.3972 | 56.958 | 65.256 | +1.97% | +0.18% | 0.08x | 7.0 | 2026-11-27T21:52:35.023951+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.864 | 735.98 | -0.05% | 0.68x |
| 2 | NIGHT/USD | 75.953 | 0.04999 | -0.28% | 3.49x |
| 3 | HYPE/USD | 73.125 | 63.97 | -0.09% | 1.14x |
| 4 | XDG/USD | 69.866 | 0.0575724 | -0.08% | 1.19x |
| 5 | TAO/USD | 65.256 | 187.3972 | +0.18% | 0.08x |
| 6 | RENDER/USD | 64.908 | 1.407 | +0.43% | 0.35x |
| 7 | LTC/USD | 63.955 | 44.37 | +0.07% | 0.47x |
| 8 | SOL/USD | 63.777 | 71.9 | +0.11% | 1.72x |
| 9 | PAXG/USD | 60.520 | 3642.94 | -0.02% | 38.39x |
| 10 | SUI/USD | 59.595 | 0.6735 | -0.07% | 1.04x |
| 11 | LINK/USD | 57.284 | 9.31743 | -0.38% | 50.25x |
| 12 | WLD/USD | 44.351 | 0.2457 | +0.04% | 9.24x |

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

- Persisted scans: 2065; predictions: 18482; observations: 1250438.
- Matured sampled outcomes across 1/6/24/48h: 41987; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
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

**Writer:** 46072769880 · **Generation:** 2065 · **Legacy run:** 46072769880
**Main quote time:** 2026-11-27T21:52:42.824760+00:00 · **Legacy report time:** 2026-11-27T21:53:39.522982+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 735.98 | 96.39 | -0.05% | 0.68x | MODERATE 53/100 | VERY_HIGH 76/100 | Watch |
| 2 | NIGHT/USD | 0.04999 | 89.56 | -0.28% | 3.49x | STRONG 75/100 | HIGH 61/100 | Watch |
| 3 | PAXG/USD | 3642.94 | 75.43 | -0.02% | 38.39x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 4 | HYPE/USD | 63.97 | 74.06 | -0.09% | 1.14x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 5 | SOL/USD | 71.9 | 71.54 | +0.11% | 1.72x | STRONG 71/100 | HIGH 55/100 | Watch |
| 6 | XDG/USD | 0.0575724 | 71.41 | -0.08% | 1.19x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 7 | LINK/USD | 9.31743 | 70.36 | -0.38% | 50.25x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 8 | RENDER/USD | 1.407 | 60.57 | +0.43% | 0.35x | MODERATE 55/100 | VERY_HIGH 81/100 | Watch |
| 9 | SUI/USD | 0.6735 | 59.59 | -0.07% | 1.04x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | WLD/USD | 0.2457 | 59.55 | +0.04% | 9.24x | STRONG 75/100 | HIGH 60/100 | Watch |
| 11 | LTC/USD | 44.37 | 59.00 | +0.07% | 0.47x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | TAO/USD | 187.3972 | 56.96 | +0.18% | 0.08x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD | 0.05304 | 85.59 | +1.98% | 2.23x | 8235 | STRONG 93/100 | HIGH 61/100 | Consider small entry |
| 2 | ENA/USD | 0.104 | 79.51 | +0.29% | 47.81x | 2769 | STRONG 95/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
