# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T13:52:52.902606+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46151530986
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 55b475be043fe629aa601b1eedf88aee3017fcd8 (atomic ledger/results publication)
**Ledger generation:** 2162 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05405 | 88.202 | 96.295 | +7.58% | -0.61% | 0.49x | 7.4 | 2026-11-28T13:52:50.675376+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XMR/USD | 432.26 | 81.526 | 85.654 | +6.14% | -1.14% | 1.16x | 24.6 | 2026-11-28T13:52:50.675376+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 84/100 | Watch | WATCH |
| 3 | SENT/USD | 0.024419 | 61.367 | 48.218 | +2.97% | -0.37% | 5.55x | 8.2 | 2026-11-28T13:52:50.675376+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | VVV/USD | 26.527 | 55.957 | 60.522 | +3.02% | -0.66% | 0.87x | 7.9 | 2026-11-28T13:52:50.675376+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | AKE/USD | 0.00113739 | 46.430 | 46.631 | +4.68% | +1.27% | 0.35x | 43.5 | 2026-11-28T13:52:50.675376+00:00 | Not calibrated | WEAK 38/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 96.295 | 0.05405 | -0.61% | 0.49x |
| 2 | XMR/USD | 85.654 | 432.26 | -1.14% | 1.16x |
| 3 | VVV/USD | 60.522 | 26.527 | -0.66% | 0.87x |
| 4 | SENT/USD | 48.218 | 0.024419 | -0.37% | 5.55x |
| 5 | AKE/USD | 46.631 | 0.00113739 | +1.27% | 0.35x |

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

- Persisted scans: 2162; predictions: 19241; observations: 1309218.
- Matured sampled outcomes across 1/6/24/48h: 46156; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46151530986 · **Generation:** 2162 · **Legacy run:** 46151530986
**Main quote time:** 2026-11-28T13:52:52.902606+00:00 · **Legacy report time:** 2026-11-28T13:53:49.701351+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05405 | 88.20 | -0.61% | 0.49x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 2 | XMR/USD | 432.26 | 81.53 | -1.14% | 1.16x | WEAK 41/100 | VERY_HIGH 84/100 | Watch |
| 3 | SENT/USD | 0.024419 | 61.37 | -0.37% | 5.55x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 4 | VVV/USD | 26.527 | 55.96 | -0.66% | 0.87x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 5 | AKE/USD | 0.00113739 | 46.43 | +1.27% | 0.35x | WEAK 38/100 | EXTREME 97/100 | Do nothing |

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
