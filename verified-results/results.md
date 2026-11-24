# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T09:41:47.228624+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45367282629
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a2361122a5736a571fc7847d113fbd2202f54667 (atomic ledger/results publication)
**Ledger generation:** 1557 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01268 | 70.301 | 78.718 | +10.07% | -1.25% | 0.78x | 15.8 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 2 | VVV/USD | 25.063 | 64.287 | 67.225 | +2.52% | +0.28% | 0.57x | 10.8 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.603e-05 | 61.251 | 58.080 | +5.89% | -0.69% | 1.66x | 30.5 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 4 | LCX/USD | 0.03341 | 61.094 | 65.502 | +5.26% | -1.71% | 1.42x | 6.0 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 5 | 2Z/USD | 0.0163 | 60.065 | 56.728 | +4.15% | +0.18% | 1.24x | 6.1 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | XMR/USD | 497.61 | 58.742 | 65.460 | +2.38% | -0.19% | 0.42x | 12.5 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | PEPE/USD | 3.486e-06 | 57.394 | 62.146 | +1.87% | +0.00% | 0.52x | 2.9 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | LINK/USD | 9.05163 | 52.344 | 55.495 | +0.52% | +0.13% | 0.62x | 6.3 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | BABY/USD | 0.00891 | 44.986 | 49.570 | +4.82% | +0.79% | 0.15x | 33.7 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | WEAK 42/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | BAT/USD | 0.07899 | 42.658 | 45.087 | +2.36% | -0.58% | 1.05x | 7.6 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 11 | ATOM/USD | 1.2957 | 31.136 | 35.210 | +1.05% | +0.13% | 0.53x | 10.8 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | XTZ/USD | 0.21375 | 22.428 | 25.683 | +0.42% | +0.41% | 0.47x | 16.4 | 2026-11-24T09:41:40.203437+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.718 | 0.01268 | -1.25% | 0.78x |
| 2 | VVV/USD | 67.225 | 25.063 | +0.28% | 0.57x |
| 3 | LCX/USD | 65.502 | 0.03341 | -1.71% | 1.42x |
| 4 | XMR/USD | 65.460 | 497.61 | -0.19% | 0.42x |
| 5 | PEPE/USD | 62.146 | 3.486e-06 | +0.00% | 0.52x |
| 6 | LUNA/USD | 58.080 | 4.603e-05 | -0.69% | 1.66x |
| 7 | 2Z/USD | 56.728 | 0.0163 | +0.18% | 1.24x |
| 8 | LINK/USD | 55.495 | 9.05163 | +0.13% | 0.62x |
| 9 | BABY/USD | 49.570 | 0.00891 | +0.79% | 0.15x |
| 10 | BAT/USD | 45.087 | 0.07899 | -0.58% | 1.05x |
| 11 | ATOM/USD | 35.210 | 1.2957 | +0.13% | 0.53x |
| 12 | XTZ/USD | 25.683 | 0.21375 | +0.41% | 0.47x |

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

- Persisted scans: 1557; predictions: 13409; observations: 943311.
- Matured sampled outcomes across 1/6/24/48h: 25544; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
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

**Writer:** 45367282629 · **Generation:** 1557 · **Legacy run:** 45367282629
**Main quote time:** 2026-11-24T09:41:47.228624+00:00 · **Legacy report time:** 2026-11-24T09:42:58.725483+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01268 | 70.30 | -1.25% | 0.78x | WEAK 35/100 | VERY_HIGH 78/100 | Do nothing |
| 2 | VVV/USD | 25.063 | 64.29 | +0.28% | 0.57x | MODERATE 57/100 | VERY_HIGH 76/100 | Watch |
| 3 | LUNA/USD | 4.603e-05 | 61.25 | -0.69% | 1.66x | WEAK 41/100 | VERY_HIGH 78/100 | Watch |
| 4 | LCX/USD | 0.03341 | 61.09 | -1.71% | 1.42x | MODERATE 51/100 | VERY_HIGH 77/100 | Do nothing |
| 5 | 2Z/USD ⭐ | 0.0163 | 60.07 | +0.18% | 1.24x | MODERATE 65/100 | VERY_HIGH 74/100 | Watch |
| 6 | XMR/USD | 497.61 | 58.74 | -0.19% | 0.42x | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | PEPE/USD | 3.486e-06 | 57.39 | +0.00% | 0.52x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 8 | LINK/USD | 9.05163 | 52.34 | +0.13% | 0.62x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 9 | BABY/USD | 0.00891 | 44.99 | +0.79% | 0.15x | WEAK 42/100 | EXTREME 87/100 | Do nothing |
| 10 | BAT/USD | 0.07899 | 42.66 | -0.58% | 1.05x | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing |
| 11 | ATOM/USD | 1.2957 | 31.14 | +0.13% | 0.53x | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | XTZ/USD | 0.21375 | 22.43 | +0.41% | 0.47x | WEAK 36/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INX/USD | 0.004031 | 66.78 | +0.56% | 1.28x | 4244 | MODERATE 58/100 | VERY_HIGH 72/100 | Watch |
| 2 | 2Z/USD ⭐ | 0.0163 | 61.97 | +0.18% | 1.24x | 1115 | MODERATE 66/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
