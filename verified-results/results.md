# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T04:40:54.436477+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44986018164
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 9ccf51cf352847f380704850a8740a5578bc6221 (atomic ledger/results publication)
**Ledger generation:** 1234 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | RENDER/USD | 1.312 | 54.005 | 34.002 | +0.61% | +1.00% | 4.58x | 15.3 | 2026-11-22T04:40:50.496785+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PEARL/USD | 2.018 | 53.406 | 53.391 | +3.58% | +0.49% | 0.76x | 29.4 | 2026-11-22T04:40:50.496785+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.0445 | 40.786 | 48.230 | +0.50% | +0.13% | 0.19x | 6.7 | 2026-11-22T04:40:50.496785+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | TRUMP/USD | 0.894 | 39.353 | 35.243 | +0.90% | +0.79% | 1.02x | 11.2 | 2026-11-22T04:40:50.496785+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | SPX/USD | 0.2806 | 27.226 | 24.863 | +0.43% | -0.07% | 1.27x | 21.4 | 2026-11-22T04:40:50.496785+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 78/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 53.391 | 2.018 | +0.49% | 0.76x |
| 2 | NIGHT/USD | 48.230 | 0.0445 | +0.13% | 0.19x |
| 3 | TRUMP/USD | 35.243 | 0.894 | +0.79% | 1.02x |
| 4 | RENDER/USD | 34.002 | 1.312 | +1.00% | 4.58x |
| 5 | SPX/USD | 24.863 | 0.2806 | -0.07% | 1.27x |

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

- Persisted scans: 1234; predictions: 9909; observations: 746630.
- Matured sampled outcomes across 1/6/24/48h: 14008; gap abstentions: 21972. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 35 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44986018164 · **Generation:** 1234 · **Legacy run:** 44986018164
**Main quote time:** 2026-11-22T04:40:54.436477+00:00 · **Legacy report time:** 2026-11-22T04:41:44.720008+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | RENDER/USD ⭐ | 1.312 | 54.01 | +1.00% | 4.58x | STRONG 87/100 | HIGH 61/100 | Consider small entry |
| 2 | PEARL/USD | 2.018 | 53.41 | +0.49% | 0.76x | MODERATE 47/100 | VERY_HIGH 74/100 | Watch |
| 3 | NIGHT/USD | 0.0445 | 40.79 | +0.13% | 0.19x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 4 | TRUMP/USD ⭐ | 0.894 | 39.35 | +0.79% | 1.02x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 5 | SPX/USD | 0.2806 | 27.23 | -0.07% | 1.27x | WEAK 14/100 | VERY_HIGH 78/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RENDER/USD ⭐ | 1.312 | 44.77 | +1.00% | 4.58x | 4069 | STRONG 82/100 | HIGH 61/100 | Consider small entry |
| 2 | TRUMP/USD ⭐ | 0.893 | 36.62 | +0.79% | 1.02x | 2936 | MODERATE 58/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** RENDER/USD, TRUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
