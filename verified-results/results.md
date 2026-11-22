# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T04:50:58.787525+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44986734115
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** c587440948e38cdfc8402c17182a26e8fe85e46e (atomic ledger/results publication)
**Ledger generation:** 1235 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 2.0182 | 56.552 | 55.356 | +3.59% | +0.95% | 0.65x | 25.3 | 2026-11-22T04:50:55.539275+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.0446 | 40.220 | 47.540 | +0.72% | -0.58% | 0.56x | 11.2 | 2026-11-22T04:50:55.539275+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | TRUMP/USD | 0.889 | 34.574 | 25.821 | +0.34% | -0.78% | 2.27x | 22.5 | 2026-11-22T04:50:55.539275+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 4 | RENDER/USD | 1.312 | 26.386 | 33.956 | +0.61% | +0.08% | 0.20x | 15.2 | 2026-11-22T04:50:55.539275+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 55.356 | 2.0182 | +0.95% | 0.65x |
| 2 | NIGHT/USD | 47.540 | 0.0446 | -0.58% | 0.56x |
| 3 | RENDER/USD | 33.956 | 1.312 | +0.08% | 0.20x |
| 4 | TRUMP/USD | 25.821 | 0.889 | -0.78% | 2.27x |

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

- Persisted scans: 1235; predictions: 9913; observations: 747238.
- Matured sampled outcomes across 1/6/24/48h: 14029; gap abstentions: 21974. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 37 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44986734115 · **Generation:** 1235 · **Legacy run:** 44986734115
**Main quote time:** 2026-11-22T04:50:58.787525+00:00 · **Legacy report time:** 2026-11-22T04:52:01.538871+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.0182 | 56.55 | +0.95% | 0.65x | MODERATE 48/100 | VERY_HIGH 82/100 | Watch |
| 2 | NIGHT/USD | 0.0446 | 40.22 | -0.58% | 0.56x | WEAK 20/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | TRUMP/USD | 0.889 | 34.57 | -0.78% | 2.27x | WEAK 37/100 | VERY_HIGH 78/100 | Watch |
| 4 | RENDER/USD | 1.312 | 26.39 | +0.08% | 0.20x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |

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
