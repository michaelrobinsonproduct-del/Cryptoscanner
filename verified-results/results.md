# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T13:11:32.680675+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44907450888
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 3d8dfd8dce4896f77240f5abb6fa301ffab5f548 (atomic ledger/results publication)
**Ledger generation:** 1137 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.885 | 94.491 | 94.099 | +10.35% | +1.13% | 0.48x | 11.8 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | ZEC/USD | 779.48 | 85.410 | 71.076 | +2.85% | +1.27% | 1.80x | 7.7 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | CT/USD | 0.1285 | 83.831 | 70.379 | +6.11% | -0.31% | 3.52x | 7.8 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | ETH/USD | 1671.09 | 76.369 | 76.332 | +3.20% | +0.38% | 0.81x | 2.1 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 5 | TRX/USD | 0.303048 | 74.213 | 58.370 | +0.51% | +0.17% | 3.43x | 0.4 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XMR/USD | 469.78 | 71.478 | 71.864 | +2.96% | +0.31% | 0.81x | 7.7 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 7 | TAO/USD | 184.3677 | 67.629 | 66.233 | +2.14% | +0.89% | 0.69x | 7.5 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SENT/USD | 0.021395 | 61.505 | 54.257 | +3.88% | +2.00% | 0.72x | 8.0 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | XBT/USD | 59233.6 | 60.245 | 59.249 | +0.73% | +0.79% | 0.71x | 1.7 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | AAVE/USD | 99.89 | 60.227 | 56.521 | +2.04% | +0.93% | 0.91x | 8.0 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 11 | SOL/USD | 69.47 | 57.459 | 61.303 | +1.11% | +0.32% | 0.46x | 2.9 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | USELESS/USD | 0.07764 | 56.104 | 57.161 | +4.21% | +1.12% | 0.34x | 24.5 | 2026-11-21T13:11:25.113116+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 94.099 | 22.885 | +1.13% | 0.48x |
| 2 | ETH/USD | 76.332 | 1671.09 | +0.38% | 0.81x |
| 3 | XMR/USD | 71.864 | 469.78 | +0.31% | 0.81x |
| 4 | ZEC/USD | 71.076 | 779.48 | +1.27% | 1.80x |
| 5 | CT/USD | 70.379 | 0.1285 | -0.31% | 3.52x |
| 6 | TAO/USD | 66.233 | 184.3677 | +0.89% | 0.69x |
| 7 | SOL/USD | 61.303 | 69.47 | +0.32% | 0.46x |
| 8 | XBT/USD | 59.249 | 59233.6 | +0.79% | 0.71x |
| 9 | TRX/USD | 58.370 | 0.303048 | +0.17% | 3.43x |
| 10 | USELESS/USD | 57.161 | 0.07764 | +1.12% | 0.34x |
| 11 | AAVE/USD | 56.521 | 99.89 | +0.93% | 0.91x |
| 12 | SENT/USD | 54.257 | 0.021395 | +2.00% | 0.72x |

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

- Persisted scans: 1137; predictions: 8953; observations: 687655.
- Matured sampled outcomes across 1/6/24/48h: 11743; gap abstentions: 20385. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44907450888 · **Generation:** 1137 · **Legacy run:** 44907450888
**Main quote time:** 2026-11-21T13:11:32.680675+00:00 · **Legacy report time:** 2026-11-21T13:12:37.523619+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.885 | 94.49 | +1.13% | 0.48x | STRONG 72/100 | VERY_HIGH 76/100 | Watch |
| 2 | ZEC/USD ⭐ | 779.48 | 85.41 | +1.27% | 1.80x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | CT/USD | 0.1285 | 83.83 | -0.31% | 3.52x | STRONG 72/100 | VERY_HIGH 73/100 | Watch |
| 4 | ETH/USD | 1671.09 | 76.37 | +0.38% | 0.81x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 5 | TRX/USD ⭐ | 0.303048 | 74.21 | +0.17% | 3.43x | STRONG 92/100 | HIGH 55/100 | Watch |
| 6 | XMR/USD | 469.78 | 71.48 | +0.31% | 0.81x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 7 | TAO/USD | 184.3677 | 67.63 | +0.89% | 0.69x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 8 | SENT/USD | 0.021395 | 61.50 | +2.00% | 0.72x | MODERATE 61/100 | VERY_HIGH 82/100 | Watch |
| 9 | XBT/USD | 59233.6 | 60.24 | +0.79% | 0.71x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 10 | AAVE/USD | 99.89 | 60.23 | +0.93% | 0.91x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 11 | SOL/USD | 69.47 | 57.46 | +0.32% | 0.46x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | USELESS/USD | 0.07764 | 56.10 | +1.12% | 0.34x | MODERATE 48/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 780.2 | 80.96 | +1.27% | 1.80x | 57519 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | PEAQ/USD | 0.02071 | 72.51 | +0.24% | 1.59x | 2515 | STRONG 76/100 | VERY_HIGH 73/100 | Watch |
| 3 | TRX/USD ⭐ | 0.303048 | 64.94 | +0.17% | 3.43x | 6781 | STRONG 87/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
