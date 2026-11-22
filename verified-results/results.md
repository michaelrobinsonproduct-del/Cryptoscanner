# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T06:21:01.431689+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44993204701
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 432158a3ce8f193ba5e9500e7e7355a2ab7bf355 (atomic ledger/results publication)
**Ledger generation:** 1244 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 783.42 | 72.231 | 58.192 | +0.67% | -0.19% | 10.00x | 3.1 | 2026-11-22T06:20:58.133656+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.0487 | 61.043 | 38.646 | +1.69% | +1.48% | 3.44x | 8.2 | 2026-11-22T06:20:58.133656+00:00 | Not calibrated | STRONG 86/100 | HIGH 67/100 | Watch | WATCH |
| 3 | TRUMP/USD | 0.891 | 40.235 | 32.733 | +0.56% | +0.34% | 1.58x | 11.2 | 2026-11-22T06:20:58.133656+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.9588 | 33.014 | 36.581 | +0.54% | -0.62% | 0.95x | 18.9 | 2026-11-22T06:20:58.133656+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 74/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 58.192 | 783.42 | -0.19% | 10.00x |
| 2 | MEGA/USD | 38.646 | 0.0487 | +1.48% | 3.44x |
| 3 | PEARL/USD | 36.581 | 1.9588 | -0.62% | 0.95x |
| 4 | TRUMP/USD | 32.733 | 0.891 | +0.34% | 1.58x |

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

- Persisted scans: 1244; predictions: 9936; observations: 752710.
- Matured sampled outcomes across 1/6/24/48h: 14212; gap abstentions: 21994. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 55 (sampled only; not a success-rate estimate).
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

**Writer:** 44993204701 · **Generation:** 1244 · **Legacy run:** 44993204701
**Main quote time:** 2026-11-22T06:21:01.431689+00:00 · **Legacy report time:** 2026-11-22T06:22:04.763162+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 783.42 | 72.23 | -0.19% | 10.00x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 2 | MEGA/USD | 0.0487 | 61.04 | +1.48% | 3.44x | STRONG 86/100 | HIGH 67/100 | Watch |
| 3 | TRUMP/USD ⭐ | 0.891 | 40.23 | +0.34% | 1.58x | STRONG 70/100 | HIGH 66/100 | Watch |
| 4 | PEARL/USD | 1.9588 | 33.01 | -0.62% | 0.95x | WEAK 17/100 | VERY_HIGH 74/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUMP/USD ⭐ | 0.889 | 32.05 | +0.34% | 1.58x | 2919 | MODERATE 66/100 | HIGH 66/100 | Watch |

**Same-run overlap:** TRUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
