# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T22:11:07.320113+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44955266154
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 5ad38b5eddb3c4981cec272d1ecefb9fe73778ba (atomic ledger/results publication)
**Ledger generation:** 1193 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 488.41 | 90.912 | 96.620 | +7.04% | -0.66% | 0.76x | 6.8 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 2 | WINGS/USD | 0.0019 | 90.856 | 76.986 | +8.45% | +3.76% | 0.51x | 5.3 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | STRONG 75/100 | EXTREME 85/100 | Do nothing | WATCH |
| 3 | PEARL/USD | 1.969 | 80.779 | 75.710 | +7.70% | -1.99% | 2.87x | 26.0 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 4 | ETH/USD | 1679.02 | 79.873 | 80.360 | +3.69% | -0.32% | 1.11x | 0.9 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04498 | 79.590 | 87.557 | +6.54% | -0.40% | 0.40x | 11.1 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | TAO/USD | 184.3487 | 78.162 | 66.870 | +2.13% | -0.74% | 10.94x | 6.0 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 7 | UNI/USD | 4.695 | 77.118 | 86.432 | +5.10% | -0.56% | 0.35x | 8.5 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XRP/USD | 0.92501 | 76.644 | 67.502 | +1.79% | -0.39% | 2.11x | 0.1 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ZEC/USD | 782.45 | 75.326 | 75.812 | +3.24% | -1.38% | 1.64x | 3.7 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | MODERATE 58/100 | HIGH 65/100 | Do nothing | WATCH |
| 10 | SOL/USD | 70 | 75.279 | 67.428 | +1.88% | -0.40% | 1.98x | 1.4 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 11 | HYPE/USD | 61.06 | 66.486 | 55.547 | +0.31% | -0.81% | 3.45x | 3.3 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XBT/USD | 60128.4 | 66.365 | 70.728 | +2.25% | -0.34% | 0.73x | 0.0 | 2026-11-21T22:11:01.209960+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 96.620 | 488.41 | -0.66% | 0.76x |
| 2 | NIGHT/USD | 87.557 | 0.04498 | -0.40% | 0.40x |
| 3 | UNI/USD | 86.432 | 4.695 | -0.56% | 0.35x |
| 4 | ETH/USD | 80.360 | 1679.02 | -0.32% | 1.11x |
| 5 | WINGS/USD | 76.986 | 0.0019 | +3.76% | 0.51x |
| 6 | ZEC/USD | 75.812 | 782.45 | -1.38% | 1.64x |
| 7 | PEARL/USD | 75.710 | 1.969 | -1.99% | 2.87x |
| 8 | XBT/USD | 70.728 | 60128.4 | -0.34% | 0.73x |
| 9 | XRP/USD | 67.502 | 0.92501 | -0.39% | 2.11x |
| 10 | SOL/USD | 67.428 | 70 | -0.40% | 1.98x |
| 11 | TAO/USD | 66.870 | 184.3487 | -0.74% | 10.94x |
| 12 | HYPE/USD | 55.547 | 61.06 | -0.81% | 3.45x |

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

- Persisted scans: 1193; predictions: 9625; observations: 721703.
- Matured sampled outcomes across 1/6/24/48h: 12868; gap abstentions: 21514. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44955266154 · **Generation:** 1193 · **Legacy run:** 44955266154
**Main quote time:** 2026-11-21T22:11:07.320113+00:00 · **Legacy report time:** 2026-11-21T22:11:52.270027+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 488.41 | 90.91 | -0.66% | 0.76x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 2 | WINGS/USD | 0.0019 | 90.86 | +3.76% | 0.51x | STRONG 75/100 | EXTREME 85/100 | Do nothing |
| 3 | PEARL/USD | 1.969 | 80.78 | -1.99% | 2.87x | MODERATE 60/100 | VERY_HIGH 77/100 | Do nothing |
| 4 | ETH/USD | 1679.02 | 79.87 | -0.32% | 1.11x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 5 | NIGHT/USD | 0.04498 | 79.59 | -0.40% | 0.40x | WEAK 40/100 | VERY_HIGH 82/100 | Watch |
| 6 | TAO/USD | 184.3487 | 78.16 | -0.74% | 10.94x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 7 | UNI/USD | 4.695 | 77.12 | -0.56% | 0.35x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 8 | XRP/USD | 0.92501 | 76.64 | -0.39% | 2.11x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 9 | ZEC/USD | 782.45 | 75.33 | -1.38% | 1.64x | MODERATE 58/100 | HIGH 65/100 | Do nothing |
| 10 | SOL/USD | 70 | 75.28 | -0.40% | 1.98x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 11 | HYPE/USD | 61.06 | 66.49 | -0.81% | 3.45x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 12 | XBT/USD | 60128.4 | 66.36 | -0.34% | 0.73x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPX/USD | 0.2766 | 72.29 | +0.14% | 1.95x | 2780 | MODERATE 61/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
