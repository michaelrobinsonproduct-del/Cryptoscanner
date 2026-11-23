# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T12:11:40.346767+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45171640036
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 34f83479fef1943b6289c347815a70b1e859302d (atomic ledger/results publication)
**Ledger generation:** 1428 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 155.26 | 97.385 | 89.409 | +8.24% | +0.93% | 1.33x | 7.7 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6738 | 88.880 | 72.839 | +2.76% | +0.21% | 3.37x | 3.0 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UAI/USD | 0.0313 | 84.869 | 63.732 | +5.85% | +1.23% | 3.30x | 16.0 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | STRONG 92/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | ALGO/USD | 0.08367 | 73.682 | 74.205 | +10.92% | +0.47% | 0.71x | 12.0 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | XRP/USD | 0.93957 | 67.006 | 63.813 | +1.30% | -0.06% | 1.35x | 0.5 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 72.45 | 66.978 | 72.347 | +2.58% | -0.07% | 0.50x | 1.4 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | PAXG/USD | 3606.81 | 66.217 | 51.443 | +0.97% | -0.05% | 3.21x | 0.5 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 8 | HYPE/USD | 64.12 | 64.429 | 65.205 | +1.68% | -0.03% | 0.94x | 3.1 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | CC/USD | 0.07656 | 63.266 | 63.026 | +4.49% | +0.31% | 0.87x | 6.5 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | MODERATE 62/100 | HIGH 67/100 | Watch | WATCH |
| 10 | XMR/USD | 503.09 | 60.776 | 66.510 | +1.90% | -0.05% | 0.45x | 3.6 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XBT/USD | 61334 | 59.328 | 56.867 | +0.27% | -0.03% | 1.26x | 0.0 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | WEAK 40/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XLM/USD | 0.128897 | 58.752 | 60.161 | +1.07% | +0.01% | 0.85x | 1.9 | 2026-11-23T12:11:33.772689+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 89.409 | 155.26 | +0.93% | 1.33x |
| 2 | ALGO/USD | 74.205 | 0.08367 | +0.47% | 0.71x |
| 3 | SUI/USD | 72.839 | 0.6738 | +0.21% | 3.37x |
| 4 | SOL/USD | 72.347 | 72.45 | -0.07% | 0.50x |
| 5 | XMR/USD | 66.510 | 503.09 | -0.05% | 0.45x |
| 6 | HYPE/USD | 65.205 | 64.12 | -0.03% | 0.94x |
| 7 | XRP/USD | 63.813 | 0.93957 | -0.06% | 1.35x |
| 8 | UAI/USD | 63.732 | 0.0313 | +1.23% | 3.30x |
| 9 | CC/USD | 63.026 | 0.07656 | +0.31% | 0.87x |
| 10 | XLM/USD | 60.161 | 0.128897 | +0.01% | 0.85x |
| 11 | XBT/USD | 56.867 | 61334 | -0.03% | 1.26x |
| 12 | PAXG/USD | 51.443 | 3606.81 | -0.05% | 3.21x |

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

- Persisted scans: 1428; predictions: 11903; observations: 864755.
- Matured sampled outcomes across 1/6/24/48h: 19841; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45171640036 · **Generation:** 1428 · **Legacy run:** 45171640036
**Main quote time:** 2026-11-23T12:11:40.346767+00:00 · **Legacy report time:** 2026-11-23T12:12:35.337994+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 155.26 | 97.38 | +0.93% | 1.33x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SUI/USD ⭐ | 0.6738 | 88.88 | +0.21% | 3.37x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UAI/USD ⭐ | 0.0313 | 84.87 | +1.23% | 3.30x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 4 | ALGO/USD | 0.08367 | 73.68 | +0.47% | 0.71x | MODERATE 62/100 | VERY_HIGH 81/100 | Watch |
| 5 | XRP/USD | 0.93957 | 67.01 | -0.06% | 1.35x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD | 72.45 | 66.98 | -0.07% | 0.50x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 7 | PAXG/USD | 3606.81 | 66.22 | -0.05% | 3.21x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 8 | HYPE/USD | 64.12 | 64.43 | -0.03% | 0.94x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | CC/USD | 0.07656 | 63.27 | +0.31% | 0.87x | MODERATE 62/100 | HIGH 67/100 | Watch |
| 10 | XMR/USD | 503.09 | 60.78 | -0.05% | 0.45x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | XBT/USD | 61334 | 59.33 | -0.03% | 1.26x | WEAK 40/100 | HIGH 61/100 | Watch |
| 12 | XLM/USD | 0.128897 | 58.75 | +0.01% | 0.85x | MODERATE 49/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.6742 | 88.54 | +0.21% | 3.37x | 5731 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | QNT/USD ⭐ | 155.16 | 88.47 | +0.93% | 1.33x | 5857 | STRONG 99/100 | HIGH 55/100 | Watch |
| 3 | INJ/USD | 6.453 | 82.38 | +0.39% | 2.74x | 4410 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 4 | UAI/USD ⭐ | 0.03131 | 75.61 | +1.23% | 3.30x | 1855 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 5 | ENA/USD | 0.1041 | 65.11 | +0.19% | 1.60x | 2512 | MODERATE 68/100 | HIGH 55/100 | Watch |

**Same-run overlap:** QNT/USD, SUI/USD, UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
