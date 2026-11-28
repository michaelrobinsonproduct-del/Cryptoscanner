# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T10:27:29.976881+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46135045791
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 26b80ba315a5eab354492b76632d13b1049cf0e3 (atomic ledger/results publication)
**Ledger generation:** 2141 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 435.12 | 97.921 | 94.254 | +6.84% | +0.98% | 0.88x | 11.5 | 2026-11-28T10:27:27.048088+00:00 | Not calibrated | STRONG 74/100 | HIGH 68/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.004516 | 81.858 | 75.525 | +8.09% | -0.07% | 1.67x | 2.2 | 2026-11-28T10:27:27.048088+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05277 | 79.034 | 84.568 | +5.04% | +0.44% | 0.23x | 11.4 | 2026-11-28T10:27:27.048088+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | VVV/USD | 26.59 | 68.821 | 63.469 | +3.27% | +0.14% | 1.46x | 7.1 | 2026-11-28T10:27:27.048088+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SENT/USD | 0.024399 | 57.158 | 50.337 | +2.89% | +1.87% | 0.75x | 2.5 | 2026-11-28T10:27:27.048088+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | CC/USD | 0.07486 | 31.373 | 37.413 | +0.96% | +0.21% | 0.29x | 6.7 | 2026-11-28T10:27:27.048088+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | TON/USD | 0.982 | 22.670 | 29.890 | +0.31% | +0.20% | 0.18x | 10.2 | 2026-11-28T10:27:27.048088+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 94.254 | 435.12 | +0.98% | 0.88x |
| 2 | NIGHT/USD | 84.568 | 0.05277 | +0.44% | 0.23x |
| 3 | SPACE/USD | 75.525 | 0.004516 | -0.07% | 1.67x |
| 4 | VVV/USD | 63.469 | 26.59 | +0.14% | 1.46x |
| 5 | SENT/USD | 50.337 | 0.024399 | +1.87% | 0.75x |
| 6 | CC/USD | 37.413 | 0.07486 | +0.21% | 0.29x |
| 7 | TON/USD | 29.890 | 0.982 | +0.20% | 0.18x |

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

- Persisted scans: 2141; predictions: 19117; observations: 1296492.
- Matured sampled outcomes across 1/6/24/48h: 45381; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46135045791 · **Generation:** 2141 · **Legacy run:** 46135045791
**Main quote time:** 2026-11-28T10:27:29.976881+00:00 · **Legacy report time:** 2026-11-28T10:28:05.900310+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 435.12 | 97.92 | +0.98% | 0.88x | STRONG 74/100 | HIGH 68/100 | Watch |
| 2 | SPACE/USD | 0.004516 | 81.86 | -0.07% | 1.67x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 3 | NIGHT/USD | 0.05277 | 79.03 | +0.44% | 0.23x | MODERATE 65/100 | VERY_HIGH 76/100 | Watch |
| 4 | VVV/USD ⭐ | 26.59 | 68.82 | +0.14% | 1.46x | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | SENT/USD | 0.024399 | 57.16 | +1.87% | 0.75x | MODERATE 59/100 | VERY_HIGH 82/100 | Watch |
| 6 | CC/USD | 0.07486 | 31.37 | +0.21% | 0.29x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |
| 7 | TON/USD | 0.982 | 22.67 | +0.20% | 0.18x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.59 | 73.46 | +0.14% | 1.46x | 7601 | STRONG 82/100 | HIGH 55/100 | Watch |
| 2 | SEI/USD | 0.03847 | 30.96 | +1.00% | 1.69x | 3399 | MODERATE 55/100 | HIGH 66/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
