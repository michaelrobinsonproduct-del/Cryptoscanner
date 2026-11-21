# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T16:50:55.543431+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44926673070
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** 34e796c05df4e808b84828db20e21dbc0586e249 (atomic ledger/results publication)
**Ledger generation:** 1160 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 480.66 | 96.873 | 87.493 | +5.34% | +0.92% | 1.48x | 9.8 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 2 | UNI/USD | 4.7278 | 92.353 | 93.401 | +5.83% | +0.11% | 0.84x | 4.9 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 3 | ZEC/USD | 786.68 | 91.571 | 79.601 | +3.80% | +0.14% | 2.13x | 3.9 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 4 | TAO/USD | 186.3894 | 89.267 | 74.266 | +3.26% | +0.00% | 3.28x | 7.1 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04387 | 85.656 | 71.157 | +3.91% | +1.18% | 1.86x | 4.6 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | ETH/USD | 1682.18 | 84.302 | 82.143 | +3.88% | +0.06% | 1.19x | 0.1 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XRP/USD | 0.92945 | 76.078 | 70.330 | +2.28% | +0.10% | 1.53x | 1.3 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SOL/USD | 70.57 | 71.969 | 72.532 | +2.71% | +0.23% | 0.83x | 2.8 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XBT/USD | 60032.5 | 66.730 | 69.587 | +2.08% | +0.10% | 0.66x | 0.0 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | PAXG/USD | 3545.88 | 63.483 | 57.035 | +0.41% | +0.05% | 1.62x | 0.9 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128296 | 63.078 | 59.545 | +0.86% | +0.18% | 1.26x | 3.0 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | MODERATE 57/100 | HIGH 55/100 | Watch | WATCH |
| 12 | CT/USD | 0.1327 | 62.253 | 69.029 | +9.58% | -0.08% | 0.36x | 15.1 | 2026-11-21T16:50:47.205229+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 93.401 | 4.7278 | +0.11% | 0.84x |
| 2 | XMR/USD | 87.493 | 480.66 | +0.92% | 1.48x |
| 3 | ETH/USD | 82.143 | 1682.18 | +0.06% | 1.19x |
| 4 | ZEC/USD | 79.601 | 786.68 | +0.14% | 2.13x |
| 5 | TAO/USD | 74.266 | 186.3894 | +0.00% | 3.28x |
| 6 | SOL/USD | 72.532 | 70.57 | +0.23% | 0.83x |
| 7 | NIGHT/USD | 71.157 | 0.04387 | +1.18% | 1.86x |
| 8 | XRP/USD | 70.330 | 0.92945 | +0.10% | 1.53x |
| 9 | XBT/USD | 69.587 | 60032.5 | +0.10% | 0.66x |
| 10 | CT/USD | 69.029 | 0.1327 | -0.08% | 0.36x |
| 11 | XLM/USD | 59.545 | 0.128296 | +0.18% | 1.26x |
| 12 | PAXG/USD | 57.035 | 3545.88 | +0.05% | 1.62x |

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

- Persisted scans: 1160; predictions: 9229; observations: 701639.
- Matured sampled outcomes across 1/6/24/48h: 12138; gap abstentions: 20840. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44926673070 · **Generation:** 1160 · **Legacy run:** 44926673070
**Main quote time:** 2026-11-21T16:50:55.543431+00:00 · **Legacy report time:** 2026-11-21T16:51:48.560540+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 480.66 | 96.87 | +0.92% | 1.48x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | UNI/USD | 4.7278 | 92.35 | +0.11% | 0.84x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 3 | ZEC/USD ⭐ | 786.68 | 91.57 | +0.14% | 2.13x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | TAO/USD | 186.3894 | 89.27 | +0.00% | 3.28x | STRONG 90/100 | HIGH 55/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.04387 | 85.66 | +1.18% | 1.86x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 6 | ETH/USD ⭐ | 1682.18 | 84.30 | +0.06% | 1.19x | STRONG 77/100 | HIGH 62/100 | Watch |
| 7 | XRP/USD ⭐ | 0.92945 | 76.08 | +0.10% | 1.53x | STRONG 83/100 | HIGH 55/100 | Watch |
| 8 | SOL/USD | 70.57 | 71.97 | +0.23% | 0.83x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 9 | XBT/USD | 60032.5 | 66.73 | +0.10% | 0.66x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 10 | PAXG/USD | 3545.88 | 63.48 | +0.05% | 1.62x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 11 | XLM/USD | 0.128296 | 63.08 | +0.18% | 1.26x | MODERATE 57/100 | HIGH 55/100 | Watch |
| 12 | CT/USD | 0.1327 | 62.25 | -0.08% | 0.36x | WEAK 31/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1682.37 | 99.52 | +0.06% | 1.19x | 88729 | STRONG 85/100 | HIGH 62/100 | Watch |
| 2 | ZEC/USD ⭐ | 786.38 | 92.34 | +0.14% | 2.13x | 49875 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD ⭐ | 480.66 | 89.67 | +0.92% | 1.48x | 12719 | STRONG 95/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD ⭐ | 0.04377 | 83.95 | +1.18% | 1.86x | 11185 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.9279 | 78.23 | +0.10% | 1.53x | 63234 | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | PIEVERSE/USD | 3.1304 | 77.31 | +1.77% | 1.79x | 2252 | STRONG 79/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** XMR/USD, ZEC/USD, NIGHT/USD, ETH/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
