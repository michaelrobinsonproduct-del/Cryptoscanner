# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:10:26.171302+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44551631194
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** f45f94ac5a28a7231b86da6339d08745b4d5267e (atomic ledger/results publication)
**Ledger generation:** 798 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 10s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.348 | 113.177 | 97.641 | +7.74% | +0.11% | 2.89x | 4.7 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | INJ/USD | 7.288 | 91.190 | 72.466 | +4.40% | +0.77% | 2.49x | 2.8 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SENT/USD | 0.021896 | 87.806 | 72.328 | +6.27% | +0.10% | 3.62x | 10.5 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | STRONG 84/100 | HIGH 66/100 | Watch | WATCH |
| 4 | TAO/USD | 197.86 | 86.898 | 72.705 | +3.07% | +0.38% | 2.23x | 7.6 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ZEC/USD | 942.61 | 83.149 | 74.604 | +3.36% | +0.60% | 1.56x | 7.9 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | TRUST/USD | 0.05266 | 75.383 | 75.200 | +7.03% | -1.05% | 1.54x | 1.9 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 7 | HYPE/USD | 69.18 | 75.202 | 77.627 | +3.44% | +0.41% | 0.55x | 2.9 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ADA/USD | 0.155055 | 72.463 | 72.559 | +2.51% | +0.34% | 0.82x | 0.1 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 9 | PUMP/USD | 0.002748 | 71.972 | 80.234 | +5.86% | -0.07% | 0.21x | 7.3 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SOL/USD | 75.16 | 69.721 | 69.755 | +2.20% | +0.48% | 0.76x | 1.3 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XRP/USD | 0.9876 | 66.823 | 69.568 | +2.20% | +0.05% | 0.70x | 1.6 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XBT/USD | 63578 | 62.780 | 61.588 | +0.94% | +0.00% | 1.12x | 0.0 | 2026-11-19T15:10:16.486330+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 97.641 | 23.348 | +0.11% | 2.89x |
| 2 | PUMP/USD | 80.234 | 0.002748 | -0.07% | 0.21x |
| 3 | HYPE/USD | 77.627 | 69.18 | +0.41% | 0.55x |
| 4 | TRUST/USD | 75.200 | 0.05266 | -1.05% | 1.54x |
| 5 | ZEC/USD | 74.604 | 942.61 | +0.60% | 1.56x |
| 6 | TAO/USD | 72.705 | 197.86 | +0.38% | 2.23x |
| 7 | ADA/USD | 72.559 | 0.155055 | +0.34% | 0.82x |
| 8 | INJ/USD | 72.466 | 7.288 | +0.77% | 2.49x |
| 9 | SENT/USD | 72.328 | 0.021896 | +0.10% | 3.62x |
| 10 | SOL/USD | 69.755 | 75.16 | +0.48% | 0.76x |
| 11 | XRP/USD | 69.568 | 0.9876 | +0.05% | 0.70x |
| 12 | XBT/USD | 61.588 | 63578 | +0.00% | 1.12x |

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

- Persisted scans: 798; predictions: 6720; observations: 482644.
- Matured sampled outcomes across 1/6/24/48h: 6731; gap abstentions: 15174. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44551631194 · **Generation:** 798 · **Legacy run:** 44551631194
**Main quote time:** 2026-11-19T15:10:26.171302+00:00 · **Legacy report time:** 2026-11-19T15:11:16.908604+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 23.348 | 113.18 | +0.11% | 2.89x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | INJ/USD ⭐ | 7.288 | 91.19 | +0.77% | 2.49x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD ⭐ | 0.021896 | 87.81 | +0.10% | 3.62x | STRONG 94/100 | HIGH 66/100 | Watch |
| 4 | TAO/USD ⭐ | 197.86 | 86.90 | +0.38% | 2.23x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD ⭐ | 942.61 | 83.15 | +0.60% | 1.56x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 6 | TRUST/USD | 0.05266 | 75.38 | -1.05% | 1.54x | MODERATE 58/100 | VERY_HIGH 77/100 | Watch |
| 7 | HYPE/USD | 69.18 | 75.20 | +0.41% | 0.55x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 8 | ADA/USD | 0.155055 | 72.46 | +0.34% | 0.82x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 9 | PUMP/USD | 0.002748 | 71.97 | -0.07% | 0.21x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 10 | SOL/USD | 75.16 | 69.72 | +0.48% | 0.76x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 11 | XRP/USD | 0.9876 | 66.82 | +0.05% | 0.70x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 12 | XBT/USD | 63578 | 62.78 | +0.00% | 1.12x | MODERATE 56/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 23.26 | 92.86 | +0.11% | 2.89x | 12336 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | INJ/USD ⭐ | 7.259 | 92.59 | +0.77% | 2.49x | 6520 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD ⭐ | 0.021905 | 84.58 | +0.10% | 3.62x | 13912 | STRONG 97/100 | HIGH 60/100 | Watch |
| 4 | ZEC/USD ⭐ | 940.07 | 81.09 | +0.60% | 1.56x | 20601 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | AKT/USD | 0.5543 | 80.08 | +0.40% | 4.39x | 3099 | STRONG 90/100 | VERY_HIGH 73/100 | Watch |
| 6 | TAO/USD ⭐ | 197.625 | 78.47 | +0.38% | 2.23x | 5937 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | PYTH/USD | 0.05665 | 78.30 | +0.42% | 2.43x | 2664 | STRONG 89/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** VVV/USD, INJ/USD, SENT/USD, TAO/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
