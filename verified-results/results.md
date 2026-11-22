# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T16:41:27.013556+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45045064577
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 511ee1e036d4d4dcd50582d367b7be120fce7e7d (atomic ledger/results publication)
**Ledger generation:** 1308 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 6.245 | 82.857 | 69.453 | +4.55% | -0.32% | 4.63x | 6.4 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XBT/USD | 61264.6 | 78.860 | 68.595 | +1.95% | -0.04% | 2.04x | 0.2 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NEAR/USD | 2.9917 | 77.625 | 78.388 | +3.65% | -0.71% | 1.28x | 4.3 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 4 | DRV/USD | 0.36181 | 74.181 | 81.388 | +7.94% | -0.28% | 0.42x | 14.4 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002539 | 73.449 | 81.642 | +8.32% | -0.74% | 0.55x | 7.9 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | HYPE/USD | 63 | 70.598 | 73.530 | +2.87% | -0.17% | 0.79x | 3.2 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ZEC/USD | 793.69 | 69.300 | 66.820 | +1.99% | -0.28% | 1.39x | 4.3 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ETH/USD | 1720.78 | 69.138 | 70.991 | +2.29% | -0.03% | 0.83x | 0.1 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6604 | 64.064 | 68.409 | +2.02% | -0.18% | 0.66x | 1.5 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SOL/USD | 70.54 | 61.413 | 57.274 | +0.53% | +0.01% | 1.41x | 2.8 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 11 | ZBCN/USD | 0.001906 | 61.343 | 68.475 | +10.36% | +0.37% | 0.10x | 21.0 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | DOT/USD | 0.6645 | 58.834 | 43.834 | +1.76% | +0.00% | 6.62x | 1.5 | 2026-11-22T16:41:18.639792+00:00 | Not calibrated | STRONG 74/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 81.642 | 0.002539 | -0.74% | 0.55x |
| 2 | DRV/USD | 81.388 | 0.36181 | -0.28% | 0.42x |
| 3 | NEAR/USD | 78.388 | 2.9917 | -0.71% | 1.28x |
| 4 | HYPE/USD | 73.530 | 63 | -0.17% | 0.79x |
| 5 | ETH/USD | 70.991 | 1720.78 | -0.03% | 0.83x |
| 6 | INJ/USD | 69.453 | 6.245 | -0.32% | 4.63x |
| 7 | XBT/USD | 68.595 | 61264.6 | -0.04% | 2.04x |
| 8 | ZBCN/USD | 68.475 | 0.001906 | +0.37% | 0.10x |
| 9 | SUI/USD | 68.409 | 0.6604 | -0.18% | 0.66x |
| 10 | ZEC/USD | 66.820 | 793.69 | -0.28% | 1.39x |
| 11 | SOL/USD | 57.274 | 70.54 | +0.01% | 1.41x |
| 12 | DOT/USD | 43.834 | 0.6645 | +0.00% | 6.62x |

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

- Persisted scans: 1308; predictions: 10615; observations: 791680.
- Matured sampled outcomes across 1/6/24/48h: 15694; gap abstentions: 22323. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45045064577 · **Generation:** 1308 · **Legacy run:** 45045064577
**Main quote time:** 2026-11-22T16:41:27.013556+00:00 · **Legacy report time:** 2026-11-22T16:42:14.442493+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 6.245 | 82.86 | -0.32% | 4.63x | STRONG 71/100 | HIGH 61/100 | Watch |
| 2 | XBT/USD | 61264.6 | 78.86 | -0.04% | 2.04x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 3 | NEAR/USD | 2.9917 | 77.63 | -0.71% | 1.28x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 4 | DRV/USD | 0.36181 | 74.18 | -0.28% | 0.42x | WEAK 37/100 | VERY_HIGH 82/100 | Watch |
| 5 | PUMP/USD | 0.002539 | 73.45 | -0.74% | 0.55x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | HYPE/USD | 63 | 70.60 | -0.17% | 0.79x | WEAK 40/100 | HIGH 68/100 | Watch |
| 7 | ZEC/USD | 793.69 | 69.30 | -0.28% | 1.39x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 8 | ETH/USD | 1720.78 | 69.14 | -0.03% | 0.83x | WEAK 40/100 | HIGH 68/100 | Watch |
| 9 | SUI/USD | 0.6604 | 64.06 | -0.18% | 0.66x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | SOL/USD | 70.54 | 61.41 | +0.01% | 1.41x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 11 | ZBCN/USD | 0.001906 | 61.34 | +0.37% | 0.10x | MODERATE 51/100 | EXTREME 87/100 | Do nothing |
| 12 | DOT/USD | 0.6645 | 58.83 | +0.00% | 6.62x | STRONG 74/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04963 | 91.85 | +1.98% | 2.21x | 10083 | STRONG 91/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
