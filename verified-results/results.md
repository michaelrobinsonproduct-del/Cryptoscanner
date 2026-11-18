# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T02:10:04.043219+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44221178116
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** c62d74400e66fca203e70b1bfe70887c904c07e0 (atomic ledger/results publication)
**Ledger generation:** 503 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5177 | 58.601 | 41.953 | +1.65% | +0.33% | 2.66x | 3.9 | 2026-11-18T02:10:01.299955+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 2 | TON/USD | 1.09 | 55.594 | 38.290 | +1.21% | +0.46% | 11.16x | 18.3 | 2026-11-18T02:10:01.299955+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 3 | UP/USD | 0.0552 | 48.200 | 51.541 | +4.17% | +0.16% | 0.58x | 18.2 | 2026-11-18T02:10:01.299955+00:00 | Not calibrated | WEAK 39/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.018719 | 27.470 | 26.585 | +0.27% | +0.28% | 0.95x | 12.3 | 2026-11-18T02:10:01.299955+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 5 | CAP/USD | 0.10164 | 23.416 | 34.436 | +0.66% | -0.50% | 0.15x | 5.2 | 2026-11-18T02:10:01.299955+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 51.541 | 0.0552 | +0.16% | 0.58x |
| 2 | AKT/USD | 41.953 | 0.5177 | +0.33% | 2.66x |
| 3 | TON/USD | 38.290 | 1.09 | +0.46% | 11.16x |
| 4 | CAP/USD | 34.436 | 0.10164 | -0.50% | 0.15x |
| 5 | SENT/USD | 26.585 | 0.018719 | +0.28% | 0.95x |

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

- Persisted scans: 503; predictions: 4292; observations: 303334.
- Matured sampled outcomes across 1/6/24/48h: 3453; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44221178116 · **Generation:** 503 · **Legacy run:** 44221178116
**Main quote time:** 2026-11-18T02:10:04.043219+00:00 · **Legacy report time:** 2026-11-18T02:10:18.369485+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5177 | 58.60 | +0.33% | 2.66x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 2 | TON/USD ⭐ | 1.09 | 55.59 | +0.46% | 11.16x | STRONG 88/100 | HIGH 61/100 | Consider small entry |
| 3 | UP/USD | 0.0552 | 48.20 | +0.16% | 0.58x | WEAK 39/100 | EXTREME 88/100 | Do nothing |
| 4 | SENT/USD | 0.018719 | 27.47 | +0.28% | 0.95x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 5 | CAP/USD | 0.10164 | 23.42 | -0.50% | 0.15x | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5183 | 63.37 | +0.33% | 2.66x | 3597 | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 2 | PEARL/USD | 1.8427 | 62.23 | +2.54% | 4.28x | 4345 | STRONG 81/100 | HIGH 66/100 | Watch |
| 3 | TON/USD ⭐ | 1.09 | 51.28 | +0.46% | 11.16x | 5398 | STRONG 86/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** AKT/USD, TON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
