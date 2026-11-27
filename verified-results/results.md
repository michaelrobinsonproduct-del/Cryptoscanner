# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T11:32:10.012814+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45990897434
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 06ee076f53494b38c08e51e2696200950f08c7c7 (atomic ledger/results publication)
**Ledger generation:** 2001 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 757.45 | 99.272 | 98.283 | +11.12% | -0.23% | 1.22x | 3.4 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | MODERATE 60/100 | HIGH 68/100 | Watch | WATCH |
| 2 | SUI/USD | 0.688 | 88.960 | 75.555 | +3.04% | -0.32% | 3.85x | 1.5 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.99 | 85.403 | 95.899 | +6.06% | -0.17% | 0.03x | 3.0 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | ETH/USD | 1727.79 | 77.447 | 71.608 | +2.38% | -0.01% | 1.59x | 0.1 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 73.27 | 76.991 | 77.309 | +3.28% | -0.03% | 0.98x | 1.4 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0587208 | 76.989 | 76.386 | +4.16% | +0.04% | 1.04x | 0.0 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XRP/USD | 0.97755 | 73.487 | 80.481 | +3.69% | -0.20% | 0.40x | 0.7 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | PEPE/USD | 3.658e-06 | 71.419 | 77.621 | +5.18% | -0.41% | 0.58x | 5.5 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XBT/USD | 61710.5 | 70.851 | 69.021 | +2.00% | +0.07% | 1.15x | 0.0 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 10 | LINK/USD | 9.52863 | 64.005 | 72.754 | +2.81% | -0.06% | 0.16x | 3.8 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | DOT/USD | 0.6845 | 61.636 | 45.317 | +1.78% | +0.26% | 4.84x | 1.5 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Watch | WATCH |
| 12 | PAXG/USD | 3662.48 | 53.699 | 62.192 | +2.97% | +0.05% | 0.13x | 0.0 | 2026-11-27T11:32:02.066461+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.283 | 757.45 | -0.23% | 1.22x |
| 2 | HYPE/USD | 95.899 | 65.99 | -0.17% | 0.03x |
| 3 | XRP/USD | 80.481 | 0.97755 | -0.20% | 0.40x |
| 4 | PEPE/USD | 77.621 | 3.658e-06 | -0.41% | 0.58x |
| 5 | SOL/USD | 77.309 | 73.27 | -0.03% | 0.98x |
| 6 | XDG/USD | 76.386 | 0.0587208 | +0.04% | 1.04x |
| 7 | SUI/USD | 75.555 | 0.688 | -0.32% | 3.85x |
| 8 | LINK/USD | 72.754 | 9.52863 | -0.06% | 0.16x |
| 9 | ETH/USD | 71.608 | 1727.79 | -0.01% | 1.59x |
| 10 | XBT/USD | 69.021 | 61710.5 | +0.07% | 1.15x |
| 11 | PAXG/USD | 62.192 | 3662.48 | +0.05% | 0.13x |
| 12 | DOT/USD | 45.317 | 0.6845 | +0.26% | 4.84x |

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

- Persisted scans: 2001; predictions: 17714; observations: 1211752.
- Matured sampled outcomes across 1/6/24/48h: 39389; gap abstentions: 25807. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45990897434 · **Generation:** 2001 · **Legacy run:** 45990897434
**Main quote time:** 2026-11-27T11:32:10.012814+00:00 · **Legacy report time:** 2026-11-27T11:32:58.290755+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 757.45 | 99.27 | -0.23% | 1.22x | MODERATE 60/100 | HIGH 68/100 | Watch |
| 2 | SUI/USD | 0.688 | 88.96 | -0.32% | 3.85x | STRONG 74/100 | HIGH 61/100 | Watch |
| 3 | HYPE/USD | 65.99 | 85.40 | -0.17% | 0.03x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 4 | ETH/USD | 1727.79 | 77.45 | -0.01% | 1.59x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD | 73.27 | 76.99 | -0.03% | 0.98x | WEAK 43/100 | HIGH 68/100 | Watch |
| 6 | XDG/USD | 0.0587208 | 76.99 | +0.04% | 1.04x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 7 | XRP/USD | 0.97755 | 73.49 | -0.20% | 0.40x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 8 | PEPE/USD | 3.658e-06 | 71.42 | -0.41% | 0.58x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 9 | XBT/USD | 61710.5 | 70.85 | +0.07% | 1.15x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 10 | LINK/USD | 9.52863 | 64.00 | -0.06% | 0.16x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | DOT/USD | 0.6845 | 61.64 | +0.26% | 4.84x | STRONG 86/100 | HIGH 60/100 | Watch |
| 12 | PAXG/USD | 3662.48 | 53.70 | +0.05% | 0.13x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 27.226 | 89.93 | +0.43% | 2.34x | 9523 | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 2 | INJ/USD | 6.481 | 88.73 | +0.19% | 4.69x | 4873 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
