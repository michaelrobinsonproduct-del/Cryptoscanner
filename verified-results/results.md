# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T09:01:09.272429+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45005350899
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** a00f167900db3f416f84a0276725fe8696339479 (atomic ledger/results publication)
**Ledger generation:** 1261 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZBCN/USD | 0.001918 | 94.063 | 62.018 | +11.06% | +3.41% | 3.78x | 31.3 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | STRONG 92/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | ZEC/USD | 792.89 | 78.305 | 63.261 | +1.89% | +0.01% | 2.50x | 10.0 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 3 | TAO/USD | 189.7341 | 63.656 | 66.406 | +2.16% | -0.06% | 0.75x | 6.8 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 4 | NEAR/USD | 2.9268 | 60.421 | 61.576 | +1.40% | +0.02% | 0.87x | 6.5 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 5 | VVV/USD | 25.42 | 59.930 | 64.499 | +2.09% | -0.77% | 0.93x | 10.2 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 6 | PUMP/USD | 0.002397 | 55.598 | 51.731 | +2.26% | +0.17% | 1.30x | 12.5 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ENA/USD | 0.0991 | 51.653 | 36.653 | +0.81% | +0.00% | 6.02x | 10.1 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | MODERATE 66/100 | HIGH 66/100 | Watch | WATCH |
| 8 | ETH/USD | 1686.74 | 50.105 | 55.670 | +0.27% | +0.07% | 0.41x | 2.4 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LINK/USD | 8.64751 | 48.942 | 54.596 | +0.61% | -0.31% | 0.59x | 3.8 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | INJ/USD | 6.086 | 48.482 | 49.220 | +1.89% | +0.12% | 0.87x | 8.2 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | WEAK 44/100 | HIGH 62/100 | Watch | WATCH |
| 11 | AVAX/USD | 6.592 | 47.316 | 45.678 | +0.44% | -0.14% | 1.23x | 4.5 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | ASTER/USD | 0.50058 | 44.712 | 50.421 | +3.07% | +0.01% | 0.42x | 11.0 | 2026-11-22T09:01:01.029574+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 66.406 | 189.7341 | -0.06% | 0.75x |
| 2 | VVV/USD | 64.499 | 25.42 | -0.77% | 0.93x |
| 3 | ZEC/USD | 63.261 | 792.89 | +0.01% | 2.50x |
| 4 | ZBCN/USD | 62.018 | 0.001918 | +3.41% | 3.78x |
| 5 | NEAR/USD | 61.576 | 2.9268 | +0.02% | 0.87x |
| 6 | ETH/USD | 55.670 | 1686.74 | +0.07% | 0.41x |
| 7 | LINK/USD | 54.596 | 8.64751 | -0.31% | 0.59x |
| 8 | PUMP/USD | 51.731 | 0.002397 | +0.17% | 1.30x |
| 9 | ASTER/USD | 50.421 | 0.50058 | +0.01% | 0.42x |
| 10 | INJ/USD | 49.220 | 6.086 | +0.12% | 0.87x |
| 11 | AVAX/USD | 45.678 | 6.592 | -0.14% | 1.23x |
| 12 | ENA/USD | 36.653 | 0.0991 | +0.00% | 6.02x |

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

- Persisted scans: 1261; predictions: 10056; observations: 763058.
- Matured sampled outcomes across 1/6/24/48h: 14480; gap abstentions: 22131. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45005350899 · **Generation:** 1261 · **Legacy run:** 45005350899
**Main quote time:** 2026-11-22T09:01:09.272429+00:00 · **Legacy report time:** 2026-11-22T09:01:56.059107+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD | 0.001918 | 94.06 | +3.41% | 3.78x | STRONG 92/100 | VERY_HIGH 82/100 | Watch |
| 2 | ZEC/USD | 792.89 | 78.30 | +0.01% | 2.50x | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | TAO/USD | 189.7341 | 63.66 | -0.06% | 0.75x | WEAK 37/100 | HIGH 68/100 | Watch |
| 4 | NEAR/USD | 2.9268 | 60.42 | +0.02% | 0.87x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 5 | VVV/USD | 25.42 | 59.93 | -0.77% | 0.93x | WEAK 30/100 | VERY_HIGH 74/100 | Do nothing |
| 6 | PUMP/USD ⭐ | 0.002397 | 55.60 | +0.17% | 1.30x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 7 | ENA/USD | 0.0991 | 51.65 | +0.00% | 6.02x | MODERATE 66/100 | HIGH 66/100 | Watch |
| 8 | ETH/USD | 1686.74 | 50.11 | +0.07% | 0.41x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 9 | LINK/USD | 8.64751 | 48.94 | -0.31% | 0.59x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | INJ/USD | 6.086 | 48.48 | +0.12% | 0.87x | WEAK 44/100 | HIGH 62/100 | Watch |
| 11 | AVAX/USD | 6.592 | 47.32 | -0.14% | 1.23x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 12 | ASTER/USD | 0.50058 | 44.71 | +0.01% | 0.42x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002397 | 58.14 | +0.17% | 1.30x | 4639 | STRONG 74/100 | HIGH 55/100 | Watch |
| 2 | PEARL/USD | 1.9908 | 57.94 | +0.24% | 1.44x | 8323 | MODERATE 69/100 | HIGH 61/100 | Watch |

**Same-run overlap:** PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
