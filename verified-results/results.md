# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T06:56:39.803514+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45771469244
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2da157eff1dac9732e0b66f5d601f342a6642401 (atomic ledger/results publication)
**Ledger generation:** 1827 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07102 | 75.156 | 67.281 | +7.17% | +0.94% | 1.32x | 19.7 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Watch | WATCH |
| 2 | LINK/USD | 9.14393 | 74.642 | 62.101 | +1.10% | -0.49% | 8.38x | 0.0 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 43.35 | 69.070 | 63.182 | +1.50% | -0.55% | 1.86x | 4.6 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XDG/USD | 0.056287 | 63.955 | 54.690 | +0.59% | -0.27% | 2.06x | 0.2 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XRP/USD | 0.94917 | 61.003 | 64.372 | +1.35% | -0.21% | 0.77x | 0.1 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ADA/USD | 0.148022 | 60.424 | 64.699 | +1.54% | -0.18% | 0.66x | 2.2 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | SOL/USD | 70.57 | 59.724 | 56.082 | +0.26% | -0.17% | 1.45x | 1.4 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 8 | TAO/USD | 182.2971 | 53.897 | 54.741 | +0.39% | -0.32% | 1.07x | 5.9 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | QNT/USD | 147.85 | 52.355 | 61.895 | +2.11% | +0.02% | 0.04x | 5.4 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | INJ/USD | 6.107 | 51.306 | 58.599 | +2.57% | -0.47% | 0.51x | 3.3 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | SKY/USD | 0.04358 | 49.682 | 57.400 | +4.06% | -0.30% | 0.38x | 9.2 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | ATOM/USD | 1.2391 | 48.193 | 31.817 | +0.28% | +0.28% | 6.02x | 9.7 | 2026-11-26T06:56:31.780884+00:00 | Not calibrated | STRONG 79/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 67.281 | 0.07102 | +0.94% | 1.32x |
| 2 | ADA/USD | 64.699 | 0.148022 | -0.18% | 0.66x |
| 3 | XRP/USD | 64.372 | 0.94917 | -0.21% | 0.77x |
| 4 | LTC/USD | 63.182 | 43.35 | -0.55% | 1.86x |
| 5 | LINK/USD | 62.101 | 9.14393 | -0.49% | 8.38x |
| 6 | QNT/USD | 61.895 | 147.85 | +0.02% | 0.04x |
| 7 | INJ/USD | 58.599 | 6.107 | -0.47% | 0.51x |
| 8 | SKY/USD | 57.400 | 0.04358 | -0.30% | 0.38x |
| 9 | SOL/USD | 56.082 | 70.57 | -0.17% | 1.45x |
| 10 | TAO/USD | 54.741 | 182.2971 | -0.32% | 1.07x |
| 11 | XDG/USD | 54.690 | 0.056287 | -0.27% | 2.06x |
| 12 | ATOM/USD | 31.817 | 1.2391 | +0.28% | 6.02x |

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

- Persisted scans: 1827; predictions: 15659; observations: 1107687.
- Matured sampled outcomes across 1/6/24/48h: 33950; gap abstentions: 24138. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45771469244 · **Generation:** 1827 · **Legacy run:** 45771469244
**Main quote time:** 2026-11-26T06:56:39.803514+00:00 · **Legacy report time:** 2026-11-26T06:57:57.296969+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07102 | 75.16 | +0.94% | 1.32x | STRONG 88/100 | HIGH 66/100 | Watch |
| 2 | LINK/USD | 9.14393 | 74.64 | -0.49% | 8.38x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 43.35 | 69.07 | -0.55% | 1.86x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 4 | XDG/USD | 0.056287 | 63.95 | -0.27% | 2.06x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 5 | XRP/USD | 0.94917 | 61.00 | -0.21% | 0.77x | WEAK 36/100 | HIGH 68/100 | Watch |
| 6 | ADA/USD | 0.148022 | 60.42 | -0.18% | 0.66x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 7 | SOL/USD | 70.57 | 59.72 | -0.17% | 1.45x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 8 | TAO/USD | 182.2971 | 53.90 | -0.32% | 1.07x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | QNT/USD | 147.85 | 52.36 | +0.02% | 0.04x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 10 | INJ/USD | 6.107 | 51.31 | -0.47% | 0.51x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | SKY/USD | 0.04358 | 49.68 | -0.30% | 0.38x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | ATOM/USD | 1.2391 | 48.19 | +0.28% | 6.02x | STRONG 79/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07105 | 75.38 | +0.94% | 1.32x | 3675 | STRONG 83/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
