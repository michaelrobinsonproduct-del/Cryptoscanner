# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T16:27:15.325975+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44924520960
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** fe41df8cef8d13545dec9b858621d75cfcdbcde9 (atomic ledger/results publication)
**Ledger generation:** 1157 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.178 | 109.919 | 95.904 | +11.76% | -0.20% | 4.00x | 8.2 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | UNI/USD | 4.7137 | 106.714 | 92.034 | +5.52% | +0.54% | 2.20x | 3.2 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XMR/USD | 477.77 | 87.470 | 84.602 | +4.71% | +0.51% | 1.03x | 6.7 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | STRONG 79/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ZEC/USD | 785.09 | 81.795 | 79.020 | +3.59% | -0.01% | 1.28x | 2.2 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.0831 | 81.397 | 78.697 | +11.54% | +1.84% | 0.35x | 12.1 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ETH/USD | 1678.32 | 75.969 | 80.475 | +3.64% | +0.13% | 0.48x | 0.1 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | TAO/USD | 186.183 | 75.740 | 73.820 | +3.14% | -0.35% | 1.37x | 6.4 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SOL/USD | 70.26 | 68.531 | 69.367 | +2.26% | +0.34% | 0.75x | 2.8 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 59870.7 | 68.037 | 67.660 | +1.81% | +0.35% | 0.86x | 0.0 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0548884 | 65.814 | 62.902 | +1.13% | +0.11% | 1.24x | 0.0 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XRP/USD | 0.92612 | 64.627 | 67.872 | +1.92% | +0.45% | 0.45x | 1.1 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | BEAM/USD | 0.00352 | 57.604 | 68.344 | +7.38% | -1.28% | 0.57x | 17.0 | 2026-11-21T16:27:06.940584+00:00 | Not calibrated | WEAK 29/100 | EXTREME 91/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.904 | 23.178 | -0.20% | 4.00x |
| 2 | UNI/USD | 92.034 | 4.7137 | +0.54% | 2.20x |
| 3 | XMR/USD | 84.602 | 477.77 | +0.51% | 1.03x |
| 4 | ETH/USD | 80.475 | 1678.32 | +0.13% | 0.48x |
| 5 | ZEC/USD | 79.020 | 785.09 | -0.01% | 1.28x |
| 6 | USELESS/USD | 78.697 | 0.0831 | +1.84% | 0.35x |
| 7 | TAO/USD | 73.820 | 186.183 | -0.35% | 1.37x |
| 8 | SOL/USD | 69.367 | 70.26 | +0.34% | 0.75x |
| 9 | BEAM/USD | 68.344 | 0.00352 | -1.28% | 0.57x |
| 10 | XRP/USD | 67.872 | 0.92612 | +0.45% | 0.45x |
| 11 | XBT/USD | 67.660 | 59870.7 | +0.35% | 0.86x |
| 12 | XDG/USD | 62.902 | 0.0548884 | +0.11% | 1.24x |

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

- Persisted scans: 1157; predictions: 9193; observations: 699815.
- Matured sampled outcomes across 1/6/24/48h: 12099; gap abstentions: 20791. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44924520960 · **Generation:** 1157 · **Legacy run:** 44924520960
**Main quote time:** 2026-11-21T16:27:15.325975+00:00 · **Legacy report time:** 2026-11-21T16:28:20.521418+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 23.178 | 109.92 | -0.20% | 4.00x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | UNI/USD ⭐ | 4.7137 | 106.71 | +0.54% | 2.20x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD ⭐ | 477.77 | 87.47 | +0.51% | 1.03x | STRONG 89/100 | HIGH 62/100 | Watch |
| 4 | ZEC/USD | 785.09 | 81.80 | -0.01% | 1.28x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 5 | USELESS/USD | 0.0831 | 81.40 | +1.84% | 0.35x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 6 | ETH/USD | 1678.32 | 75.97 | +0.13% | 0.48x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 7 | TAO/USD | 186.183 | 75.74 | -0.35% | 1.37x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | SOL/USD | 70.26 | 68.53 | +0.34% | 0.75x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 59870.7 | 68.04 | +0.35% | 0.86x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 10 | XDG/USD | 0.0548884 | 65.81 | +0.11% | 1.24x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 11 | XRP/USD | 0.92612 | 64.63 | +0.45% | 0.45x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 12 | BEAM/USD | 0.00352 | 57.60 | -1.28% | 0.57x | WEAK 29/100 | EXTREME 91/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7019 | 100.00 | +0.54% | 2.20x | 12122 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 477.99 | 87.81 | +0.51% | 1.03x | 12706 | STRONG 89/100 | HIGH 62/100 | Watch |

**Same-run overlap:** UNI/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
