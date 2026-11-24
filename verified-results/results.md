# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T10:21:46.773696+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45373702216
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4be593c5afc8b31e5c5fb8c1cf25765bda7a9a36 (atomic ledger/results publication)
**Ledger generation:** 1561 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01255 | 81.492 | 78.460 | +8.94% | +0.56% | 1.02x | 16.0 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | STRONG 71/100 | HIGH 68/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.482e-06 | 75.949 | 60.230 | +1.75% | +0.14% | 3.69x | 5.7 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | VVV/USD | 25.227 | 73.952 | 73.347 | +3.19% | +0.26% | 0.93x | 7.9 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XMR/USD | 495.96 | 67.478 | 63.367 | +2.05% | -0.01% | 1.41x | 11.9 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ICNT/USD | 0.3372 | 61.033 | 64.397 | +9.09% | +0.92% | 0.20x | 26.8 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | LUNA/USD | 4.687e-05 | 57.925 | 55.838 | +7.82% | +0.41% | 1.01x | 42.6 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 89/100 | Do nothing | WATCH |
| 7 | 2Z/USD | 0.0161 | 47.456 | 47.741 | +2.88% | -0.06% | 1.00x | 6.2 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 8 | BAT/USD | 0.07804 | 46.241 | 35.147 | +1.13% | +0.35% | 1.94x | 10.3 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 9 | ATOM/USD | 1.2901 | 43.266 | 31.770 | +0.62% | -0.02% | 2.16x | 11.6 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | INX/USD | 0.003958 | 23.596 | 33.587 | +1.54% | -0.38% | 0.19x | 17.8 | 2026-11-24T10:21:39.788647+00:00 | Not calibrated | WEAK 12/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.460 | 0.01255 | +0.56% | 1.02x |
| 2 | VVV/USD | 73.347 | 25.227 | +0.26% | 0.93x |
| 3 | ICNT/USD | 64.397 | 0.3372 | +0.92% | 0.20x |
| 4 | XMR/USD | 63.367 | 495.96 | -0.01% | 1.41x |
| 5 | PEPE/USD | 60.230 | 3.482e-06 | +0.14% | 3.69x |
| 6 | LUNA/USD | 55.838 | 4.687e-05 | +0.41% | 1.01x |
| 7 | 2Z/USD | 47.741 | 0.0161 | -0.06% | 1.00x |
| 8 | BAT/USD | 35.147 | 0.07804 | +0.35% | 1.94x |
| 9 | INX/USD | 33.587 | 0.003958 | -0.38% | 0.19x |
| 10 | ATOM/USD | 31.770 | 1.2901 | -0.02% | 2.16x |

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

- Persisted scans: 1561; predictions: 13447; observations: 945747.
- Matured sampled outcomes across 1/6/24/48h: 25714; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
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

**Writer:** 45373702216 · **Generation:** 1561 · **Legacy run:** 45373702216
**Main quote time:** 2026-11-24T10:21:46.773696+00:00 · **Legacy report time:** 2026-11-24T10:22:58.961198+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01255 | 81.49 | +0.56% | 1.02x | STRONG 81/100 | HIGH 68/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.482e-06 | 75.95 | +0.14% | 3.69x | STRONG 93/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD | 25.227 | 73.95 | +0.26% | 0.93x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 4 | XMR/USD | 495.96 | 67.48 | -0.01% | 1.41x | MODERATE 49/100 | HIGH 67/100 | Watch |
| 5 | ICNT/USD | 0.3372 | 61.03 | +0.92% | 0.20x | MODERATE 51/100 | EXTREME 87/100 | Do nothing |
| 6 | LUNA/USD ⭐ | 4.687e-05 | 57.92 | +0.41% | 1.01x | MODERATE 59/100 | EXTREME 89/100 | Do nothing |
| 7 | 2Z/USD | 0.0161 | 47.46 | -0.06% | 1.00x | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing |
| 8 | BAT/USD | 0.07804 | 46.24 | +0.35% | 1.94x | MODERATE 63/100 | HIGH 66/100 | Watch |
| 9 | ATOM/USD | 1.2901 | 43.27 | -0.02% | 2.16x | MODERATE 47/100 | VERY_HIGH 72/100 | Watch |
| 10 | INX/USD | 0.003958 | 23.60 | -0.38% | 0.19x | WEAK 12/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01254 | 78.64 | +0.56% | 1.02x | 10293 | STRONG 79/100 | HIGH 68/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.707e-05 | 66.81 | +0.41% | 1.01x | 1952 | MODERATE 68/100 | VERY_HIGH 79/100 | Watch |
| 3 | PEPE/USD ⭐ | 3.479e-06 | 66.38 | +0.14% | 3.69x | 9249 | STRONG 88/100 | HIGH 55/100 | Watch |

**Same-run overlap:** MON/USD, PEPE/USD, LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
