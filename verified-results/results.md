# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T21:41:12.977608+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45073324017
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 31d5536773dc43115622bb7bd8168289e8037cc2 (atomic ledger/results publication)
**Ledger generation:** 1339 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04902 | 85.948 | 88.197 | +10.70% | +0.43% | 0.56x | 10.2 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | HYPE/USD | 62.71 | 85.527 | 71.005 | +2.40% | -0.10% | 2.84x | 1.6 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.00258 | 82.698 | 82.824 | +10.07% | -0.27% | 1.12x | 7.8 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 4 | VVV/USD | 25.994 | 78.040 | 80.752 | +4.39% | -0.38% | 0.92x | 10.0 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | ZEC/USD | 792.83 | 75.498 | 65.914 | +1.88% | -0.36% | 2.14x | 4.5 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NEAR/USD | 2.9984 | 74.553 | 80.686 | +3.88% | +0.03% | 0.37x | 3.0 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ETH/USD | 1721.8 | 70.856 | 71.415 | +2.35% | -0.13% | 1.01x | 0.1 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6566 | 64.250 | 64.157 | +1.44% | +0.11% | 0.96x | 1.5 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XBT/USD | 60911.7 | 59.984 | 64.565 | +1.37% | +0.00% | 0.54x | 0.0 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | BNB/USD | 557.18 | 49.991 | 49.016 | +1.78% | -0.17% | 1.18x | 1.4 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | LTC/USD | 40.09 | 46.367 | 47.849 | +0.91% | -0.03% | 0.86x | 2.5 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | WEAK 28/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | XMR/USD | 493.74 | 45.536 | 52.694 | +0.39% | -0.32% | 0.45x | 10.1 | 2026-11-22T21:41:06.930718+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 88.197 | 0.04902 | +0.43% | 0.56x |
| 2 | PUMP/USD | 82.824 | 0.00258 | -0.27% | 1.12x |
| 3 | VVV/USD | 80.752 | 25.994 | -0.38% | 0.92x |
| 4 | NEAR/USD | 80.686 | 2.9984 | +0.03% | 0.37x |
| 5 | ETH/USD | 71.415 | 1721.8 | -0.13% | 1.01x |
| 6 | HYPE/USD | 71.005 | 62.71 | -0.10% | 2.84x |
| 7 | ZEC/USD | 65.914 | 792.83 | -0.36% | 2.14x |
| 8 | XBT/USD | 64.565 | 60911.7 | +0.00% | 0.54x |
| 9 | SUI/USD | 64.157 | 0.6566 | +0.11% | 0.96x |
| 10 | XMR/USD | 52.694 | 493.74 | -0.32% | 0.45x |
| 11 | BNB/USD | 49.016 | 557.18 | -0.17% | 1.18x |
| 12 | LTC/USD | 47.849 | 40.09 | -0.03% | 0.86x |

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

- Persisted scans: 1339; predictions: 10987; observations: 810559.
- Matured sampled outcomes across 1/6/24/48h: 16809; gap abstentions: 22367. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45073324017 · **Generation:** 1339 · **Legacy run:** 45073324017
**Main quote time:** 2026-11-22T21:41:12.977608+00:00 · **Legacy report time:** 2026-11-22T21:42:17.947857+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04902 | 85.95 | +0.43% | 0.56x | MODERATE 68/100 | VERY_HIGH 76/100 | Watch |
| 2 | HYPE/USD | 62.71 | 85.53 | -0.10% | 2.84x | STRONG 73/100 | HIGH 61/100 | Watch |
| 3 | PUMP/USD | 0.00258 | 82.70 | -0.27% | 1.12x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 4 | VVV/USD | 25.994 | 78.04 | -0.38% | 0.92x | WEAK 39/100 | VERY_HIGH 74/100 | Watch |
| 5 | ZEC/USD | 792.83 | 75.50 | -0.36% | 2.14x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 6 | NEAR/USD | 2.9984 | 74.55 | +0.03% | 0.37x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | ETH/USD | 1721.8 | 70.86 | -0.13% | 1.01x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 8 | SUI/USD | 0.6566 | 64.25 | +0.11% | 0.96x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 9 | XBT/USD | 60911.7 | 59.98 | +0.00% | 0.54x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | BNB/USD | 557.18 | 49.99 | -0.17% | 1.18x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | LTC/USD | 40.09 | 46.37 | -0.03% | 0.86x | WEAK 28/100 | HIGH 68/100 | Do nothing |
| 12 | XMR/USD | 493.74 | 45.54 | -0.32% | 0.45x | WEAK 23/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
