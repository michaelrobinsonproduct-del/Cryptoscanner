# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T09:41:25.511051+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45008610197
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 7a1ad14d1a3c1018f1752b097620d74a9f1826b7 (atomic ledger/results publication)
**Ledger generation:** 1265 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 190.7194 | 83.512 | 69.898 | +2.69% | -0.28% | 5.23x | 6.9 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 2 | BLESS/USD | 0.013028 | 67.429 | 58.337 | +5.62% | +0.91% | 1.45x | 41.0 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002409 | 66.967 | 55.136 | +2.77% | -0.17% | 2.27x | 12.5 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 4 | ASTER/USD | 0.50531 | 66.815 | 60.216 | +4.05% | +0.31% | 1.50x | 5.3 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |
| 5 | LINK/USD | 8.65417 | 65.252 | 55.250 | +0.69% | +0.03% | 1.98x | 3.0 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ETH/USD | 1690.84 | 63.785 | 58.532 | +0.51% | +0.10% | 1.47x | 0.1 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6516 | 59.540 | 58.883 | +0.66% | -0.28% | 1.20x | 1.5 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ZEC/USD | 793.09 | 58.241 | 66.592 | +1.92% | -0.26% | 0.30x | 3.7 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | VVV/USD | 25.22 | 57.027 | 61.020 | +1.29% | +0.31% | 0.44x | 6.0 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | NEAR/USD | 2.9054 | 46.404 | 57.911 | +0.66% | -0.71% | 0.21x | 3.4 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | AVAX/USD | 6.608 | 37.430 | 47.853 | +0.69% | -0.29% | 0.10x | 3.0 | 2026-11-22T09:41:17.624053+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 69.898 | 190.7194 | -0.28% | 5.23x |
| 2 | ZEC/USD | 66.592 | 793.09 | -0.26% | 0.30x |
| 3 | VVV/USD | 61.020 | 25.22 | +0.31% | 0.44x |
| 4 | ASTER/USD | 60.216 | 0.50531 | +0.31% | 1.50x |
| 5 | SUI/USD | 58.883 | 0.6516 | -0.28% | 1.20x |
| 6 | ETH/USD | 58.532 | 1690.84 | +0.10% | 1.47x |
| 7 | BLESS/USD | 58.337 | 0.013028 | +0.91% | 1.45x |
| 8 | NEAR/USD | 57.911 | 2.9054 | -0.71% | 0.21x |
| 9 | LINK/USD | 55.250 | 8.65417 | +0.03% | 1.98x |
| 10 | PUMP/USD | 55.136 | 0.002409 | -0.17% | 2.27x |
| 11 | AVAX/USD | 47.853 | 6.608 | -0.29% | 0.10x |

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

- Persisted scans: 1265; predictions: 10100; observations: 765494.
- Matured sampled outcomes across 1/6/24/48h: 14531; gap abstentions: 22168. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45008610197 · **Generation:** 1265 · **Legacy run:** 45008610197
**Main quote time:** 2026-11-22T09:41:25.511051+00:00 · **Legacy report time:** 2026-11-22T09:42:19.019240+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD | 190.7194 | 83.51 | -0.28% | 5.23x | STRONG 72/100 | HIGH 61/100 | Watch |
| 2 | BLESS/USD | 0.013028 | 67.43 | +0.91% | 1.45x | MODERATE 64/100 | VERY_HIGH 77/100 | Watch |
| 3 | PUMP/USD | 0.002409 | 66.97 | -0.17% | 2.27x | MODERATE 58/100 | HIGH 67/100 | Watch |
| 4 | ASTER/USD ⭐ | 0.50531 | 66.82 | +0.31% | 1.50x | STRONG 88/100 | HIGH 60/100 | Consider small entry |
| 5 | LINK/USD | 8.65417 | 65.25 | +0.03% | 1.98x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 6 | ETH/USD ⭐ | 1690.84 | 63.79 | +0.10% | 1.47x | STRONG 77/100 | HIGH 55/100 | Watch |
| 7 | SUI/USD | 0.6516 | 59.54 | -0.28% | 1.20x | WEAK 40/100 | HIGH 68/100 | Watch |
| 8 | ZEC/USD | 793.09 | 58.24 | -0.26% | 0.30x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | VVV/USD | 25.22 | 57.03 | +0.31% | 0.44x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 10 | NEAR/USD | 2.9054 | 46.40 | -0.71% | 0.21x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | AVAX/USD | 6.608 | 37.43 | -0.29% | 0.10x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ASTER/USD ⭐ | 0.50555 | 71.99 | +0.31% | 1.50x | 2059 | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1691.29 | 60.51 | +0.10% | 1.47x | 44964 | STRONG 75/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ASTER/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
