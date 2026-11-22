# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T02:21:32.837542+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44975554832
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** ad10f6eaa364f4f431ffc3fd207a21395a2b6531 (atomic ledger/results publication)
**Ledger generation:** 1220 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | RENDER/USD | 1.313 | 52.045 | 39.321 | +0.69% | -0.46% | 15.73x | 7.6 | 2026-11-22T02:21:26.563613+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZBCN/USD | 0.001802 | 47.893 | 43.807 | +4.34% | -0.44% | 1.63x | 38.9 | 2026-11-22T02:21:26.563613+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.0445 | 41.966 | 45.768 | +0.50% | -0.25% | 0.74x | 11.2 | 2026-11-22T02:21:26.563613+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | PEPE/USD | 3.413e-06 | 36.029 | 43.481 | +0.29% | -0.09% | 0.30x | 8.8 | 2026-11-22T02:21:26.563613+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | PEARL/USD | 1.955 | 31.113 | 33.021 | +0.34% | -2.09% | 1.85x | 24.6 | 2026-11-22T02:21:26.563613+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 6 | ZRO/USD | 1.181 | 24.283 | 35.915 | +0.68% | -0.84% | 0.26x | 17.0 | 2026-11-22T02:21:26.563613+00:00 | Not calibrated | WEAK 12/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 45.768 | 0.0445 | -0.25% | 0.74x |
| 2 | ZBCN/USD | 43.807 | 0.001802 | -0.44% | 1.63x |
| 3 | PEPE/USD | 43.481 | 3.413e-06 | -0.09% | 0.30x |
| 4 | RENDER/USD | 39.321 | 1.313 | -0.46% | 15.73x |
| 5 | ZRO/USD | 35.915 | 1.181 | -0.84% | 0.26x |
| 6 | PEARL/USD | 33.021 | 1.955 | -2.09% | 1.85x |

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

- Persisted scans: 1220; predictions: 9866; observations: 738118.
- Matured sampled outcomes across 1/6/24/48h: 13615; gap abstentions: 21891. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 24 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44975554832 · **Generation:** 1220 · **Legacy run:** 44975554832
**Main quote time:** 2026-11-22T02:21:32.837542+00:00 · **Legacy report time:** 2026-11-22T02:22:37.881821+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | RENDER/USD | 1.313 | 52.04 | -0.46% | 15.73x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 2 | ZBCN/USD | 0.001802 | 47.89 | -0.44% | 1.63x | WEAK 29/100 | VERY_HIGH 78/100 | Do nothing |
| 3 | NIGHT/USD | 0.0445 | 41.97 | -0.25% | 0.74x | WEAK 21/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | PEPE/USD | 3.413e-06 | 36.03 | -0.09% | 0.30x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | PEARL/USD | 1.955 | 31.11 | -2.09% | 1.85x | WEAK 26/100 | VERY_HIGH 77/100 | Do nothing |
| 6 | ZRO/USD | 1.181 | 24.28 | -0.84% | 0.26x | WEAK 12/100 | VERY_HIGH 82/100 | Do nothing |

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
