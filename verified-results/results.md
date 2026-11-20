# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T09:10:47.746411+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44708331150
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** de66f7219d8f1498c4d491d944ac51d9c1168b4a (atomic ledger/results publication)
**Ledger generation:** 958 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 606; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HBAR/USD | 0.05406 | 50.472 | 42.549 | +0.56% | -0.26% | 1.92x | 3.7 | 2026-11-20T09:10:42.718100+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SAPIEN/USD | 0.04089 | 34.439 | 36.382 | +1.82% | +0.59% | 0.51x | 14.7 | 2026-11-20T09:10:42.718100+00:00 | Not calibrated | WEAK 42/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | SKR/USD | 0.01023 | 28.285 | 38.397 | +1.83% | -1.13% | 0.56x | 11.7 | 2026-11-20T09:10:42.718100+00:00 | Not calibrated | WEAK 14/100 | EXTREME 98/100 | Do nothing | WATCH |
| 4 | TON/USD | 1.02 | 22.810 | 25.376 | +0.29% | -0.29% | 0.89x | 19.6 | 2026-11-20T09:10:42.718100+00:00 | Not calibrated | WEAK 11/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 5 | ICNT/USD | 0.4345 | 13.647 | 36.245 | +1.97% | -2.78% | 0.13x | 32.3 | 2026-11-20T09:10:42.718100+00:00 | Not calibrated | WEAK 2/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HBAR/USD | 42.549 | 0.05406 | -0.26% | 1.92x |
| 2 | SKR/USD | 38.397 | 0.01023 | -1.13% | 0.56x |
| 3 | SAPIEN/USD | 36.382 | 0.04089 | +0.59% | 0.51x |
| 4 | ICNT/USD | 36.245 | 0.4345 | -2.78% | 0.13x |
| 5 | TON/USD | 25.376 | 1.02 | -0.29% | 0.89x |

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

- Persisted scans: 958; predictions: 8130; observations: 578867.
- Matured sampled outcomes across 1/6/24/48h: 9676; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44708331150 · **Generation:** 958 · **Legacy run:** 44708331150
**Main quote time:** 2026-11-20T09:10:47.746411+00:00 · **Legacy report time:** 2026-11-20T09:11:52.695966+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD | 0.05406 | 50.47 | -0.26% | 1.92x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 2 | SAPIEN/USD | 0.04089 | 34.44 | +0.59% | 0.51x | WEAK 42/100 | EXTREME 88/100 | Do nothing |
| 3 | SKR/USD | 0.01023 | 28.29 | -1.13% | 0.56x | WEAK 14/100 | EXTREME 98/100 | Do nothing |
| 4 | TON/USD | 1.02 | 22.81 | -0.29% | 0.89x | WEAK 11/100 | VERY_HIGH 79/100 | Do nothing |
| 5 | ICNT/USD | 0.4345 | 13.65 | -2.78% | 0.13x | WEAK 2/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.09674 | 27.93 | +0.21% | 1.34x | 6849 | MODERATE 54/100 | HIGH 66/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
