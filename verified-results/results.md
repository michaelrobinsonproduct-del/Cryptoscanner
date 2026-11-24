# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T22:22:09.534422+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45499850831
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a59958dbe71933d13dc6a0ff95bb651af4870cd4 (atomic ledger/results publication)
**Ledger generation:** 1633 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | GBP/USD | 1.31074 | 73.813 | 58.909 | +0.57% | -0.02% | 3.50x | 0.2 | 2026-11-24T22:22:04.340364+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 507.7 | 71.247 | 76.556 | +4.46% | -0.07% | 0.50x | 19.3 | 2026-11-24T22:22:04.340364+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | VVV/USD | 24.797 | 62.223 | 61.562 | +1.43% | +1.15% | 0.49x | 6.9 | 2026-11-24T22:22:04.340364+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.485e-06 | 59.818 | 55.177 | +1.84% | +0.26% | 1.33x | 5.7 | 2026-11-24T22:22:04.340364+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04869 | 41.838 | 44.174 | +1.12% | -0.06% | 0.80x | 6.2 | 2026-11-24T22:22:04.340364+00:00 | Not calibrated | WEAK 26/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | SKY/USD | 0.04081 | 31.845 | 35.020 | +1.04% | -0.49% | 0.93x | 12.3 | 2026-11-24T22:22:04.340364+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | LUNA/USD | 4.488e-05 | 28.123 | 35.454 | +3.24% | -0.49% | 0.51x | 37.8 | 2026-11-24T22:22:04.340364+00:00 | Not calibrated | WEAK 4/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 76.556 | 507.7 | -0.07% | 0.50x |
| 2 | VVV/USD | 61.562 | 24.797 | +1.15% | 0.49x |
| 3 | GBP/USD | 58.909 | 1.31074 | -0.02% | 3.50x |
| 4 | PEPE/USD | 55.177 | 3.485e-06 | +0.26% | 1.33x |
| 5 | NIGHT/USD | 44.174 | 0.04869 | -0.06% | 0.80x |
| 6 | LUNA/USD | 35.454 | 4.488e-05 | -0.49% | 0.51x |
| 7 | SKY/USD | 35.020 | 0.04081 | -0.49% | 0.93x |

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

- Persisted scans: 1633; predictions: 13987; observations: 989588.
- Matured sampled outcomes across 1/6/24/48h: 28811; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45499850831 · **Generation:** 1633 · **Legacy run:** 45499850831
**Main quote time:** 2026-11-24T22:22:09.534422+00:00 · **Legacy report time:** 2026-11-24T22:23:24.209833+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | GBP/USD | 1.31074 | 73.81 | -0.02% | 3.50x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 507.7 | 71.25 | -0.07% | 0.50x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 3 | VVV/USD | 24.797 | 62.22 | +1.15% | 0.49x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.485e-06 | 59.82 | +0.26% | 1.33x | STRONG 85/100 | HIGH 55/100 | Watch |
| 5 | NIGHT/USD | 0.04869 | 41.84 | -0.06% | 0.80x | WEAK 26/100 | HIGH 68/100 | Do nothing |
| 6 | SKY/USD | 0.04081 | 31.84 | -0.49% | 0.93x | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | LUNA/USD | 4.488e-05 | 28.12 | -0.49% | 0.51x | WEAK 4/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.483e-06 | 63.85 | +0.26% | 1.33x | 6783 | STRONG 87/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
