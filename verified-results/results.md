# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T19:29:37.703664+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43752672810
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** 7446ff33522ee85ac5f5647abe31378d02e91c61 (atomic ledger/results publication)
**Ledger generation:** 435 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 498.58 | 100.855 | 92.378 | +6.04% | -0.00% | 1.85x | 9.8 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | UNI/USD | 5.1832 | 99.890 | 95.566 | +6.17% | +0.03% | 1.42x | 5.2 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | AAVE/USD | 107.73 | 96.779 | 87.301 | +7.14% | +0.02% | 1.94x | 5.6 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ZEC/USD | 899.81 | 95.505 | 82.344 | +4.16% | -0.37% | 6.70x | 3.6 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 5 | CC/USD | 0.08297 | 94.403 | 86.824 | +6.91% | -1.48% | 9.39x | 6.0 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 77/100 | HIGH 65/100 | Do nothing | WATCH |
| 6 | QNT/USD | 154.88 | 94.232 | 95.162 | +8.07% | +0.27% | 0.77x | 9.7 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ETH/USD | 1824.68 | 92.141 | 77.344 | +3.20% | -0.04% | 3.61x | 0.1 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ASTER/USD | 0.54783 | 91.760 | 83.390 | +9.44% | +0.02% | 1.83x | 6.4 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.1483 | 89.145 | 80.531 | +3.94% | -0.10% | 1.91x | 4.1 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XRP/USD | 0.95674 | 88.535 | 87.596 | +4.70% | +0.04% | 1.07x | 0.6 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XBT/USD | 64954.1 | 79.287 | 64.152 | +1.31% | +0.03% | 3.98x | 0.0 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0588882 | 78.873 | 74.203 | +2.74% | +0.11% | 1.41x | 0.0 | 2026-11-15T19:29:31.556987+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 95.566 | 5.1832 | +0.03% | 1.42x |
| 2 | QNT/USD | 95.162 | 154.88 | +0.27% | 0.77x |
| 3 | XMR/USD | 92.378 | 498.58 | -0.00% | 1.85x |
| 4 | XRP/USD | 87.596 | 0.95674 | +0.04% | 1.07x |
| 5 | AAVE/USD | 87.301 | 107.73 | +0.02% | 1.94x |
| 6 | CC/USD | 86.824 | 0.08297 | -1.48% | 9.39x |
| 7 | ASTER/USD | 83.390 | 0.54783 | +0.02% | 1.83x |
| 8 | ZEC/USD | 82.344 | 899.81 | -0.37% | 6.70x |
| 9 | NEAR/USD | 80.531 | 3.1483 | -0.10% | 1.91x |
| 10 | ETH/USD | 77.344 | 1824.68 | -0.04% | 3.61x |
| 11 | XDG/USD | 74.203 | 0.0588882 | +0.11% | 1.41x |
| 12 | XBT/USD | 64.152 | 64954.1 | +0.03% | 3.98x |

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

- Persisted scans: 435; predictions: 3736; observations: 261960.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11129. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 43752672810 · **Generation:** 435 · **Legacy run:** 43752672810
**Main quote time:** 2026-11-15T19:29:37.703664+00:00 · **Legacy report time:** 2026-11-15T19:29:52.058723+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 498.58 | 100.85 | -0.00% | 1.85x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | UNI/USD | 5.1832 | 99.89 | +0.03% | 1.42x | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | AAVE/USD | 107.73 | 96.78 | +0.02% | 1.94x | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | ZEC/USD | 899.81 | 95.51 | -0.37% | 6.70x | STRONG 78/100 | HIGH 61/100 | Watch |
| 5 | CC/USD | 0.08297 | 94.40 | -1.48% | 9.39x | STRONG 77/100 | HIGH 65/100 | Do nothing |
| 6 | QNT/USD | 154.88 | 94.23 | +0.27% | 0.77x | STRONG 77/100 | HIGH 62/100 | Watch |
| 7 | ETH/USD | 1824.68 | 92.14 | -0.04% | 3.61x | STRONG 76/100 | HIGH 61/100 | Watch |
| 8 | ASTER/USD | 0.54783 | 91.76 | +0.02% | 1.83x | STRONG 81/100 | HIGH 55/100 | Watch |
| 9 | NEAR/USD | 3.1483 | 89.14 | -0.10% | 1.91x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 10 | XRP/USD | 0.95674 | 88.53 | +0.04% | 1.07x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 11 | XBT/USD | 64954.1 | 79.29 | +0.03% | 3.98x | STRONG 85/100 | HIGH 55/100 | Watch |
| 12 | XDG/USD ⭐ | 0.0588882 | 78.87 | +0.11% | 1.41x | STRONG 84/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD | 191.1543 | 92.94 | +0.25% | 1.32x | 14703 | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | XDG/USD ⭐ | 0.0588882 | 86.88 | +0.11% | 1.41x | 21620 | STRONG 88/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
