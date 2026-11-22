# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T10:41:06.917320+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45013509664
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 5ad361a34b8bc456b4e0d2a4554d2d78cf1d968d (atomic ledger/results publication)
**Ledger generation:** 1271 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 2.0715 | 98.449 | 81.227 | +6.32% | +1.14% | 2.15x | 12.6 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | STRONG 99/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 2.974 | 70.639 | 73.411 | +3.04% | +0.01% | 0.72x | 5.7 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002461 | 70.113 | 74.699 | +4.99% | +0.33% | 0.38x | 4.1 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | TAO/USD | 190.8216 | 62.193 | 71.386 | +2.74% | -0.07% | 0.12x | 5.6 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ZEC/USD | 796.69 | 61.861 | 70.091 | +2.38% | -0.36% | 0.36x | 3.1 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | JTO/USD | 0.23542 | 59.046 | 66.352 | +5.82% | -0.03% | 0.29x | 11.0 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | WEAK 30/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | LINK/USD | 8.7894 | 58.712 | 66.448 | +2.26% | +0.26% | 0.10x | 3.8 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ETH/USD | 1707.19 | 58.044 | 65.336 | +1.48% | +0.08% | 0.23x | 0.1 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | HYPE/USD | 62.29 | 57.983 | 65.396 | +1.71% | -0.06% | 0.29x | 3.2 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | SUI/USD | 0.6584 | 57.974 | 66.244 | +1.71% | -0.08% | 0.21x | 1.5 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XLM/USD | 0.12925 | 57.577 | 52.061 | +0.35% | +0.05% | 1.53x | 1.7 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | MODERATE 64/100 | HIGH 55/100 | Watch | WATCH |
| 12 | INJ/USD | 6.146 | 55.406 | 59.288 | +2.90% | +0.41% | 0.41x | 3.3 | 2026-11-22T10:41:01.026923+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 81.227 | 2.0715 | +1.14% | 2.15x |
| 2 | PUMP/USD | 74.699 | 0.002461 | +0.33% | 0.38x |
| 3 | NEAR/USD | 73.411 | 2.974 | +0.01% | 0.72x |
| 4 | TAO/USD | 71.386 | 190.8216 | -0.07% | 0.12x |
| 5 | ZEC/USD | 70.091 | 796.69 | -0.36% | 0.36x |
| 6 | LINK/USD | 66.448 | 8.7894 | +0.26% | 0.10x |
| 7 | JTO/USD | 66.352 | 0.23542 | -0.03% | 0.29x |
| 8 | SUI/USD | 66.244 | 0.6584 | -0.08% | 0.21x |
| 9 | HYPE/USD | 65.396 | 62.29 | -0.06% | 0.29x |
| 10 | ETH/USD | 65.336 | 1707.19 | +0.08% | 0.23x |
| 11 | INJ/USD | 59.288 | 6.146 | +0.41% | 0.41x |
| 12 | XLM/USD | 52.061 | 0.12925 | +0.05% | 1.53x |

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

- Persisted scans: 1271; predictions: 10172; observations: 769148.
- Matured sampled outcomes across 1/6/24/48h: 14659; gap abstentions: 22195. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
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

**Writer:** 45013509664 · **Generation:** 1271 · **Legacy run:** 45013509664
**Main quote time:** 2026-11-22T10:41:06.917320+00:00 · **Legacy report time:** 2026-11-22T10:41:51.815867+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.0715 | 98.45 | +1.14% | 2.15x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | NEAR/USD | 2.974 | 70.64 | +0.01% | 0.72x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 3 | PUMP/USD | 0.002461 | 70.11 | +0.33% | 0.38x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 4 | TAO/USD | 190.8216 | 62.19 | -0.07% | 0.12x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 5 | ZEC/USD | 796.69 | 61.86 | -0.36% | 0.36x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 6 | JTO/USD | 0.23542 | 59.05 | -0.03% | 0.29x | WEAK 30/100 | EXTREME 94/100 | Do nothing |
| 7 | LINK/USD | 8.7894 | 58.71 | +0.26% | 0.10x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 8 | ETH/USD | 1707.19 | 58.04 | +0.08% | 0.23x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 9 | HYPE/USD | 62.29 | 57.98 | -0.06% | 0.29x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | SUI/USD | 0.6584 | 57.97 | -0.08% | 0.21x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XLM/USD | 0.12925 | 57.58 | +0.05% | 1.53x | MODERATE 64/100 | HIGH 55/100 | Watch |
| 12 | INJ/USD | 6.146 | 55.41 | +0.41% | 0.41x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.0707 | 88.41 | +1.14% | 2.15x | 8270 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ASTER/USD | 0.50634 | 73.43 | +0.11% | 1.23x | 2054 | MODERATE 62/100 | HIGH 67/100 | Watch |

**Same-run overlap:** PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
