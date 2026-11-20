# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T03:30:34.833094+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44668078314
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 6432c82b73b0132035587284bced96778807c662 (atomic ledger/results publication)
**Ledger generation:** 915 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SHX/USD | 0.003596 | 47.658 | 31.404 | +0.28% | +0.25% | 2.92x | 2.8 | 2026-11-20T03:30:31.213046+00:00 | Not calibrated | STRONG 79/100 | HIGH 67/100 | Watch | WATCH |
| 2 | ICNT/USD | 0.4309 | 47.061 | 35.179 | +1.13% | +1.25% | 1.57x | 20.9 | 2026-11-20T03:30:31.213046+00:00 | Not calibrated | MODERATE 59/100 | HIGH 67/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04511 | 42.154 | 39.745 | +0.78% | -0.15% | 1.32x | 13.3 | 2026-11-20T03:30:31.213046+00:00 | Not calibrated | WEAK 36/100 | HIGH 67/100 | Watch | WATCH |
| 4 | SKR/USD | 0.010084 | 30.516 | 27.877 | +0.38% | +0.67% | 0.93x | 11.9 | 2026-11-20T03:30:31.213046+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 5 | SAPIEN/USD | 0.04117 | 20.666 | 31.418 | +2.51% | -0.99% | 0.42x | 33.9 | 2026-11-20T03:30:31.213046+00:00 | Not calibrated | WEAK 5/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 39.745 | 0.04511 | -0.15% | 1.32x |
| 2 | ICNT/USD | 35.179 | 0.4309 | +1.25% | 1.57x |
| 3 | SAPIEN/USD | 31.418 | 0.04117 | -0.99% | 0.42x |
| 4 | SHX/USD | 31.404 | 0.003596 | +0.25% | 2.92x |
| 5 | SKR/USD | 27.877 | 0.010084 | +0.67% | 0.93x |

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

- Persisted scans: 915; predictions: 7907; observations: 552870.
- Matured sampled outcomes across 1/6/24/48h: 9034; gap abstentions: 16548. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44668078314 · **Generation:** 915 · **Legacy run:** 44668078314
**Main quote time:** 2026-11-20T03:30:34.833094+00:00 · **Legacy report time:** 2026-11-20T03:31:22.619667+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SHX/USD ⭐ | 0.003596 | 47.66 | +0.25% | 2.92x | STRONG 89/100 | HIGH 67/100 | Consider small entry |
| 2 | ICNT/USD ⭐ | 0.4309 | 47.06 | +1.25% | 1.57x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 3 | NIGHT/USD | 0.04511 | 42.15 | -0.15% | 1.32x | WEAK 36/100 | HIGH 67/100 | Watch |
| 4 | SKR/USD | 0.010084 | 30.52 | +0.67% | 0.93x | WEAK 40/100 | VERY_HIGH 80/100 | Watch |
| 5 | SAPIEN/USD | 0.04117 | 20.67 | -0.99% | 0.42x | WEAK 5/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XBT/USD | 62052.8 | 59.06 | +0.21% | 1.94x | 144799 | STRONG 75/100 | HIGH 55/100 | Watch |
| 2 | ICNT/USD ⭐ | 0.4344 | 56.05 | +1.25% | 1.57x | 7540 | STRONG 73/100 | HIGH 67/100 | Watch |
| 3 | SHX/USD ⭐ | 0.003596 | 37.82 | +0.25% | 2.92x | 1931 | STRONG 84/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SHX/USD, ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
