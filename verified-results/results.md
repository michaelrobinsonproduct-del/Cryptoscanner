# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T00:50:07.392920+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44210974039
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 9d1ff2aa562287261526a7f04d8c1f9947ab3d06 (atomic ledger/results publication)
**Ledger generation:** 487 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 198.4372 | 72.650 | 55.954 | +0.45% | +0.34% | 4.44x | 4.4 | 2026-11-18T00:50:01.743463+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 21.1 | 60.964 | 47.311 | +0.35% | -0.27% | 12.55x | 8.1 | 2026-11-18T00:50:01.743463+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5142 | 50.946 | 31.136 | +0.96% | +0.96% | 4.00x | 15.6 | 2026-11-18T00:50:01.743463+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 4 | CAP/USD | 0.102547 | 43.901 | 40.430 | +1.56% | -0.14% | 1.42x | 6.1 | 2026-11-18T00:50:01.743463+00:00 | Not calibrated | WEAK 42/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 55.954 | 198.4372 | +0.34% | 4.44x |
| 2 | VVV/USD | 47.311 | 21.1 | -0.27% | 12.55x |
| 3 | CAP/USD | 40.430 | 0.102547 | -0.14% | 1.42x |
| 4 | AKT/USD | 31.136 | 0.5142 | +0.96% | 4.00x |

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

- Persisted scans: 487; predictions: 4239; observations: 293590.
- Matured sampled outcomes across 1/6/24/48h: 3315; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44210974039 · **Generation:** 487 · **Legacy run:** 44210974039
**Main quote time:** 2026-11-18T00:50:07.392920+00:00 · **Legacy report time:** 2026-11-18T00:50:21.915540+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 198.4372 | 72.65 | +0.34% | 4.44x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 21.1 | 60.96 | -0.27% | 12.55x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5142 | 50.95 | +0.96% | 4.00x | STRONG 85/100 | HIGH 66/100 | Consider small entry |
| 4 | CAP/USD | 0.102547 | 43.90 | -0.14% | 1.42x | WEAK 42/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 198.4372 | 57.09 | +0.34% | 4.44x | 5724 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5142 | 49.06 | +0.96% | 4.00x | 3391 | STRONG 90/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** TAO/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
