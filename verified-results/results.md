# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:35:22.152835+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44459267542
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 1b680e2336931627c996a4766c89d9c35c2660bb (atomic ledger/results publication)
**Ledger generation:** 756 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.4049 | 91.069 | 77.087 | +3.26% | +0.21% | 2.29x | 1.5 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.69 | 83.543 | 81.871 | +4.70% | +1.14% | 0.60x | 6.6 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 67.57 | 72.562 | 61.481 | +1.03% | +0.28% | 1.97x | 1.5 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XBT/USD | 63353 | 67.253 | 59.088 | +0.59% | +0.16% | 1.74x | 0.0 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 5 | TAO/USD | 195.2706 | 64.128 | 63.859 | +1.72% | +0.49% | 0.78x | 6.4 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ZEC/USD | 929.17 | 64.006 | 66.819 | +1.89% | +0.47% | 0.48x | 2.8 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SOL/USD | 74.57 | 63.279 | 64.134 | +1.40% | +0.46% | 0.69x | 1.3 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0591381 | 61.450 | 54.640 | +0.74% | +0.29% | 1.54x | 0.0 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 9 | PYTH/USD | 0.05541 | 60.975 | 61.569 | +5.02% | -0.05% | 0.97x | 10.8 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 10 | ETH/USD | 1795.78 | 55.930 | 63.263 | +1.18% | +0.06% | 0.24x | 0.1 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | SUI/USD | 0.7259 | 55.176 | 61.126 | +0.97% | +0.26% | 0.27x | 1.4 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.97134 | 53.988 | 58.291 | +0.51% | +0.15% | 0.49x | 0.6 | 2026-11-19T04:35:16.460684+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 81.871 | 22.69 | +1.14% | 0.60x |
| 2 | NEAR/USD | 77.087 | 3.4049 | +0.21% | 2.29x |
| 3 | ZEC/USD | 66.819 | 929.17 | +0.47% | 0.48x |
| 4 | SOL/USD | 64.134 | 74.57 | +0.46% | 0.69x |
| 5 | TAO/USD | 63.859 | 195.2706 | +0.49% | 0.78x |
| 6 | ETH/USD | 63.263 | 1795.78 | +0.06% | 0.24x |
| 7 | PYTH/USD | 61.569 | 0.05541 | -0.05% | 0.97x |
| 8 | HYPE/USD | 61.481 | 67.57 | +0.28% | 1.97x |
| 9 | SUI/USD | 61.126 | 0.7259 | +0.26% | 0.27x |
| 10 | XBT/USD | 59.088 | 63353 | +0.16% | 1.74x |
| 11 | XRP/USD | 58.291 | 0.97134 | +0.15% | 0.49x |
| 12 | XDG/USD | 54.640 | 0.0591381 | +0.29% | 1.54x |

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

- Persisted scans: 756; predictions: 6216; observations: 457410.
- Matured sampled outcomes across 1/6/24/48h: 6195; gap abstentions: 13663. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44459267542 · **Generation:** 756 · **Legacy run:** 44459267542
**Main quote time:** 2026-11-19T04:35:22.152835+00:00 · **Legacy report time:** 2026-11-19T04:36:10.203719+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.4049 | 91.07 | +0.21% | 2.29x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 22.69 | 83.54 | +1.14% | 0.60x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD ⭐ | 67.57 | 72.56 | +0.28% | 1.97x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | XBT/USD ⭐ | 63353 | 67.25 | +0.16% | 1.74x | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | TAO/USD | 195.2706 | 64.13 | +0.49% | 0.78x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 6 | ZEC/USD | 929.17 | 64.01 | +0.47% | 0.48x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 7 | SOL/USD | 74.57 | 63.28 | +0.46% | 0.69x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 8 | XDG/USD | 0.0591381 | 61.45 | +0.29% | 1.54x | STRONG 76/100 | HIGH 55/100 | Watch |
| 9 | PYTH/USD | 0.05541 | 60.98 | -0.05% | 0.97x | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing |
| 10 | ETH/USD | 1795.78 | 55.93 | +0.06% | 0.24x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 11 | SUI/USD | 0.7259 | 55.18 | +0.26% | 0.27x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.97134 | 53.99 | +0.15% | 0.49x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.4047 | 94.50 | +0.21% | 2.29x | 14496 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD | 0.023139 | 80.74 | +4.95% | 1.36x | 9586 | STRONG 80/100 | VERY_HIGH 76/100 | Watch |
| 3 | HYPE/USD ⭐ | 67.48 | 64.52 | +0.28% | 1.97x | 14540 | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 4 | XBT/USD ⭐ | 63322.6 | 61.84 | +0.16% | 1.74x | 147698 | STRONG 76/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, HYPE/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
