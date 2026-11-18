# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T02:17:25.485315+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44222093063
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** daa96e05a6faf2b9bceb6104f9b664c4106c2639 (atomic ledger/results publication)
**Ledger generation:** 505 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.8481 | 69.013 | 41.068 | +2.08% | +2.59% | 5.15x | 17.9 | 2026-11-18T02:17:22.359295+00:00 | Not calibrated | STRONG 85/100 | HIGH 66/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5186 | 59.274 | 41.281 | +1.83% | +0.60% | 3.18x | 7.7 | 2026-11-18T02:17:22.359295+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 3 | UP/USD | 0.0552 | 54.431 | 56.145 | +4.17% | +0.64% | 0.51x | 9.1 | 2026-11-18T02:17:22.359295+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | TON/USD | 1.084 | 45.425 | 38.909 | +0.65% | +0.83% | 1.24x | 9.2 | 2026-11-18T02:17:22.359295+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 5 | SENT/USD | 0.018724 | 35.402 | 28.907 | +0.29% | +0.71% | 1.29x | 8.0 | 2026-11-18T02:17:22.359295+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 6 | CAP/USD | 0.101323 | 22.448 | 31.686 | +0.35% | -0.61% | 0.38x | 6.1 | 2026-11-18T02:17:22.359295+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 56.145 | 0.0552 | +0.64% | 0.51x |
| 2 | AKT/USD | 41.281 | 0.5186 | +0.60% | 3.18x |
| 3 | PEARL/USD | 41.068 | 1.8481 | +2.59% | 5.15x |
| 4 | TON/USD | 38.909 | 1.084 | +0.83% | 1.24x |
| 5 | CAP/USD | 31.686 | 0.101323 | -0.61% | 0.38x |
| 6 | SENT/USD | 28.907 | 0.018724 | +0.71% | 1.29x |

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

- Persisted scans: 505; predictions: 4304; observations: 304552.
- Matured sampled outcomes across 1/6/24/48h: 3463; gap abstentions: 12412. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44222093063 · **Generation:** 505 · **Legacy run:** 44222093063
**Main quote time:** 2026-11-18T02:17:25.485315+00:00 · **Legacy report time:** 2026-11-18T02:17:37.653167+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.8481 | 69.01 | +2.59% | 5.15x | STRONG 95/100 | HIGH 66/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5186 | 59.27 | +0.60% | 3.18x | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 3 | UP/USD | 0.0552 | 54.43 | +0.64% | 0.51x | MODERATE 57/100 | VERY_HIGH 82/100 | Watch |
| 4 | TON/USD ⭐ | 1.084 | 45.42 | +0.83% | 1.24x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 5 | SENT/USD ⭐ | 0.018724 | 35.40 | +0.71% | 1.29x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 6 | CAP/USD | 0.101323 | 22.45 | -0.61% | 0.38x | WEAK 16/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.8481 | 65.98 | +2.59% | 5.15x | 4362 | STRONG 93/100 | HIGH 66/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5196 | 64.78 | +0.60% | 3.18x | 3640 | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 3 | TON/USD ⭐ | 1.084 | 38.62 | +0.83% | 1.24x | 5402 | MODERATE 64/100 | HIGH 62/100 | Watch |
| 4 | SENT/USD ⭐ | 0.018724 | 29.36 | +0.71% | 1.29x | 3821 | MODERATE 60/100 | HIGH 67/100 | Watch |

**Same-run overlap:** PEARL/USD, AKT/USD, TON/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
