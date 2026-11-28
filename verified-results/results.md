# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T15:02:51.048456+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46157467521
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cd49c5e25d91999923b20a375137dd1df360cb29 (atomic ledger/results publication)
**Ledger generation:** 2169 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.0534 | 95.145 | 93.204 | +6.29% | -0.74% | 1.57x | 11.2 | 2026-11-28T15:02:47.500872+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 2 | XMR/USD | 429.3 | 92.658 | 90.883 | +5.41% | -0.07% | 1.21x | 4.0 | 2026-11-28T15:02:47.500872+00:00 | Not calibrated | MODERATE 56/100 | HIGH 68/100 | Watch | WATCH |
| 3 | VVV/USD | 26.651 | 65.463 | 62.977 | +3.50% | -0.60% | 1.55x | 7.9 | 2026-11-28T15:02:47.500872+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 4 | MNT/USD | 0.3918 | 61.060 | 70.546 | +6.41% | -0.64% | 0.37x | 10.3 | 2026-11-28T15:02:47.500872+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.024312 | 42.222 | 45.442 | +2.52% | -0.07% | 0.71x | 7.4 | 2026-11-28T15:02:47.500872+00:00 | Not calibrated | WEAK 26/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | CSPR/USD | 0.0017656 | 33.201 | 25.345 | +1.45% | +1.73% | 0.92x | 31.2 | 2026-11-28T15:02:47.500872+00:00 | Not calibrated | WEAK 37/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 93.204 | 0.0534 | -0.74% | 1.57x |
| 2 | XMR/USD | 90.883 | 429.3 | -0.07% | 1.21x |
| 3 | MNT/USD | 70.546 | 0.3918 | -0.64% | 0.37x |
| 4 | VVV/USD | 62.977 | 26.651 | -0.60% | 1.55x |
| 5 | SENT/USD | 45.442 | 0.024312 | -0.07% | 0.71x |
| 6 | CSPR/USD | 25.345 | 0.0017656 | +1.73% | 0.92x |

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

- Persisted scans: 2169; predictions: 19276; observations: 1313460.
- Matured sampled outcomes across 1/6/24/48h: 46409; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46157467521 · **Generation:** 2169 · **Legacy run:** 46157467521
**Main quote time:** 2026-11-28T15:02:51.048456+00:00 · **Legacy report time:** 2026-11-28T15:03:37.789898+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.0534 | 95.14 | -0.74% | 1.57x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 2 | XMR/USD | 429.3 | 92.66 | -0.07% | 1.21x | MODERATE 56/100 | HIGH 68/100 | Watch |
| 3 | VVV/USD | 26.651 | 65.46 | -0.60% | 1.55x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 4 | MNT/USD | 0.3918 | 61.06 | -0.64% | 0.37x | WEAK 31/100 | EXTREME 94/100 | Do nothing |
| 5 | SENT/USD | 0.024312 | 42.22 | -0.07% | 0.71x | WEAK 26/100 | EXTREME 88/100 | Do nothing |
| 6 | CSPR/USD | 0.0017656 | 33.20 | +1.73% | 0.92x | WEAK 37/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.786e-05 | 65.91 | +0.42% | 2.44x | 1230 | STRONG 73/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
