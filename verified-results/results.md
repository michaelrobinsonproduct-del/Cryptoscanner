# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T22:35:04.885180+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44191382760
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** 8f2bb0554c8b7fcab2361d17ce8df4b99f1bf074 (atomic ledger/results publication)
**Ledger generation:** 460 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 944.94 | 94.419 | 84.790 | +4.55% | +0.74% | 1.59x | 4.1 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.33 | 91.304 | 91.221 | +5.45% | +0.69% | 0.66x | 3.9 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.109e-05 | 88.329 | 69.405 | +10.16% | +0.78% | 4.78x | 17.0 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | STRONG 94/100 | HIGH 66/100 | Consider small entry | WATCH |
| 4 | INJ/USD | 7.246 | 84.005 | 86.755 | +5.03% | +0.40% | 0.52x | 6.9 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5019 | 82.415 | 65.426 | +4.91% | +1.23% | 2.08x | 2.0 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | STRONG 96/100 | HIGH 60/100 | Consider small entry | WATCH |
| 6 | XRP/USD | 0.97126 | 75.392 | 66.737 | +1.73% | +0.10% | 1.81x | 0.7 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 7 | LINK/USD | 9.23431 | 73.696 | 59.853 | +1.08% | +0.56% | 2.11x | 2.9 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | SOL/USD | 73.83 | 73.640 | 76.932 | +3.23% | +0.27% | 0.53x | 1.4 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | JUP/USD | 0.2575 | 69.543 | 71.744 | +7.04% | +0.83% | 0.37x | 12.8 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | VVV/USD | 20.915 | 66.656 | 69.680 | +3.81% | +1.25% | 0.07x | 7.2 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0595897 | 65.165 | 62.000 | +1.20% | +0.37% | 1.13x | 0.7 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XMR/USD | 506.01 | 64.969 | 70.256 | +2.52% | -0.17% | 0.55x | 4.7 | 2026-11-17T22:34:56.457032+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 91.221 | 3.33 | +0.69% | 0.66x |
| 2 | INJ/USD | 86.755 | 7.246 | +0.40% | 0.52x |
| 3 | ZEC/USD | 84.790 | 944.94 | +0.74% | 1.59x |
| 4 | SOL/USD | 76.932 | 73.83 | +0.27% | 0.53x |
| 5 | JUP/USD | 71.744 | 0.2575 | +0.83% | 0.37x |
| 6 | XMR/USD | 70.256 | 506.01 | -0.17% | 0.55x |
| 7 | VVV/USD | 69.680 | 20.915 | +1.25% | 0.07x |
| 8 | LUNA/USD | 69.405 | 4.109e-05 | +0.78% | 4.78x |
| 9 | XRP/USD | 66.737 | 0.97126 | +0.10% | 1.81x |
| 10 | AKT/USD | 65.426 | 0.5019 | +1.23% | 2.08x |
| 11 | XDG/USD | 62.000 | 0.0595897 | +0.37% | 1.13x |
| 12 | LINK/USD | 59.853 | 9.23431 | +0.56% | 2.11x |

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

- Persisted scans: 460; predictions: 4001; observations: 277147.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12386. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44191382760 · **Generation:** 460 · **Legacy run:** 44191382760
**Main quote time:** 2026-11-17T22:35:04.885180+00:00 · **Legacy report time:** 2026-11-17T22:35:15.451037+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 944.94 | 94.42 | +0.74% | 1.59x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.33 | 91.30 | +0.69% | 0.66x | STRONG 86/100 | VERY_HIGH 70/100 | Watch |
| 3 | LUNA/USD ⭐ | 4.109e-05 | 88.33 | +0.78% | 4.78x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 4 | INJ/USD ⭐ | 7.246 | 84.00 | +0.40% | 0.52x | STRONG 82/100 | VERY_HIGH 70/100 | Watch |
| 5 | AKT/USD ⭐ | 0.5019 | 82.41 | +1.23% | 2.08x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 6 | XRP/USD ⭐ | 0.97126 | 75.39 | +0.10% | 1.81x | STRONG 83/100 | HIGH 55/100 | Watch |
| 7 | LINK/USD | 9.23431 | 73.70 | +0.56% | 2.11x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 8 | SOL/USD ⭐ | 73.83 | 73.64 | +0.27% | 0.53x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 9 | JUP/USD | 0.2575 | 69.54 | +0.83% | 0.37x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 10 | VVV/USD | 20.915 | 66.66 | +1.25% | 0.07x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0595897 | 65.16 | +0.37% | 1.13x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 12 | XMR/USD | 506.01 | 64.97 | -0.17% | 0.55x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 944.95 | 100.00 | +1.25% | 2.03x | 25818 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.3307 | 99.85 | +1.05% | 1.98x | 14814 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | INJ/USD ⭐ | 7.248 | 92.77 | +1.10% | 1.82x | 9734 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 73.83 | 89.96 | +0.41% | 1.17x | 35143 | STRONG 90/100 | HIGH 62/100 | Watch |
| 5 | AKT/USD ⭐ | 0.5018 | 82.29 | +1.23% | 2.08x | 2940 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 6 | LUNA/USD ⭐ | 4.109e-05 | 79.97 | +0.07% | 4.09x | 3243 | STRONG 90/100 | HIGH 66/100 | Watch |
| 7 | XRP/USD ⭐ | 0.97101 | 75.35 | +0.21% | 1.94x | 29705 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, NEAR/USD, LUNA/USD, INJ/USD, AKT/USD, XRP/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
