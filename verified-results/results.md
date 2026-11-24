# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T22:52:18.070486+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45504505347
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 21aeb83652f0feb7079ccd43644a267cba780b01 (atomic ledger/results publication)
**Ledger generation:** 1636 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 508.97 | 97.248 | 84.416 | +4.72% | -0.43% | 5.86x | 7.3 | 2026-11-24T22:52:11.896291+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 24.893 | 79.403 | 64.523 | +1.82% | -0.02% | 3.08x | 6.4 | 2026-11-24T22:52:11.896291+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31113 | 66.319 | 59.042 | +0.60% | +0.01% | 1.73x | 0.4 | 2026-11-24T22:52:11.896291+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.493e-06 | 61.739 | 58.472 | +2.07% | -0.26% | 1.45x | 2.9 | 2026-11-24T22:52:11.896291+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04893 | 51.767 | 47.513 | +1.62% | -0.04% | 1.45x | 6.2 | 2026-11-24T22:52:11.896291+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LUNA/USD | 4.538e-05 | 46.284 | 49.187 | +4.39% | +0.42% | 0.50x | 26.5 | 2026-11-24T22:52:11.896291+00:00 | Not calibrated | WEAK 43/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | AUD/USD | 0.66449 | 45.229 | 45.391 | +0.29% | -0.00% | 0.99x | 0.6 | 2026-11-24T22:52:11.896291+00:00 | Not calibrated | WEAK 28/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | ZEUS/USD | 0.00452 | 39.140 | 42.913 | +3.20% | +0.67% | 0.29x | 22.1 | 2026-11-24T22:52:11.896291+00:00 | Not calibrated | WEAK 40/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | SKY/USD | 0.04087 | 32.176 | 39.689 | +1.19% | +0.34% | 0.08x | 4.9 | 2026-11-24T22:52:11.896291+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 84.416 | 508.97 | -0.43% | 5.86x |
| 2 | VVV/USD | 64.523 | 24.893 | -0.02% | 3.08x |
| 3 | GBP/USD | 59.042 | 1.31113 | +0.01% | 1.73x |
| 4 | PEPE/USD | 58.472 | 3.493e-06 | -0.26% | 1.45x |
| 5 | LUNA/USD | 49.187 | 4.538e-05 | +0.42% | 0.50x |
| 6 | NIGHT/USD | 47.513 | 0.04893 | -0.04% | 1.45x |
| 7 | AUD/USD | 45.391 | 0.66449 | -0.00% | 0.99x |
| 8 | ZEUS/USD | 42.913 | 0.00452 | +0.67% | 0.29x |
| 9 | SKY/USD | 39.689 | 0.04087 | +0.34% | 0.08x |

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

- Persisted scans: 1636; predictions: 14011; observations: 991415.
- Matured sampled outcomes across 1/6/24/48h: 28928; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45504505347 · **Generation:** 1636 · **Legacy run:** 45504505347
**Main quote time:** 2026-11-24T22:52:18.070486+00:00 · **Legacy report time:** 2026-11-24T22:53:12.082756+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 508.97 | 97.25 | -0.43% | 5.86x | STRONG 79/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD | 24.893 | 79.40 | -0.02% | 3.08x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | GBP/USD | 1.31113 | 66.32 | +0.01% | 1.73x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD | 3.493e-06 | 61.74 | -0.26% | 1.45x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD | 0.04893 | 51.77 | -0.04% | 1.45x | MODERATE 46/100 | HIGH 61/100 | Watch |
| 6 | LUNA/USD | 4.538e-05 | 46.28 | +0.42% | 0.50x | WEAK 43/100 | EXTREME 87/100 | Do nothing |
| 7 | AUD/USD | 0.66449 | 45.23 | -0.00% | 0.99x | WEAK 28/100 | HIGH 68/100 | Do nothing |
| 8 | ZEUS/USD | 0.00452 | 39.14 | +0.67% | 0.29x | WEAK 40/100 | EXTREME 94/100 | Do nothing |
| 9 | SKY/USD | 0.04087 | 32.18 | +0.34% | 0.08x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

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
