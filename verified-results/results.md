# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:30:21.816616+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44444705223
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 767771224d0649275ecef42f9cf2ec73577bd090 (atomic ledger/results publication)
**Ledger generation:** 731 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021918 | 84.555 | 72.951 | +6.37% | +1.43% | 1.44x | 6.4 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Watch | WATCH |
| 2 | VVV/USD | 22.166 | 82.697 | 63.535 | +2.28% | +0.83% | 3.85x | 2.7 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.3277 | 61.469 | 59.323 | +0.92% | +0.19% | 1.12x | 4.2 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ICP/USD | 2.25 | 50.532 | 52.201 | +3.31% | +0.31% | 0.68x | 17.8 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05783 | 46.442 | 42.859 | +3.27% | -0.28% | 1.50x | 22.6 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | WEAK 33/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | TON/USD | 1.026 | 44.274 | 27.808 | +0.49% | +0.29% | 2.61x | 19.5 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | STRONG 72/100 | HIGH 66/100 | Watch | WATCH |
| 7 | BMT/USD | 0.01963 | 42.407 | 53.441 | +3.97% | -0.81% | 0.30x | 10.2 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | WEAK 21/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | TRX/USD | 0.310165 | 31.920 | 42.074 | +0.29% | -0.16% | 0.07x | 0.0 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | W/USD | 0.00897 | 29.557 | 30.227 | +0.67% | +0.56% | 0.65x | 11.2 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | WEAK 40/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | TRUMP/USD | 0.95 | 29.164 | 33.296 | +0.53% | +0.32% | 0.43x | 10.5 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | DRV/USD | 0.26635 | 27.194 | 35.051 | +0.63% | -0.07% | 0.25x | 5.3 | 2026-11-19T02:30:13.893659+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.951 | 0.021918 | +1.43% | 1.44x |
| 2 | VVV/USD | 63.535 | 22.166 | +0.83% | 3.85x |
| 3 | NEAR/USD | 59.323 | 3.3277 | +0.19% | 1.12x |
| 4 | BMT/USD | 53.441 | 0.01963 | -0.81% | 0.30x |
| 5 | ICP/USD | 52.201 | 2.25 | +0.31% | 0.68x |
| 6 | MEGA/USD | 42.859 | 0.05783 | -0.28% | 1.50x |
| 7 | TRX/USD | 42.074 | 0.310165 | -0.16% | 0.07x |
| 8 | DRV/USD | 35.051 | 0.26635 | -0.07% | 0.25x |
| 9 | TRUMP/USD | 33.296 | 0.95 | +0.32% | 0.43x |
| 10 | W/USD | 30.227 | 0.00897 | +0.56% | 0.65x |
| 11 | TON/USD | 27.808 | 1.026 | +0.29% | 2.61x |

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

- Persisted scans: 731; predictions: 5946; observations: 442186.
- Matured sampled outcomes across 1/6/24/48h: 5887; gap abstentions: 13493. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44444705223 · **Generation:** 731 · **Legacy run:** 44444705223
**Main quote time:** 2026-11-19T02:30:21.816616+00:00 · **Legacy report time:** 2026-11-19T02:30:59.505230+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021918 | 84.56 | +1.43% | 1.44x | STRONG 97/100 | HIGH 67/100 | Watch |
| 2 | VVV/USD ⭐ | 22.166 | 82.70 | +0.83% | 3.85x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.3277 | 61.47 | +0.19% | 1.12x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 4 | ICP/USD | 2.25 | 50.53 | +0.31% | 0.68x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 5 | MEGA/USD | 0.05783 | 46.44 | -0.28% | 1.50x | WEAK 33/100 | EXTREME 85/100 | Do nothing |
| 6 | TON/USD | 1.026 | 44.27 | +0.29% | 2.61x | STRONG 72/100 | HIGH 66/100 | Watch |
| 7 | BMT/USD | 0.01963 | 42.41 | -0.81% | 0.30x | WEAK 21/100 | EXTREME 94/100 | Do nothing |
| 8 | TRX/USD | 0.310165 | 31.92 | -0.16% | 0.07x | WEAK 21/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | W/USD | 0.00897 | 29.56 | +0.56% | 0.65x | WEAK 40/100 | EXTREME 88/100 | Do nothing |
| 10 | TRUMP/USD | 0.95 | 29.16 | +0.32% | 0.43x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 11 | DRV/USD | 0.26635 | 27.19 | -0.07% | 0.25x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021868 | 77.00 | +1.43% | 1.44x | 7805 | STRONG 93/100 | HIGH 67/100 | Watch |
| 2 | VVV/USD ⭐ | 22.087 | 66.84 | +0.83% | 3.85x | 8066 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.3277 | 56.84 | +0.19% | 1.12x | 13222 | MODERATE 63/100 | HIGH 62/100 | Watch |
| 4 | UAI/USD | 0.03376 | 51.11 | +0.66% | 3.24x | 2047 | STRONG 81/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD, VVV/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
