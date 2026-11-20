# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T06:40:31.204693+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44689352401
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 6bd9fd78a944ceaeacc07a6b117ae23727c07e9d (atomic ledger/results publication)
**Ledger generation:** 942 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4405 | 67.206 | 53.724 | +3.38% | +1.08% | 1.81x | 15.9 | 2026-11-20T06:40:27.095093+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PROS/USD | 0.5856 | 60.242 | 64.730 | +8.71% | -0.44% | 0.77x | 22.3 | 2026-11-20T06:40:27.095093+00:00 | Not calibrated | WEAK 25/100 | EXTREME 92/100 | Do nothing | WATCH |
| 3 | BMT/USD | 0.02172 | 59.401 | 55.894 | +8.17% | -0.36% | 1.53x | 41.5 | 2026-11-20T06:40:27.095093+00:00 | Not calibrated | WEAK 35/100 | EXTREME 95/100 | Do nothing | WATCH |
| 4 | XRP/USD | 0.9631 | 57.096 | 57.394 | +0.40% | -0.17% | 1.05x | 0.8 | 2026-11-20T06:40:27.095093+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 5 | XLM/USD | 0.133355 | 51.411 | 57.143 | +0.49% | +0.10% | 0.38x | 2.6 | 2026-11-20T06:40:27.095093+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AUD/USD | 0.66738 | 50.831 | 40.907 | +0.28% | -0.01% | 2.00x | 0.1 | 2026-11-20T06:40:27.095093+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.09961 | 50.492 | 50.151 | +3.51% | +0.61% | 0.73x | 13.1 | 2026-11-20T06:40:27.095093+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | SKR/USD | 0.010232 | 32.329 | 34.854 | +1.85% | +0.36% | 0.57x | 18.6 | 2026-11-20T06:40:27.095093+00:00 | Not calibrated | WEAK 41/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 64.730 | 0.5856 | -0.44% | 0.77x |
| 2 | XRP/USD | 57.394 | 0.9631 | -0.17% | 1.05x |
| 3 | XLM/USD | 57.143 | 0.133355 | +0.10% | 0.38x |
| 4 | BMT/USD | 55.894 | 0.02172 | -0.36% | 1.53x |
| 5 | ICNT/USD | 53.724 | 0.4405 | +1.08% | 1.81x |
| 6 | SYRUP/USD | 50.151 | 0.09961 | +0.61% | 0.73x |
| 7 | AUD/USD | 40.907 | 0.66738 | -0.01% | 2.00x |
| 8 | SKR/USD | 34.854 | 0.010232 | +0.36% | 0.57x |

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

- Persisted scans: 942; predictions: 7996; observations: 569181.
- Matured sampled outcomes across 1/6/24/48h: 9386; gap abstentions: 17252. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44689352401 · **Generation:** 942 · **Legacy run:** 44689352401
**Main quote time:** 2026-11-20T06:40:31.204693+00:00 · **Legacy report time:** 2026-11-20T06:41:17.800267+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4405 | 67.21 | +1.08% | 1.81x | STRONG 84/100 | HIGH 61/100 | Consider small entry |
| 2 | PROS/USD | 0.5856 | 60.24 | -0.44% | 0.77x | WEAK 25/100 | EXTREME 92/100 | Do nothing |
| 3 | BMT/USD | 0.02172 | 59.40 | -0.36% | 1.53x | WEAK 35/100 | EXTREME 95/100 | Do nothing |
| 4 | XRP/USD | 0.9631 | 57.10 | -0.17% | 1.05x | WEAK 39/100 | HIGH 68/100 | Watch |
| 5 | XLM/USD | 0.133355 | 51.41 | +0.10% | 0.38x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 6 | AUD/USD | 0.66738 | 50.83 | -0.01% | 2.00x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 7 | SYRUP/USD | 0.09961 | 50.49 | +0.61% | 0.73x | MODERATE 50/100 | VERY_HIGH 81/100 | Watch |
| 8 | SKR/USD | 0.010232 | 32.33 | +0.36% | 0.57x | WEAK 41/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4405 | 73.85 | +1.08% | 1.81x | 7640 | STRONG 87/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
