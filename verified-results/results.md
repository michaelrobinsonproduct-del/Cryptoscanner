# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T23:32:11.398521+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45510406252
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 705cfea92b7e23f57c43964f529cfa0786d66b9b (atomic ledger/results publication)
**Ledger generation:** 1640 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 509.22 | 81.650 | 85.953 | +4.77% | -0.12% | 0.63x | 4.9 | 2026-11-24T23:32:07.178703+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | WINGS/USD | 0.00222 | 65.878 | 63.054 | +7.14% | +1.18% | 0.69x | 26.9 | 2026-11-24T23:32:07.178703+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | LUNA/USD | 4.579e-05 | 64.730 | 50.480 | +5.34% | +1.48% | 1.69x | 37.1 | 2026-11-24T23:32:07.178703+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | GBP/USD | 1.31063 | 53.371 | 58.811 | +0.57% | +0.00% | 0.45x | 0.3 | 2026-11-24T23:32:07.178703+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | VVV/USD | 24.639 | 51.307 | 56.402 | +0.78% | -0.52% | 0.75x | 8.1 | 2026-11-24T23:32:07.178703+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | NIGHT/USD | 0.04887 | 42.946 | 47.511 | +1.50% | -0.10% | 0.59x | 4.1 | 2026-11-24T23:32:07.178703+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | SKY/USD | 0.04116 | 42.812 | 42.304 | +1.91% | +0.71% | 0.70x | 9.7 | 2026-11-24T23:32:07.178703+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | PEPE/USD | 3.446e-06 | 39.877 | 44.420 | +0.70% | -0.23% | 0.66x | 11.6 | 2026-11-24T23:32:07.178703+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 85.953 | 509.22 | -0.12% | 0.63x |
| 2 | WINGS/USD | 63.054 | 0.00222 | +1.18% | 0.69x |
| 3 | GBP/USD | 58.811 | 1.31063 | +0.00% | 0.45x |
| 4 | VVV/USD | 56.402 | 24.639 | -0.52% | 0.75x |
| 5 | LUNA/USD | 50.480 | 4.579e-05 | +1.48% | 1.69x |
| 6 | NIGHT/USD | 47.511 | 0.04887 | -0.10% | 0.59x |
| 7 | PEPE/USD | 44.420 | 3.446e-06 | -0.23% | 0.66x |
| 8 | SKY/USD | 42.304 | 0.04116 | +0.71% | 0.70x |

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

- Persisted scans: 1640; predictions: 14043; observations: 993851.
- Matured sampled outcomes across 1/6/24/48h: 29071; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45510406252 · **Generation:** 1640 · **Legacy run:** 45510406252
**Main quote time:** 2026-11-24T23:32:11.398521+00:00 · **Legacy report time:** 2026-11-24T23:33:26.913841+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 509.22 | 81.65 | -0.12% | 0.63x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 2 | WINGS/USD | 0.00222 | 65.88 | +1.18% | 0.69x | MODERATE 53/100 | EXTREME 94/100 | Do nothing |
| 3 | LUNA/USD ⭐ | 4.579e-05 | 64.73 | +1.48% | 1.69x | STRONG 72/100 | VERY_HIGH 72/100 | Watch |
| 4 | GBP/USD | 1.31063 | 53.37 | +0.00% | 0.45x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 5 | VVV/USD | 24.639 | 51.31 | -0.52% | 0.75x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 6 | NIGHT/USD | 0.04887 | 42.95 | -0.10% | 0.59x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | SKY/USD | 0.04116 | 42.81 | +0.71% | 0.70x | MODERATE 51/100 | VERY_HIGH 75/100 | Watch |
| 8 | PEPE/USD | 3.446e-06 | 39.88 | -0.23% | 0.66x | WEAK 20/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.578e-05 | 71.98 | +1.48% | 1.69x | 1896 | STRONG 86/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
