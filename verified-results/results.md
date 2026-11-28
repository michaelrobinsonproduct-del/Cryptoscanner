# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T12:42:41.303218+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46145757457
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 66326680666c6239652a9902c2143efab459f72c (atomic ledger/results publication)
**Ledger generation:** 2155 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05451 | 99.107 | 97.329 | +8.50% | +0.33% | 1.01x | 3.7 | 2026-11-28T12:42:37.508008+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XMR/USD | 437.67 | 89.524 | 89.258 | +7.46% | +0.09% | 0.98x | 21.5 | 2026-11-28T12:42:37.508008+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | VVV/USD | 26.885 | 71.247 | 69.452 | +4.41% | -0.70% | 1.53x | 10.1 | 2026-11-28T12:42:37.508008+00:00 | Not calibrated | MODERATE 51/100 | HIGH 67/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004456 | 62.630 | 70.941 | +6.65% | -0.34% | 0.34x | 11.2 | 2026-11-28T12:42:37.508008+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | AKE/USD | 0.00112431 | 45.352 | 48.055 | +3.48% | +0.09% | 0.69x | 24.8 | 2026-11-28T12:42:37.508008+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | SENT/USD | 0.024469 | 39.215 | 51.086 | +3.18% | -1.07% | 0.35x | 5.3 | 2026-11-28T12:42:37.508008+00:00 | Not calibrated | WEAK 25/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 97.329 | 0.05451 | +0.33% | 1.01x |
| 2 | XMR/USD | 89.258 | 437.67 | +0.09% | 0.98x |
| 3 | SPACE/USD | 70.941 | 0.004456 | -0.34% | 0.34x |
| 4 | VVV/USD | 69.452 | 26.885 | -0.70% | 1.53x |
| 5 | SENT/USD | 51.086 | 0.024469 | -1.07% | 0.35x |
| 6 | AKE/USD | 48.055 | 0.00112431 | +0.09% | 0.69x |

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

- Persisted scans: 2155; predictions: 19207; observations: 1304976.
- Matured sampled outcomes across 1/6/24/48h: 45891; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46145757457 · **Generation:** 2155 · **Legacy run:** 46145757457
**Main quote time:** 2026-11-28T12:42:41.303218+00:00 · **Legacy report time:** 2026-11-28T12:43:22.376507+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05451 | 99.11 | +0.33% | 1.01x | STRONG 95/100 | HIGH 62/100 | Watch |
| 2 | XMR/USD | 437.67 | 89.52 | +0.09% | 0.98x | MODERATE 55/100 | VERY_HIGH 74/100 | Watch |
| 3 | VVV/USD | 26.885 | 71.25 | -0.70% | 1.53x | MODERATE 51/100 | HIGH 67/100 | Watch |
| 4 | SPACE/USD | 0.004456 | 62.63 | -0.34% | 0.34x | WEAK 31/100 | EXTREME 94/100 | Do nothing |
| 5 | AKE/USD | 0.00112431 | 45.35 | +0.09% | 0.69x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 6 | SENT/USD | 0.024469 | 39.21 | -1.07% | 0.35x | WEAK 25/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05447 | 85.62 | +0.33% | 1.01x | 19563 | STRONG 83/100 | HIGH 68/100 | Watch |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
