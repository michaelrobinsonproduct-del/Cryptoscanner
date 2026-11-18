# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:30:26.183527+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44421194268
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** d27d3c2c2bdd416ccd950404289bbe2763ffd448 (atomic ledger/results publication)
**Ledger generation:** 695 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.325e-05 | 74.708 | 57.663 | +3.84% | +1.00% | 2.20x | 2.3 | 2026-11-18T23:30:20.609974+00:00 | Not calibrated | STRONG 92/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | MEGA/USD | 0.05559 | 67.895 | 66.257 | +7.65% | +0.27% | 1.03x | 19.9 | 2026-11-18T23:30:20.609974+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04503 | 55.419 | 41.732 | +0.31% | -0.02% | 2.38x | 8.9 | 2026-11-18T23:30:20.609974+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 4 | TRX/USD | 0.309137 | 38.242 | 42.615 | +0.40% | +0.16% | 0.48x | 0.0 | 2026-11-18T23:30:20.609974+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5138 | 35.545 | 34.981 | +0.88% | +0.71% | 0.70x | 5.8 | 2026-11-18T23:30:20.609974+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | AKE/USD | 0.01016922 | 35.102 | 33.711 | +1.85% | +0.74% | 0.77x | 27.4 | 2026-11-18T23:30:20.609974+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 66.257 | 0.05559 | +0.27% | 1.03x |
| 2 | LUNA/USD | 57.663 | 4.325e-05 | +1.00% | 2.20x |
| 3 | TRX/USD | 42.615 | 0.309137 | +0.16% | 0.48x |
| 4 | NIGHT/USD | 41.732 | 0.04503 | -0.02% | 2.38x |
| 5 | AKT/USD | 34.981 | 0.5138 | +0.71% | 0.70x |
| 6 | AKE/USD | 33.711 | 0.01016922 | +0.74% | 0.77x |

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

- Persisted scans: 695; predictions: 5628; observations: 420262.
- Matured sampled outcomes across 1/6/24/48h: 5479; gap abstentions: 13242. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44421194268 · **Generation:** 695 · **Legacy run:** 44421194268
**Main quote time:** 2026-11-18T23:30:26.183527+00:00 · **Legacy report time:** 2026-11-18T23:31:09.461519+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.325e-05 | 74.71 | +1.00% | 2.20x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.05559 | 67.90 | +0.27% | 1.03x | STRONG 74/100 | VERY_HIGH 80/100 | Watch |
| 3 | NIGHT/USD | 0.04503 | 55.42 | -0.02% | 2.38x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 4 | TRX/USD | 0.309137 | 38.24 | +0.16% | 0.48x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 5 | AKT/USD | 0.5138 | 35.55 | +0.71% | 0.70x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |
| 6 | AKE/USD | 0.01016922 | 35.10 | +0.74% | 0.77x | WEAK 38/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.325e-05 | 80.29 | +1.00% | 2.20x | 1781 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.0554 | 60.34 | +0.27% | 1.03x | 1284 | STRONG 70/100 | VERY_HIGH 80/100 | Watch |

**Same-run overlap:** LUNA/USD, MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
