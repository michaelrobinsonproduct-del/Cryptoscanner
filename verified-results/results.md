# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T15:31:08.340524+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44763792366
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 1818f5622a294e69bc55906b0e59adbc59c2f8a3 (atomic ledger/results publication)
**Ledger generation:** 997 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BLUR/USD | 0.00712 | 67.647 | 62.328 | +6.43% | -0.97% | 2.02x | 28.1 | 2026-11-20T15:31:03.530028+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 85/100 | Do nothing | WATCH |
| 2 | TAC/USD | 0.001305 | 43.079 | 47.651 | +4.57% | -3.91% | 16.95x | 30.8 | 2026-11-20T15:31:03.530028+00:00 | Not calibrated | WEAK 42/100 | EXTREME 89/100 | Do nothing | WATCH |
| 3 | MON/USD | 0.0138 | 42.184 | 28.985 | +0.29% | -0.29% | 2.46x | 14.5 | 2026-11-20T15:31:03.530028+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.4274 | 39.522 | 23.803 | +0.31% | +0.14% | 3.37x | 30.5 | 2026-11-20T15:31:03.530028+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLUR/USD | 62.328 | 0.00712 | -0.97% | 2.02x |
| 2 | TAC/USD | 47.651 | 0.001305 | -3.91% | 16.95x |
| 3 | MON/USD | 28.985 | 0.0138 | -0.29% | 2.46x |
| 4 | ICNT/USD | 23.803 | 0.4274 | +0.14% | 3.37x |

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

- Persisted scans: 997; predictions: 8276; observations: 602536.
- Matured sampled outcomes across 1/6/24/48h: 10334; gap abstentions: 17743. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44763792366 · **Generation:** 997 · **Legacy run:** 44763792366
**Main quote time:** 2026-11-20T15:31:08.340524+00:00 · **Legacy report time:** 2026-11-20T15:32:04.460707+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BLUR/USD | 0.00712 | 67.65 | -0.97% | 2.02x | MODERATE 54/100 | EXTREME 85/100 | Do nothing |
| 2 | TAC/USD | 0.001305 | 43.08 | -3.91% | 16.95x | WEAK 42/100 | EXTREME 89/100 | Do nothing |
| 3 | MON/USD | 0.0138 | 42.18 | -0.29% | 2.46x | MODERATE 46/100 | VERY_HIGH 72/100 | Watch |
| 4 | ICNT/USD | 0.4274 | 39.52 | +0.14% | 3.37x | MODERATE 55/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
