# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T01:05:19.774109+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44650855793
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** e3d800505378815895ab44401e2dfcf930abb063 (atomic ledger/results publication)
**Ledger generation:** 893 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.13334 | 58.524 | 56.686 | +0.48% | +0.12% | 1.12x | 3.4 | 2026-11-20T01:05:15.820704+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XMR/USD | 500.3 | 56.916 | 55.566 | +0.57% | +0.17% | 1.05x | 6.8 | 2026-11-20T01:05:15.820704+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 3 | SYRUP/USD | 0.09858 | 42.453 | 40.174 | +2.44% | +1.13% | 0.66x | 17.3 | 2026-11-20T01:05:15.820704+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | STRK/USD | 0.03178 | 29.072 | 28.119 | +0.28% | +0.09% | 1.05x | 18.9 | 2026-11-20T01:05:15.820704+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05856 | 26.149 | 25.642 | +0.51% | -0.39% | 1.25x | 20.5 | 2026-11-20T01:05:15.820704+00:00 | Not calibrated | WEAK 13/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5361 | 24.866 | 30.682 | +0.49% | +0.54% | 0.15x | 11.2 | 2026-11-20T01:05:15.820704+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | RARE/USD | 0.01346 | 19.108 | 30.717 | +1.51% | -3.99% | 1.84x | 22.2 | 2026-11-20T01:05:15.820704+00:00 | Not calibrated | WEAK 20/100 | EXTREME 89/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 56.686 | 0.13334 | +0.12% | 1.12x |
| 2 | XMR/USD | 55.566 | 500.3 | +0.17% | 1.05x |
| 3 | SYRUP/USD | 40.174 | 0.09858 | +1.13% | 0.66x |
| 4 | RARE/USD | 30.717 | 0.01346 | -3.99% | 1.84x |
| 5 | AKT/USD | 30.682 | 0.5361 | +0.54% | 0.15x |
| 6 | STRK/USD | 28.119 | 0.03178 | +0.09% | 1.05x |
| 7 | MEGA/USD | 25.642 | 0.05856 | -0.39% | 1.25x |

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

- Persisted scans: 893; predictions: 7785; observations: 539604.
- Matured sampled outcomes across 1/6/24/48h: 8522; gap abstentions: 16137. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44650855793 · **Generation:** 893 · **Legacy run:** 44650855793
**Main quote time:** 2026-11-20T01:05:19.774109+00:00 · **Legacy report time:** 2026-11-20T01:06:02.831539+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.13334 | 58.52 | +0.12% | 1.12x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 2 | XMR/USD ⭐ | 500.3 | 56.92 | +0.17% | 1.05x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 3 | SYRUP/USD | 0.09858 | 42.45 | +1.13% | 0.66x | MODERATE 46/100 | VERY_HIGH 81/100 | Watch |
| 4 | STRK/USD ⭐ | 0.03178 | 29.07 | +0.09% | 1.05x | MODERATE 45/100 | VERY_HIGH 73/100 | Watch |
| 5 | MEGA/USD | 0.05856 | 26.15 | -0.39% | 1.25x | WEAK 13/100 | EXTREME 85/100 | Do nothing |
| 6 | AKT/USD | 0.5361 | 24.87 | +0.54% | 0.15x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |
| 7 | RARE/USD | 0.01346 | 19.11 | -3.99% | 1.84x | WEAK 20/100 | EXTREME 89/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.133038 | 47.94 | +0.12% | 1.12x | 10421 | MODERATE 59/100 | HIGH 62/100 | Watch |
| 2 | XMR/USD ⭐ | 499.63 | 42.89 | +0.17% | 1.05x | 7812 | MODERATE 51/100 | HIGH 68/100 | Watch |
| 3 | USELESS/USD | 0.09942 | 34.04 | +0.80% | 1.20x | 7569 | MODERATE 47/100 | HIGH 68/100 | Watch |
| 4 | STRK/USD ⭐ | 0.03178 | 29.23 | +0.09% | 1.05x | 4054 | MODERATE 50/100 | HIGH 67/100 | Watch |

**Same-run overlap:** XLM/USD, XMR/USD, STRK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
