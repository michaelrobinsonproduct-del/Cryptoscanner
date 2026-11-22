# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T11:50:34.132727+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45019158488
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 18d60087c1e9ca9142dcbd9542fda5a964b45a41 (atomic ledger/results publication)
**Ledger generation:** 1278 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04728 | 113.791 | 86.656 | +6.78% | +2.43% | 6.75x | 8.5 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.35286 | 81.582 | 69.853 | +5.27% | +2.28% | 1.03x | 15.9 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | STRONG 71/100 | HIGH 68/100 | Watch | WATCH |
| 3 | CRV/USD | 0.18577 | 80.989 | 68.557 | +4.15% | -0.26% | 2.37x | 11.3 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 4 | NEAR/USD | 2.9935 | 73.010 | 79.161 | +3.71% | -0.12% | 0.45x | 3.7 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002477 | 67.273 | 75.468 | +5.67% | -0.12% | 0.24x | 12.1 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | INJ/USD | 6.22 | 66.389 | 68.717 | +4.14% | -0.69% | 1.11x | 4.8 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.55 | 63.202 | 68.375 | +2.14% | +0.24% | 0.36x | 3.2 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ZEC/USD | 795.15 | 62.313 | 67.884 | +2.18% | -0.44% | 0.66x | 4.8 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6597 | 58.525 | 66.893 | +1.92% | -0.21% | 0.27x | 3.0 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | XBT/USD | 60859.9 | 58.241 | 63.962 | +1.28% | -0.18% | 0.52x | 0.0 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1704.92 | 56.336 | 64.391 | +1.35% | -0.15% | 0.27x | 0.1 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SOL/USD | 70.59 | 52.454 | 58.481 | +0.60% | -0.17% | 0.48x | 1.4 | 2026-11-22T11:50:28.142961+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 86.656 | 0.04728 | +2.43% | 6.75x |
| 2 | NEAR/USD | 79.161 | 2.9935 | -0.12% | 0.45x |
| 3 | PUMP/USD | 75.468 | 0.002477 | -0.12% | 0.24x |
| 4 | DRV/USD | 69.853 | 0.35286 | +2.28% | 1.03x |
| 5 | INJ/USD | 68.717 | 6.22 | -0.69% | 1.11x |
| 6 | CRV/USD | 68.557 | 0.18577 | -0.26% | 2.37x |
| 7 | HYPE/USD | 68.375 | 62.55 | +0.24% | 0.36x |
| 8 | ZEC/USD | 67.884 | 795.15 | -0.44% | 0.66x |
| 9 | SUI/USD | 66.893 | 0.6597 | -0.21% | 0.27x |
| 10 | ETH/USD | 64.391 | 1704.92 | -0.15% | 0.27x |
| 11 | XBT/USD | 63.962 | 60859.9 | -0.18% | 0.52x |
| 12 | SOL/USD | 58.481 | 70.59 | -0.17% | 0.48x |

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

- Persisted scans: 1278; predictions: 10256; observations: 773411.
- Matured sampled outcomes across 1/6/24/48h: 14814; gap abstentions: 22226. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45019158488 · **Generation:** 1278 · **Legacy run:** 45019158488
**Main quote time:** 2026-11-22T11:50:34.132727+00:00 · **Legacy report time:** 2026-11-22T11:51:19.312363+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04728 | 113.79 | +2.43% | 6.75x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | DRV/USD | 0.35286 | 81.58 | +2.28% | 1.03x | STRONG 71/100 | HIGH 68/100 | Watch |
| 3 | CRV/USD | 0.18577 | 80.99 | -0.26% | 2.37x | MODERATE 65/100 | HIGH 67/100 | Watch |
| 4 | NEAR/USD | 2.9935 | 73.01 | -0.12% | 0.45x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 5 | PUMP/USD | 0.002477 | 67.27 | -0.12% | 0.24x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | INJ/USD | 6.22 | 66.39 | -0.69% | 1.11x | WEAK 43/100 | HIGH 68/100 | Watch |
| 7 | HYPE/USD | 62.55 | 63.20 | +0.24% | 0.36x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 8 | ZEC/USD | 795.15 | 62.31 | -0.44% | 0.66x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | SUI/USD | 0.6597 | 58.53 | -0.21% | 0.27x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | XBT/USD | 60859.9 | 58.24 | -0.18% | 0.52x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ETH/USD | 1704.92 | 56.34 | -0.15% | 0.27x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SOL/USD | 70.59 | 52.45 | -0.17% | 0.48x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04726 | 94.80 | +2.43% | 6.75x | 9092 | STRONG 100/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
