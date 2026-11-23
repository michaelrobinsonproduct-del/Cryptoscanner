# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T08:21:36.351327+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45137701239
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7095ce883495dcdfd7391e1d63c35efff79d993a (atomic ledger/results publication)
**Ledger generation:** 1404 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | JUP/USD | 0.24311 | 73.042 | 74.501 | +8.26% | +0.01% | 0.85x | 10.7 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SOL/USD | 71.97 | 69.823 | 66.891 | +1.90% | -0.10% | 1.34x | 2.8 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PAXG/USD | 3592.26 | 62.204 | 48.375 | +0.56% | -0.23% | 7.50x | 1.0 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 4 | AUD/USD | 0.66444 | 57.637 | 42.779 | +0.43% | -0.03% | 3.46x | 1.1 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.05011 | 57.450 | 59.458 | +1.91% | -0.26% | 0.93x | 10.0 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | SUI/USD | 0.664 | 55.578 | 62.355 | +1.27% | -0.42% | 0.53x | 3.0 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | DOT/USD | 0.6688 | 53.762 | 40.995 | +1.21% | -0.45% | 12.81x | 1.5 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93468 | 50.460 | 59.211 | +0.77% | -0.19% | 0.22x | 2.4 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | ADA/USD | 0.145525 | 48.991 | 52.209 | +0.64% | -0.47% | 0.91x | 1.9 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | WEAK 29/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | LTC/USD | 40.5 | 47.913 | 47.697 | +0.85% | -0.15% | 1.10x | 2.5 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | PEPE/USD | 3.403e-06 | 46.420 | 35.504 | +0.41% | -0.82% | 4.68x | 11.8 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |
| 12 | XAUT/USD | 3591.6 | 32.446 | 37.244 | +0.55% | -0.29% | 0.67x | 0.3 | 2026-11-23T08:21:28.855424+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 74.501 | 0.24311 | +0.01% | 0.85x |
| 2 | SOL/USD | 66.891 | 71.97 | -0.10% | 1.34x |
| 3 | SUI/USD | 62.355 | 0.664 | -0.42% | 0.53x |
| 4 | NIGHT/USD | 59.458 | 0.05011 | -0.26% | 0.93x |
| 5 | XRP/USD | 59.211 | 0.93468 | -0.19% | 0.22x |
| 6 | ADA/USD | 52.209 | 0.145525 | -0.47% | 0.91x |
| 7 | PAXG/USD | 48.375 | 3592.26 | -0.23% | 7.50x |
| 8 | LTC/USD | 47.697 | 40.5 | -0.15% | 1.10x |
| 9 | AUD/USD | 42.779 | 0.66444 | -0.03% | 3.46x |
| 10 | DOT/USD | 40.995 | 0.6688 | -0.45% | 12.81x |
| 11 | XAUT/USD | 37.244 | 3591.6 | -0.29% | 0.67x |
| 12 | PEPE/USD | 35.504 | 3.403e-06 | -0.82% | 4.68x |

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

- Persisted scans: 1404; predictions: 11615; observations: 850139.
- Matured sampled outcomes across 1/6/24/48h: 18942; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 127 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45137701239 · **Generation:** 1404 · **Legacy run:** 45137701239
**Main quote time:** 2026-11-23T08:21:36.351327+00:00 · **Legacy report time:** 2026-11-23T08:22:44.540512+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD | 0.24311 | 73.04 | +0.01% | 0.85x | MODERATE 52/100 | VERY_HIGH 73/100 | Watch |
| 2 | SOL/USD | 71.97 | 69.82 | -0.10% | 1.34x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 3 | PAXG/USD | 3592.26 | 62.20 | -0.23% | 7.50x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 4 | AUD/USD | 0.66444 | 57.64 | -0.03% | 3.46x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD | 0.05011 | 57.45 | -0.26% | 0.93x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 6 | SUI/USD | 0.664 | 55.58 | -0.42% | 0.53x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | DOT/USD | 0.6688 | 53.76 | -0.45% | 12.81x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 8 | XRP/USD | 0.93468 | 50.46 | -0.19% | 0.22x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | ADA/USD | 0.145525 | 48.99 | -0.47% | 0.91x | WEAK 29/100 | HIGH 68/100 | Do nothing |
| 10 | LTC/USD | 40.5 | 47.91 | -0.15% | 1.10x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 11 | PEPE/USD | 3.403e-06 | 46.42 | -0.82% | 4.68x | MODERATE 48/100 | HIGH 67/100 | Watch |
| 12 | XAUT/USD | 3591.6 | 32.45 | -0.29% | 0.67x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |

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
