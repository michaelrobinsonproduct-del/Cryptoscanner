# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T06:10:22.340205+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44470128343
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** c21942877a868c0cdf064bad1076d0ccc66dbc50 (atomic ledger/results publication)
**Ledger generation:** 773 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LIGHTER/USD | 2.902 | 94.657 | 71.230 | +6.93% | +2.87% | 1.91x | 20.7 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | STRONG 82/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | ZEC/USD | 940.21 | 93.379 | 76.639 | +3.10% | +0.35% | 5.62x | 0.1 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 22.844 | 87.436 | 89.564 | +5.41% | +0.67% | 0.45x | 5.7 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | TAO/USD | 195.324 | 81.240 | 64.996 | +1.75% | +0.25% | 3.59x | 4.5 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ETH/USD | 1799.3 | 73.844 | 64.484 | +1.38% | +0.21% | 1.83x | 0.4 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | LINK/USD | 9.11104 | 73.173 | 57.951 | +0.42% | +0.04% | 3.47x | 0.0 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.3935 | 72.874 | 73.777 | +2.91% | +0.52% | 0.65x | 3.2 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SOL/USD | 74.65 | 68.994 | 64.896 | +1.51% | +0.21% | 1.30x | 1.3 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 9 | HYPE/USD | 67.9 | 64.825 | 64.939 | +1.53% | +0.03% | 0.97x | 1.5 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 10 | TRX/USD | 0.312498 | 64.755 | 48.933 | +1.04% | +0.16% | 37.30x | 0.0 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 11 | ONDO/USD | 0.30158 | 60.288 | 44.158 | +1.32% | +0.23% | 19.11x | 0.3 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 12 | XBT/USD | 63386.7 | 55.337 | 59.462 | +0.64% | +0.25% | 0.46x | 0.0 | 2026-11-19T06:10:16.558874+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 89.564 | 22.844 | +0.67% | 0.45x |
| 2 | ZEC/USD | 76.639 | 940.21 | +0.35% | 5.62x |
| 3 | NEAR/USD | 73.777 | 3.3935 | +0.52% | 0.65x |
| 4 | LIGHTER/USD | 71.230 | 2.902 | +2.87% | 1.91x |
| 5 | TAO/USD | 64.996 | 195.324 | +0.25% | 3.59x |
| 6 | HYPE/USD | 64.939 | 67.9 | +0.03% | 0.97x |
| 7 | SOL/USD | 64.896 | 74.65 | +0.21% | 1.30x |
| 8 | ETH/USD | 64.484 | 1799.3 | +0.21% | 1.83x |
| 9 | XBT/USD | 59.462 | 63386.7 | +0.25% | 0.46x |
| 10 | LINK/USD | 57.951 | 9.11104 | +0.04% | 3.47x |
| 11 | TRX/USD | 48.933 | 0.312498 | +0.16% | 37.30x |
| 12 | ONDO/USD | 44.158 | 0.30158 | +0.23% | 19.11x |

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

- Persisted scans: 773; predictions: 6420; observations: 467763.
- Matured sampled outcomes across 1/6/24/48h: 6470; gap abstentions: 13818. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44470128343 · **Generation:** 773 · **Legacy run:** 44470128343
**Main quote time:** 2026-11-19T06:10:22.340205+00:00 · **Legacy report time:** 2026-11-19T06:11:13.433025+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD ⭐ | 2.902 | 94.66 | +2.87% | 1.91x | STRONG 92/100 | VERY_HIGH 72/100 | Watch |
| 2 | ZEC/USD ⭐ | 940.21 | 93.38 | +0.35% | 5.62x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD | 22.844 | 87.44 | +0.67% | 0.45x | STRONG 74/100 | VERY_HIGH 70/100 | Watch |
| 4 | TAO/USD | 195.324 | 81.24 | +0.25% | 3.59x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | ETH/USD ⭐ | 1799.3 | 73.84 | +0.21% | 1.83x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 6 | LINK/USD | 9.11104 | 73.17 | +0.04% | 3.47x | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | NEAR/USD | 3.3935 | 72.87 | +0.52% | 0.65x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 8 | SOL/USD ⭐ | 74.65 | 68.99 | +0.21% | 1.30x | STRONG 89/100 | HIGH 55/100 | Watch |
| 9 | HYPE/USD | 67.9 | 64.82 | +0.03% | 0.97x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 10 | TRX/USD | 0.312498 | 64.76 | +0.16% | 37.30x | STRONG 77/100 | HIGH 55/100 | Watch |
| 11 | ONDO/USD | 0.30158 | 60.29 | +0.23% | 19.11x | STRONG 85/100 | HIGH 60/100 | Watch |
| 12 | XBT/USD | 63386.7 | 55.34 | +0.25% | 0.46x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 940.57 | 97.22 | +0.35% | 5.62x | 22333 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LIGHTER/USD ⭐ | 2.902 | 85.57 | +2.87% | 1.91x | 4184 | STRONG 88/100 | VERY_HIGH 72/100 | Watch |
| 3 | ETH/USD ⭐ | 1799.19 | 72.36 | +0.21% | 1.83x | 58321 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 74.63 | 68.96 | +0.21% | 1.30x | 35205 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LIGHTER/USD, ZEC/USD, ETH/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
