# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T18:40:11.856566+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44372103531
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 6f8c0d36b6ef04eb0fcb0d82bac9aea075ac189d (atomic ledger/results publication)
**Ledger generation:** 638 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019968 | 64.585 | 72.352 | +6.96% | -0.41% | 0.43x | 7.5 | 2026-11-18T18:40:06.858090+00:00 | Not calibrated | WEAK 37/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | STABLE/USD | 0.02326 | 61.782 | 69.531 | +10.50% | -0.30% | 0.38x | 12.9 | 2026-11-18T18:40:06.858090+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.04516 | 51.228 | 48.842 | +0.60% | -0.29% | 1.38x | 6.6 | 2026-11-18T18:40:06.858090+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.0536 | 48.890 | 48.363 | +3.80% | +0.30% | 0.90x | 18.7 | 2026-11-18T18:40:06.858090+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 5 | MNT/USD | 0.3851 | 42.636 | 50.105 | +3.16% | +0.10% | 0.20x | 7.8 | 2026-11-18T18:40:06.858090+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | CC/USD | 0.08238 | 28.931 | 34.276 | +0.30% | -0.01% | 0.47x | 6.1 | 2026-11-18T18:40:06.858090+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | SPACE/USD | 0.003356 | 22.048 | 27.522 | +0.39% | +0.60% | 0.15x | 11.9 | 2026-11-18T18:40:06.858090+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.352 | 0.019968 | -0.41% | 0.43x |
| 2 | STABLE/USD | 69.531 | 0.02326 | -0.30% | 0.38x |
| 3 | MNT/USD | 50.105 | 0.3851 | +0.10% | 0.20x |
| 4 | NIGHT/USD | 48.842 | 0.04516 | -0.29% | 1.38x |
| 5 | MEGA/USD | 48.363 | 0.0536 | +0.30% | 0.90x |
| 6 | CC/USD | 34.276 | 0.08238 | -0.01% | 0.47x |
| 7 | SPACE/USD | 27.522 | 0.003356 | +0.60% | 0.15x |

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

- Persisted scans: 638; predictions: 5416; observations: 385549.
- Matured sampled outcomes across 1/6/24/48h: 4718; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44372103531 · **Generation:** 638 · **Legacy run:** 44372103531
**Main quote time:** 2026-11-18T18:40:11.856566+00:00 · **Legacy report time:** 2026-11-18T18:40:39.389149+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019968 | 64.59 | -0.41% | 0.43x | WEAK 37/100 | EXTREME 88/100 | Do nothing |
| 2 | STABLE/USD | 0.02326 | 61.78 | -0.30% | 0.38x | WEAK 31/100 | EXTREME 94/100 | Do nothing |
| 3 | NIGHT/USD | 0.04516 | 51.23 | -0.29% | 1.38x | MODERATE 46/100 | HIGH 61/100 | Watch |
| 4 | MEGA/USD | 0.0536 | 48.89 | +0.30% | 0.90x | MODERATE 49/100 | VERY_HIGH 80/100 | Watch |
| 5 | MNT/USD | 0.3851 | 42.64 | +0.10% | 0.20x | WEAK 41/100 | VERY_HIGH 75/100 | Watch |
| 6 | CC/USD | 0.08238 | 28.93 | -0.01% | 0.47x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | SPACE/USD | 0.003356 | 22.05 | +0.60% | 0.15x | WEAK 36/100 | EXTREME 88/100 | Do nothing |

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
