# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T11:01:46.200759+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45379968410
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4006628d4c29259b392dd6cf261a60093cb16c0b (atomic ledger/results publication)
**Ledger generation:** 1565 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.316 | 97.130 | 76.281 | +3.55% | +1.17% | 3.40x | 7.1 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.01259 | 79.100 | 82.476 | +9.29% | -0.47% | 0.90x | 7.9 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 3 | XMR/USD | 497.34 | 64.656 | 67.676 | +2.33% | +0.27% | 0.56x | 7.3 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.478e-06 | 63.392 | 60.999 | +1.64% | +0.84% | 0.82x | 2.9 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 5 | BAT/USD | 0.07821 | 58.624 | 41.247 | +1.35% | +0.48% | 2.77x | 1.3 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 6 | ARB/USD | 0.1137 | 56.636 | 39.426 | +0.98% | +0.44% | 4.10x | 8.8 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 7 | GBP/USD | 1.30686 | 50.998 | 56.862 | +0.28% | +0.04% | 0.39x | 0.2 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | 2Z/USD | 0.01606 | 48.862 | 45.923 | +2.62% | +0.06% | 1.26x | 6.2 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |
| 9 | XDC/USD | 0.02622 | 48.429 | 35.897 | +0.92% | -0.49% | 15.95x | 11.4 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | DBR/USD | 0.01432 | 47.635 | 55.146 | +6.71% | -0.35% | 0.42x | 42.0 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | WEAK 14/100 | EXTREME 100/100 | Do nothing | WATCH |
| 11 | INX/USD | 0.003935 | 43.570 | 21.837 | +0.95% | +1.35% | 2.89x | 33.1 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 12 | BABY/USD | 0.00857 | 31.931 | 32.553 | +0.82% | -0.12% | 1.00x | 11.7 | 2026-11-24T11:01:41.335687+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 82.476 | 0.01259 | -0.47% | 0.90x |
| 2 | VVV/USD | 76.281 | 25.316 | +1.17% | 3.40x |
| 3 | XMR/USD | 67.676 | 497.34 | +0.27% | 0.56x |
| 4 | PEPE/USD | 60.999 | 3.478e-06 | +0.84% | 0.82x |
| 5 | GBP/USD | 56.862 | 1.30686 | +0.04% | 0.39x |
| 6 | DBR/USD | 55.146 | 0.01432 | -0.35% | 0.42x |
| 7 | 2Z/USD | 45.923 | 0.01606 | +0.06% | 1.26x |
| 8 | BAT/USD | 41.247 | 0.07821 | +0.48% | 2.77x |
| 9 | ARB/USD | 39.426 | 0.1137 | +0.44% | 4.10x |
| 10 | XDC/USD | 35.897 | 0.02622 | -0.49% | 15.95x |
| 11 | BABY/USD | 32.553 | 0.00857 | -0.12% | 1.00x |
| 12 | INX/USD | 21.837 | 0.003935 | +1.35% | 2.89x |

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

- Persisted scans: 1565; predictions: 13487; observations: 948183.
- Matured sampled outcomes across 1/6/24/48h: 25897; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45379968410 · **Generation:** 1565 · **Legacy run:** 45379968410
**Main quote time:** 2026-11-24T11:01:46.200759+00:00 · **Legacy report time:** 2026-11-24T11:02:57.978763+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.316 | 97.13 | +1.17% | 3.40x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | MON/USD | 0.01259 | 79.10 | -0.47% | 0.90x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 3 | XMR/USD | 497.34 | 64.66 | +0.27% | 0.56x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 4 | PEPE/USD | 3.478e-06 | 63.39 | +0.84% | 0.82x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 5 | BAT/USD ⭐ | 0.07821 | 58.62 | +0.48% | 2.77x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 6 | ARB/USD ⭐ | 0.1137 | 56.64 | +0.44% | 4.10x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 7 | GBP/USD | 1.30686 | 51.00 | +0.04% | 0.39x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 8 | 2Z/USD ⭐ | 0.01606 | 48.86 | +0.06% | 1.26x | MODERATE 59/100 | HIGH 67/100 | Watch |
| 9 | XDC/USD | 0.02622 | 48.43 | -0.49% | 15.95x | MODERATE 49/100 | VERY_HIGH 72/100 | Watch |
| 10 | DBR/USD | 0.01432 | 47.63 | -0.35% | 0.42x | WEAK 14/100 | EXTREME 100/100 | Do nothing |
| 11 | INX/USD | 0.003935 | 43.57 | +1.35% | 2.89x | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |
| 12 | BABY/USD | 0.00857 | 31.93 | -0.12% | 1.00x | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.17 | 83.95 | +1.17% | 3.40x | 13541 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | BAT/USD ⭐ | 0.078 | 52.17 | +0.48% | 2.77x | 3793 | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 3 | ARB/USD ⭐ | 0.1137 | 47.09 | +0.44% | 4.10x | 2622 | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 4 | 2Z/USD ⭐ | 0.01606 | 45.34 | +0.06% | 1.26x | 1165 | MODERATE 58/100 | HIGH 67/100 | Watch |
| 5 | NIGHT/USD | 0.04825 | 37.97 | +0.40% | 1.25x | 12343 | MODERATE 54/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, BAT/USD, ARB/USD, 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
