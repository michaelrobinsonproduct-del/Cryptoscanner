# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T16:32:34.961185+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45437736991
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5f517c87cf62644d1daeef3589ec192ce5d8dfb9 (atomic ledger/results publication)
**Ledger generation:** 1598 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 495.44 | 79.776 | 63.925 | +1.94% | +0.85% | 2.16x | 9.3 | 2026-11-24T16:32:31.829524+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | GBP/USD | 1.31108 | 67.173 | 58.862 | +0.60% | +0.02% | 1.82x | 0.7 | 2026-11-24T16:32:31.829524+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 3 | VVV/USD | 24.705 | 57.577 | 57.492 | +1.05% | +0.38% | 0.82x | 9.7 | 2026-11-24T16:32:31.829524+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.3225 | 49.047 | 55.634 | +4.34% | +0.47% | 0.11x | 15.5 | 2026-11-24T16:32:31.829524+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | 2Z/USD | 0.01598 | 39.036 | 42.374 | +2.11% | +0.25% | 0.54x | 6.3 | 2026-11-24T16:32:31.829524+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 63.925 | 495.44 | +0.85% | 2.16x |
| 2 | GBP/USD | 58.862 | 1.31108 | +0.02% | 1.82x |
| 3 | VVV/USD | 57.492 | 24.705 | +0.38% | 0.82x |
| 4 | ICNT/USD | 55.634 | 0.3225 | +0.47% | 0.11x |
| 5 | 2Z/USD | 42.374 | 0.01598 | +0.25% | 0.54x |

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

- Persisted scans: 1598; predictions: 13743; observations: 968274.
- Matured sampled outcomes across 1/6/24/48h: 27418; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45437736991 · **Generation:** 1598 · **Legacy run:** 45437736991
**Main quote time:** 2026-11-24T16:32:34.961185+00:00 · **Legacy report time:** 2026-11-24T16:33:27.585718+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 495.44 | 79.78 | +0.85% | 2.16x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | GBP/USD | 1.31108 | 67.17 | +0.02% | 1.82x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD | 24.705 | 57.58 | +0.38% | 0.82x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 4 | ICNT/USD | 0.3225 | 49.05 | +0.47% | 0.11x | MODERATE 50/100 | VERY_HIGH 81/100 | Watch |
| 5 | 2Z/USD | 0.01598 | 39.04 | +0.25% | 0.54x | MODERATE 50/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 495.68 | 68.04 | +0.85% | 2.16x | 9556 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | AUD/USD | 0.66533 | 44.79 | +0.79% | 10.86x | 4071 | MODERATE 62/100 | VERY_HIGH 77/100 | Watch |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
