# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T16:31:33.998321+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45044125231
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 10792e7f4f722dcedeefef420385280581331217 (atomic ledger/results publication)
**Ledger generation:** 1307 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04941 | 104.815 | 86.281 | +11.59% | +2.83% | 1.44x | 14.2 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.9886 | 91.403 | 77.803 | +3.54% | -0.28% | 3.75x | 4.0 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ZBCN/USD | 0.001904 | 86.075 | 71.075 | +10.25% | +0.00% | 5.13x | 15.8 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | STRONG 83/100 | HIGH 66/100 | Watch | WATCH |
| 4 | DRV/USD | 0.36307 | 79.993 | 86.040 | +8.31% | -0.38% | 0.58x | 5.2 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | INJ/USD | 6.226 | 73.315 | 67.183 | +4.24% | -0.18% | 1.70x | 6.4 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 6 | PUMP/USD | 0.00254 | 71.061 | 79.645 | +8.36% | -0.31% | 0.30x | 11.8 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.93 | 70.858 | 73.522 | +2.76% | -0.08% | 0.77x | 1.6 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ZEC/USD | 794.91 | 70.815 | 67.856 | +2.15% | +0.07% | 1.26x | 4.4 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | MODERATE 60/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XBT/USD | 61142.4 | 66.592 | 67.253 | +1.75% | +0.26% | 0.80x | 0.0 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ETH/USD | 1718.31 | 65.010 | 69.236 | +2.14% | +0.10% | 0.53x | 1.5 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ADA/USD | 0.145173 | 61.669 | 46.783 | +0.72% | +0.00% | 2.49x | 2.2 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 12 | DOT/USD | 0.6627 | 56.627 | 41.778 | +1.49% | -0.03% | 3.45x | 1.5 | 2026-11-22T16:31:25.090616+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 86.281 | 0.04941 | +2.83% | 1.44x |
| 2 | DRV/USD | 86.040 | 0.36307 | -0.38% | 0.58x |
| 3 | PUMP/USD | 79.645 | 0.00254 | -0.31% | 0.30x |
| 4 | NEAR/USD | 77.803 | 2.9886 | -0.28% | 3.75x |
| 5 | HYPE/USD | 73.522 | 62.93 | -0.08% | 0.77x |
| 6 | ZBCN/USD | 71.075 | 0.001904 | +0.00% | 5.13x |
| 7 | ETH/USD | 69.236 | 1718.31 | +0.10% | 0.53x |
| 8 | ZEC/USD | 67.856 | 794.91 | +0.07% | 1.26x |
| 9 | XBT/USD | 67.253 | 61142.4 | +0.26% | 0.80x |
| 10 | INJ/USD | 67.183 | 6.226 | -0.18% | 1.70x |
| 11 | ADA/USD | 46.783 | 0.145173 | +0.00% | 2.49x |
| 12 | DOT/USD | 41.778 | 0.6627 | -0.03% | 3.45x |

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

- Persisted scans: 1307; predictions: 10603; observations: 791071.
- Matured sampled outcomes across 1/6/24/48h: 15658; gap abstentions: 22323. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45044125231 · **Generation:** 1307 · **Legacy run:** 45044125231
**Main quote time:** 2026-11-22T16:31:33.998321+00:00 · **Legacy report time:** 2026-11-22T16:32:20.633985+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04941 | 104.81 | +2.83% | 1.44x | STRONG 100/100 | HIGH 61/100 | Watch |
| 2 | NEAR/USD | 2.9886 | 91.40 | -0.28% | 3.75x | STRONG 76/100 | HIGH 61/100 | Watch |
| 3 | ZBCN/USD | 0.001904 | 86.07 | +0.00% | 5.13x | STRONG 83/100 | HIGH 66/100 | Watch |
| 4 | DRV/USD | 0.36307 | 79.99 | -0.38% | 0.58x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 5 | INJ/USD | 6.226 | 73.31 | -0.18% | 1.70x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 6 | PUMP/USD | 0.00254 | 71.06 | -0.31% | 0.30x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 7 | HYPE/USD | 62.93 | 70.86 | -0.08% | 0.77x | WEAK 40/100 | HIGH 68/100 | Watch |
| 8 | ZEC/USD ⭐ | 794.91 | 70.81 | +0.07% | 1.26x | STRONG 70/100 | HIGH 55/100 | Watch |
| 9 | XBT/USD | 61142.4 | 66.59 | +0.26% | 0.80x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 10 | ETH/USD | 1718.31 | 65.01 | +0.10% | 0.53x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 11 | ADA/USD | 0.145173 | 61.67 | +0.00% | 2.49x | STRONG 76/100 | HIGH 55/100 | Watch |
| 12 | DOT/USD | 0.6627 | 56.63 | -0.03% | 3.45x | MODERATE 58/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04943 | 90.78 | +2.83% | 1.44x | 10089 | STRONG 95/100 | HIGH 61/100 | Watch |
| 2 | SUI/USD | 0.6594 | 76.96 | +0.20% | 16.92x | 6243 | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD ⭐ | 794.91 | 74.53 | +0.07% | 1.26x | 21807 | STRONG 72/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
