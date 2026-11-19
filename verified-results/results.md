# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T00:05:13.122879+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44426030219
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** eb83a713863aa46181511c2b26501f963bf51af2 (atomic ledger/results publication)
**Ledger generation:** 702 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 7.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.404 | 50.910 | 34.840 | +0.29% | +0.21% | 3.50x | 14.3 | 2026-11-19T00:05:10.989809+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04557 | 42.884 | 42.988 | +0.33% | +0.44% | 0.77x | 6.6 | 2026-11-19T00:05:10.989809+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 3 | STX/USD | 0.2718 | 31.288 | 25.630 | +0.26% | -0.29% | 1.71x | 14.7 | 2026-11-19T00:05:10.989809+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 4 | ICP/USD | 2.186 | 21.302 | 32.543 | +0.37% | -0.77% | 0.26x | 13.8 | 2026-11-19T00:05:10.989809+00:00 | Not calibrated | WEAK 11/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 42.988 | 0.04557 | +0.44% | 0.77x |
| 2 | ZRO/USD | 34.840 | 1.404 | +0.21% | 3.50x |
| 3 | ICP/USD | 32.543 | 2.186 | -0.77% | 0.26x |
| 4 | STX/USD | 25.630 | 0.2718 | -0.29% | 1.71x |

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

- Persisted scans: 702; predictions: 5667; observations: 424525.
- Matured sampled outcomes across 1/6/24/48h: 5533; gap abstentions: 13326. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44426030219 · **Generation:** 702 · **Legacy run:** 44426030219
**Main quote time:** 2026-11-19T00:05:13.122879+00:00 · **Legacy report time:** 2026-11-19T00:05:41.029141+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.404 | 50.91 | +0.21% | 3.50x | STRONG 85/100 | HIGH 61/100 | Consider small entry |
| 2 | NIGHT/USD | 0.04557 | 42.88 | +0.44% | 0.77x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 3 | STX/USD | 0.2718 | 31.29 | -0.29% | 1.71x | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing |
| 4 | ICP/USD | 2.186 | 21.30 | -0.77% | 0.26x | WEAK 11/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.404 | 40.06 | +0.21% | 3.50x | 2730 | STRONG 80/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** ZRO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
