# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T17:00:56.690395+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44927553807
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** b5ec3072d48c7d7d55d695ae979b9f955e966c07 (atomic ledger/results publication)
**Ledger generation:** 1161 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 481.35 | 101.877 | 93.237 | +5.49% | +0.49% | 1.62x | 0.4 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.7283 | 98.866 | 92.953 | +5.84% | +0.51% | 1.34x | 5.9 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 785.16 | 94.025 | 77.305 | +3.60% | +0.34% | 7.79x | 5.7 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ETH/USD | 1682.5 | 85.167 | 82.252 | +3.90% | +0.08% | 1.25x | 0.1 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XRP/USD | 0.92839 | 79.693 | 69.352 | +2.17% | +0.15% | 1.96x | 1.6 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SOL/USD | 70.61 | 77.344 | 73.648 | +2.77% | +0.20% | 1.27x | 1.4 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | MODERATE 64/100 | HIGH 55/100 | Watch | WATCH |
| 7 | TAO/USD | 185.5205 | 72.642 | 72.550 | +2.78% | -0.51% | 1.26x | 3.8 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XBT/USD | 59991.3 | 66.339 | 69.096 | +2.01% | +0.09% | 0.68x | 0.0 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | CT/USD | 0.1322 | 64.419 | 69.016 | +9.17% | -0.53% | 0.80x | 15.1 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | WEAK 32/100 | EXTREME 86/100 | Do nothing | WATCH |
| 10 | XDG/USD | 0.0550282 | 61.748 | 64.542 | +1.39% | +0.11% | 0.66x | 0.3 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | BEAM/USD | 0.003559 | 61.279 | 68.512 | +8.57% | -0.69% | 0.62x | 16.9 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | PAXG/USD | 3546.44 | 60.576 | 56.990 | +0.42% | +0.08% | 1.32x | 1.2 | 2026-11-21T17:00:50.775437+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 93.237 | 481.35 | +0.49% | 1.62x |
| 2 | UNI/USD | 92.953 | 4.7283 | +0.51% | 1.34x |
| 3 | ETH/USD | 82.252 | 1682.5 | +0.08% | 1.25x |
| 4 | ZEC/USD | 77.305 | 785.16 | +0.34% | 7.79x |
| 5 | SOL/USD | 73.648 | 70.61 | +0.20% | 1.27x |
| 6 | TAO/USD | 72.550 | 185.5205 | -0.51% | 1.26x |
| 7 | XRP/USD | 69.352 | 0.92839 | +0.15% | 1.96x |
| 8 | XBT/USD | 69.096 | 59991.3 | +0.09% | 0.68x |
| 9 | CT/USD | 69.016 | 0.1322 | -0.53% | 0.80x |
| 10 | BEAM/USD | 68.512 | 0.003559 | -0.69% | 0.62x |
| 11 | XDG/USD | 64.542 | 0.0550282 | +0.11% | 0.66x |
| 12 | PAXG/USD | 56.990 | 3546.44 | +0.08% | 1.32x |

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

- Persisted scans: 1161; predictions: 9241; observations: 702247.
- Matured sampled outcomes across 1/6/24/48h: 12157; gap abstentions: 20866. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44927553807 · **Generation:** 1161 · **Legacy run:** 44927553807
**Main quote time:** 2026-11-21T17:00:56.690395+00:00 · **Legacy report time:** 2026-11-21T17:02:01.052320+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 481.35 | 101.88 | +0.49% | 1.62x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.7283 | 98.87 | +0.51% | 1.34x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD ⭐ | 785.16 | 94.02 | +0.34% | 7.79x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1682.5 | 85.17 | +0.08% | 1.25x | STRONG 78/100 | HIGH 55/100 | Watch |
| 5 | XRP/USD ⭐ | 0.92839 | 79.69 | +0.15% | 1.96x | STRONG 85/100 | HIGH 55/100 | Watch |
| 6 | SOL/USD ⭐ | 70.61 | 77.34 | +0.20% | 1.27x | STRONG 74/100 | HIGH 55/100 | Watch |
| 7 | TAO/USD | 185.5205 | 72.64 | -0.51% | 1.26x | MODERATE 46/100 | HIGH 61/100 | Watch |
| 8 | XBT/USD | 59991.3 | 66.34 | +0.09% | 0.68x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 9 | CT/USD | 0.1322 | 64.42 | -0.53% | 0.80x | WEAK 32/100 | EXTREME 86/100 | Do nothing |
| 10 | XDG/USD | 0.0550282 | 61.75 | +0.11% | 0.66x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | BEAM/USD | 0.003559 | 61.28 | -0.69% | 0.62x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 12 | PAXG/USD | 3546.44 | 60.58 | +0.08% | 1.32x | MODERATE 65/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1684.08 | 97.56 | +0.08% | 1.25x | 87939 | STRONG 84/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 787.92 | 97.37 | +0.34% | 7.79x | 48774 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD ⭐ | 481.5 | 88.94 | +0.49% | 1.62x | 12671 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 4 | UNI/USD ⭐ | 4.7389 | 87.88 | +0.51% | 1.34x | 12021 | STRONG 99/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD ⭐ | 70.66 | 84.90 | +0.20% | 1.27x | 53126 | STRONG 77/100 | HIGH 55/100 | Watch |
| 6 | XRP/USD ⭐ | 0.92977 | 81.51 | +0.15% | 1.96x | 62982 | STRONG 86/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XMR/USD, UNI/USD, ZEC/USD, ETH/USD, XRP/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
