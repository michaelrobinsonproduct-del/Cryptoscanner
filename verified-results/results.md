# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T01:51:27.255155+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45924771683
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7e89a2e9995a12a14531b2ef550e32b3b8d657a6 (atomic ledger/results publication)
**Ledger generation:** 1942 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 705.05 | 75.544 | 76.748 | +3.43% | +0.66% | 0.55x | 4.5 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | SOL/USD | 71.33 | 73.849 | 58.147 | +0.55% | +0.14% | 4.20x | 1.4 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ADA/USD | 0.149277 | 69.371 | 54.435 | +0.55% | -0.01% | 7.03x | 4.7 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94679 | 65.322 | 57.788 | +0.43% | +0.14% | 1.68x | 0.4 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.0652 | 60.774 | 57.178 | +0.57% | +0.22% | 1.25x | 3.6 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0566786 | 60.010 | 44.522 | +0.54% | +0.10% | 2.71x | 0.8 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.511e-06 | 59.042 | 44.469 | +0.95% | -0.09% | 26.27x | 2.8 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ETH/USD | 1696.93 | 54.630 | 58.807 | +0.55% | +0.07% | 0.55x | 0.1 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | HYPE/USD | 62.64 | 53.525 | 58.927 | +0.68% | -0.02% | 0.47x | 1.6 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | LTC/USD | 44.13 | 51.221 | 58.954 | +0.89% | -0.05% | 0.25x | 4.5 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ONDO/USD | 0.28857 | 49.298 | 34.229 | +0.37% | +0.01% | 3.46x | 0.7 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 12 | XMR/USD | 461.49 | 49.120 | 57.949 | +0.99% | -0.32% | 0.28x | 8.0 | 2026-11-27T01:51:19.674908+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 76.748 | 705.05 | +0.66% | 0.55x |
| 2 | LTC/USD | 58.954 | 44.13 | -0.05% | 0.25x |
| 3 | HYPE/USD | 58.927 | 62.64 | -0.02% | 0.47x |
| 4 | ETH/USD | 58.807 | 1696.93 | +0.07% | 0.55x |
| 5 | SOL/USD | 58.147 | 71.33 | +0.14% | 4.20x |
| 6 | XMR/USD | 57.949 | 461.49 | -0.32% | 0.28x |
| 7 | XRP/USD | 57.788 | 0.94679 | +0.14% | 1.68x |
| 8 | NEAR/USD | 57.178 | 3.0652 | +0.22% | 1.25x |
| 9 | ADA/USD | 54.435 | 0.149277 | -0.01% | 7.03x |
| 10 | XDG/USD | 44.522 | 0.0566786 | +0.10% | 2.71x |
| 11 | PEPE/USD | 44.469 | 3.511e-06 | -0.09% | 26.27x |
| 12 | ONDO/USD | 34.229 | 0.28857 | +0.01% | 3.46x |

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

- Persisted scans: 1942; predictions: 17006; observations: 1176227.
- Matured sampled outcomes across 1/6/24/48h: 37302; gap abstentions: 25443. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45924771683 · **Generation:** 1942 · **Legacy run:** 45924771683
**Main quote time:** 2026-11-27T01:51:27.255155+00:00 · **Legacy report time:** 2026-11-27T01:52:19.357701+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 705.05 | 75.54 | +0.66% | 0.55x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 2 | SOL/USD ⭐ | 71.33 | 73.85 | +0.14% | 4.20x | STRONG 92/100 | HIGH 55/100 | Watch |
| 3 | ADA/USD | 0.149277 | 69.37 | -0.01% | 7.03x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD ⭐ | 0.94679 | 65.32 | +0.14% | 1.68x | STRONG 78/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD ⭐ | 3.0652 | 60.77 | +0.22% | 1.25x | STRONG 75/100 | HIGH 55/100 | Watch |
| 6 | XDG/USD ⭐ | 0.0566786 | 60.01 | +0.10% | 2.71x | STRONG 85/100 | HIGH 55/100 | Watch |
| 7 | PEPE/USD | 3.511e-06 | 59.04 | -0.09% | 26.27x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 8 | ETH/USD | 1696.93 | 54.63 | +0.07% | 0.55x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 9 | HYPE/USD | 62.64 | 53.53 | -0.02% | 0.47x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | LTC/USD | 44.13 | 51.22 | -0.05% | 0.25x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ONDO/USD | 0.28857 | 49.30 | +0.01% | 3.46x | STRONG 70/100 | HIGH 60/100 | Watch |
| 12 | XMR/USD | 461.49 | 49.12 | -0.32% | 0.28x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 71.31 | 63.87 | +0.14% | 4.20x | 32845 | STRONG 87/100 | HIGH 55/100 | Watch |
| 2 | XRP/USD ⭐ | 0.94582 | 58.85 | +0.14% | 1.68x | 20876 | STRONG 74/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0566786 | 57.24 | +0.10% | 2.71x | 5041 | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD ⭐ | 3.0609 | 52.24 | +0.22% | 1.25x | 13192 | STRONG 71/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SOL/USD, XRP/USD, NEAR/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
