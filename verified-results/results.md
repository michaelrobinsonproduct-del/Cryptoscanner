# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T18:44:28.499872+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46177046000
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 885fd431a5137e75e60944504e63c21c82d9066a (atomic ledger/results publication)
**Ledger generation:** 2192 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 607; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 428.8 | 92.615 | 88.157 | +5.29% | +1.29% | 0.80x | 7.7 | 2026-11-28T18:44:24.273618+00:00 | Not calibrated | STRONG 76/100 | HIGH 62/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05216 | 74.279 | 75.619 | +3.82% | +0.10% | 0.82x | 9.6 | 2026-11-28T18:44:24.273618+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 3 | TEL/USD | 0.00223 | 53.809 | 54.275 | +6.19% | +1.74% | 0.09x | 40.5 | 2026-11-28T18:44:24.273618+00:00 | Not calibrated | WEAK 42/100 | EXTREME 100/100 | Do nothing | WATCH |
| 4 | VVV/USD | 26.285 | 50.820 | 52.502 | +2.08% | +0.24% | 0.71x | 7.6 | 2026-11-28T18:44:24.273618+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SENT/USD | 0.024154 | 45.177 | 41.211 | +1.86% | -0.18% | 1.49x | 6.2 | 2026-11-28T18:44:24.273618+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 88.157 | 428.8 | +1.29% | 0.80x |
| 2 | NIGHT/USD | 75.619 | 0.05216 | +0.10% | 0.82x |
| 3 | TEL/USD | 54.275 | 0.00223 | +1.74% | 0.09x |
| 4 | VVV/USD | 52.502 | 26.285 | +0.24% | 0.71x |
| 5 | SENT/USD | 41.211 | 0.024154 | -0.18% | 1.49x |

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

- Persisted scans: 2192; predictions: 19367; observations: 1327405.
- Matured sampled outcomes across 1/6/24/48h: 47165; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 158 (sampled only; not a success-rate estimate).
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

**Writer:** 46177046000 · **Generation:** 2192 · **Legacy run:** 46177046000
**Main quote time:** 2026-11-28T18:44:28.499872+00:00 · **Legacy report time:** 2026-11-28T18:45:16.054506+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 428.8 | 92.62 | +1.29% | 0.80x | STRONG 76/100 | HIGH 62/100 | Watch |
| 2 | NIGHT/USD | 0.05216 | 74.28 | +0.10% | 0.82x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 3 | TEL/USD | 0.00223 | 53.81 | +1.74% | 0.09x | WEAK 42/100 | EXTREME 100/100 | Do nothing |
| 4 | VVV/USD | 26.285 | 50.82 | +0.24% | 0.71x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 5 | SENT/USD ⭐ | 0.024154 | 45.18 | -0.18% | 1.49x | MODERATE 53/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.02415 | 61.15 | +0.57% | 1.31x | 6430 | STRONG 86/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
