# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T23:36:03.473419+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45722420513
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fa13c05334909f54ac7fd4f2fddff280daf149ab (atomic ledger/results publication)
**Ledger generation:** 1782 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0051 | 95.456 | 83.268 | +4.18% | -0.56% | 2.69x | 2.0 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6636 | 81.177 | 70.898 | +2.49% | -0.03% | 2.04x | 3.0 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 42.4 | 77.804 | 80.381 | +3.79% | -0.19% | 0.84x | 2.4 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XLM/USD | 0.12747 | 76.625 | 62.794 | +2.75% | -0.23% | 3.10x | 1.0 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ZEC/USD | 761.57 | 75.989 | 75.370 | +3.07% | -0.10% | 1.11x | 2.2 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 6 | HYPE/USD | 61.17 | 66.345 | 69.382 | +2.17% | -0.13% | 0.76x | 1.6 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XMR/USD | 521.15 | 61.647 | 67.410 | +2.27% | +0.18% | 0.33x | 6.9 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XAUT/USD | 3566.6 | 59.075 | 44.398 | +0.82% | -0.06% | 6.44x | 0.6 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XRP/USD | 0.93475 | 59.057 | 63.389 | +1.21% | +0.03% | 0.55x | 0.1 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1688.6 | 56.258 | 59.514 | +0.65% | +0.03% | 0.66x | 0.1 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 60159.5 | 53.413 | 59.892 | +0.70% | -0.06% | 0.38x | 0.0 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XDG/USD | 0.0557946 | 51.976 | 55.190 | +1.01% | -0.06% | 0.71x | 0.0 | 2026-11-25T23:35:56.428124+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 83.268 | 3.0051 | -0.56% | 2.69x |
| 2 | LTC/USD | 80.381 | 42.4 | -0.19% | 0.84x |
| 3 | ZEC/USD | 75.370 | 761.57 | -0.10% | 1.11x |
| 4 | SUI/USD | 70.898 | 0.6636 | -0.03% | 2.04x |
| 5 | HYPE/USD | 69.382 | 61.17 | -0.13% | 0.76x |
| 6 | XMR/USD | 67.410 | 521.15 | +0.18% | 0.33x |
| 7 | XRP/USD | 63.389 | 0.93475 | +0.03% | 0.55x |
| 8 | XLM/USD | 62.794 | 0.12747 | -0.23% | 3.10x |
| 9 | XBT/USD | 59.892 | 60159.5 | -0.06% | 0.38x |
| 10 | ETH/USD | 59.514 | 1688.6 | +0.03% | 0.66x |
| 11 | XDG/USD | 55.190 | 0.0557946 | -0.06% | 0.71x |
| 12 | XAUT/USD | 44.398 | 3566.6 | -0.06% | 6.44x |

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

- Persisted scans: 1782; predictions: 15128; observations: 1080282.
- Matured sampled outcomes across 1/6/24/48h: 32899; gap abstentions: 23393. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45722420513 · **Generation:** 1782 · **Legacy run:** 45722420513
**Main quote time:** 2026-11-25T23:36:03.473419+00:00 · **Legacy report time:** 2026-11-25T23:37:19.627338+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0051 | 95.46 | -0.56% | 2.69x | STRONG 78/100 | HIGH 61/100 | Watch |
| 2 | SUI/USD | 0.6636 | 81.18 | -0.03% | 2.04x | STRONG 71/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 42.4 | 77.80 | -0.19% | 0.84x | WEAK 44/100 | HIGH 68/100 | Watch |
| 4 | XLM/USD | 0.12747 | 76.62 | -0.23% | 3.10x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | ZEC/USD | 761.57 | 75.99 | -0.10% | 1.11x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 6 | HYPE/USD | 61.17 | 66.34 | -0.13% | 0.76x | WEAK 38/100 | HIGH 68/100 | Watch |
| 7 | XMR/USD | 521.15 | 61.65 | +0.18% | 0.33x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 8 | XAUT/USD | 3566.6 | 59.08 | -0.06% | 6.44x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 9 | XRP/USD | 0.93475 | 59.06 | +0.03% | 0.55x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1688.6 | 56.26 | +0.03% | 0.66x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 60159.5 | 53.41 | -0.06% | 0.38x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XDG/USD | 0.0557946 | 51.98 | -0.06% | 0.71x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 0.968 | 82.30 | +0.73% | 2.91x | 2958 | STRONG 86/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
