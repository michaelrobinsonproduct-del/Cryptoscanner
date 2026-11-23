# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T22:17:01.565127+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45277768221
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e32c2b923b3376e5da5bb85f082ba9286f2358f9 (atomic ledger/results publication)
**Ledger generation:** 1488 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.44 | 108.895 | 97.443 | +9.06% | -0.34% | 2.32x | 5.1 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08109 | 89.799 | 91.183 | +7.50% | -0.16% | 0.94x | 7.4 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 3 | SHX/USD | 0.003624 | 81.281 | 69.424 | +7.38% | -0.06% | 2.21x | 13.8 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | CAP/USD | 0.102024 | 77.100 | 76.153 | +9.03% | -0.15% | 1.17x | 6.1 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | ATOM/USD | 1.2515 | 74.928 | 73.229 | +6.78% | -0.89% | 1.62x | 9.6 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 6 | SOL/USD | 72.13 | 72.067 | 69.173 | +2.12% | -0.30% | 1.44x | 1.4 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 7 | CC/USD | 0.07725 | 69.645 | 71.795 | +5.43% | -0.24% | 0.91x | 5.2 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | PAXG/USD | 3625.89 | 67.420 | 61.407 | +1.50% | +0.09% | 1.56x | 0.6 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 9 | LTC/USD | 41.14 | 64.450 | 70.867 | +2.44% | -0.29% | 0.50x | 2.4 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XLM/USD | 0.130225 | 62.954 | 69.113 | +2.11% | -0.54% | 0.65x | 1.4 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0563045 | 62.810 | 67.604 | +1.85% | -0.28% | 0.66x | 0.6 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | INJ/USD | 6.264 | 60.647 | 55.355 | +0.58% | -1.94% | 16.13x | 4.8 | 2026-11-23T22:16:55.195304+00:00 | Not calibrated | MODERATE 60/100 | HIGH 65/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.443 | 156.44 | -0.34% | 2.32x |
| 2 | ALGO/USD | 91.183 | 0.08109 | -0.16% | 0.94x |
| 3 | CAP/USD | 76.153 | 0.102024 | -0.15% | 1.17x |
| 4 | ATOM/USD | 73.229 | 1.2515 | -0.89% | 1.62x |
| 5 | CC/USD | 71.795 | 0.07725 | -0.24% | 0.91x |
| 6 | LTC/USD | 70.867 | 41.14 | -0.29% | 0.50x |
| 7 | SHX/USD | 69.424 | 0.003624 | -0.06% | 2.21x |
| 8 | SOL/USD | 69.173 | 72.13 | -0.30% | 1.44x |
| 9 | XLM/USD | 69.113 | 0.130225 | -0.54% | 0.65x |
| 10 | XDG/USD | 67.604 | 0.0563045 | -0.28% | 0.66x |
| 11 | PAXG/USD | 61.407 | 3625.89 | +0.09% | 1.56x |
| 12 | INJ/USD | 55.355 | 6.264 | -1.94% | 16.13x |

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

- Persisted scans: 1488; predictions: 12623; observations: 901294.
- Matured sampled outcomes across 1/6/24/48h: 22804; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45277768221 · **Generation:** 1488 · **Legacy run:** 45277768221
**Main quote time:** 2026-11-23T22:17:01.565127+00:00 · **Legacy report time:** 2026-11-23T22:18:11.054240+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 156.44 | 108.89 | -0.34% | 2.32x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | ALGO/USD | 0.08109 | 89.80 | -0.16% | 0.94x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 3 | SHX/USD | 0.003624 | 81.28 | -0.06% | 2.21x | MODERATE 66/100 | VERY_HIGH 79/100 | Watch |
| 4 | CAP/USD | 0.102024 | 77.10 | -0.15% | 1.17x | MODERATE 49/100 | VERY_HIGH 73/100 | Watch |
| 5 | ATOM/USD | 1.2515 | 74.93 | -0.89% | 1.62x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 6 | SOL/USD | 72.13 | 72.07 | -0.30% | 1.44x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 7 | CC/USD | 0.07725 | 69.65 | -0.24% | 0.91x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |
| 8 | PAXG/USD | 3625.89 | 67.42 | +0.09% | 1.56x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 9 | LTC/USD | 41.14 | 64.45 | -0.29% | 0.50x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | XLM/USD | 0.130225 | 62.95 | -0.54% | 0.65x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0563045 | 62.81 | -0.28% | 0.66x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | INJ/USD | 6.264 | 60.65 | -1.94% | 16.13x | MODERATE 60/100 | HIGH 65/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD | 0.002069 | 74.52 | +0.24% | 1.60x | 6306 | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
