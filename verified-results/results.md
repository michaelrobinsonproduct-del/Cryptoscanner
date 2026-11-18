# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:30:21.885908+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44324824320
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** f2a5e0feb5ac4cf4c9d226e6c3d1eac853621912 (atomic ledger/results publication)
**Ledger generation:** 589 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04696 | 91.143 | 74.507 | +4.61% | +0.36% | 2.48x | 12.8 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | STRONG 96/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.98945 | 66.493 | 59.880 | +0.70% | +0.29% | 1.52x | 0.1 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SENT/USD | 0.019629 | 62.559 | 63.246 | +5.14% | +0.95% | 0.45x | 7.6 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | CT/USD | 0.1219 | 62.094 | 63.615 | +7.88% | +0.33% | 0.68x | 24.7 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | STABLE/USD | 0.02318 | 60.751 | 67.350 | +10.12% | -0.22% | 0.45x | 17.3 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | WEAK 30/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | INFI/USD | 0.1379 | 59.185 | 72.859 | +8.58% | -4.44% | 1.85x | 7.2 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 7 | VVV/USD | 21.195 | 46.883 | 48.733 | +0.80% | -0.09% | 0.86x | 10.4 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 8 | CC/USD | 0.0832 | 45.715 | 39.115 | +1.30% | +0.04% | 1.64x | 10.8 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5234 | 40.347 | 45.161 | +2.77% | +0.38% | 0.33x | 13.4 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | TRX/USD | 0.30992 | 39.327 | 46.267 | +0.66% | +0.11% | 0.25x | 0.0 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | W/USD | 0.00902 | 30.922 | 33.239 | +1.01% | +0.33% | 0.60x | 11.1 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | PEARL/USD | 1.8517 | 30.539 | 45.890 | +2.28% | -1.28% | 0.11x | 16.8 | 2026-11-18T14:30:13.388716+00:00 | Not calibrated | WEAK 15/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 74.507 | 0.04696 | +0.36% | 2.48x |
| 2 | INFI/USD | 72.859 | 0.1379 | -4.44% | 1.85x |
| 3 | STABLE/USD | 67.350 | 0.02318 | -0.22% | 0.45x |
| 4 | CT/USD | 63.615 | 0.1219 | +0.33% | 0.68x |
| 5 | SENT/USD | 63.246 | 0.019629 | +0.95% | 0.45x |
| 6 | XRP/USD | 59.880 | 0.98945 | +0.29% | 1.52x |
| 7 | VVV/USD | 48.733 | 21.195 | -0.09% | 0.86x |
| 8 | TRX/USD | 46.267 | 0.30992 | +0.11% | 0.25x |
| 9 | PEARL/USD | 45.890 | 1.8517 | -1.28% | 0.11x |
| 10 | AKT/USD | 45.161 | 0.5234 | +0.38% | 0.33x |
| 11 | CC/USD | 39.115 | 0.0832 | +0.04% | 1.64x |
| 12 | W/USD | 33.239 | 0.00902 | +0.33% | 0.60x |

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

- Persisted scans: 589; predictions: 5016; observations: 355708.
- Matured sampled outcomes across 1/6/24/48h: 4235; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44324824320 · **Generation:** 589 · **Legacy run:** 44324824320
**Main quote time:** 2026-11-18T14:30:21.885908+00:00 · **Legacy report time:** 2026-11-18T14:30:47.926709+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04696 | 91.14 | +0.36% | 2.48x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.98945 | 66.49 | +0.29% | 1.52x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD | 0.019629 | 62.56 | +0.95% | 0.45x | MODERATE 61/100 | VERY_HIGH 82/100 | Watch |
| 4 | CT/USD | 0.1219 | 62.09 | +0.33% | 0.68x | MODERATE 51/100 | EXTREME 94/100 | Do nothing |
| 5 | STABLE/USD | 0.02318 | 60.75 | -0.22% | 0.45x | WEAK 30/100 | EXTREME 94/100 | Do nothing |
| 6 | INFI/USD | 0.1379 | 59.18 | -4.44% | 1.85x | MODERATE 50/100 | VERY_HIGH 77/100 | Do nothing |
| 7 | VVV/USD | 21.195 | 46.88 | -0.09% | 0.86x | WEAK 23/100 | VERY_HIGH 74/100 | Do nothing |
| 8 | CC/USD | 0.0832 | 45.72 | +0.04% | 1.64x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 9 | AKT/USD | 0.5234 | 40.35 | +0.38% | 0.33x | MODERATE 45/100 | VERY_HIGH 81/100 | Watch |
| 10 | TRX/USD | 0.30992 | 39.33 | +0.11% | 0.25x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 11 | W/USD | 0.00902 | 30.92 | +0.33% | 0.60x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 12 | PEARL/USD | 1.8517 | 30.54 | -1.28% | 0.11x | WEAK 15/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04696 | 88.19 | +0.36% | 2.48x | 15784 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.99046 | 61.59 | +0.29% | 1.52x | 35342 | STRONG 86/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
