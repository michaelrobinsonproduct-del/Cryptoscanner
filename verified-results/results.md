# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:00:27.673070+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44433409788
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** df42328690f7fbb4a2d425189eeb496b55c3e7c5 (atomic ledger/results publication)
**Ledger generation:** 713 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PAXG/USD | 3745.65 | 59.449 | 44.532 | +0.39% | -0.02% | 2.74x | 1.1 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XBT/USD | 63154.7 | 58.980 | 56.884 | +0.27% | +0.03% | 1.20x | 0.0 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 3 | TRX/USD | 0.310691 | 57.339 | 41.986 | +0.46% | +0.07% | 4.55x | 0.0 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1784.06 | 57.167 | 58.640 | +0.52% | +0.06% | 0.82x | 0.1 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 5 | TAO/USD | 193.1847 | 55.721 | 56.627 | +0.64% | +0.26% | 0.78x | 5.7 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SUI/USD | 0.7211 | 54.856 | 56.449 | +0.31% | +0.01% | 0.83x | 1.4 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 7 | HYPE/USD | 67.14 | 54.640 | 56.232 | +0.39% | +0.06% | 0.81x | 3.0 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ADA/USD | 0.151708 | 53.871 | 55.487 | +0.30% | +0.04% | 0.82x | 3.2 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ZEC/USD | 916.24 | 52.246 | 57.584 | +0.47% | -0.12% | 0.53x | 1.4 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | XDG/USD | 0.0589278 | 50.256 | 51.020 | +0.38% | -0.06% | 0.95x | 1.6 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | NEAR/USD | 3.3219 | 48.253 | 57.645 | +0.74% | -0.19% | 0.15x | 5.1 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | LTC/USD | 44.27 | 46.460 | 49.361 | +0.59% | +0.09% | 0.66x | 2.3 | 2026-11-19T01:00:19.284947+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ETH/USD | 58.640 | 1784.06 | +0.06% | 0.82x |
| 2 | NEAR/USD | 57.645 | 3.3219 | -0.19% | 0.15x |
| 3 | ZEC/USD | 57.584 | 916.24 | -0.12% | 0.53x |
| 4 | XBT/USD | 56.884 | 63154.7 | +0.03% | 1.20x |
| 5 | TAO/USD | 56.627 | 193.1847 | +0.26% | 0.78x |
| 6 | SUI/USD | 56.449 | 0.7211 | +0.01% | 0.83x |
| 7 | HYPE/USD | 56.232 | 67.14 | +0.06% | 0.81x |
| 8 | ADA/USD | 55.487 | 0.151708 | +0.04% | 0.82x |
| 9 | XDG/USD | 51.020 | 0.0589278 | -0.06% | 0.95x |
| 10 | LTC/USD | 49.361 | 44.27 | +0.09% | 0.66x |
| 11 | PAXG/USD | 44.532 | 3745.65 | -0.02% | 2.74x |
| 12 | TRX/USD | 41.986 | 0.310691 | +0.07% | 4.55x |

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

- Persisted scans: 713; predictions: 5781; observations: 431224.
- Matured sampled outcomes across 1/6/24/48h: 5665; gap abstentions: 13425. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44433409788 · **Generation:** 713 · **Legacy run:** 44433409788
**Main quote time:** 2026-11-19T01:00:27.673070+00:00 · **Legacy report time:** 2026-11-19T01:01:00.094543+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD | 3745.65 | 59.45 | -0.02% | 2.74x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 2 | XBT/USD | 63154.7 | 58.98 | +0.03% | 1.20x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 3 | TRX/USD | 0.310691 | 57.34 | +0.07% | 4.55x | STRONG 74/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1784.06 | 57.17 | +0.06% | 0.82x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 5 | TAO/USD | 193.1847 | 55.72 | +0.26% | 0.78x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 6 | SUI/USD | 0.7211 | 54.86 | +0.01% | 0.83x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 7 | HYPE/USD | 67.14 | 54.64 | +0.06% | 0.81x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 8 | ADA/USD | 0.151708 | 53.87 | +0.04% | 0.82x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 9 | ZEC/USD | 916.24 | 52.25 | -0.12% | 0.53x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | XDG/USD | 0.0589278 | 50.26 | -0.06% | 0.95x | WEAK 30/100 | HIGH 68/100 | Do nothing |
| 11 | NEAR/USD | 3.3219 | 48.25 | -0.19% | 0.15x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | LTC/USD | 44.27 | 46.46 | +0.09% | 0.66x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD | 0.05114 | 69.36 | +0.93% | 1.21x | 2094 | MODERATE 60/100 | EXTREME 86/100 | Do nothing |
| 2 | LUNA/USD | 4.476e-05 | 69.26 | +1.61% | 1.89x | 1858 | STRONG 80/100 | HIGH 60/100 | Watch |
| 3 | PROS/USD | 0.6889 | 62.89 | +1.41% | 2.04x | 2322 | STRONG 76/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
