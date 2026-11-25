# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T12:42:18.772849+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45615875492
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a50b948f36954d0ecf31071df3c838ce9c8c0f75 (atomic ledger/results publication)
**Ledger generation:** 1719 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BABY/USD | 0.00884 | 82.506 | 70.886 | +7.02% | -0.67% | 2.50x | 11.3 | 2026-11-25T12:42:14.614553+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | VVV/USD | 25.192 | 75.596 | 69.289 | +2.67% | +0.53% | 1.37x | 8.7 | 2026-11-25T12:42:14.614553+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | MON/USD | 0.00991 | 66.887 | 70.686 | +4.65% | +0.20% | 0.52x | 20.2 | 2026-11-25T12:42:14.614553+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | CT/USD | 0.1308 | 57.913 | 44.437 | +3.56% | -0.30% | 3.90x | 23.1 | 2026-11-25T12:42:14.614553+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 85/100 | Do nothing | WATCH |
| 5 | INX/USD | 0.003939 | 37.106 | 39.005 | +2.82% | -1.60% | 1.61x | 22.8 | 2026-11-25T12:42:14.614553+00:00 | Not calibrated | WEAK 29/100 | EXTREME 89/100 | Do nothing | WATCH |
| 6 | CAP/USD | 0.092948 | 29.829 | 32.747 | +0.57% | +0.49% | 0.46x | 6.0 | 2026-11-25T12:42:14.614553+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | XPL/USD | 0.0446 | 26.636 | 33.558 | +1.36% | -0.67% | 0.64x | 22.5 | 2026-11-25T12:42:14.614553+00:00 | Not calibrated | WEAK 8/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BABY/USD | 70.886 | 0.00884 | -0.67% | 2.50x |
| 2 | MON/USD | 70.686 | 0.00991 | +0.20% | 0.52x |
| 3 | VVV/USD | 69.289 | 25.192 | +0.53% | 1.37x |
| 4 | CT/USD | 44.437 | 0.1308 | -0.30% | 3.90x |
| 5 | INX/USD | 39.005 | 0.003939 | -1.60% | 1.61x |
| 6 | XPL/USD | 33.558 | 0.0446 | -0.67% | 0.64x |
| 7 | CAP/USD | 32.747 | 0.092948 | +0.49% | 0.46x |

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

- Persisted scans: 1719; predictions: 14515; observations: 1041937.
- Matured sampled outcomes across 1/6/24/48h: 31742; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45615875492 · **Generation:** 1719 · **Legacy run:** 45615875492
**Main quote time:** 2026-11-25T12:42:18.772849+00:00 · **Legacy report time:** 2026-11-25T12:43:06.206970+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD | 0.00884 | 82.51 | -0.67% | 2.50x | MODERATE 66/100 | VERY_HIGH 79/100 | Watch |
| 2 | VVV/USD ⭐ | 25.192 | 75.60 | +0.53% | 1.37x | STRONG 93/100 | HIGH 55/100 | Watch |
| 3 | MON/USD | 0.00991 | 66.89 | +0.20% | 0.52x | MODERATE 53/100 | VERY_HIGH 82/100 | Watch |
| 4 | CT/USD | 0.1308 | 57.91 | -0.30% | 3.90x | MODERATE 49/100 | EXTREME 85/100 | Do nothing |
| 5 | INX/USD | 0.003939 | 37.11 | -1.60% | 1.61x | WEAK 29/100 | EXTREME 89/100 | Do nothing |
| 6 | CAP/USD | 0.092948 | 29.83 | +0.49% | 0.46x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |
| 7 | XPL/USD | 0.0446 | 26.64 | -0.67% | 0.64x | WEAK 8/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.239 | 74.33 | +0.53% | 1.37x | 12571 | STRONG 87/100 | HIGH 61/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
