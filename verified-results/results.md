# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T19:21:29.028460+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45060103515
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 2031cded701820bc91b853a3350cba3c117de450 (atomic ledger/results publication)
**Ledger generation:** 1325 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.37232 | 86.497 | 78.567 | +11.07% | +0.47% | 1.56x | 21.8 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | STRONG 78/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | WLD/USD | 0.239 | 83.980 | 66.038 | +4.96% | +0.59% | 3.11x | 4.2 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | STRONG 97/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | ETH/USD | 1711.16 | 80.391 | 66.988 | +1.72% | -0.09% | 2.39x | 0.1 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04875 | 80.103 | 88.226 | +10.09% | -0.20% | 0.29x | 8.2 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | VVV/USD | 25.84 | 80.004 | 77.357 | +3.78% | +0.10% | 1.22x | 8.1 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 6 | PUMP/USD | 0.002557 | 77.509 | 81.910 | +9.09% | +0.59% | 0.26x | 7.8 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.0032 | 76.655 | 81.353 | +4.05% | +0.29% | 0.38x | 4.0 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | PYTH/USD | 0.05218 | 76.542 | 71.598 | +6.77% | +1.16% | 0.91x | 9.6 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 9 | LINK/USD | 8.79181 | 70.467 | 58.484 | +2.29% | -0.09% | 2.24x | 2.9 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ZEC/USD | 787.27 | 63.679 | 61.725 | +1.17% | -0.06% | 1.23x | 2.9 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XBT/USD | 60544.1 | 60.819 | 60.200 | +0.76% | -0.07% | 1.10x | 0.2 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 12 | HYPE/USD | 62.36 | 59.975 | 66.198 | +1.83% | +0.03% | 0.36x | 3.2 | 2026-11-22T19:21:19.937921+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 88.226 | 0.04875 | -0.20% | 0.29x |
| 2 | PUMP/USD | 81.910 | 0.002557 | +0.59% | 0.26x |
| 3 | NEAR/USD | 81.353 | 3.0032 | +0.29% | 0.38x |
| 4 | DRV/USD | 78.567 | 0.37232 | +0.47% | 1.56x |
| 5 | VVV/USD | 77.357 | 25.84 | +0.10% | 1.22x |
| 6 | PYTH/USD | 71.598 | 0.05218 | +1.16% | 0.91x |
| 7 | ETH/USD | 66.988 | 1711.16 | -0.09% | 2.39x |
| 8 | HYPE/USD | 66.198 | 62.36 | +0.03% | 0.36x |
| 9 | WLD/USD | 66.038 | 0.239 | +0.59% | 3.11x |
| 10 | ZEC/USD | 61.725 | 787.27 | -0.06% | 1.23x |
| 11 | XBT/USD | 60.200 | 60544.1 | -0.07% | 1.10x |
| 12 | LINK/USD | 58.484 | 8.79181 | -0.09% | 2.24x |

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

- Persisted scans: 1325; predictions: 10819; observations: 802033.
- Matured sampled outcomes across 1/6/24/48h: 16306; gap abstentions: 22342. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45060103515 · **Generation:** 1325 · **Legacy run:** 45060103515
**Main quote time:** 2026-11-22T19:21:29.028460+00:00 · **Legacy report time:** 2026-11-22T19:22:36.854692+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37232 | 86.50 | +0.47% | 1.56x | STRONG 88/100 | HIGH 67/100 | Consider small entry |
| 2 | WLD/USD ⭐ | 0.239 | 83.98 | +0.59% | 3.11x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | ETH/USD | 1711.16 | 80.39 | -0.09% | 2.39x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD | 0.04875 | 80.10 | -0.20% | 0.29x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 5 | VVV/USD ⭐ | 25.84 | 80.00 | +0.10% | 1.22x | STRONG 75/100 | HIGH 62/100 | Watch |
| 6 | PUMP/USD | 0.002557 | 77.51 | +0.59% | 0.26x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 7 | NEAR/USD | 3.0032 | 76.65 | +0.29% | 0.38x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 8 | PYTH/USD | 0.05218 | 76.54 | +1.16% | 0.91x | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |
| 9 | LINK/USD | 8.79181 | 70.47 | -0.09% | 2.24x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 10 | ZEC/USD | 787.27 | 63.68 | -0.06% | 1.23x | WEAK 42/100 | HIGH 68/100 | Watch |
| 11 | XBT/USD | 60544.1 | 60.82 | -0.07% | 1.10x | WEAK 40/100 | HIGH 68/100 | Watch |
| 12 | HYPE/USD | 62.36 | 59.97 | +0.03% | 0.36x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.84 | 89.94 | +0.10% | 1.22x | 12091 | STRONG 80/100 | HIGH 62/100 | Watch |
| 2 | WLD/USD ⭐ | 0.2385 | 86.88 | +0.59% | 3.11x | 2456 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | DRV/USD ⭐ | 0.37232 | 82.30 | +0.47% | 1.56x | 18463 | STRONG 91/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** DRV/USD, WLD/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
