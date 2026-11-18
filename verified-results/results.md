# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:00:13.988372+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44330415240
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 7272711a784014ee4eb45f7cf11b22c2e6e534b6 (atomic ledger/results publication)
**Ledger generation:** 595 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 10s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1222 | 85.340 | 63.706 | +8.14% | +1.33% | 2.66x | 24.6 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | STRONG 88/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | XRP/USD | 0.98521 | 72.707 | 55.285 | +0.27% | +0.48% | 8.75x | 3.2 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SENT/USD | 0.019699 | 71.503 | 65.621 | +5.52% | +0.28% | 1.45x | 8.1 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | STRONG 81/100 | HIGH 67/100 | Watch | WATCH |
| 4 | MNT/USD | 0.3867 | 70.707 | 52.977 | +3.59% | +0.55% | 5.12x | 10.3 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | STRONG 85/100 | HIGH 66/100 | Consider small entry | WATCH |
| 5 | VVV/USD | 21.107 | 62.967 | 48.015 | +0.39% | -0.01% | 3.40x | 6.6 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 6 | STABLE/USD | 0.02306 | 62.025 | 65.143 | +9.55% | -0.22% | 0.80x | 21.7 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | WEAK 26/100 | EXTREME 92/100 | Do nothing | WATCH |
| 7 | NIGHT/USD | 0.04567 | 61.761 | 56.844 | +1.74% | -2.02% | 2.72x | 6.6 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | MODERATE 61/100 | HIGH 65/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5192 | 60.534 | 43.114 | +1.94% | +0.48% | 2.55x | 5.8 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 9 | TRX/USD | 0.309771 | 59.048 | 45.055 | +0.61% | +0.20% | 2.30x | 0.5 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 10 | CC/USD | 0.0829 | 55.250 | 39.222 | +0.94% | +0.21% | 8.85x | 6.0 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 11 | AKE/USD | 0.0105445 | 54.408 | 57.572 | +5.61% | +0.86% | 0.25x | 30.7 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | ZAMA/USD | 0.06088 | 40.108 | 37.781 | +1.59% | +0.26% | 1.10x | 9.9 | 2026-11-18T15:00:04.437926+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 65.621 | 0.019699 | +0.28% | 1.45x |
| 2 | STABLE/USD | 65.143 | 0.02306 | -0.22% | 0.80x |
| 3 | CT/USD | 63.706 | 0.1222 | +1.33% | 2.66x |
| 4 | AKE/USD | 57.572 | 0.0105445 | +0.86% | 0.25x |
| 5 | NIGHT/USD | 56.844 | 0.04567 | -2.02% | 2.72x |
| 6 | XRP/USD | 55.285 | 0.98521 | +0.48% | 8.75x |
| 7 | MNT/USD | 52.977 | 0.3867 | +0.55% | 5.12x |
| 8 | VVV/USD | 48.015 | 21.107 | -0.01% | 3.40x |
| 9 | TRX/USD | 45.055 | 0.309771 | +0.20% | 2.30x |
| 10 | AKT/USD | 43.114 | 0.5192 | +0.48% | 2.55x |
| 11 | CC/USD | 39.222 | 0.0829 | +0.21% | 8.85x |
| 12 | ZAMA/USD | 37.781 | 0.06088 | +0.26% | 1.10x |

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

- Persisted scans: 595; predictions: 5077; observations: 359362.
- Matured sampled outcomes across 1/6/24/48h: 4286; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44330415240 · **Generation:** 595 · **Legacy run:** 44330415240
**Main quote time:** 2026-11-18T15:00:13.988372+00:00 · **Legacy report time:** 2026-11-18T15:00:35.741247+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1222 | 85.34 | +1.33% | 2.66x | STRONG 98/100 | VERY_HIGH 79/100 | Watch |
| 2 | XRP/USD ⭐ | 0.98521 | 72.71 | +0.48% | 8.75x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD ⭐ | 0.019699 | 71.50 | +0.28% | 1.45x | STRONG 91/100 | HIGH 67/100 | Watch |
| 4 | MNT/USD ⭐ | 0.3867 | 70.71 | +0.55% | 5.12x | STRONG 95/100 | HIGH 66/100 | Consider small entry |
| 5 | VVV/USD | 21.107 | 62.97 | -0.01% | 3.40x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 6 | STABLE/USD | 0.02306 | 62.03 | -0.22% | 0.80x | WEAK 26/100 | EXTREME 92/100 | Do nothing |
| 7 | NIGHT/USD | 0.04567 | 61.76 | -2.02% | 2.72x | MODERATE 61/100 | HIGH 65/100 | Do nothing |
| 8 | AKT/USD ⭐ | 0.5192 | 60.53 | +0.48% | 2.55x | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 9 | TRX/USD ⭐ | 0.309771 | 59.05 | +0.20% | 2.30x | STRONG 85/100 | HIGH 55/100 | Watch |
| 10 | CC/USD ⭐ | 0.0829 | 55.25 | +0.21% | 8.85x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 11 | AKE/USD | 0.0105445 | 54.41 | +0.86% | 0.25x | MODERATE 47/100 | EXTREME 87/100 | Do nothing |
| 12 | ZAMA/USD ⭐ | 0.06088 | 40.11 | +0.26% | 1.10x | MODERATE 65/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019716 | 73.27 | +0.28% | 1.45x | 5772 | STRONG 87/100 | VERY_HIGH 73/100 | Watch |
| 2 | MNT/USD ⭐ | 0.3871 | 72.53 | +0.55% | 5.12x | 2006 | STRONG 91/100 | VERY_HIGH 72/100 | Watch |
| 3 | CT/USD ⭐ | 0.1222 | 69.45 | +1.33% | 2.66x | 1230 | STRONG 90/100 | VERY_HIGH 79/100 | Watch |
| 4 | XRP/USD ⭐ | 0.98752 | 64.10 | +0.48% | 8.75x | 36161 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 5 | AKT/USD ⭐ | 0.5203 | 57.00 | +0.48% | 2.55x | 4702 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 6 | ZAMA/USD ⭐ | 0.06097 | 56.71 | +0.26% | 1.10x | 3501 | STRONG 73/100 | VERY_HIGH 74/100 | Watch |
| 7 | CC/USD ⭐ | 0.083 | 54.51 | +0.21% | 8.85x | 4813 | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 8 | TRX/USD ⭐ | 0.309878 | 52.29 | +0.20% | 2.30x | 4245 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** CT/USD, XRP/USD, SENT/USD, MNT/USD, AKT/USD, TRX/USD, CC/USD, ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
