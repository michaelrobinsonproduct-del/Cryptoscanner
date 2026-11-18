# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T22:45:18.451658+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44414444386
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** f4f1084eb41e0bc977fa13e40e21ad2d6678eb44 (atomic ledger/results publication)
**Ledger generation:** 686 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.284e-05 | 39.091 | 43.607 | +2.86% | +0.90% | 0.10x | 16.3 | 2026-11-18T22:45:15.239363+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 2 | VVV/USD | 21.111 | 37.050 | 46.518 | +0.40% | -0.09% | 0.10x | 5.7 | 2026-11-18T22:45:15.239363+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | TRX/USD | 0.3089 | 36.820 | 41.692 | +0.32% | +0.06% | 0.48x | 1.2 | 2026-11-18T22:45:15.239363+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | AKE/USD | 0.01013158 | 22.421 | 33.747 | +1.48% | -1.25% | 0.49x | 22.0 | 2026-11-18T22:45:15.239363+00:00 | Not calibrated | WEAK 6/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 46.518 | 21.111 | -0.09% | 0.10x |
| 2 | LUNA/USD | 43.607 | 4.284e-05 | +0.90% | 0.10x |
| 3 | TRX/USD | 41.692 | 0.3089 | +0.06% | 0.48x |
| 4 | AKE/USD | 33.747 | 0.01013158 | -1.25% | 0.49x |

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

- Persisted scans: 686; predictions: 5596; observations: 414781.
- Matured sampled outcomes across 1/6/24/48h: 5394; gap abstentions: 13170. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44414444386 · **Generation:** 686 · **Legacy run:** 44414444386
**Main quote time:** 2026-11-18T22:45:18.451658+00:00 · **Legacy report time:** 2026-11-18T22:45:55.845497+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.284e-05 | 39.09 | +0.90% | 0.10x | MODERATE 45/100 | VERY_HIGH 81/100 | Watch |
| 2 | VVV/USD | 21.111 | 37.05 | -0.09% | 0.10x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | TRX/USD | 0.3089 | 36.82 | +0.06% | 0.48x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 4 | AKE/USD | 0.01013158 | 22.42 | -1.25% | 0.49x | WEAK 6/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD | 0.001913 | 91.72 | +3.57% | 3.11x | 4605 | STRONG 100/100 | VERY_HIGH 70/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
