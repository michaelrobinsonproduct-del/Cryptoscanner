# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T16:01:06.653781+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44922078365
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 5702437bd379168a35514b5cb49c707dbb3fb3dd (atomic ledger/results publication)
**Ledger generation:** 1154 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 476.59 | 82.540 | 81.312 | +4.45% | +0.21% | 1.02x | 9.7 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | STRONG 76/100 | HIGH 62/100 | Watch | WATCH |
| 2 | USELESS/USD | 0.08193 | 77.343 | 75.501 | +9.97% | -1.09% | 1.73x | 19.5 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 3 | UNI/USD | 4.6917 | 77.272 | 89.007 | +5.03% | -0.73% | 0.19x | 2.3 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | ETH/USD | 1681.38 | 75.576 | 81.798 | +3.83% | -0.28% | 0.52x | 0.1 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ZEC/USD | 788.7 | 73.810 | 82.423 | +4.06% | -0.68% | 0.48x | 2.0 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | TAO/USD | 187.6966 | 71.647 | 78.950 | +3.98% | -0.42% | 0.48x | 7.9 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | BEAM/USD | 0.003587 | 67.977 | 72.686 | +9.43% | -1.40% | 1.23x | 8.4 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 8 | SOL/USD | 70.27 | 61.356 | 70.181 | +2.27% | -0.33% | 0.28x | 1.4 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XBT/USD | 59849.9 | 60.007 | 67.413 | +1.77% | -0.34% | 0.43x | 0.0 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0550583 | 59.894 | 64.866 | +1.44% | -0.34% | 0.67x | 0.5 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | TRX/USD | 0.304454 | 58.144 | 57.707 | +0.98% | -0.03% | 1.06x | 1.1 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XRP/USD | 0.92261 | 57.927 | 65.382 | +1.53% | -0.30% | 0.40x | 0.7 | 2026-11-21T16:00:57.886422+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 89.007 | 4.6917 | -0.73% | 0.19x |
| 2 | ZEC/USD | 82.423 | 788.7 | -0.68% | 0.48x |
| 3 | ETH/USD | 81.798 | 1681.38 | -0.28% | 0.52x |
| 4 | XMR/USD | 81.312 | 476.59 | +0.21% | 1.02x |
| 5 | TAO/USD | 78.950 | 187.6966 | -0.42% | 0.48x |
| 6 | USELESS/USD | 75.501 | 0.08193 | -1.09% | 1.73x |
| 7 | BEAM/USD | 72.686 | 0.003587 | -1.40% | 1.23x |
| 8 | SOL/USD | 70.181 | 70.27 | -0.33% | 0.28x |
| 9 | XBT/USD | 67.413 | 59849.9 | -0.34% | 0.43x |
| 10 | XRP/USD | 65.382 | 0.92261 | -0.30% | 0.40x |
| 11 | XDG/USD | 64.866 | 0.0550583 | -0.34% | 0.67x |
| 12 | TRX/USD | 57.707 | 0.304454 | -0.03% | 1.06x |

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

- Persisted scans: 1154; predictions: 9157; observations: 697991.
- Matured sampled outcomes across 1/6/24/48h: 12042; gap abstentions: 20725. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44922078365 · **Generation:** 1154 · **Legacy run:** 44922078365
**Main quote time:** 2026-11-21T16:01:06.653781+00:00 · **Legacy report time:** 2026-11-21T16:01:55.469579+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 476.59 | 82.54 | +0.21% | 1.02x | STRONG 86/100 | HIGH 62/100 | Watch |
| 2 | USELESS/USD | 0.08193 | 77.34 | -1.09% | 1.73x | MODERATE 54/100 | VERY_HIGH 71/100 | Watch |
| 3 | UNI/USD | 4.6917 | 77.27 | -0.73% | 0.19x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 4 | ETH/USD | 1681.38 | 75.58 | -0.28% | 0.52x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 5 | ZEC/USD | 788.7 | 73.81 | -0.68% | 0.48x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | TAO/USD | 187.6966 | 71.65 | -0.42% | 0.48x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 7 | BEAM/USD | 0.003587 | 67.98 | -1.40% | 1.23x | WEAK 44/100 | VERY_HIGH 77/100 | Do nothing |
| 8 | SOL/USD | 70.27 | 61.36 | -0.33% | 0.28x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | XBT/USD | 59849.9 | 60.01 | -0.34% | 0.43x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | XDG/USD | 0.0550583 | 59.89 | -0.34% | 0.67x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | TRX/USD | 0.304454 | 58.14 | -0.03% | 1.06x | WEAK 39/100 | HIGH 68/100 | Watch |
| 12 | XRP/USD | 0.92261 | 57.93 | -0.30% | 0.40x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 475.5 | 86.41 | +0.21% | 1.02x | 12759 | STRONG 88/100 | HIGH 62/100 | Watch |
| 2 | SHX/USD | 0.0035 | 76.24 | +0.40% | 2.00x | 2781 | STRONG 83/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
