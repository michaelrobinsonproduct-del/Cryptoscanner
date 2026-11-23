# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T22:51:53.599338+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45283320705
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 308997d98b47172ff6f88c02c1c9c964ccf1874e (atomic ledger/results publication)
**Ledger generation:** 1492 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08076 | 102.798 | 91.723 | +7.07% | -0.07% | 2.14x | 6.2 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | QNT/USD | 155.49 | 98.268 | 96.787 | +8.40% | -0.28% | 1.29x | 6.4 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ATOM/USD | 1.2555 | 76.788 | 72.910 | +7.12% | +0.40% | 1.19x | 10.3 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0559142 | 75.475 | 62.785 | +1.14% | -0.46% | 8.96x | 0.4 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | HYPE/USD | 63.37 | 70.454 | 57.652 | +0.49% | -0.44% | 4.77x | 1.6 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LTC/USD | 40.98 | 69.975 | 66.853 | +2.04% | -0.24% | 1.43x | 4.9 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 7 | CAP/USD | 0.101653 | 67.750 | 76.946 | +8.64% | -0.36% | 0.26x | 4.4 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | SOL/USD | 71.71 | 67.654 | 65.006 | +1.53% | -0.47% | 1.50x | 1.4 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SHX/USD | 0.0036 | 66.995 | 74.957 | +6.67% | -0.36% | 0.38x | 2.8 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | WEAK 38/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | CC/USD | 0.07682 | 61.704 | 68.275 | +4.85% | -0.04% | 0.36x | 3.9 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | XRP/USD | 0.93473 | 59.738 | 60.373 | +0.78% | -0.32% | 1.10x | 0.1 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 12 | PAXG/USD | 3625.06 | 58.580 | 60.900 | +1.48% | -0.02% | 0.78x | 1.2 | 2026-11-23T22:51:44.638534+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 96.787 | 155.49 | -0.28% | 1.29x |
| 2 | ALGO/USD | 91.723 | 0.08076 | -0.07% | 2.14x |
| 3 | CAP/USD | 76.946 | 0.101653 | -0.36% | 0.26x |
| 4 | SHX/USD | 74.957 | 0.0036 | -0.36% | 0.38x |
| 5 | ATOM/USD | 72.910 | 1.2555 | +0.40% | 1.19x |
| 6 | CC/USD | 68.275 | 0.07682 | -0.04% | 0.36x |
| 7 | LTC/USD | 66.853 | 40.98 | -0.24% | 1.43x |
| 8 | SOL/USD | 65.006 | 71.71 | -0.47% | 1.50x |
| 9 | XDG/USD | 62.785 | 0.0559142 | -0.46% | 8.96x |
| 10 | PAXG/USD | 60.900 | 3625.06 | -0.02% | 0.78x |
| 11 | XRP/USD | 60.373 | 0.93473 | -0.32% | 1.10x |
| 12 | HYPE/USD | 57.652 | 63.37 | -0.44% | 4.77x |

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

- Persisted scans: 1492; predictions: 12671; observations: 903730.
- Matured sampled outcomes across 1/6/24/48h: 22984; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45283320705 · **Generation:** 1492 · **Legacy run:** 45283320705
**Main quote time:** 2026-11-23T22:51:53.599338+00:00 · **Legacy report time:** 2026-11-23T22:53:04.190705+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08076 | 102.80 | -0.07% | 2.14x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | QNT/USD | 155.49 | 98.27 | -0.28% | 1.29x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 3 | ATOM/USD ⭐ | 1.2555 | 76.79 | +0.40% | 1.19x | STRONG 78/100 | VERY_HIGH 73/100 | Watch |
| 4 | XDG/USD | 0.0559142 | 75.48 | -0.46% | 8.96x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | HYPE/USD | 63.37 | 70.45 | -0.44% | 4.77x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | LTC/USD | 40.98 | 69.97 | -0.24% | 1.43x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 7 | CAP/USD | 0.101653 | 67.75 | -0.36% | 0.26x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 8 | SOL/USD | 71.71 | 67.65 | -0.47% | 1.50x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 9 | SHX/USD | 0.0036 | 66.99 | -0.36% | 0.38x | WEAK 38/100 | EXTREME 88/100 | Do nothing |
| 10 | CC/USD | 0.07682 | 61.70 | -0.04% | 0.36x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |
| 11 | XRP/USD | 0.93473 | 59.74 | -0.32% | 1.10x | WEAK 40/100 | HIGH 68/100 | Watch |
| 12 | PAXG/USD | 3625.06 | 58.58 | -0.02% | 0.78x | WEAK 34/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ATOM/USD ⭐ | 1.2555 | 73.80 | +0.40% | 1.19x | 3699 | STRONG 77/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** ATOM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
