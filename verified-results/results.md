# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T03:50:33.307278+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44670309279
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 95c7c189bc0f93c4b8e24d99853bdaf979c566b3 (atomic ledger/results publication)
**Ledger generation:** 918 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04564 | 61.198 | 50.373 | +1.97% | +1.24% | 1.46x | 8.8 | 2026-11-20T03:50:29.513897+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XRP/USD | 0.96427 | 60.822 | 58.611 | +0.52% | +0.91% | 0.77x | 0.1 | 2026-11-20T03:50:29.513897+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 3 | XBT/USD | 62172.5 | 53.255 | 57.920 | +0.42% | +0.40% | 0.33x | 0.0 | 2026-11-20T03:50:29.513897+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | CT/USD | 0.1306 | 52.013 | 31.986 | +1.63% | +1.01% | 4.16x | 22.9 | 2026-11-20T03:50:29.513897+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | SAPIEN/USD | 0.0408 | 36.409 | 35.818 | +1.59% | +0.84% | 0.64x | 12.2 | 2026-11-20T03:50:29.513897+00:00 | Not calibrated | WEAK 43/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 58.611 | 0.96427 | +0.91% | 0.77x |
| 2 | XBT/USD | 57.920 | 62172.5 | +0.40% | 0.33x |
| 3 | NIGHT/USD | 50.373 | 0.04564 | +1.24% | 1.46x |
| 4 | SAPIEN/USD | 35.818 | 0.0408 | +0.84% | 0.64x |
| 5 | CT/USD | 31.986 | 0.1306 | +1.01% | 4.16x |

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

- Persisted scans: 918; predictions: 7921; observations: 554679.
- Matured sampled outcomes across 1/6/24/48h: 9061; gap abstentions: 16611. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44670309279 · **Generation:** 918 · **Legacy run:** 44670309279
**Main quote time:** 2026-11-20T03:50:33.307278+00:00 · **Legacy report time:** 2026-11-20T03:51:27.356655+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04564 | 61.20 | +1.24% | 1.46x | STRONG 86/100 | HIGH 55/100 | Watch |
| 2 | XRP/USD | 0.96427 | 60.82 | +0.91% | 0.77x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 3 | XBT/USD | 62172.5 | 53.26 | +0.40% | 0.33x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 4 | CT/USD ⭐ | 0.1306 | 52.01 | +1.01% | 4.16x | STRONG 81/100 | VERY_HIGH 72/100 | Watch |
| 5 | SAPIEN/USD | 0.0408 | 36.41 | +0.84% | 0.64x | WEAK 43/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04561 | 63.19 | +1.24% | 1.46x | 8448 | STRONG 87/100 | HIGH 55/100 | Watch |
| 2 | CT/USD ⭐ | 0.1312 | 58.59 | +1.01% | 4.16x | 2537 | STRONG 84/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** NIGHT/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
