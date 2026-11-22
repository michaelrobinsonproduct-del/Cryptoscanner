# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T11:31:18.420619+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45017576669
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 48bd9c8359ebaba0b617d10ff5414fbbca21014e (atomic ledger/results publication)
**Ledger generation:** 1276 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CRV/USD | 0.18605 | 85.170 | 69.173 | +4.31% | +0.20% | 2.83x | 12.9 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | STRONG 83/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ETH/USD | 1706.38 | 78.894 | 64.999 | +1.43% | -0.14% | 2.46x | 0.1 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NEAR/USD | 2.9892 | 77.752 | 77.612 | +3.57% | -0.58% | 1.31x | 4.7 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.002482 | 71.936 | 79.451 | +5.89% | +0.08% | 0.21x | 8.1 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ZEC/USD | 798.82 | 70.592 | 70.320 | +2.65% | +0.13% | 0.96x | 6.5 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 6 | INJ/USD | 6.248 | 64.728 | 72.006 | +4.60% | +0.21% | 0.17x | 4.8 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6608 | 60.924 | 68.842 | +2.09% | -0.06% | 0.24x | 1.5 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | LINK/USD | 8.81861 | 60.753 | 68.882 | +2.60% | -0.04% | 0.21x | 3.9 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.04598 | 60.361 | 65.992 | +3.84% | -0.41% | 0.64x | 10.9 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | DRV/USD | 0.34124 | 60.334 | 52.285 | +1.80% | +0.27% | 1.67x | 2.3 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 11 | TAO/USD | 190.2381 | 59.468 | 68.936 | +2.43% | -0.35% | 0.23x | 6.1 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XBT/USD | 60885.8 | 59.326 | 64.263 | +1.32% | +0.05% | 0.48x | 0.0 | 2026-11-22T11:31:10.316036+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 79.451 | 0.002482 | +0.08% | 0.21x |
| 2 | NEAR/USD | 77.612 | 2.9892 | -0.58% | 1.31x |
| 3 | INJ/USD | 72.006 | 6.248 | +0.21% | 0.17x |
| 4 | ZEC/USD | 70.320 | 798.82 | +0.13% | 0.96x |
| 5 | CRV/USD | 69.173 | 0.18605 | +0.20% | 2.83x |
| 6 | TAO/USD | 68.936 | 190.2381 | -0.35% | 0.23x |
| 7 | LINK/USD | 68.882 | 8.81861 | -0.04% | 0.21x |
| 8 | SUI/USD | 68.842 | 0.6608 | -0.06% | 0.24x |
| 9 | NIGHT/USD | 65.992 | 0.04598 | -0.41% | 0.64x |
| 10 | ETH/USD | 64.999 | 1706.38 | -0.14% | 2.46x |
| 11 | XBT/USD | 64.263 | 60885.8 | +0.05% | 0.48x |
| 12 | DRV/USD | 52.285 | 0.34124 | +0.27% | 1.67x |

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

- Persisted scans: 1276; predictions: 10232; observations: 772193.
- Matured sampled outcomes across 1/6/24/48h: 14766; gap abstentions: 22211. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45017576669 · **Generation:** 1276 · **Legacy run:** 45017576669
**Main quote time:** 2026-11-22T11:31:18.420619+00:00 · **Legacy report time:** 2026-11-22T11:32:01.168996+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CRV/USD ⭐ | 0.18605 | 85.17 | +0.20% | 2.83x | STRONG 93/100 | HIGH 61/100 | Watch |
| 2 | ETH/USD | 1706.38 | 78.89 | -0.14% | 2.46x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 3 | NEAR/USD | 2.9892 | 77.75 | -0.58% | 1.31x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 4 | PUMP/USD | 0.002482 | 71.94 | +0.08% | 0.21x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 5 | ZEC/USD | 798.82 | 70.59 | +0.13% | 0.96x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 6 | INJ/USD | 6.248 | 64.73 | +0.21% | 0.17x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 7 | SUI/USD | 0.6608 | 60.92 | -0.06% | 0.24x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 8 | LINK/USD | 8.81861 | 60.75 | -0.04% | 0.21x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | NIGHT/USD | 0.04598 | 60.36 | -0.41% | 0.64x | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | DRV/USD | 0.34124 | 60.33 | +0.27% | 1.67x | STRONG 75/100 | HIGH 55/100 | Watch |
| 11 | TAO/USD | 190.2381 | 59.47 | -0.35% | 0.23x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | XBT/USD | 60885.8 | 59.33 | +0.05% | 0.48x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CRV/USD ⭐ | 0.18605 | 87.17 | +0.20% | 2.83x | 6828 | STRONG 94/100 | HIGH 61/100 | Watch |
| 2 | ZBCN/USD | 0.001972 | 87.16 | +2.40% | 4.13x | 4129 | STRONG 84/100 | VERY_HIGH 82/100 | Watch |

**Same-run overlap:** CRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
