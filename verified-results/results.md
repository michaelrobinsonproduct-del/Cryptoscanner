# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:50:11.307776+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44328540433
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 6626c6024aa5c7eb855019298ab9ba50046d48f2 (atomic ledger/results publication)
**Ledger generation:** 593 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1212 | 79.447 | 67.731 | +7.26% | +0.17% | 2.09x | 16.5 | 2026-11-18T14:50:04.299774+00:00 | Not calibrated | STRONG 80/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019716 | 67.672 | 67.551 | +5.61% | +0.71% | 0.66x | 5.6 | 2026-11-18T14:50:04.299774+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04585 | 62.135 | 56.341 | +2.14% | -1.84% | 3.83x | 13.1 | 2026-11-18T14:50:04.299774+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 4 | STABLE/USD | 0.02303 | 56.038 | 65.121 | +9.41% | -0.43% | 0.31x | 21.7 | 2026-11-18T14:50:04.299774+00:00 | Not calibrated | WEAK 23/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | VVV/USD | 21.151 | 55.862 | 48.211 | +0.59% | -0.60% | 2.06x | 9.0 | 2026-11-18T14:50:04.299774+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 6 | CC/USD | 0.08295 | 50.562 | 36.524 | +1.00% | -0.19% | 14.27x | 12.0 | 2026-11-18T14:50:04.299774+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | TRX/USD | 0.309367 | 41.135 | 44.170 | +0.48% | -0.04% | 0.72x | 0.1 | 2026-11-18T14:50:04.299774+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5188 | 36.851 | 36.777 | +1.87% | -0.54% | 1.28x | 17.3 | 2026-11-18T14:50:04.299774+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 9 | ZAMA/USD | 0.0608 | 35.685 | 36.841 | +1.45% | -0.07% | 0.92x | 9.9 | 2026-11-18T14:50:04.299774+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CT/USD | 67.731 | 0.1212 | +0.17% | 2.09x |
| 2 | SENT/USD | 67.551 | 0.019716 | +0.71% | 0.66x |
| 3 | STABLE/USD | 65.121 | 0.02303 | -0.43% | 0.31x |
| 4 | NIGHT/USD | 56.341 | 0.04585 | -1.84% | 3.83x |
| 5 | VVV/USD | 48.211 | 21.151 | -0.60% | 2.06x |
| 6 | TRX/USD | 44.170 | 0.309367 | -0.04% | 0.72x |
| 7 | ZAMA/USD | 36.841 | 0.0608 | -0.07% | 0.92x |
| 8 | AKT/USD | 36.777 | 0.5188 | -0.54% | 1.28x |
| 9 | CC/USD | 36.524 | 0.08295 | -0.19% | 14.27x |

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

- Persisted scans: 593; predictions: 5055; observations: 358144.
- Matured sampled outcomes across 1/6/24/48h: 4268; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44328540433 · **Generation:** 593 · **Legacy run:** 44328540433
**Main quote time:** 2026-11-18T14:50:11.307776+00:00 · **Legacy report time:** 2026-11-18T14:50:31.541664+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1212 | 79.45 | +0.17% | 2.09x | STRONG 90/100 | VERY_HIGH 73/100 | Watch |
| 2 | SENT/USD | 0.019716 | 67.67 | +0.71% | 0.66x | MODERATE 64/100 | VERY_HIGH 82/100 | Watch |
| 3 | NIGHT/USD | 0.04585 | 62.14 | -1.84% | 3.83x | MODERATE 56/100 | VERY_HIGH 71/100 | Do nothing |
| 4 | STABLE/USD | 0.02303 | 56.04 | -0.43% | 0.31x | WEAK 23/100 | EXTREME 100/100 | Do nothing |
| 5 | VVV/USD | 21.151 | 55.86 | -0.60% | 2.06x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 6 | CC/USD | 0.08295 | 50.56 | -0.19% | 14.27x | MODERATE 50/100 | VERY_HIGH 72/100 | Watch |
| 7 | TRX/USD | 0.309367 | 41.13 | -0.04% | 0.72x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | AKT/USD | 0.5188 | 36.85 | -0.54% | 1.28x | WEAK 23/100 | VERY_HIGH 72/100 | Do nothing |
| 9 | ZAMA/USD | 0.0608 | 35.69 | -0.07% | 0.92x | WEAK 23/100 | VERY_HIGH 80/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1212 | 63.57 | +0.17% | 2.09x | 1216 | STRONG 77/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
