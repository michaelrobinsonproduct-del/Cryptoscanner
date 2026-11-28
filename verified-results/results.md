# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T12:53:00.575950+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46146562968
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bb6b565f1a1998884893e012827ff66a21363b28 (atomic ledger/results publication)
**Ledger generation:** 2156 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05462 | 96.411 | 97.516 | +8.72% | -0.39% | 1.08x | 3.7 | 2026-11-28T12:52:57.275276+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 2 | XMR/USD | 438.66 | 84.538 | 93.488 | +7.71% | -0.94% | 0.57x | 13.0 | 2026-11-28T12:52:57.275276+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | VVV/USD | 26.681 | 72.202 | 65.529 | +3.62% | -1.67% | 3.39x | 7.5 | 2026-11-28T12:52:57.275276+00:00 | Not calibrated | MODERATE 66/100 | HIGH 65/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.024469 | 46.538 | 51.905 | +3.18% | +0.28% | 0.33x | 3.7 | 2026-11-28T12:52:57.275276+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 97.516 | 0.05462 | -0.39% | 1.08x |
| 2 | XMR/USD | 93.488 | 438.66 | -0.94% | 0.57x |
| 3 | VVV/USD | 65.529 | 26.681 | -1.67% | 3.39x |
| 4 | SENT/USD | 51.905 | 0.024469 | +0.28% | 0.33x |

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

- Persisted scans: 2156; predictions: 19211; observations: 1305582.
- Matured sampled outcomes across 1/6/24/48h: 45932; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46146562968 · **Generation:** 2156 · **Legacy run:** 46146562968
**Main quote time:** 2026-11-28T12:53:00.575950+00:00 · **Legacy report time:** 2026-11-28T12:53:48.556753+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05462 | 96.41 | -0.39% | 1.08x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 2 | XMR/USD | 438.66 | 84.54 | -0.94% | 0.57x | WEAK 42/100 | VERY_HIGH 82/100 | Watch |
| 3 | VVV/USD | 26.681 | 72.20 | -1.67% | 3.39x | MODERATE 66/100 | HIGH 65/100 | Do nothing |
| 4 | SENT/USD | 0.024469 | 46.54 | +0.28% | 0.33x | MODERATE 53/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKE/USD | 0.00113003 | 83.44 | +1.97% | 1.98x | 8035 | STRONG 72/100 | VERY_HIGH 82/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
