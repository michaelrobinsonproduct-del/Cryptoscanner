# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T14:40:52.293861+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44755572556
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** c5f53074d77da88de61a7d220313b39dffe746c9 (atomic ledger/results publication)
**Ledger generation:** 992 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CARV/USD | 0.02549 | 64.271 | 66.025 | +8.98% | +0.20% | 0.73x | 19.6 | 2026-11-20T14:40:48.067066+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.02205 | 59.909 | 53.297 | +3.57% | +0.16% | 1.58x | 7.7 | 2026-11-20T14:40:48.067066+00:00 | Not calibrated | MODERATE 65/100 | HIGH 60/100 | Watch | WATCH |
| 3 | MON/USD | 0.01408 | 48.965 | 46.406 | +2.33% | +0.86% | 0.83x | 7.1 | 2026-11-20T14:40:48.067066+00:00 | Not calibrated | MODERATE 54/100 | HIGH 67/100 | Watch | WATCH |
| 4 | DOS/USD | 0.1938 | 48.255 | 59.676 | +5.61% | -0.51% | 0.11x | 20.7 | 2026-11-20T14:40:48.067066+00:00 | Not calibrated | WEAK 19/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | CAP/USD | 0.098105 | 36.194 | 40.891 | +1.54% | -0.08% | 0.57x | 6.1 | 2026-11-20T14:40:48.067066+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CARV/USD | 66.025 | 0.02549 | +0.20% | 0.73x |
| 2 | DOS/USD | 59.676 | 0.1938 | -0.51% | 0.11x |
| 3 | SENT/USD | 53.297 | 0.02205 | +0.16% | 1.58x |
| 4 | MON/USD | 46.406 | 0.01408 | +0.86% | 0.83x |
| 5 | CAP/USD | 40.891 | 0.098105 | -0.08% | 0.57x |

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

- Persisted scans: 992; predictions: 8262; observations: 599498.
- Matured sampled outcomes across 1/6/24/48h: 10174; gap abstentions: 17636. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44755572556 · **Generation:** 992 · **Legacy run:** 44755572556
**Main quote time:** 2026-11-20T14:40:52.293861+00:00 · **Legacy report time:** 2026-11-20T14:41:47.195551+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CARV/USD | 0.02549 | 64.27 | +0.20% | 0.73x | MODERATE 47/100 | EXTREME 88/100 | Do nothing |
| 2 | SENT/USD ⭐ | 0.02205 | 59.91 | +0.16% | 1.58x | STRONG 75/100 | HIGH 60/100 | Watch |
| 3 | MON/USD | 0.01408 | 48.97 | +0.86% | 0.83x | MODERATE 54/100 | HIGH 67/100 | Watch |
| 4 | DOS/USD | 0.1938 | 48.26 | -0.51% | 0.11x | WEAK 19/100 | EXTREME 100/100 | Do nothing |
| 5 | CAP/USD | 0.098105 | 36.19 | -0.08% | 0.57x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.02205 | 76.69 | +0.16% | 1.58x | 6809 | STRONG 83/100 | HIGH 60/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
