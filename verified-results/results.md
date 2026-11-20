# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T07:20:53.228793+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44694129725
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** e2e9ac0316b67a223bb4656e91178942b9903bc8 (atomic ledger/results publication)
**Ledger generation:** 947 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4556 | 91.917 | 71.817 | +6.92% | +1.02% | 2.73x | 24.2 | 2026-11-20T07:20:47.876588+00:00 | Not calibrated | STRONG 91/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.96596 | 69.427 | 59.845 | +0.70% | -0.10% | 2.01x | 0.1 | 2026-11-20T07:20:47.876588+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XLM/USD | 0.134352 | 60.596 | 62.970 | +1.24% | +0.33% | 0.60x | 1.5 | 2026-11-20T07:20:47.876588+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.09976 | 51.627 | 51.284 | +3.67% | +0.41% | 0.83x | 13.0 | 2026-11-20T07:20:47.876588+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | ATOM/USD | 1.2651 | 45.643 | 30.998 | +0.29% | -0.07% | 9.31x | 7.1 | 2026-11-20T07:20:47.876588+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 6 | HBAR/USD | 0.05407 | 38.086 | 41.673 | +0.58% | +0.11% | 0.59x | 5.6 | 2026-11-20T07:20:47.876588+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | AUD/USD | 0.66758 | 36.274 | 40.954 | +0.31% | +0.00% | 0.53x | 0.4 | 2026-11-20T07:20:47.876588+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SKR/USD | 0.010223 | 33.405 | 30.802 | +1.76% | +0.18% | 1.17x | 25.5 | 2026-11-20T07:20:47.876588+00:00 | Not calibrated | WEAK 32/100 | EXTREME 86/100 | Do nothing | WATCH |
| 9 | BLUR/USD | 0.00678 | 10.813 | 18.667 | +1.35% | +0.00% | 0.21x | 44.2 | 2026-11-20T07:20:47.876588+00:00 | Not calibrated | WEAK 10/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 71.817 | 0.4556 | +1.02% | 2.73x |
| 2 | XLM/USD | 62.970 | 0.134352 | +0.33% | 0.60x |
| 3 | XRP/USD | 59.845 | 0.96596 | -0.10% | 2.01x |
| 4 | SYRUP/USD | 51.284 | 0.09976 | +0.41% | 0.83x |
| 5 | HBAR/USD | 41.673 | 0.05407 | +0.11% | 0.59x |
| 6 | AUD/USD | 40.954 | 0.66758 | +0.00% | 0.53x |
| 7 | ATOM/USD | 30.998 | 1.2651 | -0.07% | 9.31x |
| 8 | SKR/USD | 30.802 | 0.010223 | +0.18% | 1.17x |
| 9 | BLUR/USD | 18.667 | 0.00678 | +0.00% | 0.21x |

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

- Persisted scans: 947; predictions: 8040; observations: 572206.
- Matured sampled outcomes across 1/6/24/48h: 9457; gap abstentions: 17388. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44694129725 · **Generation:** 947 · **Legacy run:** 44694129725
**Main quote time:** 2026-11-20T07:20:53.228793+00:00 · **Legacy report time:** 2026-11-20T07:21:41.211068+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4556 | 91.92 | +1.02% | 2.73x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | XRP/USD | 0.96596 | 69.43 | -0.10% | 2.01x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | XLM/USD | 0.134352 | 60.60 | +0.33% | 0.60x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 4 | SYRUP/USD | 0.09976 | 51.63 | +0.41% | 0.83x | MODERATE 51/100 | VERY_HIGH 73/100 | Watch |
| 5 | ATOM/USD | 1.2651 | 45.64 | -0.07% | 9.31x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 6 | HBAR/USD | 0.05407 | 38.09 | +0.11% | 0.59x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 7 | AUD/USD | 0.66758 | 36.27 | +0.00% | 0.53x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 8 | SKR/USD ⭐ | 0.010223 | 33.41 | +0.18% | 1.17x | WEAK 42/100 | EXTREME 86/100 | Do nothing |
| 9 | BLUR/USD | 0.00678 | 10.81 | +0.00% | 0.21x | WEAK 10/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4563 | 85.33 | +1.02% | 2.73x | 7841 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | SKR/USD ⭐ | 0.010223 | 36.52 | +0.18% | 1.17x | 1613 | MODERATE 48/100 | VERY_HIGH 80/100 | Watch |

**Same-run overlap:** ICNT/USD, SKR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
