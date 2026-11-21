# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T16:10:52.724629+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44923009494
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** 5ff6a10a2a3f97c536d21e3bd33bd2fb05193c58 (atomic ledger/results publication)
**Ledger generation:** 1155 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SHX/USD | 0.00352 | 82.946 | 65.232 | +4.98% | +0.54% | 9.40x | 2.8 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | STRONG 96/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.6942 | 79.325 | 88.762 | +5.08% | -0.17% | 0.14x | 3.6 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | XMR/USD | 475.08 | 77.273 | 79.826 | +4.12% | -0.56% | 1.02x | 8.0 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.0816 | 74.771 | 75.520 | +9.53% | -0.68% | 1.27x | 18.4 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | WEAK 42/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ETH/USD | 1677.66 | 73.112 | 80.189 | +3.60% | -0.32% | 0.45x | 0.1 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ZEC/USD | 787.76 | 72.271 | 80.347 | +3.94% | -0.49% | 0.44x | 4.4 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | BEAM/USD | 0.003589 | 71.743 | 71.280 | +9.49% | +0.34% | 0.88x | 11.2 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | TAO/USD | 186.8648 | 69.571 | 76.407 | +3.52% | -0.30% | 0.47x | 6.5 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SOL/USD | 70.16 | 63.581 | 69.059 | +2.11% | -0.31% | 0.61x | 1.4 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.92382 | 61.206 | 66.423 | +1.66% | +0.16% | 0.40x | 0.4 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 59758.9 | 59.490 | 66.330 | +1.62% | -0.22% | 0.42x | 0.0 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | QNT/USD | 140.01 | 59.033 | 60.234 | +0.90% | +0.42% | 0.67x | 2.1 | 2026-11-21T16:10:45.031062+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 88.762 | 4.6942 | -0.17% | 0.14x |
| 2 | ZEC/USD | 80.347 | 787.76 | -0.49% | 0.44x |
| 3 | ETH/USD | 80.189 | 1677.66 | -0.32% | 0.45x |
| 4 | XMR/USD | 79.826 | 475.08 | -0.56% | 1.02x |
| 5 | TAO/USD | 76.407 | 186.8648 | -0.30% | 0.47x |
| 6 | USELESS/USD | 75.520 | 0.0816 | -0.68% | 1.27x |
| 7 | BEAM/USD | 71.280 | 0.003589 | +0.34% | 0.88x |
| 8 | SOL/USD | 69.059 | 70.16 | -0.31% | 0.61x |
| 9 | XRP/USD | 66.423 | 0.92382 | +0.16% | 0.40x |
| 10 | XBT/USD | 66.330 | 59758.9 | -0.22% | 0.42x |
| 11 | SHX/USD | 65.232 | 0.00352 | +0.54% | 9.40x |
| 12 | QNT/USD | 60.234 | 140.01 | +0.42% | 0.67x |

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

- Persisted scans: 1155; predictions: 9169; observations: 698599.
- Matured sampled outcomes across 1/6/24/48h: 12060; gap abstentions: 20750. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44923009494 · **Generation:** 1155 · **Legacy run:** 44923009494
**Main quote time:** 2026-11-21T16:10:52.724629+00:00 · **Legacy report time:** 2026-11-21T16:11:45.715227+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SHX/USD ⭐ | 0.00352 | 82.95 | +0.54% | 9.40x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | UNI/USD | 4.6942 | 79.33 | -0.17% | 0.14x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 3 | XMR/USD | 475.08 | 77.27 | -0.56% | 1.02x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 4 | USELESS/USD | 0.0816 | 74.77 | -0.68% | 1.27x | WEAK 42/100 | HIGH 67/100 | Watch |
| 5 | ETH/USD | 1677.66 | 73.11 | -0.32% | 0.45x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | ZEC/USD | 787.76 | 72.27 | -0.49% | 0.44x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 7 | BEAM/USD | 0.003589 | 71.74 | +0.34% | 0.88x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 8 | TAO/USD | 186.8648 | 69.57 | -0.30% | 0.47x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 9 | SOL/USD | 70.16 | 63.58 | -0.31% | 0.61x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.92382 | 61.21 | +0.16% | 0.40x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 59758.9 | 59.49 | -0.22% | 0.42x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | QNT/USD | 140.01 | 59.03 | +0.42% | 0.67x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SHX/USD ⭐ | 0.003509 | 90.00 | +0.54% | 9.40x | 2765 | STRONG 100/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SHX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
