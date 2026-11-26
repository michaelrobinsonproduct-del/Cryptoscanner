# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T11:31:19.339080+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45811039593
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c0dc38e0f28354795b4600fb3481149857b0171b (atomic ledger/results publication)
**Ledger generation:** 1855 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 586; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SEI/USD | 0.03652 | 88.418 | 73.505 | +9.64% | +1.08% | 1.95x | 8.2 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | STRONG 89/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | FET/USD | 0.1152 | 85.999 | 68.044 | +6.18% | +0.96% | 2.31x | 17.4 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | STRONG 93/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | SKY/USD | 0.04462 | 80.552 | 75.460 | +6.54% | +0.32% | 1.35x | 6.7 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 4 | ADA/USD | 0.148039 | 79.117 | 64.646 | +1.56% | -0.11% | 3.80x | 2.5 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.07189 | 69.979 | 71.746 | +8.48% | +0.32% | 0.66x | 11.1 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | LTC/USD | 43.44 | 68.281 | 65.814 | +1.71% | -0.09% | 1.29x | 2.3 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 7 | INJ/USD | 6.198 | 66.588 | 70.683 | +4.10% | +0.37% | 0.40x | 3.2 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95146 | 66.255 | 66.084 | +1.59% | +0.11% | 0.96x | 0.1 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LINK/USD | 9.21551 | 66.067 | 67.773 | +1.89% | +0.03% | 0.81x | 0.9 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.0597 | 64.763 | 55.615 | +0.32% | +0.80% | 1.51x | 3.3 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 11 | QNT/USD | 148.5 | 59.079 | 65.206 | +2.56% | +0.29% | 0.24x | 5.4 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ETH/USD | 1697.04 | 58.716 | 57.716 | +0.39% | +0.15% | 1.02x | 0.1 | 2026-11-26T11:31:12.715844+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.460 | 0.04462 | +0.32% | 1.35x |
| 2 | SEI/USD | 73.505 | 0.03652 | +1.08% | 1.95x |
| 3 | SYRUP/USD | 71.746 | 0.07189 | +0.32% | 0.66x |
| 4 | INJ/USD | 70.683 | 6.198 | +0.37% | 0.40x |
| 5 | FET/USD | 68.044 | 0.1152 | +0.96% | 2.31x |
| 6 | LINK/USD | 67.773 | 9.21551 | +0.03% | 0.81x |
| 7 | XRP/USD | 66.084 | 0.95146 | +0.11% | 0.96x |
| 8 | LTC/USD | 65.814 | 43.44 | -0.09% | 1.29x |
| 9 | QNT/USD | 65.206 | 148.5 | +0.29% | 0.24x |
| 10 | ADA/USD | 64.646 | 0.148039 | -0.11% | 3.80x |
| 11 | ETH/USD | 57.716 | 1697.04 | +0.15% | 1.02x |
| 12 | NEAR/USD | 55.615 | 3.0597 | +0.80% | 1.51x |

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

- Persisted scans: 1855; predictions: 15995; observations: 1124422.
- Matured sampled outcomes across 1/6/24/48h: 34622; gap abstentions: 24654. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45811039593 · **Generation:** 1855 · **Legacy run:** 45811039593
**Main quote time:** 2026-11-26T11:31:19.339080+00:00 · **Legacy report time:** 2026-11-26T11:32:29.697380+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD ⭐ | 0.03652 | 88.42 | +1.08% | 1.95x | STRONG 99/100 | HIGH 60/100 | Consider small entry |
| 2 | FET/USD ⭐ | 0.1152 | 86.00 | +0.96% | 2.31x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | SKY/USD ⭐ | 0.04462 | 80.55 | +0.32% | 1.35x | STRONG 95/100 | HIGH 60/100 | Watch |
| 4 | ADA/USD | 0.148039 | 79.12 | -0.11% | 3.80x | STRONG 70/100 | HIGH 61/100 | Watch |
| 5 | SYRUP/USD | 0.07189 | 69.98 | +0.32% | 0.66x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 6 | LTC/USD | 43.44 | 68.28 | -0.09% | 1.29x | WEAK 44/100 | HIGH 61/100 | Watch |
| 7 | INJ/USD | 6.198 | 66.59 | +0.37% | 0.40x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.95146 | 66.26 | +0.11% | 0.96x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 9 | LINK/USD | 9.21551 | 66.07 | +0.03% | 0.81x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 10 | NEAR/USD | 3.0597 | 64.76 | +0.80% | 1.51x | STRONG 77/100 | HIGH 55/100 | Watch |
| 11 | QNT/USD | 148.5 | 59.08 | +0.29% | 0.24x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 12 | ETH/USD | 1697.04 | 58.72 | +0.15% | 1.02x | MODERATE 54/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD ⭐ | 0.03664 | 78.61 | +1.08% | 1.95x | 2687 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 2 | FET/USD ⭐ | 0.1152 | 77.45 | +0.96% | 2.31x | 2304 | STRONG 99/100 | HIGH 66/100 | Consider small entry |
| 3 | SKY/USD ⭐ | 0.04462 | 74.65 | +0.32% | 1.35x | 4233 | STRONG 92/100 | HIGH 60/100 | Watch |

**Same-run overlap:** SEI/USD, FET/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
