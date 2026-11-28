# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T08:27:21.439765+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46125671366
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4c43f795d58a9e293ead7109e56f0ea4b4d753f3 (atomic ledger/results publication)
**Ledger generation:** 2129 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 421.61 | 80.679 | 66.226 | +3.52% | -0.11% | 3.04x | 26.8 | 2026-11-28T08:27:18.334953+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | VVV/USD | 26.653 | 75.728 | 61.892 | +3.51% | -0.23% | 4.42x | 14.6 | 2026-11-28T08:27:18.334953+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05065 | 56.971 | 56.762 | +0.82% | +0.40% | 0.82x | 7.9 | 2026-11-28T08:27:18.334953+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.00439 | 55.514 | 60.565 | +5.07% | +0.71% | 0.14x | 11.4 | 2026-11-28T08:27:18.334953+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | HYPE/USD | 63.83 | 52.223 | 57.183 | +0.54% | -0.05% | 0.53x | 3.1 | 2026-11-28T08:27:18.334953+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 66.226 | 421.61 | -0.11% | 3.04x |
| 2 | VVV/USD | 61.892 | 26.653 | -0.23% | 4.42x |
| 3 | SPACE/USD | 60.565 | 0.00439 | +0.71% | 0.14x |
| 4 | HYPE/USD | 57.183 | 63.83 | -0.05% | 0.53x |
| 5 | NIGHT/USD | 56.762 | 0.05065 | +0.40% | 0.82x |

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

- Persisted scans: 2129; predictions: 19057; observations: 1289220.
- Matured sampled outcomes across 1/6/24/48h: 44872; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46125671366 · **Generation:** 2129 · **Legacy run:** 46125671366
**Main quote time:** 2026-11-28T08:27:21.439765+00:00 · **Legacy report time:** 2026-11-28T08:27:57.302659+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 421.61 | 80.68 | -0.11% | 3.04x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD | 26.653 | 75.73 | -0.23% | 4.42x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 3 | NIGHT/USD | 0.05065 | 56.97 | +0.40% | 0.82x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 4 | SPACE/USD | 0.00439 | 55.51 | +0.71% | 0.14x | MODERATE 53/100 | EXTREME 88/100 | Do nothing |
| 5 | HYPE/USD | 63.83 | 52.22 | -0.05% | 0.53x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XTZ/USD | 0.22778 | 30.99 | +0.44% | 9.31x | 2188 | MODERATE 65/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
