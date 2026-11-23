# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T03:51:19.923693+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45108224907
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** b1e38c2c7f24eb85dd35f660114d9b98eb561b93 (atomic ledger/results publication)
**Ledger generation:** 1377 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 499.18 | 73.075 | 61.451 | +1.11% | +0.03% | 2.15x | 2.6 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SOL/USD | 71.09 | 70.156 | 58.856 | +0.65% | -0.74% | 5.81x | 1.4 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.0086 | 63.569 | 58.989 | +0.90% | -0.63% | 1.78x | 4.7 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 4 | BLESS/USD | 0.017676 | 62.714 | 64.309 | +9.84% | -1.00% | 1.34x | 39.5 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | ETH/USD | 1726.61 | 62.281 | 55.730 | +0.29% | -0.48% | 1.90x | 2.6 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 6 | UNI/USD | 4.7434 | 59.266 | 48.619 | +1.33% | -0.87% | 5.17x | 5.3 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | LINK/USD | 8.84418 | 56.043 | 44.033 | +0.38% | -0.60% | 2.96x | 3.6 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 8 | CC/USD | 0.07546 | 54.713 | 51.885 | +2.99% | -0.33% | 1.45x | 8.0 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | MODERATE 47/100 | HIGH 66/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.04957 | 50.553 | 49.756 | +0.81% | -0.38% | 1.27x | 12.1 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | WEAK 30/100 | HIGH 67/100 | Do nothing | WATCH |
| 10 | JUP/USD | 0.231 | 45.681 | 46.184 | +2.86% | -0.98% | 1.44x | 15.2 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 11 | PAXG/USD | 3593.15 | 45.645 | 47.587 | +0.59% | -0.08% | 0.85x | 1.9 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | WEAK 28/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | ALGO/USD | 0.07583 | 45.149 | 33.229 | +0.53% | -0.62% | 17.60x | 5.3 | 2026-11-23T03:51:12.078843+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 64.309 | 0.017676 | -1.00% | 1.34x |
| 2 | XMR/USD | 61.451 | 499.18 | +0.03% | 2.15x |
| 3 | NEAR/USD | 58.989 | 3.0086 | -0.63% | 1.78x |
| 4 | SOL/USD | 58.856 | 71.09 | -0.74% | 5.81x |
| 5 | ETH/USD | 55.730 | 1726.61 | -0.48% | 1.90x |
| 6 | CC/USD | 51.885 | 0.07546 | -0.33% | 1.45x |
| 7 | NIGHT/USD | 49.756 | 0.04957 | -0.38% | 1.27x |
| 8 | UNI/USD | 48.619 | 4.7434 | -0.87% | 5.17x |
| 9 | PAXG/USD | 47.587 | 3593.15 | -0.08% | 0.85x |
| 10 | JUP/USD | 46.184 | 0.231 | -0.98% | 1.44x |
| 11 | LINK/USD | 44.033 | 8.84418 | -0.60% | 2.96x |
| 12 | ALGO/USD | 33.229 | 0.07583 | -0.62% | 17.60x |

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

- Persisted scans: 1377; predictions: 11291; observations: 833698.
- Matured sampled outcomes across 1/6/24/48h: 18212; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 92 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45108224907 · **Generation:** 1377 · **Legacy run:** 45108224907
**Main quote time:** 2026-11-23T03:51:19.923693+00:00 · **Legacy report time:** 2026-11-23T03:52:07.538006+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 499.18 | 73.08 | +0.03% | 2.15x | STRONG 82/100 | HIGH 55/100 | Watch |
| 2 | SOL/USD | 71.09 | 70.16 | -0.74% | 5.81x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | NEAR/USD | 3.0086 | 63.57 | -0.63% | 1.78x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 4 | BLESS/USD | 0.017676 | 62.71 | -1.00% | 1.34x | WEAK 36/100 | VERY_HIGH 73/100 | Watch |
| 5 | ETH/USD | 1726.61 | 62.28 | -0.48% | 1.90x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 6 | UNI/USD | 4.7434 | 59.27 | -0.87% | 5.17x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | LINK/USD | 8.84418 | 56.04 | -0.60% | 2.96x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | CC/USD | 0.07546 | 54.71 | -0.33% | 1.45x | MODERATE 47/100 | HIGH 66/100 | Watch |
| 9 | NIGHT/USD | 0.04957 | 50.55 | -0.38% | 1.27x | WEAK 30/100 | HIGH 67/100 | Do nothing |
| 10 | JUP/USD | 0.231 | 45.68 | -0.98% | 1.44x | WEAK 38/100 | VERY_HIGH 72/100 | Watch |
| 11 | PAXG/USD | 3593.15 | 45.65 | -0.08% | 0.85x | WEAK 28/100 | HIGH 68/100 | Do nothing |
| 12 | ALGO/USD | 0.07583 | 45.15 | -0.62% | 17.60x | MODERATE 53/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.096766 | 67.60 | +0.94% | 1.12x | 4732 | MODERATE 64/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
