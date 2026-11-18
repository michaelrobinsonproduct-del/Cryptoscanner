# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:05:16.223953+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44354529838
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** a50636969dd2acb167db3b49bd7d6b99bd8bd773 (atomic ledger/results publication)
**Ledger generation:** 619 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUST/USD | 0.04936 | 71.434 | 54.910 | +4.69% | +0.30% | 2.92x | 20.4 | 2026-11-18T17:05:12.094346+00:00 | Not calibrated | STRONG 81/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019726 | 69.075 | 67.648 | +5.66% | +0.97% | 0.66x | 6.1 | 2026-11-18T17:05:12.094346+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.05323 | 44.813 | 42.352 | +3.08% | +0.57% | 0.96x | 20.7 | 2026-11-18T17:05:12.094346+00:00 | Not calibrated | WEAK 42/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | CC/USD | 0.08264 | 42.621 | 36.223 | +0.62% | +0.98% | 1.15x | 7.3 | 2026-11-18T17:05:12.094346+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ZAMA/USD | 0.06037 | 27.977 | 31.710 | +0.73% | +0.48% | 0.39x | 9.9 | 2026-11-18T17:05:12.094346+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 67.648 | 0.019726 | +0.97% | 0.66x |
| 2 | TRUST/USD | 54.910 | 0.04936 | +0.30% | 2.92x |
| 3 | MEGA/USD | 42.352 | 0.05323 | +0.57% | 0.96x |
| 4 | CC/USD | 36.223 | 0.08264 | +0.98% | 1.15x |
| 5 | ZAMA/USD | 31.710 | 0.06037 | +0.48% | 0.39x |

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

- Persisted scans: 619; predictions: 5286; observations: 373978.
- Matured sampled outcomes across 1/6/24/48h: 4556; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44354529838 · **Generation:** 619 · **Legacy run:** 44354529838
**Main quote time:** 2026-11-18T17:05:16.223953+00:00 · **Legacy report time:** 2026-11-18T17:05:45.374956+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD ⭐ | 0.04936 | 71.43 | +0.30% | 2.92x | STRONG 91/100 | VERY_HIGH 72/100 | Watch |
| 2 | SENT/USD | 0.019726 | 69.08 | +0.97% | 0.66x | MODERATE 65/100 | VERY_HIGH 82/100 | Watch |
| 3 | MEGA/USD | 0.05323 | 44.81 | +0.57% | 0.96x | WEAK 42/100 | EXTREME 86/100 | Do nothing |
| 4 | CC/USD ⭐ | 0.08264 | 42.62 | +0.98% | 1.15x | MODERATE 66/100 | HIGH 67/100 | Watch |
| 5 | ZAMA/USD | 0.06037 | 27.98 | +0.48% | 0.39x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD ⭐ | 0.04936 | 79.98 | +0.30% | 2.92x | 3288 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | CC/USD ⭐ | 0.08268 | 37.35 | +0.98% | 1.15x | 4904 | MODERATE 64/100 | HIGH 67/100 | Watch |

**Same-run overlap:** TRUST/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
