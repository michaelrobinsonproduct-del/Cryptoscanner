# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T10:21:07.659091+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45011876588
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 982d1a6f45b0c45512c8d6441caa900a8f089075 (atomic ledger/results publication)
**Ledger generation:** 1269 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 800.47 | 92.615 | 74.997 | +2.87% | +0.52% | 6.60x | 0.1 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 2.9682 | 91.336 | 73.009 | +2.84% | +0.67% | 8.06x | 3.7 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 25.45 | 85.605 | 67.122 | +2.21% | +0.70% | 5.23x | 6.7 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | TAO/USD | 191.1153 | 84.580 | 71.165 | +2.90% | -0.32% | 2.55x | 8.3 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PEARL/USD | 2.0409 | 84.568 | 69.187 | +4.75% | +0.41% | 2.33x | 13.8 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 92/100 | HIGH 61/100 | Consider small entry | WATCH |
| 6 | HYPE/USD | 62.31 | 83.206 | 65.625 | +1.75% | +0.52% | 22.98x | 3.2 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | SUI/USD | 0.6592 | 82.034 | 66.350 | +1.84% | +0.14% | 5.21x | 3.0 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 8 | LINK/USD | 8.7584 | 80.957 | 64.473 | +1.90% | +0.30% | 3.22x | 3.5 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | ETH/USD | 1708 | 80.343 | 65.673 | +1.53% | -0.07% | 4.26x | 0.1 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XBT/USD | 60769.4 | 77.651 | 62.907 | +1.13% | -0.05% | 7.81x | 0.0 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0554278 | 70.257 | 54.982 | +0.45% | +0.06% | 18.98x | 0.3 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 12 | JTO/USD | 0.23657 | 70.257 | 69.975 | +6.33% | -0.01% | 1.03x | 11.0 | 2026-11-22T10:21:01.646714+00:00 | Not calibrated | WEAK 40/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 74.997 | 800.47 | +0.52% | 6.60x |
| 2 | NEAR/USD | 73.009 | 2.9682 | +0.67% | 8.06x |
| 3 | TAO/USD | 71.165 | 191.1153 | -0.32% | 2.55x |
| 4 | JTO/USD | 69.975 | 0.23657 | -0.01% | 1.03x |
| 5 | PEARL/USD | 69.187 | 2.0409 | +0.41% | 2.33x |
| 6 | VVV/USD | 67.122 | 25.45 | +0.70% | 5.23x |
| 7 | SUI/USD | 66.350 | 0.6592 | +0.14% | 5.21x |
| 8 | ETH/USD | 65.673 | 1708 | -0.07% | 4.26x |
| 9 | HYPE/USD | 65.625 | 62.31 | +0.52% | 22.98x |
| 10 | LINK/USD | 64.473 | 8.7584 | +0.30% | 3.22x |
| 11 | XBT/USD | 62.907 | 60769.4 | -0.05% | 7.81x |
| 12 | XDG/USD | 54.982 | 0.0554278 | +0.06% | 18.98x |

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

- Persisted scans: 1269; predictions: 10148; observations: 767930.
- Matured sampled outcomes across 1/6/24/48h: 14607; gap abstentions: 22186. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45011876588 · **Generation:** 1269 · **Legacy run:** 45011876588
**Main quote time:** 2026-11-22T10:21:07.659091+00:00 · **Legacy report time:** 2026-11-22T10:21:53.353773+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 800.47 | 92.62 | +0.52% | 6.60x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 2.9682 | 91.34 | +0.67% | 8.06x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 25.45 | 85.61 | +0.70% | 5.23x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD | 191.1153 | 84.58 | -0.32% | 2.55x | STRONG 72/100 | HIGH 61/100 | Watch |
| 5 | PEARL/USD ⭐ | 2.0409 | 84.57 | +0.41% | 2.33x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 6 | HYPE/USD ⭐ | 62.31 | 83.21 | +0.52% | 22.98x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | SUI/USD ⭐ | 0.6592 | 82.03 | +0.14% | 5.21x | STRONG 96/100 | HIGH 55/100 | Watch |
| 8 | LINK/USD ⭐ | 8.7584 | 80.96 | +0.30% | 3.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | ETH/USD | 1708 | 80.34 | -0.07% | 4.26x | STRONG 70/100 | HIGH 61/100 | Watch |
| 10 | XBT/USD | 60769.4 | 77.65 | -0.05% | 7.81x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 11 | XDG/USD | 0.0554278 | 70.26 | +0.06% | 18.98x | STRONG 80/100 | HIGH 55/100 | Watch |
| 12 | JTO/USD | 0.23657 | 70.26 | -0.01% | 1.03x | WEAK 40/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9642 | 88.32 | +0.67% | 8.06x | 12670 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 799.6 | 85.86 | +0.52% | 6.60x | 27800 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PEARL/USD ⭐ | 2.0381 | 84.49 | +0.41% | 2.33x | 8244 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD ⭐ | 25.474 | 78.77 | +0.70% | 5.23x | 14215 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | SUI/USD ⭐ | 0.6585 | 78.14 | +0.14% | 5.21x | 7707 | STRONG 94/100 | HIGH 55/100 | Watch |
| 6 | LINK/USD ⭐ | 8.7573 | 77.47 | +0.30% | 3.22x | 6313 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | RENDER/USD | 1.351 | 76.46 | +0.59% | 2.37x | 3553 | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 8 | HYPE/USD ⭐ | 62.28 | 75.50 | +0.52% | 22.98x | 14117 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, NEAR/USD, VVV/USD, PEARL/USD, HYPE/USD, SUI/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
