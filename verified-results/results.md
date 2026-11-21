# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T12:10:44.635765+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44902499728
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** d484c6c87e094ced4455124752e4231f52368a86 (atomic ledger/results publication)
**Ledger generation:** 1131 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.098 | 99.251 | 98.641 | +6.55% | +0.63% | 0.74x | 2.7 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | STRONG 80/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | XMR/USD | 473.47 | 73.238 | 78.928 | +3.77% | +0.44% | 0.21x | 4.9 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ETH/USD | 1648.22 | 62.424 | 67.463 | +1.78% | -0.06% | 0.53x | 0.1 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | TRX/USD | 0.302683 | 54.412 | 57.721 | +0.39% | -0.11% | 0.72x | 0.0 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | WINGS/USD | 0.001818 | 50.835 | 56.133 | +3.77% | +0.17% | 0.39x | 5.5 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | ZEC/USD | 763.16 | 50.108 | 56.966 | +0.69% | +0.14% | 0.25x | 5.8 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | AAVE/USD | 99.08 | 48.036 | 52.122 | +1.22% | -0.23% | 0.71x | 5.0 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | UNI/USD | 4.4786 | 45.950 | 54.665 | +0.26% | -0.28% | 0.27x | 4.2 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SENT/USD | 0.021039 | 43.378 | 42.045 | +2.16% | +0.67% | 0.80x | 8.1 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 10 | SKY/USD | 0.04456 | 37.163 | 41.317 | +1.64% | -0.22% | 0.70x | 9.0 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | AKT/USD | 0.5059 | 26.087 | 31.076 | +0.40% | +0.30% | 0.35x | 9.9 | 2026-11-21T12:10:38.760477+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 98.641 | 22.098 | +0.63% | 0.74x |
| 2 | XMR/USD | 78.928 | 473.47 | +0.44% | 0.21x |
| 3 | ETH/USD | 67.463 | 1648.22 | -0.06% | 0.53x |
| 4 | TRX/USD | 57.721 | 0.302683 | -0.11% | 0.72x |
| 5 | ZEC/USD | 56.966 | 763.16 | +0.14% | 0.25x |
| 6 | WINGS/USD | 56.133 | 0.001818 | +0.17% | 0.39x |
| 7 | UNI/USD | 54.665 | 4.4786 | -0.28% | 0.27x |
| 8 | AAVE/USD | 52.122 | 99.08 | -0.23% | 0.71x |
| 9 | SENT/USD | 42.045 | 0.021039 | +0.67% | 0.80x |
| 10 | SKY/USD | 41.317 | 0.04456 | -0.22% | 0.70x |
| 11 | AKT/USD | 31.076 | 0.5059 | +0.30% | 0.35x |

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

- Persisted scans: 1131; predictions: 8883; observations: 684007.
- Matured sampled outcomes across 1/6/24/48h: 11685; gap abstentions: 20365. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 15 (sampled only; not a success-rate estimate).
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

**Writer:** 44902499728 · **Generation:** 1131 · **Legacy run:** 44902499728
**Main quote time:** 2026-11-21T12:10:44.635765+00:00 · **Legacy report time:** 2026-11-21T12:11:29.817988+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.098 | 99.25 | +0.63% | 0.74x | STRONG 80/100 | VERY_HIGH 70/100 | Watch |
| 2 | XMR/USD | 473.47 | 73.24 | +0.44% | 0.21x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 3 | ETH/USD | 1648.22 | 62.42 | -0.06% | 0.53x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 4 | TRX/USD | 0.302683 | 54.41 | -0.11% | 0.72x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | WINGS/USD | 0.001818 | 50.84 | +0.17% | 0.39x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |
| 6 | ZEC/USD | 763.16 | 50.11 | +0.14% | 0.25x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 7 | AAVE/USD | 99.08 | 48.04 | -0.23% | 0.71x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | UNI/USD | 4.4786 | 45.95 | -0.28% | 0.27x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SENT/USD | 0.021039 | 43.38 | +0.67% | 0.80x | MODERATE 52/100 | VERY_HIGH 74/100 | Watch |
| 10 | SKY/USD | 0.04456 | 37.16 | -0.22% | 0.70x | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | AKT/USD | 0.5059 | 26.09 | +0.30% | 0.35x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD | 68.79 | 51.84 | +0.06% | 1.29x | 57773 | MODERATE 51/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
