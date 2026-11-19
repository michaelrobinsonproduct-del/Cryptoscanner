# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:40:25.208570+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44452977672
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 3d12f10373fc71d0cf804ed0c39e725903fca637 (atomic ledger/results publication)
**Ledger generation:** 745 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3509 | 80.239 | 64.418 | +1.62% | +0.16% | 5.33x | 3.9 | 2026-11-19T03:40:16.914085+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 2 | TAO/USD | 192.7249 | 72.910 | 54.561 | +0.40% | +0.67% | 6.95x | 6.5 | 2026-11-19T03:40:16.914085+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LUNA/USD | 4.725e-05 | 64.763 | 68.216 | +8.52% | -0.92% | 1.12x | 19.1 | 2026-11-19T03:40:16.914085+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | VVV/USD | 22.102 | 58.956 | 59.283 | +1.99% | +0.43% | 0.75x | 8.2 | 2026-11-19T03:40:16.914085+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 5 | CC/USD | 0.08223 | 54.130 | 37.177 | +0.43% | +0.39% | 2.60x | 2.4 | 2026-11-19T03:40:16.914085+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 6 | ONDO/USD | 0.29848 | 54.084 | 35.389 | +0.28% | +0.74% | 20.06x | 2.7 | 2026-11-19T03:40:16.914085+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 7 | LTC/USD | 44.17 | 49.634 | 46.547 | +0.36% | +0.27% | 1.17x | 4.5 | 2026-11-19T03:40:16.914085+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 8 | TRX/USD | 0.310156 | 41.232 | 41.803 | +0.28% | +0.09% | 0.90x | 1.0 | 2026-11-19T03:40:16.914085+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 9 | WLD/USD | 0.2611 | 27.561 | 32.051 | +0.27% | +0.38% | 0.36x | 3.8 | 2026-11-19T03:40:16.914085+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 68.216 | 4.725e-05 | -0.92% | 1.12x |
| 2 | NEAR/USD | 64.418 | 3.3509 | +0.16% | 5.33x |
| 3 | VVV/USD | 59.283 | 22.102 | +0.43% | 0.75x |
| 4 | TAO/USD | 54.561 | 192.7249 | +0.67% | 6.95x |
| 5 | LTC/USD | 46.547 | 44.17 | +0.27% | 1.17x |
| 6 | TRX/USD | 41.803 | 0.310156 | +0.09% | 0.90x |
| 7 | CC/USD | 37.177 | 0.08223 | +0.39% | 2.60x |
| 8 | ONDO/USD | 35.389 | 0.29848 | +0.74% | 20.06x |
| 9 | WLD/USD | 32.051 | 0.2611 | +0.38% | 0.36x |

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

- Persisted scans: 745; predictions: 6084; observations: 450712.
- Matured sampled outcomes across 1/6/24/48h: 6053; gap abstentions: 13555. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44452977672 · **Generation:** 745 · **Legacy run:** 44452977672
**Main quote time:** 2026-11-19T03:40:25.208570+00:00 · **Legacy report time:** 2026-11-19T03:41:14.395658+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3509 | 80.24 | +0.16% | 5.33x | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | TAO/USD | 192.7249 | 72.91 | +0.67% | 6.95x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 3 | LUNA/USD | 4.725e-05 | 64.76 | -0.92% | 1.12x | WEAK 37/100 | VERY_HIGH 79/100 | Watch |
| 4 | VVV/USD | 22.102 | 58.96 | +0.43% | 0.75x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 5 | CC/USD | 0.08223 | 54.13 | +0.39% | 2.60x | STRONG 82/100 | HIGH 60/100 | Watch |
| 6 | ONDO/USD | 0.29848 | 54.08 | +0.74% | 20.06x | STRONG 82/100 | HIGH 60/100 | Watch |
| 7 | LTC/USD ⭐ | 44.17 | 49.63 | +0.27% | 1.17x | STRONG 70/100 | HIGH 62/100 | Watch |
| 8 | TRX/USD | 0.310156 | 41.23 | +0.09% | 0.90x | WEAK 41/100 | HIGH 62/100 | Watch |
| 9 | WLD/USD | 0.2611 | 27.56 | +0.38% | 0.36x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.357 | 76.82 | +0.16% | 5.33x | 13694 | STRONG 93/100 | HIGH 55/100 | Watch |
| 2 | SOL/USD | 73.68 | 60.76 | +0.40% | 4.51x | 35157 | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | SUI/USD | 0.72 | 59.98 | +0.31% | 6.26x | 6642 | STRONG 85/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1778.95 | 58.47 | +0.23% | 1.77x | 57933 | STRONG 74/100 | HIGH 55/100 | Watch |
| 5 | LTC/USD ⭐ | 44.23 | 49.76 | +0.27% | 1.17x | 11699 | STRONG 70/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NEAR/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
