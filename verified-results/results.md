# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T02:35:01.825944+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44224272371
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** cce7158d04d337a368ab7bd203f83ea2fa1cd4b6 (atomic ledger/results publication)
**Ledger generation:** 508 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UP/USD | 0.05536 | 60.346 | 61.063 | +4.47% | -0.60% | 1.23x | 3.6 | 2026-11-18T02:34:59.133177+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5243 | 48.671 | 47.286 | +2.95% | +0.77% | 0.75x | 11.5 | 2026-11-18T02:34:59.133177+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | ICNT/USD | 0.2772 | 34.560 | 25.971 | +0.40% | +1.17% | 1.27x | 18.1 | 2026-11-18T02:34:59.133177+00:00 | Not calibrated | MODERATE 47/100 | HIGH 66/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.8171 | 34.101 | 28.308 | +0.36% | -1.84% | 12.97x | 19.3 | 2026-11-18T02:34:59.133177+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | TON/USD | 1.085 | 26.000 | 34.955 | +0.74% | +0.00% | 0.10x | 18.5 | 2026-11-18T02:34:59.133177+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 61.063 | 0.05536 | -0.60% | 1.23x |
| 2 | AKT/USD | 47.286 | 0.5243 | +0.77% | 0.75x |
| 3 | TON/USD | 34.955 | 1.085 | +0.00% | 0.10x |
| 4 | PEARL/USD | 28.308 | 1.8171 | -1.84% | 12.97x |
| 5 | ICNT/USD | 25.971 | 0.2772 | +1.17% | 1.27x |

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

- Persisted scans: 508; predictions: 4321; observations: 306379.
- Matured sampled outcomes across 1/6/24/48h: 3477; gap abstentions: 12412. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44224272371 · **Generation:** 508 · **Legacy run:** 44224272371
**Main quote time:** 2026-11-18T02:35:01.825944+00:00 · **Legacy report time:** 2026-11-18T02:35:14.563885+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UP/USD | 0.05536 | 60.35 | -0.60% | 1.23x | WEAK 40/100 | VERY_HIGH 80/100 | Watch |
| 2 | AKT/USD | 0.5243 | 48.67 | +0.77% | 0.75x | MODERATE 49/100 | VERY_HIGH 73/100 | Watch |
| 3 | ICNT/USD ⭐ | 0.2772 | 34.56 | +1.17% | 1.27x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 4 | PEARL/USD | 1.8171 | 34.10 | -1.84% | 12.97x | WEAK 42/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | TON/USD | 1.085 | 26.00 | +0.00% | 0.10x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2764 | 29.24 | +1.17% | 1.27x | 3670 | MODERATE 55/100 | HIGH 66/100 | Watch |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
