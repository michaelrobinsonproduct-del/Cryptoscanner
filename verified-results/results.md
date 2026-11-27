# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T21:12:32.549435+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46068437731
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f1781aa4b831732cd9b4c29bec444a96c1d1be70 (atomic ledger/results publication)
**Ledger generation:** 2061 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 735.52 | 92.901 | 98.029 | +7.90% | +0.28% | 0.35x | 3.9 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TAO/USD | 187.8902 | 88.359 | 68.534 | +2.23% | +0.97% | 24.49x | 4.2 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | RENDER/USD | 1.407 | 81.296 | 64.872 | +5.55% | +0.28% | 2.69x | 14.2 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | STRONG 91/100 | HIGH 66/100 | Consider small entry | WATCH |
| 4 | LTC/USD | 44.3 | 80.780 | 62.833 | +1.28% | +0.59% | 3.79x | 2.3 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | SPACE/USD | 0.004177 | 71.046 | 71.056 | +7.88% | +1.02% | 0.49x | 9.6 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0576774 | 70.720 | 71.031 | +2.31% | +0.14% | 0.90x | 0.3 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 7 | HYPE/USD | 64.05 | 67.666 | 74.807 | +2.94% | +0.19% | 0.19x | 1.6 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | NIGHT/USD | 0.05003 | 67.014 | 74.531 | +3.22% | -0.20% | 0.35x | 6.0 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94872 | 63.366 | 59.222 | +0.63% | +0.12% | 1.36x | 0.4 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SOL/USD | 71.96 | 60.510 | 64.370 | +1.44% | +0.17% | 0.53x | 1.4 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AVAX/USD | 6.64 | 58.995 | 43.844 | +0.68% | +0.03% | 3.79x | 1.5 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XAUT/USD | 3645.7 | 58.352 | 54.488 | +2.42% | -0.04% | 1.40x | 0.3 | 2026-11-27T21:12:26.540032+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.029 | 735.52 | +0.28% | 0.35x |
| 2 | HYPE/USD | 74.807 | 64.05 | +0.19% | 0.19x |
| 3 | NIGHT/USD | 74.531 | 0.05003 | -0.20% | 0.35x |
| 4 | SPACE/USD | 71.056 | 0.004177 | +1.02% | 0.49x |
| 5 | XDG/USD | 71.031 | 0.0576774 | +0.14% | 0.90x |
| 6 | TAO/USD | 68.534 | 187.8902 | +0.97% | 24.49x |
| 7 | RENDER/USD | 64.872 | 1.407 | +0.28% | 2.69x |
| 8 | SOL/USD | 64.370 | 71.96 | +0.17% | 0.53x |
| 9 | LTC/USD | 62.833 | 44.3 | +0.59% | 3.79x |
| 10 | XRP/USD | 59.222 | 0.94872 | +0.12% | 1.36x |
| 11 | XAUT/USD | 54.488 | 3645.7 | -0.04% | 1.40x |
| 12 | AVAX/USD | 43.844 | 6.64 | +0.03% | 3.79x |

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

- Persisted scans: 2061; predictions: 18434; observations: 1248014.
- Matured sampled outcomes across 1/6/24/48h: 41795; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46068437731 · **Generation:** 2061 · **Legacy run:** 46068437731
**Main quote time:** 2026-11-27T21:12:32.549435+00:00 · **Legacy report time:** 2026-11-27T21:13:27.120245+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 735.52 | 92.90 | +0.28% | 0.35x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 2 | TAO/USD | 187.8902 | 88.36 | +0.97% | 24.49x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | RENDER/USD ⭐ | 1.407 | 81.30 | +0.28% | 2.69x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 4 | LTC/USD | 44.3 | 80.78 | +0.59% | 3.79x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 5 | SPACE/USD | 0.004177 | 71.05 | +1.02% | 0.49x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 6 | XDG/USD | 0.0576774 | 70.72 | +0.14% | 0.90x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 7 | HYPE/USD | 64.05 | 67.67 | +0.19% | 0.19x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 8 | NIGHT/USD | 0.05003 | 67.01 | -0.20% | 0.35x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 9 | XRP/USD | 0.94872 | 63.37 | +0.12% | 1.36x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 10 | SOL/USD | 71.96 | 60.51 | +0.17% | 0.53x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 11 | AVAX/USD | 6.64 | 58.99 | +0.03% | 3.79x | STRONG 74/100 | HIGH 55/100 | Watch |
| 12 | XAUT/USD | 3645.7 | 58.35 | -0.04% | 1.40x | MODERATE 49/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RENDER/USD ⭐ | 1.406 | 73.70 | +0.28% | 2.69x | 1943 | STRONG 97/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** RENDER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
