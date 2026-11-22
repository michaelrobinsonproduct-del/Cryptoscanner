# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T06:41:03.890740+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44994710392
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 3597fd6025d83747d7596834cf117daa05982175 (atomic ledger/results publication)
**Ledger generation:** 1246 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 786.98 | 57.633 | 61.845 | +1.13% | +0.81% | 0.17x | 2.2 | 2026-11-22T06:40:59.389326+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TRUMP/USD | 0.894 | 50.035 | 35.253 | +0.90% | +0.22% | 2.37x | 11.2 | 2026-11-22T06:40:59.389326+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 3 | SPX/USD | 0.2812 | 46.644 | 26.070 | +0.64% | +1.11% | 23.75x | 21.3 | 2026-11-22T06:40:59.389326+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.9719 | 41.744 | 35.683 | +1.21% | +0.67% | 1.27x | 30.0 | 2026-11-22T06:40:59.389326+00:00 | Not calibrated | MODERATE 46/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 61.845 | 786.98 | +0.81% | 0.17x |
| 2 | PEARL/USD | 35.683 | 1.9719 | +0.67% | 1.27x |
| 3 | TRUMP/USD | 35.253 | 0.894 | +0.22% | 2.37x |
| 4 | SPX/USD | 26.070 | 0.2812 | +1.11% | 23.75x |

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

- Persisted scans: 1246; predictions: 9943; observations: 753926.
- Matured sampled outcomes across 1/6/24/48h: 14249; gap abstentions: 22006. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 55 (sampled only; not a success-rate estimate).
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

**Writer:** 44994710392 · **Generation:** 1246 · **Legacy run:** 44994710392
**Main quote time:** 2026-11-22T06:41:03.890740+00:00 · **Legacy report time:** 2026-11-22T06:42:08.601338+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 786.98 | 57.63 | +0.81% | 0.17x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 2 | TRUMP/USD ⭐ | 0.894 | 50.03 | +0.22% | 2.37x | STRONG 85/100 | HIGH 66/100 | Consider small entry |
| 3 | SPX/USD | 0.2812 | 46.64 | +1.11% | 23.75x | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |
| 4 | PEARL/USD ⭐ | 1.9719 | 41.74 | +0.67% | 1.27x | MODERATE 56/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.9719 | 46.95 | +0.67% | 1.27x | 8603 | MODERATE 53/100 | HIGH 67/100 | Watch |
| 2 | TRUMP/USD ⭐ | 0.894 | 41.69 | +0.22% | 2.37x | 2942 | STRONG 81/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** TRUMP/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
