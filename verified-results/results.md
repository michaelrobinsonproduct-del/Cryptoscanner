# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:00:29.995394+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44624234171
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** de855415114c6f44fb3fba9e12a3614e648a3a30 (atomic ledger/results publication)
**Ledger generation:** 865 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05975 | 71.722 | 56.219 | +6.70% | +0.10% | 2.71x | 42.0 | 2026-11-19T22:00:25.596425+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.779e-05 | 66.094 | 72.788 | +9.76% | +0.00% | 0.33x | 18.9 | 2026-11-19T22:00:25.596425+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ALEO/USD | 0.03132 | 64.108 | 64.211 | +4.47% | +0.84% | 0.57x | 12.8 | 2026-11-19T22:00:25.596425+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | CSPR/USD | 0.0017074 | 52.825 | 55.817 | +4.55% | +0.39% | 0.50x | 15.8 | 2026-11-19T22:00:25.596425+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.0981 | 45.856 | 45.932 | +2.66% | +0.07% | 0.96x | 23.5 | 2026-11-19T22:00:25.596425+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 6 | SENT/USD | 0.021178 | 45.442 | 47.200 | +2.78% | -0.01% | 0.83x | 13.2 | 2026-11-19T22:00:25.596425+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5357 | 40.561 | 48.764 | +3.42% | -0.19% | 0.27x | 14.9 | 2026-11-19T22:00:25.596425+00:00 | Not calibrated | WEAK 20/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | SKR/USD | 0.009968 | 30.660 | 34.852 | +3.48% | -0.34% | 0.75x | 41.2 | 2026-11-19T22:00:25.596425+00:00 | Not calibrated | WEAK 5/100 | EXTREME 100/100 | Do nothing | WATCH |
| 9 | XPL/USD | 0.0464 | 12.444 | 18.105 | +0.87% | -0.43% | 0.65x | 43.1 | 2026-11-19T22:00:25.596425+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 72.788 | 4.779e-05 | +0.00% | 0.33x |
| 2 | ALEO/USD | 64.211 | 0.03132 | +0.84% | 0.57x |
| 3 | MEGA/USD | 56.219 | 0.05975 | +0.10% | 2.71x |
| 4 | CSPR/USD | 55.817 | 0.0017074 | +0.39% | 0.50x |
| 5 | AKT/USD | 48.764 | 0.5357 | -0.19% | 0.27x |
| 6 | SENT/USD | 47.200 | 0.021178 | -0.01% | 0.83x |
| 7 | USELESS/USD | 45.932 | 0.0981 | +0.07% | 0.96x |
| 8 | SKR/USD | 34.852 | 0.009968 | -0.34% | 0.75x |
| 9 | XPL/USD | 18.105 | 0.0464 | -0.43% | 0.65x |

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

- Persisted scans: 865; predictions: 7512; observations: 522733.
- Matured sampled outcomes across 1/6/24/48h: 7859; gap abstentions: 15721. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44624234171 · **Generation:** 865 · **Legacy run:** 44624234171
**Main quote time:** 2026-11-19T22:00:29.995394+00:00 · **Legacy report time:** 2026-11-19T22:01:36.830064+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05975 | 71.72 | +0.10% | 2.71x | STRONG 76/100 | VERY_HIGH 82/100 | Watch |
| 2 | LUNA/USD | 4.779e-05 | 66.09 | +0.00% | 0.33x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 3 | ALEO/USD | 0.03132 | 64.11 | +0.84% | 0.57x | MODERATE 57/100 | VERY_HIGH 76/100 | Watch |
| 4 | CSPR/USD | 0.0017074 | 52.83 | +0.39% | 0.50x | MODERATE 51/100 | VERY_HIGH 81/100 | Watch |
| 5 | USELESS/USD | 0.0981 | 45.86 | +0.07% | 0.96x | WEAK 33/100 | VERY_HIGH 74/100 | Do nothing |
| 6 | SENT/USD | 0.021178 | 45.44 | -0.01% | 0.83x | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | AKT/USD | 0.5357 | 40.56 | -0.19% | 0.27x | WEAK 20/100 | EXTREME 87/100 | Do nothing |
| 8 | SKR/USD | 0.009968 | 30.66 | -0.34% | 0.75x | WEAK 5/100 | EXTREME 100/100 | Do nothing |
| 9 | XPL/USD | 0.0464 | 12.44 | -0.43% | 0.65x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05997 | 74.62 | +0.10% | 2.71x | 2181 | STRONG 82/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
