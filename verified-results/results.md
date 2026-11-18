# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:45:13.352168+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44350729526
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 36264a1e54a171e91f4717a3174a89f54a82cfbb (atomic ledger/results publication)
**Ledger generation:** 615 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019526 | 55.520 | 59.852 | +4.59% | -0.20% | 0.67x | 6.7 | 2026-11-18T16:45:09.151710+00:00 | Not calibrated | WEAK 33/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | MEGA/USD | 0.05301 | 52.785 | 41.210 | +2.65% | +0.19% | 2.06x | 17.0 | 2026-11-18T16:45:09.151710+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | TRUST/USD | 0.04928 | 45.297 | 50.678 | +4.52% | -0.54% | 0.73x | 26.5 | 2026-11-18T16:45:09.151710+00:00 | Not calibrated | WEAK 18/100 | EXTREME 93/100 | Do nothing | WATCH |
| 4 | CT/USD | 0.1151 | 27.765 | 31.027 | +1.86% | -0.78% | 1.06x | 26.1 | 2026-11-18T16:45:09.151710+00:00 | Not calibrated | WEAK 14/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 59.852 | 0.019526 | -0.20% | 0.67x |
| 2 | TRUST/USD | 50.678 | 0.04928 | -0.54% | 0.73x |
| 3 | MEGA/USD | 41.210 | 0.05301 | +0.19% | 2.06x |
| 4 | CT/USD | 31.027 | 0.1151 | -0.78% | 1.06x |

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

- Persisted scans: 615; predictions: 5270; observations: 371542.
- Matured sampled outcomes across 1/6/24/48h: 4509; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44350729526 · **Generation:** 615 · **Legacy run:** 44350729526
**Main quote time:** 2026-11-18T16:45:13.352168+00:00 · **Legacy report time:** 2026-11-18T16:45:44.384391+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019526 | 55.52 | -0.20% | 0.67x | WEAK 33/100 | EXTREME 88/100 | Do nothing |
| 2 | MEGA/USD ⭐ | 0.05301 | 52.78 | +0.19% | 2.06x | STRONG 76/100 | VERY_HIGH 73/100 | Watch |
| 3 | TRUST/USD | 0.04928 | 45.30 | -0.54% | 0.73x | WEAK 18/100 | EXTREME 93/100 | Do nothing |
| 4 | CT/USD | 0.1151 | 27.77 | -0.78% | 1.06x | WEAK 14/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05315 | 50.39 | +0.19% | 2.06x | 1177 | STRONG 75/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
