# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T17:31:23.247058+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45049731858
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 095397d00090f0703cc6f1bcde4d8e8f035af7b1 (atomic ledger/results publication)
**Ledger generation:** 1314 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.3629 | 103.876 | 85.019 | +8.26% | +1.34% | 2.21x | 7.7 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 794.01 | 83.865 | 68.177 | +2.04% | +0.14% | 3.89x | 2.1 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.0046 | 82.751 | 81.526 | +4.10% | +0.62% | 0.81x | 4.3 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 4 | PEARL/USD | 2.0605 | 82.281 | 72.697 | +5.76% | +1.93% | 0.99x | 19.1 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | MODERATE 66/100 | HIGH 68/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002562 | 82.208 | 82.197 | +9.30% | -0.35% | 1.18x | 7.8 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 6 | HYPE/USD | 62.92 | 79.097 | 73.408 | +2.74% | +0.26% | 1.44x | 1.6 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ETH/USD | 1713.01 | 78.380 | 67.758 | +1.83% | +0.13% | 2.00x | 0.1 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 8 | VVV/USD | 25.446 | 67.343 | 67.406 | +2.19% | +0.03% | 0.98x | 5.9 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XBT/USD | 60772.2 | 63.661 | 62.940 | +1.14% | +0.14% | 1.00x | 0.0 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 10 | AERO/USD | 0.4232 | 62.457 | 65.820 | +6.20% | -0.47% | 0.90x | 18.9 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 11 | BNB/USD | 557.46 | 46.175 | 49.220 | +1.84% | +0.15% | 0.62x | 1.6 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AVAX/USD | 6.673 | 43.934 | 52.609 | +1.68% | -0.09% | 0.18x | 1.5 | 2026-11-22T17:31:13.949839+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 85.019 | 0.3629 | +1.34% | 2.21x |
| 2 | PUMP/USD | 82.197 | 0.002562 | -0.35% | 1.18x |
| 3 | NEAR/USD | 81.526 | 3.0046 | +0.62% | 0.81x |
| 4 | HYPE/USD | 73.408 | 62.92 | +0.26% | 1.44x |
| 5 | PEARL/USD | 72.697 | 2.0605 | +1.93% | 0.99x |
| 6 | ZEC/USD | 68.177 | 794.01 | +0.14% | 3.89x |
| 7 | ETH/USD | 67.758 | 1713.01 | +0.13% | 2.00x |
| 8 | VVV/USD | 67.406 | 25.446 | +0.03% | 0.98x |
| 9 | AERO/USD | 65.820 | 0.4232 | -0.47% | 0.90x |
| 10 | XBT/USD | 62.940 | 60772.2 | +0.14% | 1.00x |
| 11 | AVAX/USD | 52.609 | 6.673 | -0.09% | 0.18x |
| 12 | BNB/USD | 49.220 | 557.46 | +0.15% | 0.62x |

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

- Persisted scans: 1314; predictions: 10687; observations: 795334.
- Matured sampled outcomes across 1/6/24/48h: 15886; gap abstentions: 22330. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45049731858 · **Generation:** 1314 · **Legacy run:** 45049731858
**Main quote time:** 2026-11-22T17:31:23.247058+00:00 · **Legacy report time:** 2026-11-22T17:32:28.899399+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.3629 | 103.88 | +1.34% | 2.21x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 794.01 | 83.87 | +0.14% | 3.89x | STRONG 97/100 | HIGH 55/100 | Watch |
| 3 | NEAR/USD | 3.0046 | 82.75 | +0.62% | 0.81x | STRONG 71/100 | HIGH 62/100 | Watch |
| 4 | PEARL/USD | 2.0605 | 82.28 | +1.93% | 0.99x | MODERATE 66/100 | HIGH 68/100 | Watch |
| 5 | PUMP/USD | 0.002562 | 82.21 | -0.35% | 1.18x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 6 | HYPE/USD ⭐ | 62.92 | 79.10 | +0.26% | 1.44x | STRONG 95/100 | HIGH 55/100 | Watch |
| 7 | ETH/USD ⭐ | 1713.01 | 78.38 | +0.13% | 2.00x | STRONG 84/100 | HIGH 55/100 | Watch |
| 8 | VVV/USD | 25.446 | 67.34 | +0.03% | 0.98x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 9 | XBT/USD | 60772.2 | 63.66 | +0.14% | 1.00x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 10 | AERO/USD | 0.4232 | 62.46 | -0.47% | 0.90x | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing |
| 11 | BNB/USD | 557.46 | 46.17 | +0.15% | 0.62x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 12 | AVAX/USD | 6.673 | 43.93 | -0.09% | 0.18x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.36366 | 92.33 | +1.34% | 2.21x | 18589 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 62.87 | 80.11 | +0.26% | 1.44x | 10350 | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | ETH/USD ⭐ | 1712.1 | 77.53 | +0.13% | 2.00x | 38658 | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | ZEC/USD ⭐ | 794.01 | 75.28 | +0.14% | 3.89x | 20631 | STRONG 93/100 | HIGH 55/100 | Watch |
| 5 | LINK/USD | 8.81503 | 71.40 | +0.24% | 1.37x | 4835 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** DRV/USD, ZEC/USD, HYPE/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
