# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T22:31:08.649408+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44412224281
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ffe3bfe0119be01342839b8f68aaf537ba4cf4e7 (atomic ledger/results publication)
**Ledger generation:** 684 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020163 | 65.232 | 72.733 | +8.00% | -1.73% | 1.11x | 6.9 | 2026-11-18T22:31:03.617432+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 2 | STABLE/USD | 0.02292 | 48.968 | 60.527 | +8.88% | -0.48% | 0.08x | 30.6 | 2026-11-18T22:31:03.617432+00:00 | Not calibrated | WEAK 19/100 | EXTREME 100/100 | Do nothing | WATCH |
| 3 | VVV/USD | 21.134 | 39.380 | 50.383 | +0.51% | -0.61% | 0.21x | 0.9 | 2026-11-18T22:31:03.617432+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | AKE/USD | 0.01023727 | 38.745 | 42.322 | +2.53% | -0.37% | 0.83x | 19.8 | 2026-11-18T22:31:03.617432+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 5 | LUNA/USD | 4.248e-05 | 31.095 | 38.617 | +1.99% | +0.35% | 0.07x | 14.1 | 2026-11-18T22:31:03.617432+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | WINGS/USD | 0.001847 | 10.551 | 28.748 | +0.76% | -2.99% | 0.68x | 16.3 | 2026-11-18T22:31:03.617432+00:00 | Not calibrated | WEAK 5/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.733 | 0.020163 | -1.73% | 1.11x |
| 2 | STABLE/USD | 60.527 | 0.02292 | -0.48% | 0.08x |
| 3 | VVV/USD | 50.383 | 21.134 | -0.61% | 0.21x |
| 4 | AKE/USD | 42.322 | 0.01023727 | -0.37% | 0.83x |
| 5 | LUNA/USD | 38.617 | 4.248e-05 | +0.35% | 0.07x |
| 6 | WINGS/USD | 28.748 | 0.001847 | -2.99% | 0.68x |

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

- Persisted scans: 684; predictions: 5587; observations: 413563.
- Matured sampled outcomes across 1/6/24/48h: 5355; gap abstentions: 13170. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44412224281 · **Generation:** 684 · **Legacy run:** 44412224281
**Main quote time:** 2026-11-18T22:31:08.649408+00:00 · **Legacy report time:** 2026-11-18T22:31:36.249563+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.020163 | 65.23 | -1.73% | 1.11x | WEAK 43/100 | VERY_HIGH 84/100 | Do nothing |
| 2 | STABLE/USD | 0.02292 | 48.97 | -0.48% | 0.08x | WEAK 19/100 | EXTREME 100/100 | Do nothing |
| 3 | VVV/USD | 21.134 | 39.38 | -0.61% | 0.21x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | AKE/USD | 0.01023727 | 38.75 | -0.37% | 0.83x | WEAK 19/100 | VERY_HIGH 79/100 | Do nothing |
| 5 | LUNA/USD | 4.248e-05 | 31.10 | +0.35% | 0.07x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |
| 6 | WINGS/USD | 0.001847 | 10.55 | -2.99% | 0.68x | WEAK 5/100 | EXTREME 98/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
