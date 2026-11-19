# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T18:25:38.242197+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44587475928
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 21b7efb965a84e23125370134ffd110a0eb01aad (atomic ledger/results publication)
**Ledger generation:** 834 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 69.69 | 89.340 | 82.258 | +4.20% | +0.40% | 1.51x | 4.3 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | PUMP/USD | 0.002706 | 73.442 | 68.267 | +4.24% | +1.01% | 1.01x | 7.4 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 3 | VVV/USD | 22.565 | 71.411 | 78.778 | +4.13% | -0.12% | 0.32x | 10.2 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | SKR/USD | 0.010212 | 69.312 | 68.791 | +6.01% | +0.28% | 0.91x | 8.8 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | LIGHTER/USD | 2.848 | 66.320 | 67.580 | +4.94% | -0.45% | 1.10x | 3.5 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | CT/USD | 0.128 | 66.215 | 68.976 | +8.29% | +0.55% | 0.45x | 15.6 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | ADA/USD | 0.153659 | 61.351 | 64.373 | +1.59% | +0.44% | 0.48x | 3.5 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97438 | 61.134 | 60.289 | +0.83% | +0.38% | 0.89x | 1.0 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5511 | 58.452 | 66.842 | +6.39% | +0.09% | 0.12x | 20.0 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | ETH/USD | 1780.81 | 57.635 | 57.358 | +0.34% | +0.39% | 0.83x | 0.1 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 11 | SOL/USD | 74.25 | 55.838 | 61.085 | +0.97% | +0.42% | 0.27x | 1.3 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AVAX/USD | 7.055 | 42.523 | 48.017 | +0.48% | +0.59% | 0.16x | 4.3 | 2026-11-19T18:25:29.884459+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 82.258 | 69.69 | +0.40% | 1.51x |
| 2 | VVV/USD | 78.778 | 22.565 | -0.12% | 0.32x |
| 3 | CT/USD | 68.976 | 0.128 | +0.55% | 0.45x |
| 4 | SKR/USD | 68.791 | 0.010212 | +0.28% | 0.91x |
| 5 | PUMP/USD | 68.267 | 0.002706 | +1.01% | 1.01x |
| 6 | LIGHTER/USD | 67.580 | 2.848 | -0.45% | 1.10x |
| 7 | AKT/USD | 66.842 | 0.5511 | +0.09% | 0.12x |
| 8 | ADA/USD | 64.373 | 0.153659 | +0.44% | 0.48x |
| 9 | SOL/USD | 61.085 | 74.25 | +0.42% | 0.27x |
| 10 | XRP/USD | 60.289 | 0.97438 | +0.38% | 0.89x |
| 11 | ETH/USD | 57.358 | 1780.81 | +0.39% | 0.83x |
| 12 | AVAX/USD | 48.017 | 7.055 | +0.59% | 0.16x |

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

- Persisted scans: 834; predictions: 7152; observations: 504143.
- Matured sampled outcomes across 1/6/24/48h: 7139; gap abstentions: 15516. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44587475928 · **Generation:** 834 · **Legacy run:** 44587475928
**Main quote time:** 2026-11-19T18:25:38.242197+00:00 · **Legacy report time:** 2026-11-19T18:26:22.001731+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 69.69 | 89.34 | +0.40% | 1.51x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PUMP/USD ⭐ | 0.002706 | 73.44 | +1.01% | 1.01x | STRONG 82/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD | 22.565 | 71.41 | -0.12% | 0.32x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 4 | SKR/USD | 0.010212 | 69.31 | +0.28% | 0.91x | MODERATE 65/100 | VERY_HIGH 74/100 | Watch |
| 5 | LIGHTER/USD | 2.848 | 66.32 | -0.45% | 1.10x | WEAK 43/100 | VERY_HIGH 73/100 | Watch |
| 6 | CT/USD | 0.128 | 66.22 | +0.55% | 0.45x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 7 | ADA/USD | 0.153659 | 61.35 | +0.44% | 0.48x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.97438 | 61.13 | +0.38% | 0.89x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 9 | AKT/USD | 0.5511 | 58.45 | +0.09% | 0.12x | WEAK 44/100 | VERY_HIGH 81/100 | Watch |
| 10 | ETH/USD | 1780.81 | 57.63 | +0.39% | 0.83x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 11 | SOL/USD | 74.25 | 55.84 | +0.42% | 0.27x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 12 | AVAX/USD | 7.055 | 42.52 | +0.59% | 0.16x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 69.66 | 94.62 | +0.40% | 1.51x | 13525 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PUMP/USD ⭐ | 0.002706 | 80.46 | +1.01% | 1.01x | 4100 | STRONG 80/100 | HIGH 68/100 | Watch |
| 3 | INJ/USD | 7.178 | 76.02 | +1.02% | 1.51x | 7006 | STRONG 83/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** HYPE/USD, PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
