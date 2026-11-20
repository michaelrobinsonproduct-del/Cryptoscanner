# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T06:30:37.467660+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44688165120
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 17a1c7e704498286e6ae941e1454cecb4c7895a7 (atomic ledger/results publication)
**Ledger generation:** 941 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.9646 | 60.030 | 58.749 | +0.56% | -0.36% | 1.31x | 0.3 | 2026-11-20T06:30:32.502082+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XLM/USD | 0.13335 | 53.591 | 56.481 | +0.49% | +0.06% | 0.68x | 3.9 | 2026-11-20T06:30:32.502082+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ICNT/USD | 0.4379 | 53.261 | 43.684 | +2.77% | +0.50% | 1.71x | 27.4 | 2026-11-20T06:30:32.502082+00:00 | Not calibrated | MODERATE 62/100 | HIGH 67/100 | Watch | WATCH |
| 4 | PROS/USD | 0.5772 | 43.718 | 55.164 | +7.15% | -1.50% | 0.61x | 41.4 | 2026-11-20T06:30:32.502082+00:00 | Not calibrated | WEAK 12/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.09953 | 41.978 | 43.020 | +3.43% | +0.41% | 0.69x | 26.1 | 2026-11-20T06:30:32.502082+00:00 | Not calibrated | WEAK 41/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | AUD/USD | 0.66731 | 31.348 | 40.185 | +0.27% | -0.01% | 0.12x | 1.3 | 2026-11-20T06:30:32.502082+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | SKR/USD | 0.010245 | 24.867 | 31.366 | +1.98% | -0.45% | 0.57x | 27.4 | 2026-11-20T06:30:32.502082+00:00 | Not calibrated | WEAK 7/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 58.749 | 0.9646 | -0.36% | 1.31x |
| 2 | XLM/USD | 56.481 | 0.13335 | +0.06% | 0.68x |
| 3 | PROS/USD | 55.164 | 0.5772 | -1.50% | 0.61x |
| 4 | ICNT/USD | 43.684 | 0.4379 | +0.50% | 1.71x |
| 5 | SYRUP/USD | 43.020 | 0.09953 | +0.41% | 0.69x |
| 6 | AUD/USD | 40.185 | 0.66731 | -0.01% | 0.12x |
| 7 | SKR/USD | 31.366 | 0.010245 | -0.45% | 0.57x |

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

- Persisted scans: 941; predictions: 7988; observations: 568576.
- Matured sampled outcomes across 1/6/24/48h: 9373; gap abstentions: 17213. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44688165120 · **Generation:** 941 · **Legacy run:** 44688165120
**Main quote time:** 2026-11-20T06:30:37.467660+00:00 · **Legacy report time:** 2026-11-20T06:31:43.520015+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.9646 | 60.03 | -0.36% | 1.31x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 2 | XLM/USD | 0.13335 | 53.59 | +0.06% | 0.68x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 3 | ICNT/USD ⭐ | 0.4379 | 53.26 | +0.50% | 1.71x | STRONG 72/100 | HIGH 67/100 | Watch |
| 4 | PROS/USD | 0.5772 | 43.72 | -1.50% | 0.61x | WEAK 12/100 | EXTREME 100/100 | Do nothing |
| 5 | SYRUP/USD | 0.09953 | 41.98 | +0.41% | 0.69x | WEAK 41/100 | EXTREME 87/100 | Do nothing |
| 6 | AUD/USD | 0.66731 | 31.35 | -0.01% | 0.12x | WEAK 21/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | SKR/USD | 0.010245 | 24.87 | -0.45% | 0.57x | WEAK 7/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4394 | 68.61 | +0.50% | 1.71x | 7659 | STRONG 79/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
