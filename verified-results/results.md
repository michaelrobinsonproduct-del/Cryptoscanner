# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T12:51:38.130212+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45177954573
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b47b5d0470f495f1bcdaeff941dde3c20d3646ef (atomic ledger/results publication)
**Ledger generation:** 1432 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.44 | 101.381 | 89.412 | +9.06% | +0.49% | 1.95x | 6.4 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.93837 | 78.168 | 63.120 | +1.17% | +0.01% | 2.62x | 0.1 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SOL/USD | 72.01 | 75.294 | 67.983 | +1.95% | -0.44% | 1.95x | 1.4 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03173 | 70.439 | 66.360 | +7.30% | +0.57% | 1.12x | 18.9 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 5 | ALGO/USD | 0.08291 | 69.576 | 77.673 | +9.92% | -0.04% | 0.21x | 6.0 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | LTC/USD | 40.81 | 67.099 | 51.976 | +1.62% | +0.02% | 3.04x | 2.5 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 7 | KAS/USD | 0.02714 | 60.781 | 66.578 | +5.15% | +0.11% | 0.36x | 7.4 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | XMR/USD | 502.45 | 60.615 | 65.401 | +1.77% | -0.22% | 0.63x | 4.0 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | UNI/USD | 4.7355 | 58.975 | 47.578 | +1.16% | -0.72% | 7.48x | 0.2 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SUI/USD | 0.667 | 58.726 | 65.563 | +1.72% | -0.40% | 0.52x | 3.0 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | CC/USD | 0.07639 | 58.420 | 62.720 | +4.26% | -0.26% | 0.70x | 3.9 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | TRX/USD | 0.306838 | 54.928 | 41.490 | +0.54% | -0.12% | 2.40x | 1.0 | 2026-11-23T12:51:31.501846+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 89.412 | 156.44 | +0.49% | 1.95x |
| 2 | ALGO/USD | 77.673 | 0.08291 | -0.04% | 0.21x |
| 3 | SOL/USD | 67.983 | 72.01 | -0.44% | 1.95x |
| 4 | KAS/USD | 66.578 | 0.02714 | +0.11% | 0.36x |
| 5 | UAI/USD | 66.360 | 0.03173 | +0.57% | 1.12x |
| 6 | SUI/USD | 65.563 | 0.667 | -0.40% | 0.52x |
| 7 | XMR/USD | 65.401 | 502.45 | -0.22% | 0.63x |
| 8 | XRP/USD | 63.120 | 0.93837 | +0.01% | 2.62x |
| 9 | CC/USD | 62.720 | 0.07639 | -0.26% | 0.70x |
| 10 | LTC/USD | 51.976 | 40.81 | +0.02% | 3.04x |
| 11 | UNI/USD | 47.578 | 4.7355 | -0.72% | 7.48x |
| 12 | TRX/USD | 41.490 | 0.306838 | -0.12% | 2.40x |

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

- Persisted scans: 1432; predictions: 11951; observations: 867191.
- Matured sampled outcomes across 1/6/24/48h: 20048; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45177954573 · **Generation:** 1432 · **Legacy run:** 45177954573
**Main quote time:** 2026-11-23T12:51:38.130212+00:00 · **Legacy report time:** 2026-11-23T12:52:32.281980+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 156.44 | 101.38 | +0.49% | 1.95x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD | 0.93837 | 78.17 | +0.01% | 2.62x | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD | 72.01 | 75.29 | -0.44% | 1.95x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 4 | UAI/USD ⭐ | 0.03173 | 70.44 | +0.57% | 1.12x | STRONG 75/100 | VERY_HIGH 80/100 | Watch |
| 5 | ALGO/USD | 0.08291 | 69.58 | -0.04% | 0.21x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 6 | LTC/USD | 40.81 | 67.10 | +0.02% | 3.04x | STRONG 79/100 | HIGH 55/100 | Watch |
| 7 | KAS/USD | 0.02714 | 60.78 | +0.11% | 0.36x | MODERATE 50/100 | VERY_HIGH 75/100 | Watch |
| 8 | XMR/USD | 502.45 | 60.62 | -0.22% | 0.63x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | UNI/USD | 4.7355 | 58.97 | -0.72% | 7.48x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 10 | SUI/USD | 0.667 | 58.73 | -0.40% | 0.52x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | CC/USD | 0.07639 | 58.42 | -0.26% | 0.70x | WEAK 34/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | TRX/USD | 0.306838 | 54.93 | -0.12% | 2.40x | MODERATE 57/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 156.88 | 86.82 | +0.49% | 1.95x | 6065 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 2 | UAI/USD ⭐ | 0.03173 | 66.43 | +0.57% | 1.12x | 1889 | STRONG 78/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** QNT/USD, UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
