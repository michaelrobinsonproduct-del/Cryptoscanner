# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T21:46:55.390676+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45272737071
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f20163b9fed4a265c1b2664e7cf19a82a4d1e5c6 (atomic ledger/results publication)
**Ledger generation:** 1485 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 157.8 | 91.548 | 96.185 | +10.01% | -0.06% | 0.57x | 7.6 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08132 | 82.847 | 91.914 | +7.81% | +0.00% | 0.09x | 6.2 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | CAP/USD | 0.103427 | 71.916 | 76.100 | +10.53% | +0.10% | 0.53x | 6.1 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | SHX/USD | 0.003623 | 69.240 | 74.926 | +7.35% | +0.00% | 0.43x | 2.8 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6735 | 68.505 | 72.516 | +2.71% | -0.30% | 0.75x | 3.0 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.263 | 68.020 | 74.865 | +7.76% | -0.35% | 0.49x | 6.3 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | CC/USD | 0.07728 | 67.032 | 70.888 | +5.47% | +0.12% | 0.56x | 7.8 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | INJ/USD | 6.433 | 66.911 | 72.841 | +3.29% | -0.76% | 0.78x | 6.2 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | TRX/USD | 0.309245 | 65.454 | 50.398 | +1.33% | +0.01% | 11.33x | 1.1 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 10 | KAS/USD | 0.02713 | 60.778 | 70.901 | +5.11% | -0.33% | 0.15x | 3.7 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SOL/USD | 72.02 | 59.705 | 68.082 | +1.97% | -0.28% | 0.30x | 1.4 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0564094 | 59.695 | 68.534 | +2.04% | -0.20% | 0.22x | 1.4 | 2026-11-23T21:46:46.915706+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 96.185 | 157.8 | -0.06% | 0.57x |
| 2 | ALGO/USD | 91.914 | 0.08132 | +0.00% | 0.09x |
| 3 | CAP/USD | 76.100 | 0.103427 | +0.10% | 0.53x |
| 4 | SHX/USD | 74.926 | 0.003623 | +0.00% | 0.43x |
| 5 | ATOM/USD | 74.865 | 1.263 | -0.35% | 0.49x |
| 6 | INJ/USD | 72.841 | 6.433 | -0.76% | 0.78x |
| 7 | SUI/USD | 72.516 | 0.6735 | -0.30% | 0.75x |
| 8 | KAS/USD | 70.901 | 0.02713 | -0.33% | 0.15x |
| 9 | CC/USD | 70.888 | 0.07728 | +0.12% | 0.56x |
| 10 | XDG/USD | 68.534 | 0.0564094 | -0.20% | 0.22x |
| 11 | SOL/USD | 68.082 | 72.02 | -0.28% | 0.30x |
| 12 | TRX/USD | 50.398 | 0.309245 | +0.01% | 11.33x |

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

- Persisted scans: 1485; predictions: 12587; observations: 899467.
- Matured sampled outcomes across 1/6/24/48h: 22660; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45272737071 · **Generation:** 1485 · **Legacy run:** 45272737071
**Main quote time:** 2026-11-23T21:46:55.390676+00:00 · **Legacy report time:** 2026-11-23T21:47:46.141131+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 157.8 | 91.55 | -0.06% | 0.57x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 2 | ALGO/USD | 0.08132 | 82.85 | +0.00% | 0.09x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 3 | CAP/USD | 0.103427 | 71.92 | +0.10% | 0.53x | MODERATE 56/100 | VERY_HIGH 75/100 | Watch |
| 4 | SHX/USD | 0.003623 | 69.24 | +0.00% | 0.43x | MODERATE 55/100 | VERY_HIGH 82/100 | Watch |
| 5 | SUI/USD | 0.6735 | 68.51 | -0.30% | 0.75x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 6 | ATOM/USD | 1.263 | 68.02 | -0.35% | 0.49x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 7 | CC/USD | 0.07728 | 67.03 | +0.12% | 0.56x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 8 | INJ/USD | 6.433 | 66.91 | -0.76% | 0.78x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | TRX/USD | 0.309245 | 65.45 | +0.01% | 11.33x | STRONG 78/100 | HIGH 55/100 | Watch |
| 10 | KAS/USD | 0.02713 | 60.78 | -0.33% | 0.15x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | SOL/USD | 72.02 | 59.71 | -0.28% | 0.30x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | XDG/USD | 0.0564094 | 59.69 | -0.20% | 0.22x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PENGU/USD | 0.00441 | 72.93 | +0.14% | 1.08x | 4370 | MODERATE 61/100 | HIGH 67/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
