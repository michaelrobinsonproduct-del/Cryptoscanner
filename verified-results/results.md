# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T02:55:01.259440+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44226638713
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** a75081f4c834f1af2756111d663603412402def6 (atomic ledger/results publication)
**Ledger generation:** 512 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 7.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2788 | 45.600 | 33.707 | +0.98% | +0.98% | 1.70x | 10.7 | 2026-11-18T02:54:59.183156+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5218 | 37.778 | 39.990 | +2.45% | +0.19% | 0.68x | 19.2 | 2026-11-18T02:54:59.183156+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 3 | CC/USD | 0.08234 | 28.963 | 33.740 | +0.26% | +0.18% | 0.43x | 6.1 | 2026-11-18T02:54:59.183156+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 75/100 | Do nothing | WATCH |
| 4 | PEARL/USD | 1.8286 | 28.453 | 32.920 | +1.00% | +0.61% | 0.25x | 18.6 | 2026-11-18T02:54:59.183156+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AKT/USD | 39.990 | 0.5218 | +0.19% | 0.68x |
| 2 | CC/USD | 33.740 | 0.08234 | +0.18% | 0.43x |
| 3 | ICNT/USD | 33.707 | 0.2788 | +0.98% | 1.70x |
| 4 | PEARL/USD | 32.920 | 1.8286 | +0.61% | 0.25x |

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

- Persisted scans: 512; predictions: 4336; observations: 308815.
- Matured sampled outcomes across 1/6/24/48h: 3491; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44226638713 · **Generation:** 512 · **Legacy run:** 44226638713
**Main quote time:** 2026-11-18T02:55:01.259440+00:00 · **Legacy report time:** 2026-11-18T02:55:15.533236+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2788 | 45.60 | +0.98% | 1.70x | STRONG 73/100 | HIGH 66/100 | Watch |
| 2 | AKT/USD | 0.5218 | 37.78 | +0.19% | 0.68x | WEAK 34/100 | VERY_HIGH 81/100 | Do nothing |
| 3 | CC/USD | 0.08234 | 28.96 | +0.18% | 0.43x | WEAK 34/100 | VERY_HIGH 75/100 | Do nothing |
| 4 | PEARL/USD | 1.8286 | 28.45 | +0.61% | 0.25x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.279 | 41.68 | +0.98% | 1.70x | 3643 | STRONG 71/100 | HIGH 66/100 | Watch |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
