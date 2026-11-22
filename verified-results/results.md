# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T08:52:08.789739+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45004601484
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 72e8bad44134463beeeeb7db1ffdb9b7f46d9b35 (atomic ledger/results publication)
**Ledger generation:** 1260 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 792.06 | 76.227 | 64.210 | +1.78% | -0.60% | 5.33x | 6.6 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.912 | 76.174 | 58.654 | +0.89% | +0.50% | 5.51x | 5.2 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 25.296 | 74.838 | 60.997 | +1.59% | -0.23% | 3.00x | 10.3 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | MODERATE 62/100 | HIGH 67/100 | Watch | WATCH |
| 4 | TAO/USD | 189.2147 | 66.745 | 65.123 | +1.88% | -0.15% | 1.24x | 5.9 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 5 | LINK/USD | 8.62962 | 65.585 | 52.101 | +0.40% | -0.30% | 3.38x | 6.0 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 6 | AVAX/USD | 6.581 | 59.405 | 45.316 | +0.27% | -0.18% | 2.50x | 3.0 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | INJ/USD | 6.054 | 59.319 | 48.674 | +1.36% | -0.26% | 2.20x | 1.7 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ZBCN/USD | 0.001836 | 56.384 | 62.820 | +6.31% | -0.22% | 0.47x | 27.4 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | WEAK 23/100 | EXTREME 93/100 | Do nothing | WATCH |
| 9 | ASTER/USD | 0.50032 | 48.567 | 49.281 | +3.02% | +0.22% | 0.82x | 12.6 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | DASH/USD | 34.947 | 31.212 | 38.510 | +0.94% | -0.15% | 0.34x | 6.3 | 2026-11-22T08:52:02.080234+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 65.123 | 189.2147 | -0.15% | 1.24x |
| 2 | ZEC/USD | 64.210 | 792.06 | -0.60% | 5.33x |
| 3 | ZBCN/USD | 62.820 | 0.001836 | -0.22% | 0.47x |
| 4 | VVV/USD | 60.997 | 25.296 | -0.23% | 3.00x |
| 5 | NEAR/USD | 58.654 | 2.912 | +0.50% | 5.51x |
| 6 | LINK/USD | 52.101 | 8.62962 | -0.30% | 3.38x |
| 7 | ASTER/USD | 49.281 | 0.50032 | +0.22% | 0.82x |
| 8 | INJ/USD | 48.674 | 6.054 | -0.26% | 2.20x |
| 9 | AVAX/USD | 45.316 | 6.581 | -0.18% | 2.50x |
| 10 | DASH/USD | 38.510 | 34.947 | -0.15% | 0.34x |

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

- Persisted scans: 1260; predictions: 10044; observations: 762449.
- Matured sampled outcomes across 1/6/24/48h: 14464; gap abstentions: 22121. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45004601484 · **Generation:** 1260 · **Legacy run:** 45004601484
**Main quote time:** 2026-11-22T08:52:08.789739+00:00 · **Legacy report time:** 2026-11-22T08:52:59.634847+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 792.06 | 76.23 | -0.60% | 5.33x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | NEAR/USD ⭐ | 2.912 | 76.17 | +0.50% | 5.51x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD | 25.296 | 74.84 | -0.23% | 3.00x | MODERATE 62/100 | HIGH 67/100 | Watch |
| 4 | TAO/USD | 189.2147 | 66.75 | -0.15% | 1.24x | WEAK 43/100 | HIGH 68/100 | Watch |
| 5 | LINK/USD | 8.62962 | 65.58 | -0.30% | 3.38x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 6 | AVAX/USD | 6.581 | 59.41 | -0.18% | 2.50x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | INJ/USD | 6.054 | 59.32 | -0.26% | 2.20x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 8 | ZBCN/USD | 0.001836 | 56.38 | -0.22% | 0.47x | WEAK 23/100 | EXTREME 93/100 | Do nothing |
| 9 | ASTER/USD | 0.50032 | 48.57 | +0.22% | 0.82x | MODERATE 49/100 | VERY_HIGH 73/100 | Watch |
| 10 | DASH/USD | 34.947 | 31.21 | -0.15% | 0.34x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.912 | 62.56 | +0.50% | 5.51x | 12275 | STRONG 96/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
