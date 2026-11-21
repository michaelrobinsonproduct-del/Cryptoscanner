# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T13:20:53.160972+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44908285620
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** a4ef06a405153572530c529c756e96468c9dc231 (atomic ledger/results publication)
**Ledger generation:** 1138 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.927 | 97.397 | 96.503 | +10.55% | +0.77% | 0.70x | 7.0 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ZEC/USD | 781.65 | 88.397 | 74.367 | +3.13% | +1.73% | 1.54x | 5.1 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ETH/USD | 1668.86 | 76.172 | 74.617 | +3.06% | +0.36% | 0.97x | 3.6 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 4 | TAO/USD | 184.9898 | 75.021 | 68.818 | +2.48% | +0.92% | 1.16x | 7.1 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 5 | AVAX/USD | 6.539 | 73.024 | 57.021 | +0.51% | +0.60% | 2.30x | 3.1 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | UNI/USD | 4.5122 | 65.246 | 59.059 | +1.01% | +0.76% | 1.24x | 6.0 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XMR/USD | 468.79 | 64.599 | 69.805 | +2.74% | -0.09% | 0.52x | 8.7 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | CT/USD | 0.13 | 63.827 | 64.917 | +7.35% | +1.17% | 0.31x | 23.2 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | USELESS/USD | 0.078 | 63.630 | 63.858 | +4.70% | +1.31% | 0.32x | 18.0 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SOL/USD | 69.5 | 59.418 | 62.329 | +1.15% | +0.46% | 0.48x | 1.4 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | TRX/USD | 0.303392 | 57.606 | 58.740 | +0.63% | +0.13% | 0.82x | 1.3 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XBT/USD | 59124.8 | 57.357 | 58.782 | +0.54% | +0.48% | 0.62x | 0.0 | 2026-11-21T13:20:46.859502+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 96.503 | 22.927 | +0.77% | 0.70x |
| 2 | ETH/USD | 74.617 | 1668.86 | +0.36% | 0.97x |
| 3 | ZEC/USD | 74.367 | 781.65 | +1.73% | 1.54x |
| 4 | XMR/USD | 69.805 | 468.79 | -0.09% | 0.52x |
| 5 | TAO/USD | 68.818 | 184.9898 | +0.92% | 1.16x |
| 6 | CT/USD | 64.917 | 0.13 | +1.17% | 0.31x |
| 7 | USELESS/USD | 63.858 | 0.078 | +1.31% | 0.32x |
| 8 | SOL/USD | 62.329 | 69.5 | +0.46% | 0.48x |
| 9 | UNI/USD | 59.059 | 4.5122 | +0.76% | 1.24x |
| 10 | XBT/USD | 58.782 | 59124.8 | +0.48% | 0.62x |
| 11 | TRX/USD | 58.740 | 0.303392 | +0.13% | 0.82x |
| 12 | AVAX/USD | 57.021 | 6.539 | +0.60% | 2.30x |

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

- Persisted scans: 1138; predictions: 8965; observations: 688263.
- Matured sampled outcomes across 1/6/24/48h: 11753; gap abstentions: 20387. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44908285620 · **Generation:** 1138 · **Legacy run:** 44908285620
**Main quote time:** 2026-11-21T13:20:53.160972+00:00 · **Legacy report time:** 2026-11-21T13:21:56.093908+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.927 | 97.40 | +0.77% | 0.70x | STRONG 79/100 | VERY_HIGH 70/100 | Watch |
| 2 | ZEC/USD ⭐ | 781.65 | 88.40 | +1.73% | 1.54x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD | 1668.86 | 76.17 | +0.36% | 0.97x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 4 | TAO/USD ⭐ | 184.9898 | 75.02 | +0.92% | 1.16x | STRONG 83/100 | HIGH 62/100 | Watch |
| 5 | AVAX/USD | 6.539 | 73.02 | +0.60% | 2.30x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 6 | UNI/USD ⭐ | 4.5122 | 65.25 | +0.76% | 1.24x | STRONG 78/100 | HIGH 62/100 | Watch |
| 7 | XMR/USD | 468.79 | 64.60 | -0.09% | 0.52x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 8 | CT/USD | 0.13 | 63.83 | +1.17% | 0.31x | MODERATE 52/100 | EXTREME 94/100 | Do nothing |
| 9 | USELESS/USD | 0.078 | 63.63 | +1.31% | 0.32x | MODERATE 57/100 | VERY_HIGH 76/100 | Watch |
| 10 | SOL/USD | 69.5 | 59.42 | +0.46% | 0.48x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 11 | TRX/USD | 0.303392 | 57.61 | +0.13% | 0.82x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 12 | XBT/USD | 59124.8 | 57.36 | +0.48% | 0.62x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 785.22 | 98.76 | +1.73% | 1.54x | 57766 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 184.8435 | 69.22 | +0.92% | 1.16x | 16629 | STRONG 80/100 | HIGH 62/100 | Watch |
| 3 | UNI/USD ⭐ | 4.546 | 64.95 | +0.76% | 1.24x | 12641 | STRONG 77/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZEC/USD, TAO/USD, UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
