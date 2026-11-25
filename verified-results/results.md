# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T04:07:26.585255+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45544269263
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0684e725fb5dd7d1ca894b63da88ac9942d06647 (atomic ledger/results publication)
**Ledger generation:** 1667 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.0098 | 72.595 | 67.517 | +3.48% | -0.31% | 1.66x | 10.2 | 2026-11-25T04:07:22.646829+00:00 | Not calibrated | MODERATE 51/100 | HIGH 67/100 | Watch | WATCH |
| 2 | DRV/USD | 0.32819 | 66.472 | 58.282 | +4.43% | -1.36% | 3.55x | 16.2 | 2026-11-25T04:07:22.646829+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | SKY/USD | 0.04169 | 57.686 | 41.240 | +1.73% | +0.29% | 14.28x | 9.6 | 2026-11-25T04:07:22.646829+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 4 | XMR/USD | 511.58 | 53.161 | 51.247 | +0.39% | +0.15% | 1.11x | 9.4 | 2026-11-25T04:07:22.646829+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.07087 | 20.103 | 30.414 | +1.72% | -0.54% | 0.24x | 26.8 | 2026-11-25T04:07:22.646829+00:00 | Not calibrated | WEAK 5/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 67.517 | 0.0098 | -0.31% | 1.66x |
| 2 | DRV/USD | 58.282 | 0.32819 | -1.36% | 3.55x |
| 3 | XMR/USD | 51.247 | 511.58 | +0.15% | 1.11x |
| 4 | SKY/USD | 41.240 | 0.04169 | +0.29% | 14.28x |
| 5 | SYRUP/USD | 30.414 | 0.07087 | -0.54% | 0.24x |

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

- Persisted scans: 1667; predictions: 14175; observations: 1010294.
- Matured sampled outcomes across 1/6/24/48h: 29906; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45544269263 · **Generation:** 1667 · **Legacy run:** 45544269263
**Main quote time:** 2026-11-25T04:07:26.585255+00:00 · **Legacy report time:** 2026-11-25T04:08:41.001260+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.0098 | 72.59 | -0.31% | 1.66x | MODERATE 51/100 | HIGH 67/100 | Watch |
| 2 | DRV/USD | 0.32819 | 66.47 | -1.36% | 3.55x | MODERATE 58/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | SKY/USD ⭐ | 0.04169 | 57.69 | +0.29% | 14.28x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 4 | XMR/USD ⭐ | 511.58 | 53.16 | +0.15% | 1.11x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 5 | SYRUP/USD | 0.07087 | 20.10 | -0.54% | 0.24x | WEAK 5/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04155 | 49.90 | +0.29% | 14.28x | 4401 | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 511.52 | 41.36 | +0.15% | 1.11x | 6922 | MODERATE 51/100 | HIGH 68/100 | Watch |

**Same-run overlap:** SKY/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
