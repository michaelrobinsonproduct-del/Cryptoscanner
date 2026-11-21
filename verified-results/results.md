# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T05:00:38.404902+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44868713807
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** f8b288953e556e2f63985f5a0dbd2e53a246bf79 (atomic ledger/results publication)
**Ledger generation:** 1086 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 7.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CAP/USD | 0.095209 | 62.196 | 54.166 | +4.01% | -1.39% | 5.93x | 15.1 | 2026-11-21T05:00:35.904186+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 2 | RARE/USD | 0.01374 | 59.251 | 43.746 | +3.31% | +1.27% | 1.92x | 22.0 | 2026-11-21T05:00:35.904186+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | BLESS/USD | 0.014368 | 58.699 | 44.635 | +4.33% | +3.35% | 0.73x | 43.2 | 2026-11-21T05:00:35.904186+00:00 | Not calibrated | WEAK 44/100 | EXTREME 100/100 | Do nothing | WATCH |
| 4 | DRV/USD | 0.25553 | 56.684 | 61.155 | +4.07% | +0.33% | 0.39x | 9.4 | 2026-11-21T05:00:35.904186+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 61.155 | 0.25553 | +0.33% | 0.39x |
| 2 | CAP/USD | 54.166 | 0.095209 | -1.39% | 5.93x |
| 3 | BLESS/USD | 44.635 | 0.014368 | +3.35% | 0.73x |
| 4 | RARE/USD | 43.746 | 0.01374 | +1.27% | 1.92x |

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

- Persisted scans: 1086; predictions: 8607; observations: 656648.
- Matured sampled outcomes across 1/6/24/48h: 11168; gap abstentions: 19821. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44868713807 · **Generation:** 1086 · **Legacy run:** 44868713807
**Main quote time:** 2026-11-21T05:00:38.404902+00:00 · **Legacy report time:** 2026-11-21T05:01:22.133616+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.095209 | 62.20 | -1.39% | 5.93x | MODERATE 56/100 | VERY_HIGH 76/100 | Do nothing |
| 2 | RARE/USD ⭐ | 0.01374 | 59.25 | +1.27% | 1.92x | STRONG 75/100 | VERY_HIGH 79/100 | Watch |
| 3 | BLESS/USD | 0.014368 | 58.70 | +3.35% | 0.73x | WEAK 44/100 | EXTREME 100/100 | Do nothing |
| 4 | DRV/USD | 0.25553 | 56.68 | +0.33% | 0.39x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RARE/USD ⭐ | 0.01378 | 73.72 | +1.27% | 1.92x | 5613 | STRONG 87/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** RARE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
