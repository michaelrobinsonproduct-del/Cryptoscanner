# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T15:23:16.796307+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45643872517
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 269f63c11f7959a7a10ef4ce4b98c6aff7647440 (atomic ledger/results publication)
**Ledger generation:** 1735 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PIEVERSE/USD | 3.3869 | 88.683 | 56.214 | +9.95% | +3.49% | 5.86x | 40.8 | 2026-11-25T15:23:12.743722+00:00 | Not calibrated | STRONG 84/100 | EXTREME 99/100 | Do nothing | WATCH |
| 2 | MOODENG/USD | 0.02674 | 60.243 | 64.751 | +9.91% | +0.72% | 0.19x | 26.2 | 2026-11-25T15:23:12.743722+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | MON/USD | 0.00993 | 56.268 | 67.062 | +4.86% | -1.40% | 0.62x | 20.1 | 2026-11-25T15:23:12.743722+00:00 | Not calibrated | WEAK 23/100 | EXTREME 92/100 | Do nothing | WATCH |
| 4 | DRV/USD | 0.32322 | 49.355 | 46.633 | +2.84% | -1.14% | 1.84x | 22.0 | 2026-11-25T15:23:12.743722+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 5 | XPL/USD | 0.0449 | 31.793 | 38.545 | +2.05% | -1.97% | 1.31x | 22.3 | 2026-11-25T15:23:12.743722+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | CT/USD | 0.1304 | 24.463 | 38.453 | +3.25% | -1.67% | 0.44x | 30.8 | 2026-11-25T15:23:12.743722+00:00 | Not calibrated | WEAK 7/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 67.062 | 0.00993 | -1.40% | 0.62x |
| 2 | MOODENG/USD | 64.751 | 0.02674 | +0.72% | 0.19x |
| 3 | PIEVERSE/USD | 56.214 | 3.3869 | +3.49% | 5.86x |
| 4 | DRV/USD | 46.633 | 0.32322 | -1.14% | 1.84x |
| 5 | XPL/USD | 38.545 | 0.0449 | -1.97% | 1.31x |
| 6 | CT/USD | 38.453 | 0.1304 | -1.67% | 0.44x |

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

- Persisted scans: 1735; predictions: 14607; observations: 1051665.
- Matured sampled outcomes across 1/6/24/48h: 32304; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45643872517 · **Generation:** 1735 · **Legacy run:** 45643872517
**Main quote time:** 2026-11-25T15:23:16.796307+00:00 · **Legacy report time:** 2026-11-25T15:24:21.015188+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.3869 | 88.68 | +3.49% | 5.86x | STRONG 94/100 | EXTREME 99/100 | Do nothing |
| 2 | MOODENG/USD | 0.02674 | 60.24 | +0.72% | 0.19x | MODERATE 50/100 | EXTREME 87/100 | Do nothing |
| 3 | MON/USD | 0.00993 | 56.27 | -1.40% | 0.62x | WEAK 23/100 | EXTREME 92/100 | Do nothing |
| 4 | DRV/USD | 0.32322 | 49.35 | -1.14% | 1.84x | WEAK 35/100 | VERY_HIGH 77/100 | Watch |
| 5 | XPL/USD | 0.0449 | 31.79 | -1.97% | 1.31x | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | CT/USD | 0.1304 | 24.46 | -1.67% | 0.44x | WEAK 7/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.3791 | 75.32 | +3.49% | 5.86x | 1242 | STRONG 88/100 | EXTREME 99/100 | Do nothing |

**Same-run overlap:** PIEVERSE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
