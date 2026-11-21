# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T23:01:09.348464+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44959524204
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 36304588f2018bf59eb191f99608a29ab5824383 (atomic ledger/results publication)
**Ledger generation:** 1198 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 488.65 | 88.050 | 96.217 | +7.09% | -0.08% | 0.22x | 7.6 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | UNI/USD | 4.7081 | 87.554 | 90.643 | +5.39% | +0.13% | 0.63x | 4.0 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | QNT/USD | 142.97 | 84.632 | 70.994 | +3.03% | -0.27% | 2.73x | 10.5 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04469 | 79.323 | 85.314 | +5.85% | -0.25% | 0.52x | 6.7 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ETH/USD | 1676.62 | 74.018 | 79.740 | +3.54% | +0.01% | 0.42x | 0.1 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PEARL/USD | 1.9551 | 73.876 | 73.432 | +6.94% | -0.46% | 1.28x | 29.2 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | XBT/USD | 60014.7 | 69.674 | 69.375 | +2.05% | -0.07% | 1.06x | 0.0 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ADA/USD | 0.144014 | 69.548 | 59.558 | +0.81% | -0.06% | 2.03x | 2.3 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 9 | TAO/USD | 185.7305 | 69.386 | 72.135 | +2.89% | +0.20% | 0.62x | 6.2 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ZEC/USD | 781.47 | 67.284 | 75.287 | +3.11% | -0.15% | 0.28x | 2.9 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SOL/USD | 70.07 | 67.179 | 68.142 | +1.98% | +0.10% | 0.85x | 1.4 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XRP/USD | 0.92558 | 66.790 | 67.941 | +1.86% | -0.06% | 0.92x | 0.1 | 2026-11-21T23:01:03.679495+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 96.217 | 488.65 | -0.08% | 0.22x |
| 2 | UNI/USD | 90.643 | 4.7081 | +0.13% | 0.63x |
| 3 | NIGHT/USD | 85.314 | 0.04469 | -0.25% | 0.52x |
| 4 | ETH/USD | 79.740 | 1676.62 | +0.01% | 0.42x |
| 5 | ZEC/USD | 75.287 | 781.47 | -0.15% | 0.28x |
| 6 | PEARL/USD | 73.432 | 1.9551 | -0.46% | 1.28x |
| 7 | TAO/USD | 72.135 | 185.7305 | +0.20% | 0.62x |
| 8 | QNT/USD | 70.994 | 142.97 | -0.27% | 2.73x |
| 9 | XBT/USD | 69.375 | 60014.7 | -0.07% | 1.06x |
| 10 | SOL/USD | 68.142 | 70.07 | +0.10% | 0.85x |
| 11 | XRP/USD | 67.941 | 0.92558 | -0.06% | 0.92x |
| 12 | ADA/USD | 59.558 | 0.144014 | -0.06% | 2.03x |

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

- Persisted scans: 1198; predictions: 9685; observations: 724743.
- Matured sampled outcomes across 1/6/24/48h: 12989; gap abstentions: 21590. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44959524204 · **Generation:** 1198 · **Legacy run:** 44959524204
**Main quote time:** 2026-11-21T23:01:09.348464+00:00 · **Legacy report time:** 2026-11-21T23:02:16.423143+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 488.65 | 88.05 | -0.08% | 0.22x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 2 | UNI/USD | 4.7081 | 87.55 | +0.13% | 0.63x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 3 | QNT/USD | 142.97 | 84.63 | -0.27% | 2.73x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 4 | NIGHT/USD | 0.04469 | 79.32 | -0.25% | 0.52x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 5 | ETH/USD | 1676.62 | 74.02 | +0.01% | 0.42x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 6 | PEARL/USD | 1.9551 | 73.88 | -0.46% | 1.28x | WEAK 37/100 | VERY_HIGH 73/100 | Watch |
| 7 | XBT/USD | 60014.7 | 69.67 | -0.07% | 1.06x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 8 | ADA/USD | 0.144014 | 69.55 | -0.06% | 2.03x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 9 | TAO/USD | 185.7305 | 69.39 | +0.20% | 0.62x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 10 | ZEC/USD | 781.47 | 67.28 | -0.15% | 0.28x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 11 | SOL/USD | 70.07 | 67.18 | +0.10% | 0.85x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 12 | XRP/USD | 0.92558 | 66.79 | -0.06% | 0.92x | WEAK 38/100 | HIGH 68/100 | Watch |

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
