# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T08:16:39.215999+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45781502480
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4abbfde3a11d441b121c4086a872155bda5f9309 (atomic ledger/results publication)
**Ledger generation:** 1835 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04358 | 78.073 | 57.512 | +4.06% | +1.11% | 7.86x | 9.2 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | STRONG 94/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | SYRUP/USD | 0.07237 | 66.523 | 70.384 | +9.20% | +0.61% | 0.31x | 13.8 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 3 | LTC/USD | 43.32 | 63.151 | 62.687 | +1.43% | -0.12% | 1.10x | 4.6 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 4 | INJ/USD | 6.164 | 62.562 | 64.756 | +3.53% | +0.65% | 0.45x | 4.9 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95099 | 62.047 | 65.260 | +1.54% | +0.15% | 0.60x | 1.1 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ADA/USD | 0.147645 | 60.480 | 62.547 | +1.29% | -0.01% | 0.80x | 2.9 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SOL/USD | 70.8 | 60.474 | 58.371 | +0.58% | +0.20% | 1.11x | 1.4 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 8 | LINK/USD | 9.14392 | 56.956 | 60.807 | +1.10% | +0.04% | 0.59x | 2.3 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | HBAR/USD | 0.05333 | 56.216 | 51.762 | +2.36% | +0.07% | 1.41x | 3.8 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XBT/USD | 60521.1 | 50.418 | 56.760 | +0.25% | +0.14% | 0.30x | 0.0 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0564376 | 48.572 | 55.432 | +0.86% | +0.00% | 0.31x | 1.2 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AAVE/USD | 95.68 | 37.998 | 40.893 | +0.34% | +0.26% | 0.58x | 6.3 | 2026-11-26T08:16:31.050618+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 70.384 | 0.07237 | +0.61% | 0.31x |
| 2 | XRP/USD | 65.260 | 0.95099 | +0.15% | 0.60x |
| 3 | INJ/USD | 64.756 | 6.164 | +0.65% | 0.45x |
| 4 | LTC/USD | 62.687 | 43.32 | -0.12% | 1.10x |
| 5 | ADA/USD | 62.547 | 0.147645 | -0.01% | 0.80x |
| 6 | LINK/USD | 60.807 | 9.14392 | +0.04% | 0.59x |
| 7 | SOL/USD | 58.371 | 70.8 | +0.20% | 1.11x |
| 8 | SKY/USD | 57.512 | 0.04358 | +1.11% | 7.86x |
| 9 | XBT/USD | 56.760 | 60521.1 | +0.14% | 0.30x |
| 10 | XDG/USD | 55.432 | 0.0564376 | +0.00% | 0.31x |
| 11 | HBAR/USD | 51.762 | 0.05333 | +0.07% | 1.41x |
| 12 | AAVE/USD | 40.893 | 95.68 | +0.26% | 0.58x |

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

- Persisted scans: 1835; predictions: 15755; observations: 1112557.
- Matured sampled outcomes across 1/6/24/48h: 34142; gap abstentions: 24319. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45781502480 · **Generation:** 1835 · **Legacy run:** 45781502480
**Main quote time:** 2026-11-26T08:16:39.215999+00:00 · **Legacy report time:** 2026-11-26T08:17:44.990080+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04358 | 78.07 | +1.11% | 7.86x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | SYRUP/USD | 0.07237 | 66.52 | +0.61% | 0.31x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 3 | LTC/USD | 43.32 | 63.15 | -0.12% | 1.10x | WEAK 42/100 | HIGH 68/100 | Watch |
| 4 | INJ/USD | 6.164 | 62.56 | +0.65% | 0.45x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 5 | XRP/USD | 0.95099 | 62.05 | +0.15% | 0.60x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 6 | ADA/USD | 0.147645 | 60.48 | -0.01% | 0.80x | WEAK 35/100 | HIGH 68/100 | Watch |
| 7 | SOL/USD | 70.8 | 60.47 | +0.20% | 1.11x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 8 | LINK/USD | 9.14392 | 56.96 | +0.04% | 0.59x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 9 | HBAR/USD | 0.05333 | 56.22 | +0.07% | 1.41x | MODERATE 63/100 | HIGH 55/100 | Watch |
| 10 | XBT/USD | 60521.1 | 50.42 | +0.14% | 0.30x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0564376 | 48.57 | +0.00% | 0.31x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 12 | AAVE/USD | 95.68 | 38.00 | +0.26% | 0.58x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HONEY/USD | 0.000224 | 97.42 | +2.79% | 2.10x | 12327 | STRONG 89/100 | VERY_HIGH 77/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04367 | 84.78 | +1.11% | 7.86x | 4110 | STRONG 100/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
