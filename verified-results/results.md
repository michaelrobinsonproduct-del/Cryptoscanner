# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T01:30:46.673541+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44971698699
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 5fe4d42e09c220ae3055dd64f066056b31443c89 (atomic ledger/results publication)
**Ledger generation:** 1214 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.34529 | 65.363 | 59.009 | +3.01% | +0.66% | 1.31x | 20.3 | 2026-11-22T01:30:38.887314+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.8943 | 55.894 | 55.557 | +0.28% | -0.45% | 1.26x | 2.8 | 2026-11-22T01:30:38.887314+00:00 | Not calibrated | WEAK 38/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.98 | 48.578 | 41.425 | +1.63% | +1.65% | 0.89x | 25.8 | 2026-11-22T01:30:38.887314+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | RENDER/USD | 1.31 | 36.182 | 37.476 | +0.46% | +0.00% | 0.87x | 7.6 | 2026-11-22T01:30:38.887314+00:00 | Not calibrated | WEAK 38/100 | HIGH 62/100 | Watch | WATCH |
| 5 | CAP/USD | 0.093216 | 35.352 | 39.373 | +1.37% | +0.48% | 0.36x | 10.9 | 2026-11-22T01:30:38.887314+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 59.009 | 0.34529 | +0.66% | 1.31x |
| 2 | NEAR/USD | 55.557 | 2.8943 | -0.45% | 1.26x |
| 3 | PEARL/USD | 41.425 | 1.98 | +1.65% | 0.89x |
| 4 | CAP/USD | 39.373 | 0.093216 | +0.48% | 0.36x |
| 5 | RENDER/USD | 37.476 | 1.31 | +0.00% | 0.87x |

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

- Persisted scans: 1214; predictions: 9816; observations: 734470.
- Matured sampled outcomes across 1/6/24/48h: 13444; gap abstentions: 21804. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 21 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 19; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44971698699 · **Generation:** 1214 · **Legacy run:** 44971698699
**Main quote time:** 2026-11-22T01:30:46.673541+00:00 · **Legacy report time:** 2026-11-22T01:31:28.833992+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.34529 | 65.36 | +0.66% | 1.31x | STRONG 78/100 | HIGH 67/100 | Watch |
| 2 | NEAR/USD | 2.8943 | 55.89 | -0.45% | 1.26x | WEAK 38/100 | HIGH 61/100 | Watch |
| 3 | PEARL/USD | 1.98 | 48.58 | +1.65% | 0.89x | WEAK 44/100 | VERY_HIGH 74/100 | Watch |
| 4 | RENDER/USD | 1.31 | 36.18 | +0.00% | 0.87x | WEAK 38/100 | HIGH 62/100 | Watch |
| 5 | CAP/USD | 0.093216 | 35.35 | +0.48% | 0.36x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.34338 | 65.28 | +0.66% | 1.31x | 16421 | STRONG 78/100 | HIGH 67/100 | Watch |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
