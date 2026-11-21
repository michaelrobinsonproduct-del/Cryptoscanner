# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T05:10:29.925227+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44869538090
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** b384419be958e8ff7ab26c51afffbcc1fb30c2f6 (atomic ledger/results publication)
**Ledger generation:** 1087 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 6.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | RARE/USD | 0.01385 | 77.088 | 46.055 | +4.14% | +3.21% | 2.89x | 29.0 | 2026-11-21T05:10:28.169040+00:00 | Not calibrated | STRONG 84/100 | EXTREME 89/100 | Do nothing | WATCH |
| 2 | DRV/USD | 0.25556 | 58.492 | 58.098 | +4.08% | -0.16% | 1.12x | 15.7 | 2026-11-21T05:10:28.169040+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 3 | CAP/USD | 0.094194 | 51.071 | 50.909 | +2.90% | -2.27% | 2.15x | 6.0 | 2026-11-21T05:10:28.169040+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 58.098 | 0.25556 | -0.16% | 1.12x |
| 2 | CAP/USD | 50.909 | 0.094194 | -2.27% | 2.15x |
| 3 | RARE/USD | 46.055 | 0.01385 | +3.21% | 2.89x |

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

- Persisted scans: 1087; predictions: 8610; observations: 657256.
- Matured sampled outcomes across 1/6/24/48h: 11170; gap abstentions: 19846. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44869538090 · **Generation:** 1087 · **Legacy run:** 44869538090
**Main quote time:** 2026-11-21T05:10:29.925227+00:00 · **Legacy report time:** 2026-11-21T05:11:17.694997+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | RARE/USD ⭐ | 0.01385 | 77.09 | +3.21% | 2.89x | STRONG 94/100 | EXTREME 89/100 | Do nothing |
| 2 | DRV/USD | 0.25556 | 58.49 | -0.16% | 1.12x | WEAK 34/100 | VERY_HIGH 74/100 | Do nothing |
| 3 | CAP/USD | 0.094194 | 51.07 | -2.27% | 2.15x | MODERATE 56/100 | VERY_HIGH 70/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RARE/USD ⭐ | 0.01398 | 86.54 | +3.21% | 2.89x | 5763 | STRONG 93/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** RARE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
