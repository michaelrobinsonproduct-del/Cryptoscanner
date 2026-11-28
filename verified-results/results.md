# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T10:37:34.705760+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46135824678
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 71756e150027887ce1f72702d99c0d8eff37c06a (atomic ledger/results publication)
**Ledger generation:** 2142 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 436 | 89.716 | 93.915 | +7.05% | -0.16% | 0.66x | 12.2 | 2026-11-28T10:37:31.253349+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05299 | 87.926 | 86.707 | +5.47% | +0.78% | 0.73x | 13.2 | 2026-11-28T10:37:31.253349+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | VVV/USD | 26.576 | 64.854 | 61.008 | +3.21% | +0.41% | 1.18x | 11.3 | 2026-11-28T10:37:31.253349+00:00 | Not calibrated | MODERATE 62/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004401 | 59.891 | 59.903 | +5.34% | -2.09% | 2.04x | 18.2 | 2026-11-28T10:37:31.253349+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.024289 | 41.505 | 47.489 | +2.42% | +0.45% | 0.18x | 1.6 | 2026-11-28T10:37:31.253349+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | CC/USD | 0.07471 | 30.851 | 37.992 | +0.76% | -0.12% | 0.35x | 2.7 | 2026-11-28T10:37:31.253349+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 93.915 | 436 | -0.16% | 0.66x |
| 2 | NIGHT/USD | 86.707 | 0.05299 | +0.78% | 0.73x |
| 3 | VVV/USD | 61.008 | 26.576 | +0.41% | 1.18x |
| 4 | SPACE/USD | 59.903 | 0.004401 | -2.09% | 2.04x |
| 5 | SENT/USD | 47.489 | 0.024289 | +0.45% | 0.18x |
| 6 | CC/USD | 37.992 | 0.07471 | -0.12% | 0.35x |

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

- Persisted scans: 2142; predictions: 19123; observations: 1297098.
- Matured sampled outcomes across 1/6/24/48h: 45420; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46135824678 · **Generation:** 2142 · **Legacy run:** 46135824678
**Main quote time:** 2026-11-28T10:37:34.705760+00:00 · **Legacy report time:** 2026-11-28T10:38:20.238203+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 436 | 89.72 | -0.16% | 0.66x | MODERATE 45/100 | VERY_HIGH 82/100 | Watch |
| 2 | NIGHT/USD | 0.05299 | 87.93 | +0.78% | 0.73x | MODERATE 69/100 | VERY_HIGH 76/100 | Watch |
| 3 | VVV/USD ⭐ | 26.576 | 64.85 | +0.41% | 1.18x | STRONG 72/100 | HIGH 68/100 | Watch |
| 4 | SPACE/USD | 0.004401 | 59.89 | -2.09% | 2.04x | MODERATE 55/100 | VERY_HIGH 83/100 | Do nothing |
| 5 | SENT/USD | 0.024289 | 41.51 | +0.45% | 0.18x | MODERATE 51/100 | VERY_HIGH 82/100 | Watch |
| 6 | CC/USD | 0.07471 | 30.85 | -0.12% | 0.35x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.576 | 71.00 | +0.41% | 1.18x | 7701 | STRONG 80/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
