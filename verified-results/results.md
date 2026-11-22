# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T09:11:17.401904+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45006163029
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** c508a4f20c15a9498e391b82c70c22a941c09f1b (atomic ledger/results publication)
**Ledger generation:** 1262 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.244 | 57.842 | 60.508 | +1.38% | +0.52% | 0.47x | 8.3 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TAO/USD | 189.5551 | 56.456 | 64.625 | +2.06% | -0.00% | 0.18x | 8.0 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | ZEC/USD | 789.88 | 55.271 | 63.445 | +1.50% | -0.41% | 0.39x | 4.2 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | NEAR/USD | 2.9081 | 54.229 | 57.880 | +0.76% | +0.06% | 0.61x | 4.8 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ASTER/USD | 0.49978 | 46.148 | 52.255 | +2.91% | -0.13% | 0.46x | 5.0 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 6 | AI/USD | 0.01573 | 45.939 | 66.315 | +11.72% | -2.24% | 0.08x | 18.9 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | WEAK 23/100 | EXTREME 98/100 | Do nothing | WATCH |
| 7 | RENDER/USD | 1.337 | 44.473 | 50.552 | +2.53% | -0.07% | 0.43x | 7.5 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | LINK/USD | 8.61875 | 43.191 | 53.145 | +0.28% | -0.13% | 0.07x | 1.6 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | PUMP/USD | 0.002392 | 41.264 | 49.953 | +2.05% | +0.08% | 0.09x | 12.6 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.582 | 40.898 | 44.481 | +0.29% | -0.02% | 0.65x | 4.6 | 2026-11-22T09:11:09.499886+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 66.315 | 0.01573 | -2.24% | 0.08x |
| 2 | TAO/USD | 64.625 | 189.5551 | -0.00% | 0.18x |
| 3 | ZEC/USD | 63.445 | 789.88 | -0.41% | 0.39x |
| 4 | VVV/USD | 60.508 | 25.244 | +0.52% | 0.47x |
| 5 | NEAR/USD | 57.880 | 2.9081 | +0.06% | 0.61x |
| 6 | LINK/USD | 53.145 | 8.61875 | -0.13% | 0.07x |
| 7 | ASTER/USD | 52.255 | 0.49978 | -0.13% | 0.46x |
| 8 | RENDER/USD | 50.552 | 1.337 | -0.07% | 0.43x |
| 9 | PUMP/USD | 49.953 | 0.002392 | +0.08% | 0.09x |
| 10 | AVAX/USD | 44.481 | 6.582 | -0.02% | 0.65x |

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

- Persisted scans: 1262; predictions: 10066; observations: 763667.
- Matured sampled outcomes across 1/6/24/48h: 14492; gap abstentions: 22140. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45006163029 · **Generation:** 1262 · **Legacy run:** 45006163029
**Main quote time:** 2026-11-22T09:11:17.401904+00:00 · **Legacy report time:** 2026-11-22T09:12:21.250372+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.244 | 57.84 | +0.52% | 0.47x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 2 | TAO/USD | 189.5551 | 56.46 | -0.00% | 0.18x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | ZEC/USD | 789.88 | 55.27 | -0.41% | 0.39x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | NEAR/USD | 2.9081 | 54.23 | +0.06% | 0.61x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 5 | ASTER/USD | 0.49978 | 46.15 | -0.13% | 0.46x | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing |
| 6 | AI/USD | 0.01573 | 45.94 | -2.24% | 0.08x | WEAK 23/100 | EXTREME 98/100 | Do nothing |
| 7 | RENDER/USD | 1.337 | 44.47 | -0.07% | 0.43x | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | LINK/USD | 8.61875 | 43.19 | -0.13% | 0.07x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | PUMP/USD | 0.002392 | 41.26 | +0.08% | 0.09x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | AVAX/USD | 6.582 | 40.90 | -0.02% | 0.65x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD | 0.001946 | 87.68 | +3.15% | 5.29x | 3606 | STRONG 84/100 | VERY_HIGH 82/100 | Watch |
| 2 | PEARL/USD | 1.9943 | 61.48 | +0.61% | 1.49x | 8320 | MODERATE 66/100 | HIGH 67/100 | Watch |
| 3 | AUD/USD | 0.66098 | 43.75 | +0.11% | 1.55x | 3393 | MODERATE 57/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
