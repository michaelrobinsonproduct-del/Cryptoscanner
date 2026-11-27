# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T20:02:32.920348+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46060501235
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f0a2e07d1c4c779e8a0cd22c8ca60c6694ca277b (atomic ledger/results publication)
**Ledger generation:** 2053 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 742.54 | 102.871 | 98.317 | +8.93% | -0.11% | 1.51x | 3.4 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05025 | 94.624 | 76.729 | +3.67% | +0.58% | 3.23x | 8.0 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 4.8327 | 79.027 | 78.389 | +3.93% | -0.28% | 1.20x | 3.5 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94898 | 72.845 | 59.573 | +0.66% | -0.14% | 2.40x | 0.1 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SKY/USD | 0.04913 | 72.621 | 72.179 | +5.86% | +0.47% | 0.81x | 8.1 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | MODERATE 66/100 | HIGH 67/100 | Watch | WATCH |
| 6 | LTC/USD | 43.96 | 71.249 | 57.383 | +0.50% | -0.02% | 2.40x | 2.3 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.057619 | 68.148 | 70.149 | +2.21% | -0.42% | 1.01x | 0.6 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 8 | HYPE/USD | 63.82 | 63.862 | 72.217 | +2.57% | -0.02% | 0.17x | 1.6 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SOL/USD | 71.89 | 61.279 | 63.679 | +1.34% | -0.48% | 1.00x | 1.4 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6722 | 59.808 | 58.974 | +0.67% | -0.33% | 1.25x | 1.5 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 11 | PAXG/USD | 3643.38 | 57.596 | 59.916 | +2.44% | +0.07% | 0.73x | 0.0 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | INJ/USD | 6.369 | 54.669 | 60.062 | +2.86% | -0.31% | 0.62x | 4.7 | 2026-11-27T20:02:26.676614+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.317 | 742.54 | -0.11% | 1.51x |
| 2 | UNI/USD | 78.389 | 4.8327 | -0.28% | 1.20x |
| 3 | NIGHT/USD | 76.729 | 0.05025 | +0.58% | 3.23x |
| 4 | HYPE/USD | 72.217 | 63.82 | -0.02% | 0.17x |
| 5 | SKY/USD | 72.179 | 0.04913 | +0.47% | 0.81x |
| 6 | XDG/USD | 70.149 | 0.057619 | -0.42% | 1.01x |
| 7 | SOL/USD | 63.679 | 71.89 | -0.48% | 1.00x |
| 8 | INJ/USD | 60.062 | 6.369 | -0.31% | 0.62x |
| 9 | PAXG/USD | 59.916 | 3643.38 | +0.07% | 0.73x |
| 10 | XRP/USD | 59.573 | 0.94898 | -0.14% | 2.40x |
| 11 | SUI/USD | 58.974 | 0.6722 | -0.33% | 1.25x |
| 12 | LTC/USD | 57.383 | 43.96 | -0.02% | 2.40x |

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

- Persisted scans: 2053; predictions: 18338; observations: 1243174.
- Matured sampled outcomes across 1/6/24/48h: 41435; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46060501235 · **Generation:** 2053 · **Legacy run:** 46060501235
**Main quote time:** 2026-11-27T20:02:32.920348+00:00 · **Legacy report time:** 2026-11-27T20:03:28.470635+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 742.54 | 102.87 | -0.11% | 1.51x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.05025 | 94.62 | +0.58% | 3.23x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD | 4.8327 | 79.03 | -0.28% | 1.20x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 4 | XRP/USD | 0.94898 | 72.84 | -0.14% | 2.40x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 5 | SKY/USD | 0.04913 | 72.62 | +0.47% | 0.81x | MODERATE 66/100 | HIGH 67/100 | Watch |
| 6 | LTC/USD | 43.96 | 71.25 | -0.02% | 2.40x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.057619 | 68.15 | -0.42% | 1.01x | WEAK 44/100 | HIGH 68/100 | Watch |
| 8 | HYPE/USD | 63.82 | 63.86 | -0.02% | 0.17x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | SOL/USD | 71.89 | 61.28 | -0.48% | 1.00x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | SUI/USD | 0.6722 | 59.81 | -0.33% | 1.25x | WEAK 40/100 | HIGH 68/100 | Watch |
| 11 | PAXG/USD | 3643.38 | 57.60 | +0.07% | 0.73x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | INJ/USD | 6.369 | 54.67 | -0.31% | 0.62x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05035 | 100.00 | +0.58% | 3.23x | 17852 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
