# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:55:15.020530+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44329484493
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** bb85f8f8a86b2b1bb889922d1d116bd4583edd23 (atomic ledger/results publication)
**Ledger generation:** 594 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1213 | 81.525 | 63.623 | +7.35% | +0.58% | 4.03x | 24.7 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | STRONG 86/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019696 | 71.558 | 65.770 | +5.50% | +0.15% | 1.50x | 7.6 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | STRONG 71/100 | HIGH 67/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3866 | 70.903 | 52.780 | +3.56% | +0.62% | 3.91x | 10.4 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | STRONG 85/100 | HIGH 66/100 | Consider small entry | WATCH |
| 4 | STABLE/USD | 0.02314 | 62.455 | 65.170 | +9.93% | +0.35% | 0.56x | 21.7 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | TRX/USD | 0.309689 | 60.225 | 44.443 | +0.58% | +0.16% | 2.55x | 1.3 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.0457 | 59.951 | 55.039 | +1.80% | -1.91% | 2.45x | 11.0 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 7 | VVV/USD | 21.087 | 57.287 | 45.702 | +0.29% | -0.68% | 3.37x | 10.0 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 8 | CC/USD | 0.08294 | 55.960 | 39.570 | +0.99% | +0.28% | 12.37x | 6.0 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5201 | 48.478 | 39.536 | +2.12% | +0.46% | 1.66x | 15.4 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 10 | ZAMA/USD | 0.06079 | 35.781 | 35.891 | +1.44% | +0.12% | 0.93x | 11.5 | 2026-11-18T14:55:06.459840+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 65.770 | 0.019696 | +0.15% | 1.50x |
| 2 | STABLE/USD | 65.170 | 0.02314 | +0.35% | 0.56x |
| 3 | CT/USD | 63.623 | 0.1213 | +0.58% | 4.03x |
| 4 | NIGHT/USD | 55.039 | 0.0457 | -1.91% | 2.45x |
| 5 | MNT/USD | 52.780 | 0.3866 | +0.62% | 3.91x |
| 6 | VVV/USD | 45.702 | 21.087 | -0.68% | 3.37x |
| 7 | TRX/USD | 44.443 | 0.309689 | +0.16% | 2.55x |
| 8 | CC/USD | 39.570 | 0.08294 | +0.28% | 12.37x |
| 9 | AKT/USD | 39.536 | 0.5201 | +0.46% | 1.66x |
| 10 | ZAMA/USD | 35.891 | 0.06079 | +0.12% | 0.93x |

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

- Persisted scans: 594; predictions: 5065; observations: 358753.
- Matured sampled outcomes across 1/6/24/48h: 4286; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44329484493 · **Generation:** 594 · **Legacy run:** 44329484493
**Main quote time:** 2026-11-18T14:55:15.020530+00:00 · **Legacy report time:** 2026-11-18T14:55:43.847026+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1213 | 81.53 | +0.58% | 4.03x | STRONG 96/100 | VERY_HIGH 79/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019696 | 71.56 | +0.15% | 1.50x | STRONG 81/100 | HIGH 67/100 | Watch |
| 3 | MNT/USD ⭐ | 0.3866 | 70.90 | +0.62% | 3.91x | STRONG 95/100 | HIGH 66/100 | Consider small entry |
| 4 | STABLE/USD | 0.02314 | 62.46 | +0.35% | 0.56x | MODERATE 51/100 | EXTREME 94/100 | Do nothing |
| 5 | TRX/USD ⭐ | 0.309689 | 60.23 | +0.16% | 2.55x | STRONG 85/100 | HIGH 55/100 | Watch |
| 6 | NIGHT/USD | 0.0457 | 59.95 | -1.91% | 2.45x | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing |
| 7 | VVV/USD | 21.087 | 57.29 | -0.68% | 3.37x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 8 | CC/USD ⭐ | 0.08294 | 55.96 | +0.28% | 12.37x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 9 | AKT/USD ⭐ | 0.5201 | 48.48 | +0.46% | 1.66x | STRONG 74/100 | HIGH 66/100 | Watch |
| 10 | ZAMA/USD | 0.06079 | 35.78 | +0.12% | 0.93x | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019715 | 74.92 | +0.15% | 1.50x | 5752 | STRONG 82/100 | HIGH 67/100 | Watch |
| 2 | MNT/USD ⭐ | 0.3866 | 71.12 | +0.62% | 3.91x | 2002 | STRONG 96/100 | HIGH 66/100 | Consider small entry |
| 3 | CT/USD ⭐ | 0.1213 | 68.51 | +0.58% | 4.03x | 1222 | STRONG 89/100 | VERY_HIGH 79/100 | Watch |
| 4 | TRX/USD ⭐ | 0.309652 | 55.07 | +0.16% | 2.55x | 4236 | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | AKT/USD ⭐ | 0.5201 | 52.93 | +0.46% | 1.66x | 4705 | STRONG 76/100 | HIGH 66/100 | Consider small entry |
| 6 | CC/USD ⭐ | 0.08291 | 45.64 | +0.28% | 12.37x | 4815 | STRONG 88/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** CT/USD, SENT/USD, MNT/USD, TRX/USD, CC/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
