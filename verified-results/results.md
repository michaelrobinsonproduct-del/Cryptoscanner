# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T23:11:51.552083+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45507511776
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a5ee8d586979b29142503f0d635ce708b1924190 (atomic ledger/results publication)
**Ledger generation:** 1638 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WINGS/USD | 0.002186 | 84.486 | 58.734 | +5.50% | +2.15% | 3.26x | 22.5 | 2026-11-24T23:11:47.038232+00:00 | Not calibrated | STRONG 87/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | XMR/USD | 509.63 | 80.119 | 83.998 | +4.86% | +0.19% | 0.52x | 10.0 | 2026-11-24T23:11:47.038232+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | VVV/USD | 24.785 | 53.916 | 60.406 | +1.38% | -0.47% | 0.58x | 8.5 | 2026-11-24T23:11:47.038232+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | GBP/USD | 1.31047 | 53.853 | 58.687 | +0.55% | -0.04% | 0.54x | 0.4 | 2026-11-24T23:11:47.038232+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | PEPE/USD | 3.471e-06 | 52.271 | 51.224 | +1.43% | -0.34% | 1.28x | 8.6 | 2026-11-24T23:11:47.038232+00:00 | Not calibrated | WEAK 36/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04885 | 45.243 | 45.257 | +1.45% | +0.04% | 0.98x | 8.2 | 2026-11-24T23:11:47.038232+00:00 | Not calibrated | WEAK 43/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SKY/USD | 0.04094 | 44.336 | 38.464 | +1.36% | -0.66% | 1.92x | 9.8 | 2026-11-24T23:11:47.038232+00:00 | Not calibrated | WEAK 42/100 | HIGH 66/100 | Watch | WATCH |
| 8 | ZEUS/USD | 0.00453 | 34.957 | 44.540 | +3.42% | +0.00% | 0.04x | 22.1 | 2026-11-24T23:11:47.038232+00:00 | Not calibrated | WEAK 27/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 83.998 | 509.63 | +0.19% | 0.52x |
| 2 | VVV/USD | 60.406 | 24.785 | -0.47% | 0.58x |
| 3 | WINGS/USD | 58.734 | 0.002186 | +2.15% | 3.26x |
| 4 | GBP/USD | 58.687 | 1.31047 | -0.04% | 0.54x |
| 5 | PEPE/USD | 51.224 | 3.471e-06 | -0.34% | 1.28x |
| 6 | NIGHT/USD | 45.257 | 0.04885 | +0.04% | 0.98x |
| 7 | ZEUS/USD | 44.540 | 0.00453 | +0.00% | 0.04x |
| 8 | SKY/USD | 38.464 | 0.04094 | -0.66% | 1.92x |

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

- Persisted scans: 1638; predictions: 14028; observations: 992633.
- Matured sampled outcomes across 1/6/24/48h: 28987; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45507511776 · **Generation:** 1638 · **Legacy run:** 45507511776
**Main quote time:** 2026-11-24T23:11:51.552083+00:00 · **Legacy report time:** 2026-11-24T23:12:37.475983+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD ⭐ | 0.002186 | 84.49 | +2.15% | 3.26x | STRONG 97/100 | VERY_HIGH 79/100 | Watch |
| 2 | XMR/USD | 509.63 | 80.12 | +0.19% | 0.52x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |
| 3 | VVV/USD | 24.785 | 53.92 | -0.47% | 0.58x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | GBP/USD | 1.31047 | 53.85 | -0.04% | 0.54x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | PEPE/USD | 3.471e-06 | 52.27 | -0.34% | 1.28x | WEAK 36/100 | HIGH 61/100 | Watch |
| 6 | NIGHT/USD | 0.04885 | 45.24 | +0.04% | 0.98x | WEAK 43/100 | HIGH 62/100 | Watch |
| 7 | SKY/USD | 0.04094 | 44.34 | -0.66% | 1.92x | WEAK 42/100 | HIGH 66/100 | Watch |
| 8 | ZEUS/USD | 0.00453 | 34.96 | +0.00% | 0.04x | WEAK 27/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD ⭐ | 0.00223 | 85.35 | +2.15% | 3.26x | 3823 | STRONG 98/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** WINGS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
