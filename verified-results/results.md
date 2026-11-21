# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T01:30:29.338571+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44850476903
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 2b6fcaf5358982906f7877d6ff62b1e550b207a5 (atomic ledger/results publication)
**Ledger generation:** 1055 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.105 | 83.095 | 63.565 | +1.76% | +0.91% | 9.34x | 7.6 | 2026-11-21T01:30:22.571563+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | BLESS/USD | 0.014057 | 37.278 | 34.423 | +2.07% | +1.38% | 0.60x | 31.3 | 2026-11-21T01:30:22.571563+00:00 | Not calibrated | WEAK 39/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | PIEVERSE/USD | 3.0506 | 36.706 | 36.971 | +1.73% | +0.01% | 0.97x | 20.0 | 2026-11-21T01:30:22.571563+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 4 | SKY/USD | 0.0441 | 33.304 | 34.261 | +0.59% | +0.48% | 0.67x | 11.3 | 2026-11-21T01:30:22.571563+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | CT/USD | 0.1223 | 29.116 | 30.692 | +0.99% | -0.49% | 1.09x | 16.4 | 2026-11-21T01:30:22.571563+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 6 | DCR/USD | 10.184 | 28.198 | 29.801 | +0.78% | +0.36% | 0.66x | 12.8 | 2026-11-21T01:30:22.571563+00:00 | Not calibrated | WEAK 39/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | TRAC/USD | 0.271 | 11.591 | 16.784 | +0.37% | +0.04% | 0.46x | 33.3 | 2026-11-21T01:30:22.571563+00:00 | Not calibrated | WEAK 16/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 63.565 | 21.105 | +0.91% | 9.34x |
| 2 | PIEVERSE/USD | 36.971 | 3.0506 | +0.01% | 0.97x |
| 3 | BLESS/USD | 34.423 | 0.014057 | +1.38% | 0.60x |
| 4 | SKY/USD | 34.261 | 0.0441 | +0.48% | 0.67x |
| 5 | CT/USD | 30.692 | 0.1223 | -0.49% | 1.09x |
| 6 | DCR/USD | 29.801 | 10.184 | +0.36% | 0.66x |
| 7 | TRAC/USD | 16.784 | 0.271 | +0.04% | 0.46x |

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

- Persisted scans: 1055; predictions: 8458; observations: 637800.
- Matured sampled outcomes across 1/6/24/48h: 10938; gap abstentions: 19197. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44850476903 · **Generation:** 1055 · **Legacy run:** 44850476903
**Main quote time:** 2026-11-21T01:30:29.338571+00:00 · **Legacy report time:** 2026-11-21T01:31:31.773806+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.105 | 83.10 | +0.91% | 9.34x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | BLESS/USD | 0.014057 | 37.28 | +1.38% | 0.60x | WEAK 39/100 | EXTREME 87/100 | Do nothing |
| 3 | PIEVERSE/USD | 3.0506 | 36.71 | +0.01% | 0.97x | WEAK 28/100 | VERY_HIGH 79/100 | Do nothing |
| 4 | SKY/USD | 0.0441 | 33.30 | +0.48% | 0.67x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |
| 5 | CT/USD | 0.1223 | 29.12 | -0.49% | 1.09x | WEAK 20/100 | VERY_HIGH 79/100 | Do nothing |
| 6 | DCR/USD | 10.184 | 28.20 | +0.36% | 0.66x | WEAK 39/100 | EXTREME 88/100 | Do nothing |
| 7 | TRAC/USD | 0.271 | 11.59 | +0.04% | 0.46x | WEAK 16/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.161 | 72.14 | +0.91% | 9.34x | 11643 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
