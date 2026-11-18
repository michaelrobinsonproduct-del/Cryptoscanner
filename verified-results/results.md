# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T01:20:00.280999+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44214927224
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 0108b0bc060b1d03e41ca50250f9c5e1d2acb058 (atomic ledger/results publication)
**Ledger generation:** 493 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CAP/USD | 0.101439 | 45.883 | 32.736 | +0.46% | -0.37% | 2.55x | 6.1 | 2026-11-18T01:19:57.143127+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 2 | UP/USD | 0.05516 | 44.807 | 42.554 | +4.10% | +1.20% | 0.63x | 34.6 | 2026-11-18T01:19:57.143127+00:00 | Not calibrated | WEAK 42/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | PROS/USD | 0.5317 | 32.561 | 34.696 | +2.86% | -0.62% | 1.10x | 32.3 | 2026-11-18T01:19:57.143127+00:00 | Not calibrated | WEAK 16/100 | EXTREME 92/100 | Do nothing | WATCH |
| 4 | AKE/USD | 0.01001579 | 31.227 | 28.498 | +0.32% | +0.04% | 1.25x | 17.2 | 2026-11-18T01:19:57.143127+00:00 | Not calibrated | WEAK 36/100 | HIGH 66/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5134 | 23.887 | 30.048 | +0.81% | +0.27% | 0.25x | 15.6 | 2026-11-18T01:19:57.143127+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 42.554 | 0.05516 | +1.20% | 0.63x |
| 2 | PROS/USD | 34.696 | 0.5317 | -0.62% | 1.10x |
| 3 | CAP/USD | 32.736 | 0.101439 | -0.37% | 2.55x |
| 4 | AKT/USD | 30.048 | 0.5134 | +0.27% | 0.25x |
| 5 | AKE/USD | 28.498 | 0.01001579 | +0.04% | 1.25x |

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

- Persisted scans: 493; predictions: 4257; observations: 297244.
- Matured sampled outcomes across 1/6/24/48h: 3375; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44214927224 · **Generation:** 493 · **Legacy run:** 44214927224
**Main quote time:** 2026-11-18T01:20:00.280999+00:00 · **Legacy report time:** 2026-11-18T01:20:13.875995+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.101439 | 45.88 | -0.37% | 2.55x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 2 | UP/USD ⭐ | 0.05516 | 44.81 | +1.20% | 0.63x | MODERATE 52/100 | EXTREME 94/100 | Do nothing |
| 3 | PROS/USD ⭐ | 0.5317 | 32.56 | -0.62% | 1.10x | WEAK 26/100 | EXTREME 92/100 | Do nothing |
| 4 | AKE/USD ⭐ | 0.01001579 | 31.23 | +0.04% | 1.25x | MODERATE 46/100 | HIGH 66/100 | Watch |
| 5 | AKT/USD | 0.5134 | 23.89 | +0.27% | 0.25x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UP/USD ⭐ | 0.05516 | 79.08 | +2.03% | 1.56x | 3480 | STRONG 85/100 | VERY_HIGH 79/100 | Watch |
| 2 | PROS/USD ⭐ | 0.5275 | 39.39 | +0.53% | 1.74x | 1169 | MODERATE 65/100 | VERY_HIGH 79/100 | Watch |
| 3 | AKE/USD ⭐ | 0.01001579 | 32.69 | +0.50% | 1.61x | 5823 | MODERATE 66/100 | HIGH 66/100 | Watch |

**Same-run overlap:** UP/USD, PROS/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
