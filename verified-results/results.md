# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T02:10:59.552818+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44974758453
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 666efbae51d15c37d83d17244d4928daea83b073 (atomic ledger/results publication)
**Ledger generation:** 1219 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 2.911 | 72.809 | 58.929 | +0.86% | +0.14% | 2.32x | 4.1 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZBCN/USD | 0.001815 | 65.836 | 46.394 | +5.10% | +0.89% | 2.64x | 44.3 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | RENDER/USD | 1.318 | 54.742 | 42.006 | +1.07% | -0.45% | 15.56x | 7.6 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 4 | TAO/USD | 186.5089 | 52.441 | 56.175 | +0.42% | -0.26% | 0.76x | 3.5 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | NIGHT/USD | 0.04468 | 45.961 | 49.817 | +0.90% | +0.02% | 0.60x | 9.0 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PROMPT/USD | 0.01081 | 41.491 | 28.560 | +0.28% | +0.00% | 2.29x | 9.3 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | MODERATE 66/100 | HIGH 67/100 | Watch | WATCH |
| 7 | TRUMP/USD | 0.889 | 35.599 | 31.775 | +0.34% | -0.34% | 1.55x | 11.2 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 8 | DRV/USD | 0.3364 | 32.638 | 43.936 | +0.36% | -0.86% | 0.30x | 12.5 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | ZRO/USD | 1.188 | 29.386 | 40.235 | +1.28% | -0.67% | 0.25x | 16.8 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | WEAK 15/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | ENA/USD | 0.0986 | 28.750 | 38.556 | +0.31% | -0.20% | 0.12x | 10.2 | 2026-11-22T02:10:52.921153+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 58.929 | 2.911 | +0.14% | 2.32x |
| 2 | TAO/USD | 56.175 | 186.5089 | -0.26% | 0.76x |
| 3 | NIGHT/USD | 49.817 | 0.04468 | +0.02% | 0.60x |
| 4 | ZBCN/USD | 46.394 | 0.001815 | +0.89% | 2.64x |
| 5 | DRV/USD | 43.936 | 0.3364 | -0.86% | 0.30x |
| 6 | RENDER/USD | 42.006 | 1.318 | -0.45% | 15.56x |
| 7 | ZRO/USD | 40.235 | 1.188 | -0.67% | 0.25x |
| 8 | ENA/USD | 38.556 | 0.0986 | -0.20% | 0.12x |
| 9 | TRUMP/USD | 31.775 | 0.889 | -0.34% | 1.55x |
| 10 | PROMPT/USD | 28.560 | 0.01081 | +0.00% | 2.29x |

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

- Persisted scans: 1219; predictions: 9860; observations: 737510.
- Matured sampled outcomes across 1/6/24/48h: 13584; gap abstentions: 21879. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 22 (sampled only; not a success-rate estimate).
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

**Writer:** 44974758453 · **Generation:** 1219 · **Legacy run:** 44974758453
**Main quote time:** 2026-11-22T02:10:59.552818+00:00 · **Legacy report time:** 2026-11-22T02:12:03.169444+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.911 | 72.81 | +0.14% | 2.32x | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | ZBCN/USD ⭐ | 0.001815 | 65.84 | +0.89% | 2.64x | STRONG 83/100 | VERY_HIGH 82/100 | Watch |
| 3 | RENDER/USD | 1.318 | 54.74 | -0.45% | 15.56x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 4 | TAO/USD | 186.5089 | 52.44 | -0.26% | 0.76x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 5 | NIGHT/USD | 0.04468 | 45.96 | +0.02% | 0.60x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 6 | PROMPT/USD | 0.01081 | 41.49 | +0.00% | 2.29x | MODERATE 66/100 | HIGH 67/100 | Watch |
| 7 | TRUMP/USD | 0.889 | 35.60 | -0.34% | 1.55x | WEAK 33/100 | VERY_HIGH 72/100 | Do nothing |
| 8 | DRV/USD | 0.3364 | 32.64 | -0.86% | 0.30x | WEAK 16/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | ZRO/USD | 1.188 | 29.39 | -0.67% | 0.25x | WEAK 15/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | ENA/USD | 0.0986 | 28.75 | -0.20% | 0.12x | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD ⭐ | 0.001813 | 80.94 | +0.89% | 2.64x | 3525 | STRONG 90/100 | VERY_HIGH 82/100 | Watch |
| 2 | NEAR/USD ⭐ | 2.9097 | 60.54 | +0.14% | 2.32x | 19864 | STRONG 85/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, ZBCN/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
