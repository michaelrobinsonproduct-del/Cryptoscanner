# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T22:42:09.122196+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45502986413
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 51a6315bbf78f1e24e720188243821d1df40a056 (atomic ledger/results publication)
**Ledger generation:** 1635 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 512 | 106.463 | 87.725 | +5.35% | +0.75% | 3.40x | 9.4 | 2026-11-24T22:42:03.381548+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 24.893 | 80.974 | 64.726 | +1.82% | +0.25% | 2.91x | 6.0 | 2026-11-24T22:42:03.381548+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | GBP/USD | 1.31084 | 73.989 | 58.886 | +0.58% | +0.02% | 5.31x | 0.4 | 2026-11-24T22:42:03.381548+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.498e-06 | 62.496 | 59.524 | +2.22% | +0.55% | 1.02x | 2.9 | 2026-11-24T22:42:03.381548+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04879 | 45.373 | 46.641 | +1.33% | +0.08% | 0.83x | 4.1 | 2026-11-24T22:42:03.381548+00:00 | Not calibrated | WEAK 43/100 | HIGH 62/100 | Watch | WATCH |
| 6 | LUNA/USD | 4.499e-05 | 43.425 | 45.025 | +3.50% | +0.49% | 0.59x | 22.2 | 2026-11-24T22:42:03.381548+00:00 | Not calibrated | WEAK 42/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | ZEUS/USD | 0.00451 | 30.481 | 30.201 | +2.97% | +0.00% | 1.03x | 44.3 | 2026-11-24T22:42:03.381548+00:00 | Not calibrated | WEAK 25/100 | EXTREME 96/100 | Do nothing | WATCH |
| 8 | SKY/USD | 0.04087 | 29.801 | 38.474 | +1.19% | +0.10% | 0.08x | 7.3 | 2026-11-24T22:42:03.381548+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 87.725 | 512 | +0.75% | 3.40x |
| 2 | VVV/USD | 64.726 | 24.893 | +0.25% | 2.91x |
| 3 | PEPE/USD | 59.524 | 3.498e-06 | +0.55% | 1.02x |
| 4 | GBP/USD | 58.886 | 1.31084 | +0.02% | 5.31x |
| 5 | NIGHT/USD | 46.641 | 0.04879 | +0.08% | 0.83x |
| 6 | LUNA/USD | 45.025 | 4.499e-05 | +0.49% | 0.59x |
| 7 | SKY/USD | 38.474 | 0.04087 | +0.10% | 0.08x |
| 8 | ZEUS/USD | 30.201 | 0.00451 | +0.00% | 1.03x |

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

- Persisted scans: 1635; predictions: 14002; observations: 990806.
- Matured sampled outcomes across 1/6/24/48h: 28868; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45502986413 · **Generation:** 1635 · **Legacy run:** 45502986413
**Main quote time:** 2026-11-24T22:42:09.122196+00:00 · **Legacy report time:** 2026-11-24T22:43:17.582158+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 512 | 106.46 | +0.75% | 3.40x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 24.893 | 80.97 | +0.25% | 2.91x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | GBP/USD | 1.31084 | 73.99 | +0.02% | 5.31x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.498e-06 | 62.50 | +0.55% | 1.02x | STRONG 76/100 | HIGH 62/100 | Watch |
| 5 | NIGHT/USD | 0.04879 | 45.37 | +0.08% | 0.83x | WEAK 43/100 | HIGH 62/100 | Watch |
| 6 | LUNA/USD | 4.499e-05 | 43.43 | +0.49% | 0.59x | WEAK 42/100 | EXTREME 94/100 | Do nothing |
| 7 | ZEUS/USD | 0.00451 | 30.48 | +0.00% | 1.03x | WEAK 25/100 | EXTREME 96/100 | Do nothing |
| 8 | SKY/USD | 0.04087 | 29.80 | +0.10% | 0.08x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 512.19 | 95.24 | +0.75% | 3.40x | 7674 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | PEPE/USD ⭐ | 3.498e-06 | 68.90 | +0.55% | 1.02x | 6822 | STRONG 79/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD ⭐ | 24.827 | 66.92 | +0.25% | 2.91x | 17005 | STRONG 98/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, VVV/USD, PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
