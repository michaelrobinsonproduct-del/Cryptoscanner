# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:15:23.996732+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44419011894
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 2ef56d499c8b6e6098773638ec5ab508018b639f (atomic ledger/results publication)
**Ledger generation:** 692 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05544 | 82.808 | 64.449 | +7.36% | +0.67% | 9.90x | 23.5 | 2026-11-18T23:15:21.119768+00:00 | Not calibrated | STRONG 86/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04504 | 49.083 | 42.175 | +0.33% | +0.33% | 1.52x | 8.9 | 2026-11-18T23:15:21.119768+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 3 | AKE/USD | 0.01005757 | 36.495 | 27.233 | +0.73% | -1.15% | 2.96x | 24.7 | 2026-11-18T23:15:21.119768+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 64.449 | 0.05544 | +0.67% | 9.90x |
| 2 | NIGHT/USD | 42.175 | 0.04504 | +0.33% | 1.52x |
| 3 | AKE/USD | 27.233 | 0.01005757 | -1.15% | 2.96x |

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

- Persisted scans: 692; predictions: 5612; observations: 418435.
- Matured sampled outcomes across 1/6/24/48h: 5454; gap abstentions: 13206. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44419011894 · **Generation:** 692 · **Legacy run:** 44419011894
**Main quote time:** 2026-11-18T23:15:23.996732+00:00 · **Legacy report time:** 2026-11-18T23:15:57.340109+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05544 | 82.81 | +0.67% | 9.90x | STRONG 96/100 | VERY_HIGH 79/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04504 | 49.08 | +0.33% | 1.52x | STRONG 80/100 | HIGH 55/100 | Consider small entry |
| 3 | AKE/USD | 0.01005757 | 36.50 | -1.15% | 2.96x | WEAK 38/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05544 | 69.40 | +0.67% | 9.90x | 1281 | STRONG 90/100 | VERY_HIGH 79/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04504 | 37.66 | +0.33% | 1.52x | 11668 | MODERATE 69/100 | HIGH 61/100 | Watch |
| 3 | AKT/USD | 0.5103 | 37.28 | +1.29% | 17.79x | 4058 | MODERATE 69/100 | HIGH 66/100 | Watch |

**Same-run overlap:** MEGA/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
