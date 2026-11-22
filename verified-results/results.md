# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T07:51:01.203809+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44999976271
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 762d3bcc07d5f3a28d53fdaf9bbda3d4aee9c82d (atomic ledger/results publication)
**Ledger generation:** 1253 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 785.62 | 73.630 | 60.683 | +0.96% | +0.35% | 2.12x | 2.0 | 2026-11-22T07:50:57.511382+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | TAO/USD | 186.4989 | 70.681 | 55.476 | +0.41% | +0.04% | 3.54x | 4.9 | 2026-11-22T07:50:57.511382+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04478 | 62.908 | 51.689 | +1.13% | +0.83% | 1.71x | 2.2 | 2026-11-22T07:50:57.511382+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 4 | VVV/USD | 25.07 | 60.265 | 56.386 | +0.68% | +0.94% | 0.92x | 6.8 | 2026-11-22T07:50:57.511382+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 5 | ZBCN/USD | 0.001837 | 55.507 | 60.552 | +6.37% | +0.55% | 0.22x | 32.7 | 2026-11-22T07:50:57.511382+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | PEARL/USD | 1.9669 | 28.952 | 28.686 | +0.95% | +0.17% | 0.94x | 39.8 | 2026-11-22T07:50:57.511382+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 74/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 60.683 | 785.62 | +0.35% | 2.12x |
| 2 | ZBCN/USD | 60.552 | 0.001837 | +0.55% | 0.22x |
| 3 | VVV/USD | 56.386 | 25.07 | +0.94% | 0.92x |
| 4 | TAO/USD | 55.476 | 186.4989 | +0.04% | 3.54x |
| 5 | NIGHT/USD | 51.689 | 0.04478 | +0.83% | 1.71x |
| 6 | PEARL/USD | 28.686 | 1.9669 | +0.17% | 0.94x |

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

- Persisted scans: 1253; predictions: 9974; observations: 758187.
- Matured sampled outcomes across 1/6/24/48h: 14337; gap abstentions: 22067. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 58 (sampled only; not a success-rate estimate).
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

**Writer:** 44999976271 · **Generation:** 1253 · **Legacy run:** 44999976271
**Main quote time:** 2026-11-22T07:51:01.203809+00:00 · **Legacy report time:** 2026-11-22T07:51:52.606896+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 785.62 | 73.63 | +0.35% | 2.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD | 186.4989 | 70.68 | +0.04% | 3.54x | STRONG 80/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04478 | 62.91 | +0.83% | 1.71x | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD | 25.07 | 60.26 | +0.94% | 0.92x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 5 | ZBCN/USD | 0.001837 | 55.51 | +0.55% | 0.22x | MODERATE 48/100 | EXTREME 87/100 | Do nothing |
| 6 | PEARL/USD | 1.9669 | 28.95 | +0.17% | 0.94x | WEAK 19/100 | VERY_HIGH 74/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.8032 | 87.32 | +2.31% | 3.03x | 2606 | STRONG 84/100 | VERY_HIGH 72/100 | Watch |
| 2 | ZEC/USD ⭐ | 785.94 | 66.20 | +0.35% | 2.12x | 29220 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04472 | 58.70 | +0.83% | 1.71x | 8605 | STRONG 84/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
