# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T20:11:21.049031+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44944768799
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 677e43b39675f12b5382c6331c1d00d2c0a0f3bd (atomic ledger/results publication)
**Ledger generation:** 1180 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 790.45 | 100.553 | 84.990 | +4.29% | +0.11% | 6.15x | 0.1 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 487.28 | 97.479 | 94.966 | +6.79% | +0.40% | 1.05x | 10.1 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | STRONG 79/100 | HIGH 68/100 | Watch | WATCH |
| 3 | XBT/USD | 60267.4 | 88.301 | 72.383 | +2.48% | +0.18% | 2.80x | 0.0 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04542 | 87.226 | 83.865 | +7.58% | +0.20% | 1.24x | 19.8 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | MODERATE 64/100 | HIGH 68/100 | Watch | WATCH |
| 5 | ETH/USD | 1683.53 | 85.418 | 82.727 | +3.97% | -0.06% | 1.30x | 0.1 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 6 | UNI/USD | 4.6987 | 83.353 | 86.266 | +5.18% | +0.44% | 0.49x | 10.0 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | SOL/USD | 70.41 | 73.052 | 71.609 | +2.47% | -0.07% | 1.18x | 1.4 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93492 | 68.861 | 74.816 | +2.88% | +0.02% | 0.39x | 0.7 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | PAXG/USD | 3554.09 | 68.786 | 53.905 | +0.64% | -0.02% | 7.60x | 0.7 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0551651 | 68.455 | 66.471 | +1.64% | +0.03% | 1.19x | 0.0 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XLM/USD | 0.129567 | 68.420 | 67.055 | +1.86% | +0.17% | 1.05x | 1.9 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 12 | TAO/USD | 184.8302 | 61.430 | 69.100 | +2.39% | -0.03% | 0.25x | 5.3 | 2026-11-21T20:11:12.488444+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 94.966 | 487.28 | +0.40% | 1.05x |
| 2 | UNI/USD | 86.266 | 4.6987 | +0.44% | 0.49x |
| 3 | ZEC/USD | 84.990 | 790.45 | +0.11% | 6.15x |
| 4 | NIGHT/USD | 83.865 | 0.04542 | +0.20% | 1.24x |
| 5 | ETH/USD | 82.727 | 1683.53 | -0.06% | 1.30x |
| 6 | XRP/USD | 74.816 | 0.93492 | +0.02% | 0.39x |
| 7 | XBT/USD | 72.383 | 60267.4 | +0.18% | 2.80x |
| 8 | SOL/USD | 71.609 | 70.41 | -0.07% | 1.18x |
| 9 | TAO/USD | 69.100 | 184.8302 | -0.03% | 0.25x |
| 10 | XLM/USD | 67.055 | 0.129567 | +0.17% | 1.05x |
| 11 | XDG/USD | 66.471 | 0.0551651 | +0.03% | 1.19x |
| 12 | PAXG/USD | 53.905 | 3554.09 | -0.02% | 7.60x |

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

- Persisted scans: 1180; predictions: 9469; observations: 713799.
- Matured sampled outcomes across 1/6/24/48h: 12580; gap abstentions: 21282. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44944768799 · **Generation:** 1180 · **Legacy run:** 44944768799
**Main quote time:** 2026-11-21T20:11:21.049031+00:00 · **Legacy report time:** 2026-11-21T20:12:10.249675+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 790.45 | 100.55 | +0.11% | 6.15x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 487.28 | 97.48 | +0.40% | 1.05x | STRONG 89/100 | HIGH 68/100 | Watch |
| 3 | XBT/USD ⭐ | 60267.4 | 88.30 | +0.18% | 2.80x | STRONG 99/100 | HIGH 55/100 | Watch |
| 4 | NIGHT/USD ⭐ | 0.04542 | 87.23 | +0.20% | 1.24x | STRONG 74/100 | HIGH 68/100 | Watch |
| 5 | ETH/USD | 1683.53 | 85.42 | -0.06% | 1.30x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 6 | UNI/USD | 4.6987 | 83.35 | +0.44% | 0.49x | MODERATE 67/100 | VERY_HIGH 76/100 | Watch |
| 7 | SOL/USD | 70.41 | 73.05 | -0.07% | 1.18x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 8 | XRP/USD | 0.93492 | 68.86 | +0.02% | 0.39x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 9 | PAXG/USD | 3554.09 | 68.79 | -0.02% | 7.60x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 10 | XDG/USD | 0.0551651 | 68.45 | +0.03% | 1.19x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 11 | XLM/USD | 0.129567 | 68.42 | +0.17% | 1.05x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 12 | TAO/USD | 184.8302 | 61.43 | -0.03% | 0.25x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 789.46 | 100.00 | +0.11% | 6.15x | 43568 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XBT/USD ⭐ | 60225.7 | 88.68 | +0.18% | 2.80x | 218724 | STRONG 99/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD ⭐ | 486.83 | 88.66 | +0.40% | 1.05x | 12451 | STRONG 89/100 | HIGH 62/100 | Watch |
| 4 | ZBCN/USD | 0.0017 | 84.51 | +1.67% | 3.85x | 3348 | STRONG 82/100 | VERY_HIGH 82/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.0453 | 82.79 | +0.20% | 1.24x | 11594 | STRONG 71/100 | HIGH 68/100 | Watch |

**Same-run overlap:** ZEC/USD, XMR/USD, XBT/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
