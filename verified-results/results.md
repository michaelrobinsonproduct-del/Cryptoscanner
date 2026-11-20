# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T15:01:09.711797+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44758769969
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** c468914c39889b1450b7e56787446c5354f20e65 (atomic ledger/results publication)
**Ledger generation:** 994 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01441 | 86.066 | 60.073 | +4.72% | +2.20% | 4.11x | 13.9 | 2026-11-20T15:01:05.207311+00:00 | Not calibrated | STRONG 93/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | MNT/USD | 0.3935 | 46.993 | 30.333 | +0.49% | +0.33% | 2.97x | 7.6 | 2026-11-20T15:01:05.207311+00:00 | Not calibrated | STRONG 78/100 | HIGH 67/100 | Watch | WATCH |
| 3 | SENT/USD | 0.021634 | 45.156 | 39.191 | +1.62% | -1.81% | 3.69x | 8.3 | 2026-11-20T15:01:05.207311+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 4 | CAP/USD | 0.098308 | 41.827 | 37.931 | +1.75% | +0.19% | 1.30x | 14.7 | 2026-11-20T15:01:05.207311+00:00 | Not calibrated | WEAK 41/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 60.073 | 0.01441 | +2.20% | 4.11x |
| 2 | SENT/USD | 39.191 | 0.021634 | -1.81% | 3.69x |
| 3 | CAP/USD | 37.931 | 0.098308 | +0.19% | 1.30x |
| 4 | MNT/USD | 30.333 | 0.3935 | +0.33% | 2.97x |

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

- Persisted scans: 994; predictions: 8270; observations: 600712.
- Matured sampled outcomes across 1/6/24/48h: 10234; gap abstentions: 17682. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44758769969 · **Generation:** 994 · **Legacy run:** 44758769969
**Main quote time:** 2026-11-20T15:01:09.711797+00:00 · **Legacy report time:** 2026-11-20T15:02:05.018340+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01441 | 86.07 | +2.20% | 4.11x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | MNT/USD | 0.3935 | 46.99 | +0.33% | 2.97x | STRONG 78/100 | HIGH 67/100 | Watch |
| 3 | SENT/USD | 0.021634 | 45.16 | -1.81% | 3.69x | MODERATE 53/100 | VERY_HIGH 70/100 | Do nothing |
| 4 | CAP/USD ⭐ | 0.098308 | 41.83 | +0.19% | 1.30x | MODERATE 51/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01434 | 86.97 | +2.20% | 4.11x | 3673 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | CAP/USD ⭐ | 0.098188 | 45.06 | +0.19% | 1.30x | 4500 | MODERATE 53/100 | HIGH 66/100 | Watch |

**Same-run overlap:** MON/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
