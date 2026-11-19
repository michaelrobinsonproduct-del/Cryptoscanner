# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T13:10:26.632583+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44530686789
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** a03be82f96a957c7c4fa60b43339b23bcaf31abb (atomic ledger/results publication)
**Ledger generation:** 779 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.983e-06 | 96.540 | 82.292 | +6.33% | -0.15% | 3.71x | 5.0 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 22.862 | 89.384 | 90.629 | +5.50% | -0.10% | 0.92x | 5.7 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 3 | XRP/USD | 0.98923 | 84.153 | 71.508 | +2.37% | +0.14% | 2.20x | 0.1 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5527 | 81.828 | 75.726 | +6.70% | +0.75% | 1.24x | 1.8 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | HYPE/USD | 68.95 | 76.190 | 75.214 | +3.10% | +0.10% | 1.05x | 2.9 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ZEC/USD | 948.81 | 73.738 | 81.975 | +4.04% | +0.02% | 0.16x | 2.6 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.3985 | 72.097 | 74.843 | +3.07% | +0.17% | 0.64x | 3.2 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ETH/USD | 1807.95 | 66.104 | 68.063 | +1.87% | +0.27% | 0.67x | 0.1 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 63850 | 61.050 | 64.611 | +1.37% | -0.02% | 0.65x | 0.0 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SOL/USD | 74.74 | 58.887 | 65.753 | +1.63% | -0.05% | 0.34x | 1.3 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0596023 | 58.271 | 61.953 | +1.53% | +0.04% | 0.61x | 0.2 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ONDO/USD | 0.3057 | 49.129 | 53.266 | +2.70% | +0.08% | 0.55x | 1.0 | 2026-11-19T13:10:20.146968+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 90.629 | 22.862 | -0.10% | 0.92x |
| 2 | PEPE/USD | 82.292 | 3.983e-06 | -0.15% | 3.71x |
| 3 | ZEC/USD | 81.975 | 948.81 | +0.02% | 0.16x |
| 4 | AKT/USD | 75.726 | 0.5527 | +0.75% | 1.24x |
| 5 | HYPE/USD | 75.214 | 68.95 | +0.10% | 1.05x |
| 6 | NEAR/USD | 74.843 | 3.3985 | +0.17% | 0.64x |
| 7 | XRP/USD | 71.508 | 0.98923 | +0.14% | 2.20x |
| 8 | ETH/USD | 68.063 | 1807.95 | +0.27% | 0.67x |
| 9 | SOL/USD | 65.753 | 74.74 | -0.05% | 0.34x |
| 10 | XBT/USD | 64.611 | 63850 | -0.02% | 0.65x |
| 11 | XDG/USD | 61.953 | 0.0596023 | +0.04% | 0.61x |
| 12 | ONDO/USD | 53.266 | 0.3057 | +0.08% | 0.55x |

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

- Persisted scans: 779; predictions: 6492; observations: 471366.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 14940. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44530686789 · **Generation:** 779 · **Legacy run:** 44530686789
**Main quote time:** 2026-11-19T13:10:26.632583+00:00 · **Legacy report time:** 2026-11-19T13:11:18.870082+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.983e-06 | 96.54 | -0.15% | 3.71x | STRONG 78/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD | 22.862 | 89.38 | -0.10% | 0.92x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 3 | XRP/USD ⭐ | 0.98923 | 84.15 | +0.14% | 2.20x | STRONG 97/100 | HIGH 55/100 | Watch |
| 4 | AKT/USD | 0.5527 | 81.83 | +0.75% | 1.24x | STRONG 76/100 | VERY_HIGH 74/100 | Watch |
| 5 | HYPE/USD ⭐ | 68.95 | 76.19 | +0.10% | 1.05x | STRONG 73/100 | HIGH 62/100 | Watch |
| 6 | ZEC/USD | 948.81 | 73.74 | +0.02% | 0.16x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | NEAR/USD | 3.3985 | 72.10 | +0.17% | 0.64x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 8 | ETH/USD | 1807.95 | 66.10 | +0.27% | 0.67x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 63850 | 61.05 | -0.02% | 0.65x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | SOL/USD | 74.74 | 58.89 | -0.05% | 0.34x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XDG/USD | 0.0596023 | 58.27 | +0.04% | 0.61x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | ONDO/USD | 0.3057 | 49.13 | +0.08% | 0.55x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 68.91 | 86.01 | +0.10% | 1.05x | 14621 | STRONG 78/100 | HIGH 62/100 | Watch |
| 2 | XRP/USD ⭐ | 0.98932 | 83.06 | +0.14% | 2.20x | 34475 | STRONG 97/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
