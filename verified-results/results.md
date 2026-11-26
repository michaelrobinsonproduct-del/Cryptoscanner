# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T16:10:56.803817+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45856098294
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c309d4aeebd6769d61b3150e08afd75762f6bea4 (atomic ledger/results publication)
**Ledger generation:** 1883 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WIF/USD | 0.1355 | 79.447 | 72.678 | +6.44% | -0.29% | 1.82x | 7.4 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04597 | 76.722 | 75.198 | +9.77% | +0.72% | 0.79x | 8.7 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 3 | XRP/USD | 0.94849 | 76.028 | 63.126 | +1.27% | +0.14% | 2.22x | 1.6 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 4 | KNTQ/USD | 0.16094 | 75.488 | 74.403 | +6.27% | +0.21% | 1.00x | 1.9 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | AKT/USD | 0.503 | 72.654 | 73.133 | +6.32% | +0.56% | 0.67x | 8.0 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0836 | 64.687 | 62.086 | +1.10% | +0.37% | 1.08x | 1.3 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ADA/USD | 0.148502 | 61.543 | 66.740 | +1.87% | +0.01% | 0.48x | 2.8 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | STBL/USD | 0.02085 | 58.075 | 64.922 | +10.40% | -1.19% | 0.91x | 22.1 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | WEAK 24/100 | EXTREME 96/100 | Do nothing | WATCH |
| 9 | LTC/USD | 43.46 | 57.852 | 66.142 | +1.76% | -0.21% | 0.27x | 2.3 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | XBT/USD | 60613 | 54.521 | 57.826 | +0.40% | +0.03% | 0.65x | 0.0 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | SOL/USD | 71.01 | 53.790 | 60.462 | +0.88% | -0.08% | 0.38x | 1.4 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | DRV/USD | 0.36522 | 50.583 | 50.336 | +2.07% | +0.61% | 0.72x | 0.3 | 2026-11-26T16:10:49.966408+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.198 | 0.04597 | +0.72% | 0.79x |
| 2 | KNTQ/USD | 74.403 | 0.16094 | +0.21% | 1.00x |
| 3 | AKT/USD | 73.133 | 0.503 | +0.56% | 0.67x |
| 4 | WIF/USD | 72.678 | 0.1355 | -0.29% | 1.82x |
| 5 | ADA/USD | 66.740 | 0.148502 | +0.01% | 0.48x |
| 6 | LTC/USD | 66.142 | 43.46 | -0.21% | 0.27x |
| 7 | STBL/USD | 64.922 | 0.02085 | -1.19% | 0.91x |
| 8 | XRP/USD | 63.126 | 0.94849 | +0.14% | 2.22x |
| 9 | NEAR/USD | 62.086 | 3.0836 | +0.37% | 1.08x |
| 10 | SOL/USD | 60.462 | 71.01 | -0.08% | 0.38x |
| 11 | XBT/USD | 57.826 | 60613 | +0.03% | 0.65x |
| 12 | DRV/USD | 50.336 | 0.36522 | +0.61% | 0.72x |

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

- Persisted scans: 1883; predictions: 16331; observations: 1140925.
- Matured sampled outcomes across 1/6/24/48h: 35294; gap abstentions: 25048. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45856098294 · **Generation:** 1883 · **Legacy run:** 45856098294
**Main quote time:** 2026-11-26T16:10:56.803817+00:00 · **Legacy report time:** 2026-11-26T16:11:36.963126+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WIF/USD | 0.1355 | 79.45 | -0.29% | 1.82x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 2 | SKY/USD | 0.04597 | 76.72 | +0.72% | 0.79x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 3 | XRP/USD | 0.94849 | 76.03 | +0.14% | 2.22x | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | KNTQ/USD | 0.16094 | 75.49 | +0.21% | 1.00x | STRONG 73/100 | VERY_HIGH 74/100 | Watch |
| 5 | AKT/USD | 0.503 | 72.65 | +0.56% | 0.67x | MODERATE 66/100 | VERY_HIGH 75/100 | Watch |
| 6 | NEAR/USD | 3.0836 | 64.69 | +0.37% | 1.08x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 7 | ADA/USD | 0.148502 | 61.54 | +0.01% | 0.48x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 8 | STBL/USD | 0.02085 | 58.08 | -1.19% | 0.91x | WEAK 24/100 | EXTREME 96/100 | Do nothing |
| 9 | LTC/USD | 43.46 | 57.85 | -0.21% | 0.27x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | XBT/USD | 60613 | 54.52 | +0.03% | 0.65x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 11 | SOL/USD | 71.01 | 53.79 | -0.08% | 0.38x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | DRV/USD | 0.36522 | 50.58 | +0.61% | 0.72x | MODERATE 55/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2Z/USD | 0.01759 | 68.39 | +0.06% | 1.04x | 2293 | MODERATE 49/100 | EXTREME 86/100 | Do nothing |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
