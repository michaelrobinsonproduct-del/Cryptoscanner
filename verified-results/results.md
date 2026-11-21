# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T02:45:51.754256+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44857520339
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** aef73e95729991f5a5f5fdbc431d8bcc8f05b357 (atomic ledger/results publication)
**Ledger generation:** 1066 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.26909 | 93.875 | 65.232 | +9.59% | +2.73% | 9.09x | 33.1 | 2026-11-21T02:45:45.606906+00:00 | Not calibrated | STRONG 92/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 20.913 | 65.141 | 56.571 | +0.84% | -0.94% | 2.33x | 8.6 | 2026-11-21T02:45:45.606906+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 3 | CAP/USD | 0.094408 | 41.500 | 48.340 | +3.13% | -0.15% | 0.39x | 13.9 | 2026-11-21T02:45:45.606906+00:00 | Not calibrated | WEAK 21/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | STBL/USD | 0.016061 | 26.710 | 33.547 | +1.17% | -1.15% | 0.89x | 11.2 | 2026-11-21T02:45:45.606906+00:00 | Not calibrated | WEAK 13/100 | EXTREME 90/100 | Do nothing | WATCH |
| 5 | DCR/USD | 10.195 | 21.610 | 31.096 | +0.89% | -0.23% | 0.16x | 11.8 | 2026-11-21T02:45:45.606906+00:00 | Not calibrated | WEAK 11/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 65.232 | 0.26909 | +2.73% | 9.09x |
| 2 | VVV/USD | 56.571 | 20.913 | -0.94% | 2.33x |
| 3 | CAP/USD | 48.340 | 0.094408 | -0.15% | 0.39x |
| 4 | STBL/USD | 33.547 | 0.016061 | -1.15% | 0.89x |
| 5 | DCR/USD | 31.096 | 10.195 | -0.23% | 0.16x |

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

- Persisted scans: 1066; predictions: 8554; observations: 644488.
- Matured sampled outcomes across 1/6/24/48h: 11019; gap abstentions: 19449. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44857520339 · **Generation:** 1066 · **Legacy run:** 44857520339
**Main quote time:** 2026-11-21T02:45:51.754256+00:00 · **Legacy report time:** 2026-11-21T02:46:38.589770+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.26909 | 93.88 | +2.73% | 9.09x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD | 20.913 | 65.14 | -0.94% | 2.33x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 3 | CAP/USD | 0.094408 | 41.50 | -0.15% | 0.39x | WEAK 21/100 | EXTREME 87/100 | Do nothing |
| 4 | STBL/USD | 0.016061 | 26.71 | -1.15% | 0.89x | WEAK 13/100 | EXTREME 90/100 | Do nothing |
| 5 | DCR/USD | 10.195 | 21.61 | -0.23% | 0.16x | WEAK 11/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.27095 | 90.12 | +2.73% | 9.09x | 6948 | STRONG 100/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
