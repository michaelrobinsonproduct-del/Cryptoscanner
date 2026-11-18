# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T18:05:09.542030+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44365684848
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** bc917b965073293b90df5b1349701ea079dd20c4 (atomic ledger/results publication)
**Ledger generation:** 631 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUST/USD | 0.04978 | 79.585 | 66.286 | +5.58% | -0.34% | 3.54x | 10.0 | 2026-11-18T18:05:05.674611+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019967 | 75.110 | 71.835 | +6.95% | +0.32% | 1.17x | 8.5 | 2026-11-18T18:05:05.674611+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3817 | 58.271 | 43.664 | +2.25% | -0.08% | 3.37x | 7.9 | 2026-11-18T18:05:05.674611+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 4 | INFI/USD | 0.1294 | 55.419 | 40.483 | +1.89% | +2.29% | 1.35x | 7.7 | 2026-11-18T18:05:05.674611+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04543 | 48.788 | 52.797 | +1.20% | +0.86% | 0.17x | 8.8 | 2026-11-18T18:05:05.674611+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | MEGA/USD | 0.05296 | 25.295 | 39.569 | +2.56% | -1.76% | 0.45x | 18.9 | 2026-11-18T18:05:05.674611+00:00 | Not calibrated | WEAK 13/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 71.835 | 0.019967 | +0.32% | 1.17x |
| 2 | TRUST/USD | 66.286 | 0.04978 | -0.34% | 3.54x |
| 3 | NIGHT/USD | 52.797 | 0.04543 | +0.86% | 0.17x |
| 4 | MNT/USD | 43.664 | 0.3817 | -0.08% | 3.37x |
| 5 | INFI/USD | 40.483 | 0.1294 | +2.29% | 1.35x |
| 6 | MEGA/USD | 39.569 | 0.05296 | -1.76% | 0.45x |

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

- Persisted scans: 631; predictions: 5382; observations: 381286.
- Matured sampled outcomes across 1/6/24/48h: 4682; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44365684848 · **Generation:** 631 · **Legacy run:** 44365684848
**Main quote time:** 2026-11-18T18:05:09.542030+00:00 · **Legacy report time:** 2026-11-18T18:05:33.311192+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD | 0.04978 | 79.58 | -0.34% | 3.54x | MODERATE 65/100 | VERY_HIGH 72/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019967 | 75.11 | +0.32% | 1.17x | STRONG 83/100 | VERY_HIGH 74/100 | Watch |
| 3 | MNT/USD | 0.3817 | 58.27 | -0.08% | 3.37x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 4 | INFI/USD ⭐ | 0.1294 | 55.42 | +2.29% | 1.35x | STRONG 83/100 | HIGH 67/100 | Watch |
| 5 | NIGHT/USD | 0.04543 | 48.79 | +0.86% | 0.17x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 6 | MEGA/USD | 0.05296 | 25.29 | -1.76% | 0.45x | WEAK 13/100 | EXTREME 98/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019967 | 78.26 | +0.32% | 1.17x | 6091 | STRONG 84/100 | VERY_HIGH 74/100 | Watch |
| 2 | INFI/USD ⭐ | 0.1294 | 53.61 | +2.29% | 1.35x | 3799 | STRONG 82/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD, INFI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
