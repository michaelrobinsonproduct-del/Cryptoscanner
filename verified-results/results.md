# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T16:21:13.891079+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45043188807
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** f72577e1e032cd8b53d3c0be6cb64735735b4964 (atomic ledger/results publication)
**Ledger generation:** 1306 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 2.9965 | 95.029 | 79.723 | +3.82% | +0.15% | 2.46x | 4.0 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.002554 | 83.474 | 82.141 | +8.96% | +0.79% | 0.74x | 7.8 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SUI/USD | 0.6588 | 82.514 | 66.677 | +1.78% | +0.17% | 3.44x | 1.5 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04848 | 81.041 | 86.128 | +9.49% | +0.43% | 0.27x | 12.4 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | DRV/USD | 0.36341 | 80.382 | 88.712 | +8.42% | -0.44% | 0.39x | 0.3 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | INJ/USD | 6.262 | 77.059 | 70.746 | +4.84% | +1.10% | 1.08x | 8.0 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | STRONG 74/100 | HIGH 62/100 | Watch | WATCH |
| 7 | STBL/USD | 0.017226 | 76.049 | 68.581 | +7.64% | +0.27% | 1.61x | 14.5 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.84 | 68.599 | 72.493 | +2.61% | +0.10% | 0.56x | 1.6 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 60938.4 | 63.343 | 64.876 | +1.41% | +0.07% | 0.81x | 0.0 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.691 | 63.339 | 54.355 | +1.95% | +0.25% | 1.77x | 1.5 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 11 | ZEC/USD | 793.72 | 61.568 | 67.539 | +2.00% | +0.26% | 0.27x | 2.9 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ETH/USD | 1715.14 | 61.227 | 68.644 | +1.95% | -0.08% | 0.30x | 0.1 | 2026-11-22T16:21:07.636378+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 88.712 | 0.36341 | -0.44% | 0.39x |
| 2 | NIGHT/USD | 86.128 | 0.04848 | +0.43% | 0.27x |
| 3 | PUMP/USD | 82.141 | 0.002554 | +0.79% | 0.74x |
| 4 | NEAR/USD | 79.723 | 2.9965 | +0.15% | 2.46x |
| 5 | HYPE/USD | 72.493 | 62.84 | +0.10% | 0.56x |
| 6 | INJ/USD | 70.746 | 6.262 | +1.10% | 1.08x |
| 7 | ETH/USD | 68.644 | 1715.14 | -0.08% | 0.30x |
| 8 | STBL/USD | 68.581 | 0.017226 | +0.27% | 1.61x |
| 9 | ZEC/USD | 67.539 | 793.72 | +0.26% | 0.27x |
| 10 | SUI/USD | 66.677 | 0.6588 | +0.17% | 3.44x |
| 11 | XBT/USD | 64.876 | 60938.4 | +0.07% | 0.81x |
| 12 | AVAX/USD | 54.355 | 6.691 | +0.25% | 1.77x |

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

- Persisted scans: 1306; predictions: 10591; observations: 790462.
- Matured sampled outcomes across 1/6/24/48h: 15623; gap abstentions: 22322. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45043188807 · **Generation:** 1306 · **Legacy run:** 45043188807
**Main quote time:** 2026-11-22T16:21:13.891079+00:00 · **Legacy report time:** 2026-11-22T16:22:17.814785+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9965 | 95.03 | +0.15% | 2.46x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | PUMP/USD | 0.002554 | 83.47 | +0.79% | 0.74x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 3 | SUI/USD ⭐ | 0.6588 | 82.51 | +0.17% | 3.44x | STRONG 96/100 | HIGH 55/100 | Watch |
| 4 | NIGHT/USD | 0.04848 | 81.04 | +0.43% | 0.27x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 5 | DRV/USD | 0.36341 | 80.38 | -0.44% | 0.39x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 6 | INJ/USD ⭐ | 6.262 | 77.06 | +1.10% | 1.08x | STRONG 84/100 | HIGH 62/100 | Watch |
| 7 | STBL/USD | 0.017226 | 76.05 | +0.27% | 1.61x | STRONG 78/100 | VERY_HIGH 73/100 | Watch |
| 8 | HYPE/USD | 62.84 | 68.60 | +0.10% | 0.56x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 60938.4 | 63.34 | +0.07% | 0.81x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 10 | AVAX/USD | 6.691 | 63.34 | +0.25% | 1.77x | STRONG 77/100 | HIGH 55/100 | Watch |
| 11 | ZEC/USD | 793.72 | 61.57 | +0.26% | 0.27x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 12 | ETH/USD | 1715.14 | 61.23 | -0.08% | 0.30x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9914 | 90.60 | +0.15% | 2.46x | 12765 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | PIEVERSE/USD | 3.7589 | 85.26 | +4.84% | 1.06x | 6446 | MODERATE 63/100 | EXTREME 94/100 | Do nothing |
| 3 | ZBCN/USD | 0.001907 | 81.48 | +0.37% | 9.37x | 5521 | STRONG 86/100 | VERY_HIGH 72/100 | Watch |
| 4 | INJ/USD ⭐ | 6.249 | 80.11 | +1.10% | 1.08x | 6040 | STRONG 80/100 | HIGH 68/100 | Watch |
| 5 | SUI/USD ⭐ | 0.6588 | 75.75 | +0.17% | 3.44x | 6238 | STRONG 93/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, SUI/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
