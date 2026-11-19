# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T00:25:15.674976+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44428758547
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 087178530dc60972870727497d7a7d1b3c8fb0c3 (atomic ledger/results publication)
**Ledger generation:** 706 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020815 | 43.273 | 35.090 | +1.02% | +0.91% | 1.36x | 6.7 | 2026-11-19T00:25:11.355158+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 2 | UAI/USD | 0.03325 | 42.791 | 26.283 | +0.42% | +0.30% | 2.63x | 15.0 | 2026-11-19T00:25:11.355158+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | W/USD | 0.00894 | 40.600 | 27.844 | +0.34% | +0.11% | 2.22x | 11.2 | 2026-11-19T00:25:11.355158+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05642 | 22.520 | 24.922 | +0.75% | +0.70% | 0.41x | 23.0 | 2026-11-19T00:25:11.355158+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 35.090 | 0.020815 | +0.91% | 1.36x |
| 2 | W/USD | 27.844 | 0.00894 | +0.11% | 2.22x |
| 3 | UAI/USD | 26.283 | 0.03325 | +0.30% | 2.63x |
| 4 | MEGA/USD | 24.922 | 0.05642 | +0.70% | 0.41x |

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

- Persisted scans: 706; predictions: 5697; observations: 426961.
- Matured sampled outcomes across 1/6/24/48h: 5600; gap abstentions: 13374. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44428758547 · **Generation:** 706 · **Legacy run:** 44428758547
**Main quote time:** 2026-11-19T00:25:15.674976+00:00 · **Legacy report time:** 2026-11-19T00:25:43.788817+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020815 | 43.27 | +0.91% | 1.36x | STRONG 77/100 | HIGH 67/100 | Watch |
| 2 | UAI/USD ⭐ | 0.03325 | 42.79 | +0.30% | 2.63x | STRONG 81/100 | VERY_HIGH 73/100 | Watch |
| 3 | W/USD | 0.00894 | 40.60 | +0.11% | 2.22x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 4 | MEGA/USD | 0.05642 | 22.52 | +0.70% | 0.41x | WEAK 31/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020811 | 38.98 | +0.91% | 1.36x | 6916 | STRONG 74/100 | HIGH 67/100 | Watch |
| 2 | UAI/USD ⭐ | 0.03325 | 29.53 | +0.30% | 2.63x | 1983 | STRONG 75/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
