# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:15:05.673854+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44249893179
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 9a6e231b8c563300058d0b0d82ca520642fedd2a (atomic ledger/results publication)
**Ledger generation:** 552 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019935 | 95.167 | 71.989 | +6.78% | +1.64% | 3.71x | 8.0 | 2026-11-18T06:14:58.210505+00:00 | Not calibrated | STRONG 100/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | CC/USD | 0.08457 | 68.243 | 54.128 | +2.97% | -0.18% | 4.58x | 4.7 | 2026-11-18T06:14:58.210505+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 3 | VVV/USD | 21.317 | 64.433 | 53.281 | +1.38% | +0.30% | 1.97x | 9.8 | 2026-11-18T06:14:58.210505+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.4166 | 55.227 | 58.613 | +0.70% | +0.59% | 0.36x | 2.6 | 2026-11-18T06:14:58.210505+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | MNT/USD | 0.3787 | 39.439 | 39.036 | +1.45% | +0.40% | 0.84x | 7.9 | 2026-11-18T06:14:58.210505+00:00 | Not calibrated | MODERATE 50/100 | HIGH 67/100 | Watch | WATCH |
| 6 | PEARL/USD | 1.8392 | 34.696 | 36.853 | +1.59% | -0.37% | 0.97x | 17.9 | 2026-11-18T06:14:58.210505+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5143 | 34.605 | 38.313 | +0.98% | -0.85% | 1.05x | 1.9 | 2026-11-18T06:14:58.210505+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 8 | CT/USD | 0.1154 | 27.227 | 37.151 | +2.12% | -0.26% | 0.14x | 17.3 | 2026-11-18T06:14:58.210505+00:00 | Not calibrated | WEAK 14/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 71.989 | 0.019935 | +1.64% | 3.71x |
| 2 | NEAR/USD | 58.613 | 3.4166 | +0.59% | 0.36x |
| 3 | CC/USD | 54.128 | 0.08457 | -0.18% | 4.58x |
| 4 | VVV/USD | 53.281 | 21.317 | +0.30% | 1.97x |
| 5 | MNT/USD | 39.036 | 0.3787 | +0.40% | 0.84x |
| 6 | AKT/USD | 38.313 | 0.5143 | -0.85% | 1.05x |
| 7 | CT/USD | 37.151 | 0.1154 | -0.26% | 0.14x |
| 8 | PEARL/USD | 36.853 | 1.8392 | -0.37% | 0.97x |

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

- Persisted scans: 552; predictions: 4660; observations: 333175.
- Matured sampled outcomes across 1/6/24/48h: 3890; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44249893179 · **Generation:** 552 · **Legacy run:** 44249893179
**Main quote time:** 2026-11-18T06:15:05.673854+00:00 · **Legacy report time:** 2026-11-18T06:15:20.867033+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019935 | 95.17 | +1.64% | 3.71x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | CC/USD | 0.08457 | 68.24 | -0.18% | 4.58x | MODERATE 64/100 | HIGH 66/100 | Watch |
| 3 | VVV/USD ⭐ | 21.317 | 64.43 | +0.30% | 1.97x | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD | 3.4166 | 55.23 | +0.59% | 0.36x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 5 | MNT/USD | 0.3787 | 39.44 | +0.40% | 0.84x | MODERATE 50/100 | HIGH 67/100 | Watch |
| 6 | PEARL/USD | 1.8392 | 34.70 | -0.37% | 0.97x | WEAK 17/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | AKT/USD | 0.5143 | 34.61 | -0.85% | 1.05x | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing |
| 8 | CT/USD | 0.1154 | 27.23 | -0.26% | 0.14x | WEAK 14/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019908 | 82.01 | +1.14% | 3.91x | 4560 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 21.317 | 54.47 | +0.30% | 1.97x | 7362 | STRONG 82/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SENT/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
