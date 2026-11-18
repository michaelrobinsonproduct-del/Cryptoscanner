# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:40:06.528415+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44252957219
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** c5f67e1cf3a9bf48d0c0000b0b27c59f75082574 (atomic ledger/results publication)
**Ledger generation:** 557 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.3003 | 69.193 | 70.074 | +8.76% | +0.98% | 0.42x | 16.6 | 2026-11-18T06:40:01.366125+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019627 | 59.469 | 63.293 | +5.13% | -0.12% | 0.68x | 7.1 | 2026-11-18T06:40:01.366125+00:00 | Not calibrated | WEAK 35/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | PEARL/USD | 1.8489 | 55.242 | 48.229 | +2.12% | -0.01% | 1.70x | 2.7 | 2026-11-18T06:40:01.366125+00:00 | Not calibrated | MODERATE 48/100 | HIGH 66/100 | Watch | WATCH |
| 4 | CC/USD | 0.08429 | 48.057 | 51.157 | +2.63% | -0.04% | 0.71x | 5.9 | 2026-11-18T06:40:01.366125+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 5 | MNT/USD | 0.3783 | 36.857 | 32.966 | +1.34% | -0.05% | 1.42x | 18.5 | 2026-11-18T06:40:01.366125+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5165 | 33.644 | 37.481 | +1.41% | +0.64% | 0.29x | 9.7 | 2026-11-18T06:40:01.366125+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | AKE/USD | 0.01009415 | 30.978 | 25.017 | +1.10% | -1.81% | 3.91x | 34.2 | 2026-11-18T06:40:01.366125+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 70.074 | 0.3003 | +0.98% | 0.42x |
| 2 | SENT/USD | 63.293 | 0.019627 | -0.12% | 0.68x |
| 3 | CC/USD | 51.157 | 0.08429 | -0.04% | 0.71x |
| 4 | PEARL/USD | 48.229 | 1.8489 | -0.01% | 1.70x |
| 5 | AKT/USD | 37.481 | 0.5165 | +0.64% | 0.29x |
| 6 | MNT/USD | 32.966 | 0.3783 | -0.05% | 1.42x |
| 7 | AKE/USD | 25.017 | 0.01009415 | -1.81% | 3.91x |

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

- Persisted scans: 557; predictions: 4698; observations: 336220.
- Matured sampled outcomes across 1/6/24/48h: 4012; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44252957219 · **Generation:** 557 · **Legacy run:** 44252957219
**Main quote time:** 2026-11-18T06:40:06.528415+00:00 · **Legacy report time:** 2026-11-18T06:40:28.663652+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.3003 | 69.19 | +0.98% | 0.42x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 2 | SENT/USD | 0.019627 | 59.47 | -0.12% | 0.68x | WEAK 35/100 | EXTREME 88/100 | Do nothing |
| 3 | PEARL/USD | 1.8489 | 55.24 | -0.01% | 1.70x | MODERATE 48/100 | HIGH 66/100 | Watch |
| 4 | CC/USD | 0.08429 | 48.06 | -0.04% | 0.71x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |
| 5 | MNT/USD | 0.3783 | 36.86 | -0.05% | 1.42x | WEAK 33/100 | VERY_HIGH 72/100 | Do nothing |
| 6 | AKT/USD | 0.5165 | 33.64 | +0.64% | 0.29x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 7 | AKE/USD | 0.01009415 | 30.98 | -1.81% | 3.91x | WEAK 35/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD | 0.308575 | 52.29 | +0.17% | 2.49x | 4089 | STRONG 71/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
