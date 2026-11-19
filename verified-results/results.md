# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T00:10:19.880725+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44426720525
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 951c7bea1951abd4314257ad3d2adfd7a272caf3 (atomic ledger/results publication)
**Ledger generation:** 703 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.404 | 47.706 | 34.833 | +0.29% | -0.43% | 2.71x | 14.3 | 2026-11-19T00:10:15.362445+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |
| 2 | INJ/USD | 7.002 | 40.583 | 41.094 | +0.30% | -0.14% | 1.02x | 4.3 | 2026-11-19T00:10:15.362445+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.04558 | 38.132 | 40.945 | +0.35% | +0.00% | 0.72x | 11.0 | 2026-11-19T00:10:15.362445+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | CAP/USD | 0.096546 | 37.183 | 29.174 | +0.55% | +0.57% | 1.52x | 12.3 | 2026-11-19T00:10:15.362445+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | STX/USD | 0.2721 | 31.349 | 30.077 | +0.37% | -0.29% | 1.27x | 7.4 | 2026-11-19T00:10:15.362445+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 6 | ICP/USD | 2.186 | 26.191 | 34.832 | +0.37% | -0.23% | 0.25x | 9.2 | 2026-11-19T00:10:15.362445+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | USELESS/USD | 0.09614 | 25.941 | 34.322 | +0.61% | -0.01% | 0.17x | 16.7 | 2026-11-19T00:10:15.362445+00:00 | Not calibrated | WEAK 13/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | ZBCN/USD | 0.001697 | 6.118 | 15.786 | +0.35% | -0.29% | 0.18x | 35.4 | 2026-11-19T00:10:15.362445+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 41.094 | 7.002 | -0.14% | 1.02x |
| 2 | NIGHT/USD | 40.945 | 0.04558 | +0.00% | 0.72x |
| 3 | ZRO/USD | 34.833 | 1.404 | -0.43% | 2.71x |
| 4 | ICP/USD | 34.832 | 2.186 | -0.23% | 0.25x |
| 5 | USELESS/USD | 34.322 | 0.09614 | -0.01% | 0.17x |
| 6 | STX/USD | 30.077 | 0.2721 | -0.29% | 1.27x |
| 7 | CAP/USD | 29.174 | 0.096546 | +0.57% | 1.52x |
| 8 | ZBCN/USD | 15.786 | 0.001697 | -0.29% | 0.18x |

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

- Persisted scans: 703; predictions: 5675; observations: 425134.
- Matured sampled outcomes across 1/6/24/48h: 5556; gap abstentions: 13338. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44426720525 · **Generation:** 703 · **Legacy run:** 44426720525
**Main quote time:** 2026-11-19T00:10:19.880725+00:00 · **Legacy report time:** 2026-11-19T00:11:02.386258+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD | 1.404 | 47.71 | -0.43% | 2.71x | MODERATE 49/100 | HIGH 67/100 | Watch |
| 2 | INJ/USD | 7.002 | 40.58 | -0.14% | 1.02x | WEAK 30/100 | HIGH 68/100 | Do nothing |
| 3 | NIGHT/USD | 0.04558 | 38.13 | +0.00% | 0.72x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | CAP/USD ⭐ | 0.096546 | 37.18 | +0.57% | 1.52x | MODERATE 69/100 | VERY_HIGH 73/100 | Watch |
| 5 | STX/USD | 0.2721 | 31.35 | -0.29% | 1.27x | WEAK 26/100 | VERY_HIGH 73/100 | Do nothing |
| 6 | ICP/USD | 2.186 | 26.19 | -0.23% | 0.25x | WEAK 18/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | USELESS/USD | 0.09614 | 25.94 | -0.01% | 0.17x | WEAK 13/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | ZBCN/USD | 0.001697 | 6.12 | -0.29% | 0.18x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD ⭐ | 0.096566 | 33.53 | +0.57% | 1.52x | 2713 | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
