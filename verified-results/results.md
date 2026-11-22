# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T15:21:19.366197+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45037667120
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 749e7494d4fedc40f6d85f04a743eb334ab9bc60 (atomic ledger/results publication)
**Ledger generation:** 1300 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 62.62 | 82.028 | 69.177 | +2.25% | -0.43% | 3.04x | 3.2 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 2 | DRV/USD | 0.37147 | 77.376 | 81.291 | +10.82% | -3.78% | 2.52x | 14.8 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.04812 | 77.346 | 84.216 | +8.67% | -1.17% | 0.90x | 16.6 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 4 | STBL/USD | 0.017075 | 75.463 | 74.951 | +6.69% | +0.56% | 0.77x | 1.8 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9996 | 73.887 | 80.315 | +3.93% | -0.94% | 0.83x | 4.3 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 6 | VVV/USD | 25.578 | 73.515 | 71.912 | +2.72% | -0.23% | 1.28x | 4.3 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ZEC/USD | 793.78 | 72.528 | 66.838 | +2.01% | -0.48% | 1.81x | 4.4 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 8 | TAO/USD | 190.7772 | 68.521 | 64.885 | +2.72% | -0.01% | 1.37x | 6.1 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ETH/USD | 1711.07 | 64.737 | 66.950 | +1.71% | -0.11% | 0.83x | 0.1 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XBT/USD | 60780.4 | 60.037 | 63.036 | +1.15% | -0.25% | 0.82x | 0.0 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6566 | 55.253 | 63.534 | +1.44% | -0.21% | 0.28x | 3.0 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | INJ/USD | 6.14 | 54.447 | 58.340 | +2.80% | -0.34% | 0.78x | 4.9 | 2026-11-22T15:21:11.128226+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 84.216 | 0.04812 | -1.17% | 0.90x |
| 2 | DRV/USD | 81.291 | 0.37147 | -3.78% | 2.52x |
| 3 | NEAR/USD | 80.315 | 2.9996 | -0.94% | 0.83x |
| 4 | STBL/USD | 74.951 | 0.017075 | +0.56% | 0.77x |
| 5 | VVV/USD | 71.912 | 25.578 | -0.23% | 1.28x |
| 6 | HYPE/USD | 69.177 | 62.62 | -0.43% | 3.04x |
| 7 | ETH/USD | 66.950 | 1711.07 | -0.11% | 0.83x |
| 8 | ZEC/USD | 66.838 | 793.78 | -0.48% | 1.81x |
| 9 | TAO/USD | 64.885 | 190.7772 | -0.01% | 1.37x |
| 10 | SUI/USD | 63.534 | 0.6566 | -0.21% | 0.28x |
| 11 | XBT/USD | 63.036 | 60780.4 | -0.25% | 0.82x |
| 12 | INJ/USD | 58.340 | 6.14 | -0.34% | 0.78x |

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

- Persisted scans: 1300; predictions: 10519; observations: 786808.
- Matured sampled outcomes across 1/6/24/48h: 15403; gap abstentions: 22303. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45037667120 · **Generation:** 1300 · **Legacy run:** 45037667120
**Main quote time:** 2026-11-22T15:21:19.366197+00:00 · **Legacy report time:** 2026-11-22T15:22:24.725112+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 62.62 | 82.03 | -0.43% | 3.04x | STRONG 71/100 | HIGH 61/100 | Watch |
| 2 | DRV/USD | 0.37147 | 77.38 | -3.78% | 2.52x | MODERATE 64/100 | VERY_HIGH 71/100 | Do nothing |
| 3 | NIGHT/USD | 0.04812 | 77.35 | -1.17% | 0.90x | WEAK 39/100 | VERY_HIGH 78/100 | Watch |
| 4 | STBL/USD | 0.017075 | 75.46 | +0.56% | 0.77x | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |
| 5 | NEAR/USD | 2.9996 | 73.89 | -0.94% | 0.83x | WEAK 42/100 | HIGH 68/100 | Watch |
| 6 | VVV/USD | 25.578 | 73.52 | -0.23% | 1.28x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 7 | ZEC/USD | 793.78 | 72.53 | -0.48% | 1.81x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 8 | TAO/USD | 190.7772 | 68.52 | -0.01% | 1.37x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 9 | ETH/USD | 1711.07 | 64.74 | -0.11% | 0.83x | WEAK 37/100 | HIGH 68/100 | Watch |
| 10 | XBT/USD | 60780.4 | 60.04 | -0.25% | 0.82x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | SUI/USD | 0.6566 | 55.25 | -0.21% | 0.28x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | INJ/USD | 6.14 | 54.45 | -0.34% | 0.78x | WEAK 32/100 | HIGH 68/100 | Do nothing |

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
