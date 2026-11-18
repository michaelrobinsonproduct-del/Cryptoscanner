# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:20:19.408334+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44323011410
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 6fb428132c202f73b02d20b0fe64f908f2801185 (atomic ledger/results publication)
**Ledger generation:** 587 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04678 | 77.900 | 73.642 | +4.21% | -0.30% | 1.57x | 8.6 | 2026-11-18T14:20:10.964136+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019431 | 68.483 | 56.027 | +4.08% | +0.60% | 1.95x | 7.2 | 2026-11-18T14:20:10.964136+00:00 | Not calibrated | STRONG 79/100 | HIGH 67/100 | Watch | WATCH |
| 3 | XRP/USD | 0.98673 | 56.161 | 57.942 | +0.43% | -0.10% | 0.87x | 0.1 | 2026-11-18T14:20:10.964136+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | VVV/USD | 21.272 | 55.270 | 54.052 | +1.17% | +0.38% | 0.93x | 5.2 | 2026-11-18T14:20:10.964136+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.8542 | 45.546 | 47.964 | +2.41% | +1.04% | 0.24x | 14.6 | 2026-11-18T14:20:10.964136+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5226 | 41.511 | 45.012 | +2.61% | +0.46% | 0.42x | 11.5 | 2026-11-18T14:20:10.964136+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | TRX/USD | 0.309657 | 40.655 | 45.476 | +0.57% | +0.01% | 0.51x | 0.4 | 2026-11-18T14:20:10.964136+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CC/USD | 0.08309 | 40.593 | 39.971 | +1.17% | +0.24% | 0.94x | 7.2 | 2026-11-18T14:20:10.964136+00:00 | Not calibrated | MODERATE 50/100 | HIGH 67/100 | Watch | WATCH |
| 9 | W/USD | 0.00902 | 27.649 | 33.230 | +1.01% | +0.00% | 0.44x | 11.1 | 2026-11-18T14:20:10.964136+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 73.642 | 0.04678 | -0.30% | 1.57x |
| 2 | XRP/USD | 57.942 | 0.98673 | -0.10% | 0.87x |
| 3 | SENT/USD | 56.027 | 0.019431 | +0.60% | 1.95x |
| 4 | VVV/USD | 54.052 | 21.272 | +0.38% | 0.93x |
| 5 | PEARL/USD | 47.964 | 1.8542 | +1.04% | 0.24x |
| 6 | TRX/USD | 45.476 | 0.309657 | +0.01% | 0.51x |
| 7 | AKT/USD | 45.012 | 0.5226 | +0.46% | 0.42x |
| 8 | CC/USD | 39.971 | 0.08309 | +0.24% | 0.94x |
| 9 | W/USD | 33.230 | 0.00902 | +0.00% | 0.44x |

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

- Persisted scans: 587; predictions: 4994; observations: 354490.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44323011410 · **Generation:** 587 · **Legacy run:** 44323011410
**Main quote time:** 2026-11-18T14:20:19.408334+00:00 · **Legacy report time:** 2026-11-18T14:20:46.146310+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04678 | 77.90 | -0.30% | 1.57x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019431 | 68.48 | +0.60% | 1.95x | STRONG 89/100 | HIGH 67/100 | Consider small entry |
| 3 | XRP/USD | 0.98673 | 56.16 | -0.10% | 0.87x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 4 | VVV/USD | 21.272 | 55.27 | +0.38% | 0.93x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 5 | PEARL/USD | 1.8542 | 45.55 | +1.04% | 0.24x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 6 | AKT/USD | 0.5226 | 41.51 | +0.46% | 0.42x | MODERATE 46/100 | VERY_HIGH 81/100 | Watch |
| 7 | TRX/USD | 0.309657 | 40.66 | +0.01% | 0.51x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 8 | CC/USD | 0.08309 | 40.59 | +0.24% | 0.94x | MODERATE 50/100 | HIGH 67/100 | Watch |
| 9 | W/USD | 0.00902 | 27.65 | +0.00% | 0.44x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019351 | 72.05 | +0.60% | 1.95x | 5675 | STRONG 86/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
