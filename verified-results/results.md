# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:45:13.472885+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44423310273
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ccb814237f10ee72f65dcb655cf2a95720eb62a3 (atomic ledger/results publication)
**Ledger generation:** 698 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRX/USD | 0.309571 | 59.341 | 43.639 | +0.54% | +0.14% | 4.11x | 0.0 | 2026-11-18T23:45:08.555684+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05563 | 56.002 | 63.636 | +7.73% | +0.07% | 0.20x | 25.2 | 2026-11-18T23:45:08.555684+00:00 | Not calibrated | WEAK 38/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | AKE/USD | 0.01031642 | 51.120 | 43.761 | +3.33% | +1.82% | 0.82x | 28.1 | 2026-11-18T23:45:08.555684+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04536 | 42.831 | 44.658 | +1.05% | +0.73% | 0.45x | 13.2 | 2026-11-18T23:45:08.555684+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5194 | 41.452 | 44.660 | +1.98% | +1.11% | 0.12x | 1.9 | 2026-11-18T23:45:08.555684+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 63.636 | 0.05563 | +0.07% | 0.20x |
| 2 | AKT/USD | 44.660 | 0.5194 | +1.11% | 0.12x |
| 3 | NIGHT/USD | 44.658 | 0.04536 | +0.73% | 0.45x |
| 4 | AKE/USD | 43.761 | 0.01031642 | +1.82% | 0.82x |
| 5 | TRX/USD | 43.639 | 0.309571 | +0.14% | 4.11x |

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

- Persisted scans: 698; predictions: 5644; observations: 422089.
- Matured sampled outcomes across 1/6/24/48h: 5503; gap abstentions: 13278. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44423310273 · **Generation:** 698 · **Legacy run:** 44423310273
**Main quote time:** 2026-11-18T23:45:13.472885+00:00 · **Legacy report time:** 2026-11-18T23:45:41.177154+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD ⭐ | 0.309571 | 59.34 | +0.14% | 4.11x | STRONG 85/100 | HIGH 55/100 | Watch |
| 2 | MEGA/USD | 0.05563 | 56.00 | +0.07% | 0.20x | WEAK 38/100 | EXTREME 94/100 | Do nothing |
| 3 | AKE/USD | 0.01031642 | 51.12 | +1.82% | 0.82x | MODERATE 46/100 | VERY_HIGH 79/100 | Watch |
| 4 | NIGHT/USD | 0.04536 | 42.83 | +0.73% | 0.45x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 5 | AKT/USD | 0.5194 | 41.45 | +1.11% | 0.12x | MODERATE 51/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD ⭐ | 0.309571 | 57.78 | +0.14% | 4.11x | 4048 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
