# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T05:15:34.230604+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44463798279
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** c1c7f535131251afb1f955a844b1b9e642d0031f (atomic ledger/results publication)
**Ledger generation:** 764 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 67.54 | 74.544 | 61.168 | +0.99% | -0.32% | 2.63x | 1.5 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 933.72 | 72.462 | 69.836 | +2.39% | -0.23% | 1.38x | 3.7 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 3 | INFI/USD | 0.1193 | 72.186 | 60.634 | +4.83% | +0.17% | 2.07x | 8.4 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | STRONG 81/100 | HIGH 67/100 | Watch | WATCH |
| 4 | ETH/USD | 1795.4 | 70.012 | 63.113 | +1.16% | -0.19% | 1.78x | 0.1 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.4053 | 69.606 | 75.850 | +3.27% | -0.34% | 0.54x | 4.1 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | VVV/USD | 22.394 | 66.799 | 73.728 | +3.34% | +0.24% | 0.19x | 7.6 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ADA/USD | 0.152452 | 66.283 | 58.970 | +0.79% | -0.19% | 1.82x | 3.1 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XBT/USD | 63386.5 | 61.441 | 59.460 | +0.64% | -0.21% | 1.30x | 0.0 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SOL/USD | 74.42 | 54.739 | 62.704 | +1.20% | -0.13% | 0.27x | 1.3 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | TAO/USD | 194.266 | 50.906 | 60.478 | +1.20% | -0.30% | 0.19x | 5.9 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | LINK/USD | 9.1072 | 50.652 | 56.161 | +0.38% | -0.32% | 0.61x | 3.0 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SUI/USD | 0.7233 | 48.848 | 58.592 | +0.61% | -0.11% | 0.08x | 1.4 | 2026-11-19T05:15:26.009024+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 75.850 | 3.4053 | -0.34% | 0.54x |
| 2 | VVV/USD | 73.728 | 22.394 | +0.24% | 0.19x |
| 3 | ZEC/USD | 69.836 | 933.72 | -0.23% | 1.38x |
| 4 | ETH/USD | 63.113 | 1795.4 | -0.19% | 1.78x |
| 5 | SOL/USD | 62.704 | 74.42 | -0.13% | 0.27x |
| 6 | HYPE/USD | 61.168 | 67.54 | -0.32% | 2.63x |
| 7 | INFI/USD | 60.634 | 0.1193 | +0.17% | 2.07x |
| 8 | TAO/USD | 60.478 | 194.266 | -0.30% | 0.19x |
| 9 | XBT/USD | 59.460 | 63386.5 | -0.21% | 1.30x |
| 10 | ADA/USD | 58.970 | 0.152452 | -0.19% | 1.82x |
| 11 | SUI/USD | 58.592 | 0.7233 | -0.11% | 0.08x |
| 12 | LINK/USD | 56.161 | 9.1072 | -0.32% | 0.61x |

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

- Persisted scans: 764; predictions: 6312; observations: 462282.
- Matured sampled outcomes across 1/6/24/48h: 6306; gap abstentions: 13731. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44463798279 · **Generation:** 764 · **Legacy run:** 44463798279
**Main quote time:** 2026-11-19T05:15:34.230604+00:00 · **Legacy report time:** 2026-11-19T05:16:10.565914+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 67.54 | 74.54 | -0.32% | 2.63x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD | 933.72 | 72.46 | -0.23% | 1.38x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 3 | INFI/USD | 0.1193 | 72.19 | +0.17% | 2.07x | STRONG 81/100 | HIGH 67/100 | Watch |
| 4 | ETH/USD | 1795.4 | 70.01 | -0.19% | 1.78x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 5 | NEAR/USD | 3.4053 | 69.61 | -0.34% | 0.54x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 6 | VVV/USD | 22.394 | 66.80 | +0.24% | 0.19x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 7 | ADA/USD | 0.152452 | 66.28 | -0.19% | 1.82x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 8 | XBT/USD | 63386.5 | 61.44 | -0.21% | 1.30x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 9 | SOL/USD | 74.42 | 54.74 | -0.13% | 0.27x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | TAO/USD | 194.266 | 50.91 | -0.30% | 0.19x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | LINK/USD | 9.1072 | 50.65 | -0.32% | 0.61x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SUI/USD | 0.7233 | 48.85 | -0.11% | 0.08x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

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
