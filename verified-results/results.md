# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T01:21:13.624921+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44970917988
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** f03cd689aeef42d06c1cbd8b5b6f685e8067807c (atomic ledger/results publication)
**Ledger generation:** 1213 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BNB/USD | 548.91 | 60.728 | 45.418 | +0.27% | +0.06% | 3.78x | 1.5 | 2026-11-22T01:21:05.700763+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.898 | 58.030 | 56.457 | +0.41% | +0.15% | 1.08x | 2.8 | 2026-11-22T01:21:05.700763+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 3 | VVV/USD | 25.065 | 50.827 | 58.840 | +0.66% | +0.01% | 0.19x | 1.6 | 2026-11-22T01:21:05.700763+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.06063 | 45.069 | 29.408 | +0.31% | +0.13% | 4.49x | 8.3 | 2026-11-22T01:21:05.700763+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ONDO/USD | 0.28252 | 42.670 | 42.781 | +0.32% | +0.06% | 0.96x | 5.7 | 2026-11-22T01:21:05.700763+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 6 | RENDER/USD | 1.309 | 38.588 | 33.109 | +0.38% | +0.15% | 1.47x | 15.3 | 2026-11-22T01:21:05.700763+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 7 | CAP/USD | 0.092885 | 30.988 | 35.543 | +1.01% | +0.15% | 0.47x | 13.9 | 2026-11-22T01:21:05.700763+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 58.840 | 25.065 | +0.01% | 0.19x |
| 2 | NEAR/USD | 56.457 | 2.898 | +0.15% | 1.08x |
| 3 | BNB/USD | 45.418 | 548.91 | +0.06% | 3.78x |
| 4 | ONDO/USD | 42.781 | 0.28252 | +0.06% | 0.96x |
| 5 | CAP/USD | 35.543 | 0.092885 | +0.15% | 0.47x |
| 6 | RENDER/USD | 33.109 | 1.309 | +0.15% | 1.47x |
| 7 | ZAMA/USD | 29.408 | 0.06063 | +0.13% | 4.49x |

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

- Persisted scans: 1213; predictions: 9811; observations: 733862.
- Matured sampled outcomes across 1/6/24/48h: 13409; gap abstentions: 21796. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 19 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44970917988 · **Generation:** 1213 · **Legacy run:** 44970917988
**Main quote time:** 2026-11-22T01:21:13.624921+00:00 · **Legacy report time:** 2026-11-22T01:22:18.843303+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BNB/USD ⭐ | 548.91 | 60.73 | +0.06% | 3.78x | STRONG 85/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD ⭐ | 2.898 | 58.03 | +0.15% | 1.08x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD | 25.065 | 50.83 | +0.01% | 0.19x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 4 | ZAMA/USD | 0.06063 | 45.07 | +0.13% | 4.49x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 5 | ONDO/USD | 0.28252 | 42.67 | +0.06% | 0.96x | WEAK 41/100 | HIGH 62/100 | Watch |
| 6 | RENDER/USD | 1.309 | 38.59 | +0.15% | 1.47x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 7 | CAP/USD | 0.092885 | 30.99 | +0.15% | 0.47x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BNB/USD ⭐ | 548.91 | 53.73 | +0.06% | 3.78x | 7046 | STRONG 82/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD | 492.85 | 51.61 | +0.11% | 1.39x | 11701 | MODERATE 61/100 | HIGH 55/100 | Watch |
| 3 | NEAR/USD ⭐ | 2.8985 | 48.20 | +0.15% | 1.08x | 20503 | MODERATE 59/100 | HIGH 62/100 | Watch |

**Same-run overlap:** BNB/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
