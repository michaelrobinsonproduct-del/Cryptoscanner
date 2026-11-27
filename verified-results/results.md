# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T07:11:27.527677+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45956533300
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dab39a10f2dfa094f4e8ef267afc449549a21c82 (atomic ledger/results publication)
**Ledger generation:** 1975 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 744.91 | 114.410 | 99.262 | +9.28% | +0.03% | 2.81x | 1.5 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | HYPE/USD | 66.2 | 92.916 | 98.266 | +6.40% | -0.06% | 0.50x | 3.0 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | VVV/USD | 27.215 | 88.323 | 78.372 | +3.94% | +1.47% | 1.26x | 8.4 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ADA/USD | 0.15293 | 86.767 | 71.430 | +3.01% | +0.07% | 3.08x | 3.2 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 5 | BIGTIME/USD | 0.00637 | 81.834 | 72.915 | +9.47% | -0.70% | 2.24x | 6.3 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | UNI/USD | 4.8756 | 80.433 | 75.504 | +4.85% | +0.06% | 1.46x | 2.7 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ENA/USD | 0.1071 | 78.042 | 75.689 | +6.67% | +0.56% | 0.95x | 9.3 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97365 | 75.852 | 77.892 | +3.28% | +0.27% | 0.66x | 0.1 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SOL/USD | 72.92 | 71.800 | 73.852 | +2.79% | -0.12% | 0.86x | 1.4 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | ETH/USD | 1730.88 | 70.132 | 72.889 | +2.56% | -0.11% | 0.78x | 0.1 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 11 | AVAX/USD | 6.755 | 69.577 | 55.021 | +2.43% | -0.09% | 5.95x | 1.5 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 12 | LINK/USD | 9.56379 | 69.450 | 76.858 | +3.19% | -0.29% | 0.41x | 0.9 | 2026-11-27T07:11:19.257831+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.262 | 744.91 | +0.03% | 2.81x |
| 2 | HYPE/USD | 98.266 | 66.2 | -0.06% | 0.50x |
| 3 | VVV/USD | 78.372 | 27.215 | +1.47% | 1.26x |
| 4 | XRP/USD | 77.892 | 0.97365 | +0.27% | 0.66x |
| 5 | LINK/USD | 76.858 | 9.56379 | -0.29% | 0.41x |
| 6 | ENA/USD | 75.689 | 0.1071 | +0.56% | 0.95x |
| 7 | UNI/USD | 75.504 | 4.8756 | +0.06% | 1.46x |
| 8 | SOL/USD | 73.852 | 72.92 | -0.12% | 0.86x |
| 9 | BIGTIME/USD | 72.915 | 0.00637 | -0.70% | 2.24x |
| 10 | ETH/USD | 72.889 | 1730.88 | -0.11% | 0.78x |
| 11 | ADA/USD | 71.430 | 0.15293 | +0.07% | 3.08x |
| 12 | AVAX/USD | 55.021 | 6.755 | -0.09% | 5.95x |

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

- Persisted scans: 1975; predictions: 17402; observations: 1196078.
- Matured sampled outcomes across 1/6/24/48h: 38444; gap abstentions: 25612. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45956533300 · **Generation:** 1975 · **Legacy run:** 45956533300
**Main quote time:** 2026-11-27T07:11:27.527677+00:00 · **Legacy report time:** 2026-11-27T07:12:00.599115+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 744.91 | 114.41 | +0.03% | 2.81x | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | HYPE/USD | 66.2 | 92.92 | -0.06% | 0.50x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 3 | VVV/USD ⭐ | 27.215 | 88.32 | +1.47% | 1.26x | STRONG 89/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD ⭐ | 0.15293 | 86.77 | +0.07% | 3.08x | STRONG 98/100 | HIGH 55/100 | Watch |
| 5 | BIGTIME/USD | 0.00637 | 81.83 | -0.70% | 2.24x | STRONG 71/100 | VERY_HIGH 73/100 | Watch |
| 6 | UNI/USD ⭐ | 4.8756 | 80.43 | +0.06% | 1.46x | STRONG 85/100 | HIGH 55/100 | Watch |
| 7 | ENA/USD | 0.1071 | 78.04 | +0.56% | 0.95x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 8 | XRP/USD | 0.97365 | 75.85 | +0.27% | 0.66x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 9 | SOL/USD | 72.92 | 71.80 | -0.12% | 0.86x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | ETH/USD | 1730.88 | 70.13 | -0.11% | 0.78x | WEAK 40/100 | HIGH 68/100 | Watch |
| 11 | AVAX/USD | 6.755 | 69.58 | -0.09% | 5.95x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 12 | LINK/USD | 9.56379 | 69.45 | -0.29% | 0.41x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.153199 | 91.25 | +0.07% | 3.08x | 9759 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | VVV/USD ⭐ | 27.215 | 89.75 | +1.47% | 1.26x | 10689 | STRONG 90/100 | HIGH 55/100 | Watch |
| 3 | UNI/USD ⭐ | 4.8756 | 86.97 | +0.06% | 1.46x | 7015 | STRONG 88/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, ADA/USD, UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
