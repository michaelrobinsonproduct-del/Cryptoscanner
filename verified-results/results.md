# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T16:03:02.467243+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46162731565
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1ab5f0930410c77fc773cb80f4e1d368cd806612 (atomic ledger/results publication)
**Ledger generation:** 2175 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 426.22 | 84.707 | 81.108 | +4.65% | +0.27% | 1.23x | 12.9 | 2026-11-28T16:02:58.521355+00:00 | Not calibrated | STRONG 72/100 | HIGH 68/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05212 | 70.975 | 74.288 | +3.74% | -0.38% | 0.86x | 11.5 | 2026-11-28T16:02:58.521355+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.764e-05 | 52.460 | 57.324 | +4.50% | -0.50% | 0.76x | 10.5 | 2026-11-28T16:02:58.521355+00:00 | Not calibrated | WEAK 26/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.024035 | 41.121 | 38.266 | +1.35% | -0.24% | 1.40x | 5.4 | 2026-11-28T16:02:58.521355+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 81.108 | 426.22 | +0.27% | 1.23x |
| 2 | NIGHT/USD | 74.288 | 0.05212 | -0.38% | 0.86x |
| 3 | LUNA/USD | 57.324 | 4.764e-05 | -0.50% | 0.76x |
| 4 | SENT/USD | 38.266 | 0.024035 | -0.24% | 1.40x |

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

- Persisted scans: 2175; predictions: 19303; observations: 1317096.
- Matured sampled outcomes across 1/6/24/48h: 46611; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46162731565 · **Generation:** 2175 · **Legacy run:** 46162731565
**Main quote time:** 2026-11-28T16:03:02.467243+00:00 · **Legacy report time:** 2026-11-28T16:04:00.737275+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 426.22 | 84.71 | +0.27% | 1.23x | STRONG 82/100 | HIGH 68/100 | Watch |
| 2 | NIGHT/USD | 0.05212 | 70.97 | -0.38% | 0.86x | WEAK 35/100 | VERY_HIGH 74/100 | Watch |
| 3 | LUNA/USD | 4.764e-05 | 52.46 | -0.50% | 0.76x | WEAK 26/100 | EXTREME 86/100 | Do nothing |
| 4 | SENT/USD | 0.024035 | 41.12 | -0.24% | 1.40x | WEAK 41/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 425.66 | 88.53 | +0.27% | 1.23x | 15703 | STRONG 89/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
