# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T22:27:19.779805+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45279385587
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bd8e18a87b11dcf3f61995783659b0eed7380188 (atomic ledger/results publication)
**Ledger generation:** 1489 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 12s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.22 | 107.195 | 97.118 | +8.91% | -0.48% | 2.25x | 5.8 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08068 | 85.653 | 91.669 | +6.96% | -0.23% | 0.52x | 6.2 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SHX/USD | 0.00361 | 81.917 | 69.397 | +6.96% | -0.50% | 3.02x | 13.9 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | CAP/USD | 0.101227 | 73.746 | 69.850 | +8.18% | -2.22% | 3.77x | 18.7 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | ATOM/USD | 1.2489 | 71.986 | 73.650 | +6.56% | -0.36% | 1.01x | 8.8 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | PAXG/USD | 3625.66 | 67.482 | 61.291 | +1.50% | +0.11% | 1.56x | 0.7 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 72.18 | 66.269 | 69.669 | +2.19% | +0.22% | 0.55x | 1.4 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | LTC/USD | 41.12 | 64.787 | 69.301 | +2.39% | -0.02% | 0.56x | 4.9 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | CC/USD | 0.07709 | 64.068 | 70.888 | +5.21% | +0.01% | 0.31x | 3.9 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | XRP/USD | 0.93913 | 64.022 | 63.534 | +1.25% | +0.08% | 1.01x | 0.4 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 11 | WINGS/USD | 0.002057 | 63.787 | 70.075 | +7.75% | +0.19% | 0.27x | 14.5 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | XDG/USD | 0.056123 | 63.652 | 65.137 | +1.52% | +0.04% | 0.83x | 1.0 | 2026-11-23T22:27:08.059384+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.118 | 156.22 | -0.48% | 2.25x |
| 2 | ALGO/USD | 91.669 | 0.08068 | -0.23% | 0.52x |
| 3 | ATOM/USD | 73.650 | 1.2489 | -0.36% | 1.01x |
| 4 | CC/USD | 70.888 | 0.07709 | +0.01% | 0.31x |
| 5 | WINGS/USD | 70.075 | 0.002057 | +0.19% | 0.27x |
| 6 | CAP/USD | 69.850 | 0.101227 | -2.22% | 3.77x |
| 7 | SOL/USD | 69.669 | 72.18 | +0.22% | 0.55x |
| 8 | SHX/USD | 69.397 | 0.00361 | -0.50% | 3.02x |
| 9 | LTC/USD | 69.301 | 41.12 | -0.02% | 0.56x |
| 10 | XDG/USD | 65.137 | 0.056123 | +0.04% | 0.83x |
| 11 | XRP/USD | 63.534 | 0.93913 | +0.08% | 1.01x |
| 12 | PAXG/USD | 61.291 | 3625.66 | +0.11% | 1.56x |

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

- Persisted scans: 1489; predictions: 12635; observations: 901903.
- Matured sampled outcomes across 1/6/24/48h: 22864; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45279385587 · **Generation:** 1489 · **Legacy run:** 45279385587
**Main quote time:** 2026-11-23T22:27:19.779805+00:00 · **Legacy report time:** 2026-11-23T22:28:27.895045+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 156.22 | 107.20 | -0.48% | 2.25x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | ALGO/USD | 0.08068 | 85.65 | -0.23% | 0.52x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 3 | SHX/USD | 0.00361 | 81.92 | -0.50% | 3.02x | MODERATE 66/100 | VERY_HIGH 79/100 | Watch |
| 4 | CAP/USD | 0.101227 | 73.75 | -2.22% | 3.77x | MODERATE 62/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | ATOM/USD | 1.2489 | 71.99 | -0.36% | 1.01x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |
| 6 | PAXG/USD | 3625.66 | 67.48 | +0.11% | 1.56x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 72.18 | 66.27 | +0.22% | 0.55x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | LTC/USD | 41.12 | 64.79 | -0.02% | 0.56x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | CC/USD | 0.07709 | 64.07 | +0.01% | 0.31x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 10 | XRP/USD | 0.93913 | 64.02 | +0.08% | 1.01x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 11 | WINGS/USD | 0.002057 | 63.79 | +0.19% | 0.27x | MODERATE 47/100 | VERY_HIGH 81/100 | Watch |
| 12 | XDG/USD | 0.056123 | 63.65 | +0.04% | 0.83x | MODERATE 52/100 | HIGH 62/100 | Watch |

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
