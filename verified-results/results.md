# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:05:16.332280+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44248664918
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** adb546be06889ea5004970c28e4d5bb40302812f (atomic ledger/results publication)
**Ledger generation:** 550 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019782 | 74.987 | 55.810 | +5.96% | +0.84% | 3.59x | 33.9 | 2026-11-18T06:05:09.194699+00:00 | Not calibrated | STRONG 82/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | VVV/USD | 21.3 | 63.953 | 53.339 | +1.30% | +0.59% | 1.77x | 8.5 | 2026-11-18T06:05:09.194699+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 3 | CC/USD | 0.08472 | 54.900 | 53.584 | +3.15% | +0.24% | 1.01x | 8.2 | 2026-11-18T06:05:09.194699+00:00 | Not calibrated | MODERATE 62/100 | HIGH 67/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.2843 | 45.811 | 43.275 | +2.97% | +0.18% | 1.17x | 21.2 | 2026-11-18T06:05:09.194699+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | CT/USD | 0.1154 | 42.999 | 41.496 | +2.12% | -0.17% | 1.24x | 8.7 | 2026-11-18T06:05:09.194699+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 6 | PEARL/USD | 1.8439 | 39.450 | 43.848 | +1.84% | -0.16% | 0.64x | 7.6 | 2026-11-18T06:05:09.194699+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.515 | 37.714 | 34.421 | +1.12% | -0.35% | 1.50x | 11.7 | 2026-11-18T06:05:09.194699+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 8 | MNT/USD | 0.3782 | 33.118 | 36.768 | +1.31% | +0.27% | 0.50x | 10.6 | 2026-11-18T06:05:09.194699+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 55.810 | 0.019782 | +0.84% | 3.59x |
| 2 | CC/USD | 53.584 | 0.08472 | +0.24% | 1.01x |
| 3 | VVV/USD | 53.339 | 21.3 | +0.59% | 1.77x |
| 4 | PEARL/USD | 43.848 | 1.8439 | -0.16% | 0.64x |
| 5 | ICNT/USD | 43.275 | 0.2843 | +0.18% | 1.17x |
| 6 | CT/USD | 41.496 | 0.1154 | -0.17% | 1.24x |
| 7 | MNT/USD | 36.768 | 0.3782 | +0.27% | 0.50x |
| 8 | AKT/USD | 34.421 | 0.515 | -0.35% | 1.50x |

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

- Persisted scans: 550; predictions: 4642; observations: 331957.
- Matured sampled outcomes across 1/6/24/48h: 3871; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44248664918 · **Generation:** 550 · **Legacy run:** 44248664918
**Main quote time:** 2026-11-18T06:05:16.332280+00:00 · **Legacy report time:** 2026-11-18T06:05:38.195004+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019782 | 74.99 | +0.84% | 3.59x | STRONG 92/100 | VERY_HIGH 79/100 | Watch |
| 2 | VVV/USD ⭐ | 21.3 | 63.95 | +0.59% | 1.77x | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 3 | CC/USD ⭐ | 0.08472 | 54.90 | +0.24% | 1.01x | STRONG 72/100 | HIGH 67/100 | Watch |
| 4 | ICNT/USD ⭐ | 0.2843 | 45.81 | +0.18% | 1.17x | MODERATE 48/100 | VERY_HIGH 79/100 | Watch |
| 5 | CT/USD | 0.1154 | 43.00 | -0.17% | 1.24x | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing |
| 6 | PEARL/USD | 1.8439 | 39.45 | -0.16% | 0.64x | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | AKT/USD | 0.515 | 37.71 | -0.35% | 1.50x | WEAK 34/100 | VERY_HIGH 72/100 | Do nothing |
| 8 | MNT/USD | 0.3782 | 33.12 | +0.27% | 0.50x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019793 | 81.14 | +0.84% | 3.59x | 4567 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | CC/USD ⭐ | 0.08467 | 63.26 | +0.24% | 1.01x | 4344 | STRONG 77/100 | HIGH 67/100 | Watch |
| 3 | VVV/USD ⭐ | 21.3 | 57.25 | +0.59% | 1.77x | 7308 | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD | 3.3977 | 55.35 | +0.40% | 2.12x | 16091 | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | ICNT/USD ⭐ | 0.2808 | 45.44 | +0.18% | 1.17x | 4616 | MODERATE 48/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** SENT/USD, VVV/USD, CC/USD, ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
