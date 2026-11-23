# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T17:21:46.885651+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45226422430
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 184c3c2cc29c20a8cd657c1b7a9b887e51b89a24 (atomic ledger/results publication)
**Ledger generation:** 1459 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.151929 | 98.211 | 88.984 | +5.07% | -0.01% | 1.93x | 3.0 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 2 | INJ/USD | 6.736 | 92.788 | 94.687 | +8.16% | -0.71% | 1.16x | 5.9 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 56/100 | HIGH 68/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.8 | 92.668 | 83.895 | +4.35% | +0.02% | 1.87x | 3.0 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6979 | 91.788 | 98.567 | +6.44% | -0.13% | 0.39x | 2.9 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | LTC/USD | 42.21 | 89.247 | 88.362 | +5.10% | -0.12% | 1.15x | 4.7 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 55/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SOL/USD | 74.16 | 88.766 | 89.311 | +5.00% | -0.12% | 1.01x | 1.3 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 54/100 | HIGH 68/100 | Watch | WATCH |
| 7 | UNI/USD | 5.0119 | 84.897 | 93.266 | +7.06% | -0.05% | 0.19x | 5.4 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0578619 | 84.638 | 86.097 | +4.66% | +0.11% | 0.80x | 3.1 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ZEC/USD | 833.35 | 80.645 | 84.538 | +4.49% | -0.69% | 0.96x | 3.8 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XRP/USD | 0.96968 | 80.234 | 86.596 | +4.54% | +0.06% | 0.33x | 0.4 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XLM/USD | 0.132556 | 79.832 | 82.410 | +3.94% | -0.21% | 0.85x | 0.4 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 12 | LINK/USD | 9.1742 | 74.864 | 81.521 | +4.12% | -0.09% | 0.38x | 4.6 | 2026-11-23T17:21:38.657256+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SUI/USD | 98.567 | 0.6979 | -0.13% | 0.39x |
| 2 | INJ/USD | 94.687 | 6.736 | -0.71% | 1.16x |
| 3 | UNI/USD | 93.266 | 5.0119 | -0.05% | 0.19x |
| 4 | SOL/USD | 89.311 | 74.16 | -0.12% | 1.01x |
| 5 | ADA/USD | 88.984 | 0.151929 | -0.01% | 1.93x |
| 6 | LTC/USD | 88.362 | 42.21 | -0.12% | 1.15x |
| 7 | XRP/USD | 86.596 | 0.96968 | +0.06% | 0.33x |
| 8 | XDG/USD | 86.097 | 0.0578619 | +0.11% | 0.80x |
| 9 | ZEC/USD | 84.538 | 833.35 | -0.69% | 0.96x |
| 10 | HYPE/USD | 83.895 | 65.8 | +0.02% | 1.87x |
| 11 | XLM/USD | 82.410 | 0.132556 | -0.21% | 0.85x |
| 12 | LINK/USD | 81.521 | 9.1742 | -0.09% | 0.38x |

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

- Persisted scans: 1459; predictions: 12275; observations: 883633.
- Matured sampled outcomes across 1/6/24/48h: 21352; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45226422430 · **Generation:** 1459 · **Legacy run:** 45226422430
**Main quote time:** 2026-11-23T17:21:46.885651+00:00 · **Legacy report time:** 2026-11-23T17:22:40.853718+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD | 0.151929 | 98.21 | -0.01% | 1.93x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 2 | INJ/USD | 6.736 | 92.79 | -0.71% | 1.16x | MODERATE 56/100 | HIGH 68/100 | Watch |
| 3 | HYPE/USD | 65.8 | 92.67 | +0.02% | 1.87x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | SUI/USD | 0.6979 | 91.79 | -0.13% | 0.39x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 5 | LTC/USD | 42.21 | 89.25 | -0.12% | 1.15x | MODERATE 55/100 | HIGH 68/100 | Watch |
| 6 | SOL/USD | 74.16 | 88.77 | -0.12% | 1.01x | MODERATE 54/100 | HIGH 68/100 | Watch |
| 7 | UNI/USD | 5.0119 | 84.90 | -0.05% | 0.19x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 8 | XDG/USD | 0.0578619 | 84.64 | +0.11% | 0.80x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 9 | ZEC/USD | 833.35 | 80.65 | -0.69% | 0.96x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 10 | XRP/USD | 0.96968 | 80.23 | +0.06% | 0.33x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 11 | XLM/USD | 0.132556 | 79.83 | -0.21% | 0.85x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 12 | LINK/USD | 9.1742 | 74.86 | -0.09% | 0.38x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 161.99 | 89.45 | +0.89% | 1.44x | 10885 | STRONG 90/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
