# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:15:17.170419+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44333340127
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** e734de1ed0687d95334c09815f689a62e7dbc906 (atomic ledger/results publication)
**Ledger generation:** 598 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | STABLE/USD | 0.02306 | 75.087 | 67.323 | +9.55% | +0.00% | 1.78x | 17.4 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | CT/USD | 0.1229 | 65.041 | 63.780 | +8.76% | +0.57% | 0.84x | 24.4 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 86/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.04535 | 64.602 | 53.105 | +1.02% | -0.70% | 3.91x | 4.4 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 4 | INFI/USD | 0.141 | 61.769 | 73.069 | +11.02% | -1.81% | 0.78x | 7.1 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.019597 | 61.117 | 63.298 | +4.97% | -0.52% | 1.04x | 5.1 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 6 | TRX/USD | 0.310085 | 57.367 | 45.680 | +0.71% | +0.10% | 2.12x | 0.5 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 7 | AKE/USD | 0.01056189 | 56.677 | 61.184 | +5.79% | +0.16% | 0.47x | 25.7 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | WEAK 38/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | MNT/USD | 0.3862 | 56.066 | 50.696 | +3.46% | -0.13% | 1.60x | 13.0 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | VVV/USD | 21.083 | 54.258 | 48.246 | +0.27% | -0.11% | 1.66x | 5.2 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 10 | AKT/USD | 0.5159 | 46.668 | 34.654 | +1.30% | -0.60% | 3.33x | 13.6 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 11 | CC/USD | 0.08295 | 41.187 | 39.660 | +1.00% | +0.06% | 1.12x | 6.0 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | MODERATE 46/100 | HIGH 67/100 | Watch | WATCH |
| 12 | ME/USD | 0.0392 | 30.141 | 29.579 | +1.55% | -0.25% | 1.18x | 25.5 | 2026-11-18T15:15:10.899064+00:00 | Not calibrated | WEAK 15/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INFI/USD | 73.069 | 0.141 | -1.81% | 0.78x |
| 2 | STABLE/USD | 67.323 | 0.02306 | +0.00% | 1.78x |
| 3 | CT/USD | 63.780 | 0.1229 | +0.57% | 0.84x |
| 4 | SENT/USD | 63.298 | 0.019597 | -0.52% | 1.04x |
| 5 | AKE/USD | 61.184 | 0.01056189 | +0.16% | 0.47x |
| 6 | NIGHT/USD | 53.105 | 0.04535 | -0.70% | 3.91x |
| 7 | MNT/USD | 50.696 | 0.3862 | -0.13% | 1.60x |
| 8 | VVV/USD | 48.246 | 21.083 | -0.11% | 1.66x |
| 9 | TRX/USD | 45.680 | 0.310085 | +0.10% | 2.12x |
| 10 | CC/USD | 39.660 | 0.08295 | +0.06% | 1.12x |
| 11 | AKT/USD | 34.654 | 0.5159 | -0.60% | 3.33x |
| 12 | ME/USD | 29.579 | 0.0392 | -0.25% | 1.18x |

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

- Persisted scans: 598; predictions: 5112; observations: 361189.
- Matured sampled outcomes across 1/6/24/48h: 4326; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44333340127 · **Generation:** 598 · **Legacy run:** 44333340127
**Main quote time:** 2026-11-18T15:15:17.170419+00:00 · **Legacy report time:** 2026-11-18T15:15:40.373382+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD | 0.02306 | 75.09 | +0.00% | 1.78x | MODERATE 68/100 | VERY_HIGH 73/100 | Watch |
| 2 | CT/USD | 0.1229 | 65.04 | +0.57% | 0.84x | MODERATE 53/100 | EXTREME 86/100 | Do nothing |
| 3 | NIGHT/USD | 0.04535 | 64.60 | -0.70% | 3.91x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 4 | INFI/USD | 0.141 | 61.77 | -1.81% | 0.78x | WEAK 36/100 | VERY_HIGH 84/100 | Do nothing |
| 5 | SENT/USD | 0.019597 | 61.12 | -0.52% | 1.04x | WEAK 41/100 | VERY_HIGH 80/100 | Watch |
| 6 | TRX/USD ⭐ | 0.310085 | 57.37 | +0.10% | 2.12x | STRONG 84/100 | HIGH 55/100 | Watch |
| 7 | AKE/USD | 0.01056189 | 56.68 | +0.16% | 0.47x | WEAK 38/100 | EXTREME 87/100 | Do nothing |
| 8 | MNT/USD | 0.3862 | 56.07 | -0.13% | 1.60x | WEAK 43/100 | VERY_HIGH 72/100 | Watch |
| 9 | VVV/USD | 21.083 | 54.26 | -0.11% | 1.66x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 10 | AKT/USD | 0.5159 | 46.67 | -0.60% | 3.33x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 11 | CC/USD ⭐ | 0.08295 | 41.19 | +0.06% | 1.12x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 12 | ME/USD | 0.0392 | 30.14 | -0.25% | 1.18x | WEAK 15/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD ⭐ | 0.310066 | 55.75 | +0.10% | 2.12x | 4244 | STRONG 83/100 | HIGH 55/100 | Watch |
| 2 | CC/USD ⭐ | 0.08297 | 38.89 | +0.06% | 1.12x | 4855 | MODERATE 54/100 | HIGH 67/100 | Watch |

**Same-run overlap:** TRX/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
