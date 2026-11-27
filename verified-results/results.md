# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T02:01:24.917816+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45925682910
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 977f37a7a57fabb656c624538e08e018653c7525 (atomic ledger/results publication)
**Ledger generation:** 1943 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 710 | 72.732 | 81.846 | +4.16% | -0.18% | 0.18x | 4.5 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XRP/USD | 0.95081 | 59.556 | 60.932 | +0.85% | +0.17% | 0.78x | 0.1 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 3 | AUD/USD | 0.66584 | 58.261 | 42.456 | +0.33% | +0.16% | 9.15x | 2.4 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0834 | 57.787 | 60.395 | +1.16% | +0.08% | 0.70x | 5.5 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ETH/USD | 1704.99 | 56.928 | 62.150 | +1.03% | +0.11% | 0.42x | 0.1 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XBT/USD | 60847.2 | 55.543 | 59.032 | +0.58% | +0.05% | 0.63x | 0.0 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SOL/USD | 71.65 | 54.596 | 60.610 | +1.00% | +0.13% | 0.34x | 2.8 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.99 | 53.468 | 62.075 | +1.24% | +0.00% | 0.14x | 3.2 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LTC/USD | 44.17 | 51.668 | 60.209 | +0.98% | -0.32% | 0.30x | 2.3 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | XMR/USD | 461.28 | 50.624 | 57.294 | +0.95% | -0.25% | 0.46x | 8.7 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | LINK/USD | 9.35269 | 48.849 | 59.117 | +0.91% | -0.19% | 0.07x | 4.5 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | PAXG/USD | 3584.54 | 47.415 | 42.564 | +0.78% | +0.44% | 1.27x | 1.8 | 2026-11-27T02:01:18.459002+00:00 | Not calibrated | MODERATE 59/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 81.846 | 710 | -0.18% | 0.18x |
| 2 | ETH/USD | 62.150 | 1704.99 | +0.11% | 0.42x |
| 3 | HYPE/USD | 62.075 | 62.99 | +0.00% | 0.14x |
| 4 | XRP/USD | 60.932 | 0.95081 | +0.17% | 0.78x |
| 5 | SOL/USD | 60.610 | 71.65 | +0.13% | 0.34x |
| 6 | NEAR/USD | 60.395 | 3.0834 | +0.08% | 0.70x |
| 7 | LTC/USD | 60.209 | 44.17 | -0.32% | 0.30x |
| 8 | LINK/USD | 59.117 | 9.35269 | -0.19% | 0.07x |
| 9 | XBT/USD | 59.032 | 60847.2 | +0.05% | 0.63x |
| 10 | XMR/USD | 57.294 | 461.28 | -0.25% | 0.46x |
| 11 | PAXG/USD | 42.564 | 3584.54 | +0.44% | 1.27x |
| 12 | AUD/USD | 42.456 | 0.66584 | +0.16% | 9.15x |

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

- Persisted scans: 1943; predictions: 17018; observations: 1176828.
- Matured sampled outcomes across 1/6/24/48h: 37329; gap abstentions: 25449. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45925682910 · **Generation:** 1943 · **Legacy run:** 45925682910
**Main quote time:** 2026-11-27T02:01:24.917816+00:00 · **Legacy report time:** 2026-11-27T02:02:15.626482+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 710 | 72.73 | -0.18% | 0.18x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 2 | XRP/USD | 0.95081 | 59.56 | +0.17% | 0.78x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 3 | AUD/USD | 0.66584 | 58.26 | +0.16% | 9.15x | STRONG 74/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD | 3.0834 | 57.79 | +0.08% | 0.70x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 5 | ETH/USD | 1704.99 | 56.93 | +0.11% | 0.42x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 6 | XBT/USD | 60847.2 | 55.54 | +0.05% | 0.63x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 7 | SOL/USD | 71.65 | 54.60 | +0.13% | 0.34x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 8 | HYPE/USD | 62.99 | 53.47 | +0.00% | 0.14x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 9 | LTC/USD | 44.17 | 51.67 | -0.32% | 0.30x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | XMR/USD | 461.28 | 50.62 | -0.25% | 0.46x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | LINK/USD | 9.35269 | 48.85 | -0.19% | 0.07x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | PAXG/USD | 3584.54 | 47.41 | +0.44% | 1.27x | MODERATE 59/100 | HIGH 55/100 | Watch |

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
