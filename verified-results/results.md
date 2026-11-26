# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T06:16:23.029235+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45766834910
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 63716d429874e92494581a5b1a7b57e3887c51f8 (atomic ledger/results publication)
**Ledger generation:** 1823 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SSV/USD | 2.492 | 86.042 | 63.864 | +7.74% | +2.93% | 1.75x | 24.2 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | INJ/USD | 6.132 | 75.072 | 60.723 | +2.99% | -0.13% | 5.11x | 4.9 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 522.94 | 74.529 | 58.993 | +1.16% | +0.11% | 7.97x | 8.2 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LINK/USD | 9.17 | 74.116 | 61.028 | +1.39% | -0.38% | 2.73x | 3.0 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 5 | QNT/USD | 147.16 | 73.572 | 57.825 | +1.63% | +0.15% | 25.30x | 6.8 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SKY/USD | 0.04382 | 70.773 | 63.744 | +4.63% | +0.14% | 1.63x | 4.6 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 7 | SOL/USD | 70.65 | 63.670 | 56.877 | +0.37% | -0.28% | 1.82x | 1.4 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ADA/USD | 0.148101 | 62.572 | 63.661 | +1.60% | -0.57% | 1.17x | 5.1 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XRP/USD | 0.95212 | 62.285 | 65.947 | +1.66% | -0.56% | 0.91x | 1.4 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 10 | LTC/USD | 43.47 | 58.898 | 66.306 | +1.78% | -0.07% | 0.29x | 2.3 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0564859 | 58.320 | 56.525 | +0.94% | -0.33% | 1.35x | 0.8 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 12 | AVAX/USD | 6.66 | 55.224 | 46.596 | +0.59% | -0.42% | 2.07x | 3.0 | 2026-11-26T06:16:14.737114+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 66.306 | 43.47 | -0.07% | 0.29x |
| 2 | XRP/USD | 65.947 | 0.95212 | -0.56% | 0.91x |
| 3 | SSV/USD | 63.864 | 2.492 | +2.93% | 1.75x |
| 4 | SKY/USD | 63.744 | 0.04382 | +0.14% | 1.63x |
| 5 | ADA/USD | 63.661 | 0.148101 | -0.57% | 1.17x |
| 6 | LINK/USD | 61.028 | 9.17 | -0.38% | 2.73x |
| 7 | INJ/USD | 60.723 | 6.132 | -0.13% | 5.11x |
| 8 | XMR/USD | 58.993 | 522.94 | +0.11% | 7.97x |
| 9 | QNT/USD | 57.825 | 147.16 | +0.15% | 25.30x |
| 10 | SOL/USD | 56.877 | 70.65 | -0.28% | 1.82x |
| 11 | XDG/USD | 56.525 | 0.0564859 | -0.33% | 1.35x |
| 12 | AVAX/USD | 46.596 | 6.66 | -0.42% | 2.07x |

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

- Persisted scans: 1823; predictions: 15611; observations: 1105251.
- Matured sampled outcomes across 1/6/24/48h: 33863; gap abstentions: 24047. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45766834910 · **Generation:** 1823 · **Legacy run:** 45766834910
**Main quote time:** 2026-11-26T06:16:23.029235+00:00 · **Legacy report time:** 2026-11-26T06:17:20.328303+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SSV/USD | 2.492 | 86.04 | +2.93% | 1.75x | STRONG 78/100 | VERY_HIGH 79/100 | Watch |
| 2 | INJ/USD | 6.132 | 75.07 | -0.13% | 5.11x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 522.94 | 74.53 | +0.11% | 7.97x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD | 9.17 | 74.12 | -0.38% | 2.73x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 5 | QNT/USD | 147.16 | 73.57 | +0.15% | 25.30x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | SKY/USD ⭐ | 0.04382 | 70.77 | +0.14% | 1.63x | STRONG 80/100 | HIGH 60/100 | Watch |
| 7 | SOL/USD | 70.65 | 63.67 | -0.28% | 1.82x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 8 | ADA/USD | 0.148101 | 62.57 | -0.57% | 1.17x | WEAK 41/100 | HIGH 68/100 | Watch |
| 9 | XRP/USD | 0.95212 | 62.28 | -0.56% | 0.91x | WEAK 36/100 | HIGH 68/100 | Watch |
| 10 | LTC/USD | 43.47 | 58.90 | -0.07% | 0.29x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XDG/USD | 0.0564859 | 58.32 | -0.33% | 1.35x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 12 | AVAX/USD | 6.66 | 55.22 | -0.42% | 2.07x | MODERATE 58/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.0438 | 76.40 | +0.14% | 1.63x | 4070 | STRONG 83/100 | HIGH 60/100 | Watch |

**Same-run overlap:** SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
