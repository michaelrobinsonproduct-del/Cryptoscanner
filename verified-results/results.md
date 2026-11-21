# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T17:50:55.699993+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44932141865
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** 607aa456bedf271d5a9bdecd599efbebd6c886c3 (atomic ledger/results publication)
**Ledger generation:** 1166 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.9834 | 104.749 | 77.549 | +8.48% | +2.44% | 5.43x | 27.8 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | STRONG 95/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 481.18 | 99.748 | 87.776 | +5.45% | +0.28% | 2.06x | 10.8 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 4.7178 | 91.431 | 92.891 | +5.61% | -0.24% | 0.97x | 2.8 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XRP/USD | 0.9329 | 85.399 | 73.259 | +2.66% | +0.05% | 2.19x | 0.8 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04551 | 83.409 | 86.517 | +7.79% | +0.71% | 0.34x | 11.0 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | BEAM/USD | 0.003481 | 82.519 | 69.521 | +6.19% | +0.06% | 2.27x | 11.5 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 7 | USELESS/USD | 0.0818 | 75.392 | 75.915 | +9.80% | +0.58% | 0.66x | 17.1 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | ETH/USD | 1677.5 | 74.529 | 80.120 | +3.59% | -0.17% | 0.53x | 0.1 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | QNT/USD | 142.12 | 74.464 | 69.487 | +2.42% | +0.97% | 1.01x | 4.9 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SOL/USD | 70.48 | 72.895 | 72.323 | +2.58% | -0.11% | 1.11x | 1.4 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0550729 | 72.419 | 65.282 | +1.47% | -0.10% | 1.76x | 0.0 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 12 | ZEC/USD | 782.44 | 70.688 | 76.380 | +3.24% | +0.02% | 0.42x | 2.6 | 2026-11-21T17:50:47.315046+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 92.891 | 4.7178 | -0.24% | 0.97x |
| 2 | XMR/USD | 87.776 | 481.18 | +0.28% | 2.06x |
| 3 | NIGHT/USD | 86.517 | 0.04551 | +0.71% | 0.34x |
| 4 | ETH/USD | 80.120 | 1677.5 | -0.17% | 0.53x |
| 5 | PEARL/USD | 77.549 | 1.9834 | +2.44% | 5.43x |
| 6 | ZEC/USD | 76.380 | 782.44 | +0.02% | 0.42x |
| 7 | USELESS/USD | 75.915 | 0.0818 | +0.58% | 0.66x |
| 8 | XRP/USD | 73.259 | 0.9329 | +0.05% | 2.19x |
| 9 | SOL/USD | 72.323 | 70.48 | -0.11% | 1.11x |
| 10 | BEAM/USD | 69.521 | 0.003481 | +0.06% | 2.27x |
| 11 | QNT/USD | 69.487 | 142.12 | +0.97% | 1.01x |
| 12 | XDG/USD | 65.282 | 0.0550729 | -0.10% | 1.76x |

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

- Persisted scans: 1166; predictions: 9301; observations: 705287.
- Matured sampled outcomes across 1/6/24/48h: 12254; gap abstentions: 20993. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44932141865 · **Generation:** 1166 · **Legacy run:** 44932141865
**Main quote time:** 2026-11-21T17:50:55.699993+00:00 · **Legacy report time:** 2026-11-21T17:51:47.453172+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.9834 | 104.75 | +2.44% | 5.43x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 481.18 | 99.75 | +0.28% | 2.06x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | UNI/USD | 4.7178 | 91.43 | -0.24% | 0.97x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 4 | XRP/USD | 0.9329 | 85.40 | +0.05% | 2.19x | STRONG 88/100 | HIGH 55/100 | Watch |
| 5 | NIGHT/USD | 0.04551 | 83.41 | +0.71% | 0.34x | MODERATE 67/100 | VERY_HIGH 76/100 | Watch |
| 6 | BEAM/USD | 0.003481 | 82.52 | +0.06% | 2.27x | STRONG 81/100 | HIGH 66/100 | Watch |
| 7 | USELESS/USD | 0.0818 | 75.39 | +0.58% | 0.66x | MODERATE 63/100 | VERY_HIGH 76/100 | Watch |
| 8 | ETH/USD | 1677.5 | 74.53 | -0.17% | 0.53x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 9 | QNT/USD ⭐ | 142.12 | 74.46 | +0.97% | 1.01x | STRONG 82/100 | HIGH 62/100 | Watch |
| 10 | SOL/USD | 70.48 | 72.89 | -0.11% | 1.11x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 11 | XDG/USD | 0.0550729 | 72.42 | -0.10% | 1.76x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 12 | ZEC/USD | 782.44 | 70.69 | +0.02% | 0.42x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.9695 | 95.13 | +2.44% | 5.43x | 12439 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 481.13 | 90.06 | +0.28% | 2.06x | 12625 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | VVV/USD | 23.709 | 87.93 | +0.85% | 1.10x | 15407 | STRONG 79/100 | HIGH 62/100 | Watch |
| 4 | SHX/USD | 0.003539 | 86.40 | +1.06% | 1.70x | 2760 | STRONG 88/100 | HIGH 60/100 | Consider small entry |
| 5 | QNT/USD ⭐ | 142.75 | 74.46 | +0.97% | 1.01x | 11369 | STRONG 82/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEARL/USD, XMR/USD, QNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
