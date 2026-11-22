# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T07:01:02.185078+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44996167278
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 884b6f717fb4e84f085566cf5a89be569c0833a1 (atomic ledger/results publication)
**Ledger generation:** 1248 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 781.37 | 47.536 | 56.212 | +0.41% | -0.49% | 0.38x | 3.3 | 2026-11-22T07:00:58.602281+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 2 | ZBCN/USD | 0.001817 | 45.878 | 49.549 | +5.21% | -0.60% | 0.93x | 38.6 | 2026-11-22T07:00:58.602281+00:00 | Not calibrated | WEAK 13/100 | EXTREME 85/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.04445 | 40.672 | 41.467 | +0.38% | -0.20% | 1.02x | 11.3 | 2026-11-22T07:00:58.602281+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 4 | RENDER/USD | 1.324 | 37.443 | 35.914 | +1.53% | +0.15% | 1.08x | 22.7 | 2026-11-22T07:00:58.602281+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 5 | PEARL/USD | 1.9702 | 29.175 | 29.706 | +1.12% | -0.25% | 1.07x | 40.8 | 2026-11-22T07:00:58.602281+00:00 | Not calibrated | WEAK 10/100 | EXTREME 90/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 56.212 | 781.37 | -0.49% | 0.38x |
| 2 | ZBCN/USD | 49.549 | 0.001817 | -0.60% | 0.93x |
| 3 | NIGHT/USD | 41.467 | 0.04445 | -0.20% | 1.02x |
| 4 | RENDER/USD | 35.914 | 1.324 | +0.15% | 1.08x |
| 5 | PEARL/USD | 29.706 | 1.9702 | -0.25% | 1.07x |

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

- Persisted scans: 1248; predictions: 9954; observations: 755142.
- Matured sampled outcomes across 1/6/24/48h: 14268; gap abstentions: 22021. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 55 (sampled only; not a success-rate estimate).
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

**Writer:** 44996167278 · **Generation:** 1248 · **Legacy run:** 44996167278
**Main quote time:** 2026-11-22T07:01:02.185078+00:00 · **Legacy report time:** 2026-11-22T07:01:52.749538+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 781.37 | 47.54 | -0.49% | 0.38x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 2 | ZBCN/USD | 0.001817 | 45.88 | -0.60% | 0.93x | WEAK 13/100 | EXTREME 85/100 | Do nothing |
| 3 | NIGHT/USD | 0.04445 | 40.67 | -0.20% | 1.02x | WEAK 25/100 | VERY_HIGH 74/100 | Do nothing |
| 4 | RENDER/USD ⭐ | 1.324 | 37.44 | +0.15% | 1.08x | WEAK 44/100 | VERY_HIGH 79/100 | Watch |
| 5 | PEARL/USD | 1.9702 | 29.17 | -0.25% | 1.07x | WEAK 10/100 | EXTREME 90/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RENDER/USD ⭐ | 1.324 | 45.09 | +0.15% | 1.08x | 3544 | MODERATE 53/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** RENDER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
