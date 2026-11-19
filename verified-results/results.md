# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:10:25.101406+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44456368565
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ff4fad3a19f79a30eb42267f3ff1ec7faecbc902 (atomic ledger/results publication)
**Ledger generation:** 751 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.4169 | 98.463 | 77.879 | +3.62% | +1.12% | 3.15x | 5.0 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.484 | 93.420 | 73.820 | +3.75% | +0.92% | 7.48x | 7.6 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LUNA/USD | 4.85e-05 | 92.143 | 76.934 | +11.39% | +3.30% | 0.87x | 2.1 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 4 | ETH/USD | 1796.28 | 81.468 | 63.460 | +1.21% | +0.60% | 6.58x | 0.1 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | PYTH/USD | 0.05545 | 75.899 | 62.099 | +5.10% | +1.35% | 1.70x | 10.8 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Consider small entry | WATCH |
| 6 | ZEC/USD | 925.6 | 75.578 | 63.533 | +1.50% | +0.99% | 1.71x | 3.9 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XRP/USD | 0.97099 | 75.317 | 58.141 | +0.48% | +0.44% | 9.23x | 0.4 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | HYPE/USD | 67.43 | 70.071 | 59.273 | +0.82% | +0.43% | 1.86x | 3.0 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | LINK/USD | 9.11651 | 64.859 | 56.327 | +0.48% | +0.64% | 1.53x | 4.1 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SOL/USD | 74.27 | 64.184 | 61.275 | +0.99% | +0.35% | 1.12x | 1.3 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 11 | TAO/USD | 194.6642 | 63.456 | 61.112 | +1.41% | +0.76% | 0.86x | 7.5 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 12 | LTC/USD | 44.43 | 62.202 | 52.033 | +0.95% | +0.18% | 1.93x | 2.3 | 2026-11-19T04:10:17.980233+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 77.879 | 3.4169 | +1.12% | 3.15x |
| 2 | LUNA/USD | 76.934 | 4.85e-05 | +3.30% | 0.87x |
| 3 | VVV/USD | 73.820 | 22.484 | +0.92% | 7.48x |
| 4 | ZEC/USD | 63.533 | 925.6 | +0.99% | 1.71x |
| 5 | ETH/USD | 63.460 | 1796.28 | +0.60% | 6.58x |
| 6 | PYTH/USD | 62.099 | 0.05545 | +1.35% | 1.70x |
| 7 | SOL/USD | 61.275 | 74.27 | +0.35% | 1.12x |
| 8 | TAO/USD | 61.112 | 194.6642 | +0.76% | 0.86x |
| 9 | HYPE/USD | 59.273 | 67.43 | +0.43% | 1.86x |
| 10 | XRP/USD | 58.141 | 0.97099 | +0.44% | 9.23x |
| 11 | LINK/USD | 56.327 | 9.11651 | +0.64% | 1.53x |
| 12 | LTC/USD | 52.033 | 44.43 | +0.18% | 1.93x |

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

- Persisted scans: 751; predictions: 6156; observations: 454365.
- Matured sampled outcomes across 1/6/24/48h: 6120; gap abstentions: 13610. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44456368565 · **Generation:** 751 · **Legacy run:** 44456368565
**Main quote time:** 2026-11-19T04:10:25.101406+00:00 · **Legacy report time:** 2026-11-19T04:11:14.754741+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.4169 | 98.46 | +1.12% | 3.15x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.484 | 93.42 | +0.92% | 7.48x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LUNA/USD | 4.85e-05 | 92.14 | +3.30% | 0.87x | STRONG 76/100 | VERY_HIGH 77/100 | Watch |
| 4 | ETH/USD ⭐ | 1796.28 | 81.47 | +0.60% | 6.58x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | PYTH/USD ⭐ | 0.05545 | 75.90 | +1.35% | 1.70x | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 6 | ZEC/USD | 925.6 | 75.58 | +0.99% | 1.71x | STRONG 83/100 | HIGH 55/100 | Consider small entry |
| 7 | XRP/USD | 0.97099 | 75.32 | +0.44% | 9.23x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 8 | HYPE/USD ⭐ | 67.43 | 70.07 | +0.43% | 1.86x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 9 | LINK/USD | 9.11651 | 64.86 | +0.64% | 1.53x | STRONG 77/100 | HIGH 55/100 | Watch |
| 10 | SOL/USD ⭐ | 74.27 | 64.18 | +0.35% | 1.12x | STRONG 77/100 | HIGH 62/100 | Watch |
| 11 | TAO/USD | 194.6642 | 63.46 | +0.76% | 0.86x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 12 | LTC/USD | 44.43 | 62.20 | +0.18% | 1.93x | MODERATE 66/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.4145 | 96.01 | +1.12% | 3.15x | 14194 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.418 | 86.91 | +0.92% | 7.48x | 8809 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1796.2 | 76.19 | +0.60% | 6.58x | 58407 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | PYTH/USD ⭐ | 0.05545 | 72.64 | +1.35% | 1.70x | 2001 | STRONG 86/100 | HIGH 66/100 | Consider small entry |
| 5 | TRUMP/USD | 0.972 | 69.52 | +0.72% | 4.45x | 2795 | STRONG 85/100 | HIGH 66/100 | Watch |
| 6 | HYPE/USD ⭐ | 67.43 | 63.65 | +0.43% | 1.86x | 14485 | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 7 | SOL/USD ⭐ | 74.24 | 62.24 | +0.35% | 1.12x | 35131 | STRONG 76/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NEAR/USD, VVV/USD, ETH/USD, PYTH/USD, HYPE/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
