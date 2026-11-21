# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T00:55:25.099403+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44846889338
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 99c9edefd7dcc840f819fbbdaa8ff5e67d32f945 (atomic ledger/results publication)
**Ledger generation:** 1050 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.8963 | 72.825 | 69.260 | +3.72% | +1.53% | 0.59x | 11.6 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | LINK/USD | 8.55529 | 64.058 | 55.169 | +0.30% | +0.29% | 1.74x | 3.9 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XBT/USD | 59015.1 | 63.221 | 57.476 | +0.35% | +0.13% | 1.51x | 0.0 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 4 | VVV/USD | 20.853 | 56.511 | 55.732 | +0.55% | +1.20% | 0.48x | 6.2 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SOL/USD | 68.9 | 52.227 | 56.210 | +0.28% | +0.03% | 0.59x | 1.5 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | UNI/USD | 4.4796 | 50.087 | 47.927 | +0.28% | +0.32% | 1.06x | 4.7 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 7 | CC/USD | 0.07485 | 49.835 | 36.662 | +0.40% | +0.31% | 2.16x | 5.3 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 8 | AKE/USD | 0.00621406 | 49.017 | 52.326 | +1.68% | +0.76% | 0.29x | 28.9 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | PUMP/USD | 0.002429 | 47.805 | 47.005 | +0.37% | +0.58% | 0.79x | 8.2 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 10 | KAS/USD | 0.02608 | 46.414 | 35.262 | +0.38% | +0.42% | 1.90x | 11.5 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 11 | CAP/USD | 0.092231 | 34.728 | 34.869 | +0.75% | +0.20% | 0.89x | 6.2 | 2026-11-21T00:55:16.901740+00:00 | Not calibrated | WEAK 37/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 69.260 | 1.8963 | +1.53% | 0.59x |
| 2 | XBT/USD | 57.476 | 59015.1 | +0.13% | 1.51x |
| 3 | SOL/USD | 56.210 | 68.9 | +0.03% | 0.59x |
| 4 | VVV/USD | 55.732 | 20.853 | +1.20% | 0.48x |
| 5 | LINK/USD | 55.169 | 8.55529 | +0.29% | 1.74x |
| 6 | AKE/USD | 52.326 | 0.00621406 | +0.76% | 0.29x |
| 7 | UNI/USD | 47.927 | 4.4796 | +0.32% | 1.06x |
| 8 | PUMP/USD | 47.005 | 0.002429 | +0.58% | 0.79x |
| 9 | CC/USD | 36.662 | 0.07485 | +0.31% | 2.16x |
| 10 | KAS/USD | 35.262 | 0.02608 | +0.42% | 1.90x |
| 11 | CAP/USD | 34.869 | 0.092231 | +0.20% | 0.89x |

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

- Persisted scans: 1050; predictions: 8407; observations: 634760.
- Matured sampled outcomes across 1/6/24/48h: 10932; gap abstentions: 19068. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44846889338 · **Generation:** 1050 · **Legacy run:** 44846889338
**Main quote time:** 2026-11-21T00:55:25.099403+00:00 · **Legacy report time:** 2026-11-21T00:56:04.861692+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 1.8963 | 72.83 | +1.53% | 0.59x | MODERATE 61/100 | VERY_HIGH 76/100 | Watch |
| 2 | LINK/USD ⭐ | 8.55529 | 64.06 | +0.29% | 1.74x | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 3 | XBT/USD ⭐ | 59015.1 | 63.22 | +0.13% | 1.51x | STRONG 77/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD | 20.853 | 56.51 | +1.20% | 0.48x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 5 | SOL/USD | 68.9 | 52.23 | +0.03% | 0.59x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 6 | UNI/USD ⭐ | 4.4796 | 50.09 | +0.32% | 1.06x | STRONG 70/100 | HIGH 62/100 | Watch |
| 7 | CC/USD | 0.07485 | 49.84 | +0.31% | 2.16x | STRONG 80/100 | HIGH 60/100 | Watch |
| 8 | AKE/USD | 0.00621406 | 49.02 | +0.76% | 0.29x | MODERATE 45/100 | VERY_HIGH 82/100 | Watch |
| 9 | PUMP/USD | 0.002429 | 47.81 | +0.58% | 0.79x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 10 | KAS/USD | 0.02608 | 46.41 | +0.42% | 1.90x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 11 | CAP/USD | 0.092231 | 34.73 | +0.20% | 0.89x | WEAK 37/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.91048 | 60.54 | +0.20% | 2.84x | 53558 | STRONG 75/100 | HIGH 55/100 | Watch |
| 2 | XBT/USD ⭐ | 59005.1 | 58.45 | +0.13% | 1.51x | 230991 | STRONG 74/100 | HIGH 55/100 | Watch |
| 3 | XLM/USD | 0.127473 | 53.54 | +0.17% | 2.18x | 11964 | STRONG 72/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD ⭐ | 8.55529 | 49.69 | +0.29% | 1.74x | 11126 | STRONG 80/100 | HIGH 55/100 | Consider small entry |
| 5 | BLUR/USD | 0.00743 | 44.89 | +1.78% | 1.02x | 2028 | MODERATE 47/100 | VERY_HIGH 79/100 | Watch |
| 6 | UNI/USD ⭐ | 4.4796 | 43.12 | +0.32% | 1.06x | 9199 | MODERATE 67/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LINK/USD, XBT/USD, UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
