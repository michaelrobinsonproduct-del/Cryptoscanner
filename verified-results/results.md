# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T15:20:49.319598+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44918570649
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 78b4bfb608433d2bf5463441f4decfeb8d61debe (atomic ledger/results publication)
**Ledger generation:** 1150 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 789.14 | 86.231 | 78.262 | +4.12% | -0.56% | 2.08x | 11.2 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 2 | VVV/USD | 23.043 | 84.450 | 86.523 | +11.11% | -1.31% | 1.45x | 27.0 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 3 | UNI/USD | 4.6937 | 83.797 | 86.868 | +5.07% | -1.25% | 1.32x | 7.2 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | MODERATE 62/100 | HIGH 65/100 | Do nothing | WATCH |
| 4 | XBT/USD | 60088 | 79.493 | 69.215 | +2.18% | -0.53% | 2.29x | 2.1 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1683.09 | 78.756 | 80.516 | +3.94% | -0.70% | 1.18x | 4.1 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 6 | TAO/USD | 187.6729 | 74.716 | 77.062 | +3.97% | -1.07% | 1.30x | 11.4 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 7 | PAXG/USD | 3544.8 | 68.358 | 56.844 | +0.38% | -0.13% | 2.22x | 1.6 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SOL/USD | 70.4 | 68.234 | 71.507 | +2.46% | -0.72% | 1.03x | 1.4 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XMR/USD | 470.16 | 64.741 | 71.492 | +3.04% | -0.42% | 0.54x | 9.6 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | USELESS/USD | 0.08157 | 63.502 | 71.863 | +9.49% | -1.14% | 0.74x | 28.2 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | WEAK 27/100 | EXTREME 92/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.92341 | 60.909 | 65.836 | +1.62% | -0.89% | 0.95x | 1.0 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 12 | TRX/USD | 0.304742 | 59.207 | 61.697 | +1.07% | -0.05% | 0.77x | 1.6 | 2026-11-21T15:20:43.015998+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 86.868 | 4.6937 | -1.25% | 1.32x |
| 2 | VVV/USD | 86.523 | 23.043 | -1.31% | 1.45x |
| 3 | ETH/USD | 80.516 | 1683.09 | -0.70% | 1.18x |
| 4 | ZEC/USD | 78.262 | 789.14 | -0.56% | 2.08x |
| 5 | TAO/USD | 77.062 | 187.6729 | -1.07% | 1.30x |
| 6 | USELESS/USD | 71.863 | 0.08157 | -1.14% | 0.74x |
| 7 | SOL/USD | 71.507 | 70.4 | -0.72% | 1.03x |
| 8 | XMR/USD | 71.492 | 470.16 | -0.42% | 0.54x |
| 9 | XBT/USD | 69.215 | 60088 | -0.53% | 2.29x |
| 10 | XRP/USD | 65.836 | 0.92341 | -0.89% | 0.95x |
| 11 | TRX/USD | 61.697 | 0.304742 | -0.05% | 0.77x |
| 12 | PAXG/USD | 56.844 | 3544.8 | -0.13% | 2.22x |

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

- Persisted scans: 1150; predictions: 9109; observations: 695559.
- Matured sampled outcomes across 1/6/24/48h: 11970; gap abstentions: 20639. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44918570649 · **Generation:** 1150 · **Legacy run:** 44918570649
**Main quote time:** 2026-11-21T15:20:49.319598+00:00 · **Legacy report time:** 2026-11-21T15:21:52.712706+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 789.14 | 86.23 | -0.56% | 2.08x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 2 | VVV/USD | 23.043 | 84.45 | -1.31% | 1.45x | MODERATE 52/100 | VERY_HIGH 77/100 | Do nothing |
| 3 | UNI/USD | 4.6937 | 83.80 | -1.25% | 1.32x | MODERATE 62/100 | HIGH 65/100 | Do nothing |
| 4 | XBT/USD | 60088 | 79.49 | -0.53% | 2.29x | STRONG 70/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1683.09 | 78.76 | -0.70% | 1.18x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 6 | TAO/USD | 187.6729 | 74.72 | -1.07% | 1.30x | WEAK 42/100 | VERY_HIGH 71/100 | Watch |
| 7 | PAXG/USD | 3544.8 | 68.36 | -0.13% | 2.22x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 8 | SOL/USD | 70.4 | 68.23 | -0.72% | 1.03x | WEAK 44/100 | HIGH 68/100 | Watch |
| 9 | XMR/USD | 470.16 | 64.74 | -0.42% | 0.54x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | USELESS/USD | 0.08157 | 63.50 | -1.14% | 0.74x | WEAK 27/100 | EXTREME 92/100 | Do nothing |
| 11 | XRP/USD | 0.92341 | 60.91 | -0.89% | 0.95x | WEAK 35/100 | HIGH 68/100 | Watch |
| 12 | TRX/USD | 0.304742 | 59.21 | -0.05% | 0.77x | WEAK 35/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CSPR/USD | 0.0017401 | 86.34 | +2.87% | 2.95x | 5027 | STRONG 83/100 | VERY_HIGH 79/100 | Watch |
| 2 | CT/USD | 0.1318 | 75.19 | +0.23% | 2.31x | 2436 | STRONG 83/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
