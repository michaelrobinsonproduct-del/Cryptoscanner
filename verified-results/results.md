# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T09:21:41.859950+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45972758096
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 18a12a62edb079949b42f64975fcf2a0e872bbc2 (atomic ledger/results publication)
**Ledger generation:** 1988 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 752.66 | 111.559 | 97.408 | +10.42% | -0.17% | 3.53x | 5.2 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SOL/USD | 73.43 | 86.926 | 78.889 | +3.51% | +0.03% | 1.79x | 1.4 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.55 | 83.371 | 90.937 | +5.35% | -0.17% | 0.33x | 3.1 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | XRP/USD | 0.97511 | 81.427 | 78.617 | +3.43% | -0.23% | 1.40x | 0.8 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 5 | UNI/USD | 4.8984 | 79.597 | 79.590 | +5.34% | +0.15% | 0.93x | 4.7 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0580936 | 74.204 | 68.295 | +3.05% | -0.11% | 1.65x | 0.1 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ENA/USD | 0.1071 | 70.491 | 76.917 | +6.67% | +0.00% | 0.36x | 9.3 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | VVV/USD | 27.02 | 69.061 | 73.066 | +3.20% | -0.14% | 0.67x | 3.7 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | FET/USD | 0.1282 | 67.996 | 72.435 | +6.48% | +0.47% | 0.32x | 15.6 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | LINK/USD | 9.56551 | 67.278 | 76.459 | +3.21% | -0.43% | 0.29x | 2.0 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | W/USD | 0.00936 | 65.753 | 72.163 | +6.24% | -1.37% | 1.04x | 10.7 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 12 | XBT/USD | 61617.7 | 65.529 | 67.948 | +1.85% | -0.14% | 0.83x | 0.0 | 2026-11-27T09:21:35.851008+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.408 | 752.66 | -0.17% | 3.53x |
| 2 | HYPE/USD | 90.937 | 65.55 | -0.17% | 0.33x |
| 3 | UNI/USD | 79.590 | 4.8984 | +0.15% | 0.93x |
| 4 | SOL/USD | 78.889 | 73.43 | +0.03% | 1.79x |
| 5 | XRP/USD | 78.617 | 0.97511 | -0.23% | 1.40x |
| 6 | ENA/USD | 76.917 | 0.1071 | +0.00% | 0.36x |
| 7 | LINK/USD | 76.459 | 9.56551 | -0.43% | 0.29x |
| 8 | VVV/USD | 73.066 | 27.02 | -0.14% | 0.67x |
| 9 | FET/USD | 72.435 | 0.1282 | +0.47% | 0.32x |
| 10 | W/USD | 72.163 | 0.00936 | -1.37% | 1.04x |
| 11 | XDG/USD | 68.295 | 0.0580936 | -0.11% | 1.65x |
| 12 | XBT/USD | 67.948 | 61617.7 | -0.14% | 0.83x |

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

- Persisted scans: 1988; predictions: 17558; observations: 1203917.
- Matured sampled outcomes across 1/6/24/48h: 38909; gap abstentions: 25724. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45972758096 · **Generation:** 1988 · **Legacy run:** 45972758096
**Main quote time:** 2026-11-27T09:21:41.859950+00:00 · **Legacy report time:** 2026-11-27T09:22:23.540077+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 752.66 | 111.56 | -0.17% | 3.53x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | SOL/USD | 73.43 | 86.93 | +0.03% | 1.79x | STRONG 78/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD | 65.55 | 83.37 | -0.17% | 0.33x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 4 | XRP/USD | 0.97511 | 81.43 | -0.23% | 1.40x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.8984 | 79.60 | +0.15% | 0.93x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 6 | XDG/USD | 0.0580936 | 74.20 | -0.11% | 1.65x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | ENA/USD | 0.1071 | 70.49 | +0.00% | 0.36x | MODERATE 55/100 | VERY_HIGH 75/100 | Watch |
| 8 | VVV/USD | 27.02 | 69.06 | -0.14% | 0.67x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 9 | FET/USD | 0.1282 | 68.00 | +0.47% | 0.32x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 10 | LINK/USD | 9.56551 | 67.28 | -0.43% | 0.29x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 11 | W/USD | 0.00936 | 65.75 | -1.37% | 1.04x | WEAK 38/100 | VERY_HIGH 83/100 | Do nothing |
| 12 | XBT/USD | 61617.7 | 65.53 | -0.14% | 0.83x | WEAK 38/100 | HIGH 68/100 | Watch |

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
