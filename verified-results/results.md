# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T00:50:29.345048+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44846363502
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 54dd9dc1242eee7a335a2ae774f07123d1439b28 (atomic ledger/results publication)
**Ledger generation:** 1049 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.8981 | 81.379 | 66.865 | +3.82% | +1.88% | 1.51x | 18.0 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | STRONG 81/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | XBT/USD | 59020 | 57.789 | 57.534 | +0.36% | +0.10% | 0.98x | 0.0 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5097 | 57.641 | 39.879 | +1.15% | +0.55% | 3.27x | 2.0 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 4 | DRV/USD | 0.24776 | 54.287 | 38.681 | +0.90% | +0.12% | 2.51x | 6.1 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 5 | ETH/USD | 1624.4 | 52.108 | 57.104 | +0.31% | +0.11% | 0.45x | 0.2 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SOL/USD | 68.95 | 51.717 | 56.719 | +0.35% | -0.12% | 0.56x | 1.5 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | VVV/USD | 20.857 | 51.236 | 54.426 | +0.57% | +0.63% | 0.36x | 9.1 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | UNI/USD | 4.4811 | 50.338 | 48.275 | +0.31% | +0.21% | 1.10x | 4.5 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LINK/USD | 8.5555 | 50.029 | 54.514 | +0.30% | +0.12% | 0.49x | 5.2 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | CC/USD | 0.07491 | 39.327 | 35.894 | +0.48% | +0.31% | 1.19x | 8.0 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |
| 11 | DCR/USD | 10.159 | 38.375 | 31.017 | +0.53% | +0.32% | 1.58x | 6.9 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | MODERATE 64/100 | HIGH 67/100 | Watch | WATCH |
| 12 | CAP/USD | 0.092086 | 31.121 | 33.820 | +0.59% | +0.14% | 0.66x | 6.1 | 2026-11-21T00:50:21.740119+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 66.865 | 1.8981 | +1.88% | 1.51x |
| 2 | XBT/USD | 57.534 | 59020 | +0.10% | 0.98x |
| 3 | ETH/USD | 57.104 | 1624.4 | +0.11% | 0.45x |
| 4 | SOL/USD | 56.719 | 68.95 | -0.12% | 0.56x |
| 5 | LINK/USD | 54.514 | 8.5555 | +0.12% | 0.49x |
| 6 | VVV/USD | 54.426 | 20.857 | +0.63% | 0.36x |
| 7 | UNI/USD | 48.275 | 4.4811 | +0.21% | 1.10x |
| 8 | AKT/USD | 39.879 | 0.5097 | +0.55% | 3.27x |
| 9 | DRV/USD | 38.681 | 0.24776 | +0.12% | 2.51x |
| 10 | CC/USD | 35.894 | 0.07491 | +0.31% | 1.19x |
| 11 | CAP/USD | 33.820 | 0.092086 | +0.14% | 0.66x |
| 12 | DCR/USD | 31.017 | 10.159 | +0.32% | 1.58x |

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

- Persisted scans: 1049; predictions: 8396; observations: 634152.
- Matured sampled outcomes across 1/6/24/48h: 10931; gap abstentions: 19059. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44846363502 · **Generation:** 1049 · **Legacy run:** 44846363502
**Main quote time:** 2026-11-21T00:50:29.345048+00:00 · **Legacy report time:** 2026-11-21T00:51:20.387369+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.8981 | 81.38 | +1.88% | 1.51x | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 2 | XBT/USD | 59020 | 57.79 | +0.10% | 0.98x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5097 | 57.64 | +0.55% | 3.27x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 4 | DRV/USD ⭐ | 0.24776 | 54.29 | +0.12% | 2.51x | STRONG 82/100 | HIGH 60/100 | Watch |
| 5 | ETH/USD | 1624.4 | 52.11 | +0.11% | 0.45x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 6 | SOL/USD | 68.95 | 51.72 | -0.12% | 0.56x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | VVV/USD | 20.857 | 51.24 | +0.63% | 0.36x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 8 | UNI/USD ⭐ | 4.4811 | 50.34 | +0.21% | 1.10x | STRONG 70/100 | HIGH 62/100 | Watch |
| 9 | LINK/USD | 8.5555 | 50.03 | +0.12% | 0.49x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 10 | CC/USD | 0.07491 | 39.33 | +0.31% | 1.19x | MODERATE 55/100 | HIGH 67/100 | Watch |
| 11 | DCR/USD | 10.159 | 38.37 | +0.32% | 1.58x | MODERATE 64/100 | HIGH 67/100 | Watch |
| 12 | CAP/USD | 0.092086 | 31.12 | +0.14% | 0.66x | WEAK 36/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.8977 | 86.69 | +1.88% | 1.51x | 21980 | STRONG 88/100 | HIGH 67/100 | Consider small entry |
| 2 | BLESS/USD | 0.014257 | 79.51 | +1.58% | 3.34x | 2535 | STRONG 80/100 | VERY_HIGH 82/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5097 | 47.15 | +0.55% | 3.27x | 4549 | STRONG 84/100 | HIGH 66/100 | Consider small entry |
| 4 | DRV/USD ⭐ | 0.24776 | 46.17 | +0.12% | 2.51x | 5988 | STRONG 78/100 | HIGH 60/100 | Watch |
| 5 | UNI/USD ⭐ | 4.4811 | 44.73 | +0.21% | 1.10x | 9187 | MODERATE 67/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEARL/USD, AKT/USD, DRV/USD, UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
