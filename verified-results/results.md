# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T01:45:51.505334+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44655817104
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 32844c3d86258b5d8ccbad804f0f3172322be1db (atomic ledger/results publication)
**Ledger generation:** 900 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 500.23 | 65.963 | 57.570 | +0.55% | -0.20% | 1.94x | 2.6 | 2026-11-20T01:45:46.893679+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XRP/USD | 0.96312 | 51.576 | 56.838 | +0.40% | -0.33% | 0.64x | 2.0 | 2026-11-20T01:45:46.893679+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.04498 | 51.406 | 39.385 | +0.49% | -0.60% | 3.54x | 8.9 | 2026-11-20T01:45:46.893679+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XLM/USD | 0.1335 | 50.024 | 57.573 | +0.60% | -0.33% | 0.41x | 3.3 | 2026-11-20T01:45:46.893679+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | CAP/USD | 0.097855 | 33.368 | 37.112 | +1.28% | +0.69% | 0.28x | 12.8 | 2026-11-20T01:45:46.893679+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | ICNT/USD | 0.4299 | 24.187 | 32.210 | +0.89% | -0.32% | 0.36x | 23.3 | 2026-11-20T01:45:46.893679+00:00 | Not calibrated | WEAK 7/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 57.573 | 0.1335 | -0.33% | 0.41x |
| 2 | XMR/USD | 57.570 | 500.23 | -0.20% | 1.94x |
| 3 | XRP/USD | 56.838 | 0.96312 | -0.33% | 0.64x |
| 4 | NIGHT/USD | 39.385 | 0.04498 | -0.60% | 3.54x |
| 5 | CAP/USD | 37.112 | 0.097855 | +0.69% | 0.28x |
| 6 | ICNT/USD | 32.210 | 0.4299 | -0.32% | 0.36x |

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

- Persisted scans: 900; predictions: 7858; observations: 543825.
- Matured sampled outcomes across 1/6/24/48h: 8670; gap abstentions: 16265. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44655817104 · **Generation:** 900 · **Legacy run:** 44655817104
**Main quote time:** 2026-11-20T01:45:51.505334+00:00 · **Legacy report time:** 2026-11-20T01:46:40.344221+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 500.23 | 65.96 | -0.20% | 1.94x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 2 | XRP/USD | 0.96312 | 51.58 | -0.33% | 0.64x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | NIGHT/USD | 0.04498 | 51.41 | -0.60% | 3.54x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 4 | XLM/USD | 0.1335 | 50.02 | -0.33% | 0.41x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | CAP/USD | 0.097855 | 33.37 | +0.69% | 0.28x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |
| 6 | ICNT/USD | 0.4299 | 24.19 | -0.32% | 0.36x | WEAK 7/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKE/USD | 0.01054926 | 27.50 | +0.23% | 1.15x | 4179 | WEAK 44/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
