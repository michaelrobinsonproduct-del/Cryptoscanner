# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T13:51:06.858789+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45029509028
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 6c00659fc1c160f30b9470a7d9b4986161e460dc (atomic ledger/results publication)
**Ledger generation:** 1291 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0091 | 96.409 | 82.454 | +4.25% | -0.21% | 2.96x | 4.7 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 2 | DRV/USD | 0.36622 | 89.099 | 82.234 | +9.25% | +1.30% | 1.03x | 9.8 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | STRONG 80/100 | HIGH 62/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04811 | 75.375 | 81.409 | +8.65% | -0.46% | 0.62x | 18.7 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | ETH/USD | 1699.7 | 74.938 | 62.219 | +1.04% | -0.46% | 2.51x | 0.1 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LINK/USD | 8.74121 | 71.805 | 58.161 | +1.70% | -0.27% | 15.16x | 1.9 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6571 | 64.039 | 64.836 | +1.51% | -0.06% | 0.95x | 1.5 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ZEC/USD | 791.15 | 62.493 | 64.908 | +1.67% | -0.41% | 0.96x | 3.5 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XBT/USD | 60582.6 | 58.922 | 60.731 | +0.82% | -0.35% | 1.00x | 0.0 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | HYPE/USD | 62.42 | 58.630 | 66.886 | +1.93% | -0.34% | 0.34x | 3.2 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | AVAX/USD | 6.644 | 48.693 | 48.455 | +1.23% | -0.36% | 1.20x | 4.5 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | BNB/USD | 552.92 | 46.803 | 44.233 | +1.01% | -0.29% | 1.40x | 2.2 | 2026-11-22T13:50:59.379694+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 82.454 | 3.0091 | -0.21% | 2.96x |
| 2 | DRV/USD | 82.234 | 0.36622 | +1.30% | 1.03x |
| 3 | NIGHT/USD | 81.409 | 0.04811 | -0.46% | 0.62x |
| 4 | HYPE/USD | 66.886 | 62.42 | -0.34% | 0.34x |
| 5 | ZEC/USD | 64.908 | 791.15 | -0.41% | 0.96x |
| 6 | SUI/USD | 64.836 | 0.6571 | -0.06% | 0.95x |
| 7 | ETH/USD | 62.219 | 1699.7 | -0.46% | 2.51x |
| 8 | XBT/USD | 60.731 | 60582.6 | -0.35% | 1.00x |
| 9 | LINK/USD | 58.161 | 8.74121 | -0.27% | 15.16x |
| 10 | AVAX/USD | 48.455 | 6.644 | -0.36% | 1.20x |
| 11 | BNB/USD | 44.233 | 552.92 | -0.29% | 1.40x |

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

- Persisted scans: 1291; predictions: 10411; observations: 781328.
- Matured sampled outcomes across 1/6/24/48h: 15129; gap abstentions: 22264. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45029509028 · **Generation:** 1291 · **Legacy run:** 45029509028
**Main quote time:** 2026-11-22T13:51:06.858789+00:00 · **Legacy report time:** 2026-11-22T13:51:57.738473+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0091 | 96.41 | -0.21% | 2.96x | STRONG 78/100 | HIGH 61/100 | Watch |
| 2 | DRV/USD ⭐ | 0.36622 | 89.10 | +1.30% | 1.03x | STRONG 90/100 | HIGH 62/100 | Watch |
| 3 | NIGHT/USD | 0.04811 | 75.37 | -0.46% | 0.62x | WEAK 38/100 | VERY_HIGH 82/100 | Watch |
| 4 | ETH/USD | 1699.7 | 74.94 | -0.46% | 2.51x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 5 | LINK/USD | 8.74121 | 71.81 | -0.27% | 15.16x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 6 | SUI/USD | 0.6571 | 64.04 | -0.06% | 0.95x | WEAK 37/100 | HIGH 68/100 | Watch |
| 7 | ZEC/USD | 791.15 | 62.49 | -0.41% | 0.96x | WEAK 36/100 | HIGH 68/100 | Watch |
| 8 | XBT/USD | 60582.6 | 58.92 | -0.35% | 1.00x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 9 | HYPE/USD | 62.42 | 58.63 | -0.34% | 0.34x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | AVAX/USD | 6.644 | 48.69 | -0.36% | 1.20x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 11 | BNB/USD | 552.92 | 46.80 | -0.29% | 1.40x | WEAK 43/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.3649 | 81.30 | +1.30% | 1.03x | 15173 | STRONG 81/100 | HIGH 68/100 | Watch |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
