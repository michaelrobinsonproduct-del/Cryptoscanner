# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T05:57:28.347773+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46114195249
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5df00dc61189819e6141f5f3d8337101a437ed32 (atomic ledger/results publication)
**Ledger generation:** 2114 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 414.4 | 56.890 | 64.238 | +1.75% | -1.20% | 0.87x | 6.0 | 2026-11-28T05:57:24.750777+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.024302 | 53.128 | 46.107 | +2.48% | -1.60% | 3.92x | 4.5 | 2026-11-28T05:57:24.750777+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 3 | ZEC/USD | 738.11 | 49.857 | 57.088 | +0.48% | -0.19% | 0.37x | 2.6 | 2026-11-28T05:57:24.750777+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | VVV/USD | 26.038 | 49.738 | 49.365 | +1.12% | -0.15% | 1.11x | 8.1 | 2026-11-28T05:57:24.750777+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 5 | KAVA/USD | 0.0274 | 21.902 | 15.658 | +0.37% | +0.37% | 1.44x | 36.6 | 2026-11-28T05:57:24.750777+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 64.238 | 414.4 | -1.20% | 0.87x |
| 2 | ZEC/USD | 57.088 | 738.11 | -0.19% | 0.37x |
| 3 | VVV/USD | 49.365 | 26.038 | -0.15% | 1.11x |
| 4 | SENT/USD | 46.107 | 0.024302 | -1.60% | 3.92x |
| 5 | KAVA/USD | 15.658 | 0.0274 | +0.37% | 1.44x |

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

- Persisted scans: 2114; predictions: 18962; observations: 1280130.
- Matured sampled outcomes across 1/6/24/48h: 44278; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46114195249 · **Generation:** 2114 · **Legacy run:** 46114195249
**Main quote time:** 2026-11-28T05:57:28.347773+00:00 · **Legacy report time:** 2026-11-28T05:58:05.058846+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 414.4 | 56.89 | -1.20% | 0.87x | WEAK 33/100 | VERY_HIGH 72/100 | Do nothing |
| 2 | SENT/USD | 0.024302 | 53.13 | -1.60% | 3.92x | MODERATE 57/100 | VERY_HIGH 77/100 | Do nothing |
| 3 | ZEC/USD | 738.11 | 49.86 | -0.19% | 0.37x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | VVV/USD | 26.038 | 49.74 | -0.15% | 1.11x | WEAK 35/100 | HIGH 68/100 | Watch |
| 5 | KAVA/USD | 0.0274 | 21.90 | +0.37% | 1.44x | WEAK 41/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD | 0.004257 | 48.55 | +0.31% | 8.38x | 1978 | MODERATE 64/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
