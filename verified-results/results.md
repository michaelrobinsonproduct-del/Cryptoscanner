# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T05:00:25.415768+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44462040012
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** c29b20332001c70863b0f94142c85770725fab40 (atomic ledger/results publication)
**Ledger generation:** 761 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.347 | 82.032 | 72.336 | +3.12% | -1.06% | 3.24x | 6.7 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | STRONG 71/100 | HIGH 65/100 | Watch | WATCH |
| 2 | HYPE/USD | 67.74 | 79.912 | 63.262 | +1.29% | +0.40% | 2.46x | 1.5 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.4172 | 76.522 | 78.526 | +3.63% | +0.72% | 0.44x | 3.8 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ZEC/USD | 934.22 | 70.003 | 69.845 | +2.44% | +0.56% | 0.74x | 4.5 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SOL/USD | 74.46 | 67.777 | 63.086 | +1.25% | -0.17% | 1.56x | 1.3 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XRP/USD | 0.97534 | 67.706 | 61.446 | +0.93% | +0.21% | 1.52x | 0.1 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ADA/USD | 0.152586 | 62.869 | 61.132 | +0.88% | -0.03% | 1.19x | 0.1 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XBT/USD | 63475.1 | 59.011 | 60.445 | +0.78% | +0.10% | 0.81x | 0.0 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 9 | TAO/USD | 195.0576 | 57.897 | 62.402 | +1.61% | -0.28% | 0.69x | 7.8 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | ETH/USD | 1796.95 | 56.877 | 63.724 | +1.25% | -0.00% | 0.32x | 0.1 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | INJ/USD | 7.001 | 55.792 | 41.286 | +0.29% | +0.60% | 2.15x | 4.3 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0591118 | 51.542 | 54.414 | +0.69% | -0.03% | 0.73x | 0.0 | 2026-11-19T05:00:17.593410+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 78.526 | 3.4172 | +0.72% | 0.44x |
| 2 | VVV/USD | 72.336 | 22.347 | -1.06% | 3.24x |
| 3 | ZEC/USD | 69.845 | 934.22 | +0.56% | 0.74x |
| 4 | ETH/USD | 63.724 | 1796.95 | -0.00% | 0.32x |
| 5 | HYPE/USD | 63.262 | 67.74 | +0.40% | 2.46x |
| 6 | SOL/USD | 63.086 | 74.46 | -0.17% | 1.56x |
| 7 | TAO/USD | 62.402 | 195.0576 | -0.28% | 0.69x |
| 8 | XRP/USD | 61.446 | 0.97534 | +0.21% | 1.52x |
| 9 | ADA/USD | 61.132 | 0.152586 | -0.03% | 1.19x |
| 10 | XBT/USD | 60.445 | 63475.1 | +0.10% | 0.81x |
| 11 | XDG/USD | 54.414 | 0.0591118 | -0.03% | 0.73x |
| 12 | INJ/USD | 41.286 | 7.001 | +0.60% | 2.15x |

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

- Persisted scans: 761; predictions: 6276; observations: 460455.
- Matured sampled outcomes across 1/6/24/48h: 6271; gap abstentions: 13707. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44462040012 · **Generation:** 761 · **Legacy run:** 44462040012
**Main quote time:** 2026-11-19T05:00:25.415768+00:00 · **Legacy report time:** 2026-11-19T05:01:06.230221+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.347 | 82.03 | -1.06% | 3.24x | STRONG 71/100 | HIGH 65/100 | Watch |
| 2 | HYPE/USD ⭐ | 67.74 | 79.91 | +0.40% | 2.46x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD | 3.4172 | 76.52 | +0.72% | 0.44x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 4 | ZEC/USD | 934.22 | 70.00 | +0.56% | 0.74x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 5 | SOL/USD | 74.46 | 67.78 | -0.17% | 1.56x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 6 | XRP/USD ⭐ | 0.97534 | 67.71 | +0.21% | 1.52x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 7 | ADA/USD | 0.152586 | 62.87 | -0.03% | 1.19x | WEAK 41/100 | HIGH 68/100 | Watch |
| 8 | XBT/USD | 63475.1 | 59.01 | +0.10% | 0.81x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 9 | TAO/USD | 195.0576 | 57.90 | -0.28% | 0.69x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | ETH/USD | 1796.95 | 56.88 | -0.00% | 0.32x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | INJ/USD | 7.001 | 55.79 | +0.60% | 2.15x | STRONG 83/100 | HIGH 55/100 | Watch |
| 12 | XDG/USD | 0.0591118 | 51.54 | -0.03% | 0.73x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 67.65 | 69.92 | +0.40% | 2.46x | 14644 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.97493 | 64.52 | +0.21% | 1.52x | 36629 | STRONG 87/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** HYPE/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
