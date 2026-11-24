# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T19:56:47.298083+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45475164960
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 309e037a06bdf23d9aa4883c821b5900e0ac9cc6 (atomic ledger/results publication)
**Ledger generation:** 1619 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 500.65 | 77.504 | 72.071 | +3.01% | -0.25% | 1.67x | 8.0 | 2026-11-24T19:56:43.753657+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31107 | 59.128 | 59.086 | +0.60% | +0.00% | 1.00x | 0.2 | 2026-11-24T19:56:43.753657+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 3 | AUD/USD | 0.66438 | 57.914 | 42.516 | +0.27% | +0.08% | 15.45x | 5.3 | 2026-11-24T19:56:43.753657+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01633 | 56.822 | 58.182 | +4.34% | -0.97% | 1.35x | 6.1 | 2026-11-24T19:56:43.753657+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.443e-06 | 44.976 | 46.276 | +0.61% | -0.09% | 0.91x | 2.9 | 2026-11-24T19:56:43.753657+00:00 | Not calibrated | WEAK 27/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | NIGHT/USD | 0.04864 | 43.564 | 46.753 | +1.02% | +0.10% | 0.63x | 2.1 | 2026-11-24T19:56:43.753657+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 72.071 | 500.65 | -0.25% | 1.67x |
| 2 | GBP/USD | 59.086 | 1.31107 | +0.00% | 1.00x |
| 3 | 2Z/USD | 58.182 | 0.01633 | -0.97% | 1.35x |
| 4 | NIGHT/USD | 46.753 | 0.04864 | +0.10% | 0.63x |
| 5 | PEPE/USD | 46.276 | 3.443e-06 | -0.09% | 0.91x |
| 6 | AUD/USD | 42.516 | 0.66438 | +0.08% | 15.45x |

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

- Persisted scans: 1619; predictions: 13896; observations: 981063.
- Matured sampled outcomes across 1/6/24/48h: 28269; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45475164960 · **Generation:** 1619 · **Legacy run:** 45475164960
**Main quote time:** 2026-11-24T19:56:47.298083+00:00 · **Legacy report time:** 2026-11-24T19:57:37.289323+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 500.65 | 77.50 | -0.25% | 1.67x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 2 | GBP/USD | 1.31107 | 59.13 | +0.00% | 1.00x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 3 | AUD/USD ⭐ | 0.66438 | 57.91 | +0.08% | 15.45x | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | 2Z/USD | 0.01633 | 56.82 | -0.97% | 1.35x | MODERATE 48/100 | VERY_HIGH 73/100 | Watch |
| 5 | PEPE/USD | 3.443e-06 | 44.98 | -0.09% | 0.91x | WEAK 27/100 | HIGH 68/100 | Do nothing |
| 6 | NIGHT/USD | 0.04864 | 43.56 | +0.10% | 0.63x | WEAK 42/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AUD/USD ⭐ | 0.66438 | 47.41 | +0.08% | 15.45x | 4149 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** AUD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
