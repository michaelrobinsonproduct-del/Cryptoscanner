# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:25:19.174316+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44554453487
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** d160b7e2f8010206cbd8a1d473b867c31f50acbc (atomic ledger/results publication)
**Ledger generation:** 801 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.865 | 82.305 | 86.783 | +5.51% | -2.02% | 1.56x | 13.6 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 2 | LIGHTER/USD | 2.922 | 79.490 | 74.086 | +7.66% | -1.92% | 2.64x | 13.7 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | AKT/USD | 0.5508 | 78.955 | 72.175 | +6.33% | -0.63% | 1.99x | 7.3 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | ZEC/USD | 932.36 | 68.198 | 69.326 | +2.24% | -1.17% | 1.47x | 2.7 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | MODERATE 54/100 | HIGH 65/100 | Watch | WATCH |
| 5 | ETH/USD | 1787.89 | 67.684 | 60.151 | +0.74% | -0.96% | 2.23x | 0.1 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SKR/USD | 0.010443 | 67.250 | 70.728 | +8.41% | -1.00% | 1.15x | 10.6 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | WEAK 39/100 | EXTREME 90/100 | Do nothing | WATCH |
| 7 | GRASS/USD | 0.445 | 66.450 | 73.283 | +9.82% | -1.40% | 1.01x | 11.2 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 8 | HYPE/USD | 68.6 | 64.978 | 71.545 | +2.57% | -0.82% | 0.76x | 2.9 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XRP/USD | 0.98286 | 59.829 | 66.436 | +1.71% | -0.53% | 0.61x | 1.0 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XBT/USD | 63344.8 | 59.191 | 58.010 | +0.57% | -0.41% | 1.32x | 2.0 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 11 | LINK/USD | 9.10932 | 55.490 | 57.692 | +0.40% | -1.00% | 1.28x | 0.3 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | WEAK 38/100 | HIGH 65/100 | Watch | WATCH |
| 12 | SOL/USD | 74.63 | 55.189 | 64.705 | +1.48% | -0.76% | 0.43x | 1.3 | 2026-11-19T15:25:12.219598+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 86.783 | 22.865 | -2.02% | 1.56x |
| 2 | LIGHTER/USD | 74.086 | 2.922 | -1.92% | 2.64x |
| 3 | GRASS/USD | 73.283 | 0.445 | -1.40% | 1.01x |
| 4 | AKT/USD | 72.175 | 0.5508 | -0.63% | 1.99x |
| 5 | HYPE/USD | 71.545 | 68.6 | -0.82% | 0.76x |
| 6 | SKR/USD | 70.728 | 0.010443 | -1.00% | 1.15x |
| 7 | ZEC/USD | 69.326 | 932.36 | -1.17% | 1.47x |
| 8 | XRP/USD | 66.436 | 0.98286 | -0.53% | 0.61x |
| 9 | SOL/USD | 64.705 | 74.63 | -0.76% | 0.43x |
| 10 | ETH/USD | 60.151 | 1787.89 | -0.96% | 2.23x |
| 11 | XBT/USD | 58.010 | 63344.8 | -0.41% | 1.32x |
| 12 | LINK/USD | 57.692 | 9.10932 | -1.00% | 1.28x |

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

- Persisted scans: 801; predictions: 6756; observations: 484432.
- Matured sampled outcomes across 1/6/24/48h: 6755; gap abstentions: 15206. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44554453487 · **Generation:** 801 · **Legacy run:** 44554453487
**Main quote time:** 2026-11-19T15:25:19.174316+00:00 · **Legacy report time:** 2026-11-19T15:26:02.185254+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.865 | 82.30 | -2.02% | 1.56x | MODERATE 56/100 | VERY_HIGH 71/100 | Do nothing |
| 2 | LIGHTER/USD | 2.922 | 79.49 | -1.92% | 2.64x | MODERATE 65/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | AKT/USD | 0.5508 | 78.96 | -0.63% | 1.99x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |
| 4 | ZEC/USD | 932.36 | 68.20 | -1.17% | 1.47x | MODERATE 54/100 | HIGH 65/100 | Watch |
| 5 | ETH/USD | 1787.89 | 67.68 | -0.96% | 2.23x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | SKR/USD | 0.010443 | 67.25 | -1.00% | 1.15x | WEAK 39/100 | EXTREME 90/100 | Do nothing |
| 7 | GRASS/USD | 0.445 | 66.45 | -1.40% | 1.01x | WEAK 38/100 | VERY_HIGH 83/100 | Do nothing |
| 8 | HYPE/USD | 68.6 | 64.98 | -0.82% | 0.76x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | XRP/USD | 0.98286 | 59.83 | -0.53% | 0.61x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | XBT/USD | 63344.8 | 59.19 | -0.41% | 1.32x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 11 | LINK/USD | 9.10932 | 55.49 | -1.00% | 1.28x | WEAK 38/100 | HIGH 65/100 | Watch |
| 12 | SOL/USD | 74.63 | 55.19 | -0.76% | 0.43x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

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
