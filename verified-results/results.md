# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:30:14.308146+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44314243341
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 87ec0bb9b71fc2a958b3a2cdb10ada098b79f7e3 (atomic ledger/results publication)
**Ledger generation:** 577 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5225 | 62.294 | 46.816 | +2.59% | +0.10% | 2.91x | 7.7 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | STRONG 76/100 | HIGH 60/100 | Watch | WATCH |
| 2 | VVV/USD | 21.368 | 59.510 | 53.128 | +1.63% | +0.68% | 1.30x | 13.1 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04636 | 55.103 | 63.841 | +3.27% | -0.43% | 0.34x | 15.1 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.019414 | 53.005 | 55.109 | +3.99% | +0.26% | 0.66x | 7.7 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | CC/USD | 0.08334 | 47.043 | 44.047 | +1.47% | +0.06% | 1.27x | 3.6 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | MODERATE 49/100 | HIGH 60/100 | Watch | WATCH |
| 6 | AKE/USD | 0.01012354 | 45.091 | 30.666 | +1.40% | -0.11% | 2.60x | 25.3 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 7 | USELESS/USD | 0.1004 | 44.916 | 53.703 | +2.89% | -0.39% | 0.31x | 16.9 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | TRX/USD | 0.309597 | 43.599 | 44.674 | +0.55% | +0.13% | 0.83x | 1.3 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | WEAK 42/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XPL/USD | 0.0474 | 42.855 | 37.187 | +2.16% | -0.42% | 1.78x | 21.1 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 10 | CAP/USD | 0.101905 | 35.129 | 35.825 | +0.92% | +0.61% | 0.62x | 3.9 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 11 | W/USD | 0.00906 | 32.099 | 36.368 | +1.46% | +0.00% | 0.57x | 11.0 | 2026-11-18T13:30:05.746677+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 63.841 | 0.04636 | -0.43% | 0.34x |
| 2 | SENT/USD | 55.109 | 0.019414 | +0.26% | 0.66x |
| 3 | USELESS/USD | 53.703 | 0.1004 | -0.39% | 0.31x |
| 4 | VVV/USD | 53.128 | 21.368 | +0.68% | 1.30x |
| 5 | AKT/USD | 46.816 | 0.5225 | +0.10% | 2.91x |
| 6 | TRX/USD | 44.674 | 0.309597 | +0.13% | 0.83x |
| 7 | CC/USD | 44.047 | 0.08334 | +0.06% | 1.27x |
| 8 | XPL/USD | 37.187 | 0.0474 | -0.42% | 1.78x |
| 9 | W/USD | 36.368 | 0.00906 | +0.00% | 0.57x |
| 10 | CAP/USD | 35.825 | 0.101905 | +0.61% | 0.62x |
| 11 | AKE/USD | 30.666 | 0.01012354 | -0.11% | 2.60x |

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

- Persisted scans: 577; predictions: 4882; observations: 348400.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13050. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44314243341 · **Generation:** 577 · **Legacy run:** 44314243341
**Main quote time:** 2026-11-18T13:30:14.308146+00:00 · **Legacy report time:** 2026-11-18T13:30:41.075786+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5225 | 62.29 | +0.10% | 2.91x | STRONG 86/100 | HIGH 60/100 | Watch |
| 2 | VVV/USD ⭐ | 21.368 | 59.51 | +0.68% | 1.30x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | NIGHT/USD | 0.04636 | 55.10 | -0.43% | 0.34x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | SENT/USD | 0.019414 | 53.01 | +0.26% | 0.66x | MODERATE 57/100 | VERY_HIGH 82/100 | Watch |
| 5 | CC/USD ⭐ | 0.08334 | 47.04 | +0.06% | 1.27x | MODERATE 59/100 | HIGH 60/100 | Watch |
| 6 | AKE/USD | 0.01012354 | 45.09 | -0.11% | 2.60x | WEAK 43/100 | VERY_HIGH 78/100 | Watch |
| 7 | USELESS/USD | 0.1004 | 44.92 | -0.39% | 0.31x | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | TRX/USD | 0.309597 | 43.60 | +0.13% | 0.83x | WEAK 42/100 | HIGH 62/100 | Watch |
| 9 | XPL/USD | 0.0474 | 42.85 | -0.42% | 1.78x | WEAK 31/100 | VERY_HIGH 78/100 | Do nothing |
| 10 | CAP/USD | 0.101905 | 35.13 | +0.61% | 0.62x | MODERATE 48/100 | VERY_HIGH 82/100 | Watch |
| 11 | W/USD | 0.00906 | 32.10 | +0.00% | 0.57x | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5226 | 73.95 | +0.10% | 2.91x | 4577 | STRONG 92/100 | HIGH 60/100 | Watch |
| 2 | VVV/USD ⭐ | 21.378 | 56.30 | +0.68% | 1.30x | 7012 | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | CC/USD ⭐ | 0.08334 | 44.84 | +0.06% | 1.27x | 4684 | MODERATE 57/100 | HIGH 60/100 | Watch |

**Same-run overlap:** AKT/USD, VVV/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
