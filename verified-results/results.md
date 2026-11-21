# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T01:00:28.745846+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44847393570
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 7cc45ff46db6a4e7dfb49509bc1893490e8bbd58 (atomic ledger/results publication)
**Ledger generation:** 1051 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.00243 | 63.833 | 45.311 | +0.41% | +0.70% | 4.02x | 12.3 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | STRONG 82/100 | HIGH 61/100 | Watch | WATCH |
| 2 | KAS/USD | 0.02613 | 54.532 | 36.646 | +0.58% | +0.58% | 3.66x | 11.5 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 3 | BLUR/USD | 0.00741 | 51.560 | 35.780 | +1.51% | +1.64% | 1.76x | 13.5 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | MODERATE 66/100 | HIGH 66/100 | Watch | WATCH |
| 4 | CC/USD | 0.07497 | 50.663 | 35.795 | +0.56% | +0.60% | 2.18x | 9.3 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 5 | VVV/USD | 20.89 | 50.388 | 55.313 | +0.73% | +0.57% | 0.23x | 9.6 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AKE/USD | 0.00618228 | 49.325 | 46.795 | +1.16% | +0.81% | 0.85x | 32.7 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | PIEVERSE/USD | 3.032 | 48.715 | 35.662 | +1.11% | -0.39% | 8.02x | 13.9 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | PEARL/USD | 1.8794 | 47.583 | 56.488 | +2.79% | -1.55% | 0.88x | 23.9 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 9 | RENDER/USD | 1.278 | 31.752 | 37.115 | +0.39% | +0.31% | 0.31x | 7.8 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | CAP/USD | 0.09225 | 31.606 | 34.068 | +0.77% | +0.27% | 0.62x | 8.0 | 2026-11-21T01:00:20.747778+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 56.488 | 1.8794 | -1.55% | 0.88x |
| 2 | VVV/USD | 55.313 | 20.89 | +0.57% | 0.23x |
| 3 | AKE/USD | 46.795 | 0.00618228 | +0.81% | 0.85x |
| 4 | PUMP/USD | 45.311 | 0.00243 | +0.70% | 4.02x |
| 5 | RENDER/USD | 37.115 | 1.278 | +0.31% | 0.31x |
| 6 | KAS/USD | 36.646 | 0.02613 | +0.58% | 3.66x |
| 7 | CC/USD | 35.795 | 0.07497 | +0.60% | 2.18x |
| 8 | BLUR/USD | 35.780 | 0.00741 | +1.64% | 1.76x |
| 9 | PIEVERSE/USD | 35.662 | 3.032 | -0.39% | 8.02x |
| 10 | CAP/USD | 34.068 | 0.09225 | +0.27% | 0.62x |

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

- Persisted scans: 1051; predictions: 8417; observations: 635368.
- Matured sampled outcomes across 1/6/24/48h: 10933; gap abstentions: 19090. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44847393570 · **Generation:** 1051 · **Legacy run:** 44847393570
**Main quote time:** 2026-11-21T01:00:28.745846+00:00 · **Legacy report time:** 2026-11-21T01:01:14.544746+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.00243 | 63.83 | +0.70% | 4.02x | STRONG 92/100 | HIGH 61/100 | Consider small entry |
| 2 | KAS/USD | 0.02613 | 54.53 | +0.58% | 3.66x | STRONG 77/100 | HIGH 61/100 | Watch |
| 3 | BLUR/USD | 0.00741 | 51.56 | +1.64% | 1.76x | MODERATE 66/100 | HIGH 66/100 | Watch |
| 4 | CC/USD | 0.07497 | 50.66 | +0.60% | 2.18x | STRONG 80/100 | HIGH 60/100 | Watch |
| 5 | VVV/USD | 20.89 | 50.39 | +0.57% | 0.23x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 6 | AKE/USD | 0.00618228 | 49.33 | +0.81% | 0.85x | MODERATE 45/100 | VERY_HIGH 74/100 | Watch |
| 7 | PIEVERSE/USD | 3.032 | 48.72 | -0.39% | 8.02x | MODERATE 49/100 | VERY_HIGH 72/100 | Watch |
| 8 | PEARL/USD | 1.8794 | 47.58 | -1.55% | 0.88x | WEAK 19/100 | VERY_HIGH 84/100 | Do nothing |
| 9 | RENDER/USD | 1.278 | 31.75 | +0.31% | 0.31x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 10 | CAP/USD | 0.09225 | 31.61 | +0.27% | 0.62x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD | 0.0543423 | 55.98 | +0.22% | 1.46x | 12482 | STRONG 73/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD | 8.54955 | 53.59 | +0.26% | 3.51x | 11044 | STRONG 82/100 | HIGH 55/100 | Watch |
| 3 | PUMP/USD ⭐ | 0.002436 | 51.23 | +0.70% | 4.02x | 7125 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD | 40.64 | 51.20 | +0.32% | 1.27x | 14946 | MODERATE 61/100 | HIGH 55/100 | Watch |
| 5 | UNI/USD | 4.4741 | 38.51 | +0.10% | 1.23x | 9209 | WEAK 44/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
