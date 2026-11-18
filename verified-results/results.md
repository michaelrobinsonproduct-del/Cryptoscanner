# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:35:20.462410+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44421914073
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** f455704870aa0d10a1f097463b5437485ae53326 (atomic ledger/results publication)
**Ledger generation:** 696 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05539 | 72.280 | 70.775 | +7.26% | +0.31% | 1.00x | 10.8 | 2026-11-18T23:35:15.085319+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | TRX/USD | 0.309254 | 59.010 | 42.963 | +0.44% | +0.21% | 3.20x | 0.0 | 2026-11-18T23:35:15.085319+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04533 | 47.084 | 46.521 | +0.98% | +0.44% | 0.83x | 8.8 | 2026-11-18T23:35:15.085319+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 4 | AKE/USD | 0.01018083 | 43.811 | 40.416 | +1.97% | +0.39% | 1.14x | 15.6 | 2026-11-18T23:35:15.085319+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5144 | 36.281 | 34.844 | +1.00% | +0.76% | 0.76x | 7.8 | 2026-11-18T23:35:15.085319+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 70.775 | 0.05539 | +0.31% | 1.00x |
| 2 | NIGHT/USD | 46.521 | 0.04533 | +0.44% | 0.83x |
| 3 | TRX/USD | 42.963 | 0.309254 | +0.21% | 3.20x |
| 4 | AKE/USD | 40.416 | 0.01018083 | +0.39% | 1.14x |
| 5 | AKT/USD | 34.844 | 0.5144 | +0.76% | 0.76x |

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

- Persisted scans: 696; predictions: 5633; observations: 420871.
- Matured sampled outcomes across 1/6/24/48h: 5492; gap abstentions: 13254. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44421914073 · **Generation:** 696 · **Legacy run:** 44421914073
**Main quote time:** 2026-11-18T23:35:20.462410+00:00 · **Legacy report time:** 2026-11-18T23:35:56.489004+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.05539 | 72.28 | +0.31% | 1.00x | MODERATE 61/100 | VERY_HIGH 80/100 | Watch |
| 2 | TRX/USD ⭐ | 0.309254 | 59.01 | +0.21% | 3.20x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD | 0.04533 | 47.08 | +0.44% | 0.83x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 4 | AKE/USD ⭐ | 0.01018083 | 43.81 | +0.39% | 1.14x | MODERATE 62/100 | VERY_HIGH 73/100 | Watch |
| 5 | AKT/USD | 0.5144 | 36.28 | +0.76% | 0.76x | MODERATE 48/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD ⭐ | 0.309161 | 56.41 | +0.21% | 3.20x | 4057 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 2 | AKE/USD ⭐ | 0.01018083 | 50.05 | +0.39% | 1.14x | 3383 | MODERATE 60/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** TRX/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
