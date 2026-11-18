# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:55:17.464375+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44424678088
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** a70463620c4a0d164ee4cc7938b8a914b0cf8ea6 (atomic ledger/results publication)
**Ledger generation:** 700 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020787 | 75.783 | 73.908 | +11.35% | +0.48% | 0.95x | 4.8 | 2026-11-18T23:55:12.429848+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | AKE/USD | 0.01035749 | 63.196 | 53.368 | +3.74% | +1.21% | 1.38x | 14.7 | 2026-11-18T23:55:12.429848+00:00 | Not calibrated | STRONG 72/100 | HIGH 66/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.0562 | 62.892 | 62.834 | +8.83% | +1.39% | 0.31x | 26.8 | 2026-11-18T23:55:12.429848+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | TRX/USD | 0.309983 | 60.198 | 44.083 | +0.68% | +0.22% | 5.31x | 1.1 | 2026-11-18T23:55:12.429848+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 5 | LUNA/USD | 4.354e-05 | 56.508 | 54.616 | +4.54% | +0.02% | 1.18x | 18.4 | 2026-11-18T23:55:12.429848+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | REKT/USD | 7.17e-08 | 44.398 | 55.138 | +10.31% | -0.55% | 0.20x | 41.9 | 2026-11-18T23:55:12.429848+00:00 | Not calibrated | WEAK 12/100 | EXTREME 100/100 | Do nothing | WATCH |
| 7 | NIGHT/USD | 0.04558 | 43.236 | 48.181 | +1.54% | +0.40% | 0.31x | 13.2 | 2026-11-18T23:55:12.429848+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5197 | 33.877 | 41.175 | +2.04% | +0.27% | 0.14x | 9.6 | 2026-11-18T23:55:12.429848+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.908 | 0.020787 | +0.48% | 0.95x |
| 2 | MEGA/USD | 62.834 | 0.0562 | +1.39% | 0.31x |
| 3 | REKT/USD | 55.138 | 7.17e-08 | -0.55% | 0.20x |
| 4 | LUNA/USD | 54.616 | 4.354e-05 | +0.02% | 1.18x |
| 5 | AKE/USD | 53.368 | 0.01035749 | +1.21% | 1.38x |
| 6 | NIGHT/USD | 48.181 | 0.04558 | +0.40% | 0.31x |
| 7 | TRX/USD | 44.083 | 0.309983 | +0.22% | 5.31x |
| 8 | AKT/USD | 41.175 | 0.5197 | +0.27% | 0.14x |

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

- Persisted scans: 700; predictions: 5658; observations: 423307.
- Matured sampled outcomes across 1/6/24/48h: 5520; gap abstentions: 13302. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44424678088 · **Generation:** 700 · **Legacy run:** 44424678088
**Main quote time:** 2026-11-18T23:55:17.464375+00:00 · **Legacy report time:** 2026-11-18T23:55:58.568615+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.020787 | 75.78 | +0.48% | 0.95x | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |
| 2 | AKE/USD ⭐ | 0.01035749 | 63.20 | +1.21% | 1.38x | STRONG 82/100 | HIGH 66/100 | Watch |
| 3 | MEGA/USD | 0.0562 | 62.89 | +1.39% | 0.31x | MODERATE 51/100 | EXTREME 94/100 | Do nothing |
| 4 | TRX/USD ⭐ | 0.309983 | 60.20 | +0.22% | 5.31x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 5 | LUNA/USD | 4.354e-05 | 56.51 | +0.02% | 1.18x | MODERATE 48/100 | VERY_HIGH 73/100 | Watch |
| 6 | REKT/USD | 7.17e-08 | 44.40 | -0.55% | 0.20x | WEAK 12/100 | EXTREME 100/100 | Do nothing |
| 7 | NIGHT/USD | 0.04558 | 43.24 | +0.40% | 0.31x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 8 | AKT/USD | 0.5197 | 33.88 | +0.27% | 0.14x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKE/USD ⭐ | 0.01035749 | 74.74 | +1.21% | 1.38x | 3407 | STRONG 82/100 | VERY_HIGH 72/100 | Watch |
| 2 | TRX/USD ⭐ | 0.309386 | 55.44 | +0.22% | 5.31x | 4056 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** AKE/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
