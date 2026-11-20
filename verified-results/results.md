# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T13:10:47.062190+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44741847266
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 058daae726c3f614f078d718234e38d884f3e21e (atomic ledger/results publication)
**Ledger generation:** 983 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | REKT/USD | 7.84e-08 | 88.815 | 58.684 | +4.53% | +3.03% | 4.07x | 12.8 | 2026-11-20T13:10:43.336583+00:00 | Not calibrated | STRONG 94/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | GBP/USD | 1.3127 | 72.716 | 56.788 | +0.34% | +0.19% | 2.57x | 1.1 | 2026-11-20T13:10:43.336583+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ICNT/USD | 0.4387 | 41.368 | 48.156 | +2.96% | -0.79% | 0.72x | 20.6 | 2026-11-20T13:10:43.336583+00:00 | Not calibrated | WEAK 16/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.02169 | 34.640 | 41.621 | +1.88% | -1.35% | 0.98x | 7.8 | 2026-11-20T13:10:43.336583+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 77/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | REKT/USD | 58.684 | 7.84e-08 | +3.03% | 4.07x |
| 2 | GBP/USD | 56.788 | 1.3127 | +0.19% | 2.57x |
| 3 | ICNT/USD | 48.156 | 0.4387 | -0.79% | 0.72x |
| 4 | SENT/USD | 41.621 | 0.02169 | -1.35% | 0.98x |

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

- Persisted scans: 983; predictions: 8222; observations: 594035.
- Matured sampled outcomes across 1/6/24/48h: 9927; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44741847266 · **Generation:** 983 · **Legacy run:** 44741847266
**Main quote time:** 2026-11-20T13:10:47.062190+00:00 · **Legacy report time:** 2026-11-20T13:11:53.252475+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | REKT/USD ⭐ | 7.84e-08 | 88.82 | +3.03% | 4.07x | STRONG 100/100 | VERY_HIGH 76/100 | Watch |
| 2 | GBP/USD ⭐ | 1.3127 | 72.72 | +0.19% | 2.57x | STRONG 91/100 | HIGH 55/100 | Watch |
| 3 | ICNT/USD | 0.4387 | 41.37 | -0.79% | 0.72x | WEAK 16/100 | EXTREME 88/100 | Do nothing |
| 4 | SENT/USD | 0.02169 | 34.64 | -1.35% | 0.98x | WEAK 22/100 | VERY_HIGH 77/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | REKT/USD ⭐ | 7.85e-08 | 88.01 | +3.03% | 4.07x | 7000 | STRONG 99/100 | VERY_HIGH 82/100 | Watch |
| 2 | GBP/USD ⭐ | 1.31271 | 61.23 | +0.19% | 2.57x | 21822 | STRONG 86/100 | HIGH 55/100 | Watch |

**Same-run overlap:** REKT/USD, GBP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
