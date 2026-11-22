# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T08:31:06.936578+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45003053998
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 5ba33f993f3d8a61414a19ab919c2896a0408cd3 (atomic ledger/results publication)
**Ledger generation:** 1257 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.406 | 82.402 | 62.524 | +2.03% | +0.98% | 3.84x | 13.4 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | STRONG 91/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | ZBCN/USD | 0.00184 | 76.538 | 60.994 | +6.54% | +0.11% | 8.22x | 32.7 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | TAO/USD | 188.8419 | 76.385 | 64.285 | +1.68% | +0.42% | 2.00x | 4.9 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | NEAR/USD | 2.8954 | 73.265 | 54.788 | +0.32% | +0.70% | 18.05x | 4.8 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | LINK/USD | 8.64386 | 71.778 | 54.388 | +0.57% | +0.48% | 5.97x | 3.5 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | ASTER/USD | 0.50011 | 70.165 | 51.914 | +2.98% | +0.65% | 4.31x | 6.8 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Consider small entry | WATCH |
| 7 | INJ/USD | 6.066 | 67.308 | 47.590 | +1.56% | +0.94% | 7.17x | 6.6 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ZEC/USD | 790.68 | 62.269 | 62.393 | +1.61% | +0.31% | 0.83x | 7.7 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 9 | AVAX/USD | 6.58 | 49.954 | 43.362 | +0.26% | +0.77% | 1.28x | 6.1 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | MODERATE 60/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SPX/USD | 0.2802 | 38.740 | 27.035 | +0.29% | +0.82% | 1.76x | 14.3 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 11 | NIGHT/USD | 0.04487 | 37.878 | 49.187 | +1.33% | -0.51% | 0.12x | 8.9 | 2026-11-22T08:30:58.497001+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 64.285 | 188.8419 | +0.42% | 2.00x |
| 2 | VVV/USD | 62.524 | 25.406 | +0.98% | 3.84x |
| 3 | ZEC/USD | 62.393 | 790.68 | +0.31% | 0.83x |
| 4 | ZBCN/USD | 60.994 | 0.00184 | +0.11% | 8.22x |
| 5 | NEAR/USD | 54.788 | 2.8954 | +0.70% | 18.05x |
| 6 | LINK/USD | 54.388 | 8.64386 | +0.48% | 5.97x |
| 7 | ASTER/USD | 51.914 | 0.50011 | +0.65% | 4.31x |
| 8 | NIGHT/USD | 49.187 | 0.04487 | -0.51% | 0.12x |
| 9 | INJ/USD | 47.590 | 6.066 | +0.94% | 7.17x |
| 10 | AVAX/USD | 43.362 | 6.58 | +0.77% | 1.28x |
| 11 | SPX/USD | 27.035 | 0.2802 | +0.82% | 1.76x |

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

- Persisted scans: 1257; predictions: 10012; observations: 760622.
- Matured sampled outcomes across 1/6/24/48h: 14422; gap abstentions: 22102. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45003053998 · **Generation:** 1257 · **Legacy run:** 45003053998
**Main quote time:** 2026-11-22T08:31:06.936578+00:00 · **Legacy report time:** 2026-11-22T08:32:11.450111+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.406 | 82.40 | +0.98% | 3.84x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | ZBCN/USD ⭐ | 0.00184 | 76.54 | +0.11% | 8.22x | STRONG 83/100 | VERY_HIGH 72/100 | Watch |
| 3 | TAO/USD ⭐ | 188.8419 | 76.39 | +0.42% | 2.00x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD ⭐ | 2.8954 | 73.27 | +0.70% | 18.05x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 8.64386 | 71.78 | +0.48% | 5.97x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | ASTER/USD ⭐ | 0.50011 | 70.16 | +0.65% | 4.31x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 7 | INJ/USD ⭐ | 6.066 | 67.31 | +0.94% | 7.17x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 8 | ZEC/USD | 790.68 | 62.27 | +0.31% | 0.83x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 9 | AVAX/USD | 6.58 | 49.95 | +0.77% | 1.28x | MODERATE 60/100 | HIGH 55/100 | Watch |
| 10 | SPX/USD | 0.2802 | 38.74 | +0.82% | 1.76x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 11 | NIGHT/USD | 0.04487 | 37.88 | -0.51% | 0.12x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD ⭐ | 0.00184 | 79.72 | +0.11% | 8.22x | 3197 | STRONG 80/100 | VERY_HIGH 72/100 | Watch |
| 2 | VVV/USD ⭐ | 25.425 | 73.23 | +0.98% | 3.84x | 13979 | STRONG 97/100 | HIGH 61/100 | Consider small entry |
| 3 | TAO/USD ⭐ | 189.5387 | 66.89 | +0.42% | 2.00x | 7183 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 4 | ASTER/USD ⭐ | 0.49804 | 62.76 | +0.65% | 4.31x | 2037 | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 8.64998 | 60.00 | +0.48% | 5.97x | 6121 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 6 | INJ/USD ⭐ | 6.071 | 58.53 | +0.94% | 7.17x | 6097 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 7 | NEAR/USD ⭐ | 2.9046 | 54.69 | +0.70% | 18.05x | 12333 | STRONG 92/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD, ZBCN/USD, TAO/USD, NEAR/USD, LINK/USD, ASTER/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
