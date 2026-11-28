# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T09:47:37.094941+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46131877877
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f1d3c893a5e0f3ba5d75e9bddb40c2dbeecdecaf (atomic ledger/results publication)
**Ledger generation:** 2137 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05272 | 102.940 | 88.605 | +4.94% | -0.13% | 3.90x | 1.9 | 2026-11-28T09:47:33.121289+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 435.5 | 78.986 | 87.249 | +6.93% | -0.70% | 0.52x | 25.5 | 2026-11-28T09:47:33.121289+00:00 | Not calibrated | WEAK 34/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | SPACE/USD | 0.004528 | 67.507 | 75.525 | +8.38% | +0.35% | 0.02x | 2.2 | 2026-11-28T09:47:33.121289+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | VVV/USD | 26.558 | 63.459 | 63.485 | +3.14% | +0.48% | 0.76x | 5.6 | 2026-11-28T09:47:33.121289+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 5 | SENT/USD | 0.023928 | 55.100 | 34.869 | +0.90% | +1.05% | 4.31x | 5.4 | 2026-11-28T09:47:33.121289+00:00 | Not calibrated | STRONG 83/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 88.605 | 0.05272 | -0.13% | 3.90x |
| 2 | XMR/USD | 87.249 | 435.5 | -0.70% | 0.52x |
| 3 | SPACE/USD | 75.525 | 0.004528 | +0.35% | 0.02x |
| 4 | VVV/USD | 63.485 | 26.558 | +0.48% | 0.76x |
| 5 | SENT/USD | 34.869 | 0.023928 | +1.05% | 4.31x |

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

- Persisted scans: 2137; predictions: 19094; observations: 1294068.
- Matured sampled outcomes across 1/6/24/48h: 45224; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46131877877 · **Generation:** 2137 · **Legacy run:** 46131877877
**Main quote time:** 2026-11-28T09:47:37.094941+00:00 · **Legacy report time:** 2026-11-28T09:48:24.958786+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05272 | 102.94 | -0.13% | 3.90x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 435.5 | 78.99 | -0.70% | 0.52x | WEAK 34/100 | EXTREME 88/100 | Do nothing |
| 3 | SPACE/USD | 0.004528 | 67.51 | +0.35% | 0.02x | MODERATE 64/100 | VERY_HIGH 82/100 | Watch |
| 4 | VVV/USD | 26.558 | 63.46 | +0.48% | 0.76x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 5 | SENT/USD ⭐ | 0.023928 | 55.10 | +1.05% | 4.31x | STRONG 93/100 | HIGH 67/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.023888 | 51.01 | +1.05% | 4.31x | 5517 | STRONG 91/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
