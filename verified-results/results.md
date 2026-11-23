# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T04:01:17.050013+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45109147253
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 8e55d31058c1c5a15e883fe53ea222710ac2a7d1 (atomic ledger/results publication)
**Ledger generation:** 1378 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 497.78 | 62.291 | 59.364 | +0.82% | -0.12% | 1.35x | 2.8 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SOL/USD | 71.2 | 58.859 | 59.947 | +0.81% | +0.06% | 0.86x | 1.4 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 3 | JUP/USD | 0.23276 | 58.290 | 54.114 | +3.65% | +0.39% | 1.22x | 10.3 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | VVV/USD | 26.862 | 57.555 | 57.850 | +1.22% | +1.49% | 0.23x | 7.8 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XRP/USD | 0.93049 | 55.518 | 57.173 | +0.32% | +0.02% | 0.82x | 0.1 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 6 | BLESS/USD | 0.017599 | 52.435 | 62.357 | +9.36% | -1.22% | 0.62x | 43.3 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | WEAK 16/100 | EXTREME 100/100 | Do nothing | WATCH |
| 7 | CC/USD | 0.07533 | 50.930 | 52.650 | +2.81% | -0.19% | 0.92x | 4.0 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 8 | ETH/USD | 1727.51 | 48.725 | 57.370 | +0.34% | -0.00% | 0.14x | 0.1 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | NEAR/USD | 3.0076 | 48.064 | 58.751 | +0.87% | -0.54% | 0.20x | 4.7 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | UNI/USD | 4.7608 | 46.172 | 51.624 | +1.70% | +0.42% | 0.25x | 4.6 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | NIGHT/USD | 0.04937 | 43.120 | 46.810 | +0.41% | +0.22% | 0.52x | 12.2 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | PAXG/USD | 3595.84 | 43.069 | 48.516 | +0.66% | -0.01% | 0.46x | 1.1 | 2026-11-23T04:01:09.359988+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 62.357 | 0.017599 | -1.22% | 0.62x |
| 2 | SOL/USD | 59.947 | 71.2 | +0.06% | 0.86x |
| 3 | XMR/USD | 59.364 | 497.78 | -0.12% | 1.35x |
| 4 | NEAR/USD | 58.751 | 3.0076 | -0.54% | 0.20x |
| 5 | VVV/USD | 57.850 | 26.862 | +1.49% | 0.23x |
| 6 | ETH/USD | 57.370 | 1727.51 | -0.00% | 0.14x |
| 7 | XRP/USD | 57.173 | 0.93049 | +0.02% | 0.82x |
| 8 | JUP/USD | 54.114 | 0.23276 | +0.39% | 1.22x |
| 9 | CC/USD | 52.650 | 0.07533 | -0.19% | 0.92x |
| 10 | UNI/USD | 51.624 | 4.7608 | +0.42% | 0.25x |
| 11 | PAXG/USD | 48.516 | 3595.84 | -0.01% | 0.46x |
| 12 | NIGHT/USD | 46.810 | 0.04937 | +0.22% | 0.52x |

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

- Persisted scans: 1378; predictions: 11303; observations: 834307.
- Matured sampled outcomes across 1/6/24/48h: 18236; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 93 (sampled only; not a success-rate estimate).
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

**Writer:** 45109147253 · **Generation:** 1378 · **Legacy run:** 45109147253
**Main quote time:** 2026-11-23T04:01:17.050013+00:00 · **Legacy report time:** 2026-11-23T04:02:00.049188+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 497.78 | 62.29 | -0.12% | 1.35x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 2 | SOL/USD | 71.2 | 58.86 | +0.06% | 0.86x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 3 | JUP/USD ⭐ | 0.23276 | 58.29 | +0.39% | 1.22x | MODERATE 69/100 | VERY_HIGH 73/100 | Watch |
| 4 | VVV/USD | 26.862 | 57.56 | +1.49% | 0.23x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 5 | XRP/USD | 0.93049 | 55.52 | +0.02% | 0.82x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 6 | BLESS/USD | 0.017599 | 52.44 | -1.22% | 0.62x | WEAK 16/100 | EXTREME 100/100 | Do nothing |
| 7 | CC/USD | 0.07533 | 50.93 | -0.19% | 0.92x | WEAK 30/100 | VERY_HIGH 73/100 | Do nothing |
| 8 | ETH/USD | 1727.51 | 48.73 | -0.00% | 0.14x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | NEAR/USD | 3.0076 | 48.06 | -0.54% | 0.20x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | UNI/USD | 4.7608 | 46.17 | +0.42% | 0.25x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 11 | NIGHT/USD | 0.04937 | 43.12 | +0.22% | 0.52x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 12 | PAXG/USD | 3595.84 | 43.07 | -0.01% | 0.46x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD ⭐ | 0.23276 | 70.08 | +0.39% | 1.22x | 2793 | STRONG 75/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** JUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
