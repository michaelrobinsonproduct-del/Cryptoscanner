# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:00:21.879506+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44448234573
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 2b3f3b3acc405af16d7c19af55ffca580aa0c8d3 (atomic ledger/results publication)
**Ledger generation:** 737 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3325 | 77.977 | 60.497 | +1.06% | +0.70% | 2.40x | 3.9 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SENT/USD | 0.022011 | 76.141 | 74.079 | +6.82% | +0.46% | 0.97x | 5.0 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | ICP/USD | 2.249 | 52.714 | 56.411 | +3.26% | +0.40% | 0.43x | 8.9 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | BMT/USD | 0.01937 | 50.823 | 41.186 | +2.60% | -1.07% | 2.56x | 15.5 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 5 | VVV/USD | 22.053 | 49.218 | 54.575 | +1.76% | +0.20% | 0.36x | 14.0 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | TON/USD | 1.027 | 42.799 | 33.401 | +0.59% | +0.29% | 1.79x | 9.8 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | MODERATE 66/100 | HIGH 60/100 | Watch | WATCH |
| 7 | FARTCOIN/USD | 0.0863 | 39.164 | 30.717 | +0.58% | +0.12% | 1.79x | 11.6 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | MODERATE 50/100 | HIGH 66/100 | Watch | WATCH |
| 8 | TRUMP/USD | 0.95 | 37.804 | 28.115 | +0.53% | -0.11% | 2.02x | 21.1 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 9 | MEGA/USD | 0.05698 | 36.753 | 37.399 | +1.75% | +0.25% | 0.81x | 12.3 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 10 | DRV/USD | 0.26587 | 31.717 | 31.346 | +0.45% | -0.08% | 1.08x | 10.2 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 11 | AKE/USD | 0.01047625 | 28.450 | 32.381 | +0.82% | +0.51% | 0.35x | 15.8 | 2026-11-19T03:00:13.766005+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 74.079 | 0.022011 | +0.46% | 0.97x |
| 2 | NEAR/USD | 60.497 | 3.3325 | +0.70% | 2.40x |
| 3 | ICP/USD | 56.411 | 2.249 | +0.40% | 0.43x |
| 4 | VVV/USD | 54.575 | 22.053 | +0.20% | 0.36x |
| 5 | BMT/USD | 41.186 | 0.01937 | -1.07% | 2.56x |
| 6 | MEGA/USD | 37.399 | 0.05698 | +0.25% | 0.81x |
| 7 | TON/USD | 33.401 | 1.027 | +0.29% | 1.79x |
| 8 | AKE/USD | 32.381 | 0.01047625 | +0.51% | 0.35x |
| 9 | DRV/USD | 31.346 | 0.26587 | -0.08% | 1.08x |
| 10 | FARTCOIN/USD | 30.717 | 0.0863 | +0.12% | 1.79x |
| 11 | TRUMP/USD | 28.115 | 0.95 | -0.11% | 2.02x |

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

- Persisted scans: 737; predictions: 6008; observations: 445840.
- Matured sampled outcomes across 1/6/24/48h: 5963; gap abstentions: 13517. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44448234573 · **Generation:** 737 · **Legacy run:** 44448234573
**Main quote time:** 2026-11-19T03:00:21.879506+00:00 · **Legacy report time:** 2026-11-19T03:00:57.078914+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3325 | 77.98 | +0.70% | 2.40x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD | 0.022011 | 76.14 | +0.46% | 0.97x | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |
| 3 | ICP/USD | 2.249 | 52.71 | +0.40% | 0.43x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 4 | BMT/USD | 0.01937 | 50.82 | -1.07% | 2.56x | MODERATE 50/100 | VERY_HIGH 83/100 | Watch |
| 5 | VVV/USD | 22.053 | 49.22 | +0.20% | 0.36x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 6 | TON/USD | 1.027 | 42.80 | +0.29% | 1.79x | MODERATE 66/100 | HIGH 60/100 | Watch |
| 7 | FARTCOIN/USD | 0.0863 | 39.16 | +0.12% | 1.79x | MODERATE 50/100 | HIGH 66/100 | Watch |
| 8 | TRUMP/USD | 0.95 | 37.80 | -0.11% | 2.02x | WEAK 39/100 | VERY_HIGH 78/100 | Watch |
| 9 | MEGA/USD | 0.05698 | 36.75 | +0.25% | 0.81x | WEAK 43/100 | VERY_HIGH 80/100 | Watch |
| 10 | DRV/USD | 0.26587 | 31.72 | -0.08% | 1.08x | WEAK 21/100 | VERY_HIGH 79/100 | Do nothing |
| 11 | AKE/USD | 0.01047625 | 28.45 | +0.51% | 0.35x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3221 | 59.04 | +0.70% | 2.40x | 13307 | STRONG 95/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
