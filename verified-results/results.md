# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:10:11.104928+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44242254552
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** d8adcc73312666dff6590a08f9020ec4ea467a46 (atomic ledger/results publication)
**Ledger generation:** 539 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019311 | 65.645 | 51.137 | +3.44% | -0.10% | 2.55x | 7.8 | 2026-11-18T05:10:06.723534+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | PEARL/USD | 1.8332 | 49.003 | 38.007 | +1.25% | -0.80% | 6.04x | 11.5 | 2026-11-18T05:10:06.723534+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | UP/USD | 0.05503 | 45.605 | 48.180 | +3.85% | -0.70% | 1.09x | 21.9 | 2026-11-18T05:10:06.723534+00:00 | Not calibrated | WEAK 23/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | XDC/USD | 0.03077 | 44.032 | 46.581 | +1.48% | -0.26% | 0.87x | 3.3 | 2026-11-18T05:10:06.723534+00:00 | Not calibrated | WEAK 27/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | CC/USD | 0.08332 | 38.682 | 42.742 | +1.45% | +0.05% | 0.57x | 6.0 | 2026-11-18T05:10:06.723534+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | MELANIA/USD | 0.0498 | 32.129 | 26.513 | +2.26% | -0.40% | 1.76x | 40.2 | 2026-11-18T05:10:06.723534+00:00 | Not calibrated | WEAK 21/100 | EXTREME 95/100 | Do nothing | WATCH |
| 7 | MEGA/USD | 0.05181 | 29.675 | 26.832 | +0.33% | -0.63% | 1.60x | 13.5 | 2026-11-18T05:10:06.723534+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 51.137 | 0.019311 | -0.10% | 2.55x |
| 2 | UP/USD | 48.180 | 0.05503 | -0.70% | 1.09x |
| 3 | XDC/USD | 46.581 | 0.03077 | -0.26% | 0.87x |
| 4 | CC/USD | 42.742 | 0.08332 | +0.05% | 0.57x |
| 5 | PEARL/USD | 38.007 | 1.8332 | -0.80% | 6.04x |
| 6 | MEGA/USD | 26.832 | 0.05181 | -0.63% | 1.60x |
| 7 | MELANIA/USD | 26.513 | 0.0498 | -0.40% | 1.76x |

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

- Persisted scans: 539; predictions: 4553; observations: 325258.
- Matured sampled outcomes across 1/6/24/48h: 3645; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44242254552 · **Generation:** 539 · **Legacy run:** 44242254552
**Main quote time:** 2026-11-18T05:10:11.104928+00:00 · **Legacy report time:** 2026-11-18T05:10:32.403383+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019311 | 65.65 | -0.10% | 2.55x | MODERATE 63/100 | VERY_HIGH 73/100 | Watch |
| 2 | PEARL/USD | 1.8332 | 49.00 | -0.80% | 6.04x | MODERATE 50/100 | VERY_HIGH 72/100 | Watch |
| 3 | UP/USD | 0.05503 | 45.61 | -0.70% | 1.09x | WEAK 23/100 | EXTREME 85/100 | Do nothing |
| 4 | XDC/USD | 0.03077 | 44.03 | -0.26% | 0.87x | WEAK 27/100 | HIGH 68/100 | Do nothing |
| 5 | CC/USD | 0.08332 | 38.68 | +0.05% | 0.57x | WEAK 39/100 | VERY_HIGH 75/100 | Watch |
| 6 | MELANIA/USD | 0.0498 | 32.13 | -0.40% | 1.76x | WEAK 21/100 | EXTREME 95/100 | Do nothing |
| 7 | MEGA/USD | 0.05181 | 29.67 | -0.63% | 1.60x | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing |

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
