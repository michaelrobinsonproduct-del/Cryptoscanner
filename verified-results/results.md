# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T08:37:39.887950+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46126461623
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e18ac851a831c7ec9a5632758dedc07705a8dac5 (atomic ledger/results publication)
**Ledger generation:** 2130 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 425.99 | 102.348 | 78.259 | +4.60% | +1.82% | 4.42x | 17.8 | 2026-11-28T08:37:36.682097+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 26.606 | 79.690 | 64.145 | +3.33% | +0.11% | 3.51x | 7.5 | 2026-11-28T08:37:36.682097+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SPACE/USD | 0.004391 | 53.439 | 61.878 | +5.10% | -0.09% | 0.20x | 9.1 | 2026-11-28T08:37:36.682097+00:00 | Not calibrated | WEAK 32/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.05058 | 47.147 | 54.793 | +0.68% | +0.20% | 0.14x | 9.9 | 2026-11-28T08:37:36.682097+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 78.259 | 425.99 | +1.82% | 4.42x |
| 2 | VVV/USD | 64.145 | 26.606 | +0.11% | 3.51x |
| 3 | SPACE/USD | 61.878 | 0.004391 | -0.09% | 0.20x |
| 4 | NIGHT/USD | 54.793 | 0.05058 | +0.20% | 0.14x |

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

- Persisted scans: 2130; predictions: 19061; observations: 1289826.
- Matured sampled outcomes across 1/6/24/48h: 44928; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46126461623 · **Generation:** 2130 · **Legacy run:** 46126461623
**Main quote time:** 2026-11-28T08:37:39.887950+00:00 · **Legacy report time:** 2026-11-28T08:38:17.103311+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 425.99 | 102.35 | +1.82% | 4.42x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 26.606 | 79.69 | +0.11% | 3.51x | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | SPACE/USD | 0.004391 | 53.44 | -0.09% | 0.20x | WEAK 32/100 | EXTREME 88/100 | Do nothing |
| 4 | NIGHT/USD | 0.05058 | 47.15 | +0.20% | 0.14x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 428.05 | 98.45 | +1.82% | 4.42x | 15121 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 26.621 | 79.74 | +0.11% | 3.51x | 7580 | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | AKE/USD | 0.00111478 | 72.93 | +3.94% | 4.10x | 8283 | STRONG 81/100 | VERY_HIGH 82/100 | Watch |

**Same-run overlap:** XMR/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
