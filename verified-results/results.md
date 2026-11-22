# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T18:51:23.584492+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45057258202
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 282a1568de1dfe43a4b7f05f7d04743050a3d79c (atomic ledger/results publication)
**Ledger generation:** 1322 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 2.9893 | 93.260 | 79.311 | +3.57% | -0.21% | 3.33x | 1.3 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.049 | 89.044 | 87.675 | +10.66% | -0.89% | 1.58x | 10.2 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | MODERATE 60/100 | HIGH 67/100 | Watch | WATCH |
| 3 | DRV/USD | 0.37005 | 84.275 | 79.537 | +10.40% | +0.66% | 1.14x | 19.2 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | STRONG 72/100 | HIGH 68/100 | Watch | WATCH |
| 4 | VVV/USD | 26.034 | 79.489 | 84.767 | +4.55% | +0.21% | 0.37x | 4.2 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002547 | 77.829 | 82.036 | +8.66% | +0.31% | 0.42x | 7.9 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6567 | 76.337 | 64.404 | +1.45% | +0.21% | 2.09x | 1.5 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | HYPE/USD | 62.51 | 69.693 | 68.717 | +2.07% | +0.11% | 1.04x | 1.6 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 8 | LINK/USD | 8.80366 | 68.863 | 59.635 | +2.43% | +0.16% | 1.85x | 2.7 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ETH/USD | 1712.95 | 67.890 | 67.733 | +1.82% | +0.08% | 0.98x | 0.1 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.672 | 67.814 | 51.988 | +1.66% | +0.17% | 2.69x | 3.0 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 11 | LTC/USD | 39.88 | 59.562 | 44.437 | +0.38% | +0.03% | 4.69x | 2.5 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XBT/USD | 60630 | 59.444 | 61.283 | +0.90% | +0.04% | 0.80x | 0.0 | 2026-11-22T18:51:15.876210+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 87.675 | 0.049 | -0.89% | 1.58x |
| 2 | VVV/USD | 84.767 | 26.034 | +0.21% | 0.37x |
| 3 | PUMP/USD | 82.036 | 0.002547 | +0.31% | 0.42x |
| 4 | DRV/USD | 79.537 | 0.37005 | +0.66% | 1.14x |
| 5 | NEAR/USD | 79.311 | 2.9893 | -0.21% | 3.33x |
| 6 | HYPE/USD | 68.717 | 62.51 | +0.11% | 1.04x |
| 7 | ETH/USD | 67.733 | 1712.95 | +0.08% | 0.98x |
| 8 | SUI/USD | 64.404 | 0.6567 | +0.21% | 2.09x |
| 9 | XBT/USD | 61.283 | 60630 | +0.04% | 0.80x |
| 10 | LINK/USD | 59.635 | 8.80366 | +0.16% | 1.85x |
| 11 | AVAX/USD | 51.988 | 6.672 | +0.17% | 2.69x |
| 12 | LTC/USD | 44.437 | 39.88 | +0.03% | 4.69x |

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

- Persisted scans: 1322; predictions: 10783; observations: 800206.
- Matured sampled outcomes across 1/6/24/48h: 16198; gap abstentions: 22342. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45057258202 · **Generation:** 1322 · **Legacy run:** 45057258202
**Main quote time:** 2026-11-22T18:51:23.584492+00:00 · **Legacy report time:** 2026-11-22T18:52:29.609871+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 2.9893 | 93.26 | -0.21% | 3.33x | STRONG 77/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD | 0.049 | 89.04 | -0.89% | 1.58x | MODERATE 60/100 | HIGH 67/100 | Watch |
| 3 | DRV/USD ⭐ | 0.37005 | 84.28 | +0.66% | 1.14x | STRONG 82/100 | HIGH 68/100 | Watch |
| 4 | VVV/USD | 26.034 | 79.49 | +0.21% | 0.37x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 5 | PUMP/USD | 0.002547 | 77.83 | +0.31% | 0.42x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 6 | SUI/USD ⭐ | 0.6567 | 76.34 | +0.21% | 2.09x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | HYPE/USD ⭐ | 62.51 | 69.69 | +0.11% | 1.04x | STRONG 70/100 | HIGH 62/100 | Watch |
| 8 | LINK/USD ⭐ | 8.80366 | 68.86 | +0.16% | 1.85x | STRONG 79/100 | HIGH 55/100 | Watch |
| 9 | ETH/USD | 1712.95 | 67.89 | +0.08% | 0.98x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 10 | AVAX/USD | 6.672 | 67.81 | +0.17% | 2.69x | STRONG 79/100 | HIGH 55/100 | Watch |
| 11 | LTC/USD | 39.88 | 59.56 | +0.03% | 4.69x | STRONG 75/100 | HIGH 55/100 | Watch |
| 12 | XBT/USD | 60630 | 59.44 | +0.04% | 0.80x | MODERATE 50/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37005 | 81.04 | +0.66% | 1.14x | 18563 | STRONG 86/100 | HIGH 62/100 | Watch |
| 2 | WLD/USD | 0.2373 | 78.97 | +0.47% | 4.77x | 2365 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 62.55 | 71.78 | +0.11% | 1.04x | 10242 | STRONG 71/100 | HIGH 62/100 | Watch |
| 4 | LINK/USD ⭐ | 8.81279 | 71.35 | +0.16% | 1.85x | 4668 | STRONG 81/100 | HIGH 55/100 | Watch |
| 5 | SUI/USD ⭐ | 0.6572 | 69.25 | +0.21% | 2.09x | 6034 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** DRV/USD, SUI/USD, HYPE/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
