# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T01:24:58.112541+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44215582575
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** a31f1e18aa70f3aa88d00c0cf4a1b67ae13cef66 (atomic ledger/results publication)
**Ledger generation:** 494 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UP/USD | 0.05517 | 56.731 | 40.910 | +4.11% | +2.03% | 1.56x | 38.2 | 2026-11-18T01:24:55.386586+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | PROS/USD | 0.5301 | 49.316 | 39.247 | +2.55% | +0.53% | 1.74x | 18.9 | 2026-11-18T01:24:55.386586+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | CAP/USD | 0.101735 | 36.695 | 34.798 | +0.75% | -1.01% | 1.70x | 6.1 | 2026-11-18T01:24:55.386586+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | AKT/USD | 0.514 | 29.909 | 35.762 | +0.92% | +0.33% | 0.25x | 5.8 | 2026-11-18T01:24:55.386586+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 40.910 | 0.05517 | +2.03% | 1.56x |
| 2 | PROS/USD | 39.247 | 0.5301 | +0.53% | 1.74x |
| 3 | AKT/USD | 35.762 | 0.514 | +0.33% | 0.25x |
| 4 | CAP/USD | 34.798 | 0.101735 | -1.01% | 1.70x |

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

- Persisted scans: 494; predictions: 4261; observations: 297853.
- Matured sampled outcomes across 1/6/24/48h: 3387; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44215582575 · **Generation:** 494 · **Legacy run:** 44215582575
**Main quote time:** 2026-11-18T01:24:58.112541+00:00 · **Legacy report time:** 2026-11-18T01:25:07.246425+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UP/USD | 0.05517 | 56.73 | +2.03% | 1.56x | MODERATE 58/100 | VERY_HIGH 79/100 | Watch |
| 2 | PROS/USD | 0.5301 | 49.32 | +0.53% | 1.74x | MODERATE 65/100 | VERY_HIGH 73/100 | Watch |
| 3 | CAP/USD | 0.101735 | 36.70 | -1.01% | 1.70x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 4 | AKT/USD | 0.514 | 29.91 | +0.33% | 0.25x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |

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
