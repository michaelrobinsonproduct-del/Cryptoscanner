# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T00:31:13.386067+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45917014048
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c6b1ce5c23101337e1ad516f68be82639fb3baad (atomic ledger/results publication)
**Ledger generation:** 1934 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 62.69 | 74.810 | 59.489 | +0.76% | +0.06% | 2.85x | 1.6 | 2026-11-27T00:31:07.377901+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 2 | LINK/USD | 9.31064 | 73.180 | 56.857 | +0.46% | +0.26% | 63.78x | 2.7 | 2026-11-27T00:31:07.377901+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 690.84 | 70.204 | 62.834 | +1.35% | +0.49% | 1.49x | 3.2 | 2026-11-27T00:31:07.377901+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | VVV/USD | 26.494 | 62.953 | 60.674 | +1.19% | +0.42% | 1.02x | 5.3 | 2026-11-27T00:31:07.377901+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 5 | LTC/USD | 43.88 | 54.279 | 56.101 | +0.32% | +0.09% | 0.77x | 2.3 | 2026-11-27T00:31:07.377901+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.228 | 53.629 | 33.232 | +0.90% | +1.08% | 4.88x | 11.4 | 2026-11-27T00:31:07.377901+00:00 | Not calibrated | STRONG 77/100 | HIGH 66/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.49e-06 | 36.103 | 40.436 | +0.34% | +0.09% | 0.52x | 2.9 | 2026-11-27T00:31:07.377901+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CRV/USD | 0.17537 | 35.255 | 35.444 | +0.72% | +0.55% | 0.71x | 11.4 | 2026-11-27T00:31:07.377901+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | HBAR/USD | 0.05423 | 33.251 | 36.357 | +0.50% | +0.41% | 0.49x | 3.7 | 2026-11-27T00:31:07.377901+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 62.834 | 690.84 | +0.49% | 1.49x |
| 2 | VVV/USD | 60.674 | 26.494 | +0.42% | 1.02x |
| 3 | HYPE/USD | 59.489 | 62.69 | +0.06% | 2.85x |
| 4 | LINK/USD | 56.857 | 9.31064 | +0.26% | 63.78x |
| 5 | LTC/USD | 56.101 | 43.88 | +0.09% | 0.77x |
| 6 | PEPE/USD | 40.436 | 3.49e-06 | +0.09% | 0.52x |
| 7 | HBAR/USD | 36.357 | 0.05423 | +0.41% | 0.49x |
| 8 | CRV/USD | 35.444 | 0.17537 | +0.55% | 0.71x |
| 9 | ATOM/USD | 33.232 | 1.228 | +1.08% | 4.88x |

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

- Persisted scans: 1934; predictions: 16910; observations: 1171419.
- Matured sampled outcomes across 1/6/24/48h: 37028; gap abstentions: 25401. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 149 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45917014048 · **Generation:** 1934 · **Legacy run:** 45917014048
**Main quote time:** 2026-11-27T00:31:13.386067+00:00 · **Legacy report time:** 2026-11-27T00:31:49.481734+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.69 | 74.81 | +0.06% | 2.85x | STRONG 92/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD ⭐ | 9.31064 | 73.18 | +0.26% | 63.78x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 690.84 | 70.20 | +0.49% | 1.49x | STRONG 90/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD ⭐ | 26.494 | 62.95 | +0.42% | 1.02x | STRONG 76/100 | HIGH 62/100 | Watch |
| 5 | LTC/USD | 43.88 | 54.28 | +0.09% | 0.77x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 6 | ATOM/USD | 1.228 | 53.63 | +1.08% | 4.88x | STRONG 77/100 | HIGH 66/100 | Watch |
| 7 | PEPE/USD | 3.49e-06 | 36.10 | +0.09% | 0.52x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 8 | CRV/USD | 0.17537 | 35.26 | +0.55% | 0.71x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |
| 9 | HBAR/USD | 0.05423 | 33.25 | +0.41% | 0.49x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.69 | 65.48 | +0.06% | 2.85x | 12730 | STRONG 88/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 690.17 | 64.04 | +0.49% | 1.49x | 33037 | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | LINK/USD ⭐ | 9.31064 | 60.57 | +0.26% | 63.78x | 6957 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD ⭐ | 26.494 | 52.58 | +0.42% | 1.02x | 19724 | STRONG 71/100 | HIGH 62/100 | Watch |

**Same-run overlap:** HYPE/USD, LINK/USD, ZEC/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
