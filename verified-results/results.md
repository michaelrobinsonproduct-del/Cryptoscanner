# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T15:12:57.775234+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46158370810
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3d076b0686d5d1b0999a20ee7a4f58a83d323bf3 (atomic ledger/results publication)
**Ledger generation:** 2170 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 429.96 | 98.949 | 90.621 | +5.57% | +0.07% | 1.80x | 6.8 | 2026-11-28T15:12:54.282554+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05315 | 95.891 | 90.549 | +5.79% | -0.11% | 1.59x | 9.4 | 2026-11-28T15:12:54.282554+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 26.549 | 64.364 | 60.171 | +3.11% | -0.88% | 1.86x | 7.5 | 2026-11-28T15:12:54.282554+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.815e-05 | 60.255 | 55.799 | +5.62% | +0.65% | 1.12x | 29.2 | 2026-11-28T15:12:54.282554+00:00 | Not calibrated | MODERATE 55/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | CSPR/USD | 0.0017522 | 42.563 | 22.718 | +0.68% | +0.97% | 2.63x | 25.7 | 2026-11-28T15:12:54.282554+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | SENT/USD | 0.024209 | 33.718 | 39.498 | +2.09% | -0.07% | 0.46x | 13.2 | 2026-11-28T15:12:54.282554+00:00 | Not calibrated | WEAK 17/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 90.621 | 429.96 | +0.07% | 1.80x |
| 2 | NIGHT/USD | 90.549 | 0.05315 | -0.11% | 1.59x |
| 3 | VVV/USD | 60.171 | 26.549 | -0.88% | 1.86x |
| 4 | LUNA/USD | 55.799 | 4.815e-05 | +0.65% | 1.12x |
| 5 | SENT/USD | 39.498 | 0.024209 | -0.07% | 0.46x |
| 6 | CSPR/USD | 22.718 | 0.0017522 | +0.97% | 2.63x |

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

- Persisted scans: 2170; predictions: 19282; observations: 1314066.
- Matured sampled outcomes across 1/6/24/48h: 46443; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46158370810 · **Generation:** 2170 · **Legacy run:** 46158370810
**Main quote time:** 2026-11-28T15:12:57.775234+00:00 · **Legacy report time:** 2026-11-28T15:13:55.667016+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 429.96 | 98.95 | +0.07% | 1.80x | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD | 0.05315 | 95.89 | -0.11% | 1.59x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD | 26.549 | 64.36 | -0.88% | 1.86x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 4 | LUNA/USD ⭐ | 4.815e-05 | 60.26 | +0.65% | 1.12x | MODERATE 65/100 | EXTREME 86/100 | Do nothing |
| 5 | CSPR/USD ⭐ | 0.0017522 | 42.56 | +0.97% | 2.63x | STRONG 76/100 | VERY_HIGH 79/100 | Watch |
| 6 | SENT/USD | 0.024209 | 33.72 | -0.07% | 0.46x | WEAK 17/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 429.9 | 88.49 | +0.07% | 1.80x | 16303 | STRONG 89/100 | HIGH 55/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.815e-05 | 61.21 | +0.65% | 1.12x | 1216 | MODERATE 66/100 | EXTREME 86/100 | Do nothing |
| 3 | CSPR/USD ⭐ | 0.0017522 | 40.11 | +0.97% | 2.63x | 3355 | STRONG 80/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** XMR/USD, LUNA/USD, CSPR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
