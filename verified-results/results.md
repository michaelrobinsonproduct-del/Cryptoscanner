# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T22:41:09.386813+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44957878843
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 9798e6ddacb241ba6dc402b4f0117cbb4882e69a (atomic ledger/results publication)
**Ledger generation:** 1196 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 489.21 | 96.777 | 98.260 | +7.21% | -0.39% | 1.05x | 3.5 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 2 | UNI/USD | 4.706 | 85.496 | 90.378 | +5.35% | -0.13% | 0.58x | 3.8 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04471 | 79.318 | 84.558 | +5.90% | -0.73% | 0.84x | 8.9 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ETH/USD | 1676.64 | 74.357 | 79.749 | +3.54% | -0.21% | 0.57x | 0.1 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | XBT/USD | 60067.4 | 71.710 | 70.002 | +2.14% | -0.18% | 1.26x | 0.0 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |
| 6 | QNT/USD | 142.95 | 68.120 | 70.197 | +3.02% | +0.11% | 0.74x | 11.9 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ZEC/USD | 782.53 | 66.881 | 77.547 | +3.25% | -0.49% | 0.18x | 0.4 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | PEARL/USD | 1.9654 | 65.927 | 74.560 | +7.50% | -0.27% | 0.27x | 27.5 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | WEAK 28/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | TAO/USD | 185.287 | 63.758 | 70.810 | +2.65% | -0.06% | 0.32x | 5.4 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.926 | 62.782 | 68.265 | +1.90% | -0.04% | 0.47x | 0.1 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0549562 | 62.559 | 63.267 | +1.26% | -0.15% | 1.01x | 1.0 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 12 | PAXG/USD | 3542.05 | 62.427 | 47.520 | +0.30% | -0.02% | 2.95x | 1.8 | 2026-11-21T22:41:00.849375+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 98.260 | 489.21 | -0.39% | 1.05x |
| 2 | UNI/USD | 90.378 | 4.706 | -0.13% | 0.58x |
| 3 | NIGHT/USD | 84.558 | 0.04471 | -0.73% | 0.84x |
| 4 | ETH/USD | 79.749 | 1676.64 | -0.21% | 0.57x |
| 5 | ZEC/USD | 77.547 | 782.53 | -0.49% | 0.18x |
| 6 | PEARL/USD | 74.560 | 1.9654 | -0.27% | 0.27x |
| 7 | TAO/USD | 70.810 | 185.287 | -0.06% | 0.32x |
| 8 | QNT/USD | 70.197 | 142.95 | +0.11% | 0.74x |
| 9 | XBT/USD | 70.002 | 60067.4 | -0.18% | 1.26x |
| 10 | XRP/USD | 68.265 | 0.926 | -0.04% | 0.47x |
| 11 | XDG/USD | 63.267 | 0.0549562 | -0.15% | 1.01x |
| 12 | PAXG/USD | 47.520 | 3542.05 | -0.02% | 2.95x |

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

- Persisted scans: 1196; predictions: 9661; observations: 723527.
- Matured sampled outcomes across 1/6/24/48h: 12940; gap abstentions: 21549. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44957878843 · **Generation:** 1196 · **Legacy run:** 44957878843
**Main quote time:** 2026-11-21T22:41:09.386813+00:00 · **Legacy report time:** 2026-11-21T22:42:01.084285+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 489.21 | 96.78 | -0.39% | 1.05x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 2 | UNI/USD | 4.706 | 85.50 | -0.13% | 0.58x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 3 | NIGHT/USD | 0.04471 | 79.32 | -0.73% | 0.84x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 4 | ETH/USD | 1676.64 | 74.36 | -0.21% | 0.57x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 5 | XBT/USD | 60067.4 | 71.71 | -0.18% | 1.26x | MODERATE 46/100 | HIGH 61/100 | Watch |
| 6 | QNT/USD | 142.95 | 68.12 | +0.11% | 0.74x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 7 | ZEC/USD | 782.53 | 66.88 | -0.49% | 0.18x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 8 | PEARL/USD | 1.9654 | 65.93 | -0.27% | 0.27x | WEAK 28/100 | EXTREME 88/100 | Do nothing |
| 9 | TAO/USD | 185.287 | 63.76 | -0.06% | 0.32x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.926 | 62.78 | -0.04% | 0.47x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0549562 | 62.56 | -0.15% | 1.01x | WEAK 41/100 | HIGH 68/100 | Watch |
| 12 | PAXG/USD | 3542.05 | 62.43 | -0.02% | 2.95x | MODERATE 61/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
