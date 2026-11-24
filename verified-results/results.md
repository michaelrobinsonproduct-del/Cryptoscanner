# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T11:31:47.408665+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45384652109
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 81444e8791881d03279fd7c9471ca0df76d801ee (atomic ledger/results publication)
**Ledger generation:** 1568 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.617 | 106.256 | 83.590 | +4.78% | +1.53% | 3.14x | 9.8 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.01281 | 106.210 | 82.843 | +11.20% | +1.67% | 3.12x | 7.8 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | GBP/USD | 1.30748 | 72.284 | 57.119 | +0.32% | +0.03% | 4.99x | 0.3 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | DBR/USD | 0.01426 | 62.644 | 57.349 | +6.26% | +1.65% | 0.71x | 35.3 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | XMR/USD | 496.8 | 61.394 | 66.403 | +2.22% | +0.05% | 0.47x | 8.2 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.463e-06 | 55.085 | 56.638 | +1.20% | -0.17% | 0.93x | 5.8 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | LUNA/USD | 4.555e-05 | 54.138 | 64.247 | +4.78% | -0.78% | 0.38x | 2.2 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | NIGHT/USD | 0.04869 | 52.701 | 48.380 | +1.12% | +0.71% | 1.08x | 16.5 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | MODERATE 56/100 | HIGH 68/100 | Watch | WATCH |
| 9 | 2Z/USD | 0.01616 | 49.438 | 50.424 | +3.26% | +0.69% | 0.56x | 6.2 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | BAT/USD | 0.07825 | 38.037 | 39.726 | +1.40% | +0.51% | 0.57x | 5.1 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | BABY/USD | 0.00863 | 25.430 | 31.791 | +1.53% | -1.37% | 1.05x | 23.2 | 2026-11-24T11:31:42.120652+00:00 | Not calibrated | WEAK 13/100 | EXTREME 89/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 83.590 | 25.617 | +1.53% | 3.14x |
| 2 | MON/USD | 82.843 | 0.01281 | +1.67% | 3.12x |
| 3 | XMR/USD | 66.403 | 496.8 | +0.05% | 0.47x |
| 4 | LUNA/USD | 64.247 | 4.555e-05 | -0.78% | 0.38x |
| 5 | DBR/USD | 57.349 | 0.01426 | +1.65% | 0.71x |
| 6 | GBP/USD | 57.119 | 1.30748 | +0.03% | 4.99x |
| 7 | PEPE/USD | 56.638 | 3.463e-06 | -0.17% | 0.93x |
| 8 | 2Z/USD | 50.424 | 0.01616 | +0.69% | 0.56x |
| 9 | NIGHT/USD | 48.380 | 0.04869 | +0.71% | 1.08x |
| 10 | BAT/USD | 39.726 | 0.07825 | +0.51% | 0.57x |
| 11 | BABY/USD | 31.791 | 0.00863 | -1.37% | 1.05x |

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

- Persisted scans: 1568; predictions: 13519; observations: 950010.
- Matured sampled outcomes across 1/6/24/48h: 26039; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45384652109 · **Generation:** 1568 · **Legacy run:** 45384652109
**Main quote time:** 2026-11-24T11:31:47.408665+00:00 · **Legacy report time:** 2026-11-24T11:32:46.683106+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.617 | 106.26 | +1.53% | 3.14x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | MON/USD ⭐ | 0.01281 | 106.21 | +1.67% | 3.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | GBP/USD | 1.30748 | 72.28 | +0.03% | 4.99x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | DBR/USD | 0.01426 | 62.64 | +1.65% | 0.71x | MODERATE 46/100 | EXTREME 94/100 | Do nothing |
| 5 | XMR/USD | 496.8 | 61.39 | +0.05% | 0.47x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 6 | PEPE/USD | 3.463e-06 | 55.09 | -0.17% | 0.93x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 7 | LUNA/USD | 4.555e-05 | 54.14 | -0.78% | 0.38x | WEAK 32/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | NIGHT/USD ⭐ | 0.04869 | 52.70 | +0.71% | 1.08x | MODERATE 66/100 | HIGH 68/100 | Watch |
| 9 | 2Z/USD | 0.01616 | 49.44 | +0.69% | 0.56x | MODERATE 55/100 | VERY_HIGH 82/100 | Watch |
| 10 | BAT/USD | 0.07825 | 38.04 | +0.51% | 0.57x | MODERATE 49/100 | VERY_HIGH 75/100 | Watch |
| 11 | BABY/USD | 0.00863 | 25.43 | -1.37% | 1.05x | WEAK 13/100 | EXTREME 89/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.564 | 100.00 | +1.53% | 3.14x | 14019 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | MON/USD ⭐ | 0.01276 | 90.03 | +1.67% | 3.12x | 10419 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04869 | 49.14 | +0.71% | 1.08x | 12257 | MODERATE 65/100 | HIGH 68/100 | Watch |

**Same-run overlap:** VVV/USD, MON/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
