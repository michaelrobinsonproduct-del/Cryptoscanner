# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T10:30:56.242396+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44894588591
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 5f46bc8b2893f24db5a9e5971076aac90e36007e (atomic ledger/results publication)
**Ledger generation:** 1121 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.877 | 111.748 | 90.660 | +5.49% | +1.22% | 2.50x | 5.5 | 2026-11-21T10:30:49.821203+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 465.85 | 74.455 | 64.078 | +2.10% | +0.80% | 1.64x | 11.2 | 2026-11-21T10:30:49.821203+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | TRX/USD | 0.302605 | 72.856 | 57.540 | +0.37% | +0.06% | 3.96x | 0.0 | 2026-11-21T10:30:49.821203+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1640.51 | 62.453 | 64.129 | +1.31% | +0.56% | 0.55x | 0.1 | 2026-11-21T10:30:49.821203+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.0769 | 58.469 | 49.192 | +3.22% | +1.96% | 0.95x | 26.2 | 2026-11-21T10:30:49.821203+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | SENT/USD | 0.02075 | 32.401 | 34.048 | +0.75% | +0.62% | 0.53x | 4.3 | 2026-11-21T10:30:49.821203+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.05812 | 31.711 | 40.802 | +1.95% | +0.09% | 0.05x | 8.6 | 2026-11-21T10:30:49.821203+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 90.660 | 21.877 | +1.22% | 2.50x |
| 2 | ETH/USD | 64.129 | 1640.51 | +0.56% | 0.55x |
| 3 | XMR/USD | 64.078 | 465.85 | +0.80% | 1.64x |
| 4 | TRX/USD | 57.540 | 0.302605 | +0.06% | 3.96x |
| 5 | USELESS/USD | 49.192 | 0.0769 | +1.96% | 0.95x |
| 6 | ZAMA/USD | 40.802 | 0.05812 | +0.09% | 0.05x |
| 7 | SENT/USD | 34.048 | 0.02075 | +0.62% | 0.53x |

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

- Persisted scans: 1121; predictions: 8796; observations: 677927.
- Matured sampled outcomes across 1/6/24/48h: 11572; gap abstentions: 20322. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44894588591 · **Generation:** 1121 · **Legacy run:** 44894588591
**Main quote time:** 2026-11-21T10:30:56.242396+00:00 · **Legacy report time:** 2026-11-21T10:32:00.155891+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.877 | 111.75 | +1.22% | 2.50x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 465.85 | 74.45 | +0.80% | 1.64x | STRONG 87/100 | HIGH 61/100 | Consider small entry |
| 3 | TRX/USD ⭐ | 0.302605 | 72.86 | +0.06% | 3.96x | STRONG 91/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1640.51 | 62.45 | +0.56% | 0.55x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 5 | USELESS/USD | 0.0769 | 58.47 | +1.96% | 0.95x | MODERATE 49/100 | VERY_HIGH 74/100 | Watch |
| 6 | SENT/USD | 0.02075 | 32.40 | +0.62% | 0.53x | MODERATE 46/100 | VERY_HIGH 82/100 | Watch |
| 7 | ZAMA/USD | 0.05812 | 31.71 | +0.09% | 0.05x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.796 | 96.81 | +1.22% | 2.50x | 14809 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 465.85 | 67.10 | +0.80% | 1.64x | 11674 | STRONG 84/100 | HIGH 61/100 | Consider small entry |
| 3 | TRX/USD ⭐ | 0.302605 | 62.99 | +0.06% | 3.96x | 6847 | STRONG 86/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, XMR/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
