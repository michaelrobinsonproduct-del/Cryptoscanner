# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:55:13.176057+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44254820960
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 8a3587432be29996ece979f7b473318a709f11f1 (atomic ledger/results publication)
**Ledger generation:** 560 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRX/USD | 0.308896 | 55.256 | 42.117 | +0.32% | +0.10% | 2.26x | 1.2 | 2026-11-18T06:55:08.210675+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 2 | MNT/USD | 0.3778 | 51.663 | 37.324 | +1.21% | -0.13% | 5.43x | 7.9 | 2026-11-18T06:55:08.210675+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 3 | AKE/USD | 0.0103 | 45.212 | 38.701 | +3.16% | +2.04% | 0.63x | 35.9 | 2026-11-18T06:55:08.210675+00:00 | Not calibrated | WEAK 38/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | TRUST/USD | 0.04752 | 34.652 | 28.269 | +0.78% | +0.11% | 1.59x | 21.0 | 2026-11-18T06:55:08.210675+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | AKT/USD | 0.515 | 28.556 | 35.378 | +1.12% | -0.29% | 0.46x | 9.7 | 2026-11-18T06:55:08.210675+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 6 | SENT/USD | 0.019294 | 23.306 | 37.514 | +3.35% | -1.88% | 0.52x | 33.7 | 2026-11-18T06:55:08.210675+00:00 | Not calibrated | WEAK 7/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TRX/USD | 42.117 | 0.308896 | +0.10% | 2.26x |
| 2 | AKE/USD | 38.701 | 0.0103 | +2.04% | 0.63x |
| 3 | SENT/USD | 37.514 | 0.019294 | -1.88% | 0.52x |
| 4 | MNT/USD | 37.324 | 0.3778 | -0.13% | 5.43x |
| 5 | AKT/USD | 35.378 | 0.515 | -0.29% | 0.46x |
| 6 | TRUST/USD | 28.269 | 0.04752 | +0.11% | 1.59x |

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

- Persisted scans: 560; predictions: 4721; observations: 338047.
- Matured sampled outcomes across 1/6/24/48h: 4049; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44254820960 · **Generation:** 560 · **Legacy run:** 44254820960
**Main quote time:** 2026-11-18T06:55:13.176057+00:00 · **Legacy report time:** 2026-11-18T06:55:30.755380+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD ⭐ | 0.308896 | 55.26 | +0.10% | 2.26x | STRONG 83/100 | HIGH 55/100 | Watch |
| 2 | MNT/USD | 0.3778 | 51.66 | -0.13% | 5.43x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 3 | AKE/USD | 0.0103 | 45.21 | +2.04% | 0.63x | WEAK 38/100 | EXTREME 87/100 | Do nothing |
| 4 | TRUST/USD ⭐ | 0.04752 | 34.65 | +0.11% | 1.59x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 5 | AKT/USD | 0.515 | 28.56 | -0.29% | 0.46x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |
| 6 | SENT/USD | 0.019294 | 23.31 | -1.88% | 0.52x | WEAK 7/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 1.9243 | 89.47 | +4.03% | 46.99x | 4145 | STRONG 95/100 | VERY_HIGH 76/100 | Watch |
| 2 | TRX/USD ⭐ | 0.308896 | 52.32 | +0.10% | 2.26x | 4104 | STRONG 81/100 | HIGH 55/100 | Watch |
| 3 | TRUST/USD ⭐ | 0.04752 | 36.05 | +0.11% | 1.59x | 7215 | MODERATE 58/100 | HIGH 66/100 | Watch |

**Same-run overlap:** TRX/USD, TRUST/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
