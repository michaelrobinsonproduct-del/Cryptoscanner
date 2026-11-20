# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T06:10:29.425784+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44685818283
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 51c5a4507f2ce73b56afc8af60ff3ad18895e021 (atomic ledger/results publication)
**Ledger generation:** 938 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.96808 | 73.092 | 60.979 | +0.92% | -0.32% | 2.37x | 0.9 | 2026-11-20T06:10:24.854288+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XLM/USD | 0.133371 | 61.831 | 57.790 | +0.51% | -0.42% | 1.61x | 1.5 | 2026-11-20T06:10:24.854288+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HBAR/USD | 0.05398 | 56.357 | 41.079 | +0.41% | +0.06% | 3.35x | 3.7 | 2026-11-20T06:10:24.854288+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SKR/USD | 0.010245 | 45.079 | 30.421 | +1.98% | +0.15% | 2.39x | 29.3 | 2026-11-20T06:10:24.854288+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | AUD/USD | 0.66721 | 32.420 | 40.650 | +0.26% | +0.06% | 0.15x | 0.6 | 2026-11-20T06:10:24.854288+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 60.979 | 0.96808 | -0.32% | 2.37x |
| 2 | XLM/USD | 57.790 | 0.133371 | -0.42% | 1.61x |
| 3 | HBAR/USD | 41.079 | 0.05398 | +0.06% | 3.35x |
| 4 | AUD/USD | 40.650 | 0.66721 | +0.06% | 0.15x |
| 5 | SKR/USD | 30.421 | 0.010245 | +0.15% | 2.39x |

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

- Persisted scans: 938; predictions: 7969; observations: 566761.
- Matured sampled outcomes across 1/6/24/48h: 9338; gap abstentions: 17140. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44685818283 · **Generation:** 938 · **Legacy run:** 44685818283
**Main quote time:** 2026-11-20T06:10:29.425784+00:00 · **Legacy report time:** 2026-11-20T06:11:22.506175+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.96808 | 73.09 | -0.32% | 2.37x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | XLM/USD | 0.133371 | 61.83 | -0.42% | 1.61x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 3 | HBAR/USD ⭐ | 0.05398 | 56.36 | +0.06% | 3.35x | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | SKR/USD ⭐ | 0.010245 | 45.08 | +0.15% | 2.39x | MODERATE 68/100 | VERY_HIGH 79/100 | Watch |
| 5 | AUD/USD | 0.66721 | 32.42 | +0.06% | 0.15x | WEAK 36/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD ⭐ | 0.05395 | 48.07 | +0.06% | 3.35x | 8787 | STRONG 79/100 | HIGH 55/100 | Watch |
| 2 | SKR/USD ⭐ | 0.010245 | 43.86 | +0.15% | 2.39x | 1602 | STRONG 72/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** HBAR/USD, SKR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
