# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T20:41:43.272197+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45261649430
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 240b1aad523744b5acc699ac130261757694adfd (atomic ledger/results publication)
**Ledger generation:** 1479 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08291 | 97.747 | 92.178 | +9.92% | -0.48% | 1.80x | 4.8 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 2 | QNT/USD | 158.57 | 90.527 | 96.849 | +10.55% | -0.14% | 0.44x | 6.3 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | INJ/USD | 6.482 | 71.573 | 78.765 | +4.08% | -0.69% | 0.63x | 6.2 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | UNI/USD | 4.8656 | 69.968 | 75.837 | +3.94% | -0.36% | 0.60x | 7.6 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SOL/USD | 72.8 | 69.358 | 75.820 | +3.07% | -0.44% | 0.57x | 1.4 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.2766 | 68.375 | 72.980 | +8.92% | -0.07% | 0.57x | 10.2 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | LTC/USD | 41.32 | 67.094 | 74.010 | +2.89% | -0.46% | 0.54x | 2.4 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6746 | 65.547 | 74.435 | +2.88% | -0.53% | 0.38x | 1.5 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | CC/USD | 0.0776 | 65.476 | 73.386 | +5.91% | -0.26% | 0.34x | 9.0 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0566296 | 60.917 | 71.290 | +2.43% | -0.54% | 0.23x | 1.5 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | PAXG/USD | 3628.27 | 60.514 | 62.083 | +1.57% | -0.02% | 0.85x | 0.0 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XRP/USD | 0.93766 | 54.970 | 62.104 | +1.09% | -0.65% | 0.61x | 1.1 | 2026-11-23T20:41:37.530170+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 96.849 | 158.57 | -0.14% | 0.44x |
| 2 | ALGO/USD | 92.178 | 0.08291 | -0.48% | 1.80x |
| 3 | INJ/USD | 78.765 | 6.482 | -0.69% | 0.63x |
| 4 | UNI/USD | 75.837 | 4.8656 | -0.36% | 0.60x |
| 5 | SOL/USD | 75.820 | 72.8 | -0.44% | 0.57x |
| 6 | SUI/USD | 74.435 | 0.6746 | -0.53% | 0.38x |
| 7 | LTC/USD | 74.010 | 41.32 | -0.46% | 0.54x |
| 8 | CC/USD | 73.386 | 0.0776 | -0.26% | 0.34x |
| 9 | ATOM/USD | 72.980 | 1.2766 | -0.07% | 0.57x |
| 10 | XDG/USD | 71.290 | 0.0566296 | -0.54% | 0.23x |
| 11 | XRP/USD | 62.104 | 0.93766 | -0.65% | 0.61x |
| 12 | PAXG/USD | 62.083 | 3628.27 | -0.02% | 0.85x |

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

- Persisted scans: 1479; predictions: 12515; observations: 895813.
- Matured sampled outcomes across 1/6/24/48h: 22336; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45261649430 · **Generation:** 1479 · **Legacy run:** 45261649430
**Main quote time:** 2026-11-23T20:41:43.272197+00:00 · **Legacy report time:** 2026-11-23T20:42:32.177605+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08291 | 97.75 | -0.48% | 1.80x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 2 | QNT/USD | 158.57 | 90.53 | -0.14% | 0.44x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 3 | INJ/USD | 6.482 | 71.57 | -0.69% | 0.63x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 4 | UNI/USD | 4.8656 | 69.97 | -0.36% | 0.60x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 5 | SOL/USD | 72.8 | 69.36 | -0.44% | 0.57x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 6 | ATOM/USD | 1.2766 | 68.37 | -0.07% | 0.57x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 7 | LTC/USD | 41.32 | 67.09 | -0.46% | 0.54x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 8 | SUI/USD | 0.6746 | 65.55 | -0.53% | 0.38x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 9 | CC/USD | 0.0776 | 65.48 | -0.26% | 0.34x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 10 | XDG/USD | 0.0566296 | 60.92 | -0.54% | 0.23x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | PAXG/USD | 3628.27 | 60.51 | -0.02% | 0.85x | WEAK 35/100 | HIGH 68/100 | Watch |
| 12 | XRP/USD | 0.93766 | 54.97 | -0.65% | 0.61x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

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
