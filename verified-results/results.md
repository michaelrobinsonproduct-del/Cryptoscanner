# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T15:02:54.526109+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45844526198
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 928e9b0ded3034b1ee3dbdd98f58f5c2af24939e (atomic ledger/results publication)
**Ledger generation:** 1876 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 591; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.083 | 82.730 | 65.428 | +5.76% | +0.46% | 3.98x | 27.7 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | STRONG 86/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 9.14093 | 73.873 | 61.189 | +1.07% | -0.46% | 13.22x | 2.0 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 43.42 | 73.155 | 65.484 | +1.66% | -0.48% | 2.01x | 2.3 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04646 | 68.615 | 76.445 | +10.94% | -2.53% | 1.48x | 6.5 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 5 | XRP/USD | 0.94382 | 64.709 | 59.208 | +0.78% | -0.21% | 1.65x | 2.4 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SEI/USD | 0.03706 | 64.027 | 73.364 | +11.26% | -1.62% | 0.88x | 10.8 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 7 | SOL/USD | 70.71 | 62.363 | 57.475 | +0.45% | -0.32% | 1.65x | 1.4 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ADA/USD | 0.147715 | 58.442 | 64.306 | +1.33% | -0.39% | 0.61x | 0.1 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | WIF/USD | 0.1336 | 55.762 | 62.148 | +4.95% | -0.74% | 0.73x | 7.5 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | WEAK 33/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | VELO/USD | 0.002518 | 53.409 | 60.092 | +10.88% | -0.28% | 0.47x | 31.8 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | WEAK 22/100 | EXTREME 100/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0565108 | 51.214 | 53.399 | +0.99% | -0.42% | 0.99x | 0.6 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | FET/USD | 0.1143 | 50.560 | 62.186 | +5.35% | -0.69% | 0.18x | 17.5 | 2026-11-26T15:02:46.715059+00:00 | Not calibrated | WEAK 25/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 76.445 | 0.04646 | -2.53% | 1.48x |
| 2 | SEI/USD | 73.364 | 0.03706 | -1.62% | 0.88x |
| 3 | LTC/USD | 65.484 | 43.42 | -0.48% | 2.01x |
| 4 | ZRO/USD | 65.428 | 1.083 | +0.46% | 3.98x |
| 5 | ADA/USD | 64.306 | 0.147715 | -0.39% | 0.61x |
| 6 | FET/USD | 62.186 | 0.1143 | -0.69% | 0.18x |
| 7 | WIF/USD | 62.148 | 0.1336 | -0.74% | 0.73x |
| 8 | LINK/USD | 61.189 | 9.14093 | -0.46% | 13.22x |
| 9 | VELO/USD | 60.092 | 0.002518 | -0.28% | 0.47x |
| 10 | XRP/USD | 59.208 | 0.94382 | -0.21% | 1.65x |
| 11 | SOL/USD | 57.475 | 70.71 | -0.32% | 1.65x |
| 12 | XDG/USD | 53.399 | 0.0565108 | -0.42% | 0.99x |

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

- Persisted scans: 1876; predictions: 16247; observations: 1136781.
- Matured sampled outcomes across 1/6/24/48h: 35138; gap abstentions: 24955. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45844526198 · **Generation:** 1876 · **Legacy run:** 45844526198
**Main quote time:** 2026-11-26T15:02:54.526109+00:00 · **Legacy report time:** 2026-11-26T15:04:14.089656+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.083 | 82.73 | +0.46% | 3.98x | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 2 | LINK/USD | 9.14093 | 73.87 | -0.46% | 13.22x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 43.42 | 73.15 | -0.48% | 2.01x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | SKY/USD | 0.04646 | 68.61 | -2.53% | 1.48x | MODERATE 54/100 | VERY_HIGH 70/100 | Do nothing |
| 5 | XRP/USD | 0.94382 | 64.71 | -0.21% | 1.65x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 6 | SEI/USD | 0.03706 | 64.03 | -1.62% | 0.88x | WEAK 32/100 | VERY_HIGH 83/100 | Do nothing |
| 7 | SOL/USD | 70.71 | 62.36 | -0.32% | 1.65x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 8 | ADA/USD | 0.147715 | 58.44 | -0.39% | 0.61x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | WIF/USD | 0.1336 | 55.76 | -0.74% | 0.73x | WEAK 33/100 | EXTREME 88/100 | Do nothing |
| 10 | VELO/USD | 0.002518 | 53.41 | -0.28% | 0.47x | WEAK 22/100 | EXTREME 100/100 | Do nothing |
| 11 | XDG/USD | 0.0565108 | 51.21 | -0.42% | 0.99x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 12 | FET/USD | 0.1143 | 50.56 | -0.69% | 0.18x | WEAK 25/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.075 | 84.72 | +0.46% | 3.98x | 3054 | STRONG 100/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** ZRO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
