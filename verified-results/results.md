# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T08:30:44.714247+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44702952251
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 1731e246bf8bc6724c732b12e277a4ef9a0977c0 (atomic ledger/results publication)
**Ledger generation:** 954 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 606; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.456 | 68.978 | 73.001 | +7.02% | +0.26% | 0.47x | 21.9 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | PROS/USD | 0.5764 | 62.983 | 63.665 | +7.00% | -1.03% | 1.45x | 24.4 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | WEAK 41/100 | EXTREME 89/100 | Do nothing | WATCH |
| 3 | XRP/USD | 0.96643 | 61.772 | 59.411 | +0.75% | +0.20% | 1.14x | 1.7 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XLM/USD | 0.134136 | 59.831 | 59.629 | +1.08% | +0.20% | 0.92x | 5.9 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 5 | ENA/USD | 0.1055 | 57.601 | 42.601 | +0.67% | +0.00% | 15.45x | 19.0 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SKR/USD | 0.010451 | 55.786 | 43.734 | +4.03% | -0.59% | 2.58x | 31.6 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 85/100 | Do nothing | WATCH |
| 7 | SYRUP/USD | 0.09945 | 52.372 | 47.490 | +3.35% | -0.16% | 1.57x | 16.1 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | CRV/USD | 0.1934 | 49.159 | 36.960 | +0.66% | +0.24% | 2.10x | 10.9 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ATOM/USD | 1.2726 | 45.420 | 34.476 | +0.88% | +0.60% | 1.79x | 8.6 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | MODERATE 68/100 | HIGH 60/100 | Watch | WATCH |
| 10 | STRK/USD | 0.03205 | 34.844 | 37.496 | +1.14% | +0.41% | 0.53x | 9.4 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | MNT/USD | 0.3959 | 28.608 | 35.874 | +1.10% | -0.35% | 0.45x | 5.1 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | WEAK 19/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | TON/USD | 1.021 | 27.361 | 31.013 | +0.39% | +0.39% | 0.44x | 9.8 | 2026-11-20T08:30:36.701591+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 73.001 | 0.456 | +0.26% | 0.47x |
| 2 | PROS/USD | 63.665 | 0.5764 | -1.03% | 1.45x |
| 3 | XLM/USD | 59.629 | 0.134136 | +0.20% | 0.92x |
| 4 | XRP/USD | 59.411 | 0.96643 | +0.20% | 1.14x |
| 5 | SYRUP/USD | 47.490 | 0.09945 | -0.16% | 1.57x |
| 6 | SKR/USD | 43.734 | 0.010451 | -0.59% | 2.58x |
| 7 | ENA/USD | 42.601 | 0.1055 | +0.00% | 15.45x |
| 8 | STRK/USD | 37.496 | 0.03205 | +0.41% | 0.53x |
| 9 | CRV/USD | 36.960 | 0.1934 | +0.24% | 2.10x |
| 10 | MNT/USD | 35.874 | 0.3959 | -0.35% | 0.45x |
| 11 | ATOM/USD | 34.476 | 1.2726 | +0.60% | 1.79x |
| 12 | TON/USD | 31.013 | 1.021 | +0.39% | 0.44x |

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

- Persisted scans: 954; predictions: 8106; observations: 576443.
- Matured sampled outcomes across 1/6/24/48h: 9614; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44702952251 · **Generation:** 954 · **Legacy run:** 44702952251
**Main quote time:** 2026-11-20T08:30:44.714247+00:00 · **Legacy report time:** 2026-11-20T08:31:36.762118+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.456 | 68.98 | +0.26% | 0.47x | MODERATE 54/100 | VERY_HIGH 82/100 | Watch |
| 2 | PROS/USD | 0.5764 | 62.98 | -1.03% | 1.45x | WEAK 41/100 | EXTREME 89/100 | Do nothing |
| 3 | XRP/USD ⭐ | 0.96643 | 61.77 | +0.20% | 1.14x | STRONG 76/100 | HIGH 62/100 | Watch |
| 4 | XLM/USD | 0.134136 | 59.83 | +0.20% | 0.92x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 5 | ENA/USD | 0.1055 | 57.60 | +0.00% | 15.45x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 6 | SKR/USD | 0.010451 | 55.79 | -0.59% | 2.58x | MODERATE 48/100 | EXTREME 85/100 | Do nothing |
| 7 | SYRUP/USD | 0.09945 | 52.37 | -0.16% | 1.57x | WEAK 41/100 | VERY_HIGH 72/100 | Watch |
| 8 | CRV/USD | 0.1934 | 49.16 | +0.24% | 2.10x | STRONG 75/100 | HIGH 61/100 | Watch |
| 9 | ATOM/USD ⭐ | 1.2726 | 45.42 | +0.60% | 1.79x | STRONG 78/100 | HIGH 60/100 | Consider small entry |
| 10 | STRK/USD | 0.03205 | 34.84 | +0.41% | 0.53x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 11 | MNT/USD | 0.3959 | 28.61 | -0.35% | 0.45x | WEAK 19/100 | EXTREME 88/100 | Do nothing |
| 12 | TON/USD | 1.021 | 27.36 | +0.39% | 0.44x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96655 | 60.62 | +0.20% | 1.14x | 32440 | STRONG 75/100 | HIGH 62/100 | Watch |
| 2 | ATOM/USD ⭐ | 1.272 | 40.96 | +0.60% | 1.79x | 3338 | STRONG 75/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** XRP/USD, ATOM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
