# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T11:50:38.401011+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44900928739
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** f037173b4d7f18359f59a4b6848775c596764b7b (atomic ledger/results publication)
**Ledger generation:** 1129 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.944 | 101.602 | 92.480 | +5.81% | -1.18% | 2.57x | 6.4 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | STRONG 80/100 | HIGH 65/100 | Watch | WATCH |
| 2 | ETH/USD | 1650.79 | 81.582 | 68.574 | +1.94% | -0.40% | 4.64x | 0.1 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 470.45 | 72.928 | 72.685 | +3.10% | +0.09% | 0.98x | 8.1 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ZEC/USD | 763.48 | 72.013 | 58.047 | +0.73% | -0.21% | 7.54x | 4.2 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 5 | UNI/USD | 4.5005 | 69.127 | 58.212 | +0.75% | -0.06% | 2.12x | 4.0 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | TRX/USD | 0.302943 | 50.626 | 57.829 | +0.48% | -0.22% | 0.39x | 1.0 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | AAVE/USD | 98.97 | 46.893 | 50.615 | +1.10% | -0.17% | 0.71x | 6.1 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5056 | 45.285 | 32.647 | +0.34% | -0.47% | 3.44x | 5.9 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 9 | SKY/USD | 0.04465 | 34.045 | 44.044 | +1.85% | -0.65% | 0.32x | 6.7 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | SENT/USD | 0.020973 | 32.325 | 40.050 | +1.84% | -0.14% | 0.30x | 7.6 | 2026-11-21T11:50:30.503993+00:00 | Not calibrated | WEAK 21/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 92.480 | 21.944 | -1.18% | 2.57x |
| 2 | XMR/USD | 72.685 | 470.45 | +0.09% | 0.98x |
| 3 | ETH/USD | 68.574 | 1650.79 | -0.40% | 4.64x |
| 4 | UNI/USD | 58.212 | 4.5005 | -0.06% | 2.12x |
| 5 | ZEC/USD | 58.047 | 763.48 | -0.21% | 7.54x |
| 6 | TRX/USD | 57.829 | 0.302943 | -0.22% | 0.39x |
| 7 | AAVE/USD | 50.615 | 98.97 | -0.17% | 0.71x |
| 8 | SKY/USD | 44.044 | 0.04465 | -0.65% | 0.32x |
| 9 | SENT/USD | 40.050 | 0.020973 | -0.14% | 0.30x |
| 10 | AKT/USD | 32.647 | 0.5056 | -0.47% | 3.44x |

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

- Persisted scans: 1129; predictions: 8861; observations: 682791.
- Matured sampled outcomes across 1/6/24/48h: 11660; gap abstentions: 20358. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 13 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44900928739 · **Generation:** 1129 · **Legacy run:** 44900928739
**Main quote time:** 2026-11-21T11:50:38.401011+00:00 · **Legacy report time:** 2026-11-21T11:51:17.705590+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.944 | 101.60 | -1.18% | 2.57x | STRONG 80/100 | HIGH 65/100 | Watch |
| 2 | ETH/USD | 1650.79 | 81.58 | -0.40% | 4.64x | STRONG 71/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 470.45 | 72.93 | +0.09% | 0.98x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 4 | ZEC/USD | 763.48 | 72.01 | -0.21% | 7.54x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.5005 | 69.13 | -0.06% | 2.12x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | TRX/USD | 0.302943 | 50.63 | -0.22% | 0.39x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | AAVE/USD | 98.97 | 46.89 | -0.17% | 0.71x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | AKT/USD | 0.5056 | 45.28 | -0.47% | 3.44x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 9 | SKY/USD | 0.04465 | 34.05 | -0.65% | 0.32x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | SENT/USD | 0.020973 | 32.32 | -0.14% | 0.30x | WEAK 21/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD | 0.001797 | 66.77 | +6.96% | 1.12x | 7680 | MODERATE 68/100 | VERY_HIGH 77/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
