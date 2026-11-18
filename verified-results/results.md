# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:25:03.357163+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44230212218
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** d786ae670b12fdc2d1423633144a0fb7765d66bd (atomic ledger/results publication)
**Ledger generation:** 518 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 512.61 | 70.690 | 52.811 | +0.73% | +0.58% | 7.22x | 14.6 | 2026-11-18T03:24:59.667275+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | CC/USD | 0.08338 | 60.411 | 43.367 | +1.52% | +0.41% | 4.27x | 4.8 | 2026-11-18T03:24:59.667275+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 3 | PIEVERSE/USD | 2.1661 | 59.541 | 60.670 | +5.74% | +0.75% | 0.51x | 22.6 | 2026-11-18T03:24:59.667275+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | ICNT/USD | 0.2829 | 49.849 | 44.249 | +2.46% | -0.35% | 1.74x | 10.6 | 2026-11-18T03:24:59.667275+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.8257 | 32.152 | 30.936 | +0.84% | +1.44% | 0.40x | 20.3 | 2026-11-18T03:24:59.667275+00:00 | Not calibrated | WEAK 36/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | SENT/USD | 0.018762 | 27.615 | 28.202 | +0.50% | +0.01% | 0.94x | 12.3 | 2026-11-18T03:24:59.667275+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.515 | 22.614 | 36.316 | +1.12% | -1.30% | 0.28x | 7.8 | 2026-11-18T03:24:59.667275+00:00 | Not calibrated | WEAK 16/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 60.670 | 2.1661 | +0.75% | 0.51x |
| 2 | XMR/USD | 52.811 | 512.61 | +0.58% | 7.22x |
| 3 | ICNT/USD | 44.249 | 0.2829 | -0.35% | 1.74x |
| 4 | CC/USD | 43.367 | 0.08338 | +0.41% | 4.27x |
| 5 | AKT/USD | 36.316 | 0.515 | -1.30% | 0.28x |
| 6 | PEARL/USD | 30.936 | 1.8257 | +1.44% | 0.40x |
| 7 | SENT/USD | 28.202 | 0.018762 | +0.01% | 0.94x |

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

- Persisted scans: 518; predictions: 4379; observations: 312469.
- Matured sampled outcomes across 1/6/24/48h: 3514; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44230212218 · **Generation:** 518 · **Legacy run:** 44230212218
**Main quote time:** 2026-11-18T03:25:03.357163+00:00 · **Legacy report time:** 2026-11-18T03:25:19.133293+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 512.61 | 70.69 | +0.58% | 7.22x | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 2 | CC/USD ⭐ | 0.08338 | 60.41 | +0.41% | 4.27x | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 3 | PIEVERSE/USD | 2.1661 | 59.54 | +0.75% | 0.51x | MODERATE 50/100 | EXTREME 87/100 | Do nothing |
| 4 | ICNT/USD | 0.2829 | 49.85 | -0.35% | 1.74x | WEAK 40/100 | VERY_HIGH 72/100 | Watch |
| 5 | PEARL/USD | 1.8257 | 32.15 | +1.44% | 0.40x | WEAK 36/100 | EXTREME 87/100 | Do nothing |
| 6 | SENT/USD | 0.018762 | 27.61 | +0.01% | 0.94x | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing |
| 7 | AKT/USD | 0.515 | 22.61 | -1.30% | 0.28x | WEAK 16/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 513.47 | 58.99 | +1.05% | 9.17x | 13020 | STRONG 89/100 | HIGH 61/100 | Consider small entry |
| 2 | CC/USD ⭐ | 0.08338 | 54.51 | +0.06% | 5.11x | 3975 | STRONG 82/100 | HIGH 60/100 | Watch |

**Same-run overlap:** XMR/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
