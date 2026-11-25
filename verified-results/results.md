# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T08:37:32.543726+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45577487742
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bfc425590eee6d9728fd93d7c284ada9faf5722a (atomic ledger/results publication)
**Ledger generation:** 1694 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.0106 | 93.152 | 90.364 | +11.93% | -0.85% | 1.70x | 9.4 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | DRV/USD | 0.33279 | 74.230 | 71.956 | +5.89% | +0.09% | 1.18x | 13.2 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | MODERATE 57/100 | HIGH 68/100 | Watch | WATCH |
| 3 | VVV/USD | 24.744 | 48.553 | 56.618 | +0.84% | -0.06% | 0.22x | 8.5 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | PROS/USD | 0.7129 | 43.502 | 56.397 | +6.29% | -1.60% | 0.51x | 39.4 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | WEAK 12/100 | EXTREME 97/100 | Do nothing | WATCH |
| 5 | PEPE/USD | 3.48e-06 | 43.097 | 49.183 | +0.78% | +0.00% | 0.39x | 2.9 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | BABY/USD | 0.0086 | 35.014 | 43.126 | +4.12% | -0.46% | 0.42x | 34.9 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | WEAK 13/100 | EXTREME 93/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.4727 | 34.814 | 38.443 | +1.68% | +0.45% | 0.41x | 10.6 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | HBAR/USD | 0.05045 | 33.494 | 37.783 | +0.38% | +0.58% | 0.28x | 2.0 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | CC/USD | 0.07534 | 30.162 | 35.867 | +0.39% | -0.01% | 0.44x | 2.7 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | TON/USD | 0.935 | 25.462 | 29.949 | +0.43% | +0.65% | 0.23x | 10.7 | 2026-11-25T08:37:25.580627+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 90.364 | 0.0106 | -0.85% | 1.70x |
| 2 | DRV/USD | 71.956 | 0.33279 | +0.09% | 1.18x |
| 3 | VVV/USD | 56.618 | 24.744 | -0.06% | 0.22x |
| 4 | PROS/USD | 56.397 | 0.7129 | -1.60% | 0.51x |
| 5 | PEPE/USD | 49.183 | 3.48e-06 | +0.00% | 0.39x |
| 6 | BABY/USD | 43.126 | 0.0086 | -0.46% | 0.42x |
| 7 | AKT/USD | 38.443 | 0.4727 | +0.45% | 0.41x |
| 8 | HBAR/USD | 37.783 | 0.05045 | +0.58% | 0.28x |
| 9 | CC/USD | 35.867 | 0.07534 | -0.01% | 0.44x |
| 10 | TON/USD | 29.949 | 0.935 | +0.65% | 0.23x |

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

- Persisted scans: 1694; predictions: 14384; observations: 1026735.
- Matured sampled outcomes across 1/6/24/48h: 30900; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45577487742 · **Generation:** 1694 · **Legacy run:** 45577487742
**Main quote time:** 2026-11-25T08:37:32.543726+00:00 · **Legacy report time:** 2026-11-25T08:38:25.645136+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.0106 | 93.15 | -0.85% | 1.70x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | DRV/USD ⭐ | 0.33279 | 74.23 | +0.09% | 1.18x | MODERATE 67/100 | HIGH 68/100 | Watch |
| 3 | VVV/USD | 24.744 | 48.55 | -0.06% | 0.22x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | PROS/USD | 0.7129 | 43.50 | -1.60% | 0.51x | WEAK 12/100 | EXTREME 97/100 | Do nothing |
| 5 | PEPE/USD | 3.48e-06 | 43.10 | +0.00% | 0.39x | WEAK 42/100 | VERY_HIGH 70/100 | Watch |
| 6 | BABY/USD | 0.0086 | 35.01 | -0.46% | 0.42x | WEAK 13/100 | EXTREME 93/100 | Do nothing |
| 7 | AKT/USD | 0.4727 | 34.81 | +0.45% | 0.41x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |
| 8 | HBAR/USD | 0.05045 | 33.49 | +0.58% | 0.28x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 9 | CC/USD | 0.07534 | 30.16 | -0.01% | 0.44x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | TON/USD | 0.935 | 25.46 | +0.65% | 0.23x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33231 | 75.41 | +0.09% | 1.18x | 9149 | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
