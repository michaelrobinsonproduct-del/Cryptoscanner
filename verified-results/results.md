# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T20:52:13.141172+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45263345418
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e138ec8a43da2c62af8d91f1264843f4175b5391 (atomic ledger/results publication)
**Ledger generation:** 1480 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.78 | 101.017 | 92.351 | +9.30% | -0.77% | 2.25x | 15.3 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 2 | SOL/USD | 72.63 | 88.653 | 74.133 | +2.83% | -0.10% | 3.05x | 1.4 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ALGO/USD | 0.08227 | 80.525 | 91.462 | +9.07% | -0.56% | 0.18x | 6.1 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | PAXG/USD | 3621.77 | 70.445 | 60.351 | +1.39% | -0.18% | 2.10x | 1.0 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | UNI/USD | 4.839 | 69.251 | 72.046 | +3.37% | -0.12% | 0.78x | 7.4 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 6 | CC/USD | 0.0775 | 69.159 | 73.052 | +5.77% | -0.10% | 0.66x | 7.7 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | ATOM/USD | 1.2688 | 67.689 | 72.531 | +8.26% | -0.22% | 0.63x | 11.1 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | INJ/USD | 6.442 | 67.472 | 73.349 | +3.44% | -0.55% | 0.69x | 7.8 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | CAP/USD | 0.104468 | 67.254 | 71.544 | +11.64% | -2.62% | 1.88x | 14.9 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | SUI/USD | 0.6716 | 66.803 | 70.485 | +2.42% | -0.18% | 0.72x | 3.0 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XRP/USD | 0.93536 | 66.522 | 60.795 | +0.84% | -0.07% | 1.61x | 0.2 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 12 | LTC/USD | 41.18 | 65.439 | 70.350 | +2.54% | -0.41% | 0.71x | 4.9 | 2026-11-23T20:52:04.640489+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 92.351 | 156.78 | -0.77% | 2.25x |
| 2 | ALGO/USD | 91.462 | 0.08227 | -0.56% | 0.18x |
| 3 | SOL/USD | 74.133 | 72.63 | -0.10% | 3.05x |
| 4 | INJ/USD | 73.349 | 6.442 | -0.55% | 0.69x |
| 5 | CC/USD | 73.052 | 0.0775 | -0.10% | 0.66x |
| 6 | ATOM/USD | 72.531 | 1.2688 | -0.22% | 0.63x |
| 7 | UNI/USD | 72.046 | 4.839 | -0.12% | 0.78x |
| 8 | CAP/USD | 71.544 | 0.104468 | -2.62% | 1.88x |
| 9 | SUI/USD | 70.485 | 0.6716 | -0.18% | 0.72x |
| 10 | LTC/USD | 70.350 | 41.18 | -0.41% | 0.71x |
| 11 | XRP/USD | 60.795 | 0.93536 | -0.07% | 1.61x |
| 12 | PAXG/USD | 60.351 | 3621.77 | -0.18% | 2.10x |

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

- Persisted scans: 1480; predictions: 12527; observations: 896422.
- Matured sampled outcomes across 1/6/24/48h: 22384; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45263345418 · **Generation:** 1480 · **Legacy run:** 45263345418
**Main quote time:** 2026-11-23T20:52:13.141172+00:00 · **Legacy report time:** 2026-11-23T20:53:04.084315+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 156.78 | 101.02 | -0.77% | 2.25x | STRONG 75/100 | HIGH 67/100 | Watch |
| 2 | SOL/USD | 72.63 | 88.65 | -0.10% | 3.05x | STRONG 74/100 | HIGH 61/100 | Watch |
| 3 | ALGO/USD | 0.08227 | 80.53 | -0.56% | 0.18x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 4 | PAXG/USD | 3621.77 | 70.45 | -0.18% | 2.10x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.839 | 69.25 | -0.12% | 0.78x | WEAK 40/100 | HIGH 68/100 | Watch |
| 6 | CC/USD | 0.0775 | 69.16 | -0.10% | 0.66x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 7 | ATOM/USD | 1.2688 | 67.69 | -0.22% | 0.63x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 8 | INJ/USD | 6.442 | 67.47 | -0.55% | 0.69x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 9 | CAP/USD | 0.104468 | 67.25 | -2.62% | 1.88x | MODERATE 49/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | SUI/USD | 0.6716 | 66.80 | -0.18% | 0.72x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 11 | XRP/USD | 0.93536 | 66.52 | -0.07% | 1.61x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 12 | LTC/USD | 41.18 | 65.44 | -0.41% | 0.71x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

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
