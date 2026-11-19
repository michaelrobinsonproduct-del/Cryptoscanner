# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:45:29.874192+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44631439312
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 4bf3833d04762d11ac1137d9de390a2160668ea4 (atomic ledger/results publication)
**Ledger generation:** 873 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05975 | 79.701 | 68.850 | +6.70% | -0.83% | 2.97x | 16.7 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | VVV/USD | 21.953 | 73.571 | 61.835 | +1.30% | -0.16% | 2.25x | 4.5 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | CT/USD | 0.1291 | 71.287 | 65.143 | +9.22% | +1.02% | 1.11x | 23.3 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.09987 | 69.807 | 69.272 | +4.51% | -0.78% | 1.45x | 5.0 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ADA/USD | 0.151878 | 64.775 | 55.483 | +0.41% | -0.08% | 1.97x | 4.8 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SKR/USD | 0.010063 | 62.045 | 61.894 | +4.46% | +0.25% | 0.89x | 1.0 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | SENT/USD | 0.021651 | 61.247 | 67.441 | +5.08% | +0.52% | 0.12x | 5.1 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5387 | 60.488 | 56.613 | +4.00% | -0.24% | 1.51x | 7.4 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | MODERATE 50/100 | HIGH 66/100 | Watch | WATCH |
| 9 | TRX/USD | 0.310471 | 60.164 | 44.699 | +0.38% | +0.09% | 5.14x | 0.5 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 10 | INJ/USD | 7.083 | 48.533 | 52.298 | +1.46% | +0.23% | 0.51x | 7.1 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PYTH/USD | 0.0531 | 29.670 | 33.984 | +0.64% | +0.06% | 0.54x | 7.5 | 2026-11-19T22:45:21.751385+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | USELESS/USD | 69.272 | 0.09987 | -0.78% | 1.45x |
| 2 | MEGA/USD | 68.850 | 0.05975 | -0.83% | 2.97x |
| 3 | SENT/USD | 67.441 | 0.021651 | +0.52% | 0.12x |
| 4 | CT/USD | 65.143 | 0.1291 | +1.02% | 1.11x |
| 5 | SKR/USD | 61.894 | 0.010063 | +0.25% | 0.89x |
| 6 | VVV/USD | 61.835 | 21.953 | -0.16% | 2.25x |
| 7 | AKT/USD | 56.613 | 0.5387 | -0.24% | 1.51x |
| 8 | ADA/USD | 55.483 | 0.151878 | -0.08% | 1.97x |
| 9 | INJ/USD | 52.298 | 7.083 | +0.23% | 0.51x |
| 10 | TRX/USD | 44.699 | 0.310471 | +0.09% | 5.14x |
| 11 | PYTH/USD | 33.984 | 0.0531 | +0.06% | 0.54x |

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

- Persisted scans: 873; predictions: 7595; observations: 527548.
- Matured sampled outcomes across 1/6/24/48h: 8022; gap abstentions: 15756. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44631439312 · **Generation:** 873 · **Legacy run:** 44631439312
**Main quote time:** 2026-11-19T22:45:29.874192+00:00 · **Legacy report time:** 2026-11-19T22:46:22.350378+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.05975 | 79.70 | -0.83% | 2.97x | MODERATE 65/100 | VERY_HIGH 72/100 | Watch |
| 2 | VVV/USD | 21.953 | 73.57 | -0.16% | 2.25x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | CT/USD ⭐ | 0.1291 | 71.29 | +1.02% | 1.11x | STRONG 71/100 | VERY_HIGH 79/100 | Watch |
| 4 | USELESS/USD | 0.09987 | 69.81 | -0.78% | 1.45x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 5 | ADA/USD | 0.151878 | 64.77 | -0.08% | 1.97x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 6 | SKR/USD | 0.010063 | 62.05 | +0.25% | 0.89x | MODERATE 61/100 | VERY_HIGH 74/100 | Watch |
| 7 | SENT/USD | 0.021651 | 61.25 | +0.52% | 0.12x | MODERATE 61/100 | VERY_HIGH 75/100 | Watch |
| 8 | AKT/USD | 0.5387 | 60.49 | -0.24% | 1.51x | MODERATE 50/100 | HIGH 66/100 | Watch |
| 9 | TRX/USD | 0.310471 | 60.16 | +0.09% | 5.14x | STRONG 75/100 | HIGH 55/100 | Watch |
| 10 | INJ/USD | 7.083 | 48.53 | +0.23% | 0.51x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 11 | PYTH/USD | 0.0531 | 29.67 | +0.06% | 0.54x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1291 | 71.23 | +1.02% | 1.11x | 2242 | STRONG 71/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
