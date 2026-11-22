# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T16:44:49.224725+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45045204321
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** f70d221f064671f1149634efdb7956784352dff2 (atomic ledger/results publication)
**Ledger generation:** 1309 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04957 | 107.333 | 85.320 | +11.95% | +1.98% | 2.21x | 16.1 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 6.245 | 82.047 | 68.643 | +4.55% | -0.32% | 4.63x | 8.0 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NEAR/USD | 2.9975 | 79.373 | 80.135 | +3.85% | -0.71% | 1.28x | 3.7 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XBT/USD | 61271.1 | 79.017 | 68.752 | +1.97% | -0.04% | 2.04x | 0.0 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002553 | 71.579 | 79.772 | +8.92% | -0.74% | 0.55x | 11.8 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | DRV/USD | 0.36248 | 71.453 | 78.659 | +8.14% | -0.28% | 0.42x | 19.9 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.93 | 70.591 | 73.523 | +2.76% | -0.17% | 0.79x | 1.6 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ZEC/USD | 793.59 | 69.398 | 66.918 | +1.98% | -0.28% | 1.39x | 3.9 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ETH/USD | 1720.66 | 69.088 | 70.941 | +2.28% | -0.03% | 0.83x | 0.1 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6607 | 64.389 | 68.734 | +2.07% | -0.18% | 0.66x | 1.5 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SOL/USD | 70.59 | 62.621 | 58.481 | +0.60% | +0.01% | 1.41x | 1.4 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 12 | DOT/USD | 0.6661 | 59.843 | 44.843 | +2.01% | +0.00% | 6.62x | 3.0 | 2026-11-22T16:44:42.144417+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 85.320 | 0.04957 | +1.98% | 2.21x |
| 2 | NEAR/USD | 80.135 | 2.9975 | -0.71% | 1.28x |
| 3 | PUMP/USD | 79.772 | 0.002553 | -0.74% | 0.55x |
| 4 | DRV/USD | 78.659 | 0.36248 | -0.28% | 0.42x |
| 5 | HYPE/USD | 73.523 | 62.93 | -0.17% | 0.79x |
| 6 | ETH/USD | 70.941 | 1720.66 | -0.03% | 0.83x |
| 7 | XBT/USD | 68.752 | 61271.1 | -0.04% | 2.04x |
| 8 | SUI/USD | 68.734 | 0.6607 | -0.18% | 0.66x |
| 9 | INJ/USD | 68.643 | 6.245 | -0.32% | 4.63x |
| 10 | ZEC/USD | 66.918 | 793.59 | -0.28% | 1.39x |
| 11 | SOL/USD | 58.481 | 70.59 | +0.01% | 1.41x |
| 12 | DOT/USD | 44.843 | 0.6661 | +0.00% | 6.62x |

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

- Persisted scans: 1309; predictions: 10627; observations: 792289.
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

**Writer:** 45045204321 · **Generation:** 1309 · **Legacy run:** 45045204321
**Main quote time:** 2026-11-22T16:44:49.224725+00:00 · **Legacy report time:** 2026-11-22T16:45:46.458095+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04957 | 107.33 | +1.98% | 2.21x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | INJ/USD | 6.245 | 82.05 | -0.32% | 4.63x | STRONG 71/100 | HIGH 61/100 | Watch |
| 3 | NEAR/USD ⭐ | 2.9975 | 79.37 | -0.71% | 1.28x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 4 | XBT/USD ⭐ | 61271.1 | 79.02 | -0.04% | 2.04x | STRONG 80/100 | HIGH 61/100 | Watch |
| 5 | PUMP/USD | 0.002553 | 71.58 | -0.74% | 0.55x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 6 | DRV/USD | 0.36248 | 71.45 | -0.28% | 0.42x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 7 | HYPE/USD | 62.93 | 70.59 | -0.17% | 0.79x | WEAK 40/100 | HIGH 68/100 | Watch |
| 8 | ZEC/USD | 793.59 | 69.40 | -0.28% | 1.39x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 9 | ETH/USD | 1720.66 | 69.09 | -0.03% | 0.83x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | SUI/USD | 0.6607 | 64.39 | -0.18% | 0.66x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | SOL/USD | 70.59 | 62.62 | +0.01% | 1.41x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 12 | DOT/USD | 0.6661 | 59.84 | +0.00% | 6.62x | STRONG 75/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9984 | 99.81 | +0.24% | 1.29x | 12889 | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | XBT/USD ⭐ | 61226.2 | 79.86 | +0.20% | 2.15x | 132046 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NEAR/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
