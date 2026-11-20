# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T06:15:32.635900+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44686412829
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 7e9d8e2dc085fa90d4d5de0808239b9d6491746e (atomic ledger/results publication)
**Ledger generation:** 939 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.9675 | 74.927 | 60.969 | +0.86% | -0.21% | 3.30x | 0.1 | 2026-11-20T06:15:27.590874+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SKR/USD | 0.010275 | 58.311 | 43.749 | +2.28% | -0.09% | 2.65x | 6.8 | 2026-11-20T06:15:27.590874+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | HBAR/USD | 0.05391 | 55.175 | 40.360 | +0.28% | -0.04% | 3.68x | 3.7 | 2026-11-20T06:15:27.590874+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XLM/USD | 0.13327 | 52.610 | 56.205 | +0.43% | -0.44% | 0.86x | 3.6 | 2026-11-20T06:15:27.590874+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | ICNT/USD | 0.4357 | 39.243 | 43.358 | +2.25% | -0.25% | 0.71x | 20.7 | 2026-11-20T06:15:27.590874+00:00 | Not calibrated | WEAK 15/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | AUD/USD | 0.66733 | 32.599 | 40.854 | +0.28% | +0.08% | 0.13x | 0.4 | 2026-11-20T06:15:27.590874+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 60.969 | 0.9675 | -0.21% | 3.30x |
| 2 | XLM/USD | 56.205 | 0.13327 | -0.44% | 0.86x |
| 3 | SKR/USD | 43.749 | 0.010275 | -0.09% | 2.65x |
| 4 | ICNT/USD | 43.358 | 0.4357 | -0.25% | 0.71x |
| 5 | AUD/USD | 40.854 | 0.66733 | +0.08% | 0.13x |
| 6 | HBAR/USD | 40.360 | 0.05391 | -0.04% | 3.68x |

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

- Persisted scans: 939; predictions: 7975; observations: 567366.
- Matured sampled outcomes across 1/6/24/48h: 9349; gap abstentions: 17161. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44686412829 · **Generation:** 939 · **Legacy run:** 44686412829
**Main quote time:** 2026-11-20T06:15:32.635900+00:00 · **Legacy report time:** 2026-11-20T06:16:24.250857+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.9675 | 74.93 | -0.21% | 3.30x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | SKR/USD | 0.010275 | 58.31 | -0.09% | 2.65x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |
| 3 | HBAR/USD | 0.05391 | 55.17 | -0.04% | 3.68x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 4 | XLM/USD | 0.13327 | 52.61 | -0.44% | 0.86x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 5 | ICNT/USD | 0.4357 | 39.24 | -0.25% | 0.71x | WEAK 15/100 | EXTREME 88/100 | Do nothing |
| 6 | AUD/USD | 0.66733 | 32.60 | +0.08% | 0.13x | WEAK 36/100 | VERY_HIGH 70/100 | Watch |

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
