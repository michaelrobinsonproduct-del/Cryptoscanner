# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T08:27:49.122164+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45576005815
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c068030bc9a03b4ca963ca8b21004bbd28f942eb (atomic ledger/results publication)
**Ledger generation:** 1693 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.0104 | 84.633 | 89.949 | +9.82% | -2.13% | 1.54x | 9.6 | 2026-11-25T08:27:40.818100+00:00 | Not calibrated | MODERATE 62/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | BABY/USD | 0.00871 | 75.441 | 58.723 | +5.45% | +0.34% | 4.36x | 23.2 | 2026-11-25T08:27:40.818100+00:00 | Not calibrated | STRONG 83/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | DRV/USD | 0.3327 | 70.883 | 74.596 | +5.86% | -0.13% | 0.69x | 7.5 | 2026-11-25T08:27:40.818100+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | VVV/USD | 24.753 | 51.550 | 58.507 | +0.88% | +0.01% | 0.30x | 5.3 | 2026-11-25T08:27:40.818100+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | AKT/USD | 0.4725 | 48.798 | 39.183 | +1.63% | +0.40% | 1.76x | 8.5 | 2026-11-25T08:27:40.818100+00:00 | Not calibrated | MODERATE 69/100 | HIGH 60/100 | Watch | WATCH |
| 6 | PROS/USD | 0.713 | 46.850 | 62.769 | +6.31% | -2.61% | 0.71x | 26.8 | 2026-11-25T08:27:40.818100+00:00 | Not calibrated | WEAK 18/100 | EXTREME 97/100 | Do nothing | WATCH |
| 7 | CC/USD | 0.07538 | 42.164 | 35.586 | +0.44% | +0.15% | 1.58x | 4.0 | 2026-11-25T08:27:40.818100+00:00 | Not calibrated | MODERATE 56/100 | HIGH 60/100 | Watch | WATCH |
| 8 | PEPE/USD | 3.48e-06 | 38.064 | 46.155 | +0.78% | -0.29% | 0.33x | 8.6 | 2026-11-25T08:27:40.818100+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | ATOM/USD | 1.2562 | 28.376 | 31.907 | +0.87% | +0.73% | 0.28x | 12.8 | 2026-11-25T08:27:40.818100+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 89.949 | 0.0104 | -2.13% | 1.54x |
| 2 | DRV/USD | 74.596 | 0.3327 | -0.13% | 0.69x |
| 3 | PROS/USD | 62.769 | 0.713 | -2.61% | 0.71x |
| 4 | BABY/USD | 58.723 | 0.00871 | +0.34% | 4.36x |
| 5 | VVV/USD | 58.507 | 24.753 | +0.01% | 0.30x |
| 6 | PEPE/USD | 46.155 | 3.48e-06 | -0.29% | 0.33x |
| 7 | AKT/USD | 39.183 | 0.4725 | +0.40% | 1.76x |
| 8 | CC/USD | 35.586 | 0.07538 | +0.15% | 1.58x |
| 9 | ATOM/USD | 31.907 | 1.2562 | +0.73% | 0.28x |

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

- Persisted scans: 1693; predictions: 14374; observations: 1026127.
- Matured sampled outcomes across 1/6/24/48h: 30862; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45576005815 · **Generation:** 1693 · **Legacy run:** 45576005815
**Main quote time:** 2026-11-25T08:27:49.122164+00:00 · **Legacy report time:** 2026-11-25T08:28:43.150660+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.0104 | 84.63 | -2.13% | 1.54x | MODERATE 62/100 | HIGH 65/100 | Do nothing |
| 2 | BABY/USD ⭐ | 0.00871 | 75.44 | +0.34% | 4.36x | STRONG 93/100 | VERY_HIGH 72/100 | Watch |
| 3 | DRV/USD | 0.3327 | 70.88 | -0.13% | 0.69x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 4 | VVV/USD | 24.753 | 51.55 | +0.01% | 0.30x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 5 | AKT/USD ⭐ | 0.4725 | 48.80 | +0.40% | 1.76x | STRONG 79/100 | HIGH 60/100 | Consider small entry |
| 6 | PROS/USD | 0.713 | 46.85 | -2.61% | 0.71x | WEAK 18/100 | EXTREME 97/100 | Do nothing |
| 7 | CC/USD ⭐ | 0.07538 | 42.16 | +0.15% | 1.58x | MODERATE 66/100 | HIGH 60/100 | Watch |
| 8 | PEPE/USD | 3.48e-06 | 38.06 | -0.29% | 0.33x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | ATOM/USD | 1.2562 | 28.38 | +0.73% | 0.28x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00868 | 80.27 | +0.34% | 4.36x | 3848 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.4725 | 49.34 | +0.40% | 1.76x | 2781 | STRONG 80/100 | HIGH 60/100 | Consider small entry |
| 3 | CC/USD ⭐ | 0.07555 | 39.87 | +0.15% | 1.58x | 5466 | MODERATE 65/100 | HIGH 60/100 | Watch |

**Same-run overlap:** BABY/USD, AKT/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
