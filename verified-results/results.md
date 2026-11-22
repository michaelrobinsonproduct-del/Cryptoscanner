# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T02:31:12.682578+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44976334480
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 2c01a92c43274fb55ee75b41cef04fbc870b569b (atomic ledger/results publication)
**Ledger generation:** 1221 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZBCN/USD | 0.001813 | 48.759 | 53.828 | +4.98% | +0.00% | 0.49x | 27.8 | 2026-11-22T02:31:05.848462+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 2 | NIGHT/USD | 0.04467 | 41.878 | 44.037 | +0.88% | -0.38% | 0.97x | 20.2 | 2026-11-22T02:31:05.848462+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 3 | RENDER/USD | 1.311 | 35.797 | 34.437 | +0.54% | -0.38% | 1.33x | 15.3 | 2026-11-22T02:31:05.848462+00:00 | Not calibrated | WEAK 33/100 | HIGH 67/100 | Do nothing | WATCH |
| 4 | ENSO/USD | 0.501 | 26.025 | 38.517 | +3.94% | -2.91% | 1.20x | 39.6 | 2026-11-22T02:31:05.848462+00:00 | Not calibrated | WEAK 8/100 | EXTREME 96/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZBCN/USD | 53.828 | 0.001813 | +0.00% | 0.49x |
| 2 | NIGHT/USD | 44.037 | 0.04467 | -0.38% | 0.97x |
| 3 | ENSO/USD | 38.517 | 0.501 | -2.91% | 1.20x |
| 4 | RENDER/USD | 34.437 | 1.311 | -0.38% | 1.33x |

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

- Persisted scans: 1221; predictions: 9870; observations: 738726.
- Matured sampled outcomes across 1/6/24/48h: 13645; gap abstentions: 21904. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 25 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44976334480 · **Generation:** 1221 · **Legacy run:** 44976334480
**Main quote time:** 2026-11-22T02:31:12.682578+00:00 · **Legacy report time:** 2026-11-22T02:32:13.033814+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD | 0.001813 | 48.76 | +0.00% | 0.49x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 2 | NIGHT/USD | 0.04467 | 41.88 | -0.38% | 0.97x | WEAK 16/100 | VERY_HIGH 80/100 | Do nothing |
| 3 | RENDER/USD | 1.311 | 35.80 | -0.38% | 1.33x | WEAK 33/100 | HIGH 67/100 | Do nothing |
| 4 | ENSO/USD | 0.501 | 26.03 | -2.91% | 1.20x | WEAK 8/100 | EXTREME 96/100 | Do nothing |

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
