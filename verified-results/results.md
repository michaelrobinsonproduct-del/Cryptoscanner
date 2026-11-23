# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T01:21:19.260015+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45093928463
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 1a3125d4e39b8d786a7e991341d92b7e201344b1 (atomic ledger/results publication)
**Ledger generation:** 1361 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PAXG/USD | 3606.18 | 69.012 | 49.277 | +0.95% | +0.95% | 8.27x | 3.3 | 2026-11-23T01:21:14.565770+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XAUT/USD | 3606.7 | 57.305 | 37.674 | +0.97% | +0.93% | 3.52x | 3.9 | 2026-11-23T01:21:14.565770+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 3 | DRV/USD | 0.38581 | 52.319 | 67.597 | +4.60% | -1.81% | 0.38x | 19.5 | 2026-11-23T01:21:14.565770+00:00 | Not calibrated | WEAK 26/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | PEARL/USD | 2.112 | 48.951 | 48.248 | +2.80% | -0.28% | 1.21x | 25.6 | 2026-11-23T01:21:14.565770+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 5 | AI/USD | 0.01489 | 44.561 | 33.889 | +1.85% | -0.87% | 2.84x | 20.1 | 2026-11-23T01:21:14.565770+00:00 | Not calibrated | WEAK 42/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | AUD/USD | 0.66469 | 44.321 | 38.469 | +0.47% | +0.16% | 1.50x | 8.6 | 2026-11-23T01:21:14.565770+00:00 | Not calibrated | MODERATE 57/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 67.597 | 0.38581 | -1.81% | 0.38x |
| 2 | PAXG/USD | 49.277 | 3606.18 | +0.95% | 8.27x |
| 3 | PEARL/USD | 48.248 | 2.112 | -0.28% | 1.21x |
| 4 | AUD/USD | 38.469 | 0.66469 | +0.16% | 1.50x |
| 5 | XAUT/USD | 37.674 | 3606.7 | +0.93% | 3.52x |
| 6 | AI/USD | 33.889 | 0.01489 | -0.87% | 2.84x |

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

- Persisted scans: 1361; predictions: 11172; observations: 823955.
- Matured sampled outcomes across 1/6/24/48h: 17654; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 71 (sampled only; not a success-rate estimate).
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

**Writer:** 45093928463 · **Generation:** 1361 · **Legacy run:** 45093928463
**Main quote time:** 2026-11-23T01:21:19.260015+00:00 · **Legacy report time:** 2026-11-23T01:22:08.371061+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3606.18 | 69.01 | +0.95% | 8.27x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XAUT/USD ⭐ | 3606.7 | 57.30 | +0.93% | 3.52x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 3 | DRV/USD | 0.38581 | 52.32 | -1.81% | 0.38x | WEAK 26/100 | EXTREME 86/100 | Do nothing |
| 4 | PEARL/USD | 2.112 | 48.95 | -0.28% | 1.21x | WEAK 24/100 | VERY_HIGH 80/100 | Do nothing |
| 5 | AI/USD | 0.01489 | 44.56 | -0.87% | 2.84x | WEAK 42/100 | EXTREME 85/100 | Do nothing |
| 6 | AUD/USD ⭐ | 0.66469 | 44.32 | +0.16% | 1.50x | MODERATE 67/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3602.55 | 66.10 | +0.95% | 8.27x | 7065 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 2 | XAUT/USD ⭐ | 3606.7 | 51.22 | +0.93% | 3.52x | 1654 | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 3 | AUD/USD ⭐ | 0.66469 | 35.84 | +0.16% | 1.50x | 3311 | MODERATE 58/100 | HIGH 61/100 | Watch |

**Same-run overlap:** PAXG/USD, XAUT/USD, AUD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
