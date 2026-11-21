# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T11:10:44.103273+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44897754054
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** f651d77785607a8c544d99f1eadbeaf90bceed8b (atomic ledger/results publication)
**Ledger generation:** 1125 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.848 | 78.627 | 88.998 | +5.35% | -0.81% | 0.37x | 6.9 | 2026-11-21T11:10:37.289960+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XMR/USD | 469.82 | 68.689 | 66.704 | +2.97% | +0.49% | 0.95x | 18.1 | 2026-11-21T11:10:37.289960+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 3 | ETH/USD | 1640.93 | 60.824 | 64.220 | +1.33% | -0.13% | 0.72x | 0.2 | 2026-11-21T11:10:37.289960+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | TRX/USD | 0.303015 | 57.041 | 57.881 | +0.50% | -0.06% | 0.94x | 1.3 | 2026-11-21T11:10:37.289960+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.021006 | 51.185 | 41.174 | +2.00% | -0.19% | 2.10x | 7.6 | 2026-11-21T11:10:37.289960+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.07681 | 44.966 | 50.268 | +3.10% | -0.36% | 0.65x | 22.2 | 2026-11-21T11:10:37.289960+00:00 | Not calibrated | WEAK 17/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | SKY/USD | 0.04455 | 38.896 | 42.446 | +1.62% | -0.65% | 0.97x | 6.7 | 2026-11-21T11:10:37.289960+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 88.998 | 21.848 | -0.81% | 0.37x |
| 2 | XMR/USD | 66.704 | 469.82 | +0.49% | 0.95x |
| 3 | ETH/USD | 64.220 | 1640.93 | -0.13% | 0.72x |
| 4 | TRX/USD | 57.881 | 0.303015 | -0.06% | 0.94x |
| 5 | USELESS/USD | 50.268 | 0.07681 | -0.36% | 0.65x |
| 6 | SKY/USD | 42.446 | 0.04455 | -0.65% | 0.97x |
| 7 | SENT/USD | 41.174 | 0.021006 | -0.19% | 2.10x |

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

- Persisted scans: 1125; predictions: 8826; observations: 680359.
- Matured sampled outcomes across 1/6/24/48h: 11614; gap abstentions: 20333. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44897754054 · **Generation:** 1125 · **Legacy run:** 44897754054
**Main quote time:** 2026-11-21T11:10:44.103273+00:00 · **Legacy report time:** 2026-11-21T11:11:34.565466+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.848 | 78.63 | -0.81% | 0.37x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 2 | XMR/USD | 469.82 | 68.69 | +0.49% | 0.95x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 3 | ETH/USD | 1640.93 | 60.82 | -0.13% | 0.72x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 4 | TRX/USD | 0.303015 | 57.04 | -0.06% | 0.94x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 5 | SENT/USD | 0.021006 | 51.19 | -0.19% | 2.10x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 6 | USELESS/USD | 0.07681 | 44.97 | -0.36% | 0.65x | WEAK 17/100 | EXTREME 88/100 | Do nothing |
| 7 | SKY/USD | 0.04455 | 38.90 | -0.65% | 0.97x | WEAK 24/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
