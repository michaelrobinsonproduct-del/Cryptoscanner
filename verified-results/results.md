# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T18:52:02.398469+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45242460617
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 336dff79da4572590e16dd03405c9f32a7f7296a (atomic ledger/results publication)
**Ledger generation:** 1468 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.9233 | 99.397 | 85.217 | +5.17% | -0.16% | 3.63x | 4.1 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6845 | 96.036 | 85.016 | +4.39% | -0.39% | 2.30x | 1.5 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ALGO/USD | 0.08422 | 95.433 | 89.196 | +11.65% | -0.13% | 1.69x | 3.6 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 4 | INJ/USD | 6.6 | 85.959 | 92.490 | +5.97% | -0.26% | 0.48x | 4.5 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | LTC/USD | 41.85 | 82.216 | 83.262 | +4.21% | -0.29% | 1.04x | 2.4 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ADA/USD | 0.15006 | 81.350 | 80.217 | +3.77% | -0.15% | 1.19x | 2.4 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 7 | HYPE/USD | 65.37 | 78.764 | 78.347 | +3.66% | -0.29% | 1.19x | 4.6 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 73.23 | 76.692 | 80.085 | +3.68% | -0.45% | 0.88x | 1.4 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0571618 | 76.406 | 76.951 | +3.40% | -0.34% | 1.12x | 3.7 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 10 | ICP/USD | 2.088 | 71.018 | 79.555 | +6.21% | -0.05% | 0.17x | 4.8 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XRP/USD | 0.95007 | 69.944 | 71.635 | +2.43% | -0.35% | 1.00x | 0.7 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 12 | CC/USD | 0.07807 | 68.991 | 78.345 | +6.55% | -0.14% | 0.13x | 6.4 | 2026-11-23T18:51:53.363673+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 92.490 | 6.6 | -0.26% | 0.48x |
| 2 | ALGO/USD | 89.196 | 0.08422 | -0.13% | 1.69x |
| 3 | UNI/USD | 85.217 | 4.9233 | -0.16% | 3.63x |
| 4 | SUI/USD | 85.016 | 0.6845 | -0.39% | 2.30x |
| 5 | LTC/USD | 83.262 | 41.85 | -0.29% | 1.04x |
| 6 | ADA/USD | 80.217 | 0.15006 | -0.15% | 1.19x |
| 7 | SOL/USD | 80.085 | 73.23 | -0.45% | 0.88x |
| 8 | ICP/USD | 79.555 | 2.088 | -0.05% | 0.17x |
| 9 | HYPE/USD | 78.347 | 65.37 | -0.29% | 1.19x |
| 10 | CC/USD | 78.345 | 0.07807 | -0.14% | 0.13x |
| 11 | XDG/USD | 76.951 | 0.0571618 | -0.34% | 1.12x |
| 12 | XRP/USD | 71.635 | 0.95007 | -0.35% | 1.00x |

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

- Persisted scans: 1468; predictions: 12383; observations: 889114.
- Matured sampled outcomes across 1/6/24/48h: 21808; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45242460617 · **Generation:** 1468 · **Legacy run:** 45242460617
**Main quote time:** 2026-11-23T18:52:02.398469+00:00 · **Legacy report time:** 2026-11-23T18:52:53.039074+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.9233 | 99.40 | -0.16% | 3.63x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | SUI/USD | 0.6845 | 96.04 | -0.39% | 2.30x | STRONG 78/100 | HIGH 61/100 | Watch |
| 3 | ALGO/USD | 0.08422 | 95.43 | -0.13% | 1.69x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 4 | INJ/USD | 6.6 | 85.96 | -0.26% | 0.48x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 5 | LTC/USD | 41.85 | 82.22 | -0.29% | 1.04x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 6 | ADA/USD | 0.15006 | 81.35 | -0.15% | 1.19x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 7 | HYPE/USD | 65.37 | 78.76 | -0.29% | 1.19x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 73.23 | 76.69 | -0.45% | 0.88x | WEAK 43/100 | HIGH 68/100 | Watch |
| 9 | XDG/USD | 0.0571618 | 76.41 | -0.34% | 1.12x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 10 | ICP/USD | 2.088 | 71.02 | -0.05% | 0.17x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 11 | XRP/USD | 0.95007 | 69.94 | -0.35% | 1.00x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 12 | CC/USD | 0.07807 | 68.99 | -0.14% | 0.13x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
